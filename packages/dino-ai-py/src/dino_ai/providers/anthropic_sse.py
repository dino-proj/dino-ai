"""Server-Sent Events parser for Anthropic Messages API streaming.

Anthropic uses typed SSE events (event: + data: pairs), unlike OpenAI
which only uses data: lines. This parser yields (event_type, data) tuples.
"""

from __future__ import annotations

import json
from collections.abc import AsyncIterator
from typing import Any


async def parse_anthropic_sse(
    byte_stream: AsyncIterator[bytes],
) -> AsyncIterator[tuple[str, dict[str, Any]]]:
    """Parse an Anthropic SSE byte stream into (event_type, data) tuples.

    Anthropic format::

        event: message_start
        data: {"type": "message_start", "message": {...}}

        event: content_block_delta
        data: {"type": "content_block_delta", "index": 0, "delta": {...}}

    Yields:
        Tuples of (event_type, parsed_data_dict).
    """
    buffer = ""
    current_event: str | None = None

    async for raw_chunk in byte_stream:
        buffer += raw_chunk.decode("utf-8", errors="replace")

        while "\n" in buffer:
            line, buffer = buffer.split("\n", 1)
            line = line.rstrip("\r")

            if not line:
                # Empty line = end of event block
                current_event = None
                continue

            if line.startswith("event:"):
                current_event = line[6:].strip()
                continue

            if line.startswith("data:"):
                data_str = line[5:].strip()
                if not data_str:
                    continue

                event_type = current_event or "unknown"

                try:
                    data = json.loads(data_str)
                    yield event_type, data
                except json.JSONDecodeError:
                    # For error events, yield the raw string wrapped in a dict
                    yield event_type, {"raw": data_str}
                continue
