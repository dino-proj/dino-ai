"""Convert dino-ai Context to AWS Bedrock Converse format.

Handles system prompts, user/assistant/tool messages, thinking blocks,
images, and tool call round-trips.
"""

from __future__ import annotations

from typing import Any

from dino_ai._sanitize import sanitize_surrogates
from dino_ai.content import ImageContent, TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context, Tool, ToolResultMessage, UserMessage
from dino_ai.model import Model

# Bedrock image format mapping
_MIME_TO_FORMAT: dict[str, str] = {
    "image/jpeg": "jpeg",
    "image/png": "png",
    "image/gif": "gif",
    "image/webp": "webp",
}


def convert_system(context: Context) -> list[dict[str, Any]] | None:
    """Extract system prompt as Bedrock system content blocks."""
    if not context.system_prompt:
        return None
    return [{"text": sanitize_surrogates(context.system_prompt)}]


def convert_messages(
    model: Model,
    context: Context,
) -> list[dict[str, Any]]:
    """Convert Context messages to Bedrock Converse messages array.

    Handles:
    - User text and image messages -> role "user"
    - Assistant messages -> role "assistant" with text, toolUse, reasoningContent
    - Tool results -> role "user" with toolResult blocks (batched)
    - Filtering errored/aborted assistant messages
    """
    result: list[dict[str, Any]] = []
    i = 0
    messages = context.messages

    while i < len(messages):
        msg = messages[i]

        if isinstance(msg, UserMessage):
            result.append(_convert_user_message(msg, model))
            i += 1

        elif isinstance(msg, AssistantMessage):
            converted = _convert_assistant_message(msg, model)
            if converted is not None:
                result.append(converted)
            i += 1

        elif isinstance(msg, ToolResultMessage):
            # Batch consecutive tool results into one user turn
            content: list[dict[str, Any]] = []
            while i < len(messages) and isinstance(messages[i], ToolResultMessage):
                tr: ToolResultMessage = messages[i]  # type: ignore[assignment]
                content.append(_convert_tool_result(tr))
                i += 1
            result.append({"role": "user", "content": content})

        else:
            i += 1

    return result


def _convert_user_message(msg: UserMessage, model: Model) -> dict[str, Any]:
    """Convert a user message to Bedrock format."""
    if isinstance(msg.content, str):
        return {"role": "user", "content": [{"text": sanitize_surrogates(msg.content)}]}

    content: list[dict[str, Any]] = []
    for block in msg.content:
        if isinstance(block, TextContent):
            content.append({"text": sanitize_surrogates(block.text)})
        elif isinstance(block, ImageContent):
            if model.capabilities.vision:
                fmt = _MIME_TO_FORMAT.get(block.mime_type, "png")
                content.append({
                    "image": {
                        "source": {"bytes": block.data},
                        "format": fmt,
                    }
                })
            else:
                content.append({"text": "(image omitted: model does not support images)"})

    if not content:
        content.append({"text": ""})

    return {"role": "user", "content": content}


def _convert_assistant_message(msg: AssistantMessage, model: Model) -> dict[str, Any] | None:
    """Convert an assistant message to Bedrock format."""
    if msg.stop_reason in ("error", "aborted"):
        return None

    is_same = msg.model == model.id and msg.provider == model.provider and msg.api == model.api
    content: list[dict[str, Any]] = []

    for block in msg.content:
        if isinstance(block, TextContent):
            if not block.text:
                continue
            content.append({"text": sanitize_surrogates(block.text)})

        elif isinstance(block, ThinkingContent):
            if not block.thinking:
                continue
            if is_same and block.signature:
                # Same model: preserve as reasoningContent with signature
                reasoning: dict[str, Any] = {
                    "text": block.thinking,
                    "signature": block.signature,
                }
                content.append({"reasoningContent": {"reasoningText": reasoning}})
            elif block.redacted:
                # Redacted thinking from different model — skip
                continue
            else:
                # Cross-model: convert thinking to plain text
                content.append({"text": block.thinking})

        elif isinstance(block, ToolCall):
            content.append({
                "toolUse": {
                    "toolUseId": _normalize_tool_id(block.id),
                    "name": block.name,
                    "input": block.arguments,
                }
            })

    if not content:
        return None

    return {"role": "assistant", "content": content}


def _convert_tool_result(msg: ToolResultMessage) -> dict[str, Any]:
    """Convert a tool result to Bedrock toolResult format."""
    result_content: list[dict[str, Any]] = []
    for block in msg.content:
        if isinstance(block, TextContent):
            result_content.append({"text": sanitize_surrogates(block.text)})

    if not result_content:
        result_content.append({"text": ""})

    tr: dict[str, Any] = {
        "toolUseId": _normalize_tool_id(msg.tool_call_id),
        "content": result_content,
    }
    if msg.is_error:
        tr["status"] = "error"

    return {"toolResult": tr}


def _normalize_tool_id(tool_id: str) -> str:
    """Normalize tool call IDs for Bedrock (alphanumeric, _, - only, max 64 chars)."""
    result: list[str] = []
    for ch in tool_id:
        if ch.isalnum() or ch in ("_", "-"):
            result.append(ch)
        else:
            result.append("_")
    normalized = "".join(result)
    return normalized[:64]


def convert_tools(tools: list[Tool]) -> list[dict[str, Any]]:
    """Convert Tool definitions to Bedrock toolSpec format."""
    specs: list[dict[str, Any]] = []
    for tool in tools:
        spec: dict[str, Any] = {
            "toolSpec": {
                "name": tool.name,
                "description": tool.description,
                "inputSchema": {"json": tool.parameters},
            }
        }
        specs.append(spec)
    return specs


def map_stop_reason(stop_reason: str | None) -> str:
    """Map Bedrock StopReason to dino-ai StopReason."""
    if not stop_reason:
        return "stop"
    r = stop_reason.upper()
    if r in ("END_TURN", "STOP_SEQUENCE"):
        return "stop"
    if r in ("MAX_TOKENS", "MODEL_CONTEXT_WINDOW_EXCEEDED"):
        return "length"
    if r == "TOOL_USE":
        return "toolUse"
    return "error"
