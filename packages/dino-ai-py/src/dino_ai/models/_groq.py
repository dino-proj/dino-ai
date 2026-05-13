"""Auto-generated models for groq.

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


class Groq:
    """Models for groq."""

    DEEPSEEK_R1_DISTILL_LLAMA_70B = Model(
        id="deepseek-r1-distill-llama-70b",
        name="DeepSeek R1 Distill Llama 70B",
        api="openai-completions",
        provider="groq",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.75,
            output=0.99,
            cache_read=0,
            cache_write=0,
        ),
    )

    GEMMA2_9B_IT = Model(
        id="gemma2-9b-it",
        name="Gemma 2 9B",
        api="openai-completions",
        provider="groq",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8192,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    GROQ__COMPOUND = Model(
        id="groq/compound",
        name="Compound",
        api="openai-completions",
        provider="groq",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    GROQ__COMPOUND_MINI = Model(
        id="groq/compound-mini",
        name="Compound Mini",
        api="openai-completions",
        provider="groq",
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
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    LLAMA_3_1_8B_INSTANT = Model(
        id="llama-3.1-8b-instant",
        name="Llama 3.1 8B Instant",
        api="openai-completions",
        provider="groq",
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
            input=0.05,
            output=0.08,
            cache_read=0,
            cache_write=0,
        ),
    )

    LLAMA_3_3_70B_VERSATILE = Model(
        id="llama-3.3-70b-versatile",
        name="Llama 3.3 70B Versatile",
        api="openai-completions",
        provider="groq",
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
            max_output_tokens=32768,
        ),
        pricing=ModelPricing(
            input=0.59,
            output=0.79,
            cache_read=0,
            cache_write=0,
        ),
    )

    LLAMA3_70B_8192 = Model(
        id="llama3-70b-8192",
        name="Llama 3 70B",
        api="openai-completions",
        provider="groq",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8192,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.59,
            output=0.79,
            cache_read=0,
            cache_write=0,
        ),
    )

    LLAMA3_8B_8192 = Model(
        id="llama3-8b-8192",
        name="Llama 3 8B",
        api="openai-completions",
        provider="groq",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8192,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.05,
            output=0.08,
            cache_read=0,
            cache_write=0,
        ),
    )

    META_LLAMA__LLAMA_4_MAVERICK_17B_128E_INSTRUCT = Model(
        id="meta-llama/llama-4-maverick-17b-128e-instruct",
        name="Llama 4 Maverick 17B",
        api="openai-completions",
        provider="groq",
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
            input=0.2,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    META_LLAMA__LLAMA_4_SCOUT_17B_16E_INSTRUCT = Model(
        id="meta-llama/llama-4-scout-17b-16e-instruct",
        name="Llama 4 Scout 17B",
        api="openai-completions",
        provider="groq",
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
            input=0.11,
            output=0.34,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_SABA_24B = Model(
        id="mistral-saba-24b",
        name="Mistral Saba 24B",
        api="openai-completions",
        provider="groq",
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
            input=0.79,
            output=0.79,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOTAI__KIMI_K2_INSTRUCT = Model(
        id="moonshotai/kimi-k2-instruct",
        name="Kimi K2 Instruct",
        api="openai-completions",
        provider="groq",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=1,
            output=3,
            cache_read=0,
            cache_write=0,
        ),
    )

    MOONSHOTAI__KIMI_K2_INSTRUCT_0905 = Model(
        id="moonshotai/kimi-k2-instruct-0905",
        name="Kimi K2 Instruct 0905",
        api="openai-completions",
        provider="groq",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=1,
            output=3,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_120B = Model(
        id="openai/gpt-oss-120b",
        name="GPT OSS 120B",
        api="openai-completions",
        provider="groq",
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
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_20B = Model(
        id="openai/gpt-oss-20b",
        name="GPT OSS 20B",
        api="openai-completions",
        provider="groq",
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
            input=0.075,
            output=0.3,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPENAI__GPT_OSS_SAFEGUARD_20B = Model(
        id="openai/gpt-oss-safeguard-20b",
        name="Safety GPT OSS 20B",
        api="openai-completions",
        provider="groq",
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
            input=0.075,
            output=0.3,
            cache_read=0.037,
            cache_write=0,
        ),
    )

    QWEN_QWQ_32B = Model(
        id="qwen-qwq-32b",
        name="Qwen QwQ 32B",
        api="openai-completions",
        provider="groq",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.29,
            output=0.39,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN__QWEN3_32B = Model(
        id="qwen/qwen3-32b",
        name="Qwen3 32B",
        api="openai-completions",
        provider="groq",
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
            max_output_tokens=40960,
        ),
        pricing=ModelPricing(
            input=0.29,
            output=0.59,
            cache_read=0,
            cache_write=0,
        ),
    )
