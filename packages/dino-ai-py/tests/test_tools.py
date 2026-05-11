"""Tests for tool calling round-trip."""

from __future__ import annotations

import pytest

from dino_ai.client import DinoClient
from dino_ai.content import ToolCall
from dino_ai.context import Context
from dino_ai.events import StreamDone, ToolCallEnd
from dino_ai.providers.faux import FauxProvider, faux_text, faux_tool_call


@pytest.mark.asyncio
async def test_tool_call_streaming(faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context):
    """Tool calls should emit ToolCallStart/Delta/End events."""
    tc = faux_tool_call("get_weather", {"city": "Tokyo"})
    faux_provider.set_responses([[tc]])

    tool_end = None
    async for event in client.stream(model, simple_context):
        if isinstance(event, ToolCallEnd):
            tool_end = event

    assert tool_end is not None
    assert tool_end.tool_call.name == "get_weather"
    assert tool_end.tool_call.arguments == {"city": "Tokyo"}


@pytest.mark.asyncio
async def test_tool_call_stop_reason(faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context):
    """Responses with tool calls should have stop_reason='toolUse'."""
    tc = faux_tool_call("search", {"query": "test"})
    faux_provider.set_responses([[tc]])

    done = None
    async for event in client.stream(model, simple_context):
        if isinstance(event, StreamDone):
            done = event

    assert done is not None
    assert done.reason == "toolUse"


@pytest.mark.asyncio
async def test_tool_call_complete(faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context):
    """Complete with tool call should return AssistantMessage with ToolCall content."""
    tc = faux_tool_call("calculator", {"expression": "2+2"}, call_id="tool-123")
    faux_provider.set_responses([[tc]])

    msg = await client.complete(model, simple_context)
    assert len(msg.content) == 1
    assert isinstance(msg.content[0], ToolCall)
    assert msg.content[0].name == "calculator"
    assert msg.content[0].id == "tool-123"


@pytest.mark.asyncio
async def test_tool_call_with_text(faux_provider: FauxProvider, client: DinoClient, model, simple_context: Context):
    """Tool call can be mixed with text content."""
    tc = faux_tool_call("lookup", {"key": "foo"})
    faux_provider.set_responses([[faux_text("Let me check..."), tc]])

    msg = await client.complete(model, simple_context)
    assert len(msg.content) == 2
    assert msg.content[0].text == "Let me check..."
    assert isinstance(msg.content[1], ToolCall)
