"""Stream options and configuration."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import Any

from dino_ai.model import Model, ThinkingLevel

# Callback type aliases
PayloadHook = Callable[[Any, Model], Awaitable[Any | None] | Any | None]
ResponseHook = Callable[[int, dict[str, str], Model], Awaitable[None] | None]


@dataclass
class StreamOptions:
    """Options for stream() and complete() calls."""

    temperature: float | None = None
    max_tokens: int | None = None
    api_key: str | None = None
    cache_retention: str | None = None  # "none" | "short" | "long"
    session_id: str | None = None
    headers: dict[str, str] | None = None
    timeout_ms: int | None = None
    max_retries: int | None = None
    metadata: dict[str, Any] | None = None
    on_payload: PayloadHook | None = None
    on_response: ResponseHook | None = None


@dataclass
class SimpleStreamOptions(StreamOptions):
    """Options for streamSimple() with unified reasoning level."""

    reasoning: ThinkingLevel | None = None
    thinking_budgets: dict[ThinkingLevel, int] = field(default_factory=dict)
