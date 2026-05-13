"""Auto-generated models for stepfun.

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


class Stepfun:
    """Models for stepfun."""

    STEP_1_32K = Model(
        id="step-1-32k",
        name="Step 1 (32K)",
        api="openai-completions",
        provider="stepfun",
        base_url="https://api.stepfun.com/v1",
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
            context_window=32768,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=2.05,
            output=9.59,
            cache_read=0.41,
            cache_write=0,
        ),
    )

    STEP_2_16K = Model(
        id="step-2-16k",
        name="Step 2 (16K)",
        api="openai-completions",
        provider="stepfun",
        base_url="https://api.stepfun.com/v1",
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
            context_window=16384,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=5.21,
            output=16.44,
            cache_read=1.04,
            cache_write=0,
        ),
    )

    STEP_3_5_FLASH = Model(
        id="step-3.5-flash",
        name="Step 3.5 Flash",
        api="openai-completions",
        provider="stepfun",
        base_url="https://api.stepfun.com/v1",
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
            context_window=256000,
            max_output_tokens=256000,
        ),
        pricing=ModelPricing(
            input=0.096,
            output=0.288,
            cache_read=0.019,
            cache_write=0,
        ),
    )

    STEP_3_5_FLASH_2603 = Model(
        id="step-3.5-flash-2603",
        name="Step 3.5 Flash 2603",
        api="openai-completions",
        provider="stepfun",
        base_url="https://api.stepfun.com/v1",
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
            context_window=256000,
            max_output_tokens=256000,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.3,
            cache_read=0.02,
            cache_write=0,
        ),
    )
