"""Content block types for messages."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class TextContent:
    """Plain text content block."""

    text: str
    type: str = field(default="text", init=False)
    text_signature: str | None = None


@dataclass(frozen=True)
class ThinkingContent:
    """Model reasoning/thinking content block."""

    thinking: str
    type: str = field(default="thinking", init=False)
    signature: str | None = None
    redacted: bool = False


@dataclass(frozen=True)
class ImageContent:
    """Image content block (base64-encoded)."""

    data: bytes
    mime_type: str
    type: str = field(default="image", init=False)


@dataclass(frozen=True)
class ToolCall:
    """Tool/function call issued by the model."""

    id: str
    name: str
    arguments: dict[str, Any]
    type: str = field(default="toolCall", init=False)
    thought_signature: str | None = None


ContentBlock = TextContent | ThinkingContent | ImageContent | ToolCall

AssistantContentBlock = TextContent | ThinkingContent | ToolCall

UserContentBlock = TextContent | ImageContent

ToolResultContentBlock = TextContent | ImageContent
