# dino-ai

Unified Python LLM API. Multi-provider, middleware pipeline, async-first, zero required dependencies.

[中文文档](README.md)

## Features

- **Unified interface** — One API for OpenAI, Anthropic, Google Gemini, AWS Bedrock, Mistral, DeepSeek, xAI, and 17+ providers
- **108 built-in models** — Auto-generated from YAML catalog, ready to use
- **Streaming events** — Async iterator yielding text, thinking, and tool call blocks
- **Middleware pipeline** — Logging, retry, cost guard — composable and extensible
- **Structured errors** — 12 `ErrorCategory` variants for rate limits, context overflow, etc.
- **Cross-provider context handoff** — Seamlessly continue conversations across different models
- **`@tool` decorator** — Auto-generate JSON Schema from type annotations
- **Zero required dependencies** — `httpx` / `boto3` lazy-imported on demand
- **Fully typed** — `py.typed` + mypy strict

## Installation

```bash
pip install dino-ai-py
```

Install optional dependencies per provider:

```bash
pip install "dino-ai-py[openai]"      # OpenAI / DeepSeek / Groq / xAI / Together / Mistral etc.
pip install "dino-ai-py[anthropic]"   # Anthropic Claude
pip install "dino-ai-py[google]"      # Google Gemini
pip install "dino-ai-py[bedrock]"     # AWS Bedrock (boto3)
pip install "dino-ai-py[all]"         # Everything
```

## Quick Start

```python
import asyncio
from dino_ai import DinoClient, Context, UserMessage
from dino_ai.providers.openai_completions import OpenAICompletionsProvider
from dino_ai.providers.anthropic import AnthropicProvider

client = DinoClient(providers=[
    OpenAICompletionsProvider(),
    AnthropicProvider(),
])

async def main():
    context = Context(messages=[UserMessage(content="Explain quantum entanglement in one sentence")])

    # Option 1: Await the full response
    message = await client.complete("gpt-4o", context)
    print(message.text)

    # Option 2: Stream events
    stream = client.stream("claude-sonnet-4-20250514", context)
    async for event in stream:
        print(event)

asyncio.run(main())
```

## Core Concepts

### Models

108 model constants grouped by provider:

```python
from dino_ai.models import Openai, Anthropic, Google

model = Openai.GPT_4O               # gpt-4o
model = Anthropic.CLAUDE_SONNET_4    # claude-sonnet-4-20250514
model = Google.GEMINI_2_5_PRO        # gemini-2.5-pro

# Or use strings directly
message = await client.complete("gpt-4o", context)
```

Each `Model` carries capability declarations, context window size, pricing, and more:

```python
model = Openai.GPT_4O
print(model.capabilities.vision)       # True
print(model.limits.context_window)     # 128000
print(model.pricing.input_per_million) # 2.5
```

### Context and Messages

```python
from dino_ai import Context, UserMessage, AssistantMessage, ToolResultMessage, Tool

# Simple conversation
context = Context(
    system_prompt="You are a helpful translator.",
    messages=[UserMessage(content="Translate 'hello' to Japanese")],
)

# Multi-turn
context = Context(messages=[
    UserMessage(content="What is 2+2?"),
    AssistantMessage(content=[TextContent(text="4")]),
    UserMessage(content="And 3+3?"),
])

# With tools
context = Context(
    messages=[UserMessage(content="What's the weather in Tokyo?")],
    tools=[
        Tool(name="get_weather", description="Get weather for a city",
             parameters={"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}),
    ],
)
```

### Streaming Events

`stream()` returns an `EventStream` — an async iterable of typed events:

| Event | Description |
|-------|-------------|
| `StreamStart` | Stream started |
| `TextStart` / `TextDelta` / `TextEnd` | Text content block |
| `ThinkingStart` / `ThinkingDelta` / `ThinkingEnd` | Thinking/reasoning block |
| `ToolCallStart` / `ToolCallDelta` / `ToolCallEnd` | Tool call block |
| `StreamDone` | Stream complete, carries final `AssistantMessage` |
| `StreamError` | Stream error, carries `DinoError` |

```python
stream = client.stream(model, context)
async for event in stream:
    match event:
        case TextDelta(text=t):
            print(t, end="", flush=True)
        case ToolCallEnd(tool_call=tc):
            print(f"\nTool call: {tc.name}({tc.arguments})")
        case StreamDone(message=msg):
            print(f"\nUsage: {msg.usage}")

# Or await the final result directly
message = await stream.result()
```

### `@tool` Decorator

Auto-generate `Tool` objects from function signatures:

```python
from dino_ai import tool
from typing import Annotated

@tool
def get_weather(
    city: Annotated[str, "City name"],
    units: Annotated[str, "Temperature units"] = "celsius",
) -> str:
    """Get the current weather for a city."""
    return f"{city}: 25 {units}"

t = get_weather.as_tool()
# Tool(name="get_weather", description="Get the current weather for a city.", parameters={...})
```

### Middleware

Middleware intercepts requests and can be composed freely:

```python
from dino_ai import DinoClient, LoggingMiddleware, RetryMiddleware, CostGuardMiddleware

client = DinoClient(
    providers=[...],
    middleware=[
        LoggingMiddleware(),                         # Log requests
        RetryMiddleware(max_retries=3),              # Auto-retry on retryable errors
        CostGuardMiddleware(max_cost_usd=1.0),       # Reject requests over cumulative cost limit
    ],
)
```

Custom middleware implements the `Middleware` protocol:

```python
from dino_ai import Middleware, MiddlewareChain, EventStream, Model, Context, StreamOptions

class TimingMiddleware:
    def intercept(
        self,
        model: Model,
        context: Context,
        options: StreamOptions | None,
        chain: MiddlewareChain,
    ) -> EventStream:
        import time
        start = time.monotonic()
        stream = chain(model, context, options)
        from dino_ai.builtin_middleware import _wrap_stream
        return _wrap_stream(stream, on_done=lambda e: print(f"Elapsed: {time.monotonic() - start:.2f}s"))
```

### Structured Errors

All provider errors are mapped to `DinoError`:

```python
from dino_ai import ErrorCategory

stream = client.stream(model, context)
message = await stream.result()

if message.error:
    match message.error.category:
        case ErrorCategory.RATE_LIMITED:
            print(f"Rate limited, retry after {message.error.retry_after_ms}ms")
        case ErrorCategory.CONTEXT_OVERFLOW:
            print("Context too long, truncation needed")
        case ErrorCategory.AUTH_FAILURE:
            print("Invalid API key")
        case _:
            print(f"Error: {message.error.message}")
```

12 error categories: `CONTEXT_OVERFLOW` · `RATE_LIMITED` · `AUTH_FAILURE` · `QUOTA_EXCEEDED` · `INVALID_REQUEST` · `MODEL_NOT_FOUND` · `CONTENT_FILTERED` · `NETWORK_ERROR` · `SERVER_ERROR` · `ABORTED` · `PROVIDER_ERROR` · `UNKNOWN`

### Cross-Provider Context Handoff

Use `transform_messages()` to transfer conversation history between providers:

```python
from dino_ai import transform_messages

message = await client.complete("gpt-4o", context)
context.messages.append(message)
context.messages.append(UserMessage(content="Continue"))

# Seamlessly switch to Claude
# transform_messages handles thinking block format differences automatically
message = await client.complete("claude-sonnet-4-20250514", context)
```

### SimpleStream — Unified Reasoning Levels

Different providers use different thinking/reasoning parameters. `stream_simple()` provides a unified `ThinkingLevel` abstraction:

```python
from dino_ai import SimpleStreamOptions, ThinkingLevel

options = SimpleStreamOptions(reasoning=ThinkingLevel.HIGH)

# Same code, different models — automatically adapted
await client.complete_simple("o3-mini", context, options)          # OpenAI reasoning_effort
await client.complete_simple("claude-sonnet-4-20250514", context, options)  # Anthropic budget_tokens
await client.complete_simple("gemini-2.5-pro", context, options)   # Google thinking budget
```

## Supported Providers

| Provider | API Type | Provider Class |
|----------|----------|----------------|
| OpenAI | `openai-completions` | `OpenAICompletionsProvider` |
| Anthropic | `anthropic-messages` | `AnthropicProvider` |
| Google Gemini | `google-generative-ai` | `GoogleProvider` |
| AWS Bedrock | `bedrock-converse-stream` | `BedrockProvider` |
| Azure OpenAI | `azure-openai` | `AzureOpenAIProvider` |
| DeepSeek | `openai-completions` | `OpenAICompletionsProvider` |
| Groq | `openai-completions` | `OpenAICompletionsProvider` |
| xAI (Grok) | `openai-completions` | `OpenAICompletionsProvider` |
| Mistral | `openai-completions` | `OpenAICompletionsProvider` |
| Together | `openai-completions` | `OpenAICompletionsProvider` |
| OpenRouter | `openai-completions` | `OpenAICompletionsProvider` |
| Baichuan | `openai-completions` | `OpenAICompletionsProvider` |
| Doubao | `openai-completions` | `OpenAICompletionsProvider` |
| Kimi | `openai-completions` | `OpenAICompletionsProvider` |
| Qwen | `openai-completions` | `OpenAICompletionsProvider` |
| StepFun | `openai-completions` | `OpenAICompletionsProvider` |
| Zhipu | `openai-completions` | `OpenAICompletionsProvider` |
| MiniMax | `openai-completions` | `OpenAICompletionsProvider` |
| MiMo | `openai-completions` | `OpenAICompletionsProvider` |

OpenAI-compatible providers share `OpenAICompletionsProvider`, with `OpenAICompatProfile` auto-adapting per-provider differences (thinking format, max_tokens field name, usage reporting, etc.).

## Environment Variables

Provider API keys via environment variables, or pass them in `StreamOptions.api_key`:

```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AIza...
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...
AWS_REGION=us-east-1
AZURE_OPENAI_API_KEY=...
DEEPSEEK_API_KEY=...
XAI_API_KEY=...
GROQ_API_KEY=...
MISTRAL_API_KEY=...
TOGETHER_API_KEY=...
OPENROUTER_API_KEY=...
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Type checking
mypy src/dino_ai

# Lint
ruff check src/ tests/
```

## License

[Apache-2.0](../../LICENSE)
