"""Auto-generated models for fireworks.

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


class Fireworks:
    """Models for fireworks."""

    ACCOUNTS__FIREWORKS__MODELS__DEEPSEEK_V3P1 = Model(
        id="accounts/fireworks/models/deepseek-v3p1",
        name="DeepSeek V3.1",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            input=0.56,
            output=1.68,
            cache_read=0,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__DEEPSEEK_V3P2 = Model(
        id="accounts/fireworks/models/deepseek-v3p2",
        name="DeepSeek V3.2",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            context_window=160000,
            max_output_tokens=160000,
        ),
        pricing=ModelPricing(
            input=0.56,
            output=1.68,
            cache_read=0.28,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__DEEPSEEK_V4_PRO = Model(
        id="accounts/fireworks/models/deepseek-v4-pro",
        name="DeepSeek V4 Pro",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            cache_read=0.15,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__GLM_4P5 = Model(
        id="accounts/fireworks/models/glm-4p5",
        name="GLM 4.5",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            input=0.55,
            output=2.19,
            cache_read=0,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__GLM_4P5_AIR = Model(
        id="accounts/fireworks/models/glm-4p5-air",
        name="GLM 4.5 Air",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            input=0.22,
            output=0.88,
            cache_read=0,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__GLM_4P7 = Model(
        id="accounts/fireworks/models/glm-4p7",
        name="GLM 4.7",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            context_window=198000,
            max_output_tokens=198000,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=2.2,
            cache_read=0.3,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__GLM_5 = Model(
        id="accounts/fireworks/models/glm-5",
        name="GLM 5",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            cache_read=0.5,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__GLM_5P1 = Model(
        id="accounts/fireworks/models/glm-5p1",
        name="GLM 5.1",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            context_window=202800,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=1.4,
            output=4.4,
            cache_read=0.26,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__GPT_OSS_120B = Model(
        id="accounts/fireworks/models/gpt-oss-120b",
        name="GPT OSS 120B",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__GPT_OSS_20B = Model(
        id="accounts/fireworks/models/gpt-oss-20b",
        name="GPT OSS 20B",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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

    ACCOUNTS__FIREWORKS__MODELS__KIMI_K2_INSTRUCT = Model(
        id="accounts/fireworks/models/kimi-k2-instruct",
        name="Kimi K2 Instruct",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=1,
            output=3,
            cache_read=0,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__KIMI_K2_THINKING = Model(
        id="accounts/fireworks/models/kimi-k2-thinking",
        name="Kimi K2 Thinking",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            cache_read=0.3,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__KIMI_K2P5 = Model(
        id="accounts/fireworks/models/kimi-k2p5",
        name="Kimi K2.5",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            cache_read=0.1,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__KIMI_K2P6 = Model(
        id="accounts/fireworks/models/kimi-k2p6",
        name="Kimi K2.6",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            context_window=262000,
            max_output_tokens=262000,
        ),
        pricing=ModelPricing(
            input=0.95,
            output=4,
            cache_read=0.16,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__MINIMAX_M2P1 = Model(
        id="accounts/fireworks/models/minimax-m2p1",
        name="MiniMax-M2.1",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            input=0.3,
            output=1.2,
            cache_read=0.03,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__MINIMAX_M2P5 = Model(
        id="accounts/fireworks/models/minimax-m2p5",
        name="MiniMax-M2.5",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            max_output_tokens=196608,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.2,
            cache_read=0.03,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__MINIMAX_M2P7 = Model(
        id="accounts/fireworks/models/minimax-m2p7",
        name="MiniMax-M2.7",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            max_output_tokens=196608,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=1.2,
            cache_read=0.03,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__MODELS__QWEN3P6_PLUS = Model(
        id="accounts/fireworks/models/qwen3p6-plus",
        name="Qwen 3.6 Plus",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=3,
            cache_read=0.1,
            cache_write=0,
        ),
    )

    ACCOUNTS__FIREWORKS__ROUTERS__KIMI_K2P5_TURBO = Model(
        id="accounts/fireworks/routers/kimi-k2p5-turbo",
        name="Kimi K2.5 Turbo",
        api="openai-completions",
        provider="fireworks",
        base_url="https://api.fireworks.ai/inference/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )
