"""OpenAI Chat Completions provider — works with OpenAI and all compatible APIs.

Uses raw httpx for HTTP/SSE to stay zero-dependency. Bring your own API key.

Usage::

    from dino_ai.providers.openai_completions import OpenAICompletionsProvider

    provider = OpenAICompletionsProvider()
    client = DinoClient(providers=[provider])

    msg = await client.complete("gpt-4o", context, StreamOptions(api_key="sk-..."))
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
from dino_ai.providers.openai_compat import OpenAICompatProfile, detect_profile
from dino_ai.providers.openai_messages import convert_messages, convert_tools, has_tool_history
from dino_ai.providers.openai_sse import parse_sse_stream
from dino_ai.stream import EventStream
from dino_ai.usage import Cost, Usage

API_ID = "openai-completions"

# ── Stop reason mapping ──────────────────────────────────────────


def _map_stop_reason(finish_reason: str | None) -> tuple[str, str | None]:
    """Map OpenAI finish_reason to (stop_reason, error_message)."""
    if finish_reason is None:
        return "stop", None
    r = finish_reason.lower()
    if r in ("stop", "end", "end_turn"):
        return "stop", None
    if r == "length":
        return "length", None
    if r in ("tool_calls", "function_call"):
        return "toolUse", None
    if r == "content_filter":
        return "error", "Content was filtered by the provider"
    if r == "network_error":
        return "error", "Network error from provider"
    return "stop", None


# ── Usage parsing ────────────────────────────────────────────────


def _parse_usage(raw: dict[str, Any], model: Model) -> Usage:
    """Parse OpenAI-style usage dict to Usage."""
    prompt = raw.get("prompt_tokens", 0) or 0
    completion = raw.get("completion_tokens", 0) or 0
    total = raw.get("total_tokens", 0) or prompt + completion

    # Cache tokens (prompt_tokens_details may exist)
    details = raw.get("prompt_tokens_details") or {}
    cache_read = details.get("cached_tokens", 0) or 0
    cache_write = 0

    # Some providers report cache_creation_input_tokens
    if "cache_creation_input_tokens" in raw:
        cache_write = raw["cache_creation_input_tokens"] or 0
    if "cache_read_input_tokens" in raw:
        cache_read = raw["cache_read_input_tokens"] or 0

    # Completion details may have reasoning tokens
    comp_details = raw.get("completion_tokens_details") or {}
    reasoning_tokens = comp_details.get("reasoning_tokens", 0) or 0
    _ = reasoning_tokens  # tracked but not used for cost yet

    pricing = model.pricing
    cost = Cost(
        input=prompt * pricing.input / 1_000_000,
        output=completion * pricing.output / 1_000_000,
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
        input_tokens=prompt,
        output_tokens=completion,
        cache_read_tokens=cache_read,
        cache_write_tokens=cache_write,
        total_tokens=total,
        cost=cost,
    )


# ── Error classification ─────────────────────────────────────────


def _classify_error(status: int, body: str, provider: str) -> DinoError:
    """Classify an HTTP error response into a structured DinoError."""
    if status == 401 or status == 403:
        category = ErrorCategory.AUTH_FAILURE
    elif status == 429:
        category = ErrorCategory.RATE_LIMITED
    elif status == 400:
        lower = body.lower()
        if "context" in lower and ("length" in lower or "overflow" in lower or "exceed" in lower):
            category = ErrorCategory.CONTEXT_OVERFLOW
        elif "content_filter" in lower or "content filter" in lower:
            category = ErrorCategory.CONTENT_FILTERED
        else:
            category = ErrorCategory.INVALID_REQUEST
    elif status == 404:
        category = ErrorCategory.MODEL_NOT_FOUND
    elif status >= 500:
        category = ErrorCategory.SERVER_ERROR
    else:
        category = ErrorCategory.PROVIDER_ERROR

    retryable = status in (429, 500, 502, 503, 504)

    # Try to extract retry-after
    retry_after_ms: int | None = None

    # Try to extract message from JSON body
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
        retry_after_ms=retry_after_ms,
        raw=body[:2000] if body else None,
    )


# ── Request building ─────────────────────────────────────────────


def _build_params(
    model: Model,
    context: Context,
    options: StreamOptions | None,
    profile: OpenAICompatProfile,
) -> dict[str, Any]:
    """Build the JSON body for a Chat Completions request."""
    messages = convert_messages(model, context, profile)

    params: dict[str, Any] = {
        "model": model.id,
        "messages": messages,
        "stream": True,
    }

    if profile.supports_usage_in_streaming:
        params["stream_options"] = {"include_usage": True}

    if profile.supports_store:
        params["store"] = False

    # Max tokens
    if options and options.max_tokens:
        if profile.max_tokens_field == "max_tokens":
            params["max_tokens"] = options.max_tokens
        else:
            params["max_completion_tokens"] = options.max_tokens

    # Temperature
    if options and options.temperature is not None:
        params["temperature"] = options.temperature

    # Tools
    if context.tools:
        params["tools"] = convert_tools(context.tools, profile)
        if profile.zai_tool_stream:
            params["tool_stream"] = True
    elif has_tool_history(context.messages):
        params["tools"] = []

    # Reasoning/thinking
    _apply_reasoning_params(params, model, options, profile)

    return params


def _apply_reasoning_params(
    params: dict[str, Any],
    model: Model,
    options: StreamOptions | None,
    profile: OpenAICompatProfile,
) -> None:
    """Apply provider-specific reasoning/thinking parameters."""
    if not model.capabilities.reasoning:
        return

    # Extract reasoning effort from metadata if provided
    effort: str | None = None
    if options and options.metadata:
        effort = options.metadata.get("reasoning_effort")

    fmt = profile.thinking_format
    if fmt == "none":
        return

    if fmt == "openai" and profile.supports_reasoning_effort:
        if effort:
            params["reasoning_effort"] = effort

    elif fmt == "deepseek":
        params["thinking"] = {"type": "enabled" if effort else "disabled"}
        if effort and profile.supports_reasoning_effort:
            params["reasoning_effort"] = effort

    elif fmt == "openrouter":
        if effort:
            params["reasoning"] = {"effort": effort}

    elif fmt == "together":
        params["reasoning"] = {"enabled": bool(effort)}
        if effort and profile.supports_reasoning_effort:
            params["reasoning_effort"] = effort

    elif fmt == "zai" or fmt == "qwen":
        params["enable_thinking"] = bool(effort)


# ── Streaming state machine ─────────────────────────────────────


class _StreamState:
    """Mutable state tracker during SSE streaming."""

    def __init__(self, output: AssistantMessage) -> None:
        self.output = output
        self.blocks: list[TextContent | ThinkingContent | ToolCall] = []
        self.text_block: TextContent | None = None
        self.thinking_block: ThinkingContent | None = None
        self.tool_blocks_by_index: dict[int, _ToolCallState] = {}
        self.tool_blocks_by_id: dict[str, _ToolCallState] = {}

    def content_index(self, block: TextContent | ThinkingContent | ToolCall) -> int:
        return self.blocks.index(block)


class _ToolCallState:
    """Tracks a tool call being streamed."""

    def __init__(self, tool_call: ToolCall, content_index: int) -> None:
        self.tool_call = tool_call
        self.content_index = content_index
        self.partial_args = ""


def _process_chunk(
    chunk: dict[str, Any],
    state: _StreamState,
    stream: EventStream,
    profile: OpenAICompatProfile,
    model: Model,
) -> None:
    """Process a single SSE chunk and emit events."""
    output = state.output

    # Response metadata
    if (chunk_id := chunk.get("id")) and not output.response_id:
        output.response_id = chunk_id
    if (chunk_model := chunk.get("model")) and isinstance(chunk_model, str) and chunk_model != model.id:
        output.response_model = chunk_model

    # Usage
    if raw_usage := chunk.get("usage"):
        output.usage = _parse_usage(raw_usage, model)

    # Process choices
    choices = chunk.get("choices")
    if not choices or not isinstance(choices, list):
        return
    choice = choices[0]

    # Fallback usage in choice
    if not chunk.get("usage") and choice.get("usage"):
        output.usage = _parse_usage(choice["usage"], model)

    # Finish reason
    if fr := choice.get("finish_reason"):
        stop_reason, error_msg = _map_stop_reason(fr)
        output.stop_reason = stop_reason
        if error_msg and output.error is None:
            output.error = DinoError(
                category=ErrorCategory.CONTENT_FILTERED,
                provider=model.provider,
                message=error_msg,
            )

    delta = choice.get("delta")
    if not delta:
        return

    # Text content
    content = delta.get("content")
    if content and isinstance(content, str):
        _handle_text_delta(state, stream, content)

    # Reasoning/thinking content
    _handle_reasoning_delta(state, stream, delta, profile)

    # Tool calls
    if tool_calls := delta.get("tool_calls"):
        for tc in tool_calls:
            _handle_tool_call_delta(state, stream, tc, model)


def _handle_text_delta(state: _StreamState, stream: EventStream, text: str) -> None:
    """Handle a text content delta."""
    output = state.output
    if state.text_block is None:
        block = TextContent(text="")
        state.text_block = block
        state.blocks.append(block)
        output.content = list(state.blocks)
        idx = state.content_index(block)
        stream.push(TextStart(content_index=idx, partial=output))
    else:
        block = state.text_block

    # TextContent is frozen, rebuild with accumulated text
    new_block = TextContent(text=block.text + text)
    bi = state.content_index(block)
    state.blocks[bi] = new_block
    state.text_block = new_block
    output.content = list(state.blocks)
    stream.push(TextDelta(content_index=bi, delta=text, partial=output))


def _handle_reasoning_delta(
    state: _StreamState,
    stream: EventStream,
    delta: dict[str, Any],
    profile: OpenAICompatProfile,
) -> None:
    """Handle reasoning/thinking content from various field names."""
    output = state.output
    reasoning_text: str | None = None

    for field_name in profile.reasoning_fields:
        val = delta.get(field_name)
        if isinstance(val, str) and val:
            reasoning_text = val
            break

    if not reasoning_text:
        return

    if state.thinking_block is None:
        block = ThinkingContent(thinking="")
        state.thinking_block = block
        state.blocks.append(block)
        output.content = list(state.blocks)
        idx = state.content_index(block)
        stream.push(ThinkingStart(content_index=idx, partial=output))
    else:
        block = state.thinking_block

    new_block = ThinkingContent(thinking=block.thinking + reasoning_text, signature=block.signature)
    bi = state.content_index(block)
    state.blocks[bi] = new_block
    state.thinking_block = new_block
    output.content = list(state.blocks)
    stream.push(ThinkingDelta(content_index=bi, delta=reasoning_text, partial=output))


def _handle_tool_call_delta(
    state: _StreamState,
    stream: EventStream,
    tc_delta: dict[str, Any],
    model: Model,
) -> None:
    """Handle a tool call delta chunk."""
    output = state.output
    stream_index: int | None = tc_delta.get("index")
    tc_id: str | None = tc_delta.get("id")
    func_data: dict[str, Any] | None = tc_delta.get("function")

    # Find or create the tool call state
    tc_state: _ToolCallState | None = None

    if stream_index is not None:
        tc_state = state.tool_blocks_by_index.get(stream_index)
    if tc_state is None and tc_id:
        tc_state = state.tool_blocks_by_id.get(tc_id)

    if tc_state is None:
        # New tool call
        tool_call = ToolCall(
            id=tc_id or "",
            name=(func_data or {}).get("name", ""),
            arguments={},
        )
        state.blocks.append(tool_call)
        output.content = list(state.blocks)
        content_index = state.content_index(tool_call)
        tc_state = _ToolCallState(tool_call=tool_call, content_index=content_index)

        if stream_index is not None:
            state.tool_blocks_by_index[stream_index] = tc_state
        if tc_id:
            state.tool_blocks_by_id[tc_id] = tc_state

        stream.push(ToolCallStart(content_index=content_index, partial=output))

    # Update existing tool call
    if tc_id and not tc_state.tool_call.id:
        # ToolCall is frozen — rebuild
        tc_state.tool_call = ToolCall(
            id=tc_id,
            name=tc_state.tool_call.name,
            arguments=tc_state.tool_call.arguments,
        )
        state.blocks[tc_state.content_index] = tc_state.tool_call
        state.tool_blocks_by_id[tc_id] = tc_state

    if func_data and func_data.get("name") and not tc_state.tool_call.name:
        tc_state.tool_call = ToolCall(
            id=tc_state.tool_call.id,
            name=func_data["name"],
            arguments=tc_state.tool_call.arguments,
        )
        state.blocks[tc_state.content_index] = tc_state.tool_call

    # Argument deltas
    arg_delta = ""
    if func_data and (args := func_data.get("arguments")):
        arg_delta = args
        tc_state.partial_args += args
        tc_state.tool_call = ToolCall(
            id=tc_state.tool_call.id,
            name=tc_state.tool_call.name,
            arguments=parse_streaming_json(tc_state.partial_args),
        )
        state.blocks[tc_state.content_index] = tc_state.tool_call

    output.content = list(state.blocks)
    stream.push(ToolCallDelta(content_index=tc_state.content_index, delta=arg_delta, partial=output))

    if stream_index is not None and stream_index not in state.tool_blocks_by_index:
        state.tool_blocks_by_index[stream_index] = tc_state


def _finalize_blocks(state: _StreamState, stream: EventStream) -> None:
    """Emit end events for all active content blocks."""
    output = state.output

    if state.text_block is not None:
        idx = state.content_index(state.text_block)
        stream.push(TextEnd(content_index=idx, text=state.text_block.text, partial=output))

    if state.thinking_block is not None:
        idx = state.content_index(state.thinking_block)
        stream.push(ThinkingEnd(content_index=idx, text=state.thinking_block.thinking, partial=output))

    for tc_state in state.tool_blocks_by_index.values():
        # Final parse of accumulated args
        tc_state.tool_call = ToolCall(
            id=tc_state.tool_call.id,
            name=tc_state.tool_call.name,
            arguments=parse_streaming_json(tc_state.partial_args),
        )
        state.blocks[tc_state.content_index] = tc_state.tool_call
        output.content = list(state.blocks)
        stream.push(ToolCallEnd(
            content_index=tc_state.content_index,
            tool_call=tc_state.tool_call,
            partial=output,
        ))

    # Also finalize any tool calls tracked only by ID (no stream_index)
    finalized_indices = {tc.content_index for tc in state.tool_blocks_by_index.values()}
    for tc_state in state.tool_blocks_by_id.values():
        if tc_state.content_index in finalized_indices:
            continue
        tc_state.tool_call = ToolCall(
            id=tc_state.tool_call.id,
            name=tc_state.tool_call.name,
            arguments=parse_streaming_json(tc_state.partial_args),
        )
        state.blocks[tc_state.content_index] = tc_state.tool_call
        output.content = list(state.blocks)
        stream.push(ToolCallEnd(
            content_index=tc_state.content_index,
            tool_call=tc_state.tool_call,
            partial=output,
        ))


# ── Provider class ───────────────────────────────────────────────


def _get_api_key(model: Model, options: StreamOptions | None) -> str:
    """Resolve API key from options, environment, or raise."""
    if options and options.api_key:
        return options.api_key

    # Check common env var patterns
    provider_upper = model.provider.upper().replace("-", "_")
    env_vars = [
        f"{provider_upper}_API_KEY",
        "OPENAI_API_KEY",
    ]
    for var in env_vars:
        val = os.environ.get(var)
        if val:
            return val

    return ""


class OpenAICompletionsProvider:
    """Provider for OpenAI Chat Completions API and compatible endpoints.

    Works with OpenAI, DeepSeek, Groq, xAI, OpenRouter, Together, and
    any other provider that follows the OpenAI Chat Completions protocol.

    Uses raw httpx for HTTP to keep dino-ai zero-dependency.
    Install httpx separately: ``pip install httpx``
    """

    def __init__(self, profile: OpenAICompatProfile | None = None) -> None:
        self._profile = profile

    @property
    def api(self) -> str:
        return API_ID

    def _get_profile(self, model: Model) -> OpenAICompatProfile:
        if self._profile is not None:
            return self._profile
        return detect_profile(model.provider, model.base_url)

    def stream(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None = None,
    ) -> EventStream:
        """Stream a response from an OpenAI-compatible endpoint."""
        profile = self._get_profile(model)
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

                params = _build_params(model, context, options, profile)

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
                }
                if api_key:
                    headers["Authorization"] = f"Bearer {api_key}"
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
                url = f"{base_url}/chat/completions"

                async with httpx.AsyncClient(timeout=timeout) as client, client.stream(
                    "POST",
                    url,
                    json=params,
                    headers=headers,
                ) as response:
                    # Response hook
                    if options and options.on_response:
                        resp_headers = dict(response.headers)
                        result = options.on_response(response.status_code, resp_headers, model)
                        if asyncio.iscoroutine(result):
                            await result

                    if response.status_code != 200:
                        body = await response.aread()
                        body_text = body.decode("utf-8", errors="replace")
                        error = _classify_error(response.status_code, body_text, model.provider)
                        output.stop_reason = "error"
                        output.error = error
                        event_stream.push(StreamError(
                            reason="error",
                            error=error,
                            message=output,
                        ))
                        event_stream.push(StreamDone(reason="error", message=output))
                        return

                    event_stream.push(StreamStart(partial=output))

                    async for chunk in parse_sse_stream(response.aiter_bytes()):
                        _process_chunk(chunk, state, event_stream, profile, model)

                _finalize_blocks(state, event_stream)

                output.content = list(state.blocks)
                event_stream.push(StreamDone(reason=output.stop_reason, message=output))

            except ImportError:
                error = DinoError(
                    category=ErrorCategory.PROVIDER_ERROR,
                    provider=model.provider,
                    message="httpx is required for OpenAI provider. Install with: pip install httpx",
                )
                output.stop_reason = "error"
                output.error = error
                event_stream.push(StreamError(reason="error", error=error, message=output))
                event_stream.push(StreamDone(reason="error", message=output))

            except Exception as exc:
                error = DinoError(
                    category=ErrorCategory.NETWORK_ERROR if "connect" in str(exc).lower() else ErrorCategory.UNKNOWN,
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

        # Map SimpleStreamOptions to StreamOptions with reasoning in metadata
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
