"""Error model with structured error categories."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ErrorCategory(Enum):
    """Machine-readable error classification."""

    CONTEXT_OVERFLOW = "context_overflow"
    RATE_LIMITED = "rate_limited"
    AUTH_FAILURE = "auth_failure"
    QUOTA_EXCEEDED = "quota_exceeded"
    INVALID_REQUEST = "invalid_request"
    MODEL_NOT_FOUND = "model_not_found"
    CONTENT_FILTERED = "content_filtered"
    NETWORK_ERROR = "network_error"
    SERVER_ERROR = "server_error"
    ABORTED = "aborted"
    PROVIDER_ERROR = "provider_error"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class DinoError:
    """Structured error returned by providers.

    Provider adapters are responsible for mapping native errors to this type.
    """

    category: ErrorCategory
    provider: str
    message: str
    retryable: bool = False
    status_code: int | None = None
    retry_after_ms: int | None = None
    raw: str | None = None


class DinoException(Exception):
    """Exception for truly exceptional failures (not API errors).

    API errors are represented as DinoError on AssistantMessage.
    This exception is for configuration errors, programming mistakes, etc.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
