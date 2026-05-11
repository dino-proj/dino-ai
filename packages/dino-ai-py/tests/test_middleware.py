"""Tests for middleware pipeline."""

from __future__ import annotations

import pytest

from dino_ai.catalog import ModelCatalog
from dino_ai.client import DinoClient
from dino_ai.context import Context
from dino_ai.middleware import MiddlewareChain
from dino_ai.model import Model
from dino_ai.options import StreamOptions
from dino_ai.providers.faux import FauxProvider, faux_model
from dino_ai.stream import EventStream


class CallCountMiddleware:
    """Tracks how many times intercept() was called."""

    def __init__(self) -> None:
        self.count = 0

    def intercept(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None,
        chain: MiddlewareChain,
    ) -> EventStream:
        self.count += 1
        return chain(model, context, options)


class OptionInjectMiddleware:
    """Injects a header into options."""

    def __init__(self, key: str, value: str) -> None:
        self._key = key
        self._value = value
        self.last_options: StreamOptions | None = None

    def intercept(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None,
        chain: MiddlewareChain,
    ) -> EventStream:
        self.last_options = options
        return chain(model, context, options)


@pytest.mark.asyncio
async def test_middleware_is_called():
    provider = FauxProvider(responses=["ok"])
    mw = CallCountMiddleware()
    catalog = ModelCatalog()
    catalog.register(faux_model())
    client = DinoClient(providers=[provider], middleware=[mw], catalog=catalog)

    ctx = Context(messages=[])
    await client.complete("faux-1", ctx)
    assert mw.count == 1


@pytest.mark.asyncio
async def test_middleware_chain_order():
    """Middleware should execute in order: first added = outermost."""
    order: list[str] = []

    class OrderMiddleware:
        def __init__(self, name: str) -> None:
            self._name = name

        def intercept(
            self, model: Model, context: Context, options: StreamOptions | None, chain: MiddlewareChain
        ) -> EventStream:
            order.append(f"{self._name}:before")
            result = chain(model, context, options)
            order.append(f"{self._name}:after")
            return result

    provider = FauxProvider(responses=["ok"])
    catalog = ModelCatalog()
    catalog.register(faux_model())
    client = DinoClient(
        providers=[provider],
        middleware=[OrderMiddleware("A"), OrderMiddleware("B")],
        catalog=catalog,
    )

    ctx = Context(messages=[])
    await client.complete("faux-1", ctx)
    assert order == ["A:before", "B:before", "B:after", "A:after"]


@pytest.mark.asyncio
async def test_no_middleware():
    """Client without middleware should still work."""
    provider = FauxProvider(responses=["direct"])
    catalog = ModelCatalog()
    catalog.register(faux_model())
    client = DinoClient(providers=[provider], catalog=catalog)

    ctx = Context(messages=[])
    msg = await client.complete("faux-1", ctx)
    assert msg.content[0].text == "direct"
