"""EventStream — async iterable that also exposes a final result as an awaitable."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator

from dino_ai.context import AssistantMessage
from dino_ai.events import AssistantMessageEvent, StreamDone, StreamError


class EventStream:
    """Async iterable of AssistantMessageEvent with a final result future.

    Usage::

        stream = provider.stream(model, context)

        # Option 1: iterate events
        async for event in stream:
            if event.type == "text_delta":
                print(event.delta, end="")

        # Option 2: await final result directly
        message = await stream.result()

    Providers push events via ``push()`` and signal completion via ``end()``.
    """

    def __init__(self) -> None:
        self._queue: asyncio.Queue[AssistantMessageEvent | None] = asyncio.Queue()
        self._result_future: asyncio.Future[AssistantMessage] = asyncio.get_event_loop().create_future()
        self._done = False

    @classmethod
    def create(cls) -> EventStream:
        """Factory that ensures an event loop is available."""
        loop = asyncio.get_event_loop()
        stream = cls.__new__(cls)
        stream._queue = asyncio.Queue()
        stream._result_future = loop.create_future()
        stream._done = False
        return stream

    def push(self, event: AssistantMessageEvent) -> None:
        """Push an event into the stream. Called by provider adapters."""
        if self._done:
            return

        if isinstance(event, (StreamDone, StreamError)):
            self._done = True
            if not self._result_future.done():
                self._result_future.set_result(event.message)

        self._queue.put_nowait(event)

        if self._done:
            self._queue.put_nowait(None)  # sentinel

    def end(self, message: AssistantMessage) -> None:
        """Signal completion without a terminal event (fallback)."""
        if self._done:
            return
        self._done = True
        if not self._result_future.done():
            self._result_future.set_result(message)
        self._queue.put_nowait(None)

    async def result(self) -> AssistantMessage:
        """Await the final AssistantMessage (consumes the stream if not already consumed)."""
        return await self._result_future

    def collect_available(self) -> list[AssistantMessageEvent]:
        """Drain all currently queued events without blocking.

        Useful in tests when events are pushed synchronously.
        """
        events: list[AssistantMessageEvent] = []
        while not self._queue.empty():
            item = self._queue.get_nowait()
            if item is None:
                break
            events.append(item)
        return events

    async def __aiter__(self) -> AsyncIterator[AssistantMessageEvent]:
        while True:
            item = await self._queue.get()
            if item is None:
                return
            yield item
