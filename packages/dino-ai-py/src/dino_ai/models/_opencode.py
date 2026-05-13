"""Auto-generated models for opencode.

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


class Opencode:
    """Models for opencode."""

    BIG_PICKLE = Model(
        id="big-pickle",
        name="Big Pickle",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    CLAUDE_3_5_HAIKU = Model(
        id="claude-3-5-haiku",
        name="Claude Haiku 3.5",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=True,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=200000,
            max_output_tokens=8192,
        ),
        pricing=ModelPricing(
            input=0.8,
            output=4,
            cache_read=0.08,
            cache_write=1,
        ),
    )

    CLAUDE_HAIKU_4_5 = Model(
        id="claude-haiku-4-5",
        name="Claude Haiku 4.5",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=1,
            output=5,
            cache_read=0.1,
            cache_write=1.25,
        ),
    )

    CLAUDE_OPUS_4_1 = Model(
        id="claude-opus-4-1",
        name="Claude Opus 4.1",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=200000,
            max_output_tokens=32000,
        ),
        pricing=ModelPricing(
            input=15,
            output=75,
            cache_read=1.5,
            cache_write=18.75,
        ),
    )

    CLAUDE_OPUS_4_5 = Model(
        id="claude-opus-4-5",
        name="Claude Opus 4.5",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=200000,
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=5,
            output=25,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_OPUS_4_6 = Model(
        id="claude-opus-4-6",
        name="Claude Opus 4.6",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=5,
            output=25,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_OPUS_4_7 = Model(
        id="claude-opus-4-7",
        name="Claude Opus 4.7",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=5,
            output=25,
            cache_read=0.5,
            cache_write=6.25,
        ),
    )

    CLAUDE_SONNET_4 = Model(
        id="claude-sonnet-4",
        name="Claude Sonnet 4",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_SONNET_4_5 = Model(
        id="claude-sonnet-4-5",
        name="Claude Sonnet 4.5",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    CLAUDE_SONNET_4_6 = Model(
        id="claude-sonnet-4-6",
        name="Claude Sonnet 4.6",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=3,
            output=15,
            cache_read=0.3,
            cache_write=3.75,
        ),
    )

    DEEPSEEK_V4_FLASH_FREE = Model(
        id="deepseek-v4-flash-free",
        name="DeepSeek V4 Flash Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    GEMINI_3_FLASH = Model(
        id="gemini-3-flash",
        name="Gemini 3 Flash",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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

    GEMINI_3_PRO = Model(
        id="gemini-3-pro",
        name="Gemini 3 Pro",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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

    GEMINI_3_1_PRO = Model(
        id="gemini-3.1-pro",
        name="Gemini 3.1 Pro Preview",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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

    GLM_4_6 = Model(
        id="glm-4.6",
        name="GLM-4.6",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0.6,
            output=2.2,
            cache_read=0.1,
            cache_write=0,
        ),
    )

    GLM_4_7 = Model(
        id="glm-4.7",
        name="GLM-4.7",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0.6,
            output=2.2,
            cache_read=0.1,
            cache_write=0,
        ),
    )

    GLM_4_7_FREE = Model(
        id="glm-4.7-free",
        name="GLM-4.7 Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    GLM_5 = Model(
        id="glm-5",
        name="GLM-5",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=1,
            output=3.2,
            cache_read=0.2,
            cache_write=0,
        ),
    )

    GLM_5_FREE = Model(
        id="glm-5-free",
        name="GLM-5 Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    GLM_5_1 = Model(
        id="glm-5.1",
        name="GLM-5.1",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=1.4,
            output=4.4,
            cache_read=0.26,
            cache_write=0,
        ),
    )

    GPT_5 = Model(
        id="gpt-5",
        name="GPT-5",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.07,
            output=8.5,
            cache_read=0.107,
            cache_write=0,
        ),
    )

    GPT_5_CODEX = Model(
        id="gpt-5-codex",
        name="GPT-5 Codex",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.07,
            output=8.5,
            cache_read=0.107,
            cache_write=0,
        ),
    )

    GPT_5_NANO = Model(
        id="gpt-5-nano",
        name="GPT-5 Nano",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.05,
            output=0.4,
            cache_read=0.005,
            cache_write=0,
        ),
    )

    GPT_5_1 = Model(
        id="gpt-5.1",
        name="GPT-5.1",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.07,
            output=8.5,
            cache_read=0.107,
            cache_write=0,
        ),
    )

    GPT_5_1_CODEX = Model(
        id="gpt-5.1-codex",
        name="GPT-5.1 Codex",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.07,
            output=8.5,
            cache_read=0.107,
            cache_write=0,
        ),
    )

    GPT_5_1_CODEX_MAX = Model(
        id="gpt-5.1-codex-max",
        name="GPT-5.1 Codex Max",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.25,
            output=10,
            cache_read=0.125,
            cache_write=0,
        ),
    )

    GPT_5_1_CODEX_MINI = Model(
        id="gpt-5.1-codex-mini",
        name="GPT-5.1 Codex Mini",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.25,
            output=2,
            cache_read=0.025,
            cache_write=0,
        ),
    )

    GPT_5_2 = Model(
        id="gpt-5.2",
        name="GPT-5.2",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.75,
            output=14,
            cache_read=0.175,
            cache_write=0,
        ),
    )

    GPT_5_2_CODEX = Model(
        id="gpt-5.2-codex",
        name="GPT-5.2 Codex",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.75,
            output=14,
            cache_read=0.175,
            cache_write=0,
        ),
    )

    GPT_5_3_CODEX = Model(
        id="gpt-5.3-codex",
        name="GPT-5.3 Codex",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=1.75,
            output=14,
            cache_read=0.175,
            cache_write=0,
        ),
    )

    GPT_5_3_CODEX_SPARK = Model(
        id="gpt-5.3-codex-spark",
        name="GPT-5.3 Codex Spark",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=1.75,
            output=14,
            cache_read=0.175,
            cache_write=0,
        ),
    )

    GPT_5_4 = Model(
        id="gpt-5.4",
        name="GPT-5.4",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=1050000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=2.5,
            output=15,
            cache_read=0.25,
            cache_write=0,
        ),
    )

    GPT_5_4_MINI = Model(
        id="gpt-5.4-mini",
        name="GPT-5.4 Mini",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.75,
            output=4.5,
            cache_read=0.075,
            cache_write=0,
        ),
    )

    GPT_5_4_NANO = Model(
        id="gpt-5.4-nano",
        name="GPT-5.4 Nano",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=400000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0.2,
            output=1.25,
            cache_read=0.02,
            cache_write=0,
        ),
    )

    GPT_5_4_PRO = Model(
        id="gpt-5.4-pro",
        name="GPT-5.4 Pro",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=1050000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=30,
            output=180,
            cache_read=30,
            cache_write=0,
        ),
    )

    GPT_5_5 = Model(
        id="gpt-5.5",
        name="GPT-5.5",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=1050000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=5,
            output=30,
            cache_read=0.5,
            cache_write=0,
        ),
    )

    GPT_5_5_PRO = Model(
        id="gpt-5.5-pro",
        name="GPT-5.5 Pro",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=1050000,
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=30,
            output=180,
            cache_read=30,
            cache_write=0,
        ),
    )

    GROK_CODE = Model(
        id="grok-code",
        name="Grok Code Fast 1",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    HY3_PREVIEW_FREE = Model(
        id="hy3-preview-free",
        name="Hy3 preview Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    KIMI_K2 = Model(
        id="kimi-k2",
        name="Kimi K2",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            output=2.5,
            cache_read=0.4,
            cache_write=0,
        ),
    )

    KIMI_K2_THINKING = Model(
        id="kimi-k2-thinking",
        name="Kimi K2 Thinking",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0.4,
            output=2.5,
            cache_read=0.4,
            cache_write=0,
        ),
    )

    KIMI_K2_5 = Model(
        id="kimi-k2.5",
        name="Kimi K2.5",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            cache_read=0.08,
            cache_write=0,
        ),
    )

    KIMI_K2_5_FREE = Model(
        id="kimi-k2.5-free",
        name="Kimi K2.5 Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    KIMI_K2_6 = Model(
        id="kimi-k2.6",
        name="Kimi K2.6",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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

    LING_2_6_FLASH_FREE = Model(
        id="ling-2.6-flash-free",
        name="Ling 2.6 Flash Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
        capabilities=ModelCapabilities(
            reasoning=False,
            vision=False,
            tool_calling=True,
            streaming=True,
            supported_thinking_levels=(),
        ),
        limits=ModelLimits(
            context_window=262100,
            max_output_tokens=32800,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MIMO_V2_FLASH_FREE = Model(
        id="mimo-v2-flash-free",
        name="MiMo V2 Flash Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MIMO_V2_OMNI_FREE = Model(
        id="mimo-v2-omni-free",
        name="MiMo V2 Omni Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MIMO_V2_PRO_FREE = Model(
        id="mimo-v2-pro-free",
        name="MiMo V2 Pro Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX_M2_1 = Model(
        id="minimax-m2.1",
        name="MiniMax M2.1",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            cache_read=0.1,
            cache_write=0,
        ),
    )

    MINIMAX_M2_1_FREE = Model(
        id="minimax-m2.1-free",
        name="MiniMax M2.1 Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX_M2_5 = Model(
        id="minimax-m2.5",
        name="MiniMax M2.5",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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

    MINIMAX_M2_5_FREE = Model(
        id="minimax-m2.5-free",
        name="MiniMax M2.5 Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    MINIMAX_M2_7 = Model(
        id="minimax-m2.7",
        name="MiniMax M2.7",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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

    NEMOTRON_3_SUPER_FREE = Model(
        id="nemotron-3-super-free",
        name="Nemotron 3 Super Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            max_output_tokens=128000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_CODER = Model(
        id="qwen3-coder",
        name="Qwen3 Coder",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            output=1.8,
            cache_read=0,
            cache_write=0,
        ),
    )

    QWEN3_5_PLUS = Model(
        id="qwen3.5-plus",
        name="Qwen3.5 Plus",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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

    QWEN3_6_PLUS_FREE = Model(
        id="qwen3.6-plus-free",
        name="Qwen3.6 Plus Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            max_output_tokens=64000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    RING_2_6_1T_FREE = Model(
        id="ring-2.6-1t-free",
        name="Ring 2.6 1T Free",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            context_window=262000,
            max_output_tokens=66000,
        ),
        pricing=ModelPricing(
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )

    TRINITY_LARGE_PREVIEW_FREE = Model(
        id="trinity-large-preview-free",
        name="Trinity Large Preview",
        api="openai-completions",
        provider="opencode",
        base_url="https://opencode.ai/zen/v1",
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
            input=0,
            output=0,
            cache_read=0,
            cache_write=0,
        ),
    )
