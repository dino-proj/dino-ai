"""AWS Bedrock Converse Stream provider.

Uses boto3's ``bedrock-runtime`` client to stream responses via the
Converse API. Runs the synchronous boto3 call in a thread executor
for async compatibility.

Requires ``boto3``: ``pip install boto3``

Usage::

    from dino_ai.providers.bedrock import BedrockProvider

    provider = BedrockProvider()
    client = DinoClient(providers=[provider])
"""

from __future__ import annotations

import asyncio
import os
import re
import time
from typing import Any

from dino_ai._json import parse_streaming_json
from dino_ai.content import TextContent, ThinkingContent, ToolCall
from dino_ai.context import AssistantMessage, Context
from dino_ai.error import DinoError, ErrorCategory
from dino_ai.events import (
    AssistantMessageEvent,
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
from dino_ai.providers.bedrock_messages import convert_messages, convert_system, convert_tools, map_stop_reason
from dino_ai.stream import EventStream
from dino_ai.usage import Cost, Usage

API_ID = "bedrock-converse-stream"

# ── Region resolution ────────────────────────────────────────────


def _resolve_region(model: Model, options: StreamOptions | None) -> str:
    """Resolve AWS region from metadata, environment, or model URL."""
    if options and options.metadata:
        region = options.metadata.get("region")
        if region:
            return str(region)

    for var in ("AWS_REGION", "AWS_DEFAULT_REGION"):
        val = os.environ.get(var)
        if val:
            return val

    # Try to extract from base_url
    match = re.search(r"bedrock-runtime\.([a-z0-9-]+)\.amazonaws\.com", model.base_url)
    if match:
        return match.group(1)

    return "us-east-1"


# ── Usage parsing ────────────────────────────────────────────────


def _parse_usage(raw: dict[str, Any], model: Model) -> Usage:
    """Parse Bedrock usage metadata into Usage."""
    input_tokens = raw.get("inputTokens", 0) or 0
    output_tokens = raw.get("outputTokens", 0) or 0
    total = raw.get("totalTokens", 0) or 0
    cache_read = raw.get("cacheReadInputTokens", 0) or 0
    cache_write = raw.get("cacheWriteInputTokens", 0) or 0

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
        total_tokens=total if total else input_tokens + output_tokens,
        cost=cost,
    )


# ── Error classification ─────────────────────────────────────────


def _classify_error(exc: Exception, provider: str) -> DinoError:
    """Classify a boto3/botocore exception into a DinoError."""
    exc_name = type(exc).__name__
    message = str(exc)

    if exc_name == "ThrottlingException":
        return DinoError(
            category=ErrorCategory.RATE_LIMITED,
            provider=provider,
            message=f"Throttling error: {message}",
            retryable=True,
        )

    if exc_name == "ValidationException":
        lower = message.lower()
        if "token" in lower and ("limit" in lower or "exceed" in lower):
            category = ErrorCategory.CONTEXT_OVERFLOW
        else:
            category = ErrorCategory.INVALID_REQUEST
        return DinoError(
            category=category,
            provider=provider,
            message=f"Validation error: {message}",
        )

    if exc_name == "AccessDeniedException":
        return DinoError(
            category=ErrorCategory.AUTH_FAILURE,
            provider=provider,
            message=f"Access denied: {message}",
        )

    if exc_name in ("InternalServerException", "ServiceUnavailableException"):
        return DinoError(
            category=ErrorCategory.SERVER_ERROR,
            provider=provider,
            message=f"Server error: {message}",
            retryable=True,
        )

    if exc_name == "ModelStreamErrorException":
        return DinoError(
            category=ErrorCategory.PROVIDER_ERROR,
            provider=provider,
            message=f"Model stream error: {message}",
            retryable=True,
        )

    if exc_name == "ResourceNotFoundException":
        return DinoError(
            category=ErrorCategory.MODEL_NOT_FOUND,
            provider=provider,
            message=f"Resource not found: {message}",
        )

    # Generic fallback
    return DinoError(
        category=ErrorCategory.UNKNOWN,
        provider=provider,
        message=message,
        retryable=True,
    )


# ── Request building ─────────────────────────────────────────────


def _build_params(
    model: Model,
    context: Context,
    options: StreamOptions | None,
) -> dict[str, Any]:
    """Build the kwargs dict for boto3's converse_stream()."""
    messages = convert_messages(model, context)

    params: dict[str, Any] = {
        "modelId": model.id,
        "messages": messages,
    }

    # System prompt
    system = convert_system(context)
    if system:
        params["system"] = system

    # Inference config
    config: dict[str, Any] = {}
    if options and options.max_tokens:
        config["maxTokens"] = options.max_tokens
    elif model.limits.max_output_tokens:
        config["maxTokens"] = model.limits.max_output_tokens

    if options and options.temperature is not None:
        config["temperature"] = options.temperature

    if config:
        params["inferenceConfig"] = config

    # Tools
    if context.tools:
        params["toolConfig"] = {"tools": convert_tools(context.tools)}

    # Thinking config for reasoning models
    if model.capabilities.reasoning:
        additional = _build_thinking_config(model, options)
        if additional:
            params["additionalModelRequestFields"] = additional

    return params


def _build_thinking_config(model: Model, options: StreamOptions | None) -> dict[str, Any] | None:
    """Build additionalModelRequestFields for thinking."""
    effort: str | None = None
    if options and options.metadata:
        effort = options.metadata.get("reasoning_effort")

    if not effort:
        return None

    # Use budget-based thinking
    budget = _effort_to_budget(effort, model)
    return {
        "thinking": {
            "type": "enabled",
            "budget_tokens": budget,
        }
    }


def _effort_to_budget(effort: str, model: Model) -> int:
    """Map reasoning effort to thinking budget tokens."""
    budgets = {
        "minimal": 1024,
        "low": 2048,
        "medium": 8192,
        "high": 16384,
    }
    return budgets.get(effort, 8192)


# ── Streaming state machine ─────────────────────────────────────

PushFn = Any  # Callable[[AssistantMessageEvent], None] — but mypy doesn't like Protocol here


class _BlockState:
    """Tracks a content block during streaming."""

    def __init__(self) -> None:
        self.block_type: str | None = None  # "text" | "thinking" | "toolCall"
        self.content_index: int = -1
        self.text = ""
        self.thinking = ""
        self.signature = ""
        self.tool_id = ""
        self.tool_name = ""
        self.partial_args = ""


class _StreamState:
    """Mutable state for Bedrock Converse streaming."""

    def __init__(self, output: AssistantMessage) -> None:
        self.output = output
        self.content_blocks: list[TextContent | ThinkingContent | ToolCall] = []
        self.active_blocks: dict[int, _BlockState] = {}  # by contentBlockIndex
        self.text_block: _BlockState | None = None
        self.thinking_block: _BlockState | None = None


def _process_event(
    event: dict[str, Any],
    state: _StreamState,
    push: PushFn,
    model: Model,
) -> None:
    """Process a single Bedrock Converse stream event."""
    if "contentBlockStart" in event:
        _handle_block_start(event["contentBlockStart"], state, push)

    elif "contentBlockDelta" in event:
        _handle_block_delta(event["contentBlockDelta"], state, push, model)

    elif "contentBlockStop" in event:
        _handle_block_stop(event["contentBlockStop"], state, push)

    elif "messageStop" in event:
        stop_data = event["messageStop"]
        state.output.stop_reason = map_stop_reason(stop_data.get("stopReason"))

    elif "metadata" in event:
        meta = event["metadata"]
        if "usage" in meta:
            state.output.usage = _parse_usage(meta["usage"], model)


def _handle_block_start(
    data: dict[str, Any],
    state: _StreamState,
    push: PushFn,
) -> None:
    """Handle contentBlockStart — only tool calls have explicit starts."""
    ci = data.get("contentBlockIndex", 0)
    start = data.get("start", {})

    if "toolUse" in start:
        tu = start["toolUse"]
        block = _BlockState()
        block.block_type = "toolCall"
        block.content_index = ci
        block.tool_id = tu.get("toolUseId", "")
        block.tool_name = tu.get("name", "")
        state.active_blocks[ci] = block

        tc: TextContent | ThinkingContent | ToolCall = ToolCall(
            id=block.tool_id, name=block.tool_name, arguments={}
        )
        # Extend content_blocks to the right index
        while len(state.content_blocks) <= ci:
            state.content_blocks.append(TextContent(text=""))
        state.content_blocks[ci] = tc
        state.output.content = list(state.content_blocks)
        push(ToolCallStart(content_index=ci, partial=state.output))


def _handle_block_delta(
    data: dict[str, Any],
    state: _StreamState,
    push: PushFn,
    model: Model,
) -> None:
    """Handle contentBlockDelta — text, tool input, or reasoning."""
    ci = data.get("contentBlockIndex", 0)
    delta = data.get("delta", {})

    if "text" in delta:
        _handle_text_delta(ci, delta["text"], state, push)

    elif "toolUse" in delta:
        _handle_tool_delta(ci, delta["toolUse"], state, push)

    elif "reasoningContent" in delta:
        _handle_thinking_delta(ci, delta["reasoningContent"], state, push)


def _handle_text_delta(ci: int, text: str, state: _StreamState, push: PushFn) -> None:
    """Handle a text delta."""
    block = state.active_blocks.get(ci)

    if block is None:
        # Lazy-create text block
        block = _BlockState()
        block.block_type = "text"
        block.content_index = ci
        state.active_blocks[ci] = block
        state.text_block = block

        while len(state.content_blocks) <= ci:
            state.content_blocks.append(TextContent(text=""))
        state.content_blocks[ci] = TextContent(text="")
        state.output.content = list(state.content_blocks)
        push(TextStart(content_index=ci, partial=state.output))

    block.text += text
    entry: TextContent | ThinkingContent | ToolCall = TextContent(text=block.text)
    state.content_blocks[ci] = entry
    state.output.content = list(state.content_blocks)
    push(TextDelta(content_index=ci, delta=text, partial=state.output))


def _handle_tool_delta(ci: int, tool_data: dict[str, Any], state: _StreamState, push: PushFn) -> None:
    """Handle a tool use input delta."""
    block = state.active_blocks.get(ci)
    if block is None:
        return

    input_chunk = tool_data.get("input", "")
    block.partial_args += input_chunk

    parsed = parse_streaming_json(block.partial_args)
    tool_call = ToolCall(id=block.tool_id, name=block.tool_name, arguments=parsed)
    entry: TextContent | ThinkingContent | ToolCall = tool_call
    state.content_blocks[ci] = entry
    state.output.content = list(state.content_blocks)
    push(ToolCallDelta(content_index=ci, delta=input_chunk, partial=state.output))


def _handle_thinking_delta(
    ci: int, reasoning: dict[str, Any], state: _StreamState, push: PushFn
) -> None:
    """Handle a reasoningContent delta."""
    text = reasoning.get("text", "")
    signature = reasoning.get("signature", "")

    block = state.active_blocks.get(ci)

    if block is None:
        # Lazy-create thinking block
        block = _BlockState()
        block.block_type = "thinking"
        block.content_index = ci
        state.active_blocks[ci] = block
        state.thinking_block = block

        while len(state.content_blocks) <= ci:
            state.content_blocks.append(TextContent(text=""))
        entry: TextContent | ThinkingContent | ToolCall = ThinkingContent(thinking="")
        state.content_blocks[ci] = entry
        state.output.content = list(state.content_blocks)
        push(ThinkingStart(content_index=ci, partial=state.output))

    if text:
        block.thinking += text
    if signature:
        block.signature = signature

    entry = ThinkingContent(thinking=block.thinking, signature=block.signature or None)
    state.content_blocks[ci] = entry
    state.output.content = list(state.content_blocks)
    if text:
        push(ThinkingDelta(content_index=ci, delta=text, partial=state.output))


def _handle_block_stop(
    data: dict[str, Any],
    state: _StreamState,
    push: PushFn,
) -> None:
    """Handle contentBlockStop — finalize the block."""
    ci = data.get("contentBlockIndex", 0)
    block = state.active_blocks.get(ci)
    if block is None:
        return

    if block.block_type == "text":
        push(TextEnd(content_index=ci, text=block.text, partial=state.output))

    elif block.block_type == "thinking":
        entry: TextContent | ThinkingContent | ToolCall = ThinkingContent(
            thinking=block.thinking, signature=block.signature or None
        )
        state.content_blocks[ci] = entry
        state.output.content = list(state.content_blocks)
        push(ThinkingEnd(content_index=ci, text=block.thinking, partial=state.output))

    elif block.block_type == "toolCall":
        parsed = parse_streaming_json(block.partial_args)
        tool_call = ToolCall(id=block.tool_id, name=block.tool_name, arguments=parsed)
        entry = tool_call
        state.content_blocks[ci] = entry
        state.output.content = list(state.content_blocks)
        push(ToolCallEnd(content_index=ci, tool_call=tool_call, partial=state.output))


# ── Provider class ───────────────────────────────────────────────


class BedrockProvider:
    """Provider for AWS Bedrock Converse Stream API.

    Uses boto3's bedrock-runtime client. The synchronous boto3 call
    runs in a thread executor for async compatibility.

    Install boto3 separately: ``pip install boto3``
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
        """Stream a response from Bedrock."""
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
            loop = asyncio.get_running_loop()

            def _push(event: AssistantMessageEvent) -> None:
                loop.call_soon_threadsafe(event_stream.push, event)

            def _sync_stream() -> None:
                import boto3  # type: ignore[import-untyped]

                region = _resolve_region(model, options)

                # Build boto3 client kwargs
                client_kwargs: dict[str, Any] = {
                    "service_name": "bedrock-runtime",
                    "region_name": region,
                }

                # Custom endpoint
                if model.base_url and "amazonaws.com" not in model.base_url:
                    client_kwargs["endpoint_url"] = model.base_url

                # Skip auth for proxy setups
                if os.environ.get("AWS_BEDROCK_SKIP_AUTH") == "1":
                    from botocore.config import Config as BotoConfig  # type: ignore[import-untyped]

                    client_kwargs["aws_access_key_id"] = "dummy"
                    client_kwargs["aws_secret_access_key"] = "dummy"
                    client_kwargs["config"] = BotoConfig(signature_version="v4")

                client = boto3.client(**client_kwargs)

                params = _build_params(model, context, options)

                # Payload hook (sync version — must not be async)
                if options and options.on_payload:
                    hook_result: Any = options.on_payload(params, model)
                    if isinstance(hook_result, dict):
                        params = hook_result

                response = client.converse_stream(**params)

                _push(StreamStart(partial=output))

                for event in response["stream"]:
                    _process_event(event, state, _push, model)

                output.content = list(state.content_blocks)
                _push(StreamDone(reason=output.stop_reason, message=output))

            try:
                await loop.run_in_executor(None, _sync_stream)

            except ImportError:
                error = DinoError(
                    category=ErrorCategory.PROVIDER_ERROR,
                    provider=model.provider,
                    message="boto3 is required for Bedrock provider. Install with: pip install boto3",
                )
                output.stop_reason = "error"
                output.error = error
                event_stream.push(StreamError(reason="error", error=error, message=output))
                event_stream.push(StreamDone(reason="error", message=output))

            except Exception as exc:
                error = _classify_error(exc, model.provider)
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
