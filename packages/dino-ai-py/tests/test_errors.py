"""Tests for error handling and DinoError categories."""

from __future__ import annotations

import pytest

from dino_ai.client import DinoClient
from dino_ai.context import AssistantMessage, Context
from dino_ai.error import DinoError, DinoException, ErrorCategory
from dino_ai.events import StreamError
from dino_ai.providers.faux import FAUX_API, FAUX_PROVIDER, FauxProvider, faux_text


@pytest.mark.asyncio
async def test_error_event_emitted(faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context):
    """When response has an error, StreamError should be emitted."""
    error_msg = AssistantMessage(
        content=[faux_text("error occurred")],
        model="faux-1",
        provider=FAUX_PROVIDER,
        api=FAUX_API,
        stop_reason="error",
        error=DinoError(
            category=ErrorCategory.RATE_LIMITED,
            provider=FAUX_PROVIDER,
            message="Rate limited",
            retryable=True,
            retry_after_ms=1000,
        ),
    )
    faux_provider.set_responses([error_msg])

    error_event = None
    async for event in client.stream(model, simple_context):
        if isinstance(event, StreamError):
            error_event = event

    assert error_event is not None
    assert error_event.error.category == ErrorCategory.RATE_LIMITED
    assert error_event.error.retryable is True
    assert error_event.error.retry_after_ms == 1000


@pytest.mark.asyncio
async def test_no_responses_emits_error(
    faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context
):
    """When no responses are configured, FauxProvider should emit an error."""
    error_event = None
    async for event in client.stream(model, simple_context):
        if isinstance(event, StreamError):
            error_event = event

    assert error_event is not None
    assert error_event.error.category == ErrorCategory.PROVIDER_ERROR


@pytest.mark.asyncio
async def test_unknown_model_raises(client: DinoClient, simple_context: Context):
    """Looking up an unknown model id should raise DinoException."""
    with pytest.raises(DinoException, match="Model not found"):
        client.stream("nonexistent-model", simple_context)


@pytest.mark.asyncio
async def test_unknown_api_raises(client: DinoClient, simple_context: Context):
    """Using a Model with an unregistered api should raise DinoException."""
    from dino_ai.model import Model, ModelCapabilities, ModelLimits, ModelPricing

    bad_model = Model(
        id="bad",
        name="Bad",
        api="unknown-api",
        provider="test",
        base_url="",
        capabilities=ModelCapabilities(),
        limits=ModelLimits(),
        pricing=ModelPricing(),
    )
    with pytest.raises(DinoException, match="No provider registered"):
        client.stream(bad_model, simple_context)


def test_error_category_values():
    """ErrorCategory enum should have all expected values."""
    assert ErrorCategory.CONTEXT_OVERFLOW.value == "context_overflow"
    assert ErrorCategory.RATE_LIMITED.value == "rate_limited"
    assert ErrorCategory.AUTH_FAILURE.value == "auth_failure"
    assert ErrorCategory.ABORTED.value == "aborted"
    assert ErrorCategory.UNKNOWN.value == "unknown"
