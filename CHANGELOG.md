# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-05-11

### Added

- `DinoClient` — instance-scoped entry point with `stream()`, `complete()`, `stream_simple()`, `complete_simple()`
- `EventStream` — async iterable event stream with `result()` for awaiting the final `AssistantMessage`
- 12 typed streaming events: `StreamStart`, `TextStart/Delta/End`, `ThinkingStart/Delta/End`, `ToolCallStart/Delta/End`, `StreamDone`, `StreamError`
- `Context`, `UserMessage`, `AssistantMessage`, `ToolResultMessage`, `Tool` message types
- `TextContent`, `ThinkingContent`, `ImageContent`, `ToolCall` content blocks
- `Model` with capabilities, limits, and pricing metadata
- `ModelCatalog` with 108 built-in models from YAML catalog (17 providers)
- `StreamOptions` and `SimpleStreamOptions` with unified `ThinkingLevel` abstraction
- `DinoError` with 12 `ErrorCategory` variants for structured error handling
- `@tool` decorator for auto-generating `Tool` from function type annotations
- `transform_messages()` for cross-provider context handoff
- `OpenAICompletionsProvider` with `OpenAICompatProfile` supporting OpenAI, DeepSeek, Groq, xAI, Mistral, Together, OpenRouter, Baichuan, Doubao, Kimi, Qwen, StepFun, Zhipu, MiniMax, MiMo
- `AnthropicProvider` with native Messages API, cache control, and thinking support
- `GoogleProvider` with Generative AI streaming, thinking budgets, and function calling
- `BedrockProvider` with Converse Stream API via boto3, reasoning content, and tool use
- `AzureOpenAIProvider` with Azure-specific URL routing and `api-key` authentication
- `LoggingMiddleware`, `RetryMiddleware`, `CostGuardMiddleware` built-in middleware
- `Middleware` protocol for custom middleware
- JSON repair utilities (`repair_json`, `parse_streaming_json`)
- Unicode surrogate sanitization (`sanitize_surrogates`)
- Full `py.typed` support with mypy strict compliance
