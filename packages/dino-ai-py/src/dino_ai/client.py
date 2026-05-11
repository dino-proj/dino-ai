"""DinoClient — instance-scoped entry point for all LLM interactions."""

from __future__ import annotations

from dino_ai.catalog import ModelCatalog
from dino_ai.context import AssistantMessage, Context
from dino_ai.error import DinoException
from dino_ai.middleware import Middleware, MiddlewareChain, build_middleware_chain
from dino_ai.model import Model
from dino_ai.options import SimpleStreamOptions, StreamOptions
from dino_ai.providers import ProviderAdapter
from dino_ai.stream import EventStream


class DinoClient:
    """Main entry point. Holds providers, middleware, and model catalog.

    Usage::

        client = DinoClient(
            providers=[OpenAICompletionsProvider(), AnthropicProvider()],
            middleware=[LoggingMiddleware()],
        )

        # Use Model object directly
        stream = client.stream(model, context)

        # Or look up by model id string
        stream = client.stream("gpt-4o", context)

        # Await final result
        message = await client.complete("claude-sonnet-4-20250514", context)
    """

    def __init__(
        self,
        providers: list[ProviderAdapter] | None = None,
        middleware: list[Middleware] | None = None,
        catalog: ModelCatalog | None = None,
    ) -> None:
        self._providers: dict[str, ProviderAdapter] = {}
        self._middleware: list[Middleware] = middleware or []
        self._catalog = catalog or ModelCatalog.with_builtins()

        for provider in providers or []:
            self._providers[provider.api] = provider

    @property
    def catalog(self) -> ModelCatalog:
        """Access the model catalog for lookup and registration."""
        return self._catalog

    def _resolve_model(self, model: Model | str) -> Model:
        if isinstance(model, Model):
            return model
        resolved = self._catalog.get(model)
        if resolved is None:
            raise DinoException(f"Model not found in catalog: {model!r}")
        return resolved

    def _resolve_provider(self, api: str) -> ProviderAdapter:
        provider = self._providers.get(api)
        if provider is None:
            raise DinoException(f"No provider registered for api: {api}")
        return provider

    def _build_chain(self, provider: ProviderAdapter) -> MiddlewareChain:
        def terminal(
            model: Model,
            context: Context,
            options: StreamOptions | None = None,
        ) -> EventStream:
            return provider.stream(model, context, options)

        return build_middleware_chain(self._middleware, terminal)

    def stream(
        self,
        model: Model | str,
        context: Context,
        options: StreamOptions | None = None,
    ) -> EventStream:
        """Stream a response with provider-specific options, through the middleware pipeline."""
        resolved = self._resolve_model(model)
        provider = self._resolve_provider(resolved.api)
        chain = self._build_chain(provider)
        return chain(resolved, context, options)

    async def complete(
        self,
        model: Model | str,
        context: Context,
        options: StreamOptions | None = None,
    ) -> AssistantMessage:
        """Complete a request and return the final AssistantMessage."""
        s = self.stream(model, context, options)
        return await s.result()

    def stream_simple(
        self,
        model: Model | str,
        context: Context,
        options: SimpleStreamOptions | None = None,
    ) -> EventStream:
        """Stream with unified reasoning level, through the middleware pipeline."""
        resolved = self._resolve_model(model)
        provider = self._resolve_provider(resolved.api)

        def terminal(
            m: Model,
            c: Context,
            o: StreamOptions | None = None,
        ) -> EventStream:
            return provider.stream_simple(m, c, options)

        chain = build_middleware_chain(self._middleware, terminal)
        return chain(resolved, context, options)

    async def complete_simple(
        self,
        model: Model | str,
        context: Context,
        options: SimpleStreamOptions | None = None,
    ) -> AssistantMessage:
        """Complete with unified reasoning level."""
        s = self.stream_simple(model, context, options)
        return await s.result()
