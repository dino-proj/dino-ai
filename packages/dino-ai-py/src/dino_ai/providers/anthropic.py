"""Anthropic Messages API provider.

Uses raw httpx for HTTP/SSE. Supports thinking/reasoning, tool calling,
images, and all standard Anthropic features.

Usage::

    from dino_ai.providers.anthropic import AnthropicProvider

    provider = AnthropicProvider()
    client = DinoClient(providers=[provider])

    msg = await client.complete("claude-sonnet-4-20250514", context, StreamOptions(api_key="sk-ant-..."))
"""

from __future__ import annotations

import asyncio
import json
import os
import time
from typing import Any

from dino_ai._json import parse_streaming_json
from dino_ai.content import TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context
from dino_ai.error import DinoError, ErrorCategory
from dino_ai.events import (
    StreamDone,
    StreamError,
    StreamStart,
    TextDelta,
    TextEnd,
    TextStart,
    ThinkingDelta,
    ThinkingEnd,
    ThinkingStart,
    ToolCallDelta,
    ToolCallEnd,
    ToolCallStart,
)
from dino_ai.model import Model
from dino_ai.options import SimpleStreamOptions, StreamOptions
from dino_ai.providers.anthropic_messages import convert_messages, convert_system, convert_tools, map_stop_reason
from dino_ai.providers.anthropic_sse import parse_anthropic_sse
from dino_ai.stream import EventStream
from dino_ai.usage import Cost, Usage

API_ID = "anthropic-messages"

ANTHROPIC_VERSION = "2023-06-01"

# ── Usage parsing ────────────────────────────────────────────────


def _parse_usage(raw: dict[str, Any], model: Model, existing: Usage | None = None) -> Usage:
    """Parse Anthropic usage into Usage, merging with existing if provided."""
    base = existing or Usage()

    input_tokens = raw.get("input_tokens") or base.input_tokens
    output_tokens = raw.get("output_tokens") or base.output_tokens
    cache_read = raw.get("cache_read_input_tokens") or base.cache_read_tokens
    cache_write = raw.get("cache_creation_input_tokens") or base.cache_write_tokens
    total = input_tokens + output_tokens + cache_read + cache_write

    pricing = model.pricing
    cost = Cost(
        input=input_tokens * pricing.input / 1_000_000,
        output=output_tokens * pricing.output / 1_000_000,
        cache_read=cache_read * pricing.cache_read / 1_000_000,
        cache_write=cache_write * pricing.cache_write / 1_000_000,
    )
    cost = Cost(
        input=cost.input,
        output=cost.output,
        cache_read=cost.cache_read,
        cache_write=cost.cache_write,
        total=cost.input + cost.output + cost.cache_read + cost.cache_write,
    )

    return Usage(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cache_read_tokens=cache_read,
        cache_write_tokens=cache_write,
        total_tokens=total,
        cost=cost,
    )


# ── Error classification ─────────────────────────────────────────


def _classify_error(status: int, body: str, provider: str) -> DinoError:
    """Classify an Anthropic HTTP error response."""
    if status in (401, 403):
        category = ErrorCategory.AUTH_FAILURE
    elif status == 429:
        category = ErrorCategory.RATE_LIMITED
    elif status == 400:
        lower = body.lower()
        if "context" in lower or "token" in lower and "exceed" in lower:
            category = ErrorCategory.CONTEXT_OVERFLOW
        elif "content" in lower and "filter" in lower:
            category = ErrorCategory.CONTENT_FILTERED
        else:
            category = ErrorCategory.INVALID_REQUEST
    elif status == 404:
        category = ErrorCategory.MODEL_NOT_FOUND
    elif status == 529:
        category = ErrorCategory.RATE_LIMITED  # Anthropic overloaded
    elif status >= 500:
        category = ErrorCategory.SERVER_ERROR
    else:
        category = ErrorCategory.PROVIDER_ERROR

    retryable = status in (429, 500, 502, 503, 504, 529)

    message = f"HTTP {status}"
    try:
        data = json.loads(body)
        err = data.get("error", {})
        if isinstance(err, dict):
            message = err.get("message", message)
        elif isinstance(err, str):
            message = err
    except (json.JSONDecodeError, ValueError):
        if body:
            message = body[:500]

    return DinoError(
        category=category,
        provider=provider,
        message=message,
        retryable=retryable,
        status_code=status,
        raw=body[:2000] if body else None,
    )


# ── Request building ─────────────────────────────────────────────


def _build_params(
    model: Model,
    context: Context,
    options: StreamOptions | None,
) -> dict[str, Any]:
    """Build the JSON body for an Anthropic Messages request."""
    messages = convert_messages(model, context)

    params: dict[str, Any] = {
        "model": model.id,
        "messages": messages,
        "stream": True,
    }

    # System prompt
    system = convert_system(context)
    if system:
        params["system"] = system

    # Max tokens (required by Anthropic)
    max_tokens = model.limits.max_output_tokens or 8192
    if options and options.max_tokens:
        max_tokens = options.max_tokens
    params["max_tokens"] = max_tokens

    # Temperature
    if options and options.temperature is not None:
        params["temperature"] = options.temperature

    # Tools
    if context.tools:
        params["tools"] = convert_tools(context.tools)

    # Thinking/reasoning
    _apply_thinking_params(params, model, options)

    return params


def _apply_thinking_params(
    params: dict[str, Any],
    model: Model,
    options: StreamOptions | None,
) -> None:
    """Apply thinking/reasoning configuration."""
    if not model.capabilities.reasoning:
        return

    # Extract reasoning level from metadata if provided
    effort: str | None = None
    if options and options.metadata:
        effort = options.metadata.get("reasoning_effort")

    if effort:
        # Adaptive thinking with effort
        params["thinking"] = {"type": "enabled", "budget_tokens": _effort_to_budget(effort, model)}
    else:
        params["thinking"] = {"type": "disabled"}


def _effort_to_budget(effort: str, model: Model) -> int:
    """Map reasoning effort to thinking budget tokens."""
    max_output = model.limits.max_output_tokens or 16384
    budgets = {
        "minimal": max(1024, max_output // 16),
        "low": max(2048, max_output // 8),
        "medium": max(4096, max_output // 4),
        "high": max(8192, max_output // 2),
        "xhigh": max_output,
    }
    return budgets.get(effort, max(4096, max_output // 4))


# ── Streaming state machine ─────────────────────────────────────


class _ContentBlock:
    """Tracks a single content block being streamed."""

    def __init__(self, block_type: str, index: int, content_index: int) -> None:
        self.block_type = block_type
        self.index = index
        self.content_index = content_index
        self.text = ""
        self.thinking = ""
        self.signature = ""
        self.redacted = False
        # Tool call fields
        self.tool_id = ""
        self.tool_name = ""
        self.partial_json = ""


class _StreamState:
    """Mutable state tracker during Anthropic SSE streaming."""

    def __init__(self, output: AssistantMessage) -> None:
        self.output = output
        self.blocks_by_index: dict[int, _ContentBlock] = {}
        self.content_blocks: list[TextContent | ThinkingContent | ToolCall] = []
        self.saw_message_start = False
        self.saw_message_stop = False


def _process_event(
    event_type: str,
    data: dict[str, Any],
    state: _StreamState,
    stream: EventStream,
    model: Model,
) -> None:
    """Process a single Anthropic SSE event."""

    if event_type == "message_start":
        state.saw_message_start = True
        msg_data = data.get("message", {})
        if response_id := msg_data.get("id"):
            state.output.response_id = response_id
        if (resp_model := msg_data.get("model")) and resp_model != model.id:
            state.output.response_model = resp_model
        if usage := msg_data.get("usage"):
            state.output.usage = _parse_usage(usage, model, state.output.usage)
        stream.push(StreamStart(partial=state.output))

    elif event_type == "content_block_start":
        _handle_block_start(data, state, stream)

    elif event_type == "content_block_delta":
        _handle_block_delta(data, state, stream, model)

    elif event_type == "content_block_stop":
        _handle_block_stop(data, state, stream)

    elif event_type == "message_delta":
        delta = data.get("delta", {})
        if stop_reason := delta.get("stop_reason"):
            state.output.stop_reason = map_stop_reason(stop_reason)
        if usage := data.get("usage"):
            state.output.usage = _parse_usage(usage, model, state.output.usage)

    elif event_type == "message_stop":
        state.saw_message_stop = True

    elif event_type == "error":
        raw = data.get("raw", "")
        error_msg = raw if isinstance(raw, str) else json.dumps(data)
        raise RuntimeError(f"Anthropic SSE error: {error_msg}")


def _handle_block_start(data: dict[str, Any], state: _StreamState, stream: EventStream) -> None:
    """Handle content_block_start event."""
    index = data.get("index", 0)
    cb = data.get("content_block", {})
    block_type = cb.get("type", "text")

    content_index = len(state.content_blocks)
    block = _ContentBlock(block_type, index, content_index)

    if block_type == "text":
        block.text = cb.get("text", "")
        text_block = TextContent(text=block.text)
        state.content_blocks.append(text_block)
        state.output.content = list(state.content_blocks)
        stream.push(TextStart(content_index=content_index, partial=state.output))

    elif block_type == "thinking":
        block.thinking = cb.get("thinking", "")
        think_block = ThinkingContent(thinking=block.thinking)
        state.content_blocks.append(think_block)
        state.output.content = list(state.content_blocks)
        stream.push(ThinkingStart(content_index=content_index, partial=state.output))

    elif block_type == "redacted_thinking":
        block.redacted = True
        block.signature = cb.get("data", "")
        redacted_block = ThinkingContent(thinking="[Reasoning redacted]", signature=block.signature, redacted=True)
        state.content_blocks.append(redacted_block)
        state.output.content = list(state.content_blocks)
        stream.push(ThinkingStart(content_index=content_index, partial=state.output))

    elif block_type == "tool_use":
        block.tool_id = cb.get("id", "")
        block.tool_name = cb.get("name", "")
        tc_block = ToolCall(id=block.tool_id, name=block.tool_name, arguments={})
        state.content_blocks.append(tc_block)
        state.output.content = list(state.content_blocks)
        stream.push(ToolCallStart(content_index=content_index, partial=state.output))

    state.blocks_by_index[index] = block


def _handle_block_delta(
    data: dict[str, Any],
    state: _StreamState,
    stream: EventStream,
    model: Model,
) -> None:
    """Handle content_block_delta event."""
    index = data.get("index", 0)
    block = state.blocks_by_index.get(index)
    if block is None:
        return

    delta = data.get("delta", {})
    delta_type = delta.get("type", "")
    ci = block.content_index

    if delta_type == "text_delta":
        text = delta.get("text", "")
        block.text += text
        entry: TextContent | ThinkingContent | ToolCall = TextContent(text=block.text)
        state.content_blocks[ci] = entry
        state.output.content = list(state.content_blocks)
        stream.push(TextDelta(content_index=ci, delta=text, partial=state.output))

    elif delta_type == "thinking_delta":
        thinking = delta.get("thinking", "")
        block.thinking += thinking
        entry = ThinkingContent(thinking=block.thinking, signature=block.signature or None)
        state.content_blocks[ci] = entry
        state.output.content = list(state.content_blocks)
        stream.push(ThinkingDelta(content_index=ci, delta=thinking, partial=state.output))

    elif delta_type == "signature_delta":
        sig = delta.get("signature", "")
        block.signature += sig
        entry = ThinkingContent(thinking=block.thinking, signature=block.signature)
        state.content_blocks[ci] = entry
        state.output.content = list(state.content_blocks)

    elif delta_type == "input_json_delta":
        partial = delta.get("partial_json", "")
        block.partial_json += partial
        parsed = parse_streaming_json(block.partial_json)
        entry = ToolCall(id=block.tool_id, name=block.tool_name, arguments=parsed)
        state.content_blocks[ci] = entry
        state.output.content = list(state.content_blocks)
        stream.push(ToolCallDelta(content_index=ci, delta=partial, partial=state.output))


def _handle_block_stop(data: dict[str, Any], state: _StreamState, stream: EventStream) -> None:
    """Handle content_block_stop event — finalize the block."""
    index = data.get("index", 0)
    block = state.blocks_by_index.get(index)
    if block is None:
        return

    ci = block.content_index

    if block.block_type == "text":
        entry: TextContent | ThinkingContent | ToolCall = TextContent(text=block.text)
        state.content_blocks[ci] = entry
        state.output.content = list(state.content_blocks)
        stream.push(TextEnd(content_index=ci, text=block.text, partial=state.output))

    elif block.block_type in ("thinking", "redacted_thinking"):
        entry = ThinkingContent(
            thinking=block.thinking,
            signature=block.signature or None,
            redacted=block.redacted,
        )
        state.content_blocks[ci] = entry
        state.output.content = list(state.content_blocks)
        stream.push(ThinkingEnd(content_index=ci, text=block.thinking, partial=state.output))

    elif block.block_type == "tool_use":
        # Final parse of accumulated JSON
        arguments = parse_streaming_json(block.partial_json)
        entry = ToolCall(id=block.tool_id, name=block.tool_name, arguments=arguments)
        state.content_blocks[ci] = entry
        state.output.content = list(state.content_blocks)
        stream.push(ToolCallEnd(content_index=ci, tool_call=entry, partial=state.output))


# ── Provider class ───────────────────────────────────────────────


def _get_api_key(model: Model, options: StreamOptions | None) -> str:
    """Resolve API key from options or environment."""
    if options and options.api_key:
        return options.api_key

    provider_upper = model.provider.upper().replace("-", "_")
    env_vars = [
        f"{provider_upper}_API_KEY",
        "ANTHROPIC_API_KEY",
    ]
    for var in env_vars:
        val = os.environ.get(var)
        if val:
            return val

    return ""


class AnthropicProvider:
    """Provider for Anthropic Messages API.

    Uses raw httpx for HTTP to keep dino-ai zero-dependency.
    Install httpx separately: ``pip install httpx``
    """

    @property
    def api(self) -> str:
        return API_ID

    def stream(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None = None,
    ) -> EventStream:
        """Stream a response from the Anthropic Messages API."""
        api_key = _get_api_key(model, options)
        event_stream = EventStream()

        async def _run() -> None:
            output = AssistantMessage(
                model=model.id,
                provider=model.provider,
                api=API_ID,
                usage=Usage(),
                stop_reason="stop",
                timestamp=int(time.time() * 1000),
            )
            state = _StreamState(output)

            try:
                import httpx

                params = _build_params(model, context, options)

                # Payload hook
                if options and options.on_payload:
                    hook_result: Any = options.on_payload(params, model)
                    if asyncio.iscoroutine(hook_result):
                        hook_result = await hook_result
                    if hook_result is not None:
                        params = hook_result

                headers: dict[str, str] = {
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream",
                    "anthropic-version": ANTHROPIC_VERSION,
                }
                if api_key:
                    headers["x-api-key"] = api_key
                if options and options.headers:
                    headers.update(options.headers)

                timeout = httpx.Timeout(
                    connect=30.0,
                    read=300.0,
                    write=30.0,
                    pool=30.0,
                )
                if options and options.timeout_ms:
                    total_s = options.timeout_ms / 1000.0
                    timeout = httpx.Timeout(total_s)

                base_url = model.base_url.rstrip("/")
                url = f"{base_url}/messages"

                async with httpx.AsyncClient(timeout=timeout) as client, client.stream(
                    "POST",
                    url,
                    json=params,
                    headers=headers,
                ) as response:
                    # Response hook
                    if options and options.on_response:
                        resp_headers = dict(response.headers)
                        hook_result = options.on_response(response.status_code, resp_headers, model)
                        if asyncio.iscoroutine(hook_result):
                            await hook_result

                    if response.status_code != 200:
                        body = await response.aread()
                        body_text = body.decode("utf-8", errors="replace")
                        error = _classify_error(response.status_code, body_text, model.provider)
                        output.stop_reason = "error"
                        output.error = error
                        event_stream.push(StreamError(reason="error", error=error, message=output))
                        event_stream.push(StreamDone(reason="error", message=output))
                        return

                    async for event_type, event_data in parse_anthropic_sse(response.aiter_bytes()):
                        _process_event(event_type, event_data, state, event_stream, model)

                # Verify stream completeness
                if state.saw_message_start and not state.saw_message_stop:
                    raise RuntimeError("Anthropic stream ended before message_stop")

                output.content = list(state.content_blocks)
                event_stream.push(StreamDone(reason=output.stop_reason, message=output))

            except ImportError:
                error = DinoError(
                    category=ErrorCategory.PROVIDER_ERROR,
                    provider=model.provider,
                    message="httpx is required for Anthropic provider. Install with: pip install httpx",
                )
                output.stop_reason = "error"
                output.error = error
                event_stream.push(StreamError(reason="error", error=error, message=output))
                event_stream.push(StreamDone(reason="error", message=output))

            except Exception as exc:
                category = ErrorCategory.NETWORK_ERROR if "connect" in str(exc).lower() else ErrorCategory.UNKNOWN
                error = DinoError(
                    category=category,
                    provider=model.provider,
                    message=str(exc),
                    retryable=True,
                )
                output.stop_reason = "error"
                output.error = error
                event_stream.push(StreamError(reason="error", error=error, message=output))
                event_stream.push(StreamDone(reason="error", message=output))

        asyncio.get_event_loop().create_task(_run())
        return event_stream

    def stream_simple(
        self,
        model: Model,
        context: Context,
        options: SimpleStreamOptions | None = None,
    ) -> EventStream:
        """Stream with unified reasoning level mapping."""
        if not options:
            return self.stream(model, context)

        stream_opts = StreamOptions(
            temperature=options.temperature,
            max_tokens=options.max_tokens,
            api_key=options.api_key,
            cache_retention=options.cache_retention,
            session_id=options.session_id,
            headers=options.headers,
            timeout_ms=options.timeout_ms,
            max_retries=options.max_retries,
            metadata={**(options.metadata or {}), "reasoning_effort": options.reasoning.value}
            if options.reasoning
            else options.metadata,
            on_payload=options.on_payload,
            on_response=options.on_response,
        )
        return self.stream(model, context, stream_opts)
