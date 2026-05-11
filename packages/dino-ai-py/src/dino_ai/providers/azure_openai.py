"""Azure OpenAI provider — thin wrapper over OpenAI Completions.

Handles Azure-specific URL patterns and authentication:
- URL: ``{base_url}/openai/deployments/{deployment}/chat/completions?api-version=...``
- Auth: ``api-key`` header (not ``Authorization: Bearer``)

Usage::

    from dino_ai.providers.azure_openai import AzureOpenAIProvider

    provider = AzureOpenAIProvider()
"""

from __future__ import annotations

import asyncio
import os
import time
from typing import Any

from dino_ai.context import AssistantMessage, Context
from dino_ai.error import DinoError, ErrorCategory
from dino_ai.events import StreamDone, StreamError, StreamStart
from dino_ai.model import Model
from dino_ai.options import SimpleStreamOptions, StreamOptions
from dino_ai.providers.openai_compat import OpenAICompatProfile
from dino_ai.providers.openai_completions import (
    _build_params,
    _classify_error,
    _finalize_blocks,
    _process_chunk,
    _StreamState,
)
from dino_ai.providers.openai_sse import parse_sse_stream
from dino_ai.stream import EventStream
from dino_ai.usage import Usage

API_ID = "openai-completions"

DEFAULT_API_VERSION = "2025-01-01-preview"

# Azure uses the same OpenAI profile but always has developer role and
# max_completion_tokens
PROFILE_AZURE = OpenAICompatProfile(
    thinking_format="openai",
    supports_reasoning_effort=True,
    supports_usage_in_streaming=True,
    supports_store=False,
    max_tokens_field="max_completion_tokens",
    use_developer_role=True,
)


def _get_azure_api_key(model: Model, options: StreamOptions | None) -> str:
    """Resolve Azure API key from options or environment."""
    if options and options.api_key:
        return options.api_key

    env_vars = ["AZURE_OPENAI_API_KEY", "AZURE_API_KEY"]
    for var in env_vars:
        val = os.environ.get(var)
        if val:
            return val

    return ""


def _get_api_version(model: Model, options: StreamOptions | None) -> str:
    """Resolve API version from metadata, environment, or default."""
    if options and options.metadata:
        v = options.metadata.get("api_version")
        if v:
            return str(v)

    val = os.environ.get("AZURE_OPENAI_API_VERSION")
    if val:
        return val

    return DEFAULT_API_VERSION


class AzureOpenAIProvider:
    """Provider for Azure OpenAI Service.

    Uses the Azure-specific URL pattern and ``api-key`` header authentication.
    Reuses the OpenAI Completions streaming state machine.
    """

    def __init__(self, api_version: str | None = None) -> None:
        self._api_version = api_version

    @property
    def api(self) -> str:
        return API_ID

    def stream(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None = None,
    ) -> EventStream:
        """Stream a response from Azure OpenAI."""
        profile = PROFILE_AZURE
        api_key = _get_azure_api_key(model, options)
        api_version = self._api_version or _get_api_version(model, options)

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

                base_url = model.base_url.rstrip("/")
                url = f"{base_url}/openai/deployments/{model.id}/chat/completions?api-version={api_version}"

                headers: dict[str, str] = {
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream",
                }
                if api_key:
                    headers["api-key"] = api_key
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
                    message="httpx is required for Azure OpenAI provider. Install with: pip install httpx",
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
