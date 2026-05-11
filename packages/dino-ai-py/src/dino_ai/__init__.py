"""dino-ai — Unified LLM API."""

# Built-in middleware
from dino_ai.builtin_middleware import CostGuardMiddleware, LoggingMiddleware, RetryMiddleware

# Core client
from dino_ai.catalog import ModelCatalog
from dino_ai.client import DinoClient

# Content blocks
from dino_ai.content import (
    ContentBlock,
    ImageContent,
    TextContent,
    ThinkingContent,
    ToolCall,
)

# Context and messages
from dino_ai.context import (
    AssistantMessage,
    Context,
    Message,
    StopReason,
    Tool,
    ToolResultMessage,
    UserMessage,
)

# Error model
from dino_ai.error import DinoError, DinoException, ErrorCategory

# Events
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

# Middleware
from dino_ai.middleware import Middleware, MiddlewareChain

# Model
from dino_ai.model import (
    Model,
    ModelCapabilities,
    ModelLimits,
    ModelPricing,
    ModelThinkingLevel,
    ThinkingLevel,
)

# Options
from dino_ai.options import SimpleStreamOptions, StreamOptions

# Provider
from dino_ai.providers import ProviderAdapter

# Stream
from dino_ai.stream import EventStream

# Tool decorator
from dino_ai.tool import tool

# Transformer
from dino_ai.transformer import transform_messages

# Usage
from dino_ai.usage import Cost, Usage

__all__ = [
    # Client
    "DinoClient",
    "ModelCatalog",
    # Content
    "ContentBlock",
    "ImageContent",
    "TextContent",
    "ThinkingContent",
    "ToolCall",
    # Context
    "AssistantMessage",
    "Context",
    "Message",
    "StopReason",
    "Tool",
    "ToolResultMessage",
    "UserMessage",
    # Error
    "DinoError",
    "DinoException",
    "ErrorCategory",
    # Events
    "AssistantMessageEvent",
    "StreamDone",
    "StreamError",
    "StreamStart",
    "TextDelta",
    "TextEnd",
    "TextStart",
    "ThinkingDelta",
    "ThinkingEnd",
    "ThinkingStart",
    "ToolCallDelta",
    "ToolCallEnd",
    "ToolCallStart",
    # Middleware
    "CostGuardMiddleware",
    "LoggingMiddleware",
    "Middleware",
    "MiddlewareChain",
    "RetryMiddleware",
    # Model
    "Model",
    "ModelCapabilities",
    "ModelLimits",
    "ModelPricing",
    "ModelThinkingLevel",
    "ThinkingLevel",
    # Options
    "SimpleStreamOptions",
    "StreamOptions",
    # Provider
    "ProviderAdapter",
    # Stream
    "EventStream",
    # Tool decorator
    "tool",
    # Transformer
    "transform_messages",
    # Usage
    "Cost",
    "Usage",
]
