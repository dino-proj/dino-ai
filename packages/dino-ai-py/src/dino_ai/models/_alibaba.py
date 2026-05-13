"""Auto-generated models for alibaba.

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


class Alibaba:
    """Models for alibaba."""

    QVQ_MAX = Model(
        id="qvq-max",
        name="QVQ Max",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=1.2,
            output=4.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_FLASH = Model(
        id="qwen-flash",
        name="Qwen Flash",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.05,
            output=0.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_MAX = Model(
        id="qwen-max",
        name="Qwen Max",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32768,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=1.6,
            output=6.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_OMNI_TURBO = Model(
        id="qwen-omni-turbo",
        name="Qwen-Omni Turbo",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.07,
            output=0.27,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_OMNI_TURBO_REALTIME = Model(
        id="qwen-omni-turbo-realtime",
        name="Qwen-Omni Turbo Realtime",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.27,
            output=1.07,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_PLUS = Model(
        id="qwen-plus",
        name="Qwen Plus",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.4,
            output=1.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_PLUS_CHARACTER_JA = Model(
        id="qwen-plus-character-ja",
        name="Qwen Plus Character (Japanese)",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8192,
            max_output_tokens=512,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=1.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_TURBO = Model(
        id="qwen-turbo",
        name="Qwen Turbo",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.05,
            output=0.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_VL_MAX = Model(
        id="qwen-vl-max",
        name="Qwen-VL Max",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.8,
            output=3.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_VL_PLUS = Model(
        id="qwen-vl-plus",
        name="Qwen-VL Plus",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.21,
            output=0.63,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_14B_INSTRUCT = Model(
        id="qwen2-5-14b-instruct",
        name="Qwen2.5 14B Instruct",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.35,
            output=1.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_32B_INSTRUCT = Model(
        id="qwen2-5-32b-instruct",
        name="Qwen2.5 32B Instruct",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.7,
            output=2.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_72B_INSTRUCT = Model(
        id="qwen2-5-72b-instruct",
        name="Qwen2.5 72B Instruct",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=1.4,
            output=5.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_7B_INSTRUCT = Model(
        id="qwen2-5-7b-instruct",
        name="Qwen2.5 7B Instruct",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.175,
            output=0.7,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_OMNI_7B = Model(
        id="qwen2-5-omni-7b",
        name="Qwen2.5-Omni 7B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.1,
            output=0.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_VL_72B_INSTRUCT = Model(
        id="qwen2-5-vl-72b-instruct",
        name="Qwen2.5-VL 72B Instruct",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=2.8,
            output=8.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN2_5_VL_7B_INSTRUCT = Model(
        id="qwen2-5-vl-7b-instruct",
        name="Qwen2.5-VL 7B Instruct",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.35,
            output=1.05,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_14B = Model(
        id="qwen3-14b",
        name="Qwen3 14B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.35,
            output=1.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_235B_A22B = Model(
        id="qwen3-235b-a22b",
        name="Qwen3 235B-A22B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.7,
            output=2.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_32B = Model(
        id="qwen3-32b",
        name="Qwen3 32B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.7,
            output=2.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_8B = Model(
        id="qwen3-8b",
        name="Qwen3 8B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.18,
            output=0.7,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_CODER_30B_A3B_INSTRUCT = Model(
        id="qwen3-coder-30b-a3b-instruct",
        name="Qwen3-Coder 30B-A3B Instruct",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.45,
            output=2.25,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_CODER_480B_A35B_INSTRUCT = Model(
        id="qwen3-coder-480b-a35b-instruct",
        name="Qwen3-Coder 480B-A35B Instruct",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=1.5,
            output=7.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_CODER_FLASH = Model(
        id="qwen3-coder-flash",
        name="Qwen3 Coder Flash",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.3,
            output=1.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_CODER_PLUS = Model(
        id="qwen3-coder-plus",
        name="Qwen3 Coder Plus",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=1.2,
            output=6,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_NEXT_80B_A3B_INSTRUCT = Model(
        id="qwen3-next-80b-a3b-instruct",
        name="Qwen3-Next 80B-A3B Instruct",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.5,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_NEXT_80B_A3B_THINKING = Model(
        id="qwen3-next-80b-a3b-thinking",
        name="Qwen3-Next 80B-A3B (Thinking)",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.5,
            output=6,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_OMNI_FLASH = Model(
        id="qwen3-omni-flash",
        name="Qwen3-Omni Flash",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.43,
            output=1.66,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_OMNI_FLASH_REALTIME = Model(
        id="qwen3-omni-flash-realtime",
        name="Qwen3-Omni Flash Realtime",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.52,
            output=1.99,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_VL_235B_A22B = Model(
        id="qwen3-vl-235b-a22b",
        name="Qwen3-VL 235B-A22B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.7,
            output=2.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_VL_30B_A3B = Model(
        id="qwen3-vl-30b-a3b",
        name="Qwen3-VL 30B-A3B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.2,
            output=0.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_VL_PLUS = Model(
        id="qwen3-vl-plus",
        name="Qwen3-VL Plus",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.2,
            output=1.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_5_122B_A10B = Model(
        id="qwen3.5-122b-a10b",
        name="Qwen3.5 122B-A10B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.4,
            output=3.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_5_27B = Model(
        id="qwen3.5-27b",
        name="Qwen3.5 27B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.3,
            output=2.4,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_5_35B_A3B = Model(
        id="qwen3.5-35b-a3b",
        name="Qwen3.5 35B-A3B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.25,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_5_397B_A17B = Model(
        id="qwen3.5-397b-a17b",
        name="Qwen3.5 397B-A17B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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

    QWEN3_5_PLUS = Model(
        id="qwen3.5-plus",
        name="Qwen3.5 Plus",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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

    QWEN3_6_27B = Model(
        id="qwen3.6-27b",
        name="Qwen3.6 27B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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

    QWEN3_6_35B_A3B = Model(
        id="qwen3.6-35b-a3b",
        name="Qwen3.6 35B-A3B",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.248,
            output=1.485,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_6_MAX_PREVIEW = Model(
        id="qwen3.6-max-preview",
        name="Qwen3.6 Max Preview",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=1.3,
            output=7.8,
            cache_read=0.13,
            cache_write=1.625,
        ),
    )

    QWEN3_6_PLUS = Model(
        id="qwen3.6-plus",
        name="Qwen3.6 Plus",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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

    QWQ_PLUS = Model(
        id="qwq-plus",
        name="QwQ Plus",
        api="openai-completions",
        provider="alibaba",
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
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
            input=0.8,
            output=2.4,
            cache_read=0,
            cache_write=0,
        ),
    )
