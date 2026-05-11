"""Tests for Anthropic Messages API provider — unit tests via _process_event."""

from __future__ import annotations

from collections.abc import AsyncIterator

import pytest

from dino_ai.content import ImageContent, TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context, Tool, ToolResultMessage, UserMessage
from dino_ai.events import (
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
from dino_ai.providers.anthropic import (
    _build_params,
    _classify_error,
    _get_api_key,
    _parse_usage,
    _process_event,
    _StreamState,
)
from dino_ai.providers.anthropic_messages import convert_messages, convert_system, convert_tools, map_stop_reason
from dino_ai.providers.anthropic_sse import parse_anthropic_sse
from dino_ai.stream import EventStream
from dino_ai.usage import Usage

# ── Helpers ──────────────────────────────────────────────────────


def _model(
    model_id: str = "claude-sonnet-4-20250514",
    provider: str = "anthropic",
    api: str = "anthropic-messages",
    reasoning: bool = False,
    vision: bool = True,
) -> Model:
    return Model(
        id=model_id,
        name="Claude Sonnet 4",
        api=api,
        provider=provider,
        base_url="https://api.anthropic.com/v1",
        capabilities=ModelCapabilities(reasoning=reasoning, vision=vision),
        limits=ModelLimits(context_window=200000, max_output_tokens=8192),
        pricing=ModelPricing(input=3.0, output=15.0, cache_read=0.3, cache_write=3.75),
    )


def _make_state(model: Model | None = None) -> tuple[_StreamState, EventStream, Model]:
    m = model or _model()
    output = AssistantMessage(
        model=m.id,
        provider=m.provider,
        api="anthropic-messages",
        usage=Usage(),
        stop_reason="stop",
    )
    state = _StreamState(output)
    stream = EventStream()
    return state, stream, m


# ── SSE Parser Tests ────────────────────────────────────────────


class TestAnthropicSSEParser:
    @pytest.mark.asyncio
    async def test_basic_event_parsing(self):
        async def byte_iter() -> AsyncIterator[bytes]:
            yield b"event: message_start\n"
            yield b'data: {"type": "message_start", "message": {"id": "msg_1"}}\n\n'

        results = [ev async for ev in parse_anthropic_sse(byte_iter())]
        assert len(results) == 1
        assert results[0][0] == "message_start"
        assert results[0][1]["message"]["id"] == "msg_1"

    @pytest.mark.asyncio
    async def test_multiple_events(self):
        async def byte_iter() -> AsyncIterator[bytes]:
            yield b"event: content_block_start\n"
            yield b'data: {"type": "content_block_start", "index": 0}\n\n'
            yield b"event: content_block_delta\n"
            data = '{"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "Hi"}}'
            yield f"data: {data}\n\n".encode()

        results = [ev async for ev in parse_anthropic_sse(byte_iter())]
        assert len(results) == 2
        assert results[0][0] == "content_block_start"
        assert results[1][0] == "content_block_delta"

    @pytest.mark.asyncio
    async def test_handles_split_chunks(self):
        async def byte_iter() -> AsyncIterator[bytes]:
            yield b"event: message_"
            yield b"start\ndata: {\"type\":"
            yield b" \"message_start\"}\n\n"

        results = [ev async for ev in parse_anthropic_sse(byte_iter())]
        assert len(results) == 1
        assert results[0][0] == "message_start"

    @pytest.mark.asyncio
    async def test_malformed_json_yields_raw(self):
        async def byte_iter() -> AsyncIterator[bytes]:
            yield b"event: error\n"
            yield b"data: not valid json\n\n"

        results = [ev async for ev in parse_anthropic_sse(byte_iter())]
        assert len(results) == 1
        assert results[0][0] == "error"
        assert results[0][1] == {"raw": "not valid json"}


# ── Message Converter Tests ─────────────────────────────────────


class TestAnthropicMessageConverter:
    def test_system_prompt(self):
        ctx = Context(system_prompt="You are a helpful assistant.", messages=[])
        result = convert_system(ctx)
        assert result is not None
        assert len(result) == 1
        assert result[0]["type"] == "text"
        assert result[0]["text"] == "You are a helpful assistant."

    def test_no_system_prompt(self):
        ctx = Context(messages=[])
        result = convert_system(ctx)
        assert result is None

    def test_user_text_message(self):
        model = _model()
        ctx = Context(messages=[UserMessage(content="Hello")])
        result = convert_messages(model, ctx)
        assert result[0] == {"role": "user", "content": "Hello"}

    def test_user_image_message(self):
        model = _model()
        ctx = Context(messages=[
            UserMessage(content=[
                TextContent(text="Describe this"),
                ImageContent(data=b"\x89PNG", mime_type="image/png"),
            ])
        ])
        result = convert_messages(model, ctx)
        parts = result[0]["content"]
        assert len(parts) == 2
        assert parts[0]["type"] == "text"
        assert parts[1]["type"] == "image"
        assert parts[1]["source"]["type"] == "base64"
        assert parts[1]["source"]["media_type"] == "image/png"

    def test_image_only_gets_placeholder(self):
        model = _model()
        ctx = Context(messages=[
            UserMessage(content=[ImageContent(data=b"\xff\xd8\xff", mime_type="image/jpeg")])
        ])
        result = convert_messages(model, ctx)
        parts = result[0]["content"]
        assert len(parts) == 2
        assert parts[0]["type"] == "text"
        assert parts[0]["text"] == "(see attached image)"
        assert parts[1]["type"] == "image"

    def test_assistant_text_message(self):
        model = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[TextContent(text="I can help")],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ])
        result = convert_messages(model, ctx)
        assert result[0]["role"] == "assistant"
        assert result[0]["content"][0]["type"] == "text"
        assert result[0]["content"][0]["text"] == "I can help"

    def test_assistant_thinking_same_model(self):
        model = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Let me think...", signature="sig123"),
                    TextContent(text="Answer"),
                ],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ])
        result = convert_messages(model, ctx)
        blocks = result[0]["content"]
        assert blocks[0]["type"] == "thinking"
        assert blocks[0]["thinking"] == "Let me think..."
        assert blocks[0]["signature"] == "sig123"
        assert blocks[1]["type"] == "text"

    def test_assistant_thinking_cross_model_becomes_text(self):
        model = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Let me think...", signature="sig123"),
                    TextContent(text="Answer"),
                ],
                model="claude-opus-4-20250514",  # Different model
                provider="anthropic",
                api="anthropic-messages",
            ),
        ])
        result = convert_messages(model, ctx)
        blocks = result[0]["content"]
        # Thinking from different model should become plain text
        assert blocks[0]["type"] == "text"
        assert blocks[0]["text"] == "Let me think..."
        assert blocks[1]["type"] == "text"

    def test_assistant_redacted_thinking_same_model(self):
        model = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="[Reasoning redacted]", signature="redacted_data", redacted=True),
                    TextContent(text="Answer"),
                ],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ])
        result = convert_messages(model, ctx)
        blocks = result[0]["content"]
        assert blocks[0]["type"] == "redacted_thinking"
        assert blocks[0]["data"] == "redacted_data"

    def test_assistant_tool_calls(self):
        model = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[ToolCall(id="tc-1", name="search", arguments={"q": "test"})],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ])
        result = convert_messages(model, ctx)
        blocks = result[0]["content"]
        assert blocks[0]["type"] == "tool_use"
        assert blocks[0]["id"] == "tc-1"
        assert blocks[0]["name"] == "search"
        assert blocks[0]["input"] == {"q": "test"}

    def test_tool_results_batched(self):
        model = _model()
        ctx = Context(messages=[
            ToolResultMessage(
                tool_call_id="tc-1",
                tool_name="search",
                content=[TextContent(text="Found 5 results")],
            ),
            ToolResultMessage(
                tool_call_id="tc-2",
                tool_name="read",
                content=[TextContent(text="File contents")],
            ),
        ])
        result = convert_messages(model, ctx)
        # Two tool results should be batched into one user message
        assert len(result) == 1
        assert result[0]["role"] == "user"
        assert len(result[0]["content"]) == 2
        assert result[0]["content"][0]["type"] == "tool_result"
        assert result[0]["content"][0]["tool_use_id"] == "tc-1"
        assert result[0]["content"][1]["type"] == "tool_result"
        assert result[0]["content"][1]["tool_use_id"] == "tc-2"

    def test_tool_result_with_error(self):
        model = _model()
        ctx = Context(messages=[
            ToolResultMessage(
                tool_call_id="tc-1",
                tool_name="search",
                content=[TextContent(text="Error occurred")],
                is_error=True,
            ),
        ])
        result = convert_messages(model, ctx)
        tr = result[0]["content"][0]
        assert tr["is_error"] is True
        assert tr["content"] == "Error occurred"

    def test_errored_assistant_skipped(self):
        model = _model()
        ctx = Context(messages=[
            UserMessage(content="hello"),
            AssistantMessage(
                content=[TextContent(text="partial")],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
                stop_reason="error",
            ),
        ])
        result = convert_messages(model, ctx)
        assert len(result) == 1
        assert result[0]["role"] == "user"

    def test_convert_tools(self):
        tools = [
            Tool(name="search", description="Search the web", parameters={
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            }),
        ]
        result = convert_tools(tools)
        assert len(result) == 1
        assert result[0]["name"] == "search"
        assert result[0]["description"] == "Search the web"
        assert result[0]["input_schema"]["type"] == "object"


# ── Stop Reason Mapping Tests ───────────────────────────────────


class TestStopReasonMapping:
    def test_end_turn(self):
        assert map_stop_reason("end_turn") == "stop"

    def test_max_tokens(self):
        assert map_stop_reason("max_tokens") == "length"

    def test_tool_use(self):
        assert map_stop_reason("tool_use") == "toolUse"

    def test_refusal(self):
        assert map_stop_reason("refusal") == "error"

    def test_sensitive(self):
        assert map_stop_reason("sensitive") == "error"

    def test_stop_sequence(self):
        assert map_stop_reason("stop_sequence") == "stop"

    def test_none(self):
        assert map_stop_reason(None) == "stop"


# ── Usage Parsing Tests ─────────────────────────────────────────


class TestUsageParsing:
    def test_basic_usage(self):
        model = _model()
        usage = _parse_usage({
            "input_tokens": 100,
            "output_tokens": 50,
        }, model)
        assert usage.input_tokens == 100
        assert usage.output_tokens == 50
        assert usage.total_tokens == 150

    def test_usage_with_cache(self):
        model = _model()
        usage = _parse_usage({
            "input_tokens": 100,
            "output_tokens": 50,
            "cache_read_input_tokens": 200,
            "cache_creation_input_tokens": 30,
        }, model)
        assert usage.cache_read_tokens == 200
        assert usage.cache_write_tokens == 30
        assert usage.total_tokens == 380  # 100 + 50 + 200 + 30

    def test_usage_merging(self):
        model = _model()
        existing = Usage(input_tokens=100, output_tokens=10, total_tokens=110)
        updated = _parse_usage({"output_tokens": 50}, model, existing)
        # input_tokens should be preserved from existing
        assert updated.input_tokens == 100
        assert updated.output_tokens == 50

    def test_cost_calculation(self):
        model = _model()
        usage = _parse_usage({
            "input_tokens": 1_000_000,
            "output_tokens": 1_000_000,
        }, model)
        assert usage.cost is not None
        assert usage.cost.input == 3.0  # 1M * $3/M
        assert usage.cost.output == 15.0  # 1M * $15/M


# ── Error Classification Tests ──────────────────────────────────


class TestErrorClassification:
    def test_auth_failure(self):
        err = _classify_error(401, '{"error": {"message": "Invalid API key"}}', "anthropic")
        assert err.category.value == "auth_failure"
        assert err.message == "Invalid API key"

    def test_rate_limited(self):
        err = _classify_error(429, '{"error": {"message": "Rate limit exceeded"}}', "anthropic")
        assert err.category.value == "rate_limited"
        assert err.retryable is True

    def test_context_overflow(self):
        err = _classify_error(400, '{"error": {"message": "Prompt exceeds context window"}}', "anthropic")
        assert err.category.value == "context_overflow"

    def test_overloaded(self):
        err = _classify_error(529, "Overloaded", "anthropic")
        assert err.category.value == "rate_limited"
        assert err.retryable is True

    def test_server_error(self):
        err = _classify_error(500, "Internal error", "anthropic")
        assert err.category.value == "server_error"
        assert err.retryable is True


# ── Stream State Machine Tests ──────────────────────────────────


class TestStreamProcessing:
    def test_message_start(self):
        state, stream, model = _make_state()
        _process_event("message_start", {
            "type": "message_start",
            "message": {
                "id": "msg_abc123",
                "model": "claude-sonnet-4-20250514",
                "usage": {"input_tokens": 100, "output_tokens": 0},
            },
        }, state, stream, model)

        assert state.saw_message_start is True
        assert state.output.response_id == "msg_abc123"
        assert state.output.usage.input_tokens == 100

        events = stream.collect_available()
        assert len(events) == 1
        assert isinstance(events[0], StreamStart)

    def test_text_block(self):
        state, stream, model = _make_state()

        # Start text block
        _process_event("content_block_start", {
            "index": 0,
            "content_block": {"type": "text", "text": ""},
        }, state, stream, model)

        events = stream.collect_available()
        assert len(events) == 1
        assert isinstance(events[0], TextStart)
        assert events[0].content_index == 0

        # Text delta
        _process_event("content_block_delta", {
            "index": 0,
            "delta": {"type": "text_delta", "text": "Hello "},
        }, state, stream, model)

        events = stream.collect_available()
        assert isinstance(events[0], TextDelta)
        assert events[0].delta == "Hello "

        _process_event("content_block_delta", {
            "index": 0,
            "delta": {"type": "text_delta", "text": "world!"},
        }, state, stream, model)

        # Stop text block
        _process_event("content_block_stop", {"index": 0}, state, stream, model)

        events = stream.collect_available()
        end_event = [e for e in events if isinstance(e, TextEnd)][0]
        assert end_event.text == "Hello world!"
        assert end_event.content_index == 0

        # Check final content
        assert len(state.content_blocks) == 1
        tc = state.content_blocks[0]
        assert isinstance(tc, TextContent)
        assert tc.text == "Hello world!"

    def test_thinking_block(self):
        state, stream, model = _make_state()

        _process_event("content_block_start", {
            "index": 0,
            "content_block": {"type": "thinking", "thinking": ""},
        }, state, stream, model)

        events = stream.collect_available()
        assert isinstance(events[0], ThinkingStart)

        _process_event("content_block_delta", {
            "index": 0,
            "delta": {"type": "thinking_delta", "thinking": "Let me think..."},
        }, state, stream, model)

        events = stream.collect_available()
        assert isinstance(events[0], ThinkingDelta)
        assert events[0].delta == "Let me think..."

        # Signature delta
        _process_event("content_block_delta", {
            "index": 0,
            "delta": {"type": "signature_delta", "signature": "sig_abc"},
        }, state, stream, model)

        _process_event("content_block_stop", {"index": 0}, state, stream, model)

        events = stream.collect_available()
        end_event = [e for e in events if isinstance(e, ThinkingEnd)][0]
        assert end_event.text == "Let me think..."

        tc = state.content_blocks[0]
        assert isinstance(tc, ThinkingContent)
        assert tc.thinking == "Let me think..."
        assert tc.signature == "sig_abc"

    def test_redacted_thinking_block(self):
        state, stream, model = _make_state()

        _process_event("content_block_start", {
            "index": 0,
            "content_block": {"type": "redacted_thinking", "data": "opaque_data_here"},
        }, state, stream, model)

        events = stream.collect_available()
        assert isinstance(events[0], ThinkingStart)

        _process_event("content_block_stop", {"index": 0}, state, stream, model)

        tc = state.content_blocks[0]
        assert isinstance(tc, ThinkingContent)
        assert tc.redacted is True
        assert tc.signature == "opaque_data_here"

    def test_tool_call_block(self):
        state, stream, model = _make_state()

        _process_event("content_block_start", {
            "index": 0,
            "content_block": {"type": "tool_use", "id": "toolu_123", "name": "search", "input": {}},
        }, state, stream, model)

        events = stream.collect_available()
        assert isinstance(events[0], ToolCallStart)

        _process_event("content_block_delta", {
            "index": 0,
            "delta": {"type": "input_json_delta", "partial_json": '{"query":'},
        }, state, stream, model)

        events = stream.collect_available()
        assert isinstance(events[0], ToolCallDelta)
        assert events[0].delta == '{"query":'

        _process_event("content_block_delta", {
            "index": 0,
            "delta": {"type": "input_json_delta", "partial_json": ' "test"}'},
        }, state, stream, model)

        _process_event("content_block_stop", {"index": 0}, state, stream, model)

        events = stream.collect_available()
        end_event = [e for e in events if isinstance(e, ToolCallEnd)][0]
        assert end_event.tool_call.id == "toolu_123"
        assert end_event.tool_call.name == "search"
        assert end_event.tool_call.arguments == {"query": "test"}

    def test_message_delta_with_stop_reason(self):
        state, stream, model = _make_state()

        _process_event("message_delta", {
            "delta": {"stop_reason": "end_turn"},
            "usage": {"output_tokens": 42},
        }, state, stream, model)

        assert state.output.stop_reason == "stop"
        assert state.output.usage.output_tokens == 42

    def test_message_stop(self):
        state, stream, model = _make_state()

        _process_event("message_stop", {}, state, stream, model)

        assert state.saw_message_stop is True

    def test_tool_use_stop_reason(self):
        state, stream, model = _make_state()

        _process_event("message_delta", {
            "delta": {"stop_reason": "tool_use"},
            "usage": {"output_tokens": 10},
        }, state, stream, model)

        assert state.output.stop_reason == "toolUse"

    def test_error_event_raises(self):
        state, stream, model = _make_state()

        with pytest.raises(RuntimeError, match="Anthropic SSE error"):
            _process_event("error", {"raw": "overloaded"}, state, stream, model)

    def test_multiple_content_blocks(self):
        """Test text + tool_use in the same response."""
        state, stream, model = _make_state()

        # Text block at index 0
        _process_event("content_block_start", {
            "index": 0,
            "content_block": {"type": "text", "text": ""},
        }, state, stream, model)
        _process_event("content_block_delta", {
            "index": 0,
            "delta": {"type": "text_delta", "text": "I'll search for that."},
        }, state, stream, model)
        _process_event("content_block_stop", {"index": 0}, state, stream, model)

        # Tool use block at index 1
        _process_event("content_block_start", {
            "index": 1,
            "content_block": {"type": "tool_use", "id": "toolu_1", "name": "search", "input": {}},
        }, state, stream, model)
        _process_event("content_block_delta", {
            "index": 1,
            "delta": {"type": "input_json_delta", "partial_json": '{"q": "hello"}'},
        }, state, stream, model)
        _process_event("content_block_stop", {"index": 1}, state, stream, model)

        assert len(state.content_blocks) == 2
        assert isinstance(state.content_blocks[0], TextContent)
        assert state.content_blocks[0].text == "I'll search for that."
        assert isinstance(state.content_blocks[1], ToolCall)
        assert state.content_blocks[1].name == "search"
        assert state.content_blocks[1].arguments == {"q": "hello"}

    def test_thinking_then_text(self):
        """Test thinking block followed by text block."""
        state, stream, model = _make_state()

        # Thinking at index 0
        _process_event("content_block_start", {
            "index": 0,
            "content_block": {"type": "thinking", "thinking": ""},
        }, state, stream, model)
        _process_event("content_block_delta", {
            "index": 0,
            "delta": {"type": "thinking_delta", "thinking": "I need to consider..."},
        }, state, stream, model)
        _process_event("content_block_delta", {
            "index": 0,
            "delta": {"type": "signature_delta", "signature": "sig_xyz"},
        }, state, stream, model)
        _process_event("content_block_stop", {"index": 0}, state, stream, model)

        # Text at index 1
        _process_event("content_block_start", {
            "index": 1,
            "content_block": {"type": "text", "text": ""},
        }, state, stream, model)
        _process_event("content_block_delta", {
            "index": 1,
            "delta": {"type": "text_delta", "text": "The answer is 42."},
        }, state, stream, model)
        _process_event("content_block_stop", {"index": 1}, state, stream, model)

        assert len(state.content_blocks) == 2
        think = state.content_blocks[0]
        assert isinstance(think, ThinkingContent)
        assert think.thinking == "I need to consider..."
        assert think.signature == "sig_xyz"
        text = state.content_blocks[1]
        assert isinstance(text, TextContent)
        assert text.text == "The answer is 42."

    def test_response_model_tracking(self):
        """When API returns a different model ID, it's tracked."""
        state, stream, model = _make_state()

        _process_event("message_start", {
            "message": {
                "id": "msg_1",
                "model": "claude-sonnet-4-20250514-v2",
                "usage": {"input_tokens": 10, "output_tokens": 0},
            },
        }, state, stream, model)

        assert state.output.response_model == "claude-sonnet-4-20250514-v2"


# ── Build Params Tests ──────────────────────────────────────────


class TestBuildParams:
    def test_basic_params(self):
        model = _model()
        ctx = Context(
            system_prompt="You are helpful.",
            messages=[UserMessage(content="Hello")],
        )
        params = _build_params(model, ctx, None)

        assert params["model"] == "claude-sonnet-4-20250514"
        assert params["stream"] is True
        assert params["max_tokens"] == 8192
        assert params["system"][0]["text"] == "You are helpful."
        assert len(params["messages"]) == 1

    def test_with_tools(self):
        model = _model()
        ctx = Context(
            messages=[UserMessage(content="Search for something")],
            tools=[Tool(
                name="search",
                description="Search",
                parameters={"type": "object", "properties": {}},
            )],
        )
        params = _build_params(model, ctx, None)
        assert "tools" in params
        assert params["tools"][0]["name"] == "search"

    def test_no_thinking_for_non_reasoning(self):
        model = _model(reasoning=False)
        ctx = Context(messages=[UserMessage(content="Hello")])
        params = _build_params(model, ctx, None)
        assert "thinking" not in params

    def test_thinking_disabled_by_default_for_reasoning_model(self):
        model = _model(reasoning=True)
        ctx = Context(messages=[UserMessage(content="Hello")])
        params = _build_params(model, ctx, None)
        assert params["thinking"]["type"] == "disabled"


# ── API Key Resolution Tests ────────────────────────────────────


class TestAPIKeyResolution:
    def test_from_options(self):
        from dino_ai.options import StreamOptions

        model = _model()
        opts = StreamOptions(api_key="sk-ant-test123")
        assert _get_api_key(model, opts) == "sk-ant-test123"

    def test_from_env(self, monkeypatch: pytest.MonkeyPatch):
        model = _model()
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-env-key")
        assert _get_api_key(model, None) == "sk-env-key"

    def test_provider_specific_env(self, monkeypatch: pytest.MonkeyPatch):
        model = _model(provider="my-anthropic")
        monkeypatch.setenv("MY_ANTHROPIC_API_KEY", "sk-custom")
        assert _get_api_key(model, None) == "sk-custom"

    def test_empty_when_missing(self, monkeypatch: pytest.MonkeyPatch):
        model = _model()
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
        assert _get_api_key(model, None) == ""
