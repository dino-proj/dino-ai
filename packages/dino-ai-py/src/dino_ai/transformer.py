"""Shared message transformer for cross-provider compatibility.

Handles:
- Image downgrade for non-vision models
- Thinking block normalization across providers
- Tool call ID normalization
- Synthetic tool results for orphaned tool calls
- Errored/aborted assistant message filtering
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from dino_ai.content import ImageContent, TextContent, ThinkingContent, ToolCall
from dino_ai.context import (
    STOP_REASON_ABORTED,
    STOP_REASON_ERROR,
    AssistantMessage,
    Message,
    ToolResultMessage,
    UserMessage,
)
from dino_ai.model import Model

_USER_IMAGE_PLACEHOLDER = "(image omitted: model does not support images)"
_TOOL_IMAGE_PLACEHOLDER = "(tool image omitted: model does not support images)"

ToolCallIdNormalizer = Callable[[str, Model, AssistantMessage], str]


def _replace_images_with_placeholder(
    content: list[TextContent | ImageContent],
    placeholder: str,
) -> list[TextContent]:
    result: list[TextContent] = []
    prev_was_placeholder = False
    for block in content:
        if isinstance(block, ImageContent):
            if not prev_was_placeholder:
                result.append(TextContent(text=placeholder))
            prev_was_placeholder = True
            continue
        result.append(block)
        prev_was_placeholder = block.text == placeholder
    return result


def _downgrade_images(messages: list[Message], model: Model) -> list[Message]:
    if model.capabilities.vision:
        return messages
    out: list[Message] = []
    for msg in messages:
        if isinstance(msg, UserMessage) and isinstance(msg.content, list):
            replaced: list[TextContent | ImageContent] = list(
                _replace_images_with_placeholder(msg.content, _USER_IMAGE_PLACEHOLDER)
            )
            new_msg = UserMessage(
                content=replaced,
                timestamp=msg.timestamp,
                metadata=msg.metadata,
            )
            out.append(new_msg)
        elif isinstance(msg, ToolResultMessage):
            replaced_tr: list[TextContent | ImageContent] = list(
                _replace_images_with_placeholder(msg.content, _TOOL_IMAGE_PLACEHOLDER)
            )
            new_msg_tr = ToolResultMessage(
                tool_call_id=msg.tool_call_id,
                tool_name=msg.tool_name,
                content=replaced_tr,
                is_error=msg.is_error,
                timestamp=msg.timestamp,
                metadata=msg.metadata,
            )
            out.append(new_msg_tr)
        else:
            out.append(msg)
    return out


@dataclass(frozen=True)
class _SyntheticToolResult:
    tool_call: ToolCall


def _transform_assistant_content(
    msg: AssistantMessage,
    model: Model,
    is_same_model: bool,
    normalize_tool_call_id: ToolCallIdNormalizer | None,
    tool_call_id_map: dict[str, str],
) -> list[TextContent | ThinkingContent | ToolCall]:
    result: list[TextContent | ThinkingContent | ToolCall] = []
    for block in msg.content:
        if isinstance(block, ThinkingContent):
            if block.redacted:
                if is_same_model:
                    result.append(block)
                continue
            if is_same_model and block.signature:
                result.append(block)
                continue
            if not block.thinking or block.thinking.strip() == "":
                continue
            if is_same_model:
                result.append(block)
            else:
                result.append(TextContent(text=block.thinking))
        elif isinstance(block, TextContent):
            if is_same_model:
                result.append(block)
            else:
                result.append(TextContent(text=block.text))
        elif isinstance(block, ToolCall):
            tc = block
            if not is_same_model and tc.thought_signature:
                tc = ToolCall(id=tc.id, name=tc.name, arguments=tc.arguments)
            if not is_same_model and normalize_tool_call_id is not None:
                new_id = normalize_tool_call_id(tc.id, model, msg)
                if new_id != tc.id:
                    tool_call_id_map[block.id] = new_id
                    tc = ToolCall(
                        id=new_id, name=tc.name, arguments=tc.arguments, thought_signature=tc.thought_signature
                    )
            result.append(tc)
    return result


def transform_messages(
    messages: list[Message],
    model: Model,
    normalize_tool_call_id: ToolCallIdNormalizer | None = None,
) -> list[Message]:
    """Transform messages for cross-provider compatibility.

    - Downgrades images for non-vision models
    - Normalizes thinking blocks (drops redacted for cross-model, converts to text)
    - Normalizes tool call IDs via optional callback
    - Inserts synthetic tool results for orphaned tool calls
    - Drops errored/aborted assistant messages
    """
    tool_call_id_map: dict[str, str] = {}
    image_aware = _downgrade_images(messages, model)

    # First pass: transform content blocks
    transformed: list[Message] = []
    for msg in image_aware:
        if isinstance(msg, UserMessage):
            transformed.append(msg)
        elif isinstance(msg, ToolResultMessage):
            normalized_id = tool_call_id_map.get(msg.tool_call_id)
            if normalized_id and normalized_id != msg.tool_call_id:
                transformed.append(
                    ToolResultMessage(
                        tool_call_id=normalized_id,
                        tool_name=msg.tool_name,
                        content=msg.content,
                        is_error=msg.is_error,
                        timestamp=msg.timestamp,
                        metadata=msg.metadata,
                    )
                )
            else:
                transformed.append(msg)
        elif isinstance(msg, AssistantMessage):
            is_same = msg.provider == model.provider and msg.api == model.api and msg.model == model.id
            new_content = _transform_assistant_content(msg, model, is_same, normalize_tool_call_id, tool_call_id_map)
            new_msg = AssistantMessage(
                content=new_content,
                model=msg.model,
                response_model=msg.response_model,
                response_id=msg.response_id,
                provider=msg.provider,
                api=msg.api,
                usage=msg.usage,
                stop_reason=msg.stop_reason,
                error=msg.error,
                timestamp=msg.timestamp,
                metadata=msg.metadata,
            )
            transformed.append(new_msg)

    # Second pass: insert synthetic tool results for orphaned tool calls, drop errored/aborted
    result: list[Message] = []
    pending_tool_calls: list[ToolCall] = []
    existing_tool_result_ids: set[str] = set()

    def flush_orphaned() -> None:
        for tc in pending_tool_calls:
            if tc.id not in existing_tool_result_ids:
                result.append(
                    ToolResultMessage(
                        tool_call_id=tc.id,
                        tool_name=tc.name,
                        content=[TextContent(text="No result provided")],
                        is_error=True,
                    )
                )
        pending_tool_calls.clear()
        existing_tool_result_ids.clear()

    for msg in transformed:
        if isinstance(msg, AssistantMessage):
            flush_orphaned()
            if msg.stop_reason in (STOP_REASON_ERROR, STOP_REASON_ABORTED):
                continue
            tool_calls = [b for b in msg.content if isinstance(b, ToolCall)]
            if tool_calls:
                pending_tool_calls.extend(tool_calls)
                existing_tool_result_ids.clear()
            result.append(msg)
        elif isinstance(msg, ToolResultMessage):
            existing_tool_result_ids.add(msg.tool_call_id)
            result.append(msg)
        elif isinstance(msg, UserMessage):
            flush_orphaned()
            result.append(msg)

    flush_orphaned()
    return result
