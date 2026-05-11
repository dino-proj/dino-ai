"""Tests for cross-provider context transfer and handoff scenarios.

Verifies that conversation history from one provider can be correctly
sent to another, with proper normalization of thinking blocks, tool call
IDs, and image handling.
"""

from __future__ import annotations

from dino_ai.content import ImageContent, TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context, ToolResultMessage, UserMessage
from dino_ai.model import Model, ModelCapabilities, ModelLimits, ModelPricing
from dino_ai.providers.anthropic_messages import convert_messages as anthropic_convert
from dino_ai.providers.bedrock_messages import convert_messages as bedrock_convert
from dino_ai.providers.google_messages import convert_messages as google_convert
from dino_ai.providers.openai_compat import PROFILE_OPENAI
from dino_ai.providers.openai_messages import convert_messages as openai_convert
from dino_ai.transformer import transform_messages


def _openai_model() -> Model:
    return Model(
        id="gpt-4o",
        name="GPT-4o",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(reasoning=False, vision=True),
        limits=ModelLimits(context_window=128000, max_output_tokens=16384),
        pricing=ModelPricing(input=2.5, output=10.0),
    )


def _anthropic_model() -> Model:
    return Model(
        id="claude-sonnet-4-20250514",
        name="Claude Sonnet 4",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com/v1",
        capabilities=ModelCapabilities(reasoning=True, vision=True),
        limits=ModelLimits(context_window=200000, max_output_tokens=8192),
        pricing=ModelPricing(input=3.0, output=15.0),
    )


def _google_model() -> Model:
    return Model(
        id="gemini-2.5-flash",
        name="Gemini 2.5 Flash",
        api="google-generative-ai",
        provider="google",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        capabilities=ModelCapabilities(reasoning=True, vision=True),
        limits=ModelLimits(context_window=1048576, max_output_tokens=65536),
        pricing=ModelPricing(input=0.15, output=0.60),
    )


def _bedrock_model() -> Model:
    return Model(
        id="anthropic.claude-sonnet-4-20250514-v1:0",
        name="Claude Sonnet 4 (Bedrock)",
        api="bedrock-converse-stream",
        provider="bedrock",
        base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
        capabilities=ModelCapabilities(reasoning=True, vision=True),
        limits=ModelLimits(context_window=200000, max_output_tokens=8192),
        pricing=ModelPricing(input=3.0, output=15.0),
    )


# ── OpenAI → Anthropic handoff ──────────────────────────────────


class TestOpenAIToAnthropic:
    def test_text_history_transfers(self):
        """Plain text from OpenAI should transfer to Anthropic cleanly."""
        messages = [
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[TextContent(text="Hi there!")],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
            ),
            UserMessage(content="How are you?"),
        ]

        target = _anthropic_model()
        transformed = transform_messages(messages, target)
        ctx = Context(messages=transformed)
        result = anthropic_convert(target, ctx)

        assert len(result) == 3
        assert result[0] == {"role": "user", "content": "Hello"}
        assert result[1]["role"] == "assistant"
        # Text from different model becomes plain text block
        assert result[1]["content"][0]["type"] == "text"
        assert result[1]["content"][0]["text"] == "Hi there!"
        assert result[2] == {"role": "user", "content": "How are you?"}

    def test_tool_calls_transfer(self):
        """Tool calls from OpenAI should transfer to Anthropic format."""
        messages = [
            UserMessage(content="Search for cats"),
            AssistantMessage(
                content=[ToolCall(id="call_abc123", name="search", arguments={"q": "cats"})],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
                stop_reason="toolUse",
            ),
            ToolResultMessage(
                tool_call_id="call_abc123",
                tool_name="search",
                content=[TextContent(text="Found 42 results")],
            ),
        ]

        target = _anthropic_model()
        transformed = transform_messages(messages, target)
        ctx = Context(messages=transformed)
        result = anthropic_convert(target, ctx)

        assert len(result) == 3
        # Assistant message with tool_use block
        assert result[1]["role"] == "assistant"
        assert result[1]["content"][0]["type"] == "tool_use"
        assert result[1]["content"][0]["id"] == "call_abc123"
        assert result[1]["content"][0]["name"] == "search"
        # Tool result as user message
        assert result[2]["role"] == "user"
        assert result[2]["content"][0]["type"] == "tool_result"
        assert result[2]["content"][0]["tool_use_id"] == "call_abc123"

    def test_image_history_transfers(self):
        """Image content from OpenAI should transfer to Anthropic format."""
        messages = [
            UserMessage(content=[
                TextContent(text="What's this?"),
                ImageContent(data=b"\x89PNG", mime_type="image/png"),
            ]),
            AssistantMessage(
                content=[TextContent(text="It's a cat")],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
            ),
        ]

        target = _anthropic_model()
        transformed = transform_messages(messages, target)
        ctx = Context(messages=transformed)
        result = anthropic_convert(target, ctx)

        assert result[0]["role"] == "user"
        parts = result[0]["content"]
        assert parts[0]["type"] == "text"
        assert parts[1]["type"] == "image"
        assert parts[1]["source"]["type"] == "base64"


# ── Anthropic → OpenAI handoff ──────────────────────────────────


class TestAnthropicToOpenAI:
    def test_text_history_transfers(self):
        """Plain text from Anthropic should transfer to OpenAI."""
        messages = [
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[TextContent(text="Hello!")],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
            UserMessage(content="Tell me more"),
        ]

        target = _openai_model()
        transformed = transform_messages(messages, target)
        ctx = Context(messages=transformed)
        result = openai_convert(target, ctx, PROFILE_OPENAI)

        assert len(result) == 3
        assert result[0] == {"role": "user", "content": "Hello"}
        assert result[1]["role"] == "assistant"
        assert result[1]["content"] == "Hello!"
        assert result[2] == {"role": "user", "content": "Tell me more"}

    def test_thinking_becomes_text_for_openai(self):
        """Anthropic thinking blocks should become plain text for OpenAI."""
        messages = [
            UserMessage(content="What is 2+2?"),
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Let me add 2+2...", signature="sig123"),
                    TextContent(text="4"),
                ],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ]

        target = _openai_model()
        transformed = transform_messages(messages, target)

        # Thinking should be converted to text for cross-model transfer
        assistant = transformed[1]
        assert isinstance(assistant, AssistantMessage)
        assert len(assistant.content) == 2
        # First block: thinking converted to text
        assert isinstance(assistant.content[0], TextContent)
        assert assistant.content[0].text == "Let me add 2+2..."
        # Second block: original text preserved
        assert isinstance(assistant.content[1], TextContent)
        assert assistant.content[1].text == "4"

    def test_redacted_thinking_dropped_for_openai(self):
        """Redacted thinking from Anthropic should be dropped for OpenAI."""
        messages = [
            UserMessage(content="Question"),
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="[Reasoning redacted]", signature="opaque", redacted=True),
                    TextContent(text="Answer"),
                ],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ]

        target = _openai_model()
        transformed = transform_messages(messages, target)

        assistant = transformed[1]
        assert isinstance(assistant, AssistantMessage)
        # Redacted thinking should be dropped entirely
        assert len(assistant.content) == 1
        assert isinstance(assistant.content[0], TextContent)
        assert assistant.content[0].text == "Answer"


# ── Anthropic → Anthropic (same model) ──────────────────────────


class TestAnthropicToAnthropic:
    def test_thinking_preserved_same_model(self):
        """Thinking blocks with signatures should be preserved for same model."""
        messages = [
            UserMessage(content="Think about this"),
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Deep thoughts...", signature="valid_sig"),
                    TextContent(text="Conclusion"),
                ],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ]

        target = _anthropic_model()
        transformed = transform_messages(messages, target)
        ctx = Context(messages=transformed)
        result = anthropic_convert(target, ctx)

        assistant = result[1]
        assert assistant["role"] == "assistant"
        blocks = assistant["content"]
        assert blocks[0]["type"] == "thinking"
        assert blocks[0]["thinking"] == "Deep thoughts..."
        assert blocks[0]["signature"] == "valid_sig"
        assert blocks[1]["type"] == "text"

    def test_redacted_thinking_preserved_same_model(self):
        """Redacted thinking should be preserved for same model."""
        messages = [
            UserMessage(content="Question"),
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="[Reasoning redacted]", signature="opaque_data", redacted=True),
                    TextContent(text="Answer"),
                ],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ]

        target = _anthropic_model()
        transformed = transform_messages(messages, target)
        ctx = Context(messages=transformed)
        result = anthropic_convert(target, ctx)

        blocks = result[1]["content"]
        assert blocks[0]["type"] == "redacted_thinking"
        assert blocks[0]["data"] == "opaque_data"


# ── Errored message handling ────────────────────────────────────


class TestErroredMessageHandling:
    def test_errored_assistant_dropped_before_handoff(self):
        """Errored assistant messages should be dropped during transformation."""
        messages = [
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[TextContent(text="partial response")],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
                stop_reason="error",
            ),
            UserMessage(content="Try again"),
        ]

        target = _anthropic_model()
        transformed = transform_messages(messages, target)

        # Should have 2 messages: user, user (errored assistant dropped)
        assert len(transformed) == 2
        assert isinstance(transformed[0], UserMessage)
        assert isinstance(transformed[1], UserMessage)

    def test_orphaned_tool_calls_get_synthetic_results(self):
        """Orphaned tool calls should get synthetic results before handoff."""
        messages = [
            UserMessage(content="Search"),
            AssistantMessage(
                content=[ToolCall(id="tc-1", name="search", arguments={"q": "test"})],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
                stop_reason="toolUse",
            ),
            # No ToolResultMessage follows — this is an orphaned tool call
            UserMessage(content="Nevermind"),
        ]

        target = _anthropic_model()
        transformed = transform_messages(messages, target)

        # Should insert a synthetic tool result between assistant and user
        assert len(transformed) == 4
        synthetic = transformed[2]
        assert isinstance(synthetic, ToolResultMessage)
        assert synthetic.tool_call_id == "tc-1"
        assert synthetic.is_error is True


# ── Image downgrade for non-vision models ────────────────────────


class TestImageDowngrade:
    def test_images_downgraded_for_non_vision_target(self):
        """Images should be replaced with placeholders for non-vision models."""
        messages = [
            UserMessage(content=[
                TextContent(text="What's this?"),
                ImageContent(data=b"\x89PNG", mime_type="image/png"),
            ]),
        ]

        target = Model(
            id="gpt-3.5-turbo",
            name="GPT-3.5 Turbo",
            api="openai-completions",
            provider="openai",
            base_url="https://api.openai.com/v1",
            capabilities=ModelCapabilities(vision=False),
            limits=ModelLimits(),
        )
        transformed = transform_messages(messages, target)

        user = transformed[0]
        assert isinstance(user, UserMessage)
        assert isinstance(user.content, list)
        # Should have text + placeholder (no ImageContent)
        assert all(isinstance(b, TextContent) for b in user.content)
        assert any("omitted" in b.text for b in user.content if isinstance(b, TextContent))


# ── OpenAI → Google handoff ─────────────────────────────────────


class TestOpenAIToGoogle:
    def test_text_history_transfers(self):
        """Text from OpenAI should transfer to Gemini as model turn."""
        messages = [
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[TextContent(text="Hi!")],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
            ),
            UserMessage(content="More"),
        ]

        target = _google_model()
        transformed = transform_messages(messages, target)
        result = google_convert(target, Context(messages=transformed))

        assert len(result) == 3
        assert result[0]["role"] == "user"
        assert result[1]["role"] == "model"
        assert result[1]["parts"][0] == {"text": "Hi!"}
        assert result[2]["role"] == "user"

    def test_tool_calls_transfer(self):
        """Tool calls from OpenAI should become functionCall parts."""
        messages = [
            UserMessage(content="Search"),
            AssistantMessage(
                content=[ToolCall(id="call_123", name="search", arguments={"q": "cats"})],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
                stop_reason="toolUse",
            ),
            ToolResultMessage(
                tool_call_id="call_123",
                tool_name="search",
                content=[TextContent(text="Found cats")],
            ),
        ]

        target = _google_model()
        transformed = transform_messages(messages, target)
        result = google_convert(target, Context(messages=transformed))

        assert result[1]["role"] == "model"
        assert result[1]["parts"][0]["functionCall"]["name"] == "search"
        assert result[2]["role"] == "user"
        assert result[2]["parts"][0]["functionResponse"]["name"] == "search"


# ── Anthropic → Google handoff ──────────────────────────────────


class TestAnthropicToGoogle:
    def test_thinking_becomes_text(self):
        """Anthropic thinking should become plain text for Gemini."""
        messages = [
            UserMessage(content="Think"),
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Deep thoughts", signature="sig"),
                    TextContent(text="Answer"),
                ],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ]

        target = _google_model()
        transformed = transform_messages(messages, target)
        result = google_convert(target, Context(messages=transformed))

        parts = result[1]["parts"]
        # Cross-model thinking becomes plain text
        assert parts[0] == {"text": "Deep thoughts"}
        assert parts[1] == {"text": "Answer"}

    def test_redacted_thinking_dropped(self):
        """Redacted thinking from Anthropic should be dropped for Gemini."""
        messages = [
            UserMessage(content="Q"),
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="[redacted]", signature="opaque", redacted=True),
                    TextContent(text="A"),
                ],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ]

        target = _google_model()
        transformed = transform_messages(messages, target)
        result = google_convert(target, Context(messages=transformed))

        parts = result[1]["parts"]
        assert len(parts) == 1
        assert parts[0] == {"text": "A"}


# ── Google → OpenAI handoff ─────────────────────────────────────


class TestGoogleToOpenAI:
    def test_text_history_transfers(self):
        """Text from Gemini should transfer to OpenAI."""
        messages = [
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[TextContent(text="Hi from Gemini")],
                model="gemini-2.5-flash",
                provider="google",
                api="google-generative-ai",
            ),
        ]

        target = _openai_model()
        transformed = transform_messages(messages, target)
        result = openai_convert(target, Context(messages=transformed), PROFILE_OPENAI)

        assert result[1]["role"] == "assistant"
        assert result[1]["content"] == "Hi from Gemini"

    def test_thinking_becomes_text(self):
        """Gemini thinking should become text for OpenAI."""
        messages = [
            UserMessage(content="Q"),
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Gemini reasoning", signature="gsig"),
                    TextContent(text="A"),
                ],
                model="gemini-2.5-flash",
                provider="google",
                api="google-generative-ai",
            ),
        ]

        target = _openai_model()
        transformed = transform_messages(messages, target)

        assistant = transformed[1]
        assert isinstance(assistant, AssistantMessage)
        assert isinstance(assistant.content[0], TextContent)
        assert assistant.content[0].text == "Gemini reasoning"


# ── Google → Anthropic handoff ──────────────────────────────────


class TestGoogleToAnthropic:
    def test_text_transfers(self):
        """Text from Gemini should transfer to Anthropic."""
        messages = [
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[TextContent(text="Hi from Gemini")],
                model="gemini-2.5-flash",
                provider="google",
                api="google-generative-ai",
            ),
        ]

        target = _anthropic_model()
        transformed = transform_messages(messages, target)
        result = anthropic_convert(target, Context(messages=transformed))

        assert result[1]["role"] == "assistant"
        assert result[1]["content"][0]["type"] == "text"
        assert result[1]["content"][0]["text"] == "Hi from Gemini"


# ── Google → Google (same model) ────────────────────────────────


class TestGoogleToGoogle:
    def test_thinking_preserved_same_model(self):
        """Thinking with signature should be preserved for same Gemini model."""
        messages = [
            UserMessage(content="Think"),
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Thoughts", signature="gsig123"),
                    TextContent(text="Result"),
                ],
                model="gemini-2.5-flash",
                provider="google",
                api="google-generative-ai",
            ),
        ]

        target = _google_model()
        transformed = transform_messages(messages, target)
        result = google_convert(target, Context(messages=transformed))

        parts = result[1]["parts"]
        assert parts[0]["text"] == "Thoughts"
        assert parts[0]["thought"] is True
        assert parts[0]["thoughtSignature"] == "gsig123"
        assert parts[1] == {"text": "Result"}


# ── OpenAI → Bedrock handoff ───────────────────────────────────


class TestOpenAIToBedrock:
    def test_text_history_transfers(self):
        """Text from OpenAI should transfer to Bedrock."""
        messages = [
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[TextContent(text="Hi!")],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
            ),
            UserMessage(content="More"),
        ]

        target = _bedrock_model()
        transformed = transform_messages(messages, target)
        result = bedrock_convert(target, Context(messages=transformed))

        assert len(result) == 3
        assert result[0]["role"] == "user"
        assert result[1]["role"] == "assistant"
        assert result[1]["content"][0] == {"text": "Hi!"}

    def test_tool_calls_transfer(self):
        """Tool calls from OpenAI should become toolUse blocks."""
        messages = [
            UserMessage(content="Search"),
            AssistantMessage(
                content=[ToolCall(id="call_123", name="search", arguments={"q": "cats"})],
                model="gpt-4o",
                provider="openai",
                api="openai-completions",
                stop_reason="toolUse",
            ),
            ToolResultMessage(
                tool_call_id="call_123",
                tool_name="search",
                content=[TextContent(text="Found cats")],
            ),
        ]

        target = _bedrock_model()
        transformed = transform_messages(messages, target)
        result = bedrock_convert(target, Context(messages=transformed))

        assert result[1]["content"][0]["toolUse"]["name"] == "search"
        assert result[2]["role"] == "user"
        assert result[2]["content"][0]["toolResult"]["toolUseId"] == "call_123"


# ── Anthropic → Bedrock handoff ─────────────────────────────────


class TestAnthropicToBedrock:
    def test_thinking_becomes_text(self):
        """Anthropic thinking should become plain text for Bedrock (different model)."""
        messages = [
            UserMessage(content="Think"),
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Deep thoughts", signature="sig"),
                    TextContent(text="Answer"),
                ],
                model="claude-sonnet-4-20250514",
                provider="anthropic",
                api="anthropic-messages",
            ),
        ]

        target = _bedrock_model()
        transformed = transform_messages(messages, target)
        result = bedrock_convert(target, Context(messages=transformed))

        blocks = result[1]["content"]
        # Cross-model thinking becomes plain text
        assert blocks[0] == {"text": "Deep thoughts"}
        assert blocks[1] == {"text": "Answer"}


# ── Bedrock → OpenAI handoff ───────────────────────────────────


class TestBedrockToOpenAI:
    def test_text_transfers(self):
        """Text from Bedrock should transfer to OpenAI."""
        messages = [
            UserMessage(content="Hello"),
            AssistantMessage(
                content=[TextContent(text="Hi from Bedrock")],
                model="anthropic.claude-sonnet-4-20250514-v1:0",
                provider="bedrock",
                api="bedrock-converse-stream",
            ),
        ]

        target = _openai_model()
        transformed = transform_messages(messages, target)
        result = openai_convert(target, Context(messages=transformed), PROFILE_OPENAI)

        assert result[1]["role"] == "assistant"
        assert result[1]["content"] == "Hi from Bedrock"

    def test_thinking_becomes_text(self):
        """Bedrock thinking should become text for OpenAI."""
        messages = [
            UserMessage(content="Q"),
            AssistantMessage(
                content=[
                    ThinkingContent(thinking="Bedrock reasoning", signature="bsig"),
                    TextContent(text="A"),
                ],
                model="anthropic.claude-sonnet-4-20250514-v1:0",
                provider="bedrock",
                api="bedrock-converse-stream",
            ),
        ]

        target = _openai_model()
        transformed = transform_messages(messages, target)

        assistant = transformed[1]
        assert isinstance(assistant, AssistantMessage)
        assert isinstance(assistant.content[0], TextContent)
        assert assistant.content[0].text == "Bedrock reasoning"
