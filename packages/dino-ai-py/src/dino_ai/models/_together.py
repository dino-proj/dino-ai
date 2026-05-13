"""Auto-generated models for together.

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


class Together:
    """Models for together."""

    MINIMAXAI__MINIMAX_M2_5 = Model(
        id="MiniMaxAI/MiniMax-M2.5",
        name="MiniMax-M2.5",
        api="openai-completions",
        provider="together",
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
            cache_read=0.06,
            cache_write=0,
        ),
    )

    MINIMAXAI__MINIMAX_M2_7 = Model(
        id="MiniMaxAI/MiniMax-M2.7",
        name="MiniMax-M2.7",
        api="openai-completions",
        provider="together",
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
            input=0.3,
            output=1.2,
            cache_read=0.06,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_235B_A22B_INSTRUCT_2507_TPUT = Model(
        id="Qwen/Qwen3-235B-A22B-Instruct-2507-tput",
        name="Qwen3 235B A22B Instruct 2507 FP8",
        api="openai-completions",
        provider="together",
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
            input=0.2,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_CODER_480B_A35B_INSTRUCT_FP8 = Model(
        id="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
        name="Qwen3 Coder 480B A35B Instruct",
        api="openai-completions",
        provider="together",
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
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=2,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_CODER_NEXT_FP8 = Model(
        id="Qwen/Qwen3-Coder-Next-FP8",
        name="Qwen3 Coder Next FP8",
        api="openai-completions",
        provider="together",
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
            input=0.5,
            output=1.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_5_397B_A17B = Model(
        id="Qwen/Qwen3.5-397B-A17B",
        name="Qwen3.5 397B A17B",
        api="openai-completions",
        provider="together",
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
            context_window=262144,
            max_output_tokens=130000,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=3.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_6_PLUS = Model(
        id="Qwen/Qwen3.6-Plus",
        name="Qwen3.6 Plus",
        api="openai-completions",
        provider="together",
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
            context_window=1000000,
            max_output_tokens=500000,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=3,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_AI__DEEPSEEK_V3 = Model(
        id="deepseek-ai/DeepSeek-V3",
        name="DeepSeek V3",
        api="openai-completions",
        provider="together",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=1.25,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_AI__DEEPSEEK_V3_1 = Model(
        id="deepseek-ai/DeepSeek-V3-1",
        name="DeepSeek V3.1",
        api="openai-completions",
        provider="together",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=1.7,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_AI__DEEPSEEK_V4_PRO = Model(
        id="deepseek-ai/DeepSeek-V4-Pro",
        name="DeepSeek V4 Pro",
        api="openai-completions",
        provider="together",
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
            context_window=512000,
            max_output_tokens=384000,
        ),
        pricing=ModelPricing(
            input=2.1,
            output=4.4,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    ESSENTIALAI__RNJ_1_INSTRUCT = Model(
        id="essentialai/Rnj-1-Instruct",
        name="Rnj-1 Instruct",
        api="openai-completions",
        provider="together",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32768,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.15,
            cache_read=0,
            cache_write=0,
        ),
    )

    GOOGLE__GEMMA_4_31B_IT = Model(
        id="google/gemma-4-31B-it",
        name="Gemma 4 31B Instruct",
        api="openai-completions",
        provider="together",
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
            context_window=262144,
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    META_LLAMA__LLAMA_3_3_70B_INSTRUCT_TURBO = Model(
        id="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        name="Llama 3.3 70B",
        api="openai-completions",
        provider="together",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.88,
            output=0.88,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOTAI__KIMI_K2_5 = Model(
        id="moonshotai/Kimi-K2.5",
        name="Kimi K2.5",
        api="openai-completions",
        provider="together",
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
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=2.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOTAI__KIMI_K2_6 = Model(
        id="moonshotai/Kimi-K2.6",
        name="Kimi K2.6",
        api="openai-completions",
        provider="together",
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
            context_window=262144,
            max_output_tokens=131000,
        ),
        pricing=ModelPricing(
            input=1.2,
            output=4.5,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_120B = Model(
        id="openai/gpt-oss-120b",
        name="GPT OSS 120B",
        api="openai-completions",
        provider="together",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    ZAI_ORG__GLM_5_1 = Model(
        id="zai-org/GLM-5.1",
        name="GLM-5.1",
        api="openai-completions",
        provider="together",
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
            input=1.4,
            output=4.4,
            cache_read=0,
            cache_write=0,
        ),
    )
