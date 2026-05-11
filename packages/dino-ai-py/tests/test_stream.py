"""Tests for basic streaming via FauxProvider."""

from __future__ import annotations

import pytest

from dino_ai.client import DinoClient
from dino_ai.context import Context
from dino_ai.events import StreamDone, TextDelta
from dino_ai.providers.faux import FauxProvider


@pytest.mark.asyncio
async def test_stream_basic_text(faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context):
    """Stream a simple text response and verify event sequence."""
    faux_provider.set_responses(["Hello, world!"])

    events = []
    async for event in client.stream(model, simple_context):
        events.append(event)

    # Should have: StreamStart, TextStart, TextDelta(s), TextEnd, StreamDone
    types = [type(e).__name__ for e in events]
    assert types[0] == "StreamStart"
    assert "TextStart" in types
    assert "TextDelta" in types
    assert "TextEnd" in types
    assert types[-1] == "StreamDone"


@pytest.mark.asyncio
async def test_stream_collects_full_text(
    faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context
):
    """TextDelta chunks should reconstruct the full text."""
    faux_provider.set_responses(["The quick brown fox"])

    deltas = []
    async for event in client.stream(model, simple_context):
        if isinstance(event, TextDelta):
            deltas.append(event.delta)

    assert "".join(deltas) == "The quick brown fox"


@pytest.mark.asyncio
async def test_stream_done_contains_message(
    faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context
):
    """StreamDone event should contain the final AssistantMessage."""
    faux_provider.set_responses(["Final answer"])

    done_event = None
    async for event in client.stream(model, simple_context):
        if isinstance(event, StreamDone):
            done_event = event

    assert done_event is not None
    assert done_event.message.content[0].text == "Final answer"
    assert done_event.reason == "stop"


@pytest.mark.asyncio
async def test_stream_model_id_string(faux_provider: FauxProvider, client: DinoClient, simple_context: Context):
    """Stream using model id string instead of Model object."""
    faux_provider.set_responses(["via string"])

    events = []
    async for event in client.stream("faux-1", simple_context):
        events.append(event)

    types = [type(e).__name__ for e in events]
    assert "StreamDone" in types
