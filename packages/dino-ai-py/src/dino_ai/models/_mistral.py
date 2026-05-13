"""Auto-generated models for mistral.

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


class Mistral:
    """Models for mistral."""

    CODESTRAL_LATEST = Model(
        id="codestral-latest",
        name="Codestral (latest)",
        api="mistral-conversations",
        provider="mistral",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=256000,
            max_output_tokens=4096,
        ),
        pricing=ModelPricing(
            input=0.3,
            output=0.9,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEVSTRAL_2512 = Model(
        id="devstral-2512",
        name="Devstral 2",
        api="mistral-conversations",
        provider="mistral",
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
            input=0.4,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEVSTRAL_MEDIUM_2507 = Model(
        id="devstral-medium-2507",
        name="Devstral Medium",
        api="mistral-conversations",
        provider="mistral",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEVSTRAL_MEDIUM_LATEST = Model(
        id="devstral-medium-latest",
        name="Devstral 2 (latest)",
        api="mistral-conversations",
        provider="mistral",
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
            input=0.4,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEVSTRAL_SMALL_2505 = Model(
        id="devstral-small-2505",
        name="Devstral Small 2505",
        api="mistral-conversations",
        provider="mistral",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.3,
            cache_read=0,
            cache_write=0,
        ),
    )

    DEVSTRAL_SMALL_2507 = Model(
        id="devstral-small-2507",
        name="Devstral Small",
        api="mistral-conversations",
        provider="mistral",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.3,
            cache_read=0,
            cache_write=0,
        ),
    )

    LABS_DEVSTRAL_SMALL_2512 = Model(
        id="labs-devstral-small-2512",
        name="Devstral Small 2",
        api="mistral-conversations",
        provider="mistral",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
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

    MAGISTRAL_MEDIUM_LATEST = Model(
        id="magistral-medium-latest",
        name="Magistral Medium (latest)",
        api="mistral-conversations",
        provider="mistral",
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
            context_window=128000,
            max_output_tokens=16384,
        ),
        pricing=ModelPricing(
            input=2,
            output=5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MAGISTRAL_SMALL = Model(
        id="magistral-small",
        name="Magistral Small",
        api="mistral-conversations",
        provider="mistral",
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
            context_window=128000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=1.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINISTRAL_3B_LATEST = Model(
        id="ministral-3b-latest",
        name="Ministral 3B (latest)",
        api="mistral-conversations",
        provider="mistral",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.04,
            output=0.04,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINISTRAL_8B_LATEST = Model(
        id="ministral-8b-latest",
        name="Ministral 8B (latest)",
        api="mistral-conversations",
        provider="mistral",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.1,
            output=0.1,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_LARGE_2411 = Model(
        id="mistral-large-2411",
        name="Mistral Large 2.1",
        api="mistral-conversations",
        provider="mistral",
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
            input=2,
            output=6,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_LARGE_2512 = Model(
        id="mistral-large-2512",
        name="Mistral Large 3",
        api="mistral-conversations",
        provider="mistral",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=1.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_LARGE_LATEST = Model(
        id="mistral-large-latest",
        name="Mistral Large (latest)",
        api="mistral-conversations",
        provider="mistral",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0.5,
            output=1.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_MEDIUM_2505 = Model(
        id="mistral-medium-2505",
        name="Mistral Medium 3",
        api="mistral-conversations",
        provider="mistral",
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
            max_output_tokens=131072,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_MEDIUM_2508 = Model(
        id="mistral-medium-2508",
        name="Mistral Medium 3.1",
        api="mistral-conversations",
        provider="mistral",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262144,
            max_output_tokens=262144,
        ),
        pricing=ModelPricing(
            input=0.4,
            output=2,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_MEDIUM_2604 = Model(
        id="mistral-medium-2604",
        name="Mistral Medium 3.5",
        api="mistral-conversations",
        provider="mistral",
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
            input=1.5,
            output=7.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_MEDIUM_LATEST = Model(
        id="mistral-medium-latest",
        name="Mistral Medium (latest)",
        api="mistral-conversations",
        provider="mistral",
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
            input=1.5,
            output=7.5,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_NEMO = Model(
        id="mistral-nemo",
        name="Mistral Nemo",
        api="mistral-conversations",
        provider="mistral",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.15,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_SMALL_2506 = Model(
        id="mistral-small-2506",
        name="Mistral Small 3.2",
        api="mistral-conversations",
        provider="mistral",
        base_url="",
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
            input=0.1,
            output=0.3,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_SMALL_2603 = Model(
        id="mistral-small-2603",
        name="Mistral Small 4",
        api="mistral-conversations",
        provider="mistral",
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
            max_output_tokens=256000,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    MISTRAL_SMALL_LATEST = Model(
        id="mistral-small-latest",
        name="Mistral Small (latest)",
        api="mistral-conversations",
        provider="mistral",
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
            max_output_tokens=256000,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.6,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPEN_MISTRAL_7B = Model(
        id="open-mistral-7b",
        name="Mistral 7B",
        api="mistral-conversations",
        provider="mistral",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=8000,
            max_output_tokens=8000,
        ),
        pricing=ModelPricing(
            input=0.25,
            output=0.25,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPEN_MIXTRAL_8X22B = Model(
        id="open-mixtral-8x22b",
        name="Mixtral 8x22B",
        api="mistral-conversations",
        provider="mistral",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=64000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=2,
            output=6,
            cache_read=0,
            cache_write=0,
        ),
    )

    OPEN_MIXTRAL_8X7B = Model(
        id="open-mixtral-8x7b",
        name="Mixtral 8x7B",
        api="mistral-conversations",
        provider="mistral",
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
            max_output_tokens=32000,
        ),
        pricing=ModelPricing(
            input=0.7,
            output=0.7,
            cache_read=0,
            cache_write=0,
        ),
    )

    PIXTRAL_12B = Model(
        id="pixtral-12b",
        name="Pixtral 12B",
        api="mistral-conversations",
        provider="mistral",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.15,
            output=0.15,
            cache_read=0,
            cache_write=0,
        ),
    )

    PIXTRAL_LARGE_LATEST = Model(
        id="pixtral-large-latest",
        name="Pixtral Large (latest)",
        api="mistral-conversations",
        provider="mistral",
        base_url="",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=128000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=2,
            output=6,
            cache_read=0,
            cache_write=0,
        ),
    )
