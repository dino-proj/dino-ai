"""Auto-generated models for kimi.

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


class Kimi:
    """Models for kimi."""

    K2P5 = Model(
        id="k2p5",
        name="Kimi K2.5",
        api="anthropic-messages",
        provider="kimi",
        base_url="https://api.kimi.com/coding/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    K2P6 = Model(
        id="k2p6",
        name="Kimi K2.6",
        api="anthropic-messages",
        provider="kimi",
        base_url="https://api.kimi.com/coding/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    KIMI_K2_THINKING = Model(
        id="kimi-k2-thinking",
        name="Kimi K2 Thinking",
        api="anthropic-messages",
        provider="kimi",
        base_url="https://api.kimi.com/coding/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )
