# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- **发布流程改进** — `just release` 增加 git 状态检查、分支验证、自动运行完整测试、构建验证、GitHub Release 创建
- **AI 发布技能** — 新增 `.agents/skills/dino-ai-release/SKILL.md`，AI 可自主执行完整发布流程

## [0.2.0] - 2026-05-14

### Changed

- **模型目录自动生成** — 从手动维护的 17 个 YAML 文件切换为从 [models.dev](https://models.dev) API 自动拉取，模型数从 108 增至 822，覆盖 30+ 厂商
- **多文件拆分** — `models.py` 拆分为 `models/` 包，每个厂商独立文件（`_anthropic.py`, `_openai.py` 等），按需导入
- **API/URL 自动推导** — 从 models.dev 的 `npm` 和 `api` 字段自动推导协议类型和 base URL，不再手工维护
- **双协议支持** — 厂商支持多套 API 协议时自动生成多个变体（如 `xiaomi` + `xiaomi-anthropic`）

### Added

- 新增厂商：DeepSeek、OpenRouter、StepFun、Zhipu、Alibaba (DashScope)、Xiaomi/MiMo（含 Anthropic 协议变体）
- `HARDCODED_PROVIDERS` 机制用于 models.dev 未覆盖的额外协议变体
- `AGENTS.md` — AI 编码助手指令文件，加速 Agent 上手

### Removed

- **13 个手动维护的 YAML 文件** — `catalog/v1/` 中已被 models.dev 覆盖的厂商文件（anthropic、bedrock、deepseek、google、groq、kimi、minimax、mistral、openai、openrouter、stepfun、xai、zhipu），保留 4 个 models.dev 未覆盖的厂商（baichuan、doubao、mimo、qwen）

### Fixed

- `intro.svg` 标题从 "Dino Sql Builder" 修正为 "Dino AI"
- README 示例：修复 `model.pricing.input_per_million` → `model.pricing.input`，补充 `TextContent` 导入，更新模型常量名

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
