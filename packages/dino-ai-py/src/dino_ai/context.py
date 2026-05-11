"""Context and message types."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from dino_ai.content import AssistantContentBlock, ToolResultContentBlock, UserContentBlock
from dino_ai.error import DinoError
from dino_ai.usage import Usage

# ── Stop reasons ─────────────────────────────────────────────────

StopReason = str  # "stop" | "length" | "toolUse" | "error" | "aborted"

STOP_REASON_STOP: StopReason = "stop"
STOP_REASON_LENGTH: StopReason = "length"
STOP_REASON_TOOL_USE: StopReason = "toolUse"
STOP_REASON_ERROR: StopReason = "error"
STOP_REASON_ABORTED: StopReason = "aborted"


# ── Messages ─────────────────────────────────────────────────────


@dataclass
class UserMessage:
    """Message from the user (or an agent acting as user)."""

    content: str | list[UserContentBlock]
    role: str = field(default="user", init=False)
    timestamp: int = 0
    metadata: dict[str, Any] | None = None


@dataclass
class AssistantMessage:
    """Response from the model."""

    content: list[AssistantContentBlock] = field(default_factory=list)
    role: str = field(default="assistant", init=False)
    model: str = ""
    response_model: str | None = None
    response_id: str | None = None
    provider: str = ""
    api: str = ""
    usage: Usage = field(default_factory=Usage)
    stop_reason: StopReason = STOP_REASON_STOP
    error: DinoError | None = None
    timestamp: int = 0
    metadata: dict[str, Any] | None = None


@dataclass
class ToolResultMessage:
    """Result of a tool call, sent back to the model."""

    tool_call_id: str
    tool_name: str
    content: list[ToolResultContentBlock] = field(default_factory=list)
    role: str = field(default="toolResult", init=False)
    is_error: bool = False
    timestamp: int = 0
    metadata: dict[str, Any] | None = None


Message = UserMessage | AssistantMessage | ToolResultMessage


# ── Tool ─────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Tool:
    """Tool definition with JSON Schema parameters."""

    name: str
    description: str
    parameters: dict[str, Any]  # JSON Schema object


# ── Context ──────────────────────────────────────────────────────


@dataclass
class Context:
    """Serializable conversation state. Passable between models for cross-provider handoff."""

    messages: list[Message] = field(default_factory=list)
    system_prompt: str | None = None
    tools: list[Tool] = field(default_factory=list)
