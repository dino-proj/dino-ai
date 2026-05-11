"""OpenAI-compatible provider configuration profiles.

Different providers use variants of the OpenAI API. This module defines
the knobs that control how requests are built and responses parsed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ThinkingFormat = Literal[
    "none",
    "openai",       # reasoning_effort param (o-series)
    "deepseek",     # thinking: {type: "enabled"} + reasoning_effort
    "openrouter",   # reasoning: {effort: ...}
    "together",     # reasoning: {enabled: true}
    "zai",          # enable_thinking param
    "qwen",         # enable_thinking param (Qwen)
]

MaxTokensField = Literal["max_completion_tokens", "max_tokens"]

CacheControlFormat = Literal["anthropic", "none"]


@dataclass(frozen=True)
class OpenAICompatProfile:
    """Configuration profile for an OpenAI-compatible provider.

    Each field controls a specific behavior difference from the
    canonical OpenAI Chat Completions API.
    """

    # How to request reasoning/thinking
    thinking_format: ThinkingFormat = "none"

    # Whether the provider supports reasoning_effort directly
    supports_reasoning_effort: bool = False

    # Whether to send stream_options.include_usage
    supports_usage_in_streaming: bool = True

    # Whether to send store: false
    supports_store: bool = False

    # Which field name to use for max output tokens
    max_tokens_field: MaxTokensField = "max_completion_tokens"

    # Whether tools support strict mode
    supports_strict_mode: bool = False

    # Whether to send session affinity headers
    send_session_affinity_headers: bool = False

    # Whether long cache retention (24h) is supported
    supports_long_cache_retention: bool = False

    # Whether the provider needs an assistant after tool results
    requires_assistant_after_tool_result: bool = False

    # Anthropic-style cache_control markers
    cache_control_format: CacheControlFormat = "none"

    # Use "developer" role instead of "system"
    use_developer_role: bool = False

    # ZAI-style tool_stream param
    zai_tool_stream: bool = False

    # OpenRouter routing preferences
    openrouter_routing: dict[str, str] | None = None

    # Reasoning content field names to check (in priority order)
    reasoning_fields: tuple[str, ...] = ("reasoning_content", "reasoning", "reasoning_text")


# ── Pre-built profiles for known providers ──────────────────────


PROFILE_OPENAI = OpenAICompatProfile(
    thinking_format="openai",
    supports_reasoning_effort=True,
    supports_usage_in_streaming=True,
    supports_store=True,
    max_tokens_field="max_completion_tokens",
    supports_long_cache_retention=True,
    send_session_affinity_headers=True,
    use_developer_role=True,
)

PROFILE_OPENAI_COMPAT = OpenAICompatProfile(
    supports_usage_in_streaming=True,
    max_tokens_field="max_completion_tokens",
)

PROFILE_DEEPSEEK = OpenAICompatProfile(
    thinking_format="deepseek",
    supports_reasoning_effort=True,
    max_tokens_field="max_tokens",
)

PROFILE_XAI = OpenAICompatProfile(
    supports_usage_in_streaming=True,
    max_tokens_field="max_tokens",
)

PROFILE_GROQ = OpenAICompatProfile(
    supports_usage_in_streaming=True,
    max_tokens_field="max_tokens",
)

PROFILE_OPENROUTER = OpenAICompatProfile(
    thinking_format="openrouter",
    supports_usage_in_streaming=True,
    cache_control_format="anthropic",
)

PROFILE_TOGETHER = OpenAICompatProfile(
    thinking_format="together",
    supports_reasoning_effort=True,
    max_tokens_field="max_tokens",
)

PROFILE_MISTRAL = OpenAICompatProfile(
    supports_usage_in_streaming=True,
    max_tokens_field="max_tokens",
)


def detect_profile(provider: str, base_url: str) -> OpenAICompatProfile:
    """Auto-detect the compat profile from provider name and base URL.

    Falls back to a generic profile for unknown providers.
    """
    p = provider.lower()

    if p == "openai":
        return PROFILE_OPENAI
    if p == "deepseek":
        return PROFILE_DEEPSEEK
    if p in ("xai", "x-ai"):
        return PROFILE_XAI
    if p == "groq":
        return PROFILE_GROQ
    if p == "openrouter":
        return PROFILE_OPENROUTER
    if p == "together":
        return PROFILE_TOGETHER
    if p == "mistral":
        return PROFILE_MISTRAL

    # URL-based detection
    if "openrouter.ai" in base_url:
        return PROFILE_OPENROUTER
    if "api.deepseek.com" in base_url:
        return PROFILE_DEEPSEEK
    if "api.x.ai" in base_url:
        return PROFILE_XAI
    if "api.groq.com" in base_url:
        return PROFILE_GROQ
    if "api.together.xyz" in base_url or "api.together.ai" in base_url:
        return PROFILE_TOGETHER

    return PROFILE_OPENAI_COMPAT
