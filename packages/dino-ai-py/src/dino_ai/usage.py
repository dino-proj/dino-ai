"""Usage and cost tracking."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Cost:
    """Cost breakdown in USD."""

    input: float = 0.0
    output: float = 0.0
    cache_read: float = 0.0
    cache_write: float = 0.0
    total: float = 0.0


@dataclass
class Usage:
    """Token usage and cost for a single response."""

    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    total_tokens: int = 0
    cost: Cost = field(default_factory=Cost)
