"""Auto-generated models for anthropic.

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


class Anthropic:
    """Models for anthropic."""

    CLAUDE_3_5_HAIKU_20241022 = Model(
        id="claude-3-5-haiku-20241022",
        name="Claude Haiku 3.5",
        api="anthropic-messages",
        provider="anthropic",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.8,
            output=4,
            cache_read=0.08,
            cache_write=1,
        ),
    )

    CLAUDE_3_5_HAIKU_LATEST = Model(
        id="claude-3-5-haiku-latest",
        name="Claude Haiku 3.5 (latest)",
        api="anthropic-messages",
        provider="anthropic",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.8,
            output=4,
            cache_read=0.08,
            cache_write=1,
        ),
    )

    CLAUDE_3_5_SONNET_20240620 = Model(
        id="claude-3-5-sonnet-20240620",
        name="Claude Sonnet 3.5",
        api="anthropic-messages",
        provider="anthropic",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_3_5_SONNET_20241022 = Model(
        id="claude-3-5-sonnet-20241022",
        name="Claude Sonnet 3.5 v2",
        api="anthropic-messages",
        provider="anthropic",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_3_7_SONNET_20250219 = Model(
        id="claude-3-7-sonnet-20250219",
        name="Claude Sonnet 3.7",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_3_HAIKU_20240307 = Model(
        id="claude-3-haiku-20240307",
        name="Claude Haiku 3",
        api="anthropic-messages",
        provider="anthropic",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.25,
            output=1.25,
            cache_read=0.03,
            cache_write=0.3,
        ),
    )

    CLAUDE_3_OPUS_20240229 = Model(
        id="claude-3-opus-20240229",
        name="Claude Opus 3",
        api="anthropic-messages",
        provider="anthropic",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=15,
            output=75,
            cache_read=1.5,
            cache_write=18.75,
        ),
    )

    CLAUDE_3_SONNET_20240229 = Model(
        id="claude-3-sonnet-20240229",
        name="Claude Sonnet 3",
        api="anthropic-messages",
        provider="anthropic",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=0.3,
        ),
    )

    CLAUDE_HAIKU_4_5 = Model(
        id="claude-haiku-4-5",
        name="Claude Haiku 4.5 (latest)",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=1,
            output=5,
            cache_read=0.1,
            cache_write=1.25,
        ),
    )

    CLAUDE_HAIKU_4_5_20251001 = Model(
        id="claude-haiku-4-5-20251001",
        name="Claude Haiku 4.5",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=1,
            output=5,
            cache_read=0.1,
            cache_write=1.25,
        ),
    )

    CLAUDE_OPUS_4_0 = Model(
        id="claude-opus-4-0",
        name="Claude Opus 4 (latest)",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=32000,
        ),
        pricing=ModelPricing(
            input=15,
            output=75,
            cache_read=1.5,
            cache_write=18.75,
        ),
    )

    CLAUDE_OPUS_4_1 = Model(
        id="claude-opus-4-1",
        name="Claude Opus 4.1 (latest)",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=32000,
        ),
        pricing=ModelPricing(
            input=15,
            output=75,
            cache_read=1.5,
            cache_write=18.75,
        ),
    )

    CLAUDE_OPUS_4_1_20250805 = Model(
        id="claude-opus-4-1-20250805",
        name="Claude Opus 4.1",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=32000,
        ),
        pricing=ModelPricing(
            input=15,
            output=75,
            cache_read=1.5,
            cache_write=18.75,
        ),
    )

    CLAUDE_OPUS_4_20250514 = Model(
        id="claude-opus-4-20250514",
        name="Claude Opus 4",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=32000,
        ),
        pricing=ModelPricing(
            input=15,
            output=75,
            cache_read=1.5,
            cache_write=18.75,
        ),
    )

    CLAUDE_OPUS_4_5 = Model(
        id="claude-opus-4-5",
        name="Claude Opus 4.5 (latest)",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=5,
            output=25,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_OPUS_4_5_20251101 = Model(
        id="claude-opus-4-5-20251101",
        name="Claude Opus 4.5",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=5,
            output=25,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_OPUS_4_6 = Model(
        id="claude-opus-4-6",
        name="Claude Opus 4.6",
        api="anthropic-messages",
        provider="anthropic",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=5,
            output=25,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_OPUS_4_7 = Model(
        id="claude-opus-4-7",
        name="Claude Opus 4.7",
        api="anthropic-messages",
        provider="anthropic",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=5,
            output=25,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_SONNET_4_0 = Model(
        id="claude-sonnet-4-0",
        name="Claude Sonnet 4 (latest)",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_SONNET_4_20250514 = Model(
        id="claude-sonnet-4-20250514",
        name="Claude Sonnet 4",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_SONNET_4_5 = Model(
        id="claude-sonnet-4-5",
        name="Claude Sonnet 4.5 (latest)",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_SONNET_4_5_20250929 = Model(
        id="claude-sonnet-4-5-20250929",
        name="Claude Sonnet 4.5",
        api="anthropic-messages",
        provider="anthropic",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_SONNET_4_6 = Model(
        id="claude-sonnet-4-6",
        name="Claude Sonnet 4.6",
        api="anthropic-messages",
        provider="anthropic",
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
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )
