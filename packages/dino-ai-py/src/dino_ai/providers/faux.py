"""Faux provider — deterministic responses for testing.

Provides a mock LLM provider that returns pre-configured responses,
emitting streaming events to exercise the full event pipeline.

Usage::

    from dino_ai.providers.faux import FauxProvider, faux_text, faux_model

    provider = FauxProvider(responses=["Hello, world!"])
    client = DinoClient(providers=[provider])

    # Responses are consumed in order
    msg = await client.complete(faux_model(), context)
    assert msg.content[0].text == "Hello, world!"
"""

from __future__ import annotations

import asyncio
import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from dino_ai.content import TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context
from dino_ai.error import DinoError, ErrorCategory
from dino_ai.events import (
    StreamDone,
    StreamError,
    StreamStart,
    TextDelta,
    TextEnd,
    TextStart,
    ThinkingDelta,
    ThinkingEnd,
    ThinkingStart,
    ToolCallDelta,
    ToolCallEnd,
    ToolCallStart,
)
from dino_ai.model import Model, ModelCapabilities, ModelLimits, ModelPricing
from dino_ai.options import SimpleStreamOptions, StreamOptions
from dino_ai.stream import EventStream
from dino_ai.usage import Cost, Usage

FAUX_API = "faux"
FAUX_PROVIDER = "faux"
FAUX_MODEL_ID = "faux-1"


def faux_model(
    model_id: str = FAUX_MODEL_ID,
    reasoning: bool = False,
    vision: bool = True,
    context_window: int = 128000,
) -> Model:
    """Create a faux Model for testing."""
    return Model(
        id=model_id,
        name="Faux Model",
        api=FAUX_API,
        provider=FAUX_PROVIDER,
        base_url="http://localhost:0",
        capabilities=ModelCapabilities(
            reasoning=reasoning,
            vision=vision,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(context_window=context_window, max_output_tokens=8192),
        pricing=ModelPricing(input=0, output=0, cache_read=0, cache_write=0),
    )


def faux_text(text: str) -> TextContent:
    """Create a TextContent block."""
    return TextContent(text=text)


def faux_thinking(thinking: str) -> ThinkingContent:
    """Create a ThinkingContent block."""
    return ThinkingContent(thinking=thinking)


def faux_tool_call(
    name: str,
    arguments: dict[str, Any],
    call_id: str | None = None,
) -> ToolCall:
    """Create a ToolCall block."""
    return ToolCall(
        id=call_id or f"tool:{int(time.time() * 1000)}",
        name=name,
        arguments=arguments,
    )


FauxContentBlock = TextContent | ThinkingContent | ToolCall

FauxResponseFactory = Callable[
    [Context, StreamOptions | None, int, Model],  # context, options, call_count, model
    AssistantMessage,
]

FauxResponseStep = AssistantMessage | FauxResponseFactory | str | FauxContentBlock | list[FauxContentBlock]


def _normalize_response(
    step: FauxResponseStep,
    call_count: int,
    context: Context,
    options: StreamOptions | None,
    model: Model,
) -> AssistantMessage:
    """Normalize a response step into an AssistantMessage."""
    if isinstance(step, AssistantMessage):
        return step
    if callable(step):
        return step(context, options, call_count, model)
    if isinstance(step, str):
        content: list[TextContent | ThinkingContent | ToolCall] = [faux_text(step)]
    elif isinstance(step, list):
        content = step
    elif isinstance(step, (TextContent, ThinkingContent, ToolCall)):
        content = [step]
    else:
        content = [faux_text(str(step))]

    return AssistantMessage(
        content=content,
        model=model.id,
        provider=FAUX_PROVIDER,
        api=FAUX_API,
        usage=Usage(),
        timestamp=int(time.time() * 1000),
    )


def _estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def _split_text(text: str, min_chunk: int = 3, max_chunk: int = 8) -> list[str]:
    """Split text into variable-size chunks to simulate streaming."""
    import random

    chunks: list[str] = []
    i = 0
    while i < len(text):
        size = random.randint(min_chunk, max_chunk)
        chunks.append(text[i : i + size])
        i += size
    return chunks if chunks else [""]


@dataclass
class _EmitState:
    content_index: int = 0


async def _emit_content_block(
    block: FauxContentBlock,
    stream: EventStream,
    partial: AssistantMessage,
    state: _EmitState,
    delay: float,
) -> None:
    idx = state.content_index
    if isinstance(block, TextContent):
        stream.push(TextStart(content_index=idx, partial=partial))
        for chunk in _split_text(block.text):
            if delay > 0:
                await asyncio.sleep(delay)
            stream.push(TextDelta(content_index=idx, delta=chunk, partial=partial))
        stream.push(TextEnd(content_index=idx, text=block.text, partial=partial))
    elif isinstance(block, ThinkingContent):
        stream.push(ThinkingStart(content_index=idx, partial=partial))
        for chunk in _split_text(block.thinking):
            if delay > 0:
                await asyncio.sleep(delay)
            stream.push(ThinkingDelta(content_index=idx, delta=chunk, partial=partial))
        stream.push(ThinkingEnd(content_index=idx, text=block.thinking, partial=partial))
    elif isinstance(block, ToolCall):
        stream.push(ToolCallStart(content_index=idx, partial=partial))
        import json

        args_str = json.dumps(block.arguments)
        for chunk in _split_text(args_str):
            if delay > 0:
                await asyncio.sleep(delay)
            stream.push(ToolCallDelta(content_index=idx, delta=chunk, partial=partial))
        stream.push(ToolCallEnd(content_index=idx, tool_call=block, partial=partial))
    state.content_index += 1


class FauxProvider:
    """Deterministic provider for testing. Returns pre-configured responses.

    Supports:
    - String responses (auto-wrapped in TextContent)
    - Pre-built AssistantMessage objects
    - Factory functions for dynamic responses
    - Error injection via DinoError on AssistantMessage
    - Streaming simulation with configurable delay
    """

    def __init__(
        self,
        responses: list[FauxResponseStep] | None = None,
        delay: float = 0.0,
    ) -> None:
        self._responses: list[FauxResponseStep] = list(responses or [])
        self._delay = delay
        self._call_count = 0

    @property
    def api(self) -> str:
        return FAUX_API

    @property
    def call_count(self) -> int:
        return self._call_count

    def set_responses(self, responses: list[FauxResponseStep]) -> None:
        """Replace all pending responses."""
        self._responses = list(responses)

    def append_responses(self, responses: list[FauxResponseStep]) -> None:
        """Add responses to the end of the queue."""
        self._responses.extend(responses)

    def stream(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None = None,
    ) -> EventStream:
        call_count = self._call_count
        self._call_count += 1

        if not self._responses:
            msg = AssistantMessage(
                content=[faux_text("(no response configured)")],
                model=model.id,
                provider=FAUX_PROVIDER,
                api=FAUX_API,
                usage=Usage(),
                stop_reason="error",
                error=DinoError(
                    category=ErrorCategory.PROVIDER_ERROR,
                    provider=FAUX_PROVIDER,
                    message="No responses configured in FauxProvider",
                ),
                timestamp=int(time.time() * 1000),
            )
            stream = EventStream.create()

            async def emit_error() -> None:
                stream.push(StreamStart(partial=msg))
                stream.push(StreamError(reason="error", error=msg.error, message=msg))  # type: ignore[arg-type]

            asyncio.ensure_future(emit_error())
            return stream

        step = self._responses.pop(0)
        response = _normalize_response(step, call_count, context, options, model)

        # Estimate usage
        total_text = ""
        for block in response.content:
            if isinstance(block, TextContent):
                total_text += block.text
            elif isinstance(block, ThinkingContent):
                total_text += block.thinking
            elif isinstance(block, ToolCall):
                import json

                total_text += json.dumps(block.arguments)

        output_tokens = _estimate_tokens(total_text)
        input_text = context.system_prompt or ""
        for m in context.messages:
            if hasattr(m, "content"):
                if isinstance(m.content, str):
                    input_text += m.content
                elif isinstance(m.content, list):
                    for b in m.content:
                        if isinstance(b, TextContent):
                            input_text += b.text
        input_tokens = _estimate_tokens(input_text)

        response.usage = Usage(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
            cost=Cost(),
        )

        stream = EventStream.create()
        delay = self._delay

        async def emit() -> None:
            partial = response
            stream.push(StreamStart(partial=partial))

            if response.error is not None:
                stream.push(StreamError(reason=response.stop_reason, error=response.error, message=partial))
                return

            state = _EmitState()
            for block in response.content:
                await _emit_content_block(block, stream, partial, state, delay)

            stop_reason = response.stop_reason
            # Auto-detect tool use
            if any(isinstance(b, ToolCall) for b in response.content):
                stop_reason = "toolUse"

            final = AssistantMessage(
                content=response.content,
                model=response.model,
                provider=response.provider,
                api=response.api,
                usage=response.usage,
                stop_reason=stop_reason,
                timestamp=response.timestamp,
                metadata=response.metadata,
            )
            stream.push(StreamDone(reason=stop_reason, message=final))

        asyncio.ensure_future(emit())
        return stream

    def stream_simple(
        self,
        model: Model,
        context: Context,
        options: SimpleStreamOptions | None = None,
    ) -> EventStream:
        return self.stream(model, context, options)
