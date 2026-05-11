"""Middleware pipeline for composable request/response interception."""

from __future__ import annotations

from collections.abc import Callable
from typing import Protocol

from dino_ai.context import Context
from dino_ai.model import Model
from dino_ai.options import StreamOptions
from dino_ai.stream import EventStream

MiddlewareChain = Callable[["Model", "Context", "StreamOptions | None"], "EventStream"]


class Middleware(Protocol):
    """Interceptor that wraps a stream() call.

    Middleware can inspect/modify the request, delegate to the next
    middleware (or provider) via ``chain``, and post-process the event stream.
    """

    def intercept(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None,
        chain: MiddlewareChain,
    ) -> EventStream: ...


def build_middleware_chain(
    middlewares: list[Middleware],
    terminal: MiddlewareChain,
) -> MiddlewareChain:
    """Build a composed chain from a list of middlewares and a terminal handler.

    Execution order: middlewares[0] wraps middlewares[1] wraps ... wraps terminal.
    """
    chain = terminal
    for mw in reversed(middlewares):
        outer_chain = chain

        def make_handler(middleware: Middleware, next_chain: MiddlewareChain) -> MiddlewareChain:
            def handler(
                model: Model,
                context: Context,
                options: StreamOptions | None = None,
            ) -> EventStream:
                return middleware.intercept(model, context, options, next_chain)

            return handler

        chain = make_handler(mw, outer_chain)

    return chain
