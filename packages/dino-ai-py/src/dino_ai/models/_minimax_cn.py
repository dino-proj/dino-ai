"""Auto-generated models for minimax-cn.

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


class MinimaxCn:
    """Models for minimax-cn."""

    MINIMAX_M2 = Model(
        id="MiniMax-M2",
        name="MiniMax-M2",
        api="anthropic-messages",
        provider="minimax-cn",
        base_url="https://api.minimaxi.com/anthropic/v1",
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
            context_window=196608,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX_M2_1 = Model(
        id="MiniMax-M2.1",
        name="MiniMax-M2.1",
        api="anthropic-messages",
        provider="minimax-cn",
        base_url="https://api.minimaxi.com/anthropic/v1",
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
            context_window=204800,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX_M2_5 = Model(
        id="MiniMax-M2.5",
        name="MiniMax-M2.5",
        api="anthropic-messages",
        provider="minimax-cn",
        base_url="https://api.minimaxi.com/anthropic/v1",
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
            context_window=204800,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.2,
            cache_read=0.03,
            cache_write=0.375,
        ),
    )

    MINIMAX_M2_5_HIGHSPEED = Model(
        id="MiniMax-M2.5-highspeed",
        name="MiniMax-M2.5-highspeed",
        api="anthropic-messages",
        provider="minimax-cn",
        base_url="https://api.minimaxi.com/anthropic/v1",
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
            context_window=204800,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.4,
            cache_read=0.06,
            cache_write=0.375,
        ),
    )

    MINIMAX_M2_7 = Model(
        id="MiniMax-M2.7",
        name="MiniMax-M2.7",
        api="anthropic-messages",
        provider="minimax-cn",
        base_url="https://api.minimaxi.com/anthropic/v1",
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
            context_window=204800,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.2,
            cache_read=0.06,
            cache_write=0.375,
        ),
    )

    MINIMAX_M2_7_HIGHSPEED = Model(
        id="MiniMax-M2.7-highspeed",
        name="MiniMax-M2.7-highspeed",
        api="anthropic-messages",
        provider="minimax-cn",
        base_url="https://api.minimaxi.com/anthropic/v1",
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
            context_window=204800,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.4,
            cache_read=0.06,
            cache_write=0.375,
        ),
    )
