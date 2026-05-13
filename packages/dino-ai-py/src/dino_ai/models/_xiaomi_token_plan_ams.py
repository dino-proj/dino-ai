"""Auto-generated models for xiaomi-token-plan-ams.

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


class XiaomiTokenPlanAms:
    """Models for xiaomi-token-plan-ams."""

    MIMO_V2_FLASH = Model(
        id="mimo-v2-flash",
        name="MiMo-V2-Flash",
        api="openai-completions",
        provider="xiaomi-token-plan-ams",
        base_url="https://token-plan-ams.xiaomimimo.com/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MIMO_V2_OMNI = Model(
        id="mimo-v2-omni",
        name="MiMo-V2-Omni",
        api="openai-completions",
        provider="xiaomi-token-plan-ams",
        base_url="https://token-plan-ams.xiaomimimo.com/v1",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MIMO_V2_PRO = Model(
        id="mimo-v2-pro",
        name="MiMo-V2-Pro",
        api="openai-completions",
        provider="xiaomi-token-plan-ams",
        base_url="https://token-plan-ams.xiaomimimo.com/v1",
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
            context_window=1048576,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MIMO_V2_5 = Model(
        id="mimo-v2.5",
        name="MiMo-V2.5",
        api="openai-completions",
        provider="xiaomi-token-plan-ams",
        base_url="https://token-plan-ams.xiaomimimo.com/v1",
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
            context_window=1048576,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MIMO_V2_5_PRO = Model(
        id="mimo-v2.5-pro",
        name="MiMo-V2.5-Pro",
        api="openai-completions",
        provider="xiaomi-token-plan-ams",
        base_url="https://token-plan-ams.xiaomimimo.com/v1",
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
            context_window=1048576,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )
