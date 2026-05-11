"""Convert dino-ai Context to Anthropic Messages API format.

Handles system prompts, user/assistant messages, thinking blocks,
tool calls, tool results, and images.
"""

from __future__ import annotations

import base64
from typing import Any

from dino_ai._sanitize import sanitize_surrogates
from dino_ai.content import ImageContent, TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context, Tool, ToolResultMessage, UserMessage
from dino_ai.model import Model


def convert_system(context: Context) -> list[dict[str, Any]] | None:
    """Convert system prompt to Anthropic format.

    Returns None if no system prompt, otherwise a list of text blocks.
    """
    if not context.system_prompt:
        return None
    return [{"type": "text", "text": sanitize_surrogates(context.system_prompt)}]


def convert_messages(
    model: Model,
    context: Context,
) -> list[dict[str, Any]]:
    """Convert Context messages to Anthropic Messages API format.

    Handles:
    - User text and image messages
    - Assistant messages with thinking blocks and tool calls
    - Batching consecutive tool results into a single user message
    - Filtering errored/aborted assistant messages
    """
    result: list[dict[str, Any]] = []
    i = 0
    messages = context.messages

    while i < len(messages):
        msg = messages[i]

        if isinstance(msg, UserMessage):
            result.append(_convert_user_message(msg))
            i += 1

        elif isinstance(msg, AssistantMessage):
            converted = _convert_assistant_message(msg, model)
            if converted is not None:
                result.append(converted)
            i += 1

        elif isinstance(msg, ToolResultMessage):
            # Batch consecutive tool results into one user message
            tool_results: list[dict[str, Any]] = []
            while i < len(messages) and isinstance(messages[i], ToolResultMessage):
                tr_msg: ToolResultMessage = messages[i]  # type: ignore[assignment]
                tool_results.append(_convert_tool_result(tr_msg))
                i += 1
            result.append({"role": "user", "content": tool_results})

        else:
            i += 1

    return result


def _convert_user_message(msg: UserMessage) -> dict[str, Any]:
    """Convert a user message to Anthropic format."""
    if isinstance(msg.content, str):
        return {"role": "user", "content": sanitize_surrogates(msg.content)}

    blocks: list[dict[str, Any]] = []
    has_text = False

    for block in msg.content:
        if isinstance(block, TextContent):
            blocks.append({"type": "text", "text": sanitize_surrogates(block.text)})
            has_text = True
        elif isinstance(block, ImageContent):
            b64 = base64.b64encode(block.data).decode("ascii")
            blocks.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": block.mime_type,
                    "data": b64,
                },
            })

    # Anthropic requires at least one text block when images are present
    if blocks and not has_text:
        blocks.insert(0, {"type": "text", "text": "(see attached image)"})

    return {"role": "user", "content": blocks}


def _convert_assistant_message(msg: AssistantMessage, model: Model) -> dict[str, Any] | None:
    """Convert an assistant message to Anthropic format."""
    # Skip errored/aborted messages
    if msg.stop_reason in ("error", "aborted"):
        return None

    blocks: list[dict[str, Any]] = []
    is_same_model = msg.model == model.id and msg.provider == model.provider and msg.api == model.api

    for block in msg.content:
        if isinstance(block, TextContent):
            entry: dict[str, Any] = {"type": "text", "text": sanitize_surrogates(block.text)}
            if block.text_signature:
                entry["citations"] = [{"type": "text_signature", "signature": block.text_signature}]
            blocks.append(entry)

        elif isinstance(block, ThinkingContent):
            if is_same_model:
                # Same model: preserve thinking blocks with signatures
                if block.redacted:
                    if block.signature:
                        blocks.append({"type": "redacted_thinking", "data": block.signature})
                elif block.signature:
                    blocks.append({
                        "type": "thinking",
                        "thinking": block.thinking,
                        "signature": block.signature,
                    })
                else:
                    # No signature — fall back to text
                    if block.thinking:
                        blocks.append({"type": "text", "text": block.thinking})
            else:
                # Cross-model: convert thinking to plain text
                if not block.redacted and block.thinking:
                    blocks.append({"type": "text", "text": block.thinking})

        elif isinstance(block, ToolCall):
            blocks.append({
                "type": "tool_use",
                "id": block.id,
                "name": block.name,
                "input": block.arguments,
            })

    if not blocks:
        return None

    return {"role": "assistant", "content": blocks}


def _convert_tool_result(msg: ToolResultMessage) -> dict[str, Any]:
    """Convert a tool result message to Anthropic tool_result block."""
    content_blocks: list[dict[str, Any]] = []

    for block in msg.content:
        if isinstance(block, TextContent):
            content_blocks.append({"type": "text", "text": sanitize_surrogates(block.text)})
        elif isinstance(block, ImageContent):
            b64 = base64.b64encode(block.data).decode("ascii")
            content_blocks.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": block.mime_type,
                    "data": b64,
                },
            })

    # Anthropic accepts string or array for content
    content: str | list[dict[str, Any]]
    if len(content_blocks) == 1 and content_blocks[0]["type"] == "text":
        content = content_blocks[0]["text"]
    elif content_blocks:
        content = content_blocks
    else:
        content = ""

    result: dict[str, Any] = {
        "type": "tool_result",
        "tool_use_id": msg.tool_call_id,
        "content": content,
    }
    if msg.is_error:
        result["is_error"] = True

    return result


def convert_tools(tools: list[Tool]) -> list[dict[str, Any]]:
    """Convert Tool definitions to Anthropic format."""
    return [
        {
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.parameters,
        }
        for tool in tools
    ]


def map_stop_reason(stop_reason: str | None) -> str:
    """Map Anthropic stop_reason to dino-ai StopReason."""
    if stop_reason is None:
        return "stop"
    r = stop_reason.lower()
    if r in ("end_turn", "stop_sequence", "pause_turn"):
        return "stop"
    if r == "max_tokens":
        return "length"
    if r == "tool_use":
        return "toolUse"
    if r in ("refusal", "sensitive"):
        return "error"
    return "stop"
