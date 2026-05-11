# dino-ai task runner

# ── Catalog ──────────────────────────────────────────────────────

# Generate Python model constants from catalog/ YAML
generate-models:
    cd packages/dino-ai-py && uv run python scripts/generate_models.py

# ── Python ───────────────────────────────────────────────────────

install:
    cd packages/dino-ai-py && uv sync --all-extras

test: generate-models
    cd packages/dino-ai-py && uv run pytest

typecheck:
    cd packages/dino-ai-py && uv run mypy src/dino_ai

lint:
    cd packages/dino-ai-py && uv run ruff check src tests

check: lint typecheck test

build: generate-models
    cp README.md README.en.md packages/dino-ai-py/
    cd packages/dino-ai-py && uv build
    rm packages/dino-ai-py/README.md packages/dino-ai-py/README.en.md
