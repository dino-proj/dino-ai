"""Convert dino-ai Context to OpenAI Chat Completions message format.

Also handles reverse conversion of streaming chunks back to dino-ai events.
"""

from __future__ import annotations

import base64
from typing import Any

from dino_ai._sanitize import sanitize_surrogates
from dino_ai.content import ImageContent, TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context, Message, Tool, ToolResultMessage, UserMessage
from dino_ai.model import Model
from dino_ai.providers.openai_compat import OpenAICompatProfile


def convert_messages(
    model: Model,
    context: Context,
    profile: OpenAICompatProfile,
) -> list[dict[str, Any]]:
    """Convert Context messages to OpenAI ChatCompletion message format.

    Returns a list of dicts matching the OpenAI Chat Completions API schema.
    """
    result: list[dict[str, Any]] = []

    # System prompt
    if context.system_prompt:
        role = "developer" if profile.use_developer_role and model.capabilities.reasoning else "system"
        result.append({"role": role, "content": sanitize_surrogates(context.system_prompt)})

    for msg in context.messages:
        if isinstance(msg, UserMessage):
            result.append(_convert_user_message(msg))
        elif isinstance(msg, AssistantMessage):
            converted = _convert_assistant_message(msg)
            if converted is not None:
                result.append(converted)
        elif isinstance(msg, ToolResultMessage):
            result.append(_convert_tool_result(msg))
            if profile.requires_assistant_after_tool_result:
                _maybe_inject_bridge_assistant(msg, context.messages, result)

    return result


def _convert_user_message(msg: UserMessage) -> dict[str, Any]:
    if isinstance(msg.content, str):
        return {"role": "user", "content": sanitize_surrogates(msg.content)}

    parts: list[dict[str, Any]] = []
    for block in msg.content:
        if isinstance(block, TextContent):
            parts.append({"type": "text", "text": sanitize_surrogates(block.text)})
        elif isinstance(block, ImageContent):
            b64 = base64.b64encode(block.data).decode("ascii")
            parts.append({
                "type": "image_url",
                "image_url": {"url": f"data:{block.mime_type};base64,{b64}"},
            })

    return {"role": "user", "content": parts}


def _convert_assistant_message(msg: AssistantMessage) -> dict[str, Any] | None:
    # Skip errored/aborted messages
    if msg.stop_reason in ("error", "aborted"):
        return None

    result: dict[str, Any] = {"role": "assistant"}
    content_parts: list[dict[str, Any]] = []
    tool_calls: list[dict[str, Any]] = []

    for block in msg.content:
        if isinstance(block, TextContent):
            content_parts.append({"type": "text", "text": sanitize_surrogates(block.text)})
        elif isinstance(block, ThinkingContent):
            # Thinking blocks are non-standard; skip for OpenAI format.
            # They're handled by the transformer for cross-model compat.
            pass
        elif isinstance(block, ToolCall):
            import json

            tool_calls.append({
                "id": block.id,
                "type": "function",
                "function": {
                    "name": block.name,
                    "arguments": json.dumps(block.arguments),
                },
            })

    # Build content field
    if len(content_parts) == 1 and content_parts[0]["type"] == "text":
        result["content"] = content_parts[0]["text"]
    elif content_parts:
        result["content"] = content_parts
    else:
        result["content"] = None

    if tool_calls:
        result["tool_calls"] = tool_calls

    return result


def _convert_tool_result(msg: ToolResultMessage) -> dict[str, Any]:
    # Build text content from tool result blocks
    text_parts: list[str] = []
    for block in msg.content:
        if isinstance(block, TextContent):
            text_parts.append(sanitize_surrogates(block.text))
        elif isinstance(block, ImageContent):
            text_parts.append("(image in tool result)")

    content = "\n".join(text_parts) if text_parts else ""

    return {
        "role": "tool",
        "tool_call_id": msg.tool_call_id,
        "content": content,
    }


def _maybe_inject_bridge_assistant(
    tool_msg: ToolResultMessage,
    all_messages: list[Message],
    result: list[dict[str, Any]],
) -> None:
    """Inject a synthetic assistant message after tool results if needed.

    Some providers (e.g., Anthropic via proxy) require assistant messages
    between tool results and user messages.
    """
    # Find position of this tool result in the original message list
    idx = -1
    for i, m in enumerate(all_messages):
        if m is tool_msg:
            idx = i
            break
    if idx < 0 or idx >= len(all_messages) - 1:
        return

    next_msg = all_messages[idx + 1]
    if isinstance(next_msg, UserMessage):
        result.append({"role": "assistant", "content": "I'll continue processing."})


def convert_tools(tools: list[Tool], profile: OpenAICompatProfile) -> list[dict[str, Any]]:
    """Convert Tool definitions to OpenAI function calling format."""
    result: list[dict[str, Any]] = []
    for tool in tools:
        entry: dict[str, Any] = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.parameters,
            },
        }
        if profile.supports_strict_mode:
            entry["function"]["strict"] = False
        result.append(entry)
    return result


def has_tool_history(messages: list[Message]) -> bool:
    """Check if conversation contains tool calls or results."""
    for msg in messages:
        if isinstance(msg, ToolResultMessage):
            return True
        if isinstance(msg, AssistantMessage) and any(isinstance(b, ToolCall) for b in msg.content):
            return True
    return False
