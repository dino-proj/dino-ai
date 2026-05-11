"""Convert dino-ai Context to Google Gemini generateContent format.

Handles system instructions, user/model messages, thinking blocks,
function calls, function responses, and inline images.
"""

from __future__ import annotations

import base64
from typing import Any

from dino_ai._sanitize import sanitize_surrogates
from dino_ai.content import ImageContent, TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context, Tool, ToolResultMessage, UserMessage
from dino_ai.model import Model


def convert_system(context: Context) -> str | None:
    """Extract system instruction as a plain string (Gemini format)."""
    if not context.system_prompt:
        return None
    return sanitize_surrogates(context.system_prompt)


def convert_messages(
    model: Model,
    context: Context,
) -> list[dict[str, Any]]:
    """Convert Context messages to Gemini contents array.

    Handles:
    - User text and image messages → role "user"
    - Assistant messages → role "model" with text, thought, functionCall parts
    - Tool results → role "user" with functionResponse parts (batched)
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
            # Batch consecutive tool results into one user turn
            parts: list[dict[str, Any]] = []
            while i < len(messages) and isinstance(messages[i], ToolResultMessage):
                tr: ToolResultMessage = messages[i]  # type: ignore[assignment]
                parts.append(_convert_tool_result(tr))
                i += 1
            result.append({"role": "user", "parts": parts})

        else:
            i += 1

    return result


def _convert_user_message(msg: UserMessage) -> dict[str, Any]:
    """Convert a user message to Gemini format."""
    if isinstance(msg.content, str):
        return {"role": "user", "parts": [{"text": sanitize_surrogates(msg.content)}]}

    parts: list[dict[str, Any]] = []
    for block in msg.content:
        if isinstance(block, TextContent):
            parts.append({"text": sanitize_surrogates(block.text)})
        elif isinstance(block, ImageContent):
            b64 = base64.b64encode(block.data).decode("ascii")
            parts.append({"inlineData": {"mimeType": block.mime_type, "data": b64}})

    if not parts:
        parts.append({"text": ""})

    return {"role": "user", "parts": parts}


def _convert_assistant_message(msg: AssistantMessage, model: Model) -> dict[str, Any] | None:
    """Convert an assistant message to Gemini model turn."""
    if msg.stop_reason in ("error", "aborted"):
        return None

    is_same = msg.model == model.id and msg.provider == model.provider and msg.api == model.api
    parts: list[dict[str, Any]] = []

    for block in msg.content:
        if isinstance(block, TextContent):
            if not block.text:
                continue
            part: dict[str, Any] = {"text": sanitize_surrogates(block.text)}
            parts.append(part)

        elif isinstance(block, ThinkingContent):
            if not block.thinking:
                continue
            if is_same and block.signature:
                # Same model: preserve as thinking part
                part = {"text": block.thinking, "thought": True}
                if block.signature:
                    part["thoughtSignature"] = block.signature
                parts.append(part)
            elif block.redacted:
                # Redacted thinking from different model — skip
                continue
            else:
                # Cross-model: convert thinking to plain text
                parts.append({"text": block.thinking})

        elif isinstance(block, ToolCall):
            fc: dict[str, Any] = {"name": block.name, "args": block.arguments}
            part = {"functionCall": fc}
            parts.append(part)

    if not parts:
        return None

    return {"role": "model", "parts": parts}


def _convert_tool_result(msg: ToolResultMessage) -> dict[str, Any]:
    """Convert a tool result to Gemini functionResponse part."""
    # Collect text content
    text_parts: list[str] = []
    for block in msg.content:
        if isinstance(block, TextContent):
            text_parts.append(sanitize_surrogates(block.text))

    output_text = "\n".join(text_parts) if text_parts else ""

    response: dict[str, Any] = {"error": output_text} if msg.is_error else {"output": output_text}

    return {"functionResponse": {"name": msg.tool_name, "response": response}}


def convert_tools(tools: list[Tool]) -> list[dict[str, Any]]:
    """Convert Tool definitions to Gemini functionDeclarations format."""
    declarations: list[dict[str, Any]] = []
    for tool in tools:
        decl: dict[str, Any] = {
            "name": tool.name,
            "description": tool.description,
        }
        # Use parametersJsonSchema for full JSON Schema support
        if tool.parameters:
            decl["parametersJsonSchema"] = tool.parameters
        declarations.append(decl)

    return [{"functionDeclarations": declarations}]


def map_stop_reason(finish_reason: str | None) -> str:
    """Map Gemini finishReason to dino-ai StopReason."""
    if not finish_reason:
        return "stop"
    r = finish_reason.upper()
    if r == "STOP":
        return "stop"
    if r == "MAX_TOKENS":
        return "length"
    # All safety/content/other reasons → error
    return "error"
