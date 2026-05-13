"""Auto-generated models for cerebras.

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


class Cerebras:
    """Models for cerebras."""

    GPT_OSS_120B = Model(
        id="gpt-oss-120b",
        name="GPT OSS 120B",
        api="openai-completions",
        provider="cerebras",
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
            input=0.25,
            output=0.69,
            cache_read=0,
            cache_write=0,
        ),
    )

    LLAMA3_1_8B = Model(
        id="llama3.1-8b",
        name="Llama 3.1 8B",
        api="openai-completions",
        provider="cerebras",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=32000,
            max_output_tokens=8000,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.1,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN_3_235B_A22B_INSTRUCT_2507 = Model(
        id="qwen-3-235b-a22b-instruct-2507",
        name="Qwen 3 235B Instruct",
        api="openai-completions",
        provider="cerebras",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=131000,
            max_output_tokens=32000,
        ),
        pricing=ModelPricing(
            input=0.6,
            output=1.2,
            cache_read=0,
            cache_write=0,
        ),
    )

    ZAI_GLM_4_7 = Model(
        id="zai-glm-4.7",
        name="Z.AI GLM-4.7",
        api="openai-completions",
        provider="cerebras",
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
            max_output_tokens=40000,
        ),
        pricing=ModelPricing(
            input=2.25,
            output=2.75,
            cache_read=0,
            cache_write=0,
        ),
    )
