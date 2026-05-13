"""Auto-generated models for moonshotai.

DO NOT EDIT — run `python scripts/generate_models.py` to regenerate.
"""

from __future__ import annotations

from dino_ai.model import (
    Model,
    ModelCapabilities,
    ModelLimits,
    ModelPricing,
    ModelThinkingLevel,
)


class Moonshotai:
    """Models for moonshotai."""

    KIMI_K2_0711_PREVIEW = Model(
        id="kimi-k2-0711-preview",
        name="Kimi K2 0711",
        api="openai-completions",
        provider="moonshotai",
        base_url="https://api.moonshot.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.5,
            cache_read=0.15,
            cache_write=0,
        ),
    )

    KIMI_K2_0905_PREVIEW = Model(
        id="kimi-k2-0905-preview",
        name="Kimi K2 0905",
        api="openai-completions",
        provider="moonshotai",
        base_url="https://api.moonshot.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.5,
            cache_read=0.15,
            cache_write=0,
        ),
    )

    KIMI_K2_THINKING = Model(
        id="kimi-k2-thinking",
        name="Kimi K2 Thinking",
        api="openai-completions",
        provider="moonshotai",
        base_url="https://api.moonshot.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(
                ModelThinkingLevel.OFF,
                ModelThinkingLevel.LOW,
                ModelThinkingLevel.MEDIUM,
                ModelThinkingLevel.HIGH,
            ),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.5,
            cache_read=0.15,
            cache_write=0,
        ),
    )

    KIMI_K2_THINKING_TURBO = Model(
        id="kimi-k2-thinking-turbo",
        name="Kimi K2 Thinking Turbo",
        api="openai-completions",
        provider="moonshotai",
        base_url="https://api.moonshot.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(
                ModelThinkingLevel.OFF,
                ModelThinkingLevel.LOW,
                ModelThinkingLevel.MEDIUM,
                ModelThinkingLevel.HIGH,
            ),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=1.15,
            output=8,
            cache_read=0.15,
            cache_write=0,
        ),
    )

    KIMI_K2_TURBO_PREVIEW = Model(
        id="kimi-k2-turbo-preview",
        name="Kimi K2 Turbo",
        api="openai-completions",
        provider="moonshotai",
        base_url="https://api.moonshot.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=2.4,
            output=10,
            cache_read=0.6,
            cache_write=0,
        ),
    )

    KIMI_K2_5 = Model(
        id="kimi-k2.5",
        name="Kimi K2.5",
        api="openai-completions",
        provider="moonshotai",
        base_url="https://api.moonshot.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(
                ModelThinkingLevel.OFF,
                ModelThinkingLevel.LOW,
                ModelThinkingLevel.MEDIUM,
                ModelThinkingLevel.HIGH,
            ),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=3,
            cache_read=0.1,
            cache_write=0,
        ),
    )

    KIMI_K2_6 = Model(
        id="kimi-k2.6",
        name="Kimi K2.6",
        api="openai-completions",
        provider="moonshotai",
        base_url="https://api.moonshot.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(
                ModelThinkingLevel.OFF,
                ModelThinkingLevel.LOW,
                ModelThinkingLevel.MEDIUM,
                ModelThinkingLevel.HIGH,
            ),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0.95,
            output=4,
            cache_read=0.16,
            cache_write=0,
        ),
    )
