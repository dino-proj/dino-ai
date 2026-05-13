"""Auto-generated models for xai.

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


class Xai:
    """Models for xai."""

    GROK_2 = Model(
        id="grok-2",
        name="Grok 2",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=2,
            output=10,
            cache_read=2,
            cache_write=0,
        ),
    )

    GROK_2_1212 = Model(
        id="grok-2-1212",
        name="Grok 2 (1212)",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=2,
            output=10,
            cache_read=2,
            cache_write=0,
        ),
    )

    GROK_2_LATEST = Model(
        id="grok-2-latest",
        name="Grok 2 Latest",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=2,
            output=10,
            cache_read=2,
            cache_write=0,
        ),
    )

    GROK_2_VISION = Model(
        id="grok-2-vision",
        name="Grok 2 Vision",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8192,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=2,
            output=10,
            cache_read=2,
            cache_write=0,
        ),
    )

    GROK_2_VISION_1212 = Model(
        id="grok-2-vision-1212",
        name="Grok 2 Vision (1212)",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8192,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=2,
            output=10,
            cache_read=2,
            cache_write=0,
        ),
    )

    GROK_2_VISION_LATEST = Model(
        id="grok-2-vision-latest",
        name="Grok 2 Vision Latest",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8192,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=2,
            output=10,
            cache_read=2,
            cache_write=0,
        ),
    )

    GROK_3 = Model(
        id="grok-3",
        name="Grok 3",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.75,
            cache_write=0,
        ),
    )

    GROK_3_FAST = Model(
        id="grok-3-fast",
        name="Grok 3 Fast",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=5,
            output=25,
            cache_read=1.25,
            cache_write=0,
        ),
    )

    GROK_3_FAST_LATEST = Model(
        id="grok-3-fast-latest",
        name="Grok 3 Fast Latest",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=5,
            output=25,
            cache_read=1.25,
            cache_write=0,
        ),
    )

    GROK_3_LATEST = Model(
        id="grok-3-latest",
        name="Grok 3 Latest",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.75,
            cache_write=0,
        ),
    )

    GROK_3_MINI = Model(
        id="grok-3-mini",
        name="Grok 3 Mini",
        api="openai-completions",
        provider="xai",
        base_url="",
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
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=0.5,
            cache_read=0.075,
            cache_write=0,
        ),
    )

    GROK_3_MINI_FAST = Model(
        id="grok-3-mini-fast",
        name="Grok 3 Mini Fast",
        api="openai-completions",
        provider="xai",
        base_url="",
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
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=4,
            cache_read=0.15,
            cache_write=0,
        ),
    )

    GROK_3_MINI_FAST_LATEST = Model(
        id="grok-3-mini-fast-latest",
        name="Grok 3 Mini Fast Latest",
        api="openai-completions",
        provider="xai",
        base_url="",
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
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=4,
            cache_read=0.15,
            cache_write=0,
        ),
    )

    GROK_3_MINI_LATEST = Model(
        id="grok-3-mini-latest",
        name="Grok 3 Mini Latest",
        api="openai-completions",
        provider="xai",
        base_url="",
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
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=0.5,
            cache_read=0.075,
            cache_write=0,
        ),
    )

    GROK_4 = Model(
        id="grok-4",
        name="Grok 4",
        api="openai-completions",
        provider="xai",
        base_url="",
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
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.75,
            cache_write=0,
        ),
    )

    GROK_4_1_FAST = Model(
        id="grok-4-1-fast",
        name="Grok 4.1 Fast",
        api="openai-completions",
        provider="xai",
        base_url="",
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
            context_window=2000000,
            max_output_tokens=30000,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.5,
            cache_read=0.05,
            cache_write=0,
        ),
    )

    GROK_4_1_FAST_NON_REASONING = Model(
        id="grok-4-1-fast-non-reasoning",
        name="Grok 4.1 Fast (Non-Reasoning)",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=2000000,
            max_output_tokens=30000,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.5,
            cache_read=0.05,
            cache_write=0,
        ),
    )

    GROK_4_FAST = Model(
        id="grok-4-fast",
        name="Grok 4 Fast",
        api="openai-completions",
        provider="xai",
        base_url="",
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
            context_window=2000000,
            max_output_tokens=30000,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.5,
            cache_read=0.05,
            cache_write=0,
        ),
    )

    GROK_4_FAST_NON_REASONING = Model(
        id="grok-4-fast-non-reasoning",
        name="Grok 4 Fast (Non-Reasoning)",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=2000000,
            max_output_tokens=30000,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.5,
            cache_read=0.05,
            cache_write=0,
        ),
    )

    GROK_4_20_0309_NON_REASONING = Model(
        id="grok-4.20-0309-non-reasoning",
        name="Grok 4.20 (Non-Reasoning)",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=2000000,
            max_output_tokens=30000,
        ),
        pricing=ModelPricing(
            input=2,
            output=6,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    GROK_4_20_0309_REASONING = Model(
        id="grok-4.20-0309-reasoning",
        name="Grok 4.20 (Reasoning)",
        api="openai-completions",
        provider="xai",
        base_url="",
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
            context_window=2000000,
            max_output_tokens=30000,
        ),
        pricing=ModelPricing(
            input=2,
            output=6,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    GROK_4_3 = Model(
        id="grok-4.3",
        name="Grok 4.3",
        api="openai-completions",
        provider="xai",
        base_url="",
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
            context_window=1000000,
            max_output_tokens=30000,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=2.5,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    GROK_BETA = Model(
        id="grok-beta",
        name="Grok Beta",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=5,
            output=15,
            cache_read=5,
            cache_write=0,
        ),
    )

    GROK_CODE_FAST_1 = Model(
        id="grok-code-fast-1",
        name="Grok Code Fast 1",
        api="openai-completions",
        provider="xai",
        base_url="",
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
            max_output_tokens=10000,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=1.5,
            cache_read=0.02,
            cache_write=0,
        ),
    )

    GROK_VISION_BETA = Model(
        id="grok-vision-beta",
        name="Grok Vision Beta",
        api="openai-completions",
        provider="xai",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8192,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=5,
            output=15,
            cache_read=5,
            cache_write=0,
        ),
    )
