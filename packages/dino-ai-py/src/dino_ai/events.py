"""Streaming event types — the unified event protocol."""

from __future__ import annotations

from dataclasses import dataclass

from dino_ai.content import ToolCall
from dino_ai.context import AssistantMessage, StopReason
from dino_ai.error import DinoError


@dataclass(frozen=True)
class StreamStart:
    """Emitted once at the beginning of a stream."""

    partial: AssistantMessage
    type: str = "start"


@dataclass(frozen=True)
class TextStart:
    """A new text content block has started."""

    content_index: int
    partial: AssistantMessage
    type: str = "text_start"


@dataclass(frozen=True)
class TextDelta:
    """Incremental text chunk."""

    content_index: int
    delta: str
    partial: AssistantMessage
    type: str = "text_delta"


@dataclass(frozen=True)
class TextEnd:
    """A text content block has finished."""

    content_index: int
    text: str
    partial: AssistantMessage
    type: str = "text_end"


@dataclass(frozen=True)
class ThinkingStart:
    """A new thinking/reasoning block has started."""

    content_index: int
    partial: AssistantMessage
    type: str = "thinking_start"


@dataclass(frozen=True)
class ThinkingDelta:
    """Incremental thinking chunk."""

    content_index: int
    delta: str
    partial: AssistantMessage
    type: str = "thinking_delta"


@dataclass(frozen=True)
class ThinkingEnd:
    """A thinking block has finished."""

    content_index: int
    text: str
    partial: AssistantMessage
    type: str = "thinking_end"


@dataclass(frozen=True)
class ToolCallStart:
    """A new tool call has started."""

    content_index: int
    partial: AssistantMessage
    type: str = "toolcall_start"


@dataclass(frozen=True)
class ToolCallDelta:
    """Incremental tool call arguments chunk."""

    content_index: int
    delta: str
    partial: AssistantMessage
    type: str = "toolcall_delta"


@dataclass(frozen=True)
class ToolCallEnd:
    """A tool call has finished with complete arguments."""

    content_index: int
    tool_call: ToolCall
    partial: AssistantMessage
    type: str = "toolcall_end"


@dataclass(frozen=True)
class StreamDone:
    """Stream completed successfully."""

    reason: StopReason
    message: AssistantMessage
    type: str = "done"


@dataclass(frozen=True)
class StreamError:
    """Stream terminated with an error."""

    reason: StopReason
    error: DinoError
    message: AssistantMessage
    type: str = "error"


AssistantMessageEvent = (
    StreamStart
    | TextStart
    | TextDelta
    | TextEnd
    | ThinkingStart
    | ThinkingDelta
    | ThinkingEnd
    | ToolCallStart
    | ToolCallDelta
    | ToolCallEnd
    | StreamDone
    | StreamError
)
