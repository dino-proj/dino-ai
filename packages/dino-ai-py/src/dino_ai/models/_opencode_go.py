"""Auto-generated models for opencode-go.

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


class OpencodeGo:
    """Models for opencode-go."""

    DEEPSEEK_V4_FLASH = Model(
        id="deepseek-v4-flash",
        name="DeepSeek V4 Flash",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            cache_read=0.0028,
            cache_write=0,
        ),
    )

    DEEPSEEK_V4_PRO = Model(
        id="deepseek-v4-pro",
        name="DeepSeek V4 Pro",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            cache_read=0.0145,
            cache_write=0,
        ),
    )

    GLM_5 = Model(
        id="glm-5",
        name="GLM-5",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=1,
            output=3.2,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    GLM_5_1 = Model(
        id="glm-5.1",
        name="GLM-5.1",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=1.4,
            output=4.4,
            cache_read=0.26,
            cache_write=0,
        ),
    )

    KIMI_K2_5 = Model(
        id="kimi-k2.5",
        name="Kimi K2.5",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            output=3,
            cache_read=0.1,
            cache_write=0,
        ),
    )

    KIMI_K2_6 = Model(
        id="kimi-k2.6",
        name="Kimi K2.6",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            input=0.95,
            output=4,
            cache_read=0.16,
            cache_write=0,
        ),
    )

    MIMO_V2_OMNI = Model(
        id="mimo-v2-omni",
        name="MiMo V2 Omni",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=2,
            cache_read=0.08,
            cache_write=0,
        ),
    )

    MIMO_V2_PRO = Model(
        id="mimo-v2-pro",
        name="MiMo V2 Pro",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1,
            output=3,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    MIMO_V2_5 = Model(
        id="mimo-v2.5",
        name="MiMo V2.5",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            input=0.4,
            output=2,
            cache_read=0.08,
            cache_write=0,
        ),
    )

    MIMO_V2_5_PRO = Model(
        id="mimo-v2.5-pro",
        name="MiMo V2.5 Pro",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1,
            output=3,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    MINIMAX_M2_5 = Model(
        id="minimax-m2.5",
        name="MiniMax M2.5",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.2,
            cache_read=0.03,
            cache_write=0,
        ),
    )

    MINIMAX_M2_7 = Model(
        id="minimax-m2.7",
        name="MiniMax M2.7",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            cache_write=0,
        ),
    )

    QWEN3_5_PLUS = Model(
        id="qwen3.5-plus",
        name="Qwen3.5 Plus",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            input=0.2,
            output=1.2,
            cache_read=0.02,
            cache_write=0.25,
        ),
    )

    QWEN3_6_PLUS = Model(
        id="qwen3.6-plus",
        name="Qwen3.6 Plus",
        api="openai-completions",
        provider="opencode-go",
        base_url="https://opencode.ai/zen/go/v1",
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
            input=0.5,
            output=3,
            cache_read=0.05,
            cache_write=0.625,
        ),
    )
