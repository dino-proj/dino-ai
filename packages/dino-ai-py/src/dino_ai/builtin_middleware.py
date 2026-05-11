"""Built-in middleware implementations.

All middleware follows the Middleware protocol: ``intercept(model, context, options, chain) -> EventStream``.
"""

from __future__ import annotations

import asyncio
import logging
import random
import time
from typing import Any

from dino_ai.context import AssistantMessage, Context
from dino_ai.error import DinoError, ErrorCategory
from dino_ai.events import AssistantMessageEvent, StreamDone, StreamError
from dino_ai.middleware import MiddlewareChain
from dino_ai.model import Model
from dino_ai.options import StreamOptions
from dino_ai.stream import EventStream

logger = logging.getLogger("dino_ai")


def _wrap_stream(
    inner: EventStream,
    on_event: Any | None = None,
    on_done: Any | None = None,
    on_error: Any | None = None,
) -> EventStream:
    """Create a proxy EventStream that intercepts events from an inner stream.

    Args:
        inner: The source event stream to wrap.
        on_event: Optional callback ``(event) -> None`` called for every event.
        on_done: Optional callback ``(StreamDone) -> None`` called on stream completion.
        on_error: Optional callback ``(StreamError) -> None`` called on stream error.

    Returns:
        A new EventStream that forwards all events from inner.
    """
    outer = EventStream()

    async def _pump() -> None:
        try:
            async for event in inner:
                if on_event:
                    on_event(event)
                if isinstance(event, StreamDone) and on_done:
                    on_done(event)
                elif isinstance(event, StreamError) and on_error:
                    on_error(event)
                outer.push(event)
        except Exception as exc:
            error = DinoError(
                category=ErrorCategory.UNKNOWN,
                provider="middleware",
                message=str(exc),
            )
            msg = AssistantMessage(stop_reason="error", error=error)
            outer.push(StreamError(reason="error", error=error, message=msg))
            outer.push(StreamDone(reason="error", message=msg))

    asyncio.get_event_loop().create_task(_pump())
    return outer


# ── LoggingMiddleware ────────────────────────────────────────────


class LoggingMiddleware:
    """Logs model, tokens, cost, and latency for each request.

    Uses the ``dino_ai`` logger at INFO level.

    Usage::

        import logging
        logging.basicConfig(level=logging.INFO)

        client = DinoClient(
            providers=[...],
            middleware=[LoggingMiddleware()],
        )
    """

    def __init__(self, log_level: int = logging.INFO) -> None:
        self._level = log_level

    def intercept(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None,
        chain: MiddlewareChain,
    ) -> EventStream:
        start_time = time.monotonic()

        def _log_done(event: StreamDone) -> None:
            elapsed = time.monotonic() - start_time
            msg = event.message
            usage = msg.usage
            parts = [
                f"model={msg.model}",
                f"stop={msg.stop_reason}",
                f"tokens={usage.total_tokens}",
                f"latency={elapsed:.2f}s",
            ]
            if usage.cost and usage.cost.total > 0:
                parts.append(f"cost=${usage.cost.total:.6f}")
            logger.log(self._level, "stream done: %s", ", ".join(parts))

        def _log_error(event: StreamError) -> None:
            elapsed = time.monotonic() - start_time
            logger.log(
                self._level,
                "stream error: model=%s, error=%s, latency=%.2fs",
                model.id,
                event.error.message,
                elapsed,
            )

        inner = chain(model, context, options)
        return _wrap_stream(inner, on_done=_log_done, on_error=_log_error)


# ── RetryMiddleware ──────────────────────────────────────────────


class RetryMiddleware:
    """Retries failed requests with exponential backoff and jitter.

    Only retries errors marked as ``retryable`` in the DinoError.
    Respects ``retry_after_ms`` from provider responses.

    Usage::

        client = DinoClient(
            providers=[...],
            middleware=[RetryMiddleware(max_retries=3)],
        )
    """

    def __init__(
        self,
        max_retries: int = 2,
        base_delay_ms: int = 1000,
        max_delay_ms: int = 30000,
    ) -> None:
        self._max_retries = max_retries
        self._base_delay_ms = base_delay_ms
        self._max_delay_ms = max_delay_ms

    def intercept(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None,
        chain: MiddlewareChain,
    ) -> EventStream:
        max_retries = self._max_retries
        if options and options.max_retries is not None:
            max_retries = options.max_retries

        outer = EventStream()

        async def _run() -> None:
            last_error: DinoError | None = None

            for attempt in range(max_retries + 1):
                inner = chain(model, context, options)
                events: list[AssistantMessageEvent] = []
                retryable_error: DinoError | None = None

                async for event in inner:
                    events.append(event)
                    if isinstance(event, StreamError) and event.error.retryable:
                        retryable_error = event.error

                # If retryable error and we have retries left, retry
                if retryable_error and attempt < max_retries:
                    last_error = retryable_error
                    delay_ms = self._compute_delay(attempt, retryable_error.retry_after_ms)
                    logger.debug(
                        "retrying (attempt %d/%d) after %dms: %s",
                        attempt + 1,
                        max_retries,
                        delay_ms,
                        retryable_error.message,
                    )
                    await asyncio.sleep(delay_ms / 1000.0)
                    continue

                # Success or non-retryable error or last attempt — forward all events
                for event in events:
                    outer.push(event)
                return

            # Should not reach here, but safety net
            error = last_error or DinoError(
                category=ErrorCategory.UNKNOWN,
                provider=model.provider,
                message="All retries exhausted",
            )
            msg = AssistantMessage(
                model=model.id,
                provider=model.provider,
                api=model.api,
                stop_reason="error",
                error=error,
            )
            outer.push(StreamError(reason="error", error=error, message=msg))
            outer.push(StreamDone(reason="error", message=msg))

        asyncio.get_event_loop().create_task(_run())
        return outer

    def _compute_delay(self, attempt: int, retry_after_ms: int | None) -> int:
        """Compute delay with exponential backoff + jitter, respecting retry-after."""
        if retry_after_ms and retry_after_ms > 0:
            return retry_after_ms

        base = self._base_delay_ms * (2**attempt)
        jitter = random.randint(0, base // 2)
        delay = base + jitter
        return delay if delay < self._max_delay_ms else self._max_delay_ms


# ── CostGuardMiddleware ──────────────────────────────────────────


class CostGuardMiddleware:
    """Rejects requests when cumulative session cost exceeds a threshold.

    Usage::

        guard = CostGuardMiddleware(max_total_cost=1.00)  # $1.00 budget
        client = DinoClient(
            providers=[...],
            middleware=[guard],
        )

        # Check remaining budget
        print(f"Spent: ${guard.total_cost:.4f}")
    """

    def __init__(self, max_total_cost: float) -> None:
        self._max_total_cost = max_total_cost
        self._total_cost = 0.0

    @property
    def total_cost(self) -> float:
        """Cumulative cost in USD across all requests."""
        return self._total_cost

    @property
    def remaining_budget(self) -> float:
        """Remaining budget in USD."""
        return max(0.0, self._max_total_cost - self._total_cost)

    def intercept(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None,
        chain: MiddlewareChain,
    ) -> EventStream:
        if self._total_cost >= self._max_total_cost:
            outer = EventStream()
            error = DinoError(
                category=ErrorCategory.QUOTA_EXCEEDED,
                provider="dino-ai",
                message=f"Cost guard: budget exhausted (${self._total_cost:.4f} >= ${self._max_total_cost:.4f})",
                retryable=False,
            )
            msg = AssistantMessage(
                model=model.id,
                provider=model.provider,
                api=model.api,
                stop_reason="error",
                error=error,
            )
            outer.push(StreamError(reason="error", error=error, message=msg))
            outer.push(StreamDone(reason="error", message=msg))
            return outer

        def _track_done(event: StreamDone) -> None:
            cost = event.message.usage.cost
            if cost:
                self._total_cost += cost.total

        def _track_error(event: StreamError) -> None:
            cost = event.message.usage.cost
            if cost:
                self._total_cost += cost.total

        inner = chain(model, context, options)
        return _wrap_stream(inner, on_done=_track_done, on_error=_track_error)
