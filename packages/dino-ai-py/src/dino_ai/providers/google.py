"""Google Gemini (Generative AI) provider.

Uses raw httpx for HTTP/SSE against the Gemini REST API.
Supports thinking/reasoning, function calling, images, and streaming.

Usage::

    from dino_ai.providers.google import GoogleProvider

    provider = GoogleProvider()
    client = DinoClient(providers=[provider])
"""

from __future__ import annotations

import asyncio
import json
import os
import time
from typing import Any

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
from dino_ai.providers.google_messages import convert_messages, convert_system, convert_tools, map_stop_reason
from dino_ai.providers.openai_sse import parse_sse_stream
from dino_ai.stream import EventStream
from dino_ai.usage import Cost, Usage

API_ID = "google-generative-ai"

# ── Usage parsing ────────────────────────────────────────────────


def _parse_usage(raw: dict[str, Any], model: Model) -> Usage:
    """Parse Gemini usageMetadata into Usage."""
    prompt = raw.get("promptTokenCount", 0) or 0
    candidates = raw.get("candidatesTokenCount", 0) or 0
    thoughts = raw.get("thoughtsTokenCount", 0) or 0
    cached = raw.get("cachedContentTokenCount", 0) or 0
    total = raw.get("totalTokenCount", 0) or 0

    input_tokens = prompt - cached
    output_tokens = candidates + thoughts

    pricing = model.pricing
    cost = Cost(
        input=input_tokens * pricing.input / 1_000_000,
        output=output_tokens * pricing.output / 1_000_000,
        cache_read=cached * pricing.cache_read / 1_000_000,
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
        cache_read_tokens=cached,
        total_tokens=total if total else input_tokens + output_tokens + cached,
        cost=cost,
    )


# ── Error classification ─────────────────────────────────────────


def _classify_error(status: int, body: str, provider: str) -> DinoError:
    """Classify a Google API HTTP error response."""
    if status in (401, 403):
        category = ErrorCategory.AUTH_FAILURE
    elif status == 429:
        category = ErrorCategory.RATE_LIMITED
    elif status == 400:
        lower = body.lower()
        if "token" in lower and ("limit" in lower or "exceed" in lower):
            category = ErrorCategory.CONTEXT_OVERFLOW
        elif "safety" in lower or "block" in lower:
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

    message = f"HTTP {status}"
    try:
        data = json.loads(body)
        if isinstance(data, dict):
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
    """Build the JSON body for a Gemini generateContent request."""
    contents = convert_messages(model, context)

    params: dict[str, Any] = {
        "contents": contents,
    }

    # Generation config
    config: dict[str, Any] = {}

    system = convert_system(context)
    if system:
        config["systemInstruction"] = system

    if options and options.max_tokens:
        config["maxOutputTokens"] = options.max_tokens
    elif model.limits.max_output_tokens:
        config["maxOutputTokens"] = model.limits.max_output_tokens

    if options and options.temperature is not None:
        config["temperature"] = options.temperature

    if context.tools:
        params["tools"] = convert_tools(context.tools)

    # Thinking config
    if model.capabilities.reasoning:
        thinking = _build_thinking_config(model, options)
        if thinking:
            config["thinkingConfig"] = thinking

    if config:
        params["generationConfig"] = config

    return params


def _build_thinking_config(model: Model, options: StreamOptions | None) -> dict[str, Any] | None:
    """Build thinking config for reasoning models."""
    effort: str | None = None
    if options and options.metadata:
        effort = options.metadata.get("reasoning_effort")

    if not effort:
        return None

    # Use thinkingBudget for Gemini 2.x style
    budget = _effort_to_budget(effort, model)
    return {"includeThoughts": True, "thinkingBudget": budget}


def _effort_to_budget(effort: str, model: Model) -> int:
    """Map reasoning effort to thinking budget tokens."""
    max_output = model.limits.max_output_tokens or 16384
    budgets = {
        "minimal": 128,
        "low": 2048,
        "medium": 8192,
        "high": max(16384, max_output),
    }
    return budgets.get(effort, 8192)


# ── Streaming state machine ─────────────────────────────────────


class _BlockState:
    """Tracks the currently active content block during streaming."""

    def __init__(self) -> None:
        self.block_type: str | None = None  # "text" | "thinking" | "toolCall"
        self.content_index: int = -1
        self.text = ""
        self.thinking = ""
        self.signature = ""
        self.tool_id = ""
        self.tool_name = ""
        self.tool_args: dict[str, Any] = {}


class _StreamState:
    """Mutable state for Gemini SSE streaming."""

    def __init__(self, output: AssistantMessage) -> None:
        self.output = output
        self.content_blocks: list[TextContent | ThinkingContent | ToolCall] = []
        self.current: _BlockState | None = None
        self.response_id: str | None = None
        self._tc_counter = 0

    def next_tool_id(self, name: str) -> str:
        self._tc_counter += 1
        return f"{name}_{int(time.time() * 1000)}_{self._tc_counter}"


def _process_chunk(
    chunk: dict[str, Any],
    state: _StreamState,
    stream: EventStream,
    model: Model,
) -> None:
    """Process a single Gemini streaming chunk."""
    # Response ID
    if not state.response_id and chunk.get("responseId"):
        state.response_id = chunk["responseId"]
        state.output.response_id = state.response_id

    # Usage
    if usage_meta := chunk.get("usageMetadata"):
        state.output.usage = _parse_usage(usage_meta, model)

    # Process candidates
    candidates = chunk.get("candidates", [])
    if not candidates:
        return

    candidate = candidates[0]

    # Finish reason
    if finish_reason := candidate.get("finishReason"):
        state.output.stop_reason = map_stop_reason(finish_reason)

    # Content parts
    content = candidate.get("content", {})
    parts = content.get("parts", [])

    for part in parts:
        _process_part(part, state, stream, model)


def _process_part(
    part: dict[str, Any],
    state: _StreamState,
    stream: EventStream,
    model: Model,
) -> None:
    """Process a single content part from a Gemini chunk."""
    signature = part.get("thoughtSignature", "")

    if "functionCall" in part:
        _handle_function_call(part, state, stream, signature)
    elif part.get("thought") is True:
        _handle_thinking(part, state, stream, signature)
    elif "text" in part:
        _handle_text(part, state, stream, signature)


def _end_current_block(state: _StreamState, stream: EventStream) -> None:
    """Finalize the current block if any."""
    cur = state.current
    if cur is None:
        return

    ci = cur.content_index

    if cur.block_type == "text":
        final: TextContent | ThinkingContent | ToolCall = TextContent(text=cur.text)
        state.content_blocks[ci] = final
        state.output.content = list(state.content_blocks)
        stream.push(TextEnd(content_index=ci, text=cur.text, partial=state.output))

    elif cur.block_type == "thinking":
        final = ThinkingContent(
            thinking=cur.thinking,
            signature=cur.signature or None,
        )
        state.content_blocks[ci] = final
        state.output.content = list(state.content_blocks)
        stream.push(ThinkingEnd(content_index=ci, text=cur.thinking, partial=state.output))

    elif cur.block_type == "toolCall":
        final = ToolCall(id=cur.tool_id, name=cur.tool_name, arguments=cur.tool_args)
        state.content_blocks[ci] = final
        state.output.content = list(state.content_blocks)
        stream.push(ToolCallEnd(content_index=ci, tool_call=final, partial=state.output))

    state.current = None


def _handle_text(
    part: dict[str, Any],
    state: _StreamState,
    stream: EventStream,
    signature: str,
) -> None:
    """Handle a text part."""
    text = part.get("text", "")

    if state.current and state.current.block_type != "text":
        _end_current_block(state, stream)

    if state.current is None:
        # Start new text block
        cur = _BlockState()
        cur.block_type = "text"
        cur.content_index = len(state.content_blocks)
        cur.text = text
        cur.signature = signature
        state.current = cur

        tc = TextContent(text=text)
        state.content_blocks.append(tc)
        state.output.content = list(state.content_blocks)
        stream.push(TextStart(content_index=cur.content_index, partial=state.output))
        if text:
            stream.push(TextDelta(content_index=cur.content_index, delta=text, partial=state.output))
    else:
        # Continue existing text block
        state.current.text += text
        if signature and not state.current.signature:
            state.current.signature = signature
        tc = TextContent(text=state.current.text)
        state.content_blocks[state.current.content_index] = tc
        state.output.content = list(state.content_blocks)
        if text:
            stream.push(TextDelta(content_index=state.current.content_index, delta=text, partial=state.output))


def _handle_thinking(
    part: dict[str, Any],
    state: _StreamState,
    stream: EventStream,
    signature: str,
) -> None:
    """Handle a thinking part."""
    thinking = part.get("text", "")

    if state.current and state.current.block_type != "thinking":
        _end_current_block(state, stream)

    if state.current is None:
        cur = _BlockState()
        cur.block_type = "thinking"
        cur.content_index = len(state.content_blocks)
        cur.thinking = thinking
        cur.signature = signature
        state.current = cur

        tc: TextContent | ThinkingContent | ToolCall = ThinkingContent(thinking=thinking)
        state.content_blocks.append(tc)
        state.output.content = list(state.content_blocks)
        stream.push(ThinkingStart(content_index=cur.content_index, partial=state.output))
        if thinking:
            stream.push(ThinkingDelta(content_index=cur.content_index, delta=thinking, partial=state.output))
    else:
        state.current.thinking += thinking
        if signature and not state.current.signature:
            state.current.signature = signature
        tc = ThinkingContent(thinking=state.current.thinking, signature=state.current.signature or None)
        state.content_blocks[state.current.content_index] = tc
        state.output.content = list(state.content_blocks)
        if thinking:
            stream.push(ThinkingDelta(content_index=state.current.content_index, delta=thinking, partial=state.output))


def _handle_function_call(
    part: dict[str, Any],
    state: _StreamState,
    stream: EventStream,
    signature: str,
) -> None:
    """Handle a functionCall part — arrives as a complete object."""
    _end_current_block(state, stream)

    fc = part["functionCall"]
    name = fc.get("name", "")
    args = fc.get("args", {})
    tool_id = fc.get("id") or state.next_tool_id(name)

    ci = len(state.content_blocks)
    tool_call = ToolCall(id=tool_id, name=name, arguments=args)
    entry: TextContent | ThinkingContent | ToolCall = tool_call
    state.content_blocks.append(entry)
    state.output.content = list(state.content_blocks)

    stream.push(ToolCallStart(content_index=ci, partial=state.output))
    args_json = json.dumps(args)
    stream.push(ToolCallDelta(content_index=ci, delta=args_json, partial=state.output))
    stream.push(ToolCallEnd(content_index=ci, tool_call=tool_call, partial=state.output))

    # Force stop reason to toolUse
    state.output.stop_reason = "toolUse"


# ── Provider class ───────────────────────────────────────────────


def _get_api_key(model: Model, options: StreamOptions | None) -> str:
    """Resolve API key from options or environment."""
    if options and options.api_key:
        return options.api_key

    provider_upper = model.provider.upper().replace("-", "_")
    env_vars = [
        f"{provider_upper}_API_KEY",
        "GOOGLE_API_KEY",
        "GEMINI_API_KEY",
    ]
    for var in env_vars:
        val = os.environ.get(var)
        if val:
            return val

    return ""


class GoogleProvider:
    """Provider for Google Gemini (Generative AI) API.

    Uses raw httpx against the REST endpoint. Supports streaming,
    thinking/reasoning, function calling, and images.

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
        """Stream a response from the Gemini API."""
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

                base_url = model.base_url.rstrip("/")
                url = f"{base_url}/models/{model.id}:streamGenerateContent?alt=sse"
                if api_key:
                    url += f"&key={api_key}"

                headers: dict[str, str] = {
                    "Content-Type": "application/json",
                }
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

                event_stream.push(StreamStart(partial=output))

                async with httpx.AsyncClient(timeout=timeout) as http_client, http_client.stream(
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

                    # Gemini REST streaming uses same SSE format as OpenAI (data: lines)
                    async for chunk_data in parse_sse_stream(response.aiter_bytes()):
                        _process_chunk(chunk_data, state, event_stream, model)

                # Finalize any open block
                _end_current_block(state, event_stream)

                output.content = list(state.content_blocks)
                event_stream.push(StreamDone(reason=output.stop_reason, message=output))

            except ImportError:
                error = DinoError(
                    category=ErrorCategory.PROVIDER_ERROR,
                    provider=model.provider,
                    message="httpx is required for Google provider. Install with: pip install httpx",
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
