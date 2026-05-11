"""Server-Sent Events (SSE) parser for OpenAI-compatible streaming.

Parses a raw byte stream (from httpx or similar) into typed event dicts.
Zero external dependencies beyond the stdlib.
"""

from __future__ import annotations

import json
from collections.abc import AsyncIterator
from typing import Any


async def parse_sse_stream(
    byte_stream: AsyncIterator[bytes],
) -> AsyncIterator[dict[str, Any]]:
    """Parse an SSE byte stream into JSON event dicts.

    Yields one dict per ``data:`` line that contains valid JSON.
    Lines with ``data: [DONE]`` are silently skipped.

    Args:
        byte_stream: Async iterator of raw bytes from an HTTP response.

    Yields:
        Parsed JSON objects from each ``data:`` SSE event.
    """
    buffer = ""

    async for raw_chunk in byte_stream:
        buffer += raw_chunk.decode("utf-8", errors="replace")

        while "\n" in buffer:
            line, buffer = buffer.split("\n", 1)
            line = line.rstrip("\r")

            if not line.startswith("data:"):
                continue

            data = line[5:].strip()

            if not data or data == "[DONE]":
                continue

            try:
                yield json.loads(data)
            except json.JSONDecodeError:
                # Skip malformed JSON lines
                continue
