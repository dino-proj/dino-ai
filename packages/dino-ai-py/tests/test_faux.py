"""Tests for FauxProvider features."""

from __future__ import annotations

import pytest

from dino_ai.context import AssistantMessage, Context, UserMessage
from dino_ai.events import StreamDone
from dino_ai.providers.faux import (
    FAUX_API,
    FAUX_PROVIDER,
    FauxProvider,
    faux_model,
    faux_text,
    faux_thinking,
)
from dino_ai.usage import Usage


@pytest.mark.asyncio
async def test_string_response():
    provider = FauxProvider(responses=["Hello"])
    model = faux_model()
    ctx = Context(messages=[UserMessage(content="Hi")])

    done = None
    async for event in provider.stream(model, ctx):
        if isinstance(event, StreamDone):
            done = event

    assert done is not None
    assert done.message.content[0].text == "Hello"


@pytest.mark.asyncio
async def test_content_block_response():
    provider = FauxProvider(responses=[[faux_text("A"), faux_thinking("hmm"), faux_text("B")]])
    model = faux_model()
    ctx = Context(messages=[UserMessage(content="test")])

    done = None
    async for event in provider.stream(model, ctx):
        if isinstance(event, StreamDone):
            done = event

    assert done is not None
    assert len(done.message.content) == 3


@pytest.mark.asyncio
async def test_factory_response():
    def factory(context, options, call_count, model):
        return AssistantMessage(
            content=[faux_text(f"Call #{call_count}")],
            model=model.id,
            provider=FAUX_PROVIDER,
            api=FAUX_API,
            usage=Usage(),
        )

    provider = FauxProvider(responses=[factory, factory])
    model = faux_model()
    ctx = Context(messages=[UserMessage(content="test")])

    done1 = None
    async for event in provider.stream(model, ctx):
        if isinstance(event, StreamDone):
            done1 = event

    done2 = None
    async for event in provider.stream(model, ctx):
        if isinstance(event, StreamDone):
            done2 = event

    assert done1 is not None
    assert done1.message.content[0].text == "Call #0"
    assert done2 is not None
    assert done2.message.content[0].text == "Call #1"


@pytest.mark.asyncio
async def test_call_count():
    provider = FauxProvider(responses=["a", "b", "c"])
    model = faux_model()
    ctx = Context(messages=[])

    assert provider.call_count == 0
    async for _ in provider.stream(model, ctx):
        pass
    assert provider.call_count == 1
    async for _ in provider.stream(model, ctx):
        pass
    assert provider.call_count == 2


@pytest.mark.asyncio
async def test_append_responses():
    provider = FauxProvider(responses=["first"])
    provider.append_responses(["second"])
    model = faux_model()
    ctx = Context(messages=[])

    done1 = None
    async for event in provider.stream(model, ctx):
        if isinstance(event, StreamDone):
            done1 = event

    done2 = None
    async for event in provider.stream(model, ctx):
        if isinstance(event, StreamDone):
            done2 = event

    assert done1 is not None
    assert done1.message.content[0].text == "first"
    assert done2 is not None
    assert done2.message.content[0].text == "second"
