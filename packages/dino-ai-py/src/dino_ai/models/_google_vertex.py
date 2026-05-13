"""Auto-generated models for google-vertex.

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


class GoogleVertex:
    """Models for google-vertex."""

    CLAUDE_3_5_HAIKU_20241022 = Model(
        id="claude-3-5-haiku@20241022",
        name="Claude Haiku 3.5",
        api="google-vertex",
        provider="google-vertex",
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

    CLAUDE_3_5_SONNET_20241022 = Model(
        id="claude-3-5-sonnet@20241022",
        name="Claude Sonnet 3.5 v2",
        api="google-vertex",
        provider="google-vertex",
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
        id="claude-3-7-sonnet@20250219",
        name="Claude Sonnet 3.7",
        api="google-vertex",
        provider="google-vertex",
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

    CLAUDE_HAIKU_4_5_20251001 = Model(
        id="claude-haiku-4-5@20251001",
        name="Claude Haiku 4.5",
        api="google-vertex",
        provider="google-vertex",
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

    CLAUDE_OPUS_4_1_20250805 = Model(
        id="claude-opus-4-1@20250805",
        name="Claude Opus 4.1",
        api="google-vertex",
        provider="google-vertex",
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

    CLAUDE_OPUS_4_5_20251101 = Model(
        id="claude-opus-4-5@20251101",
        name="Claude Opus 4.5",
        api="google-vertex",
        provider="google-vertex",
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

    CLAUDE_OPUS_4_6_DEFAULT = Model(
        id="claude-opus-4-6@default",
        name="Claude Opus 4.6",
        api="google-vertex",
        provider="google-vertex",
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

    CLAUDE_OPUS_4_7_DEFAULT = Model(
        id="claude-opus-4-7@default",
        name="Claude Opus 4.7",
        api="google-vertex",
        provider="google-vertex",
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

    CLAUDE_OPUS_4_20250514 = Model(
        id="claude-opus-4@20250514",
        name="Claude Opus 4",
        api="google-vertex",
        provider="google-vertex",
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

    CLAUDE_SONNET_4_5_20250929 = Model(
        id="claude-sonnet-4-5@20250929",
        name="Claude Sonnet 4.5",
        api="google-vertex",
        provider="google-vertex",
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

    CLAUDE_SONNET_4_6_DEFAULT = Model(
        id="claude-sonnet-4-6@default",
        name="Claude Sonnet 4.6",
        api="google-vertex",
        provider="google-vertex",
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
        id="claude-sonnet-4@20250514",
        name="Claude Sonnet 4",
        api="google-vertex",
        provider="google-vertex",
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

    DEEPSEEK_AI__DEEPSEEK_V3_1_MAAS = Model(
        id="deepseek-ai/deepseek-v3.1-maas",
        name="DeepSeek V3.1",
        api="google-vertex",
        provider="google-vertex",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=1.7,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_AI__DEEPSEEK_V3_2_MAAS = Model(
        id="deepseek-ai/deepseek-v3.2-maas",
        name="DeepSeek V3.2",
        api="google-vertex",
        provider="google-vertex",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.56,
            output=1.68,
            cache_read=0.056,
            cache_write=0,
        ),
    )

    GEMINI_2_0_FLASH = Model(
        id="gemini-2.0-flash",
        name="Gemini 2.0 Flash",
        api="google-vertex",
        provider="google-vertex",
        base_url="",
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
            input=0.15,
            output=0.6,
            cache_read=0.025,
            cache_write=0,
        ),
    )

    GEMINI_2_0_FLASH_LITE = Model(
        id="gemini-2.0-flash-lite",
        name="Gemini 2.0 Flash Lite",
        api="google-vertex",
        provider="google-vertex",
        base_url="",
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
            cache_read=0,
            cache_write=0,
        ),
    )

    GEMINI_2_5_FLASH = Model(
        id="gemini-2.5-flash",
        name="Gemini 2.5 Flash",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=2.5,
            cache_read=0.075,
            cache_write=0.383,
        ),
    )

    GEMINI_2_5_FLASH_LITE = Model(
        id="gemini-2.5-flash-lite",
        name="Gemini 2.5 Flash Lite",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.4,
            cache_read=0.01,
            cache_write=0,
        ),
    )

    GEMINI_2_5_FLASH_LITE_PREVIEW_06_17 = Model(
        id="gemini-2.5-flash-lite-preview-06-17",
        name="Gemini 2.5 Flash Lite Preview 06-17",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=65536,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.4,
            cache_read=0.025,
            cache_write=0,
        ),
    )

    GEMINI_2_5_FLASH_LITE_PREVIEW_09_2025 = Model(
        id="gemini-2.5-flash-lite-preview-09-2025",
        name="Gemini 2.5 Flash Lite Preview 09-25",
        api="google-vertex",
        provider="google-vertex",
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

    GEMINI_2_5_FLASH_PREVIEW_04_17 = Model(
        id="gemini-2.5-flash-preview-04-17",
        name="Gemini 2.5 Flash Preview 04-17",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0.0375,
            cache_write=0,
        ),
    )

    GEMINI_2_5_FLASH_PREVIEW_05_20 = Model(
        id="gemini-2.5-flash-preview-05-20",
        name="Gemini 2.5 Flash Preview 05-20",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0.0375,
            cache_write=0,
        ),
    )

    GEMINI_2_5_FLASH_PREVIEW_09_2025 = Model(
        id="gemini-2.5-flash-preview-09-2025",
        name="Gemini 2.5 Flash Preview 09-25",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=2.5,
            cache_read=0.075,
            cache_write=0.383,
        ),
    )

    GEMINI_2_5_PRO = Model(
        id="gemini-2.5-pro",
        name="Gemini 2.5 Pro",
        api="google-vertex",
        provider="google-vertex",
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

    GEMINI_2_5_PRO_PREVIEW_05_06 = Model(
        id="gemini-2.5-pro-preview-05-06",
        name="Gemini 2.5 Pro Preview 05-06",
        api="google-vertex",
        provider="google-vertex",
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

    GEMINI_2_5_PRO_PREVIEW_06_05 = Model(
        id="gemini-2.5-pro-preview-06-05",
        name="Gemini 2.5 Pro Preview 06-05",
        api="google-vertex",
        provider="google-vertex",
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

    GEMINI_3_FLASH_PREVIEW = Model(
        id="gemini-3-flash-preview",
        name="Gemini 3 Flash Preview",
        api="google-vertex",
        provider="google-vertex",
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

    GEMINI_3_PRO_PREVIEW = Model(
        id="gemini-3-pro-preview",
        name="Gemini 3 Pro Preview",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=2,
            output=12,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    GEMINI_3_1_FLASH_LITE = Model(
        id="gemini-3.1-flash-lite",
        name="Gemini 3.1 Flash Lite",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.25,
            output=1.5,
            cache_read=0.025,
            cache_write=0,
        ),
    )

    GEMINI_3_1_FLASH_LITE_PREVIEW = Model(
        id="gemini-3.1-flash-lite-preview",
        name="Gemini 3.1 Flash Lite Preview",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.25,
            output=1.5,
            cache_read=0.025,
            cache_write=0,
        ),
    )

    GEMINI_3_1_PRO_PREVIEW = Model(
        id="gemini-3.1-pro-preview",
        name="Gemini 3.1 Pro Preview",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=2,
            output=12,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    GEMINI_3_1_PRO_PREVIEW_CUSTOMTOOLS = Model(
        id="gemini-3.1-pro-preview-customtools",
        name="Gemini 3.1 Pro Preview Custom Tools",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=2,
            output=12,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    GEMINI_FLASH_LATEST = Model(
        id="gemini-flash-latest",
        name="Gemini Flash Latest",
        api="google-vertex",
        provider="google-vertex",
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
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=2.5,
            cache_read=0.075,
            cache_write=0.383,
        ),
    )

    GEMINI_FLASH_LITE_LATEST = Model(
        id="gemini-flash-lite-latest",
        name="Gemini Flash-Lite Latest",
        api="google-vertex",
        provider="google-vertex",
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

    META__LLAMA_3_3_70B_INSTRUCT_MAAS = Model(
        id="meta/llama-3.3-70b-instruct-maas",
        name="Llama 3.3 70B Instruct",
        api="google-vertex",
        provider="google-vertex",
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
            input=0.72,
            output=0.72,
            cache_read=0,
            cache_write=0,
        ),
    )

    META__LLAMA_4_MAVERICK_17B_128E_INSTRUCT_MAAS = Model(
        id="meta/llama-4-maverick-17b-128e-instruct-maas",
        name="Llama 4 Maverick 17B 128E Instruct",
        api="google-vertex",
        provider="google-vertex",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=524288,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.35,
            output=1.15,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOTAI__KIMI_K2_THINKING_MAAS = Model(
        id="moonshotai/kimi-k2-thinking-maas",
        name="Kimi K2 Thinking",
        api="google-vertex",
        provider="google-vertex",
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
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_120B_MAAS = Model(
        id="openai/gpt-oss-120b-maas",
        name="GPT OSS 120B",
        api="google-vertex",
        provider="google-vertex",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.09,
            output=0.36,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_20B_MAAS = Model(
        id="openai/gpt-oss-20b-maas",
        name="GPT OSS 20B",
        api="google-vertex",
        provider="google-vertex",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.07,
            output=0.25,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_235B_A22B_INSTRUCT_2507_MAAS = Model(
        id="qwen/qwen3-235b-a22b-instruct-2507-maas",
        name="Qwen3 235B A22B Instruct",
        api="google-vertex",
        provider="google-vertex",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.22,
            output=0.88,
            cache_read=0,
            cache_write=0,
        ),
    )

    ZAI_ORG__GLM_4_7_MAAS = Model(
        id="zai-org/glm-4.7-maas",
        name="GLM-4.7",
        api="google-vertex",
        provider="google-vertex",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    ZAI_ORG__GLM_5_MAAS = Model(
        id="zai-org/glm-5-maas",
        name="GLM-5",
        api="google-vertex",
        provider="google-vertex",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=1,
            output=3.2,
            cache_read=0.1,
            cache_write=0,
        ),
    )
