"""Tests for AWS Bedrock Converse Stream provider — unit tests via _process_event."""

from __future__ import annotations

import pytest

from dino_ai.content import ImageContent, TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context, Tool, ToolResultMessage, UserMessage
from dino_ai.events import (
    TextEnd,
    ThinkingEnd,
    ToolCallEnd,
)
from dino_ai.model import Model, ModelCapabilities, ModelLimits, ModelPricing
from dino_ai.options import StreamOptions
from dino_ai.providers.bedrock import (
    _build_params,
    _classify_error,
    _parse_usage,
    _process_event,
    _resolve_region,
    _StreamState,
)
from dino_ai.providers.bedrock_messages import (
    convert_messages,
    convert_system,
    convert_tools,
    map_stop_reason,
)
from dino_ai.usage import Usage

# ── Helpers ──────────────────────────────────────────────────────


def _model(
    model_id: str = "anthropic.claude-sonnet-4-20250514-v1:0",
    provider: str = "bedrock",
    api: str = "bedrock-converse-stream",
    reasoning: bool = False,
    vision: bool = True,
) -> Model:
    return Model(
        id=model_id,
        name="Claude Sonnet 4 (Bedrock)",
        api=api,
        provider=provider,
        base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
        capabilities=ModelCapabilities(reasoning=reasoning, vision=vision),
        limits=ModelLimits(context_window=200000, max_output_tokens=8192),
        pricing=ModelPricing(input=3.0, output=15.0, cache_read=0.3, cache_write=3.75),
    )


def _make_state(model: Model | None = None) -> tuple[_StreamState, list, Model]:
    """Create state and a list-based push collector."""
    m = model or _model()
    output = AssistantMessage(
        model=m.id,
        provider=m.provider,
        api="bedrock-converse-stream",
        usage=Usage(),
        stop_reason="stop",
    )
    state = _StreamState(output)
    events: list = []
    return state, events, m


# ── System Prompt Tests ─────────────────────────────────────────


class TestBedrockSystemPrompt:
    def test_has_system_prompt(self):
        ctx = Context(system_prompt="You are helpful.", messages=[])
        result = convert_system(ctx)
        assert result is not None
        assert result[0]["text"] == "You are helpful."

    def test_no_system_prompt(self):
        ctx = Context(messages=[])
        assert convert_system(ctx) is None


# ── Message Conversion Tests ────────────────────────────────────


class TestBedrockMessageConversion:
    def test_user_text(self):
        m = _model()
        ctx = Context(messages=[UserMessage(content="Hello")])
        result = convert_messages(m, ctx)
        assert result[0]["role"] == "user"
        assert result[0]["content"] == [{"text": "Hello"}]

    def test_user_image(self):
        m = _model()
        ctx = Context(messages=[
            UserMessage(content=[
                TextContent(text="Describe this"),
                ImageContent(data=b"\x89PNG", mime_type="image/png"),
            ])
        ])
        result = convert_messages(m, ctx)
        parts = result[0]["content"]
        assert len(parts) == 2
        assert parts[0] == {"text": "Describe this"}
        assert parts[1]["image"]["format"] == "png"
        assert parts[1]["image"]["source"]["bytes"] == b"\x89PNG"

    def test_user_image_non_vision_model(self):
        m = Model(
            id="test",
            name="Test",
            api="bedrock-converse-stream",
            provider="bedrock",
            base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
            capabilities=ModelCapabilities(vision=False),
            limits=ModelLimits(),
        )
        ctx = Context(messages=[
            UserMessage(content=[
                ImageContent(data=b"\x89PNG", mime_type="image/png"),
            ])
        ])
        result = convert_messages(m, ctx)
        parts = result[0]["content"]
        assert len(parts) == 1
        assert "omitted" in parts[0]["text"]

    def test_assistant_text(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[TextContent(text="I can help")],
                model=m.id,
                provider=m.provider,
                api=m.api,
            ),
        ])
        result = convert_messages(m, ctx)
        assert result[0]["role"] == "assistant"
        assert result[0]["content"][0] == {"text": "I can help"}

    def test_assistant_thinking_same_model(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Let me think...", signature="sig123"),
                    TextContent(text="Answer"),
                ],
                model=m.id,
                provider=m.provider,
                api=m.api,
            ),
        ])
        result = convert_messages(m, ctx)
        blocks = result[0]["content"]
        assert blocks[0]["reasoningContent"]["reasoningText"]["text"] == "Let me think..."
        assert blocks[0]["reasoningContent"]["reasoningText"]["signature"] == "sig123"
        assert blocks[1] == {"text": "Answer"}

    def test_assistant_thinking_cross_model(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Cross-model thought", signature="sig"),
                    TextContent(text="Answer"),
                ],
                model="different-model",
                provider="other",
                api="other",
            ),
        ])
        result = convert_messages(m, ctx)
        blocks = result[0]["content"]
        # Cross-model thinking becomes plain text
        assert blocks[0] == {"text": "Cross-model thought"}
        assert blocks[1] == {"text": "Answer"}

    def test_assistant_redacted_thinking_skipped(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="[redacted]", signature="data", redacted=True),
                    TextContent(text="Answer"),
                ],
                model="other",
                provider="other",
                api="other",
            ),
        ])
        result = convert_messages(m, ctx)
        blocks = result[0]["content"]
        assert len(blocks) == 1
        assert blocks[0] == {"text": "Answer"}

    def test_assistant_tool_call(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[ToolCall(id="tc-1", name="search", arguments={"q": "test"})],
                model=m.id,
                provider=m.provider,
                api=m.api,
            ),
        ])
        result = convert_messages(m, ctx)
        tu = result[0]["content"][0]["toolUse"]
        assert tu["toolUseId"] == "tc-1"
        assert tu["name"] == "search"
        assert tu["input"] == {"q": "test"}

    def test_tool_results_batched(self):
        m = _model()
        ctx = Context(messages=[
            ToolResultMessage(
                tool_call_id="tc-1",
                tool_name="search",
                content=[TextContent(text="Found it")],
            ),
            ToolResultMessage(
                tool_call_id="tc-2",
                tool_name="read",
                content=[TextContent(text="Content")],
            ),
        ])
        result = convert_messages(m, ctx)
        assert len(result) == 1
        assert result[0]["role"] == "user"
        assert len(result[0]["content"]) == 2
        assert result[0]["content"][0]["toolResult"]["toolUseId"] == "tc-1"
        assert result[0]["content"][1]["toolResult"]["toolUseId"] == "tc-2"

    def test_tool_result_error(self):
        m = _model()
        ctx = Context(messages=[
            ToolResultMessage(
                tool_call_id="tc-1",
                tool_name="search",
                content=[TextContent(text="Failed")],
                is_error=True,
            ),
        ])
        result = convert_messages(m, ctx)
        tr = result[0]["content"][0]["toolResult"]
        assert tr["status"] == "error"

    def test_errored_assistant_skipped(self):
        m = _model()
        ctx = Context(messages=[
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[TextContent(text="partial")],
                model=m.id,
                provider=m.provider,
                api=m.api,
                stop_reason="error",
            ),
        ])
        result = convert_messages(m, ctx)
        assert len(result) == 1
        assert result[0]["role"] == "user"

    def test_tool_id_normalization(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[ToolCall(id="call.foo/bar:baz", name="test", arguments={})],
                model=m.id,
                provider=m.provider,
                api=m.api,
            ),
        ])
        result = convert_messages(m, ctx)
        tu = result[0]["content"][0]["toolUse"]
        # Dots, slashes, colons should be replaced with underscore
        assert tu["toolUseId"] == "call_foo_bar_baz"


class TestBedrockToolConversion:
    def test_basic_tool(self):
        tools = [Tool(
            name="search",
            description="Search the web",
            parameters={
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        )]
        result = convert_tools(tools)
        assert len(result) == 1
        spec = result[0]["toolSpec"]
        assert spec["name"] == "search"
        assert spec["description"] == "Search the web"
        assert spec["inputSchema"]["json"]["type"] == "object"


class TestStopReasonMapping:
    def test_end_turn(self):
        assert map_stop_reason("end_turn") == "stop"

    def test_stop_sequence(self):
        assert map_stop_reason("stop_sequence") == "stop"

    def test_max_tokens(self):
        assert map_stop_reason("max_tokens") == "length"

    def test_context_exceeded(self):
        assert map_stop_reason("MODEL_CONTEXT_WINDOW_EXCEEDED") == "length"

    def test_tool_use(self):
        assert map_stop_reason("tool_use") == "toolUse"

    def test_none(self):
        assert map_stop_reason(None) == "stop"

    def test_unknown(self):
        assert map_stop_reason("SOMETHING_ELSE") == "error"


# ── Usage Parsing Tests ─────────────────────────────────────────


class TestBedrockUsageParsing:
    def test_basic_usage(self):
        m = _model()
        raw = {
            "inputTokens": 100,
            "outputTokens": 50,
            "totalTokens": 150,
        }
        usage = _parse_usage(raw, m)
        assert usage.input_tokens == 100
        assert usage.output_tokens == 50
        assert usage.total_tokens == 150
        assert usage.cost.total > 0

    def test_usage_with_cache(self):
        m = _model()
        raw = {
            "inputTokens": 100,
            "outputTokens": 50,
            "cacheReadInputTokens": 30,
            "cacheWriteInputTokens": 10,
            "totalTokens": 190,
        }
        usage = _parse_usage(raw, m)
        assert usage.cache_read_tokens == 30
        assert usage.cache_write_tokens == 10

    def test_empty_usage(self):
        m = _model()
        usage = _parse_usage({}, m)
        assert usage.input_tokens == 0
        assert usage.output_tokens == 0


# ── Error Classification Tests ───────────────────────────────────


class TestBedrockErrorClassification:
    def test_throttling(self):
        exc = type("ThrottlingException", (Exception,), {})("Rate exceeded")
        err = _classify_error(exc, "bedrock")
        assert err.category.value == "rate_limited"
        assert err.retryable is True

    def test_validation(self):
        exc = type("ValidationException", (Exception,), {})("Bad request")
        err = _classify_error(exc, "bedrock")
        assert err.category.value == "invalid_request"

    def test_validation_token_limit(self):
        exc = type("ValidationException", (Exception,), {})("Token limit exceeded")
        err = _classify_error(exc, "bedrock")
        assert err.category.value == "context_overflow"

    def test_access_denied(self):
        exc = type("AccessDeniedException", (Exception,), {})("No access")
        err = _classify_error(exc, "bedrock")
        assert err.category.value == "auth_failure"

    def test_internal_server(self):
        exc = type("InternalServerException", (Exception,), {})("Server error")
        err = _classify_error(exc, "bedrock")
        assert err.category.value == "server_error"
        assert err.retryable is True

    def test_not_found(self):
        exc = type("ResourceNotFoundException", (Exception,), {})("Not found")
        err = _classify_error(exc, "bedrock")
        assert err.category.value == "model_not_found"

    def test_generic(self):
        err = _classify_error(RuntimeError("something"), "bedrock")
        assert err.category.value == "unknown"


# ── Region Resolution Tests ─────────────────────────────────────


class TestRegionResolution:
    def test_from_metadata(self):
        m = _model()
        opts = StreamOptions(metadata={"region": "eu-west-1"})
        assert _resolve_region(m, opts) == "eu-west-1"

    def test_from_env(self, monkeypatch: pytest.MonkeyPatch):
        m = _model()
        monkeypatch.setenv("AWS_REGION", "ap-northeast-1")
        assert _resolve_region(m, None) == "ap-northeast-1"

    def test_from_url(self, monkeypatch: pytest.MonkeyPatch):
        m = Model(
            id="test",
            name="Test",
            api="bedrock-converse-stream",
            provider="bedrock",
            base_url="https://bedrock-runtime.us-west-2.amazonaws.com",
            capabilities=ModelCapabilities(),
            limits=ModelLimits(),
        )
        monkeypatch.delenv("AWS_REGION", raising=False)
        monkeypatch.delenv("AWS_DEFAULT_REGION", raising=False)
        assert _resolve_region(m, None) == "us-west-2"

    def test_default_fallback(self, monkeypatch: pytest.MonkeyPatch):
        m = Model(
            id="test",
            name="Test",
            api="bedrock-converse-stream",
            provider="bedrock",
            base_url="https://custom-proxy.example.com",
            capabilities=ModelCapabilities(),
            limits=ModelLimits(),
        )
        monkeypatch.delenv("AWS_REGION", raising=False)
        monkeypatch.delenv("AWS_DEFAULT_REGION", raising=False)
        assert _resolve_region(m, None) == "us-east-1"


# ── Build Params Tests ───────────────────────────────────────────


class TestBedrockBuildParams:
    def test_basic_params(self):
        m = _model()
        ctx = Context(messages=[UserMessage(content="Hello")])
        params = _build_params(m, ctx, None)
        assert params["modelId"] == m.id
        assert params["messages"][0]["content"][0]["text"] == "Hello"

    def test_system_prompt(self):
        m = _model()
        ctx = Context(system_prompt="Be helpful.", messages=[UserMessage(content="Hi")])
        params = _build_params(m, ctx, None)
        assert params["system"][0]["text"] == "Be helpful."

    def test_max_tokens(self):
        m = _model()
        ctx = Context(messages=[UserMessage(content="Hi")])
        params = _build_params(m, ctx, StreamOptions(max_tokens=100))
        assert params["inferenceConfig"]["maxTokens"] == 100

    def test_temperature(self):
        m = _model()
        ctx = Context(messages=[UserMessage(content="Hi")])
        params = _build_params(m, ctx, StreamOptions(temperature=0.5))
        assert params["inferenceConfig"]["temperature"] == 0.5

    def test_tools_included(self):
        m = _model()
        ctx = Context(
            messages=[UserMessage(content="Hi")],
            tools=[Tool(name="search", description="Search", parameters={"type": "object"})],
        )
        params = _build_params(m, ctx, None)
        assert "toolConfig" in params
        assert params["toolConfig"]["tools"][0]["toolSpec"]["name"] == "search"

    def test_thinking_config_reasoning_model(self):
        m = _model(reasoning=True)
        ctx = Context(messages=[UserMessage(content="Think")])
        opts = StreamOptions(metadata={"reasoning_effort": "high"})
        params = _build_params(m, ctx, opts)
        thinking = params["additionalModelRequestFields"]["thinking"]
        assert thinking["type"] == "enabled"
        assert thinking["budget_tokens"] == 16384


# ── Stream State Machine Tests ───────────────────────────────────


class TestBedrockStreamProcessing:
    def test_text_response(self):
        state, events, m = _make_state()
        push = events.append

        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 0,
            "delta": {"text": "Hello"},
        }}, state, push, m)

        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 0,
            "delta": {"text": " world"},
        }}, state, push, m)

        _process_event({"contentBlockStop": {
            "contentBlockIndex": 0,
        }}, state, push, m)

        types = [type(e).__name__ for e in events]
        assert "TextStart" in types
        assert "TextDelta" in types
        assert "TextEnd" in types
        text_end = next(e for e in events if isinstance(e, TextEnd))
        assert text_end.text == "Hello world"

    def test_thinking_response(self):
        state, events, m = _make_state()
        push = events.append

        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 0,
            "delta": {"reasoningContent": {"text": "Thinking..."}},
        }}, state, push, m)

        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 0,
            "delta": {"reasoningContent": {"text": " more", "signature": "sig-abc"}},
        }}, state, push, m)

        _process_event({"contentBlockStop": {
            "contentBlockIndex": 0,
        }}, state, push, m)

        types = [type(e).__name__ for e in events]
        assert "ThinkingStart" in types
        assert "ThinkingDelta" in types
        assert "ThinkingEnd" in types

        thinking_end = next(e for e in events if isinstance(e, ThinkingEnd))
        assert thinking_end.text == "Thinking... more"
        # Signature should be captured
        tc = state.content_blocks[0]
        assert isinstance(tc, ThinkingContent)
        assert tc.signature == "sig-abc"

    def test_tool_call(self):
        state, events, m = _make_state()
        push = events.append

        _process_event({"contentBlockStart": {
            "contentBlockIndex": 0,
            "start": {"toolUse": {"toolUseId": "tc-1", "name": "search"}},
        }}, state, push, m)

        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 0,
            "delta": {"toolUse": {"input": '{"q":'}},
        }}, state, push, m)

        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 0,
            "delta": {"toolUse": {"input": '"test"}'}},
        }}, state, push, m)

        _process_event({"contentBlockStop": {
            "contentBlockIndex": 0,
        }}, state, push, m)

        types = [type(e).__name__ for e in events]
        assert "ToolCallStart" in types
        assert "ToolCallDelta" in types
        assert "ToolCallEnd" in types

        tc_end = next(e for e in events if isinstance(e, ToolCallEnd))
        assert tc_end.tool_call.name == "search"
        assert tc_end.tool_call.arguments == {"q": "test"}
        assert tc_end.tool_call.id == "tc-1"

    def test_thinking_then_text(self):
        state, events, m = _make_state()
        push = events.append

        # Thinking at index 0
        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 0,
            "delta": {"reasoningContent": {"text": "Let me think"}},
        }}, state, push, m)
        _process_event({"contentBlockStop": {"contentBlockIndex": 0}}, state, push, m)

        # Text at index 1
        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 1,
            "delta": {"text": "Answer"},
        }}, state, push, m)
        _process_event({"contentBlockStop": {"contentBlockIndex": 1}}, state, push, m)

        types = [type(e).__name__ for e in events]
        assert types.index("ThinkingEnd") < types.index("TextStart")
        assert len(state.content_blocks) == 2
        assert isinstance(state.content_blocks[0], ThinkingContent)
        assert isinstance(state.content_blocks[1], TextContent)

    def test_usage_metadata(self):
        state, events, m = _make_state()
        push = events.append

        _process_event({"metadata": {
            "usage": {
                "inputTokens": 100,
                "outputTokens": 50,
                "totalTokens": 150,
            }
        }}, state, push, m)

        assert state.output.usage.input_tokens == 100
        assert state.output.usage.output_tokens == 50

    def test_message_stop(self):
        state, events, m = _make_state()
        push = events.append

        _process_event({"messageStop": {"stopReason": "end_turn"}}, state, push, m)
        assert state.output.stop_reason == "stop"

    def test_message_stop_tool_use(self):
        state, events, m = _make_state()
        push = events.append

        _process_event({"messageStop": {"stopReason": "tool_use"}}, state, push, m)
        assert state.output.stop_reason == "toolUse"

    def test_message_stop_max_tokens(self):
        state, events, m = _make_state()
        push = events.append

        _process_event({"messageStop": {"stopReason": "max_tokens"}}, state, push, m)
        assert state.output.stop_reason == "length"

    def test_multiple_tool_calls(self):
        state, events, m = _make_state()
        push = events.append

        # Tool call at index 0
        _process_event({"contentBlockStart": {
            "contentBlockIndex": 0,
            "start": {"toolUse": {"toolUseId": "tc-1", "name": "search"}},
        }}, state, push, m)
        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 0,
            "delta": {"toolUse": {"input": '{"q": "A"}'}},
        }}, state, push, m)
        _process_event({"contentBlockStop": {"contentBlockIndex": 0}}, state, push, m)

        # Tool call at index 1
        _process_event({"contentBlockStart": {
            "contentBlockIndex": 1,
            "start": {"toolUse": {"toolUseId": "tc-2", "name": "read"}},
        }}, state, push, m)
        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 1,
            "delta": {"toolUse": {"input": '{"path": "/x"}'}},
        }}, state, push, m)
        _process_event({"contentBlockStop": {"contentBlockIndex": 1}}, state, push, m)

        tc_ends = [e for e in events if isinstance(e, ToolCallEnd)]
        assert len(tc_ends) == 2
        assert tc_ends[0].tool_call.name == "search"
        assert tc_ends[1].tool_call.name == "read"

    def test_content_blocks_accumulate(self):
        """Thinking, text, and tool call at different indices."""
        state, events, m = _make_state()
        push = events.append

        # Thinking at 0
        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 0,
            "delta": {"reasoningContent": {"text": "Think"}},
        }}, state, push, m)
        _process_event({"contentBlockStop": {"contentBlockIndex": 0}}, state, push, m)

        # Text at 1
        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 1,
            "delta": {"text": "Hello"},
        }}, state, push, m)
        _process_event({"contentBlockStop": {"contentBlockIndex": 1}}, state, push, m)

        # Tool at 2
        _process_event({"contentBlockStart": {
            "contentBlockIndex": 2,
            "start": {"toolUse": {"toolUseId": "tc-1", "name": "act"}},
        }}, state, push, m)
        _process_event({"contentBlockDelta": {
            "contentBlockIndex": 2,
            "delta": {"toolUse": {"input": "{}"}},
        }}, state, push, m)
        _process_event({"contentBlockStop": {"contentBlockIndex": 2}}, state, push, m)

        assert len(state.content_blocks) == 3
        assert isinstance(state.content_blocks[0], ThinkingContent)
        assert isinstance(state.content_blocks[1], TextContent)
        assert isinstance(state.content_blocks[2], ToolCall)
