"""Tests for ModelCatalog."""

from __future__ import annotations

from dino_ai.catalog import ModelCatalog
from dino_ai.model import Model, ModelCapabilities, ModelLimits, ModelPricing


def test_builtins_loaded():
    catalog = ModelCatalog.with_builtins()
    assert len(catalog.list_models()) > 0


def test_get_known_model():
    catalog = ModelCatalog.with_builtins()
    model = catalog.get("gpt-4o")
    assert model is not None
    assert model.provider == "openai"
    assert model.api == "openai-completions"


def test_get_unknown_returns_none():
    catalog = ModelCatalog.with_builtins()
    assert catalog.get("nonexistent-model-xyz") is None


def test_register_custom_model():
    catalog = ModelCatalog()
    m = Model(
        id="my-model",
        name="My Model",
        api="custom",
        provider="custom-provider",
        base_url="http://localhost:8080",
        capabilities=ModelCapabilities(),
        limits=ModelLimits(),
        pricing=ModelPricing(),
    )
    catalog.register(m)
    assert catalog.get("my-model") is m


def test_register_overrides():
    catalog = ModelCatalog.with_builtins()
    original = catalog.get("gpt-4o")
    assert original is not None

    custom = Model(
        id="gpt-4o",
        name="Custom GPT-4o",
        api="custom",
        provider="custom",
        base_url="http://custom",
        capabilities=ModelCapabilities(),
        limits=ModelLimits(),
        pricing=ModelPricing(),
    )
    catalog.register(custom)
    assert catalog.get("gpt-4o") is custom


def test_list_models_by_provider():
    catalog = ModelCatalog.with_builtins()
    openai_models = catalog.list_models(provider="openai")
    assert len(openai_models) > 0
    assert all(m.provider == "openai" for m in openai_models)


def test_providers_list():
    catalog = ModelCatalog.with_builtins()
    providers = catalog.providers()
    assert "openai" in providers
    assert "anthropic" in providers
