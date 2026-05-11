"""Tests for Azure OpenAI provider — URL patterns, auth, and API version."""

from __future__ import annotations

import pytest

from dino_ai.model import Model, ModelCapabilities, ModelLimits, ModelPricing
from dino_ai.options import StreamOptions
from dino_ai.providers.azure_openai import (
    DEFAULT_API_VERSION,
    PROFILE_AZURE,
    AzureOpenAIProvider,
    _get_api_version,
    _get_azure_api_key,
)


def _model(
    model_id: str = "gpt-4o",
    provider: str = "azure",
) -> Model:
    return Model(
        id=model_id,
        name="GPT-4o (Azure)",
        api="openai-completions",
        provider=provider,
        base_url="https://my-resource.openai.azure.com",
        capabilities=ModelCapabilities(reasoning=False, vision=True),
        limits=ModelLimits(context_window=128000, max_output_tokens=16384),
        pricing=ModelPricing(input=2.5, output=10.0),
    )


class TestAzureApiKey:
    def test_from_options(self):
        m = _model()
        key = _get_azure_api_key(m, StreamOptions(api_key="opt-key"))
        assert key == "opt-key"

    def test_from_env(self, monkeypatch: pytest.MonkeyPatch):
        m = _model()
        monkeypatch.setenv("AZURE_OPENAI_API_KEY", "env-key")
        key = _get_azure_api_key(m, None)
        assert key == "env-key"

    def test_fallback_env(self, monkeypatch: pytest.MonkeyPatch):
        m = _model()
        monkeypatch.delenv("AZURE_OPENAI_API_KEY", raising=False)
        monkeypatch.setenv("AZURE_API_KEY", "fallback-key")
        key = _get_azure_api_key(m, None)
        assert key == "fallback-key"

    def test_no_key(self, monkeypatch: pytest.MonkeyPatch):
        m = _model()
        monkeypatch.delenv("AZURE_OPENAI_API_KEY", raising=False)
        monkeypatch.delenv("AZURE_API_KEY", raising=False)
        key = _get_azure_api_key(m, None)
        assert key == ""


class TestAzureApiVersion:
    def test_from_metadata(self):
        m = _model()
        opts = StreamOptions(metadata={"api_version": "2024-06-01"})
        assert _get_api_version(m, opts) == "2024-06-01"

    def test_from_env(self, monkeypatch: pytest.MonkeyPatch):
        m = _model()
        monkeypatch.setenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
        assert _get_api_version(m, None) == "2024-08-01-preview"

    def test_default(self, monkeypatch: pytest.MonkeyPatch):
        m = _model()
        monkeypatch.delenv("AZURE_OPENAI_API_VERSION", raising=False)
        assert _get_api_version(m, None) == DEFAULT_API_VERSION


class TestAzureProfile:
    def test_uses_developer_role(self):
        assert PROFILE_AZURE.use_developer_role is True

    def test_uses_max_completion_tokens(self):
        assert PROFILE_AZURE.max_tokens_field == "max_completion_tokens"

    def test_supports_reasoning(self):
        assert PROFILE_AZURE.thinking_format == "openai"
        assert PROFILE_AZURE.supports_reasoning_effort is True

    def test_no_store(self):
        assert PROFILE_AZURE.supports_store is False


class TestAzureProvider:
    def test_api_id(self):
        provider = AzureOpenAIProvider()
        assert provider.api == "openai-completions"

    def test_custom_api_version(self):
        provider = AzureOpenAIProvider(api_version="2024-01-01")
        assert provider._api_version == "2024-01-01"
