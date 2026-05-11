"""Tests for message transformer."""

from __future__ import annotations

from dino_ai.content import ImageContent, TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, ToolResultMessage, UserMessage
from dino_ai.model import Model, ModelCapabilities, ModelLimits, ModelPricing
from dino_ai.transformer import transform_messages
from dino_ai.usage import Usage


def _model(vision: bool = True, model_id: str = "test-model", provider: str = "test", api: str = "test-api") -> Model:
    return Model(
        id=model_id,
        name="Test",
        api=api,
        provider=provider,
        base_url="",
        capabilities=ModelCapabilities(vision=vision),
        limits=ModelLimits(),
        pricing=ModelPricing(),
    )


def _assistant(
    content: list,
    model_id: str = "test-model",
    provider: str = "test",
    api: str = "test-api",
    stop_reason: str = "stop",
) -> AssistantMessage:
    return AssistantMessage(
        content=content,
        model=model_id,
        provider=provider,
        api=api,
        usage=Usage(),
        stop_reason=stop_reason,
    )


def test_passthrough_same_model():
    """Messages from the same model should pass through mostly unchanged."""
    model = _model()
    msgs = [
        UserMessage(content="hello"),
        _assistant([TextContent(text="hi"), ThinkingContent(thinking="pondering", signature="sig123")]),
    ]
    result = transform_messages(msgs, model)
    assert len(result) == 2
    assert result[1].content[1].signature == "sig123"


def test_image_downgrade():
    """Images should be replaced with placeholder for non-vision models."""
    model = _model(vision=False)
    msgs = [
        UserMessage(content=[TextContent(text="look at this"), ImageContent(data=b"png", mime_type="image/png")]),
    ]
    result = transform_messages(msgs, model)
    user_msg = result[0]
    assert isinstance(user_msg.content, list)
    assert len(user_msg.content) == 2
    assert all(isinstance(b, TextContent) for b in user_msg.content)
    assert "omitted" in user_msg.content[1].text


def test_image_preserved_for_vision():
    """Images should be kept for vision models."""
    model = _model(vision=True)
    msgs = [
        UserMessage(content=[TextContent(text="look"), ImageContent(data=b"png", mime_type="image/png")]),
    ]
    result = transform_messages(msgs, model)
    assert isinstance(result[0].content[1], ImageContent)


def test_thinking_cross_model():
    """Thinking blocks should be converted to text for cross-model."""
    model = _model(model_id="different-model")
    msgs = [
        _assistant(
            [ThinkingContent(thinking="deep thought"), TextContent(text="answer")],
            model_id="original-model",
        ),
    ]
    result = transform_messages(msgs, model)
    # Thinking should become text
    assert isinstance(result[0].content[0], TextContent)
    assert result[0].content[0].text == "deep thought"


def test_redacted_thinking_dropped_cross_model():
    """Redacted thinking should be dropped for different models."""
    model = _model(model_id="different-model")
    msgs = [
        _assistant(
            [ThinkingContent(thinking="", redacted=True), TextContent(text="answer")],
            model_id="original-model",
        ),
    ]
    result = transform_messages(msgs, model)
    assert len(result[0].content) == 1
    assert result[0].content[0].text == "answer"


def test_errored_messages_dropped():
    """Errored/aborted assistant messages should be filtered out."""
    model = _model()
    msgs = [
        UserMessage(content="hello"),
        _assistant([TextContent(text="partial")], stop_reason="error"),
        UserMessage(content="retry"),
        _assistant([TextContent(text="success")]),
    ]
    result = transform_messages(msgs, model)
    assert len(result) == 3
    assert result[0].content == "hello"
    assert result[1].content == "retry"
    assert result[2].content[0].text == "success"


def test_orphaned_tool_calls_get_synthetic_results():
    """Tool calls without results should get synthetic error results."""
    model = _model()
    tc = ToolCall(id="tc1", name="search", arguments={"q": "test"})
    msgs = [
        UserMessage(content="do something"),
        _assistant([tc]),
        UserMessage(content="next"),
    ]
    result = transform_messages(msgs, model)
    # Should be: user, assistant, synthetic tool result, user
    assert len(result) == 4
    assert isinstance(result[2], ToolResultMessage)
    assert result[2].tool_call_id == "tc1"
    assert result[2].is_error is True


def test_tool_calls_with_results_no_synthetic():
    """Tool calls with matching results should not generate synthetic ones."""
    model = _model()
    tc = ToolCall(id="tc1", name="search", arguments={"q": "test"})
    msgs = [
        _assistant([tc]),
        ToolResultMessage(tool_call_id="tc1", tool_name="search", content=[TextContent(text="found it")]),
    ]
    result = transform_messages(msgs, model)
    assert len(result) == 2
