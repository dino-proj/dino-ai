"""Auto-generated models for deepseek.

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


class Deepseek:
    """Models for deepseek."""

    DEEPSEEK_CHAT = Model(
        id="deepseek-chat",
        name="DeepSeek Chat",
        api="openai-completions",
        provider="deepseek",
        base_url="https://api.deepseek.com",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=384000,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=0.28,
            cache_read=0.028,
            cache_write=0,
        ),
    )

    DEEPSEEK_REASONER = Model(
        id="deepseek-reasoner",
        name="DeepSeek Reasoner",
        api="openai-completions",
        provider="deepseek",
        base_url="https://api.deepseek.com",
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
            context_window=1000000,
            max_output_tokens=384000,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=0.28,
            cache_read=0.028,
            cache_write=0,
        ),
    )

    DEEPSEEK_V4_FLASH = Model(
        id="deepseek-v4-flash",
        name="DeepSeek V4 Flash",
        api="openai-completions",
        provider="deepseek",
        base_url="https://api.deepseek.com",
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
            context_window=1000000,
            max_output_tokens=384000,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=0.28,
            cache_read=0.028,
            cache_write=0,
        ),
    )

    DEEPSEEK_V4_PRO = Model(
        id="deepseek-v4-pro",
        name="DeepSeek V4 Pro",
        api="openai-completions",
        provider="deepseek",
        base_url="https://api.deepseek.com",
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
            context_window=1000000,
            max_output_tokens=384000,
        ),
        pricing=ModelPricing(
            input=1.74,
            output=3.48,
            cache_read=0.145,
            cache_write=0,
        ),
    )
