"""Auto-generated model constants from catalog/ YAML files.

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

    CLAUDE_OPUS_4_7 = Model(
        id="claude-opus-4-7",
        name="Claude Opus 4.7",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
                ModelThinkingLevel.XHIGH,
            ),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=5.0,
            output=25.0,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_OPUS_4_6 = Model(
        id="claude-opus-4-6",
        name="Claude Opus 4.6",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
                ModelThinkingLevel.XHIGH,
            ),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=5.0,
            output=25.0,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_OPUS_4_5 = Model(
        id="claude-opus-4-5",
        name="Claude Opus 4.5 (latest)",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=5.0,
            output=25.0,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_OPUS_4_5_20251101 = Model(
        id="claude-opus-4-5-20251101",
        name="Claude Opus 4.5",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=5.0,
            output=25.0,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_OPUS_4_0 = Model(
        id="claude-opus-4-0",
        name="Claude Opus 4 (latest)",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=15.0,
            output=75.0,
            cache_read=1.5,
            cache_write=18.75,
        ),
    )

    CLAUDE_OPUS_4_20250514 = Model(
        id="claude-opus-4-20250514",
        name="Claude Opus 4",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=15.0,
            output=75.0,
            cache_read=1.5,
            cache_write=18.75,
        ),
    )

    CLAUDE_SONNET_4_6 = Model(
        id="claude-sonnet-4-6",
        name="Claude Sonnet 4.6",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=3.0,
            output=15.0,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_SONNET_4_5 = Model(
        id="claude-sonnet-4-5",
        name="Claude Sonnet 4.5 (latest)",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=3.0,
            output=15.0,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_SONNET_4_5_20250929 = Model(
        id="claude-sonnet-4-5-20250929",
        name="Claude Sonnet 4.5",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=3.0,
            output=15.0,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_SONNET_4_0 = Model(
        id="claude-sonnet-4-0",
        name="Claude Sonnet 4 (latest)",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=3.0,
            output=15.0,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_SONNET_4_20250514 = Model(
        id="claude-sonnet-4-20250514",
        name="Claude Sonnet 4",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=3.0,
            output=15.0,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_3_7_SONNET_20250219 = Model(
        id="claude-3-7-sonnet-20250219",
        name="Claude Sonnet 3.7",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=3.0,
            output=15.0,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_HAIKU_4_5 = Model(
        id="claude-haiku-4-5",
        name="Claude Haiku 4.5 (latest)",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=1.0,
            output=5.0,
            cache_read=0.1,
            cache_write=1.25,
        ),
    )

    CLAUDE_HAIKU_4_5_20251001 = Model(
        id="claude-haiku-4-5-20251001",
        name="Claude Haiku 4.5",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=1.0,
            output=5.0,
            cache_read=0.1,
            cache_write=1.25,
        ),
    )

    CLAUDE_3_5_HAIKU_LATEST = Model(
        id="claude-3-5-haiku-latest",
        name="Claude Haiku 3.5 (latest)",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            output=4.0,
            cache_read=0.08,
            cache_write=1.0,
        ),
    )

    CLAUDE_3_5_SONNET_20241022 = Model(
        id="claude-3-5-sonnet-20241022",
        name="Claude Sonnet 3.5 v2",
        api="anthropic-messages",
        provider="anthropic",
        base_url="https://api.anthropic.com",
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
            input=3.0,
            output=15.0,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )



class Baichuan:
    """Models for baichuan."""

    BAICHUAN4_TURBO = Model(
        id="Baichuan4-Turbo",
        name="Baichuan4 Turbo",
        api="openai-completions",
        provider="baichuan",
        base_url="https://api.baichuan-ai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=1.38,
            output=1.38,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    BAICHUAN4_AIR = Model(
        id="Baichuan4-Air",
        name="Baichuan4 Air",
        api="openai-completions",
        provider="baichuan",
        base_url="https://api.baichuan-ai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.14,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    BAICHUAN3_TURBO_128K = Model(
        id="Baichuan3-Turbo-128k",
        name="Baichuan3 Turbo 128K",
        api="openai-completions",
        provider="baichuan",
        base_url="https://api.baichuan-ai.com/v1",
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
            input=0.69,
            output=0.69,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )



class AmazonBedrock:
    """Models for amazon-bedrock."""

    AMAZON_NOVA_PREMIER_V1_0 = Model(
        id="amazon.nova-premier-v1:0",
        name="Nova Premier",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=40000,
        ),
        pricing=ModelPricing(
            input=2.5,
            output=12.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    AMAZON_NOVA_2_LITE_V1_0 = Model(
        id="amazon.nova-2-lite-v1:0",
        name="Nova 2 Lite",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
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
        base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
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
        base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
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
        base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
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

    ANTHROPIC_CLAUDE_SONNET_4_20250514_V1_0 = Model(
        id="anthropic.claude-sonnet-4-20250514-v1:0",
        name="Claude Sonnet 4 (Bedrock)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=3.0,
            output=15.0,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    ANTHROPIC_CLAUDE_3_7_SONNET_20250219_V1_0 = Model(
        id="anthropic.claude-3-7-sonnet-20250219-v1:0",
        name="Claude Sonnet 3.7 (Bedrock)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=3.0,
            output=15.0,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    ANTHROPIC_CLAUDE_3_5_HAIKU_20241022_V1_0 = Model(
        id="anthropic.claude-3-5-haiku-20241022-v1:0",
        name="Claude Haiku 3.5 (Bedrock)",
        api="bedrock-converse-stream",
        provider="amazon-bedrock",
        base_url="https://bedrock-runtime.us-east-1.amazonaws.com",
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
            output=4.0,
            cache_read=0.08,
            cache_write=1.0,
        ),
    )



class Deepseek:
    """Models for deepseek."""

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
            supported_thinking_levels=(ModelThinkingLevel.HIGH, ModelThinkingLevel.XHIGH,),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=384000,
        ),
        pricing=ModelPricing(
            input=0.435,
            output=0.87,
            cache_read=0.003625,
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
            supported_thinking_levels=(ModelThinkingLevel.HIGH, ModelThinkingLevel.XHIGH,),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=384000,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=0.28,
            cache_read=0.0028,
            cache_write=0,
        ),
    )



class Doubao:
    """Models for doubao."""

    DOUBAO_SEED_1_6 = Model(
        id="doubao-seed-1.6",
        name="Doubao Seed 1.6",
        api="openai-completions",
        provider="doubao",
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.55,
            output=2.19,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    DOUBAO_1_5_PRO_256K = Model(
        id="doubao-1.5-pro-256k",
        name="Doubao 1.5 Pro 256K",
        api="openai-completions",
        provider="doubao",
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=256000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.69,
            output=1.38,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    DOUBAO_1_5_PRO_32K = Model(
        id="doubao-1.5-pro-32k",
        name="Doubao 1.5 Pro 32K",
        api="openai-completions",
        provider="doubao",
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.55,
            output=1.1,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    DOUBAO_1_5_LITE_32K = Model(
        id="doubao-1.5-lite-32k",
        name="Doubao 1.5 Lite 32K",
        api="openai-completions",
        provider="doubao",
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.21,
            output=0.41,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    DOUBAO_1_5_THINKING_PRO = Model(
        id="doubao-1.5-thinking-pro",
        name="Doubao 1.5 Thinking Pro",
        api="openai-completions",
        provider="doubao",
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=2.76,
            output=11.04,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    DOUBAO_VISION_PRO_32K = Model(
        id="doubao-vision-pro-32k",
        name="Doubao Vision Pro 32K",
        api="openai-completions",
        provider="doubao",
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=1.38,
            output=1.38,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )



class Google:
    """Models for google."""

    GEMINI_2_5_PRO = Model(
        id="gemini-2.5-pro",
        name="Gemini 2.5 Pro",
        api="google-generative-ai",
        provider="google",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=2.0,
            output=12.0,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    GEMINI_2_5_FLASH = Model(
        id="gemini-2.5-flash",
        name="Gemini 2.5 Flash",
        api="google-generative-ai",
        provider="google",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=2.5,
            cache_read=0.03,
            cache_write=0,
        ),
    )

    GEMINI_2_5_FLASH_LITE = Model(
        id="gemini-2.5-flash-lite",
        name="Gemini 2.5 Flash Lite",
        api="google-generative-ai",
        provider="google",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0.015,
            cache_write=0,
        ),
    )

    GEMINI_2_0_FLASH = Model(
        id="gemini-2.0-flash",
        name="Gemini 2.0 Flash",
        api="google-generative-ai",
        provider="google",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1048576,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.4,
            cache_read=0.025,
            cache_write=0,
        ),
    )

    GEMINI_2_0_FLASH_LITE = Model(
        id="gemini-2.0-flash-lite",
        name="Gemini 2.0 Flash Lite",
        api="google-generative-ai",
        provider="google",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1048576,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.075,
            output=0.3,
            cache_read=0.01875,
            cache_write=0,
        ),
    )

    GEMINI_1_5_PRO = Model(
        id="gemini-1.5-pro",
        name="Gemini 1.5 Pro",
        api="google-generative-ai",
        provider="google",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=5.0,
            cache_read=0.3125,
            cache_write=0,
        ),
    )

    GEMINI_1_5_FLASH = Model(
        id="gemini-1.5-flash",
        name="Gemini 1.5 Flash",
        api="google-generative-ai",
        provider="google",
        base_url="https://generativelanguage.googleapis.com/v1beta",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.075,
            output=0.3,
            cache_read=0.01875,
            cache_write=0,
        ),
    )



class Groq:
    """Models for groq."""

    LLAMA_3_3_70B_VERSATILE = Model(
        id="llama-3.3-70b-versatile",
        name="Llama 3.3 70B Versatile",
        api="openai-completions",
        provider="groq",
        base_url="https://api.groq.com/openai/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.59,
            output=0.79,
            cache_read=0,
            cache_write=0,
        ),
    )

    LLAMA_3_1_8B_INSTANT = Model(
        id="llama-3.1-8b-instant",
        name="Llama 3.1 8B Instant",
        api="openai-completions",
        provider="groq",
        base_url="https://api.groq.com/openai/v1",
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
            input=0.05,
            output=0.08,
            cache_read=0,
            cache_write=0,
        ),
    )

    META_LLAMA__LLAMA_4_SCOUT_17B_16E_INSTRUCT = Model(
        id="meta-llama/llama-4-scout-17b-16e-instruct",
        name="Llama 4 Scout 17B",
        api="openai-completions",
        provider="groq",
        base_url="https://api.groq.com/openai/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.11,
            output=0.34,
            cache_read=0,
            cache_write=0,
        ),
    )

    META_LLAMA__LLAMA_4_MAVERICK_17B_128E_INSTRUCT = Model(
        id="meta-llama/llama-4-maverick-17b-128e-instruct",
        name="Llama 4 Maverick 17B",
        api="openai-completions",
        provider="groq",
        base_url="https://api.groq.com/openai/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_R1_DISTILL_LLAMA_70B = Model(
        id="deepseek-r1-distill-llama-70b",
        name="DeepSeek R1 Distill Llama 70B",
        api="openai-completions",
        provider="groq",
        base_url="https://api.groq.com/openai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
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
            input=0.75,
            output=0.99,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_32B = Model(
        id="qwen/qwen3-32b",
        name="Qwen3 32B",
        api="openai-completions",
        provider="groq",
        base_url="https://api.groq.com/openai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
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
            input=0.29,
            output=0.39,
            cache_read=0,
            cache_write=0,
        ),
    )



class Kimi:
    """Models for kimi."""

    KIMI_K2 = Model(
        id="kimi-k2",
        name="Kimi K2",
        api="openai-completions",
        provider="kimi",
        base_url="https://api.moonshot.cn/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=2.0,
            output=8.0,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    KIMI_K1_5_LONG = Model(
        id="kimi-k1.5-long",
        name="Kimi K1.5 Long",
        api="openai-completions",
        provider="kimi",
        base_url="https://api.moonshot.cn/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=1.4,
            output=5.6,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    MOONSHOT_V1_128K = Model(
        id="moonshot-v1-128k",
        name="Moonshot V1 128K",
        api="openai-completions",
        provider="kimi",
        base_url="https://api.moonshot.cn/v1",
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
            input=0.83,
            output=0.83,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    MOONSHOT_V1_32K = Model(
        id="moonshot-v1-32k",
        name="Moonshot V1 32K",
        api="openai-completions",
        provider="kimi",
        base_url="https://api.moonshot.cn/v1",
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
            input=0.33,
            output=0.33,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )



class Mimo:
    """Models for mimo."""

    MIMO_7B_RL = Model(
        id="MiMo-7B-RL",
        name="MiMo 7B RL",
        api="openai-completions",
        provider="mimo",
        base_url="https://api.mimo.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=0.55,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )



class Minimax:
    """Models for minimax."""

    MINIMAX_M1 = Model(
        id="MiniMax-M1",
        name="MiniMax M1",
        api="openai-completions",
        provider="minimax",
        base_url="https://api.minimax.chat/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=0.55,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    MINIMAX_T1 = Model(
        id="MiniMax-T1",
        name="MiniMax T1",
        api="openai-completions",
        provider="minimax",
        base_url="https://api.minimax.chat/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=0.55,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    ABAB7_CHAT = Model(
        id="abab7-chat",
        name="ABAB 7 Chat",
        api="openai-completions",
        provider="minimax",
        base_url="https://api.minimax.chat/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=245760,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=0.14,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )



class Mistral:
    """Models for mistral."""

    MISTRAL_LARGE_LATEST = Model(
        id="mistral-large-latest",
        name="Mistral Large (latest)",
        api="mistral-conversations",
        provider="mistral",
        base_url="https://api.mistral.ai",
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
            input=2.0,
            output=6.0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_MEDIUM_LATEST = Model(
        id="mistral-medium-latest",
        name="Mistral Medium (latest)",
        api="mistral-conversations",
        provider="mistral",
        base_url="https://api.mistral.ai",
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
            input=0.4,
            output=2.0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_SMALL_LATEST = Model(
        id="mistral-small-latest",
        name="Mistral Small (latest)",
        api="mistral-conversations",
        provider="mistral",
        base_url="https://api.mistral.ai",
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
            input=0.1,
            output=0.3,
            cache_read=0,
            cache_write=0,
        ),
    )

    CODESTRAL_LATEST = Model(
        id="codestral-latest",
        name="Codestral (latest)",
        api="mistral-conversations",
        provider="mistral",
        base_url="https://api.mistral.ai",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=256000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=0.9,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEVSTRAL_MEDIUM_LATEST = Model(
        id="devstral-medium-latest",
        name="Devstral Medium (latest)",
        api="mistral-conversations",
        provider="mistral",
        base_url="https://api.mistral.ai",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=2.0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MAGISTRAL_MEDIUM_LATEST = Model(
        id="magistral-medium-latest",
        name="Magistral Medium (latest)",
        api="mistral-conversations",
        provider="mistral",
        base_url="https://api.mistral.ai",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=40000,
            max_output_tokens=40000,
        ),
        pricing=ModelPricing(
            input=2.0,
            output=6.0,
            cache_read=0,
            cache_write=0,
        ),
    )

    PIXTRAL_LARGE_LATEST = Model(
        id="pixtral-large-latest",
        name="Pixtral Large (latest)",
        api="mistral-conversations",
        provider="mistral",
        base_url="https://api.mistral.ai",
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
            input=2.0,
            output=6.0,
            cache_read=0,
            cache_write=0,
        ),
    )



class Openai:
    """Models for openai."""

    GPT_4O = Model(
        id="gpt-4o",
        name="GPT-4o",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=2.5,
            output=10.0,
            cache_read=1.25,
            cache_write=0.0,
        ),
    )

    GPT_4O_MINI = Model(
        id="gpt-4o-mini",
        name="GPT-4o mini",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0.08,
            cache_write=0.0,
        ),
    )

    GPT_4_1 = Model(
        id="gpt-4.1",
        name="GPT-4.1",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1047576,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=2.0,
            output=8.0,
            cache_read=0.5,
            cache_write=0.0,
        ),
    )

    GPT_4_1_MINI = Model(
        id="gpt-4.1-mini",
        name="GPT-4.1 mini",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1047576,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=1.6,
            cache_read=0.1,
            cache_write=0.0,
        ),
    )

    GPT_4_1_NANO = Model(
        id="gpt-4.1-nano",
        name="GPT-4.1 nano",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1047576,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.4,
            cache_read=0.03,
            cache_write=0.0,
        ),
    )

    O3 = Model(
        id="o3",
        name="o3",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=100000,
        ),
        pricing=ModelPricing(
            input=2.0,
            output=8.0,
            cache_read=0.5,
            cache_write=0.0,
        ),
    )

    O3_MINI = Model(
        id="o3-mini",
        name="o3 mini",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=100000,
        ),
        pricing=ModelPricing(
            input=1.1,
            output=4.4,
            cache_read=0.28,
            cache_write=0.0,
        ),
    )

    O3_PRO = Model(
        id="o3-pro",
        name="o3 Pro",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=100000,
        ),
        pricing=ModelPricing(
            input=20.0,
            output=80.0,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    O4_MINI = Model(
        id="o4-mini",
        name="o4 mini",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=100000,
        ),
        pricing=ModelPricing(
            input=1.1,
            output=4.4,
            cache_read=0.28,
            cache_write=0.0,
        ),
    )

    GPT_5 = Model(
        id="gpt-5",
        name="GPT-5",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=10.0,
            cache_read=0.125,
            cache_write=0.0,
        ),
    )

    GPT_5_MINI = Model(
        id="gpt-5-mini",
        name="GPT-5 mini",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1047576,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=1.6,
            cache_read=0.1,
            cache_write=0.0,
        ),
    )

    GPT_5_NANO = Model(
        id="gpt-5-nano",
        name="GPT-5 nano",
        api="openai-completions",
        provider="openai",
        base_url="https://api.openai.com/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1047576,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.4,
            cache_read=0.03,
            cache_write=0.0,
        ),
    )



class Openrouter:
    """Models for openrouter."""

    ANTHROPIC__CLAUDE_SONNET_4 = Model(
        id="anthropic/claude-sonnet-4",
        name="Claude Sonnet 4 (OpenRouter)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=3.0,
            output=15.0,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    OPENAI__GPT_4O = Model(
        id="openai/gpt-4o",
        name="GPT-4o (OpenRouter)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=2.5,
            output=10.0,
            cache_read=1.25,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_2_5_FLASH = Model(
        id="google/gemini-2.5-flash",
        name="Gemini 2.5 Flash (OpenRouter)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=2.5,
            cache_read=0.03,
            cache_write=0,
        ),
    )

    DEEPSEEK__DEEPSEEK_V4_PRO = Model(
        id="deepseek/deepseek-v4-pro",
        name="DeepSeek V4 Pro (OpenRouter)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
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
            input=0.435,
            output=0.87,
            cache_read=0.003625,
            cache_write=0,
        ),
    )



class Qwen:
    """Models for qwen."""

    QWEN3_235B_A22B = Model(
        id="qwen3-235b-a22b",
        name="Qwen3 235B A22B",
        api="openai-completions",
        provider="qwen",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.55,
            output=2.19,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    QWEN3_32B = Model(
        id="qwen3-32b",
        name="Qwen3 32B",
        api="openai-completions",
        provider="qwen",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.17,
            output=0.55,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    QWEN3_30B_A3B = Model(
        id="qwen3-30b-a3b",
        name="Qwen3 30B A3B",
        api="openai-completions",
        provider="qwen",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=0.41,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    QWEN_MAX = Model(
        id="qwen-max",
        name="Qwen Max",
        api="openai-completions",
        provider="qwen",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=1.38,
            output=5.52,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    QWEN_PLUS = Model(
        id="qwen-plus",
        name="Qwen Plus",
        api="openai-completions",
        provider="qwen",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.55,
            output=1.52,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    QWEN_TURBO = Model(
        id="qwen-turbo",
        name="Qwen Turbo",
        api="openai-completions",
        provider="qwen",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.04,
            output=0.21,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    QWEN_VL_MAX = Model(
        id="qwen-vl-max",
        name="Qwen VL Max",
        api="openai-completions",
        provider="qwen",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=1.38,
            output=5.52,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    QWEN_VL_PLUS = Model(
        id="qwen-vl-plus",
        name="Qwen VL Plus",
        api="openai-completions",
        provider="qwen",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.55,
            output=1.52,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    QWQ_PLUS = Model(
        id="qwq-plus",
        name="QwQ Plus",
        api="openai-completions",
        provider="qwen",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.55,
            output=1.52,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )



class Stepfun:
    """Models for stepfun."""

    STEP_2_16K = Model(
        id="step-2-16k",
        name="Step 2 16K",
        api="openai-completions",
        provider="stepfun",
        base_url="https://api.stepfun.com/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=16000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=5.28,
            output=19.3,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    STEP_1_32K = Model(
        id="step-1-32k",
        name="Step 1 32K",
        api="openai-completions",
        provider="stepfun",
        base_url="https://api.stepfun.com/v1",
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
            input=1.66,
            output=5.52,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    STEP_1_128K = Model(
        id="step-1-128k",
        name="Step 1 128K",
        api="openai-completions",
        provider="stepfun",
        base_url="https://api.stepfun.com/v1",
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
            input=5.8,
            output=19.3,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    STEP_1V_32K = Model(
        id="step-1v-32k",
        name="Step 1V 32K",
        api="openai-completions",
        provider="stepfun",
        base_url="https://api.stepfun.com/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=1.66,
            output=5.52,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    STEP_2_MINI = Model(
        id="step-2-mini",
        name="Step 2 Mini",
        api="openai-completions",
        provider="stepfun",
        base_url="https://api.stepfun.com/v1",
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
            input=0.14,
            output=0.28,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )



class Xai:
    """Models for xai."""

    GROK_4 = Model(
        id="grok-4",
        name="Grok 4",
        api="openai-completions",
        provider="xai",
        base_url="https://api.x.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=256000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=3.0,
            output=15.0,
            cache_read=3.0,
            cache_write=0,
        ),
    )

    GROK_3 = Model(
        id="grok-3",
        name="Grok 3",
        api="openai-completions",
        provider="xai",
        base_url="https://api.x.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=3.0,
            output=15.0,
            cache_read=3.0,
            cache_write=0,
        ),
    )

    GROK_3_FAST = Model(
        id="grok-3-fast",
        name="Grok 3 Fast",
        api="openai-completions",
        provider="xai",
        base_url="https://api.x.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=5.0,
            output=25.0,
            cache_read=5.0,
            cache_write=0,
        ),
    )

    GROK_3_MINI = Model(
        id="grok-3-mini",
        name="Grok 3 mini",
        api="openai-completions",
        provider="xai",
        base_url="https://api.x.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=0.5,
            cache_read=0.3,
            cache_write=0,
        ),
    )

    GROK_3_MINI_FAST = Model(
        id="grok-3-mini-fast",
        name="Grok 3 mini Fast",
        api="openai-completions",
        provider="xai",
        base_url="https://api.x.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131072,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=4.0,
            cache_read=0.6,
            cache_write=0,
        ),
    )

    GROK_2_LATEST = Model(
        id="grok-2-latest",
        name="Grok 2 Latest",
        api="openai-completions",
        provider="xai",
        base_url="https://api.x.ai/v1",
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
            input=2.0,
            output=10.0,
            cache_read=2.0,
            cache_write=0,
        ),
    )

    GROK_2_VISION_LATEST = Model(
        id="grok-2-vision-latest",
        name="Grok 2 Vision Latest",
        api="openai-completions",
        provider="xai",
        base_url="https://api.x.ai/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32768,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=2.0,
            output=10.0,
            cache_read=2.0,
            cache_write=0,
        ),
    )



class Zhipu:
    """Models for zhipu."""

    GLM_4_PLUS = Model(
        id="glm-4-plus",
        name="GLM-4 Plus",
        api="openai-completions",
        provider="zhipu",
        base_url="https://open.bigmodel.cn/api/paas/v4",
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
            input=6.9,
            output=6.9,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    GLM_4_AIR = Model(
        id="glm-4-air",
        name="GLM-4 Air",
        api="openai-completions",
        provider="zhipu",
        base_url="https://open.bigmodel.cn/api/paas/v4",
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
            output=0.07,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    GLM_4_AIRX = Model(
        id="glm-4-airx",
        name="GLM-4 AirX",
        api="openai-completions",
        provider="zhipu",
        base_url="https://open.bigmodel.cn/api/paas/v4",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8192,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=1.38,
            output=1.38,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    GLM_4_FLASH = Model(
        id="glm-4-flash",
        name="GLM-4 Flash",
        api="openai-completions",
        provider="zhipu",
        base_url="https://open.bigmodel.cn/api/paas/v4",
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
            input=0.0,
            output=0.0,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    GLM_4V_PLUS = Model(
        id="glm-4v-plus",
        name="GLM-4V Plus",
        api="openai-completions",
        provider="zhipu",
        base_url="https://open.bigmodel.cn/api/paas/v4",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8192,
            max_output_tokens=1024,
        ),
        pricing=ModelPricing(
            input=1.38,
            output=1.38,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    GLM_Z1_AIR = Model(
        id="glm-z1-air",
        name="GLM-Z1 Air",
        api="openai-completions",
        provider="zhipu",
        base_url="https://open.bigmodel.cn/api/paas/v4",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.07,
            output=0.07,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    GLM_Z1_AIRX = Model(
        id="glm-z1-airx",
        name="GLM-Z1 AirX",
        api="openai-completions",
        provider="zhipu",
        base_url="https://open.bigmodel.cn/api/paas/v4",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=16384,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=1.38,
            output=1.38,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )

    GLM_Z1_FLASH = Model(
        id="glm-z1-flash",
        name="GLM-Z1 Flash",
        api="openai-completions",
        provider="zhipu",
        base_url="https://open.bigmodel.cn/api/paas/v4",
        capabilities=ModelCapabilities(
            reasoning=True,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(ModelThinkingLevel.LOW, ModelThinkingLevel.MEDIUM, ModelThinkingLevel.HIGH,),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.0,
            output=0.0,
            cache_read=0.0,
            cache_write=0.0,
        ),
    )



ALL_MODELS: list[Model] = [
    Anthropic.CLAUDE_OPUS_4_7,
    Anthropic.CLAUDE_OPUS_4_6,
    Anthropic.CLAUDE_OPUS_4_5,
    Anthropic.CLAUDE_OPUS_4_5_20251101,
    Anthropic.CLAUDE_OPUS_4_0,
    Anthropic.CLAUDE_OPUS_4_20250514,
    Anthropic.CLAUDE_SONNET_4_6,
    Anthropic.CLAUDE_SONNET_4_5,
    Anthropic.CLAUDE_SONNET_4_5_20250929,
    Anthropic.CLAUDE_SONNET_4_0,
    Anthropic.CLAUDE_SONNET_4_20250514,
    Anthropic.CLAUDE_3_7_SONNET_20250219,
    Anthropic.CLAUDE_HAIKU_4_5,
    Anthropic.CLAUDE_HAIKU_4_5_20251001,
    Anthropic.CLAUDE_3_5_HAIKU_LATEST,
    Anthropic.CLAUDE_3_5_SONNET_20241022,
    Baichuan.BAICHUAN4_TURBO,
    Baichuan.BAICHUAN4_AIR,
    Baichuan.BAICHUAN3_TURBO_128K,
    AmazonBedrock.AMAZON_NOVA_PREMIER_V1_0,
    AmazonBedrock.AMAZON_NOVA_2_LITE_V1_0,
    AmazonBedrock.AMAZON_NOVA_LITE_V1_0,
    AmazonBedrock.AMAZON_NOVA_MICRO_V1_0,
    AmazonBedrock.AMAZON_NOVA_PRO_V1_0,
    AmazonBedrock.ANTHROPIC_CLAUDE_SONNET_4_20250514_V1_0,
    AmazonBedrock.ANTHROPIC_CLAUDE_3_7_SONNET_20250219_V1_0,
    AmazonBedrock.ANTHROPIC_CLAUDE_3_5_HAIKU_20241022_V1_0,
    Deepseek.DEEPSEEK_V4_PRO,
    Deepseek.DEEPSEEK_V4_FLASH,
    Doubao.DOUBAO_SEED_1_6,
    Doubao.DOUBAO_1_5_PRO_256K,
    Doubao.DOUBAO_1_5_PRO_32K,
    Doubao.DOUBAO_1_5_LITE_32K,
    Doubao.DOUBAO_1_5_THINKING_PRO,
    Doubao.DOUBAO_VISION_PRO_32K,
    Google.GEMINI_2_5_PRO,
    Google.GEMINI_2_5_FLASH,
    Google.GEMINI_2_5_FLASH_LITE,
    Google.GEMINI_2_0_FLASH,
    Google.GEMINI_2_0_FLASH_LITE,
    Google.GEMINI_1_5_PRO,
    Google.GEMINI_1_5_FLASH,
    Groq.LLAMA_3_3_70B_VERSATILE,
    Groq.LLAMA_3_1_8B_INSTANT,
    Groq.META_LLAMA__LLAMA_4_SCOUT_17B_16E_INSTRUCT,
    Groq.META_LLAMA__LLAMA_4_MAVERICK_17B_128E_INSTRUCT,
    Groq.DEEPSEEK_R1_DISTILL_LLAMA_70B,
    Groq.QWEN__QWEN3_32B,
    Kimi.KIMI_K2,
    Kimi.KIMI_K1_5_LONG,
    Kimi.MOONSHOT_V1_128K,
    Kimi.MOONSHOT_V1_32K,
    Mimo.MIMO_7B_RL,
    Minimax.MINIMAX_M1,
    Minimax.MINIMAX_T1,
    Minimax.ABAB7_CHAT,
    Mistral.MISTRAL_LARGE_LATEST,
    Mistral.MISTRAL_MEDIUM_LATEST,
    Mistral.MISTRAL_SMALL_LATEST,
    Mistral.CODESTRAL_LATEST,
    Mistral.DEVSTRAL_MEDIUM_LATEST,
    Mistral.MAGISTRAL_MEDIUM_LATEST,
    Mistral.PIXTRAL_LARGE_LATEST,
    Openai.GPT_4O,
    Openai.GPT_4O_MINI,
    Openai.GPT_4_1,
    Openai.GPT_4_1_MINI,
    Openai.GPT_4_1_NANO,
    Openai.O3,
    Openai.O3_MINI,
    Openai.O3_PRO,
    Openai.O4_MINI,
    Openai.GPT_5,
    Openai.GPT_5_MINI,
    Openai.GPT_5_NANO,
    Openrouter.ANTHROPIC__CLAUDE_SONNET_4,
    Openrouter.OPENAI__GPT_4O,
    Openrouter.GOOGLE__GEMINI_2_5_FLASH,
    Openrouter.DEEPSEEK__DEEPSEEK_V4_PRO,
    Qwen.QWEN3_235B_A22B,
    Qwen.QWEN3_32B,
    Qwen.QWEN3_30B_A3B,
    Qwen.QWEN_MAX,
    Qwen.QWEN_PLUS,
    Qwen.QWEN_TURBO,
    Qwen.QWEN_VL_MAX,
    Qwen.QWEN_VL_PLUS,
    Qwen.QWQ_PLUS,
    Stepfun.STEP_2_16K,
    Stepfun.STEP_1_32K,
    Stepfun.STEP_1_128K,
    Stepfun.STEP_1V_32K,
    Stepfun.STEP_2_MINI,
    Xai.GROK_4,
    Xai.GROK_3,
    Xai.GROK_3_FAST,
    Xai.GROK_3_MINI,
    Xai.GROK_3_MINI_FAST,
    Xai.GROK_2_LATEST,
    Xai.GROK_2_VISION_LATEST,
    Zhipu.GLM_4_PLUS,
    Zhipu.GLM_4_AIR,
    Zhipu.GLM_4_AIRX,
    Zhipu.GLM_4_FLASH,
    Zhipu.GLM_4V_PLUS,
    Zhipu.GLM_Z1_AIR,
    Zhipu.GLM_Z1_AIRX,
    Zhipu.GLM_Z1_FLASH,
]
