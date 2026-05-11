"""Model descriptor and related types."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Literal


class ThinkingLevel(Enum):
    """Unified thinking/reasoning effort levels."""

    MINIMAL = "minimal"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ModelThinkingLevel(Enum):
    """Thinking levels including off."""

    OFF = "off"
    MINIMAL = "minimal"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    XHIGH = "xhigh"


# Known API protocol identifiers
ApiType = Literal[
    "openai-completions",
    "openai-responses",
    "azure-openai-responses",
    "anthropic-messages",
    "bedrock-converse-stream",
    "google-generative-ai",
    "google-vertex",
    "mistral-conversations",
]


@dataclass(frozen=True)
class ModelCapabilities:
    """What a model supports."""

    reasoning: bool = False
    vision: bool = False
    tool_calling: bool = True
    streaming: bool = True
    supported_thinking_levels: tuple[ModelThinkingLevel, ...] = (ModelThinkingLevel.OFF,)


@dataclass(frozen=True)
class ModelLimits:
    """Token limits for a model."""

    context_window: int = 0
    max_output_tokens: int = 0


@dataclass(frozen=True)
class ModelPricing:
    """Cost per million tokens in USD."""

    input: float = 0.0
    output: float = 0.0
    cache_read: float = 0.0
    cache_write: float = 0.0


@dataclass(frozen=True)
class Model:
    """Immutable descriptor of a model endpoint."""

    id: str
    name: str
    api: str  # ApiType or custom string
    provider: str
    base_url: str
    capabilities: ModelCapabilities = field(default_factory=ModelCapabilities)
    limits: ModelLimits = field(default_factory=ModelLimits)
    pricing: ModelPricing = field(default_factory=ModelPricing)
