"""Auto-generated models for amazon-bedrock.

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


class AmazonBedrock:
    """Models for amazon-bedrock."""

    AMAZON_NOVA_2_LITE_V1_0 = Model(
        id="amazon.nova-2-lite-v1:0",
        name="Nova 2 Lite",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.33,
            output=2.75,
            cache_read=0,
            cache_write=0,
        ),
    )

    AMAZON_NOVA_LITE_V1_0 = Model(
        id="amazon.nova-lite-v1:0",
        name="Nova Lite",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=300000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.06,
            output=0.24,
            cache_read=0.015,
            cache_write=0,
        ),
    )

    AMAZON_NOVA_MICRO_V1_0 = Model(
        id="amazon.nova-micro-v1:0",
        name="Nova Micro",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.035,
            output=0.14,
            cache_read=0.00875,
            cache_write=0,
        ),
    )

    AMAZON_NOVA_PRO_V1_0 = Model(
        id="amazon.nova-pro-v1:0",
        name="Nova Pro",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=300000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.8,
            output=3.2,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    ANTHROPIC_CLAUDE_HAIKU_4_5_20251001_V1_0 = Model(
        id="anthropic.claude-haiku-4-5-20251001-v1:0",
        name="Claude Haiku 4.5",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    ANTHROPIC_CLAUDE_OPUS_4_1_20250805_V1_0 = Model(
        id="anthropic.claude-opus-4-1-20250805-v1:0",
        name="Claude Opus 4.1",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    ANTHROPIC_CLAUDE_OPUS_4_5_20251101_V1_0 = Model(
        id="anthropic.claude-opus-4-5-20251101-v1:0",
        name="Claude Opus 4.5",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    ANTHROPIC_CLAUDE_OPUS_4_6_V1 = Model(
        id="anthropic.claude-opus-4-6-v1",
        name="Claude Opus 4.6",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    ANTHROPIC_CLAUDE_OPUS_4_7 = Model(
        id="anthropic.claude-opus-4-7",
        name="Claude Opus 4.7",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    ANTHROPIC_CLAUDE_SONNET_4_5_20250929_V1_0 = Model(
        id="anthropic.claude-sonnet-4-5-20250929-v1:0",
        name="Claude Sonnet 4.5",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    ANTHROPIC_CLAUDE_SONNET_4_6 = Model(
        id="anthropic.claude-sonnet-4-6",
        name="Claude Sonnet 4.6",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    AU_ANTHROPIC_CLAUDE_HAIKU_4_5_20251001_V1_0 = Model(
        id="au.anthropic.claude-haiku-4-5-20251001-v1:0",
        name="Claude Haiku 4.5 (AU)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    AU_ANTHROPIC_CLAUDE_OPUS_4_6_V1 = Model(
        id="au.anthropic.claude-opus-4-6-v1",
        name="AU Anthropic Claude Opus 4.6",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            input=16.5,
            output=82.5,
            cache_read=1.65,
            cache_write=20.625,
        ),
    )

    AU_ANTHROPIC_CLAUDE_SONNET_4_5_20250929_V1_0 = Model(
        id="au.anthropic.claude-sonnet-4-5-20250929-v1:0",
        name="Claude Sonnet 4.5 (AU)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    AU_ANTHROPIC_CLAUDE_SONNET_4_6 = Model(
        id="au.anthropic.claude-sonnet-4-6",
        name="AU Anthropic Claude Sonnet 4.6",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            input=3.3,
            output=16.5,
            cache_read=0.33,
            cache_write=4.125,
        ),
    )

    DEEPSEEK_R1_V1_0 = Model(
        id="deepseek.r1-v1:0",
        name="DeepSeek-R1",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=128000,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=1.35,
            output=5.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_V3_V1_0 = Model(
        id="deepseek.v3-v1:0",
        name="DeepSeek-V3.1",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=163840,
            max_output_tokens=81920,
        ),
        pricing=ModelPricing(
            input=0.58,
            output=1.68,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_V3_2 = Model(
        id="deepseek.v3.2",
        name="DeepSeek-V3.2",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=163840,
            max_output_tokens=81920,
        ),
        pricing=ModelPricing(
            input=0.62,
            output=1.85,
            cache_read=0,
            cache_write=0,
        ),
    )

    EU_ANTHROPIC_CLAUDE_HAIKU_4_5_20251001_V1_0 = Model(
        id="eu.anthropic.claude-haiku-4-5-20251001-v1:0",
        name="Claude Haiku 4.5 (EU)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    EU_ANTHROPIC_CLAUDE_OPUS_4_5_20251101_V1_0 = Model(
        id="eu.anthropic.claude-opus-4-5-20251101-v1:0",
        name="Claude Opus 4.5 (EU)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    EU_ANTHROPIC_CLAUDE_OPUS_4_6_V1 = Model(
        id="eu.anthropic.claude-opus-4-6-v1",
        name="Claude Opus 4.6 (EU)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    EU_ANTHROPIC_CLAUDE_OPUS_4_7 = Model(
        id="eu.anthropic.claude-opus-4-7",
        name="Claude Opus 4.7 (EU)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    EU_ANTHROPIC_CLAUDE_SONNET_4_5_20250929_V1_0 = Model(
        id="eu.anthropic.claude-sonnet-4-5-20250929-v1:0",
        name="Claude Sonnet 4.5 (EU)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    EU_ANTHROPIC_CLAUDE_SONNET_4_6 = Model(
        id="eu.anthropic.claude-sonnet-4-6",
        name="Claude Sonnet 4.6 (EU)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    GLOBAL_ANTHROPIC_CLAUDE_HAIKU_4_5_20251001_V1_0 = Model(
        id="global.anthropic.claude-haiku-4-5-20251001-v1:0",
        name="Claude Haiku 4.5 (Global)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    GLOBAL_ANTHROPIC_CLAUDE_OPUS_4_5_20251101_V1_0 = Model(
        id="global.anthropic.claude-opus-4-5-20251101-v1:0",
        name="Claude Opus 4.5 (Global)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    GLOBAL_ANTHROPIC_CLAUDE_OPUS_4_6_V1 = Model(
        id="global.anthropic.claude-opus-4-6-v1",
        name="Claude Opus 4.6 (Global)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    GLOBAL_ANTHROPIC_CLAUDE_OPUS_4_7 = Model(
        id="global.anthropic.claude-opus-4-7",
        name="Claude Opus 4.7 (Global)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    GLOBAL_ANTHROPIC_CLAUDE_SONNET_4_5_20250929_V1_0 = Model(
        id="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
        name="Claude Sonnet 4.5 (Global)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    GLOBAL_ANTHROPIC_CLAUDE_SONNET_4_6 = Model(
        id="global.anthropic.claude-sonnet-4-6",
        name="Claude Sonnet 4.6 (Global)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    GOOGLE_GEMMA_3_27B_IT = Model(
        id="google.gemma-3-27b-it",
        name="Google Gemma 3 27B Instruct",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=202752,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.12,
            output=0.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    GOOGLE_GEMMA_3_4B_IT = Model(
        id="google.gemma-3-4b-it",
        name="Gemma 3 4B IT",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.04,
            output=0.08,
            cache_read=0,
            cache_write=0,
        ),
    )

    JP_ANTHROPIC_CLAUDE_OPUS_4_7 = Model(
        id="jp.anthropic.claude-opus-4-7",
        name="Claude Opus 4.7 (JP)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    JP_ANTHROPIC_CLAUDE_SONNET_4_5_20250929_V1_0 = Model(
        id="jp.anthropic.claude-sonnet-4-5-20250929-v1:0",
        name="Claude Sonnet 4.5 (JP)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    JP_ANTHROPIC_CLAUDE_SONNET_4_6 = Model(
        id="jp.anthropic.claude-sonnet-4-6",
        name="Claude Sonnet 4.6 (JP)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    META_LLAMA3_1_70B_INSTRUCT_V1_0 = Model(
        id="meta.llama3-1-70b-instruct-v1:0",
        name="Llama 3.1 70B Instruct",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.72,
            output=0.72,
            cache_read=0,
            cache_write=0,
        ),
    )

    META_LLAMA3_1_8B_INSTRUCT_V1_0 = Model(
        id="meta.llama3-1-8b-instruct-v1:0",
        name="Llama 3.1 8B Instruct",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.22,
            output=0.22,
            cache_read=0,
            cache_write=0,
        ),
    )

    META_LLAMA3_3_70B_INSTRUCT_V1_0 = Model(
        id="meta.llama3-3-70b-instruct-v1:0",
        name="Llama 3.3 70B Instruct",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.72,
            output=0.72,
            cache_read=0,
            cache_write=0,
        ),
    )

    META_LLAMA4_MAVERICK_17B_INSTRUCT_V1_0 = Model(
        id="meta.llama4-maverick-17b-instruct-v1:0",
        name="Llama 4 Maverick 17B Instruct",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.24,
            output=0.97,
            cache_read=0,
            cache_write=0,
        ),
    )

    META_LLAMA4_SCOUT_17B_INSTRUCT_V1_0 = Model(
        id="meta.llama4-scout-17b-instruct-v1:0",
        name="Llama 4 Scout 17B Instruct",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=3500000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.17,
            output=0.66,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX_MINIMAX_M2 = Model(
        id="minimax.minimax-m2",
        name="MiniMax M2",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=204608,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX_MINIMAX_M2_1 = Model(
        id="minimax.minimax-m2.1",
        name="MiniMax M2.1",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    MINIMAX_MINIMAX_M2_5 = Model(
        id="minimax.minimax-m2.5",
        name="MiniMax M2.5",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=196608,
            max_output_tokens=98304,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_DEVSTRAL_2_123B = Model(
        id="mistral.devstral-2-123b",
        name="Devstral 2 123B",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=256000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_MAGISTRAL_SMALL_2509 = Model(
        id="mistral.magistral-small-2509",
        name="Magistral Small 1.2",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=128000,
            max_output_tokens=40000,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=1.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_MINISTRAL_3_14B_INSTRUCT = Model(
        id="mistral.ministral-3-14b-instruct",
        name="Ministral 14B 3.0",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_MINISTRAL_3_3B_INSTRUCT = Model(
        id="mistral.ministral-3-3b-instruct",
        name="Ministral 3 3B",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=256000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.1,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_MINISTRAL_3_8B_INSTRUCT = Model(
        id="mistral.ministral-3-8b-instruct",
        name="Ministral 3 8B",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.15,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_MISTRAL_LARGE_3_675B_INSTRUCT = Model(
        id="mistral.mistral-large-3-675b-instruct",
        name="Mistral Large 3",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=256000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=1.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_PIXTRAL_LARGE_2502_V1_0 = Model(
        id="mistral.pixtral-large-2502-v1:0",
        name="Pixtral Large (25.02)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=2,
            output=6,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_VOXTRAL_MINI_3B_2507 = Model(
        id="mistral.voxtral-mini-3b-2507",
        name="Voxtral Mini 3B 2507",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.04,
            output=0.04,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_VOXTRAL_SMALL_24B_2507 = Model(
        id="mistral.voxtral-small-24b-2507",
        name="Voxtral Small 24B 2507",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.35,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOT_KIMI_K2_THINKING = Model(
        id="moonshot.kimi-k2-thinking",
        name="Kimi K2 Thinking",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            max_output_tokens=256000,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOTAI_KIMI_K2_5 = Model(
        id="moonshotai.kimi-k2.5",
        name="Kimi K2.5",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=256000,
            max_output_tokens=256000,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=3,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA_NEMOTRON_NANO_12B_V2 = Model(
        id="nvidia.nemotron-nano-12b-v2",
        name="NVIDIA Nemotron Nano 12B v2 VL BF16",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA_NEMOTRON_NANO_3_30B = Model(
        id="nvidia.nemotron-nano-3-30b",
        name="NVIDIA Nemotron Nano 3 30B",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.06,
            output=0.24,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA_NEMOTRON_NANO_9B_V2 = Model(
        id="nvidia.nemotron-nano-9b-v2",
        name="NVIDIA Nemotron Nano 9B v2",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.06,
            output=0.23,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA_NEMOTRON_SUPER_3_120B = Model(
        id="nvidia.nemotron-super-3-120b",
        name="NVIDIA Nemotron 3 Super 120B A12B",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=262144,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.65,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI_GPT_OSS_120B_1_0 = Model(
        id="openai.gpt-oss-120b-1:0",
        name="gpt-oss-120b",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI_GPT_OSS_20B_1_0 = Model(
        id="openai.gpt-oss-20b-1:0",
        name="gpt-oss-20b",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.07,
            output=0.3,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI_GPT_OSS_SAFEGUARD_120B = Model(
        id="openai.gpt-oss-safeguard-120b",
        name="GPT OSS Safeguard 120B",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI_GPT_OSS_SAFEGUARD_20B = Model(
        id="openai.gpt-oss-safeguard-20b",
        name="GPT OSS Safeguard 20B",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.07,
            output=0.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_QWEN3_235B_A22B_2507_V1_0 = Model(
        id="qwen.qwen3-235b-a22b-2507-v1:0",
        name="Qwen3 235B A22B 2507",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.22,
            output=0.88,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_QWEN3_32B_V1_0 = Model(
        id="qwen.qwen3-32b-v1:0",
        name="Qwen3 32B (dense)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=16384,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_QWEN3_CODER_30B_A3B_V1_0 = Model(
        id="qwen.qwen3-coder-30b-a3b-v1:0",
        name="Qwen3 Coder 30B A3B Instruct",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_QWEN3_CODER_480B_A35B_V1_0 = Model(
        id="qwen.qwen3-coder-480b-a35b-v1:0",
        name="Qwen3 Coder 480B A35B Instruct",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.22,
            output=1.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_QWEN3_CODER_NEXT = Model(
        id="qwen.qwen3-coder-next",
        name="Qwen3 Coder Next",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.22,
            output=1.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_QWEN3_NEXT_80B_A3B = Model(
        id="qwen.qwen3-next-80b-a3b",
        name="Qwen/Qwen3-Next-80B-A3B-Instruct",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262000,
            max_output_tokens=262000,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=1.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_QWEN3_VL_235B_A22B = Model(
        id="qwen.qwen3-vl-235b-a22b",
        name="Qwen/Qwen3-VL-235B-A22B-Instruct",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262000,
            max_output_tokens=262000,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    US_ANTHROPIC_CLAUDE_HAIKU_4_5_20251001_V1_0 = Model(
        id="us.anthropic.claude-haiku-4-5-20251001-v1:0",
        name="Claude Haiku 4.5 (US)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    US_ANTHROPIC_CLAUDE_OPUS_4_1_20250805_V1_0 = Model(
        id="us.anthropic.claude-opus-4-1-20250805-v1:0",
        name="Claude Opus 4.1 (US)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    US_ANTHROPIC_CLAUDE_OPUS_4_5_20251101_V1_0 = Model(
        id="us.anthropic.claude-opus-4-5-20251101-v1:0",
        name="Claude Opus 4.5 (US)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    US_ANTHROPIC_CLAUDE_OPUS_4_6_V1 = Model(
        id="us.anthropic.claude-opus-4-6-v1",
        name="Claude Opus 4.6 (US)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    US_ANTHROPIC_CLAUDE_OPUS_4_7 = Model(
        id="us.anthropic.claude-opus-4-7",
        name="Claude Opus 4.7 (US)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    US_ANTHROPIC_CLAUDE_SONNET_4_5_20250929_V1_0 = Model(
        id="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
        name="Claude Sonnet 4.5 (US)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    US_ANTHROPIC_CLAUDE_SONNET_4_6 = Model(
        id="us.anthropic.claude-sonnet-4-6",
        name="Claude Sonnet 4.6 (US)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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

    US_DEEPSEEK_R1_V1_0 = Model(
        id="us.deepseek.r1-v1:0",
        name="DeepSeek-R1 (US)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=128000,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=1.35,
            output=5.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    US_META_LLAMA4_MAVERICK_17B_INSTRUCT_V1_0 = Model(
        id="us.meta.llama4-maverick-17b-instruct-v1:0",
        name="Llama 4 Maverick 17B Instruct (US)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.24,
            output=0.97,
            cache_read=0,
            cache_write=0,
        ),
    )

    US_META_LLAMA4_SCOUT_17B_INSTRUCT_V1_0 = Model(
        id="us.meta.llama4-scout-17b-instruct-v1:0",
        name="Llama 4 Scout 17B Instruct (US)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=3500000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.17,
            output=0.66,
            cache_read=0,
            cache_write=0,
        ),
    )

    WRITER_PALMYRA_X4_V1_0 = Model(
        id="writer.palmyra-x4-v1:0",
        name="Palmyra X4",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=122880,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=2.5,
            output=10,
            cache_read=0,
            cache_write=0,
        ),
    )

    WRITER_PALMYRA_X5_V1_0 = Model(
        id="writer.palmyra-x5-v1:0",
        name="Palmyra X5",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=1040000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=6,
            cache_read=0,
            cache_write=0,
        ),
    )

    ZAI_GLM_4_7 = Model(
        id="zai.glm-4.7",
        name="GLM-4.7",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=204800,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    ZAI_GLM_4_7_FLASH = Model(
        id="zai.glm-4.7-flash",
        name="GLM-4.7-Flash",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=200000,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.07,
            output=0.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    ZAI_GLM_5 = Model(
        id="zai.glm-5",
        name="GLM-5",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
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
            context_window=202752,
            max_output_tokens=101376,
        ),
        pricing=ModelPricing(
            input=1,
            output=3.2,
            cache_read=0,
            cache_write=0,
        ),
    )
