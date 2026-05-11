"""Tests for client.complete() — non-streaming await."""

from __future__ import annotations

import pytest

from dino_ai.client import DinoClient
from dino_ai.content import TextContent
from dino_ai.context import Context
from dino_ai.providers.faux import FauxProvider, faux_text, faux_thinking


@pytest.mark.asyncio
async def test_complete_returns_message(
    faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context
):
    faux_provider.set_responses(["Hello from complete"])
    msg = await client.complete(model, simple_context)
    assert isinstance(msg.content[0], TextContent)
    assert msg.content[0].text == "Hello from complete"


@pytest.mark.asyncio
async def test_complete_with_thinking(faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context):
    faux_provider.set_responses([[faux_thinking("Let me think..."), faux_text("The answer is 42")]])
    msg = await client.complete(model, simple_context)
    assert len(msg.content) == 2
    assert msg.content[0].thinking == "Let me think..."
    assert msg.content[1].text == "The answer is 42"


@pytest.mark.asyncio
async def test_complete_multiple_responses(
    faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context
):
    faux_provider.set_responses(["First", "Second", "Third"])
    msg1 = await client.complete(model, simple_context)
    msg2 = await client.complete(model, simple_context)
    msg3 = await client.complete(model, simple_context)
    assert msg1.content[0].text == "First"
    assert msg2.content[0].text == "Second"
    assert msg3.content[0].text == "Third"


@pytest.mark.asyncio
async def test_complete_with_string_model_id(faux_provider: FauxProvider, client: DinoClient, simple_context: Context):
    faux_provider.set_responses(["via string id"])
    msg = await client.complete("faux-1", simple_context)
    assert msg.content[0].text == "via string id"


@pytest.mark.asyncio
async def test_complete_usage_populated(
    faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context
):
    faux_provider.set_responses(["Some response text"])
    msg = await client.complete(model, simple_context)
    assert msg.usage.input_tokens > 0
    assert msg.usage.output_tokens > 0
    assert msg.usage.total_tokens > 0
