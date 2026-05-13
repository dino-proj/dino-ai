"""Auto-generated models for google.

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


class Google:
    """Models for google."""

    GEMINI_1_5_FLASH = Model(
        id="gemini-1.5-flash",
        name="Gemini 1.5 Flash",
        api="google-generative-ai",
        provider="google",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.075,
            output=0.3,
            cache_read=0.01875,
            cache_write=0,
        ),
    )

    GEMINI_1_5_FLASH_8B = Model(
        id="gemini-1.5-flash-8b",
        name="Gemini 1.5 Flash-8B",
        api="google-generative-ai",
        provider="google",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.0375,
            output=0.15,
            cache_read=0.01,
            cache_write=0,
        ),
    )

    GEMINI_1_5_PRO = Model(
        id="gemini-1.5-pro",
        name="Gemini 1.5 Pro",
        api="google-generative-ai",
        provider="google",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=5,
            cache_read=0.3125,
            cache_write=0,
        ),
    )

    GEMINI_2_0_FLASH = Model(
        id="gemini-2.0-flash",
        name="Gemini 2.0 Flash",
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
            cache_read=0.03,
            cache_write=0,
        ),
    )

    GEMINI_2_5_FLASH_LITE = Model(
        id="gemini-2.5-flash-lite",
        name="Gemini 2.5 Flash Lite",
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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

    GEMINI_2_5_FLASH_LITE_PREVIEW_09_2025 = Model(
        id="gemini-2.5-flash-lite-preview-09-2025",
        name="Gemini 2.5 Flash Lite Preview 09-25",
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
            cache_write=0,
        ),
    )

    GEMINI_2_5_PRO = Model(
        id="gemini-2.5-pro",
        name="Gemini 2.5 Pro",
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
            input=2,
            output=12,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    GEMINI_3_1_FLASH_LITE = Model(
        id="gemini-3.1-flash-lite",
        name="Gemini 3.1 Flash Lite",
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
        api="google-generative-ai",
        provider="google",
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
            cache_write=0,
        ),
    )

    GEMINI_FLASH_LITE_LATEST = Model(
        id="gemini-flash-lite-latest",
        name="Gemini Flash-Lite Latest",
        api="google-generative-ai",
        provider="google",
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

    GEMINI_LIVE_2_5_FLASH = Model(
        id="gemini-live-2.5-flash",
        name="Gemini Live 2.5 Flash",
        api="google-generative-ai",
        provider="google",
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
            max_output_tokens=8000,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    GEMINI_LIVE_2_5_FLASH_PREVIEW_NATIVE_AUDIO = Model(
        id="gemini-live-2.5-flash-preview-native-audio",
        name="Gemini Live 2.5 Flash Preview Native Audio",
        api="google-generative-ai",
        provider="google",
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
            input=0.5,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    GEMMA_3_27B_IT = Model(
        id="gemma-3-27b-it",
        name="Gemma 3 27B",
        api="google-generative-ai",
        provider="google",
        base_url="",
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

    GEMMA_4_26B_A4B_IT = Model(
        id="gemma-4-26b-a4b-it",
        name="Gemma 4 26B",
        api="google-generative-ai",
        provider="google",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    GEMMA_4_31B_IT = Model(
        id="gemma-4-31b-it",
        name="Gemma 4 31B",
        api="google-generative-ai",
        provider="google",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )
