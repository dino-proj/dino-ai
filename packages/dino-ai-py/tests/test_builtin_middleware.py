"""Tests for built-in middleware: Logging, Retry, CostGuard."""

from __future__ import annotations

import logging

import pytest

from dino_ai.builtin_middleware import CostGuardMiddleware, LoggingMiddleware, RetryMiddleware
from dino_ai.catalog import ModelCatalog
from dino_ai.client import DinoClient
from dino_ai.context import AssistantMessage, Context, UserMessage
from dino_ai.error import DinoError, ErrorCategory
from dino_ai.model import Model, ModelCapabilities, ModelLimits, ModelPricing
from dino_ai.options import StreamOptions
from dino_ai.providers.faux import FAUX_API, FAUX_PROVIDER, FauxProvider, faux_model, faux_text


def _catalog_with_faux() -> ModelCatalog:
    catalog = ModelCatalog()
    catalog.register(faux_model())
    return catalog


def _priced_model() -> Model:
    return Model(
        id="faux-priced",
        name="Faux Priced",
        api="faux",
        provider="faux",
        base_url="",
        capabilities=ModelCapabilities(),
        limits=ModelLimits(context_window=128000, max_output_tokens=8192),
        pricing=ModelPricing(input=3.0, output=15.0),
    )


def _catalog_with_priced() -> ModelCatalog:
    catalog = ModelCatalog()
    m = _priced_model()
    catalog.register(m)
    return catalog


def _error_msg(error: DinoError) -> AssistantMessage:
    """Wrap a DinoError in an AssistantMessage for FauxProvider."""
    return AssistantMessage(
        content=[faux_text("error")],
        model=FAUX_PROVIDER,
        provider=FAUX_PROVIDER,
        api=FAUX_API,
        stop_reason="error",
        error=error,
    )


# ── LoggingMiddleware Tests ──────────────────────────────────────


class TestLoggingMiddleware:
    @pytest.mark.asyncio
    async def test_logs_on_completion(self, caplog: pytest.LogCaptureFixture):
        provider = FauxProvider(responses=["Hello world"])
        mw = LoggingMiddleware()
        client = DinoClient(
            providers=[provider],
            middleware=[mw],
            catalog=_catalog_with_faux(),
        )

        with caplog.at_level(logging.INFO, logger="dino_ai"):
            ctx = Context(messages=[UserMessage(content="Hi")])
            msg = await client.complete("faux-1", ctx)

        assert msg.stop_reason == "stop"
        assert any("stream done" in r.message for r in caplog.records)
        log_text = " ".join(r.message for r in caplog.records)
        assert "model=" in log_text
        assert "latency=" in log_text

    @pytest.mark.asyncio
    async def test_logs_on_error(self, caplog: pytest.LogCaptureFixture):
        error = DinoError(
            category=ErrorCategory.AUTH_FAILURE,
            provider="faux",
            message="Invalid API key",
        )
        provider = FauxProvider(responses=[_error_msg(error)])
        mw = LoggingMiddleware()
        client = DinoClient(
            providers=[provider],
            middleware=[mw],
            catalog=_catalog_with_faux(),
        )

        with caplog.at_level(logging.INFO, logger="dino_ai"):
            ctx = Context(messages=[UserMessage(content="Hi")])
            msg = await client.complete("faux-1", ctx)

        assert msg.stop_reason == "error"
        assert any("stream error" in r.message for r in caplog.records)

    @pytest.mark.asyncio
    async def test_custom_log_level(self, caplog: pytest.LogCaptureFixture):
        provider = FauxProvider(responses=["ok"])
        mw = LoggingMiddleware(log_level=logging.DEBUG)
        client = DinoClient(
            providers=[provider],
            middleware=[mw],
            catalog=_catalog_with_faux(),
        )

        with caplog.at_level(logging.DEBUG, logger="dino_ai"):
            ctx = Context(messages=[UserMessage(content="Hi")])
            await client.complete("faux-1", ctx)

        assert any("stream done" in r.message for r in caplog.records)
        assert all(r.levelno == logging.DEBUG for r in caplog.records if "stream done" in r.message)


# ── RetryMiddleware Tests ────────────────────────────────────────


class TestRetryMiddleware:
    @pytest.mark.asyncio
    async def test_no_retry_on_success(self):
        provider = FauxProvider(responses=["ok"])
        mw = RetryMiddleware(max_retries=2, base_delay_ms=1)
        client = DinoClient(
            providers=[provider],
            middleware=[mw],
            catalog=_catalog_with_faux(),
        )

        ctx = Context(messages=[UserMessage(content="Hi")])
        msg = await client.complete("faux-1", ctx)
        assert msg.stop_reason == "stop"
        assert provider.call_count == 1

    @pytest.mark.asyncio
    async def test_retries_retryable_error(self):
        retryable_error = DinoError(
            category=ErrorCategory.RATE_LIMITED,
            provider="faux",
            message="Rate limited",
            retryable=True,
        )
        # First call: error, second call: error, third call: success
        provider = FauxProvider(responses=[_error_msg(retryable_error), _error_msg(retryable_error), "success"])
        mw = RetryMiddleware(max_retries=2, base_delay_ms=1)
        client = DinoClient(
            providers=[provider],
            middleware=[mw],
            catalog=_catalog_with_faux(),
        )

        ctx = Context(messages=[UserMessage(content="Hi")])
        msg = await client.complete("faux-1", ctx)
        assert msg.stop_reason == "stop"
        # attempt 0: error (retry), attempt 1: error (retry), attempt 2: success (forward)
        assert provider.call_count == 3

    @pytest.mark.asyncio
    async def test_no_retry_on_non_retryable(self):
        non_retryable = DinoError(
            category=ErrorCategory.AUTH_FAILURE,
            provider="faux",
            message="Invalid key",
            retryable=False,
        )
        provider = FauxProvider(responses=[_error_msg(non_retryable), "should not reach"])
        mw = RetryMiddleware(max_retries=3, base_delay_ms=1)
        client = DinoClient(
            providers=[provider],
            middleware=[mw],
            catalog=_catalog_with_faux(),
        )

        ctx = Context(messages=[UserMessage(content="Hi")])
        msg = await client.complete("faux-1", ctx)
        assert msg.stop_reason == "error"
        # Non-retryable: only 1 call, error forwarded immediately
        assert provider.call_count == 1

    @pytest.mark.asyncio
    async def test_respects_max_retries_from_options(self):
        retryable_error = DinoError(
            category=ErrorCategory.SERVER_ERROR,
            provider="faux",
            message="500",
            retryable=True,
        )
        provider = FauxProvider(responses=[
            _error_msg(retryable_error), _error_msg(retryable_error), _error_msg(retryable_error), "ok",
        ])
        mw = RetryMiddleware(max_retries=5, base_delay_ms=1)
        client = DinoClient(
            providers=[provider],
            middleware=[mw],
            catalog=_catalog_with_faux(),
        )

        ctx = Context(messages=[UserMessage(content="Hi")])
        opts = StreamOptions(max_retries=1)
        msg = await client.complete("faux-1", ctx, opts)
        # max_retries=1: attempt 0 (error, retry), attempt 1 (error, forward)
        assert msg.stop_reason == "error"
        assert provider.call_count == 2


# ── CostGuardMiddleware Tests ───────────────────────────────────


class TestCostGuardMiddleware:
    @pytest.mark.asyncio
    async def test_allows_under_budget(self):
        provider = FauxProvider(responses=["ok"])
        guard = CostGuardMiddleware(max_total_cost=10.0)
        client = DinoClient(
            providers=[provider],
            middleware=[guard],
            catalog=_catalog_with_faux(),
        )

        ctx = Context(messages=[UserMessage(content="Hi")])
        msg = await client.complete("faux-1", ctx)
        assert msg.stop_reason == "stop"

    @pytest.mark.asyncio
    async def test_blocks_over_budget(self):
        provider = FauxProvider(responses=["ok"])
        guard = CostGuardMiddleware(max_total_cost=0.0)  # Zero budget
        client = DinoClient(
            providers=[provider],
            middleware=[guard],
            catalog=_catalog_with_faux(),
        )

        ctx = Context(messages=[UserMessage(content="Hi")])
        msg = await client.complete("faux-1", ctx)
        assert msg.stop_reason == "error"
        assert msg.error is not None
        assert msg.error.category == ErrorCategory.QUOTA_EXCEEDED
        assert "budget exhausted" in msg.error.message

    @pytest.mark.asyncio
    async def test_tracks_cumulative_cost(self):
        guard = CostGuardMiddleware(max_total_cost=10.0)
        assert guard.total_cost == 0.0
        assert guard.remaining_budget == 10.0

    @pytest.mark.asyncio
    async def test_remaining_budget(self):
        guard = CostGuardMiddleware(max_total_cost=5.0)
        assert guard.remaining_budget == 5.0

        # Simulate internal cost tracking
        guard._total_cost = 3.0
        assert guard.remaining_budget == 2.0
        assert guard.total_cost == 3.0

    @pytest.mark.asyncio
    async def test_blocks_after_budget_exceeded(self):
        provider = FauxProvider(responses=["ok", "ok"])
        guard = CostGuardMiddleware(max_total_cost=0.001)
        client = DinoClient(
            providers=[provider],
            middleware=[guard],
            catalog=_catalog_with_faux(),
        )

        ctx = Context(messages=[UserMessage(content="Hi")])
        # First call succeeds (faux has zero cost)
        msg1 = await client.complete("faux-1", ctx)
        assert msg1.stop_reason == "stop"

        # Simulate cost
        guard._total_cost = 0.002

        # Second call should be blocked
        msg2 = await client.complete("faux-1", ctx)
        assert msg2.stop_reason == "error"
        assert msg2.error is not None
        assert msg2.error.category == ErrorCategory.QUOTA_EXCEEDED
