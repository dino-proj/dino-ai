"""Auto-generated models for cloudflare-workers-ai.

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


class CloudflareWorkersAi:
    """Models for cloudflare-workers-ai."""

    CF__GOOGLE__GEMMA_4_26B_A4B_IT = Model(
        id="@cf/google/gemma-4-26b-a4b-it",
        name="Gemma 4 26B A4B IT",
        api="openai-completions",
        provider="cloudflare-workers-ai",
        base_url="https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.3,
            cache_read=0,
            cache_write=0,
        ),
    )

    CF__META__LLAMA_4_SCOUT_17B_16E_INSTRUCT = Model(
        id="@cf/meta/llama-4-scout-17b-16e-instruct",
        name="Llama 4 Scout 17B 16E Instruct",
        api="openai-completions",
        provider="cloudflare-workers-ai",
        base_url="https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/v1",
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
            input=0.27,
            output=0.85,
            cache_read=0,
            cache_write=0,
        ),
    )

    CF__MOONSHOTAI__KIMI_K2_5 = Model(
        id="@cf/moonshotai/kimi-k2.5",
        name="Kimi K2.5",
        api="openai-completions",
        provider="cloudflare-workers-ai",
        base_url="https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/v1",
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

    CF__MOONSHOTAI__KIMI_K2_6 = Model(
        id="@cf/moonshotai/kimi-k2.6",
        name="Kimi K2.6",
        api="openai-completions",
        provider="cloudflare-workers-ai",
        base_url="https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/v1",
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
            input=0.95,
            output=4,
            cache_read=0.16,
            cache_write=0,
        ),
    )

    CF__NVIDIA__NEMOTRON_3_120B_A12B = Model(
        id="@cf/nvidia/nemotron-3-120b-a12b",
        name="Nemotron 3 Super 120B",
        api="openai-completions",
        provider="cloudflare-workers-ai",
        base_url="https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/v1",
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
            input=0.5,
            output=1.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    CF__OPENAI__GPT_OSS_120B = Model(
        id="@cf/openai/gpt-oss-120b",
        name="GPT OSS 120B",
        api="openai-completions",
        provider="cloudflare-workers-ai",
        base_url="https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.35,
            output=0.75,
            cache_read=0,
            cache_write=0,
        ),
    )

    CF__OPENAI__GPT_OSS_20B = Model(
        id="@cf/openai/gpt-oss-20b",
        name="GPT OSS 20B",
        api="openai-completions",
        provider="cloudflare-workers-ai",
        base_url="https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/v1",
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
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=0.3,
            cache_read=0,
            cache_write=0,
        ),
    )

    CF__ZAI_ORG__GLM_4_7_FLASH = Model(
        id="@cf/zai-org/glm-4.7-flash",
        name="GLM-4.7-Flash",
        api="openai-completions",
        provider="cloudflare-workers-ai",
        base_url="https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/v1",
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
            input=0.06,
            output=0.4,
            cache_read=0,
            cache_write=0,
        ),
    )
