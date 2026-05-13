"""Auto-generated models for alibaba-cn.

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


class AlibabaCn:
    """Models for alibaba-cn."""

    MINIMAX_M2_5 = Model(
        id="MiniMax-M2.5",
        name="MiniMax-M2.5",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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

    MINIMAX__MINIMAX_M2_7 = Model(
        id="MiniMax/MiniMax-M2.7",
        name="MiniMax-M2.7",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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

    DEEPSEEK_R1 = Model(
        id="deepseek-r1",
        name="DeepSeek R1",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.574,
            output=2.294,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_R1_0528 = Model(
        id="deepseek-r1-0528",
        name="DeepSeek R1 0528",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.574,
            output=2.294,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_R1_DISTILL_LLAMA_70B = Model(
        id="deepseek-r1-distill-llama-70b",
        name="DeepSeek R1 Distill Llama 70B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            context_window=32768,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.287,
            output=0.861,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_R1_DISTILL_LLAMA_8B = Model(
        id="deepseek-r1-distill-llama-8b",
        name="DeepSeek R1 Distill Llama 8B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            context_window=32768,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_R1_DISTILL_QWEN_1_5B = Model(
        id="deepseek-r1-distill-qwen-1-5b",
        name="DeepSeek R1 Distill Qwen 1.5B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            context_window=32768,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_R1_DISTILL_QWEN_14B = Model(
        id="deepseek-r1-distill-qwen-14b",
        name="DeepSeek R1 Distill Qwen 14B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            context_window=32768,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.144,
            output=0.431,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_R1_DISTILL_QWEN_32B = Model(
        id="deepseek-r1-distill-qwen-32b",
        name="DeepSeek R1 Distill Qwen 32B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            context_window=32768,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.287,
            output=0.861,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_R1_DISTILL_QWEN_7B = Model(
        id="deepseek-r1-distill-qwen-7b",
        name="DeepSeek R1 Distill Qwen 7B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            context_window=32768,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.072,
            output=0.144,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_V3 = Model(
        id="deepseek-v3",
        name="DeepSeek V3",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=65536,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.287,
            output=1.147,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_V3_1 = Model(
        id="deepseek-v3-1",
        name="DeepSeek V3.1",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.574,
            output=1.721,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_V3_2_EXP = Model(
        id="deepseek-v3-2-exp",
        name="DeepSeek V3.2 Exp",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.287,
            output=0.431,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEEPSEEK_V4_FLASH = Model(
        id="deepseek-v4-flash",
        name="DeepSeek V4 Flash",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            cache_read=0.028,
            cache_write=0,
        ),
    )

    DEEPSEEK_V4_PRO = Model(
        id="deepseek-v4-pro",
        name="DeepSeek V4 Pro",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            cache_read=0.145,
            cache_write=0,
        ),
    )

    GLM_5 = Model(
        id="glm-5",
        name="GLM-5",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.86,
            output=3.15,
            cache_read=0,
            cache_write=0,
        ),
    )

    GLM_5_1 = Model(
        id="glm-5.1",
        name="GLM-5.1",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.87,
            output=3.48,
            cache_read=0.17,
            cache_write=0,
        ),
    )

    KIMI_K2_THINKING = Model(
        id="kimi-k2-thinking",
        name="Moonshot Kimi K2 Thinking",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.574,
            output=2.294,
            cache_read=0,
            cache_write=0,
        ),
    )

    KIMI_K2_5 = Model(
        id="kimi-k2.5",
        name="Moonshot Kimi K2.5",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.574,
            output=2.411,
            cache_read=0,
            cache_write=0,
        ),
    )

    KIMI_K2_6 = Model(
        id="kimi-k2.6",
        name="Moonshot Kimi K2.6",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.929,
            output=3.858,
            cache_read=0,
            cache_write=0,
        ),
    )

    KIMI__KIMI_K2_5 = Model(
        id="kimi/kimi-k2.5",
        name="kimi/kimi-k2.5",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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

    MOONSHOT_KIMI_K2_INSTRUCT = Model(
        id="moonshot-kimi-k2-instruct",
        name="Moonshot Kimi K2 Instruct",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.574,
            output=2.294,
            cache_read=0,
            cache_write=0,
        ),
    )

    QVQ_MAX = Model(
        id="qvq-max",
        name="QVQ Max",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            context_window=131072,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=1.147,
            output=4.588,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_DEEP_RESEARCH = Model(
        id="qwen-deep-research",
        name="Qwen Deep Research",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=7.742,
            output=23.367,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_DOC_TURBO = Model(
        id="qwen-doc-turbo",
        name="Qwen Doc Turbo",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.087,
            output=0.144,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_FLASH = Model(
        id="qwen-flash",
        name="Qwen Flash",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.022,
            output=0.216,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_LONG = Model(
        id="qwen-long",
        name="Qwen Long",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=10000000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.072,
            output=0.287,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_MATH_PLUS = Model(
        id="qwen-math-plus",
        name="Qwen Math Plus",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=4096,
            max_output_tokens=3072,
        ),
        pricing=ModelPricing(
            input=0.574,
            output=1.721,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_MATH_TURBO = Model(
        id="qwen-math-turbo",
        name="Qwen Math Turbo",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=4096,
            max_output_tokens=3072,
        ),
        pricing=ModelPricing(
            input=0.287,
            output=0.861,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_MAX = Model(
        id="qwen-max",
        name="Qwen Max",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.345,
            output=1.377,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_OMNI_TURBO = Model(
        id="qwen-omni-turbo",
        name="Qwen-Omni Turbo",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32768,
            max_output_tokens=2048,
        ),
        pricing=ModelPricing(
            input=0.058,
            output=0.23,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_OMNI_TURBO_REALTIME = Model(
        id="qwen-omni-turbo-realtime",
        name="Qwen-Omni Turbo Realtime",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32768,
            max_output_tokens=2048,
        ),
        pricing=ModelPricing(
            input=0.23,
            output=0.918,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_PLUS = Model(
        id="qwen-plus",
        name="Qwen Plus",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.115,
            output=0.287,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_PLUS_CHARACTER = Model(
        id="qwen-plus-character",
        name="Qwen Plus Character",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32768,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.115,
            output=0.287,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_TURBO = Model(
        id="qwen-turbo",
        name="Qwen Turbo",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.044,
            output=0.087,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_VL_MAX = Model(
        id="qwen-vl-max",
        name="Qwen-VL Max",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.23,
            output=0.574,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_VL_PLUS = Model(
        id="qwen-vl-plus",
        name="Qwen-VL Plus",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.115,
            output=0.287,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_14B_INSTRUCT = Model(
        id="qwen2-5-14b-instruct",
        name="Qwen2.5 14B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.144,
            output=0.431,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_32B_INSTRUCT = Model(
        id="qwen2-5-32b-instruct",
        name="Qwen2.5 32B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.287,
            output=0.861,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_72B_INSTRUCT = Model(
        id="qwen2-5-72b-instruct",
        name="Qwen2.5 72B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.574,
            output=1.721,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_7B_INSTRUCT = Model(
        id="qwen2-5-7b-instruct",
        name="Qwen2.5 7B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.072,
            output=0.144,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_CODER_32B_INSTRUCT = Model(
        id="qwen2-5-coder-32b-instruct",
        name="Qwen2.5-Coder 32B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.287,
            output=0.861,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_CODER_7B_INSTRUCT = Model(
        id="qwen2-5-coder-7b-instruct",
        name="Qwen2.5-Coder 7B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.144,
            output=0.287,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_MATH_72B_INSTRUCT = Model(
        id="qwen2-5-math-72b-instruct",
        name="Qwen2.5-Math 72B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=4096,
            max_output_tokens=3072,
        ),
        pricing=ModelPricing(
            input=0.574,
            output=1.721,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_MATH_7B_INSTRUCT = Model(
        id="qwen2-5-math-7b-instruct",
        name="Qwen2.5-Math 7B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=4096,
            max_output_tokens=3072,
        ),
        pricing=ModelPricing(
            input=0.144,
            output=0.287,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_OMNI_7B = Model(
        id="qwen2-5-omni-7b",
        name="Qwen2.5-Omni 7B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32768,
            max_output_tokens=2048,
        ),
        pricing=ModelPricing(
            input=0.087,
            output=0.345,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_VL_72B_INSTRUCT = Model(
        id="qwen2-5-vl-72b-instruct",
        name="Qwen2.5-VL 72B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=2.294,
            output=6.881,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_VL_7B_INSTRUCT = Model(
        id="qwen2-5-vl-7b-instruct",
        name="Qwen2.5-VL 7B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.287,
            output=0.717,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_14B = Model(
        id="qwen3-14b",
        name="Qwen3 14B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.144,
            output=0.574,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_235B_A22B = Model(
        id="qwen3-235b-a22b",
        name="Qwen3 235B-A22B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.287,
            output=1.147,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_32B = Model(
        id="qwen3-32b",
        name="Qwen3 32B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.287,
            output=1.147,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_8B = Model(
        id="qwen3-8b",
        name="Qwen3 8B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.072,
            output=0.287,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_CODER_30B_A3B_INSTRUCT = Model(
        id="qwen3-coder-30b-a3b-instruct",
        name="Qwen3-Coder 30B-A3B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.216,
            output=0.861,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_CODER_480B_A35B_INSTRUCT = Model(
        id="qwen3-coder-480b-a35b-instruct",
        name="Qwen3-Coder 480B-A35B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.861,
            output=3.441,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_CODER_FLASH = Model(
        id="qwen3-coder-flash",
        name="Qwen3 Coder Flash",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.144,
            output=0.574,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_CODER_PLUS = Model(
        id="qwen3-coder-plus",
        name="Qwen3 Coder Plus",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=1048576,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=1,
            output=5,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_MAX = Model(
        id="qwen3-max",
        name="Qwen3 Max",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=0.861,
            output=3.441,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_NEXT_80B_A3B_INSTRUCT = Model(
        id="qwen3-next-80b-a3b-instruct",
        name="Qwen3-Next 80B-A3B Instruct",
        api="openai-completions",
        provider="alibaba-cn",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.144,
            output=0.574,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_NEXT_80B_A3B_THINKING = Model(
        id="qwen3-next-80b-a3b-thinking",
        name="Qwen3-Next 80B-A3B (Thinking)",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.144,
            output=1.434,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_OMNI_FLASH = Model(
        id="qwen3-omni-flash",
        name="Qwen3-Omni Flash",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.058,
            output=0.23,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_OMNI_FLASH_REALTIME = Model(
        id="qwen3-omni-flash-realtime",
        name="Qwen3-Omni Flash Realtime",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=65536,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.23,
            output=0.918,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_VL_235B_A22B = Model(
        id="qwen3-vl-235b-a22b",
        name="Qwen3-VL 235B-A22B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            context_window=131072,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.286705,
            output=1.14682,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_VL_30B_A3B = Model(
        id="qwen3-vl-30b-a3b",
        name="Qwen3-VL 30B-A3B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            context_window=131072,
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.108,
            output=0.431,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_VL_PLUS = Model(
        id="qwen3-vl-plus",
        name="Qwen3-VL Plus",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.143353,
            output=1.43352,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_5_397B_A17B = Model(
        id="qwen3.5-397b-a17b",
        name="Qwen3.5 397B-A17B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.43,
            output=2.58,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_5_FLASH = Model(
        id="qwen3.5-flash",
        name="Qwen3.5 Flash",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.172,
            output=1.72,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_5_PLUS = Model(
        id="qwen3.5-plus",
        name="Qwen3.5 Plus",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.573,
            output=3.44,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_6_MAX_PREVIEW = Model(
        id="qwen3.6-max-preview",
        name="Qwen3.6 Max Preview",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            context_window=245800,
            max_output_tokens=65536,
        ),
        pricing=ModelPricing(
            input=1.32,
            output=7.9,
            cache_read=0.132,
            cache_write=0,
        ),
    )

    QWEN3_6_PLUS = Model(
        id="qwen3.6-plus",
        name="Qwen3.6 Plus",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.5,
            output=3,
            cache_read=0.05,
            cache_write=0.625,
        ),
    )

    QWQ_32B = Model(
        id="qwq-32b",
        name="QwQ 32B",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.287,
            output=0.861,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWQ_PLUS = Model(
        id="qwq-plus",
        name="QwQ Plus",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.23,
            output=0.574,
            cache_read=0,
            cache_write=0,
        ),
    )

    SILICONFLOW__DEEPSEEK_R1_0528 = Model(
        id="siliconflow/deepseek-r1-0528",
        name="siliconflow/deepseek-r1-0528",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            input=0.5,
            output=2.18,
            cache_read=0,
            cache_write=0,
        ),
    )

    SILICONFLOW__DEEPSEEK_V3_0324 = Model(
        id="siliconflow/deepseek-v3-0324",
        name="siliconflow/deepseek-v3-0324",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=163840,
            max_output_tokens=163840,
        ),
        pricing=ModelPricing(
            input=0.25,
            output=1,
            cache_read=0,
            cache_write=0,
        ),
    )

    SILICONFLOW__DEEPSEEK_V3_1_TERMINUS = Model(
        id="siliconflow/deepseek-v3.1-terminus",
        name="siliconflow/deepseek-v3.1-terminus",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            output=1,
            cache_read=0,
            cache_write=0,
        ),
    )

    SILICONFLOW__DEEPSEEK_V3_2 = Model(
        id="siliconflow/deepseek-v3.2",
        name="siliconflow/deepseek-v3.2",
        api="openai-completions",
        provider="alibaba-cn",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
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
            output=0.42,
            cache_read=0,
            cache_write=0,
        ),
    )
