"""Model catalog — in-memory registry backed by generated model constants."""

from __future__ import annotations

from dino_ai.model import Model


class ModelCatalog:
    """In-memory model registry with built-in + user-registered models.

    Usage::

        catalog = ModelCatalog.with_builtins()
        model = catalog.get("gpt-4o")

        # register custom model
        catalog.register(Model(...))
    """

    def __init__(self, models: list[Model] | None = None) -> None:
        self._models: dict[str, Model] = {}
        for m in models or []:
            self._models[m.id] = m

    @classmethod
    def with_builtins(cls) -> ModelCatalog:
        """Create a catalog pre-loaded with built-in models from generated constants."""
        from dino_ai.models import ALL_MODELS

        return cls(ALL_MODELS)

    def register(self, model: Model) -> None:
        """Register or override a model."""
        self._models[model.id] = model

    def get(self, model_id: str) -> Model | None:
        """Look up a model by ID."""
        return self._models.get(model_id)

    def list_models(self, provider: str | None = None) -> list[Model]:
        """List all models, optionally filtered by provider."""
        models = list(self._models.values())
        if provider is not None:
            models = [m for m in models if m.provider == provider]
        return models

    def providers(self) -> list[str]:
        """List distinct provider names."""
        return sorted({m.provider for m in self._models.values()})
