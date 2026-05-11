"""Tests for Google Gemini provider — unit tests via _process_chunk."""

from __future__ import annotations

import pytest

from dino_ai.content import ImageContent, TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context, Tool, ToolResultMessage, UserMessage
from dino_ai.events import TextEnd, ThinkingEnd, ToolCallEnd
from dino_ai.model import Model, ModelCapabilities, ModelLimits, ModelPricing
from dino_ai.providers.google import (
    _build_params,
    _classify_error,
    _end_current_block,
    _get_api_key,
    _parse_usage,
    _process_chunk,
    _StreamState,
)
from dino_ai.providers.google_messages import convert_messages, convert_system, convert_tools, map_stop_reason
from dino_ai.stream import EventStream
from dino_ai.usage import Usage

# ── Helpers ──────────────────────────────────────────────────────


def _model(
    model_id: str = "gemini-2.5-flash",
    provider: str = "google",
    api: str = "google-generative-ai",
    reasoning: bool = False,
    vision: bool = True,
) -> Model:
    return Model(
        id=model_id,
        name="Gemini 2.5 Flash",
        api=api,
        provider=provider,
        base_url="https://generativelanguage.googleapis.com/v1beta",
        capabilities=ModelCapabilities(reasoning=reasoning, vision=vision),
        limits=ModelLimits(context_window=1048576, max_output_tokens=65536),
        pricing=ModelPricing(input=0.15, output=0.60, cache_read=0.0375),
    )


def _make_state(model: Model | None = None) -> tuple[_StreamState, EventStream, Model]:
    m = model or _model()
    output = AssistantMessage(
        model=m.id,
        provider=m.provider,
        api="google-generative-ai",
        usage=Usage(),
        stop_reason="stop",
    )
    state = _StreamState(output)
    stream = EventStream()
    return state, stream, m


# ── Message Conversion Tests ────────────────────────────────────


class TestGeminiSystemInstruction:
    def test_has_system_prompt(self):
        ctx = Context(system_prompt="You are helpful.", messages=[])
        result = convert_system(ctx)
        assert result == "You are helpful."

    def test_no_system_prompt(self):
        ctx = Context(messages=[])
        assert convert_system(ctx) is None


class TestGeminiMessageConversion:
    def test_user_text_message(self):
        m = _model()
        ctx = Context(messages=[UserMessage(content="Hello")])
        result = convert_messages(m, ctx)
        assert result[0]["role"] == "user"
        assert result[0]["parts"] == [{"text": "Hello"}]

    def test_user_image_message(self):
        m = _model()
        ctx = Context(messages=[
            UserMessage(content=[
                TextContent(text="Describe this"),
                ImageContent(data=b"\x89PNG", mime_type="image/png"),
            ])
        ])
        result = convert_messages(m, ctx)
        parts = result[0]["parts"]
        assert len(parts) == 2
        assert parts[0] == {"text": "Describe this"}
        assert parts[1]["inlineData"]["mimeType"] == "image/png"

    def test_assistant_text_message(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[TextContent(text="I can help")],
                model="gemini-2.5-flash",
                provider="google",
                api="google-generative-ai",
            ),
        ])
        result = convert_messages(m, ctx)
        assert result[0]["role"] == "model"
        assert result[0]["parts"][0] == {"text": "I can help"}

    def test_assistant_thinking_same_model(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Let me reason...", signature="sig123"),
                    TextContent(text="Answer"),
                ],
                model="gemini-2.5-flash",
                provider="google",
                api="google-generative-ai",
            ),
        ])
        result = convert_messages(m, ctx)
        parts = result[0]["parts"]
        assert parts[0]["text"] == "Let me reason..."
        assert parts[0]["thought"] is True
        assert parts[0]["thoughtSignature"] == "sig123"
        assert parts[1] == {"text": "Answer"}

    def test_assistant_thinking_cross_model_becomes_text(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Let me reason...", signature="sig123"),
                    TextContent(text="Answer"),
                ],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ])
        result = convert_messages(m, ctx)
        parts = result[0]["parts"]
        # Cross-model thinking becomes plain text
        assert parts[0] == {"text": "Let me reason..."}
        assert parts[1] == {"text": "Answer"}

    def test_assistant_redacted_thinking_skipped(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="[redacted]", signature="data", redacted=True),
                    TextContent(text="Answer"),
                ],
                model="other-model",
                provider="other",
                api="other",
            ),
        ])
        result = convert_messages(m, ctx)
        parts = result[0]["parts"]
        # Redacted thinking from different model is skipped
        assert len(parts) == 1
        assert parts[0] == {"text": "Answer"}

    def test_assistant_tool_call(self):
        m = _model()
        ctx = Context(messages=[
            AssistantMessage(
                content=[ToolCall(id="tc-1", name="search", arguments={"q": "test"})],
                model="gemini-2.5-flash",
                provider="google",
                api="google-generative-ai",
            ),
        ])
        result = convert_messages(m, ctx)
        parts = result[0]["parts"]
        assert parts[0]["functionCall"]["name"] == "search"
        assert parts[0]["functionCall"]["args"] == {"q": "test"}

    def test_tool_results_batched(self):
        m = _model()
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
        result = convert_messages(m, ctx)
        assert len(result) == 1
        assert result[0]["role"] == "user"
        assert len(result[0]["parts"]) == 2
        assert result[0]["parts"][0]["functionResponse"]["name"] == "search"
        assert result[0]["parts"][0]["functionResponse"]["response"] == {"output": "Found 5 results"}
        assert result[0]["parts"][1]["functionResponse"]["name"] == "read"
        assert result[0]["parts"][1]["functionResponse"]["response"] == {"output": "File contents"}

    def test_tool_result_error(self):
        m = _model()
        ctx = Context(messages=[
            ToolResultMessage(
                tool_call_id="tc-1",
                tool_name="search",
                content=[TextContent(text="Not found")],
                is_error=True,
            ),
        ])
        result = convert_messages(m, ctx)
        resp = result[0]["parts"][0]["functionResponse"]["response"]
        assert resp == {"error": "Not found"}

    def test_errored_assistant_skipped(self):
        m = _model()
        ctx = Context(messages=[
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[TextContent(text="partial")],
                model="gemini-2.5-flash",
                provider="google",
                api="google-generative-ai",
                stop_reason="error",
            ),
        ])
        result = convert_messages(m, ctx)
        assert len(result) == 1
        assert result[0]["role"] == "user"

    def test_empty_assistant_content_skipped(self):
        m = _model()
        ctx = Context(messages=[
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[],
                model="gemini-2.5-flash",
                provider="google",
                api="google-generative-ai",
            ),
        ])
        result = convert_messages(m, ctx)
        assert len(result) == 1
        assert result[0]["role"] == "user"


class TestGeminiToolConversion:
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
        decls = result[0]["functionDeclarations"]
        assert len(decls) == 1
        assert decls[0]["name"] == "search"
        assert decls[0]["description"] == "Search the web"
        assert decls[0]["parametersJsonSchema"]["type"] == "object"

    def test_tool_empty_parameters(self):
        tools = [Tool(name="status", description="Get status", parameters={})]
        result = convert_tools(tools)
        decls = result[0]["functionDeclarations"]
        # Empty parameters dict is falsy, so no parametersJsonSchema
        assert "parametersJsonSchema" not in decls[0]


class TestStopReasonMapping:
    def test_stop(self):
        assert map_stop_reason("STOP") == "stop"

    def test_max_tokens(self):
        assert map_stop_reason("MAX_TOKENS") == "length"

    def test_safety(self):
        assert map_stop_reason("SAFETY") == "error"

    def test_none(self):
        assert map_stop_reason(None) == "stop"

    def test_unknown(self):
        assert map_stop_reason("BLOCKLIST") == "error"


# ── Usage Parsing Tests ─────────────────────────────────────────


class TestUsageParsing:
    def test_basic_usage(self):
        m = _model()
        raw = {
            "promptTokenCount": 100,
            "candidatesTokenCount": 50,
            "totalTokenCount": 150,
        }
        usage = _parse_usage(raw, m)
        assert usage.input_tokens == 100
        assert usage.output_tokens == 50
        assert usage.total_tokens == 150
        assert usage.cost.total > 0

    def test_usage_with_cache(self):
        m = _model()
        raw = {
            "promptTokenCount": 100,
            "candidatesTokenCount": 50,
            "cachedContentTokenCount": 30,
            "totalTokenCount": 180,
        }
        usage = _parse_usage(raw, m)
        assert usage.input_tokens == 70  # 100 - 30
        assert usage.output_tokens == 50
        assert usage.cache_read_tokens == 30
        assert usage.total_tokens == 180

    def test_usage_with_thoughts(self):
        m = _model()
        raw = {
            "promptTokenCount": 100,
            "candidatesTokenCount": 50,
            "thoughtsTokenCount": 200,
            "totalTokenCount": 350,
        }
        usage = _parse_usage(raw, m)
        assert usage.output_tokens == 250  # 50 + 200

    def test_empty_usage(self):
        m = _model()
        usage = _parse_usage({}, m)
        assert usage.input_tokens == 0
        assert usage.output_tokens == 0


# ── Error Classification Tests ───────────────────────────────────


class TestErrorClassification:
    def test_auth_error(self):
        err = _classify_error(401, '{"error": {"message": "Invalid API key"}}', "google")
        assert err.category.value == "auth_failure"
        assert err.status_code == 401

    def test_forbidden(self):
        err = _classify_error(403, '{"error": {"message": "Forbidden"}}', "google")
        assert err.category.value == "auth_failure"

    def test_rate_limited(self):
        err = _classify_error(429, '{"error": {"message": "Quota exceeded"}}', "google")
        assert err.category.value == "rate_limited"
        assert err.retryable is True

    def test_context_overflow(self):
        err = _classify_error(400, '{"error": {"message": "Token limit exceeded"}}', "google")
        assert err.category.value == "context_overflow"

    def test_content_filtered(self):
        err = _classify_error(400, '{"error": {"message": "Response was blocked for safety"}}', "google")
        assert err.category.value == "content_filtered"

    def test_not_found(self):
        err = _classify_error(404, '{"error": {"message": "Model not found"}}', "google")
        assert err.category.value == "model_not_found"

    def test_server_error(self):
        err = _classify_error(500, "Internal Server Error", "google")
        assert err.category.value == "server_error"
        assert err.retryable is True


# ── API Key Resolution Tests ────────────────────────────────────


class TestApiKeyResolution:
    def test_from_options(self):
        from dino_ai.options import StreamOptions
        m = _model()
        key = _get_api_key(m, StreamOptions(api_key="test-key"))
        assert key == "test-key"

    def test_from_env(self, monkeypatch: pytest.MonkeyPatch):
        m = _model()
        monkeypatch.setenv("GOOGLE_API_KEY", "env-key")
        key = _get_api_key(m, None)
        assert key == "env-key"

    def test_gemini_env(self, monkeypatch: pytest.MonkeyPatch):
        m = _model()
        monkeypatch.setenv("GEMINI_API_KEY", "gemini-key")
        key = _get_api_key(m, None)
        assert key == "gemini-key"

    def test_no_key_returns_empty(self, monkeypatch: pytest.MonkeyPatch):
        m = _model()
        monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
        monkeypatch.delenv("GEMINI_API_KEY", raising=False)
        key = _get_api_key(m, None)
        assert key == ""


# ── Build Params Tests ───────────────────────────────────────────


class TestBuildParams:
    def test_basic_params(self):
        m = _model()
        ctx = Context(messages=[UserMessage(content="Hello")])
        params = _build_params(m, ctx, None)
        assert "contents" in params
        assert params["contents"][0]["parts"][0]["text"] == "Hello"

    def test_system_instruction(self):
        m = _model()
        ctx = Context(system_prompt="Be helpful.", messages=[UserMessage(content="Hi")])
        params = _build_params(m, ctx, None)
        assert params["generationConfig"]["systemInstruction"] == "Be helpful."

    def test_max_tokens(self):
        from dino_ai.options import StreamOptions
        m = _model()
        ctx = Context(messages=[UserMessage(content="Hi")])
        params = _build_params(m, ctx, StreamOptions(max_tokens=100))
        assert params["generationConfig"]["maxOutputTokens"] == 100

    def test_temperature(self):
        from dino_ai.options import StreamOptions
        m = _model()
        ctx = Context(messages=[UserMessage(content="Hi")])
        params = _build_params(m, ctx, StreamOptions(temperature=0.5))
        assert params["generationConfig"]["temperature"] == 0.5

    def test_tools_included(self):
        m = _model()
        ctx = Context(
            messages=[UserMessage(content="Hi")],
            tools=[Tool(name="search", description="Search", parameters={"type": "object"})],
        )
        params = _build_params(m, ctx, None)
        assert "tools" in params
        assert params["tools"][0]["functionDeclarations"][0]["name"] == "search"


# ── Stream State Machine Tests ───────────────────────────────────


class TestStreamProcessing:
    def test_text_response(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{"content": {"parts": [{"text": "Hello"}]}}],
        }, state, stream, m)
        _process_chunk({
            "candidates": [{"content": {"parts": [{"text": " world"}]}}],
        }, state, stream, m)
        _end_current_block(state, stream)

        events = stream.collect_available()
        types = [type(e).__name__ for e in events]
        assert "TextStart" in types
        assert "TextDelta" in types
        assert "TextEnd" in types
        # Check accumulated text
        text_end = next(e for e in events if isinstance(e, TextEnd))
        assert text_end.text == "Hello world"

    def test_thinking_response(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{"content": {"parts": [{"text": "Reasoning...", "thought": True}]}}],
        }, state, stream, m)
        _process_chunk({
            "candidates": [{"content": {"parts": [{"text": " more", "thought": True}]}}],
        }, state, stream, m)
        _end_current_block(state, stream)

        events = stream.collect_available()
        types = [type(e).__name__ for e in events]
        assert "ThinkingStart" in types
        assert "ThinkingDelta" in types
        assert "ThinkingEnd" in types
        thinking_end = next(e for e in events if isinstance(e, ThinkingEnd))
        assert thinking_end.text == "Reasoning... more"

    def test_thinking_then_text(self):
        state, stream, m = _make_state()
        # Thinking part
        _process_chunk({
            "candidates": [{"content": {"parts": [{"text": "Let me think...", "thought": True}]}}],
        }, state, stream, m)
        # Then text part
        _process_chunk({
            "candidates": [{"content": {"parts": [{"text": "Answer"}]}}],
        }, state, stream, m)
        _end_current_block(state, stream)

        events = stream.collect_available()
        types = [type(e).__name__ for e in events]
        # Should have thinking start/delta/end then text start/delta/end
        assert types.index("ThinkingEnd") < types.index("TextStart")
        assert len(state.content_blocks) == 2
        assert isinstance(state.content_blocks[0], ThinkingContent)
        assert isinstance(state.content_blocks[1], TextContent)

    def test_function_call(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{
                "content": {
                    "parts": [{
                        "functionCall": {"name": "search", "args": {"q": "test"}}
                    }]
                }
            }],
        }, state, stream, m)

        events = stream.collect_available()
        types = [type(e).__name__ for e in events]
        assert "ToolCallStart" in types
        assert "ToolCallDelta" in types
        assert "ToolCallEnd" in types
        tc_end = next(e for e in events if isinstance(e, ToolCallEnd))
        assert tc_end.tool_call.name == "search"
        assert tc_end.tool_call.arguments == {"q": "test"}
        # Stop reason should be toolUse
        assert state.output.stop_reason == "toolUse"

    def test_multiple_function_calls(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{
                "content": {
                    "parts": [
                        {"functionCall": {"name": "search", "args": {"q": "A"}}},
                        {"functionCall": {"name": "read", "args": {"path": "/x"}}},
                    ]
                }
            }],
        }, state, stream, m)

        events = stream.collect_available()
        tc_ends = [e for e in events if isinstance(e, ToolCallEnd)]
        assert len(tc_ends) == 2
        assert tc_ends[0].tool_call.name == "search"
        assert tc_ends[1].tool_call.name == "read"

    def test_usage_metadata(self):
        state, stream, m = _make_state()
        _process_chunk({
            "usageMetadata": {
                "promptTokenCount": 100,
                "candidatesTokenCount": 50,
                "totalTokenCount": 150,
            },
            "candidates": [{"content": {"parts": [{"text": "Hi"}]}}],
        }, state, stream, m)

        assert state.output.usage.input_tokens == 100
        assert state.output.usage.output_tokens == 50

    def test_response_id(self):
        state, stream, m = _make_state()
        _process_chunk({
            "responseId": "resp-123",
            "candidates": [{"content": {"parts": [{"text": "Hi"}]}}],
        }, state, stream, m)

        assert state.response_id == "resp-123"
        assert state.output.response_id == "resp-123"

    def test_finish_reason_stop(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{
                "content": {"parts": [{"text": "Done"}]},
                "finishReason": "STOP",
            }],
        }, state, stream, m)
        assert state.output.stop_reason == "stop"

    def test_finish_reason_max_tokens(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{
                "content": {"parts": [{"text": "Trunc"}]},
                "finishReason": "MAX_TOKENS",
            }],
        }, state, stream, m)
        assert state.output.stop_reason == "length"

    def test_finish_reason_safety(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{
                "content": {"parts": []},
                "finishReason": "SAFETY",
            }],
        }, state, stream, m)
        assert state.output.stop_reason == "error"

    def test_text_then_function_call(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{"content": {"parts": [{"text": "I'll search for that."}]}}],
        }, state, stream, m)
        _process_chunk({
            "candidates": [{
                "content": {
                    "parts": [{"functionCall": {"name": "search", "args": {"q": "test"}}}]
                }
            }],
        }, state, stream, m)

        events = stream.collect_available()
        types = [type(e).__name__ for e in events]
        # Text should end before tool call starts
        assert types.index("TextEnd") < types.index("ToolCallStart")
        assert len(state.content_blocks) == 2
        assert isinstance(state.content_blocks[0], TextContent)
        assert isinstance(state.content_blocks[1], ToolCall)

    def test_thinking_with_signature(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{
                "content": {
                    "parts": [{
                        "text": "Deep thought",
                        "thought": True,
                        "thoughtSignature": "sig-abc",
                    }]
                }
            }],
        }, state, stream, m)
        _end_current_block(state, stream)

        assert len(state.content_blocks) == 1
        tc = state.content_blocks[0]
        assert isinstance(tc, ThinkingContent)
        assert tc.thinking == "Deep thought"
        assert tc.signature == "sig-abc"

    def test_empty_candidates_ignored(self):
        state, stream, m = _make_state()
        _process_chunk({"usageMetadata": {"promptTokenCount": 10}}, state, stream, m)
        events = stream.collect_available()
        assert len(events) == 0
        assert len(state.content_blocks) == 0

    def test_function_call_gets_generated_id(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{
                "content": {
                    "parts": [{"functionCall": {"name": "search", "args": {}}}]
                }
            }],
        }, state, stream, m)

        assert len(state.content_blocks) == 1
        tc = state.content_blocks[0]
        assert isinstance(tc, ToolCall)
        assert tc.id.startswith("search_")

    def test_function_call_with_explicit_id(self):
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{
                "content": {
                    "parts": [{
                        "functionCall": {"name": "search", "args": {}, "id": "call-123"}
                    }]
                }
            }],
        }, state, stream, m)

        tc = state.content_blocks[0]
        assert isinstance(tc, ToolCall)
        assert tc.id == "call-123"

    def test_content_blocks_accumulate_correctly(self):
        """Multiple different block types accumulate in order."""
        state, stream, m = _make_state()
        # Thinking
        _process_chunk({
            "candidates": [{"content": {"parts": [{"text": "Think", "thought": True}]}}],
        }, state, stream, m)
        # Text
        _process_chunk({
            "candidates": [{"content": {"parts": [{"text": "Answer"}]}}],
        }, state, stream, m)
        # Tool call
        _process_chunk({
            "candidates": [{
                "content": {
                    "parts": [{"functionCall": {"name": "act", "args": {}}}]
                }
            }],
        }, state, stream, m)

        assert len(state.content_blocks) == 3
        assert isinstance(state.content_blocks[0], ThinkingContent)
        assert isinstance(state.content_blocks[1], TextContent)
        assert isinstance(state.content_blocks[2], ToolCall)

    def test_output_content_updated_at_each_step(self):
        """Output content list is updated incrementally."""
        state, stream, m = _make_state()
        _process_chunk({
            "candidates": [{"content": {"parts": [{"text": "Hello"}]}}],
        }, state, stream, m)
        assert len(state.output.content) == 1

        _process_chunk({
            "candidates": [{
                "content": {
                    "parts": [{"functionCall": {"name": "f", "args": {}}}]
                }
            }],
        }, state, stream, m)
        assert len(state.output.content) == 2
