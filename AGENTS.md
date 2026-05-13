# dino-ai — Agent Instructions

## Project Overview

dino-ai is a zero-dependency Python 3.10+ unified LLM API with 30+ providers, middleware pipeline, and async-first streaming. See [README](README.md) and [DESIGN](DESIGN.md) for the full picture.

## Commands

All commands run from `packages/dino-ai-py/`. Use `just` (task runner) or direct commands:

| Task | Command |
|------|---------|
| Install deps | `just install` (or `uv sync --all-extras`) |
| Generate models | `just generate-models` (or `.venv/bin/python scripts/generate_models.py`) |
| Run tests | `just test` (or `.venv/bin/python -m pytest tests/`) |
| Type check | `just typecheck` (or `.venv/bin/python -m mypy src/dino_ai`) |
| Lint | `just lint` (or `.venv/bin/ruff check src/ tests/`) |
| Full check | `just check` (install → lint → typecheck → test) |

**Always use `.venv/bin/python`, not system `python3`.** The venv has PyYAML (for model generation) and all dev deps.

**After modifying code (not docs), run `just lint`**. If you modify `scripts/generate_models.py` or catalog YAML files, re-run `just generate-models` before testing.

## Architecture

```
src/dino_ai/
  client.py           # DinoClient — holds providers + middleware chain
  model.py            # Model dataclass (id, name, api, provider, capabilities, limits, pricing)
  context.py          # Context + message types (UserMessage, AssistantMessage, ToolResultMessage)
  content.py          # Content blocks (TextContent, ThinkingContent, ImageContent, ToolCall)
  catalog.py          # ModelCatalog — in-memory registry, loads from generated models/
  stream.py           # EventStream — async iterable + awaitable
  events.py           # 12 streaming event types (StreamStart, TextDelta, ToolCallEnd, etc.)
  error.py            # DinoError + 12 ErrorCategory enums
  options.py          # StreamOptions, SimpleStreamOptions, ThinkingLevel
  middleware.py        # Middleware protocol + chain
  transformer.py       # Cross-provider message normalization
  tool.py             # @tool decorator
  builtin_middleware.py # LoggingMiddleware, RetryMiddleware, CostGuardMiddleware
  providers/          # Provider adapters (openai_completions, anthropic, google, bedrock, etc.)
  models/             # GENERATED — provider model constants (36 files, ~823 models)
```

## Key Conventions

- **All type annotations required** — mypy strict mode, target Python 3.10
- **`from __future__ import annotations`** in every file with types
- **No `any` types** — use `object` or `typing.Protocol` when truly dynamic
- **Immutability** — domain types are `@dataclass(frozen=True)`
- **Zero mandatory deps** — `httpx`/`boto3`/provider SDKs imported lazily in provider constructors
- **Line length**: 120 characters (ruff)
- **No inline/dynamic imports** — all imports at top of file
- **Private internals**: underscore prefix (`_private_func`)

## Adding a Provider

See [DESIGN.md](DESIGN.md) for the full provider interface. Quick checklist:

1. Create `src/dino_ai/providers/<name>.py` implementing `ProviderAdapter` protocol
2. `stream()` returns `EventStream` (use `new_event_stream()` factory)
3. Parse streaming API responses → push typed events
4. Build `AssistantMessage` incrementally
5. Finalize with `stream.end(msg)` (success) or `stream.push(StreamError(...))` (failure)
6. Add to `DinoClient.__init__` provider list
7. Lazy-import any provider SDK in `__init__`

## Model Catalog

Models are auto-generated from [models.dev](https://models.dev) API. Do NOT edit files in `src/dino_ai/models/` or `catalog/v1/` directly.

- **To add a models.dev-covered provider**: add an entry to `PROVIDER_MAP` in `scripts/generate_models.py`
- **To add a provider NOT in models.dev**: create a YAML file in `catalog/v1/`
- **To add an alternate API protocol variant**: add an entry to `HARDCODED_PROVIDERS` in `scripts/generate_models.py`
- After any change: run `just generate-models` then `just test`

## Testing

- Tests in `tests/`, grouped by concern: `test_catalog.py`, `test_openai_completions.py`, etc.
- Uses `tests/conftest.py` for shared fixtures
- `EventStream` tests use providers/fixtures that return deterministic streams
- All tests must pass: `just test`

## Common Pitfalls

- **Don't add deps to required**: keep `dependencies = []` in pyproject.toml; move to `[project.optional-dependencies]`
- **Don't hardcode API keys**: use env vars with `os.environ.get()` pattern
- **Streaming is complex**: the `EventStream` has both async-iterable and awaitable interfaces — use factories, not manual construction
- **Model constant names**: follow `UPPER_SNAKE_CASE` generated from `_to_identifier()` in the generator script
