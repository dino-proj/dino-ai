"""Tests for OpenAI Chat Completions provider — unit tests with mocked HTTP."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator
from typing import Any

import pytest

from dino_ai.content import TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context, Tool, ToolResultMessage, UserMessage
from dino_ai.events import (
    StreamDone,
    StreamStart,
)
from dino_ai.model import Model, ModelCapabilities, ModelLimits, ModelPricing
from dino_ai.providers.openai_compat import PROFILE_OPENAI, OpenAICompatProfile
from dino_ai.providers.openai_completions import (
    OpenAICompletionsProvider,
    _classify_error,
    _finalize_blocks,
    _map_stop_reason,
    _parse_usage,
    _process_chunk,
    _StreamState,
)
from dino_ai.providers.openai_messages import convert_messages, convert_tools, has_tool_history
from dino_ai.providers.openai_sse import parse_sse_stream
from dino_ai.stream import EventStream
from dino_ai.usage import Usage

# ── Helpers ──────────────────────────────────────────────────────


def _model(
    model_id: str = "gpt-4o",
    provider: str = "openai",
    api: str = "openai-completions",
    reasoning: bool = False,
    vision: bool = True,
) -> Model:
    return Model(
        id=model_id,
        name="Test Model",
        api=api,
        provider=provider,
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(reasoning=reasoning, vision=vision),
        limits=ModelLimits(context_window=128000, max_output_tokens=16384),
        pricing=ModelPricing(input=2.5, output=10.0),
    )


def _sse_lines(*chunks: dict[str, Any]) -> list[bytes]:
    """Build SSE byte chunks from dicts."""
    lines: list[bytes] = []
    for chunk in chunks:
        lines.append(f"data: {json.dumps(chunk)}\n\n".encode())
    lines.append(b"data: [DONE]\n\n")
    return lines


def _text_chunk(
    text: str,
    index: int = 0,
    finish_reason: str | None = None,
    chunk_id: str = "chatcmpl-123",
    model: str = "gpt-4o",
) -> dict[str, Any]:
    return {
        "id": chunk_id,
        "object": "chat.completion.chunk",
        "model": model,
        "choices": [{
            "index": index,
            "delta": {"content": text},
            "finish_reason": finish_reason,
        }],
    }


def _tool_call_chunk(
    index: int = 0,
    tc_id: str | None = None,
    name: str | None = None,
    arguments: str | None = None,
    finish_reason: str | None = None,
) -> dict[str, Any]:
    tc: dict[str, Any] = {"index": 0}
    if tc_id:
        tc["id"] = tc_id
    func: dict[str, Any] = {}
    if name:
        func["name"] = name
    if arguments is not None:
        func["arguments"] = arguments
    if func:
        tc["function"] = func
    return {
        "id": "chatcmpl-123",
        "object": "chat.completion.chunk",
        "model": "gpt-4o",
        "choices": [{
            "index": index,
            "delta": {"tool_calls": [tc]},
            "finish_reason": finish_reason,
        }],
    }


def _usage_chunk(
    prompt_tokens: int = 10,
    completion_tokens: int = 20,
    total_tokens: int = 30,
) -> dict[str, Any]:
    return {
        "id": "chatcmpl-123",
        "object": "chat.completion.chunk",
        "model": "gpt-4o",
        "choices": [],
        "usage": {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
        },
    }


def _reasoning_chunk(text: str, field: str = "reasoning_content") -> dict[str, Any]:
    return {
        "id": "chatcmpl-123",
        "model": "gpt-4o",
        "choices": [{
            "index": 0,
            "delta": {field: text},
            "finish_reason": None,
        }],
    }


# ── SSE Parser Tests ────────────────────────────────────────────


class TestSSEParser:
    @pytest.mark.asyncio
    async def test_basic_parsing(self):
        async def byte_iter() -> AsyncIterator[bytes]:
            yield b'data: {"id": "1"}\n\n'
            yield b'data: {"id": "2"}\n\n'
            yield b"data: [DONE]\n\n"

        results = [chunk async for chunk in parse_sse_stream(byte_iter())]
        assert len(results) == 2
        assert results[0]["id"] == "1"
        assert results[1]["id"] == "2"

    @pytest.mark.asyncio
    async def test_handles_split_lines(self):
        async def byte_iter() -> AsyncIterator[bytes]:
            yield b'data: {"id":'
            yield b' "split"}\n\ndata: [DONE]\n\n'

        results = [chunk async for chunk in parse_sse_stream(byte_iter())]
        assert len(results) == 1
        assert results[0]["id"] == "split"

    @pytest.mark.asyncio
    async def test_skips_non_data_lines(self):
        async def byte_iter() -> AsyncIterator[bytes]:
            yield b"event: message\n"
            yield b'data: {"ok": true}\n\n'
            yield b": comment\n"
            yield b"data: [DONE]\n\n"

        results = [chunk async for chunk in parse_sse_stream(byte_iter())]
        assert len(results) == 1
        assert results[0]["ok"] is True

    @pytest.mark.asyncio
    async def test_skips_malformed_json(self):
        async def byte_iter() -> AsyncIterator[bytes]:
            yield b"data: not json\n\n"
            yield b'data: {"ok": true}\n\n'
            yield b"data: [DONE]\n\n"

        results = [chunk async for chunk in parse_sse_stream(byte_iter())]
        assert len(results) == 1


# ── Message Converter Tests ─────────────────────────────────────


class TestMessageConverter:
    def test_system_prompt_as_system(self):
        model = _model()
        ctx = Context(system_prompt="You are helpful", messages=[])
        result = convert_messages(model, ctx, PROFILE_OPENAI)
        assert result[0]["role"] == "system"

    def test_system_prompt_as_developer(self):
        model = _model(reasoning=True)
        profile = OpenAICompatProfile(use_developer_role=True)
        ctx = Context(system_prompt="Think carefully", messages=[])
        result = convert_messages(model, ctx, profile)
        assert result[0]["role"] == "developer"

    def test_user_text_message(self):
        model = _model()
        ctx = Context(messages=[UserMessage(content="Hello")])
        result = convert_messages(model, ctx, PROFILE_OPENAI)
        assert result[0] == {"role": "user", "content": "Hello"}

    def test_user_image_message(self):
        from dino_ai.content import ImageContent

        model = _model()
        ctx = Context(messages=[
            UserMessage(content=[
                TextContent(text="Describe this"),
                ImageContent(data=b"\x89PNG", mime_type="image/png"),
            ])
        ])
        result = convert_messages(model, ctx, PROFILE_OPENAI)
        parts = result[0]["content"]
        assert len(parts) == 2
        assert parts[0]["type"] == "text"
        assert parts[1]["type"] == "image_url"
        assert parts[1]["image_url"]["url"].startswith("data:image/png;base64,")

    def test_assistant_text_message(self):
        model = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[TextContent(text="I am helpful")],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
            ),
        ])
        result = convert_messages(model, ctx, PROFILE_OPENAI)
        assert result[0]["role"] == "assistant"
        assert result[0]["content"] == "I am helpful"

    def test_assistant_with_tool_calls(self):
        model = _model()
        tc = ToolCall(id="tc-1", name="search", arguments={"q": "test"})
        ctx = Context(messages=[
            AssistantMessage(
                content=[tc],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
            ),
        ])
        result = convert_messages(model, ctx, PROFILE_OPENAI)
        assert len(result[0]["tool_calls"]) == 1
        assert result[0]["tool_calls"][0]["function"]["name"] == "search"

    def test_tool_result_message(self):
        model = _model()
        ctx = Context(messages=[
            ToolResultMessage(
                tool_call_id="tc-1",
                tool_name="search",
                content=[TextContent(text="Found 5 results")],
            ),
        ])
        result = convert_messages(model, ctx, PROFILE_OPENAI)
        assert result[0]["role"] == "tool"
        assert result[0]["tool_call_id"] == "tc-1"
        assert result[0]["content"] == "Found 5 results"

    def test_errored_assistant_skipped(self):
        model = _model()
        ctx = Context(messages=[
            UserMessage(content="hello"),
            AssistantMessage(
                content=[TextContent(text="partial")],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
                stop_reason="error",
            ),
            UserMessage(content="retry"),
        ])
        result = convert_messages(model, ctx, PROFILE_OPENAI)
        assert len(result) == 2
        assert result[0]["content"] == "hello"
        assert result[1]["content"] == "retry"


class TestToolConverter:
    def test_basic_tool(self):
        tools = [Tool(
            name="search",
            description="Search the web",
            parameters={"type": "object", "properties": {"q": {"type": "string"}}},
        )]
        result = convert_tools(tools, PROFILE_OPENAI)
        assert len(result) == 1
        assert result[0]["type"] == "function"
        assert result[0]["function"]["name"] == "search"


class TestToolHistory:
    def test_no_history(self):
        assert has_tool_history([UserMessage(content="hi")]) is False

    def test_has_tool_result(self):
        msgs = [ToolResultMessage(tool_call_id="tc-1", tool_name="x", content=[])]
        assert has_tool_history(msgs) is True

    def test_has_tool_call(self):
        msgs = [AssistantMessage(
            content=[ToolCall(id="tc-1", name="x", arguments={})],
            model="m", provider="p", api="a",
        )]
        assert has_tool_history(msgs) is True


# ── Stop Reason Tests ───────────────────────────────────────────


class TestMapStopReason:
    def test_stop(self):
        assert _map_stop_reason("stop") == ("stop", None)

    def test_length(self):
        assert _map_stop_reason("length") == ("length", None)

    def test_tool_calls(self):
        assert _map_stop_reason("tool_calls") == ("toolUse", None)

    def test_content_filter(self):
        reason, msg = _map_stop_reason("content_filter")
        assert reason == "error"
        assert msg is not None

    def test_none(self):
        assert _map_stop_reason(None) == ("stop", None)


# ── Usage Parser Tests ──────────────────────────────────────────


class TestParseUsage:
    def test_basic_usage(self):
        model = _model()
        usage = _parse_usage({
            "prompt_tokens": 100,
            "completion_tokens": 50,
            "total_tokens": 150,
        }, model)
        assert usage.input_tokens == 100
        assert usage.output_tokens == 50
        assert usage.total_tokens == 150
        assert usage.cost.total > 0

    def test_cost_calculation(self):
        model = _model()
        usage = _parse_usage({
            "prompt_tokens": 1_000_000,
            "completion_tokens": 1_000_000,
            "total_tokens": 2_000_000,
        }, model)
        assert abs(usage.cost.input - 2.5) < 0.001
        assert abs(usage.cost.output - 10.0) < 0.001


# ── Error Classification Tests ──────────────────────────────────


class TestClassifyError:
    def test_auth_error(self):
        err = _classify_error(401, '{"error": {"message": "Invalid API key"}}', "openai")
        assert err.category.value == "auth_failure"
        assert err.message == "Invalid API key"

    def test_rate_limited(self):
        err = _classify_error(429, '{"error": {"message": "Rate limit"}}', "openai")
        assert err.category.value == "rate_limited"
        assert err.retryable is True

    def test_context_overflow(self):
        err = _classify_error(400, '{"error": {"message": "context length exceeded"}}', "openai")
        assert err.category.value == "context_overflow"

    def test_model_not_found(self):
        err = _classify_error(404, '{"error": {"message": "Model not found"}}', "openai")
        assert err.category.value == "model_not_found"

    def test_server_error(self):
        err = _classify_error(500, "Internal Server Error", "openai")
        assert err.category.value == "server_error"
        assert err.retryable is True


# ── Integration Tests via _process_chunk ────────────────────────


def _make_state(model: Model | None = None) -> tuple[_StreamState, EventStream]:
    m = model or _model()
    output = AssistantMessage(
        model=m.id,
        provider=m.provider,
        api="openai-completions",
        usage=Usage(),
        stop_reason="stop",
    )
    return _StreamState(output), EventStream()


@pytest.mark.asyncio
async def test_stream_basic_text():
    """Process text chunks through _process_chunk and verify events."""
    model = _model()
    state, stream = _make_state(model)
    profile = PROFILE_OPENAI

    stream.push(StreamStart(partial=state.output))

    _process_chunk(_text_chunk("Hello"), state, stream, profile, model)
    _process_chunk(_text_chunk(", world!"), state, stream, profile, model)
    _process_chunk(_text_chunk("", finish_reason="stop"), state, stream, profile, model)
    _process_chunk(_usage_chunk(10, 5, 15), state, stream, profile, model)

    _finalize_blocks(state, stream)
    state.output.content = list(state.blocks)
    stream.push(StreamDone(reason=state.output.stop_reason, message=state.output))

    events = [e async for e in stream]
    types = [type(e).__name__ for e in events]
    assert "StreamStart" in types
    assert "TextStart" in types
    assert "TextDelta" in types
    assert "TextEnd" in types
    assert "StreamDone" in types

    done = next(e for e in events if isinstance(e, StreamDone))
    assert done.message.content[0].text == "Hello, world!"
    assert done.reason == "stop"


@pytest.mark.asyncio
async def test_stream_tool_call():
    """Tool call streaming through _process_chunk."""
    model = _model()
    state, stream = _make_state(model)
    profile = PROFILE_OPENAI

    stream.push(StreamStart(partial=state.output))

    _process_chunk(_tool_call_chunk(tc_id="call-1", name="search"), state, stream, profile, model)
    _process_chunk(_tool_call_chunk(arguments='{"q": "'), state, stream, profile, model)
    _process_chunk(_tool_call_chunk(arguments='test"}'), state, stream, profile, model)
    _process_chunk(_tool_call_chunk(finish_reason="tool_calls"), state, stream, profile, model)
    _process_chunk(_usage_chunk(10, 15, 25), state, stream, profile, model)

    _finalize_blocks(state, stream)
    state.output.content = list(state.blocks)
    stream.push(StreamDone(reason=state.output.stop_reason, message=state.output))

    events = [e async for e in stream]
    types = [type(e).__name__ for e in events]
    assert "ToolCallStart" in types
    assert "ToolCallDelta" in types
    assert "ToolCallEnd" in types

    done = next(e for e in events if isinstance(e, StreamDone))
    assert done.reason == "toolUse"
    tc = done.message.content[0]
    assert isinstance(tc, ToolCall)
    assert tc.name == "search"
    assert tc.arguments.get("q") == "test"


@pytest.mark.asyncio
async def test_stream_reasoning():
    """Reasoning content through _process_chunk."""
    model = _model(reasoning=True)
    state, stream = _make_state(model)
    profile = PROFILE_OPENAI

    stream.push(StreamStart(partial=state.output))

    _process_chunk(_reasoning_chunk("Let me think"), state, stream, profile, model)
    _process_chunk(_reasoning_chunk("...carefully"), state, stream, profile, model)
    _process_chunk(_text_chunk("The answer is 42"), state, stream, profile, model)
    _process_chunk(_text_chunk("", finish_reason="stop"), state, stream, profile, model)
    _process_chunk(_usage_chunk(), state, stream, profile, model)

    _finalize_blocks(state, stream)
    state.output.content = list(state.blocks)
    stream.push(StreamDone(reason=state.output.stop_reason, message=state.output))

    events = [e async for e in stream]
    types = [type(e).__name__ for e in events]
    assert "ThinkingStart" in types
    assert "ThinkingDelta" in types
    assert "ThinkingEnd" in types

    done = next(e for e in events if isinstance(e, StreamDone))
    assert len(done.message.content) == 2
    assert isinstance(done.message.content[0], ThinkingContent)
    assert done.message.content[0].thinking == "Let me think...carefully"
    assert isinstance(done.message.content[1], TextContent)
    assert done.message.content[1].text == "The answer is 42"


@pytest.mark.asyncio
async def test_stream_usage_populated():
    """Usage data should be populated from the usage chunk."""
    model = _model()
    state, stream = _make_state(model)
    profile = PROFILE_OPENAI

    stream.push(StreamStart(partial=state.output))

    _process_chunk(_text_chunk("ok", finish_reason="stop"), state, stream, profile, model)
    _process_chunk(_usage_chunk(100, 50, 150), state, stream, profile, model)

    _finalize_blocks(state, stream)
    state.output.content = list(state.blocks)
    stream.push(StreamDone(reason=state.output.stop_reason, message=state.output))

    events = [e async for e in stream]
    done = next(e for e in events if isinstance(e, StreamDone))
    assert done.message.usage.input_tokens == 100
    assert done.message.usage.output_tokens == 50
    assert done.message.usage.total_tokens == 150
    assert done.message.usage.cost.total > 0


@pytest.mark.asyncio
async def test_stream_response_id_captured():
    """Response ID should be captured from the first chunk."""
    model = _model()
    state, stream = _make_state(model)
    profile = PROFILE_OPENAI

    _process_chunk(_text_chunk("hi", chunk_id="cmpl-abc123"), state, stream, profile, model)
    assert state.output.response_id == "cmpl-abc123"


@pytest.mark.asyncio
async def test_stream_response_model_captured():
    """Response model should be captured when different from request model."""
    model = _model(model_id="gpt-4o")
    state, stream = _make_state(model)
    profile = PROFILE_OPENAI

    _process_chunk(_text_chunk("hi", model="gpt-4o-2024-11-20"), state, stream, profile, model)
    assert state.output.response_model == "gpt-4o-2024-11-20"


def test_provider_api_id():
    """Provider should report openai-completions as its API."""
    provider = OpenAICompletionsProvider()
    assert provider.api == "openai-completions"
