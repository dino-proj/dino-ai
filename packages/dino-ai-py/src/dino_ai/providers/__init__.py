"""Provider adapter protocol — the interface all providers implement."""

from __future__ import annotations

from typing import Protocol

from dino_ai.context import Context
from dino_ai.model import Model
from dino_ai.options import SimpleStreamOptions, StreamOptions
from dino_ai.stream import EventStream


class ProviderAdapter(Protocol):
    """Protocol that all provider implementations must satisfy."""

    @property
    def api(self) -> str:
        """The API protocol identifier this provider handles."""
        ...

    def stream(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None = None,
    ) -> EventStream:
        """Stream a response with provider-specific options."""
        ...

    def stream_simple(
        self,
        model: Model,
        context: Context,
        options: SimpleStreamOptions | None = None,
    ) -> EventStream:
        """Stream a response with unified reasoning level options."""
        ...
