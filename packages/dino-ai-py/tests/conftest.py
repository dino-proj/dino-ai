"""Shared test fixtures for dino-ai."""

from __future__ import annotations

import pytest

from dino_ai.catalog import ModelCatalog
from dino_ai.client import DinoClient
from dino_ai.context import Context, UserMessage
from dino_ai.providers.faux import FauxProvider, faux_model


@pytest.fixture()
def faux_provider() -> FauxProvider:
    """A fresh FauxProvider with no responses."""
    return FauxProvider()


@pytest.fixture()
def model():
    """Default faux model."""
    return faux_model()


@pytest.fixture()
def client(faux_provider: FauxProvider) -> DinoClient:
    """DinoClient wired to the faux provider."""
    catalog = ModelCatalog()
    catalog.register(faux_model())
    return DinoClient(providers=[faux_provider], catalog=catalog)


@pytest.fixture()
def simple_context() -> Context:
    """Single-message context."""
    return Context(messages=[UserMessage(content="Hello")])
