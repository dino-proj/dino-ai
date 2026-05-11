# dino-ai

统一的 Python LLM API。多厂商、中间件管道、异步优先、零必选依赖。

[English](README.en.md)

## 特性

- **统一接口** — 一套 API 调用 OpenAI、Anthropic、Google Gemini、AWS Bedrock、Mistral、DeepSeek、xAI 等 17 家厂商
- **108 个预置模型** — YAML 目录自动生成，开箱即用
- **流式事件** — 异步迭代器逐块返回文本、思维链、工具调用
- **中间件管道** — 日志、重试、费用上限，可自由组合或自定义
- **结构化错误** — 12 种 `ErrorCategory`，统一处理速率限制、上下文溢出等
- **跨厂商上下文传递** — 在不同模型之间无缝切换对话
- **`@tool` 装饰器** — 从类型标注自动生成 JSON Schema
- **零必选依赖** — `httpx` / `boto3` 按需懒加载
- **完整类型标注** — `py.typed` + mypy strict 通过

## 安装

```bash
pip install dino-ai
```

按厂商安装可选依赖：

```bash
pip install "dino-ai[openai]"      # OpenAI / DeepSeek / Groq / xAI / Together / Mistral 等
pip install "dino-ai[anthropic]"   # Anthropic Claude
pip install "dino-ai[google]"      # Google Gemini
pip install "dino-ai[bedrock]"     # AWS Bedrock (boto3)
pip install "dino-ai[all]"         # 全部
```

## 快速开始

```python
import asyncio
from dino_ai import DinoClient, Context, UserMessage
from dino_ai.providers.openai_completions import OpenAICompletionsProvider
from dino_ai.providers.anthropic import AnthropicProvider

# 创建客户端，注册你需要的厂商
client = DinoClient(providers=[
    OpenAICompletionsProvider(),
    AnthropicProvider(),
])

async def main():
    context = Context(messages=[UserMessage(content="用一句话解释量子纠缠")])

    # 方式 1: 直接 await 获取完整回复
    message = await client.complete("gpt-4o", context)
    print(message.text)

    # 方式 2: 流式逐块接收
    stream = client.stream("claude-sonnet-4-20250514", context)
    async for event in stream:
        print(event)

asyncio.run(main())
```

## 核心概念

### 模型

108 个模型常量，按厂商分组：

```python
from dino_ai.models import Openai, Anthropic, Google

model = Openai.GPT_4O               # gpt-4o
model = Anthropic.CLAUDE_SONNET_4    # claude-sonnet-4-20250514
model = Google.GEMINI_2_5_PRO        # gemini-2.5-pro

# 也可以直接用字符串
message = await client.complete("gpt-4o", context)
```

每个 `Model` 包含能力声明、上下文窗口、定价等元信息：

```python
model = Openai.GPT_4O
print(model.capabilities.vision)       # True
print(model.limits.context_window)     # 128000
print(model.pricing.input_per_million) # 2.5
```

### 上下文与消息

```python
from dino_ai import Context, UserMessage, AssistantMessage, ToolResultMessage, Tool

# 简单对话
context = Context(
    system_prompt="你是一个翻译助手。",
    messages=[UserMessage(content="Translate 'hello' to Japanese")],
)

# 多轮对话
context = Context(messages=[
    UserMessage(content="What is 2+2?"),
    AssistantMessage(content=[TextContent(text="4")]),
    UserMessage(content="And 3+3?"),
])

# 带工具定义
context = Context(
    messages=[UserMessage(content="What's the weather in Tokyo?")],
    tools=[
        Tool(name="get_weather", description="Get weather for a city",
             parameters={"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}),
    ],
)
```

### 流式事件

`stream()` 返回 `EventStream`，可异步迭代，事件类型包括：

| 事件 | 说明 |
|------|------|
| `StreamStart` | 流开始 |
| `TextStart` / `TextDelta` / `TextEnd` | 文本内容块 |
| `ThinkingStart` / `ThinkingDelta` / `ThinkingEnd` | 思维链/推理 |
| `ToolCallStart` / `ToolCallDelta` / `ToolCallEnd` | 工具调用 |
| `StreamDone` | 流完成，携带最终 `AssistantMessage` |
| `StreamError` | 流错误，携带 `DinoError` |

```python
stream = client.stream(model, context)
async for event in stream:
    match event:
        case TextDelta(text=t):
            print(t, end="", flush=True)
        case ToolCallEnd(tool_call=tc):
            print(f"\n工具调用: {tc.name}({tc.arguments})")
        case StreamDone(message=msg):
            print(f"\n用量: {msg.usage}")

# 或直接等待最终结果
message = await stream.result()
```

### `@tool` 装饰器

从函数签名自动生成 `Tool` 对象：

```python
from dino_ai import tool
from typing import Annotated

@tool
def get_weather(
    city: Annotated[str, "城市名"],
    units: Annotated[str, "温度单位"] = "celsius",
) -> str:
    """获取指定城市的天气。"""
    return f"{city}: 25 {units}"

# 生成 Tool 对象用于 Context
t = get_weather.as_tool()
# Tool(name="get_weather", description="获取指定城市的天气。", parameters={...})
```

### 中间件

中间件在请求前后拦截，可组合使用：

```python
from dino_ai import DinoClient, LoggingMiddleware, RetryMiddleware, CostGuardMiddleware

client = DinoClient(
    providers=[...],
    middleware=[
        LoggingMiddleware(),                         # 记录请求日志
        RetryMiddleware(max_retries=3),              # 可重试错误自动重试
        CostGuardMiddleware(max_cost_usd=1.0),       # 累计费用超限后拒绝请求
    ],
)
```

自定义中间件实现 `Middleware` 协议：

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
        return _wrap_stream(stream, on_done=lambda e: print(f"耗时: {time.monotonic() - start:.2f}s"))
```

### 结构化错误

所有厂商错误统一映射为 `DinoError`：

```python
from dino_ai import ErrorCategory

stream = client.stream(model, context)
message = await stream.result()

if message.error:
    match message.error.category:
        case ErrorCategory.RATE_LIMITED:
            print(f"被限流，{message.error.retry_after_ms}ms 后重试")
        case ErrorCategory.CONTEXT_OVERFLOW:
            print("上下文太长，需要截断")
        case ErrorCategory.AUTH_FAILURE:
            print("API key 无效")
        case _:
            print(f"错误: {message.error.message}")
```

12 种错误类别：`CONTEXT_OVERFLOW` · `RATE_LIMITED` · `AUTH_FAILURE` · `QUOTA_EXCEEDED` · `INVALID_REQUEST` · `MODEL_NOT_FOUND` · `CONTENT_FILTERED` · `NETWORK_ERROR` · `SERVER_ERROR` · `ABORTED` · `PROVIDER_ERROR` · `UNKNOWN`

### 跨厂商上下文传递

使用 `transform_messages()` 在不同厂商之间转移对话历史：

```python
from dino_ai import transform_messages

# OpenAI 模型生成的回复（可能含 thinking block）
message = await client.complete("gpt-4o", context)
context.messages.append(message)
context.messages.append(UserMessage(content="继续"))

# 无缝切换到 Claude 继续对话
# transform_messages 自动处理 thinking block 格式差异
message = await client.complete("claude-sonnet-4-20250514", context)
```

### SimpleStream — 统一推理级别

不同厂商的 thinking/reasoning 参数各不相同。`stream_simple()` 提供统一的 `ThinkingLevel` 抽象：

```python
from dino_ai import SimpleStreamOptions, ThinkingLevel

# 用统一的方式请求推理
options = SimpleStreamOptions(reasoning=ThinkingLevel.HIGH)

# 同一套代码，不同模型自动适配
await client.complete_simple("o3-mini", context, options)          # OpenAI reasoning_effort
await client.complete_simple("claude-sonnet-4-20250514", context, options)  # Anthropic budget_tokens
await client.complete_simple("gemini-2.5-pro", context, options)   # Google thinking budget
```

## 支持的厂商

| 厂商 | API 类型 | Provider 类 |
|------|----------|-------------|
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
| 百川 | `openai-completions` | `OpenAICompletionsProvider` |
| 豆包 | `openai-completions` | `OpenAICompletionsProvider` |
| Kimi | `openai-completions` | `OpenAICompletionsProvider` |
| 通义千问 | `openai-completions` | `OpenAICompletionsProvider` |
| 阶跃星辰 | `openai-completions` | `OpenAICompletionsProvider` |
| 智谱 | `openai-completions` | `OpenAICompletionsProvider` |
| MiniMax | `openai-completions` | `OpenAICompletionsProvider` |
| MiMo | `openai-completions` | `OpenAICompletionsProvider` |

OpenAI 兼容的厂商共用 `OpenAICompletionsProvider`，通过 `OpenAICompatProfile` 自动适配各家差异（thinking 格式、max_tokens 字段名、usage 上报等）。

## 环境变量

各厂商的 API key 通过环境变量配置，也可在 `StreamOptions.api_key` 中传入：

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

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 类型检查
mypy src/dino_ai

# 代码风格
ruff check src/ tests/
```

## 许可证

[Apache-2.0](../../LICENSE)
