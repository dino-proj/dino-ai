"""Auto-generated models for openrouter.

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


class Openrouter:
    """Models for openrouter."""

    ANTHROPIC__CLAUDE_3_5_HAIKU = Model(
        id="anthropic/claude-3.5-haiku",
        name="Claude Haiku 3.5",
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

    ANTHROPIC__CLAUDE_3_7_SONNET = Model(
        id="anthropic/claude-3.7-sonnet",
        name="Claude Sonnet 3.7",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=15,
            output=75,
            cache_read=1.5,
            cache_write=18.75,
        ),
    )

    ANTHROPIC__CLAUDE_HAIKU_4_5 = Model(
        id="anthropic/claude-haiku-4.5",
        name="Claude Haiku 4.5",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    ANTHROPIC__CLAUDE_OPUS_4 = Model(
        id="anthropic/claude-opus-4",
        name="Claude Opus 4",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    ANTHROPIC__CLAUDE_OPUS_4_1 = Model(
        id="anthropic/claude-opus-4.1",
        name="Claude Opus 4.1",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    ANTHROPIC__CLAUDE_OPUS_4_5 = Model(
        id="anthropic/claude-opus-4.5",
        name="Claude Opus 4.5",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=5,
            output=25,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    ANTHROPIC__CLAUDE_OPUS_4_6 = Model(
        id="anthropic/claude-opus-4.6",
        name="Claude Opus 4.6",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    ANTHROPIC__CLAUDE_OPUS_4_7 = Model(
        id="anthropic/claude-opus-4.7",
        name="Claude Opus 4.7",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    ANTHROPIC__CLAUDE_SONNET_4 = Model(
        id="anthropic/claude-sonnet-4",
        name="Claude Sonnet 4",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    ANTHROPIC__CLAUDE_SONNET_4_5 = Model(
        id="anthropic/claude-sonnet-4.5",
        name="Claude Sonnet 4.5",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    ANTHROPIC__CLAUDE_SONNET_4_6 = Model(
        id="anthropic/claude-sonnet-4.6",
        name="Claude Sonnet 4.6",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    ARCEE_AI__TRINITY_LARGE_PREVIEW_FREE = Model(
        id="arcee-ai/trinity-large-preview:free",
        name="Trinity Large Preview",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    ARCEE_AI__TRINITY_LARGE_THINKING = Model(
        id="arcee-ai/trinity-large-thinking",
        name="Trinity Large Thinking",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=80000,
        ),
        pricing=ModelPricing(
            input=0.22,
            output=0.85,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK__DEEPSEEK_CHAT_V3_1 = Model(
        id="deepseek/deepseek-chat-v3.1",
        name="DeepSeek-V3.1",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=163840,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK__DEEPSEEK_R1 = Model(
        id="deepseek/deepseek-r1",
        name="DeepSeek: R1",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=64000,
            max_output_tokens=16000,
        ),
        pricing=ModelPricing(
            input=0.7,
            output=2.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK__DEEPSEEK_V3_1_TERMINUS = Model(
        id="deepseek/deepseek-v3.1-terminus",
        name="DeepSeek V3.1 Terminus",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.27,
            output=1,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK__DEEPSEEK_V3_1_TERMINUS_EXACTO = Model(
        id="deepseek/deepseek-v3.1-terminus:exacto",
        name="DeepSeek V3.1 Terminus (exacto)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.27,
            output=1,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK__DEEPSEEK_V3_2 = Model(
        id="deepseek/deepseek-v3.2",
        name="DeepSeek V3.2",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.28,
            output=0.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK__DEEPSEEK_V3_2_SPECIALE = Model(
        id="deepseek/deepseek-v3.2-speciale",
        name="DeepSeek V3.2 Speciale",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.27,
            output=0.41,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK__DEEPSEEK_V4_FLASH = Model(
        id="deepseek/deepseek-v4-flash",
        name="DeepSeek V4 Flash",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=393216,
        ),
        pricing=ModelPricing(
            input=0.14,
            output=0.28,
            cache_read=0.028,
            cache_write=0,
        ),
    )

    DEEPSEEK__DEEPSEEK_V4_PRO = Model(
        id="deepseek/deepseek-v4-pro",
        name="DeepSeek V4 Pro",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=393216,
        ),
        pricing=ModelPricing(
            input=1.74,
            output=3.48,
            cache_read=0.145,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_2_0_FLASH_001 = Model(
        id="google/gemini-2.0-flash-001",
        name="Gemini 2.0 Flash",
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

    GOOGLE__GEMINI_2_5_FLASH = Model(
        id="google/gemini-2.5-flash",
        name="Gemini 2.5 Flash",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=2.5,
            cache_read=0.0375,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_2_5_FLASH_LITE = Model(
        id="google/gemini-2.5-flash-lite",
        name="Gemini 2.5 Flash Lite",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.4,
            cache_read=0.025,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_2_5_FLASH_LITE_PREVIEW_09_2025 = Model(
        id="google/gemini-2.5-flash-lite-preview-09-2025",
        name="Gemini 2.5 Flash Lite Preview 09-25",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.4,
            cache_read=0.025,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_2_5_FLASH_PREVIEW_09_2025 = Model(
        id="google/gemini-2.5-flash-preview-09-2025",
        name="Gemini 2.5 Flash Preview 09-25",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=2.5,
            cache_read=0.031,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_2_5_PRO = Model(
        id="google/gemini-2.5-pro",
        name="Gemini 2.5 Pro",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=10,
            cache_read=0.125,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_2_5_PRO_PREVIEW_05_06 = Model(
        id="google/gemini-2.5-pro-preview-05-06",
        name="Gemini 2.5 Pro Preview 05-06",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=10,
            cache_read=0.31,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_2_5_PRO_PREVIEW_06_05 = Model(
        id="google/gemini-2.5-pro-preview-06-05",
        name="Gemini 2.5 Pro Preview 06-05",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=10,
            cache_read=0.31,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_3_FLASH_PREVIEW = Model(
        id="google/gemini-3-flash-preview",
        name="Gemini 3 Flash Preview",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=3,
            cache_read=0.05,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_3_PRO_PREVIEW = Model(
        id="google/gemini-3-pro-preview",
        name="Gemini 3 Pro Preview",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=1050000,
            max_output_tokens=66000,
        ),
        pricing=ModelPricing(
            input=2,
            output=12,
            cache_read=0,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_3_1_FLASH_LITE_PREVIEW = Model(
        id="google/gemini-3.1-flash-lite-preview",
        name="Gemini 3.1 Flash Lite Preview",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.25,
            output=1.5,
            cache_read=0.025,
            cache_write=0.083,
        ),
    )

    GOOGLE__GEMINI_3_1_PRO_PREVIEW = Model(
        id="google/gemini-3.1-pro-preview",
        name="Gemini 3.1 Pro Preview",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=2,
            output=12,
            cache_read=0,
            cache_write=0,
        ),
    )

    GOOGLE__GEMINI_3_1_PRO_PREVIEW_CUSTOMTOOLS = Model(
        id="google/gemini-3.1-pro-preview-customtools",
        name="Gemini 3.1 Pro Preview Custom Tools",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=2,
            output=12,
            cache_read=0,
            cache_write=0,
        ),
    )

    GOOGLE__GEMMA_3_27B_IT = Model(
        id="google/gemma-3-27b-it",
        name="Gemma 3 27B",
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
            context_window=96000,
            max_output_tokens=96000,
        ),
        pricing=ModelPricing(
            input=0.04,
            output=0.15,
            cache_read=0,
            cache_write=0,
        ),
    )

    GOOGLE__GEMMA_3_27B_IT_FREE = Model(
        id="google/gemma-3-27b-it:free",
        name="Gemma 3 27B (free)",
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
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    GOOGLE__GEMMA_4_26B_A4B_IT = Model(
        id="google/gemma-4-26b-a4b-it",
        name="Gemma 4 26B A4B",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.13,
            output=0.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    GOOGLE__GEMMA_4_26B_A4B_IT_FREE = Model(
        id="google/gemma-4-26b-a4b-it:free",
        name="Gemma 4 26B A4B (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    GOOGLE__GEMMA_4_31B_IT = Model(
        id="google/gemma-4-31b-it",
        name="Gemma 4 31B",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.14,
            output=0.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    GOOGLE__GEMMA_4_31B_IT_FREE = Model(
        id="google/gemma-4-31b-it:free",
        name="Gemma 4 31B (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    INCEPTION__MERCURY_2 = Model(
        id="inception/mercury-2",
        name="Mercury 2",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=50000,
        ),
        pricing=ModelPricing(
            input=0.25,
            output=0.75,
            cache_read=0.025,
            cache_write=0,
        ),
    )

    META_LLAMA__LLAMA_3_3_70B_INSTRUCT_FREE = Model(
        id="meta-llama/llama-3.3-70b-instruct:free",
        name="Llama 3.3 70B Instruct (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX__MINIMAX_01 = Model(
        id="minimax/minimax-01",
        name="MiniMax-01",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=1000000,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=1.1,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX__MINIMAX_M1 = Model(
        id="minimax/minimax-m1",
        name="MiniMax M1",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=40000,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=2.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX__MINIMAX_M2 = Model(
        id="minimax/minimax-m2",
        name="MiniMax M2",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=196600,
            max_output_tokens=118000,
        ),
        pricing=ModelPricing(
            input=0.28,
            output=1.15,
            cache_read=0.28,
            cache_write=1.15,
        ),
    )

    MINIMAX__MINIMAX_M2_1 = Model(
        id="minimax/minimax-m2.1",
        name="MiniMax M2.1",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    MINIMAX__MINIMAX_M2_5 = Model(
        id="minimax/minimax-m2.5",
        name="MiniMax M2.5",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            cache_write=0,
        ),
    )

    MINIMAX__MINIMAX_M2_5_FREE = Model(
        id="minimax/minimax-m2.5:free",
        name="MiniMax M2.5 (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX__MINIMAX_M2_7 = Model(
        id="minimax/minimax-m2.7",
        name="MiniMax M2.7",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    MISTRALAI__CODESTRAL_2508 = Model(
        id="mistralai/codestral-2508",
        name="Codestral 2508",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=256000,
            max_output_tokens=256000,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=0.9,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRALAI__DEVSTRAL_2512 = Model(
        id="mistralai/devstral-2512",
        name="Devstral 2 2512",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRALAI__DEVSTRAL_MEDIUM_2507 = Model(
        id="mistralai/devstral-medium-2507",
        name="Devstral Medium",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
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
            input=0.4,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRALAI__DEVSTRAL_SMALL_2505 = Model(
        id="mistralai/devstral-small-2505",
        name="Devstral Small",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.06,
            output=0.12,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRALAI__DEVSTRAL_SMALL_2507 = Model(
        id="mistralai/devstral-small-2507",
        name="Devstral Small 1.1",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
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
            input=0.1,
            output=0.3,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRALAI__MISTRAL_MEDIUM_3 = Model(
        id="mistralai/mistral-medium-3",
        name="Mistral Medium 3",
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
            context_window=131072,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRALAI__MISTRAL_MEDIUM_3_1 = Model(
        id="mistralai/mistral-medium-3.1",
        name="Mistral Medium 3.1",
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
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRALAI__MISTRAL_SMALL_2603 = Model(
        id="mistralai/mistral-small-2603",
        name="Mistral Small 4",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRALAI__MISTRAL_SMALL_3_1_24B_INSTRUCT = Model(
        id="mistralai/mistral-small-3.1-24b-instruct",
        name="Mistral Small 3.1 24B Instruct",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRALAI__MISTRAL_SMALL_3_2_24B_INSTRUCT = Model(
        id="mistralai/mistral-small-3.2-24b-instruct",
        name="Mistral Small 3.2 24B Instruct",
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
            context_window=96000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOTAI__KIMI_K2 = Model(
        id="moonshotai/kimi-k2",
        name="Kimi K2",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.55,
            output=2.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOTAI__KIMI_K2_0905 = Model(
        id="moonshotai/kimi-k2-0905",
        name="Kimi K2 Instruct 0905",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOTAI__KIMI_K2_0905_EXACTO = Model(
        id="moonshotai/kimi-k2-0905:exacto",
        name="Kimi K2 Instruct 0905 (exacto)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOTAI__KIMI_K2_THINKING = Model(
        id="moonshotai/kimi-k2-thinking",
        name="Kimi K2 Thinking",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    MOONSHOTAI__KIMI_K2_5 = Model(
        id="moonshotai/kimi-k2.5",
        name="Kimi K2.5",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    MOONSHOTAI__KIMI_K2_6 = Model(
        id="moonshotai/kimi-k2.6",
        name="Kimi K2.6",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    NOUSRESEARCH__HERMES_4_405B = Model(
        id="nousresearch/hermes-4-405b",
        name="Hermes 4 405B",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=1,
            output=3,
            cache_read=0,
            cache_write=0,
        ),
    )

    NOUSRESEARCH__HERMES_4_70B = Model(
        id="nousresearch/hermes-4-70b",
        name="Hermes 4 70B",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.13,
            output=0.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA__NEMOTRON_3_NANO_30B_A3B_FREE = Model(
        id="nvidia/nemotron-3-nano-30b-a3b:free",
        name="Nemotron 3 Nano 30B A3B (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA__NEMOTRON_3_NANO_OMNI_30B_A3B_REASONING_FREE = Model(
        id="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        name="Nemotron 3 Nano Omni (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA__NEMOTRON_3_SUPER_120B_A12B = Model(
        id="nvidia/nemotron-3-super-120b-a12b",
        name="Nemotron 3 Super",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.1,
            output=0.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA__NEMOTRON_3_SUPER_120B_A12B_FREE = Model(
        id="nvidia/nemotron-3-super-120b-a12b:free",
        name="Nemotron 3 Super (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA__NEMOTRON_NANO_12B_V2_VL_FREE = Model(
        id="nvidia/nemotron-nano-12b-v2-vl:free",
        name="Nemotron Nano 12B 2 VL (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA__NEMOTRON_NANO_9B_V2 = Model(
        id="nvidia/nemotron-nano-9b-v2",
        name="nvidia-nemotron-nano-9b-v2",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.04,
            output=0.16,
            cache_read=0,
            cache_write=0,
        ),
    )

    NVIDIA__NEMOTRON_NANO_9B_V2_FREE = Model(
        id="nvidia/nemotron-nano-9b-v2:free",
        name="Nemotron Nano 9B V2 (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_4_1 = Model(
        id="openai/gpt-4.1",
        name="GPT-4.1",
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
            context_window=1047576,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=2,
            output=8,
            cache_read=0.5,
            cache_write=0,
        ),
    )

    OPENAI__GPT_4_1_MINI = Model(
        id="openai/gpt-4.1-mini",
        name="GPT-4.1 Mini",
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
            context_window=1047576,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=1.6,
            cache_read=0.1,
            cache_write=0,
        ),
    )

    OPENAI__GPT_4O_MINI = Model(
        id="openai/gpt-4o-mini",
        name="GPT-4o-mini",
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
            input=0.15,
            output=0.6,
            cache_read=0.08,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5 = Model(
        id="openai/gpt-5",
        name="GPT-5",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=10,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_CODEX = Model(
        id="openai/gpt-5-codex",
        name="GPT-5 Codex",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=10,
            cache_read=0.125,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_IMAGE = Model(
        id="openai/gpt-5-image",
        name="GPT-5 Image",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=5,
            output=10,
            cache_read=1.25,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_MINI = Model(
        id="openai/gpt-5-mini",
        name="GPT-5 Mini",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.25,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_NANO = Model(
        id="openai/gpt-5-nano",
        name="GPT-5 Nano",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.05,
            output=0.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_PRO = Model(
        id="openai/gpt-5-pro",
        name="GPT-5 Pro",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=272000,
        ),
        pricing=ModelPricing(
            input=15,
            output=120,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_1 = Model(
        id="openai/gpt-5.1",
        name="GPT-5.1",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=10,
            cache_read=0.125,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_1_CHAT = Model(
        id="openai/gpt-5.1-chat",
        name="GPT-5.1 Chat",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=10,
            cache_read=0.125,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_1_CODEX = Model(
        id="openai/gpt-5.1-codex",
        name="GPT-5.1-Codex",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=10,
            cache_read=0.125,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_1_CODEX_MAX = Model(
        id="openai/gpt-5.1-codex-max",
        name="GPT-5.1-Codex-Max",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.1,
            output=9,
            cache_read=0.11,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_1_CODEX_MINI = Model(
        id="openai/gpt-5.1-codex-mini",
        name="GPT-5.1-Codex-Mini",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=100000,
        ),
        pricing=ModelPricing(
            input=0.25,
            output=2,
            cache_read=0.025,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_2 = Model(
        id="openai/gpt-5.2",
        name="GPT-5.2",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.75,
            output=14,
            cache_read=0.175,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_2_CHAT = Model(
        id="openai/gpt-5.2-chat",
        name="GPT-5.2 Chat",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=1.75,
            output=14,
            cache_read=0.175,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_2_CODEX = Model(
        id="openai/gpt-5.2-codex",
        name="GPT-5.2-Codex",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.75,
            output=14,
            cache_read=0.175,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_2_PRO = Model(
        id="openai/gpt-5.2-pro",
        name="GPT-5.2 Pro",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=21,
            output=168,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_3_CODEX = Model(
        id="openai/gpt-5.3-codex",
        name="GPT-5.3-Codex",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.75,
            output=14,
            cache_read=0.175,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_4 = Model(
        id="openai/gpt-5.4",
        name="GPT-5.4",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=1050000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=2.5,
            output=15,
            cache_read=0.25,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_4_MINI = Model(
        id="openai/gpt-5.4-mini",
        name="GPT-5.4 Mini",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.75,
            output=4.5,
            cache_read=0.075,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_4_NANO = Model(
        id="openai/gpt-5.4-nano",
        name="GPT-5.4 Nano",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=1.25,
            cache_read=0.02,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_4_PRO = Model(
        id="openai/gpt-5.4-pro",
        name="GPT-5.4 Pro",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=1050000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=30,
            output=180,
            cache_read=30,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_5 = Model(
        id="openai/gpt-5.5",
        name="GPT-5.5",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=1050000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=5,
            output=30,
            cache_read=0.5,
            cache_write=0,
        ),
    )

    OPENAI__GPT_5_5_PRO = Model(
        id="openai/gpt-5.5-pro",
        name="GPT-5.5 Pro",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=1050000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=30,
            output=180,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_120B = Model(
        id="openai/gpt-oss-120b",
        name="GPT OSS 120B",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.072,
            output=0.28,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_120B_EXACTO = Model(
        id="openai/gpt-oss-120b:exacto",
        name="GPT OSS 120B (exacto)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.05,
            output=0.24,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_120B_FREE = Model(
        id="openai/gpt-oss-120b:free",
        name="gpt-oss-120b (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_20B = Model(
        id="openai/gpt-oss-20b",
        name="GPT OSS 20B",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.05,
            output=0.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_20B_FREE = Model(
        id="openai/gpt-oss-20b:free",
        name="gpt-oss-20b (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_SAFEGUARD_20B = Model(
        id="openai/gpt-oss-safeguard-20b",
        name="GPT OSS Safeguard 20B",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.075,
            output=0.3,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__O4_MINI = Model(
        id="openai/o4-mini",
        name="o4 Mini",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=100000,
        ),
        pricing=ModelPricing(
            input=1.1,
            output=4.4,
            cache_read=0.28,
            cache_write=0,
        ),
    )

    OPENROUTER__ELEPHANT_ALPHA = Model(
        id="openrouter/elephant-alpha",
        name="Elephant (free)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    OPENROUTER__FREE = Model(
        id="openrouter/free",
        name="Free Models Router",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=8000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENROUTER__OWL_ALPHA = Model(
        id="openrouter/owl-alpha",
        name="Owl Alpha",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=1048756,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENROUTER__PARETO_CODE = Model(
        id="openrouter/pareto-code",
        name="Pareto Code Router",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=200000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    POOLSIDE__LAGUNA_M_1_FREE = Model(
        id="poolside/laguna-m.1:free",
        name="Laguna M.1",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    POOLSIDE__LAGUNA_XS_2_FREE = Model(
        id="poolside/laguna-xs.2:free",
        name="Laguna XS.2",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    PRIME_INTELLECT__INTELLECT_3 = Model(
        id="prime-intellect/intellect-3",
        name="Intellect 3",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.2,
            output=1.1,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN_3_6_27B = Model(
        id="qwen/qwen-3.6-27b",
        name="Qwen3.6 27B",
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
            context_window=262144,
            max_output_tokens=81920,
        ),
        pricing=ModelPricing(
            input=0.195,
            output=1.56,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN_PLUS = Model(
        id="qwen/qwen-plus",
        name="Qwen: Qwen-Plus",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.26,
            output=0.78,
            cache_read=0.052,
            cache_write=0.325,
        ),
    )

    QWEN__QWEN3_235B_A22B_07_25 = Model(
        id="qwen/qwen3-235b-a22b-07-25",
        name="Qwen3 235B A22B Instruct 2507",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            output=0.85,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_235B_A22B_THINKING_2507 = Model(
        id="qwen/qwen3-235b-a22b-thinking-2507",
        name="Qwen3 235B A22B Thinking 2507",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=81920,
        ),
        pricing=ModelPricing(
            input=0.078,
            output=0.312,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_30B_A3B_INSTRUCT_2507 = Model(
        id="qwen/qwen3-30b-a3b-instruct-2507",
        name="Qwen3 30B A3B Instruct 2507",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.2,
            output=0.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_30B_A3B_THINKING_2507 = Model(
        id="qwen/qwen3-30b-a3b-thinking-2507",
        name="Qwen3 30B A3B Thinking 2507",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=262000,
            max_output_tokens=262000,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_CODER = Model(
        id="qwen/qwen3-coder",
        name="Qwen3 Coder",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=66536,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_CODER_30B_A3B_INSTRUCT = Model(
        id="qwen/qwen3-coder-30b-a3b-instruct",
        name="Qwen3 Coder 30B A3B Instruct",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=160000,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.07,
            output=0.27,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_CODER_FLASH = Model(
        id="qwen/qwen3-coder-flash",
        name="Qwen3 Coder Flash",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=66536,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.5,
            cache_read=0.039,
            cache_write=0.24375,
        ),
    )

    QWEN__QWEN3_CODER_PLUS = Model(
        id="qwen/qwen3-coder-plus",
        name="Qwen3 Coder Plus",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1000000,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.65,
            output=3.25,
            cache_read=0.13,
            cache_write=0.8125,
        ),
    )

    QWEN__QWEN3_CODER_EXACTO = Model(
        id="qwen/qwen3-coder:exacto",
        name="Qwen3 Coder (exacto)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.38,
            output=1.53,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_MAX = Model(
        id="qwen/qwen3-max",
        name="Qwen3 Max",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=1.2,
            output=6,
            cache_read=0.156,
            cache_write=0.975,
        ),
    )

    QWEN__QWEN3_NEXT_80B_A3B_INSTRUCT = Model(
        id="qwen/qwen3-next-80b-a3b-instruct",
        name="Qwen3 Next 80B A3B Instruct",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.14,
            output=1.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_NEXT_80B_A3B_THINKING = Model(
        id="qwen/qwen3-next-80b-a3b-thinking",
        name="Qwen3 Next 80B A3B Thinking",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.14,
            output=1.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_5_397B_A17B = Model(
        id="qwen/qwen3.5-397b-a17b",
        name="Qwen3.5 397B A17B",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=3.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_5_FLASH_02_23 = Model(
        id="qwen/qwen3.5-flash-02-23",
        name="Qwen: Qwen3.5-Flash",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.065,
            output=0.26,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_5_PLUS_02_15 = Model(
        id="qwen/qwen3.5-plus-02-15",
        name="Qwen3.5 Plus 2026-02-15",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=2.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_6_PLUS = Model(
        id="qwen/qwen3.6-plus",
        name="Qwen3.6 Plus",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.325,
            output=1.95,
            cache_read=0.0325,
            cache_write=0.40625,
        ),
    )

    STEPFUN__STEP_3_5_FLASH = Model(
        id="stepfun/step-3.5-flash",
        name="Step 3.5 Flash",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    TENCENT__HY3_PREVIEW = Model(
        id="tencent/hy3-preview",
        name="Hy3 preview",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.066,
            output=0.26,
            cache_read=0.029,
            cache_write=0.029,
        ),
    )

    X_AI__GROK_3 = Model(
        id="x-ai/grok-3",
        name="Grok 3",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            cache_write=15,
        ),
    )

    X_AI__GROK_3_BETA = Model(
        id="x-ai/grok-3-beta",
        name="Grok 3 Beta",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            cache_write=15,
        ),
    )

    X_AI__GROK_3_MINI = Model(
        id="x-ai/grok-3-mini",
        name="Grok 3 Mini",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            cache_write=0.5,
        ),
    )

    X_AI__GROK_3_MINI_BETA = Model(
        id="x-ai/grok-3-mini-beta",
        name="Grok 3 Mini Beta",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            cache_write=0.5,
        ),
    )

    X_AI__GROK_4 = Model(
        id="x-ai/grok-4",
        name="Grok 4",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            cache_write=15,
        ),
    )

    X_AI__GROK_4_FAST = Model(
        id="x-ai/grok-4-fast",
        name="Grok 4 Fast",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            cache_write=0.05,
        ),
    )

    X_AI__GROK_4_1_FAST = Model(
        id="x-ai/grok-4.1-fast",
        name="Grok 4.1 Fast",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            cache_write=0.05,
        ),
    )

    X_AI__GROK_4_20_BETA = Model(
        id="x-ai/grok-4.20-beta",
        name="Grok 4.20 Beta",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    X_AI__GROK_4_3 = Model(
        id="x-ai/grok-4.3",
        name="Grok 4.3",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=1000000,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=2.5,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    X_AI__GROK_CODE_FAST_1 = Model(
        id="x-ai/grok-code-fast-1",
        name="Grok Code Fast 1",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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

    XIAOMI__MIMO_V2_FLASH = Model(
        id="xiaomi/mimo-v2-flash",
        name="Xiaomi: MiMo-V2-Flash",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.1,
            output=0.3,
            cache_read=0.01,
            cache_write=0,
        ),
    )

    XIAOMI__MIMO_V2_OMNI = Model(
        id="xiaomi/mimo-v2-omni",
        name="Xiaomi: MiMo-V2-Omni",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.4,
            output=2,
            cache_read=0.08,
            cache_write=0,
        ),
    )

    XIAOMI__MIMO_V2_PRO = Model(
        id="xiaomi/mimo-v2-pro",
        name="Xiaomi: MiMo-V2-Pro",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=1,
            output=3,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    XIAOMI__MIMO_V2_5 = Model(
        id="xiaomi/mimo-v2.5",
        name="Xiaomi: MiMo-V2.5",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=0.4,
            output=2,
            cache_read=0.08,
            cache_write=0,
        ),
    )

    XIAOMI__MIMO_V2_5_PRO = Model(
        id="xiaomi/mimo-v2.5-pro",
        name="Xiaomi: MiMo-V2.5-Pro",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            input=1,
            output=3,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    Z_AI__GLM_4_5 = Model(
        id="z-ai/glm-4.5",
        name="GLM 4.5",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=96000,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    Z_AI__GLM_4_5_AIR = Model(
        id="z-ai/glm-4.5-air",
        name="GLM 4.5 Air",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=96000,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=1.1,
            cache_read=0,
            cache_write=0,
        ),
    )

    Z_AI__GLM_4_5V = Model(
        id="z-ai/glm-4.5v",
        name="GLM 4.5V",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            context_window=64000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=1.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    Z_AI__GLM_4_6 = Model(
        id="z-ai/glm-4.6",
        name="GLM 4.6",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.2,
            cache_read=0.11,
            cache_write=0,
        ),
    )

    Z_AI__GLM_4_6_EXACTO = Model(
        id="z-ai/glm-4.6:exacto",
        name="GLM 4.6 (exacto)",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=1.9,
            cache_read=0.11,
            cache_write=0,
        ),
    )

    Z_AI__GLM_4_7 = Model(
        id="z-ai/glm-4.7",
        name="GLM-4.7",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            cache_read=0.11,
            cache_write=0,
        ),
    )

    Z_AI__GLM_4_7_FLASH = Model(
        id="z-ai/glm-4.7-flash",
        name="GLM-4.7-Flash",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=65535,
        ),
        pricing=ModelPricing(
            input=0.07,
            output=0.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    Z_AI__GLM_5 = Model(
        id="z-ai/glm-5",
        name="GLM-5",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=131000,
        ),
        pricing=ModelPricing(
            input=1,
            output=3.2,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    Z_AI__GLM_5_TURBO = Model(
        id="z-ai/glm-5-turbo",
        name="GLM-5-Turbo",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.96,
            output=3.2,
            cache_read=0.192,
            cache_write=0,
        ),
    )

    Z_AI__GLM_5_1 = Model(
        id="z-ai/glm-5.1",
        name="GLM-5.1",
        api="openai-completions",
        provider="openrouter",
        base_url="https://openrouter.ai/api/v1",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=1.4,
            output=4.4,
            cache_read=0.26,
            cache_write=0,
        ),
    )
