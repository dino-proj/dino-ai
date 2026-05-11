# dino-ai monorepo task runner

# ── Catalog ──────────────────────────────────────────────────────

# Generate Python model constants from catalog/ YAML
py-generate-models:
    cd packages/dino-ai-py && uv run python scripts/generate_models.py

# Copy shared catalog into Java core resources
catalog-copy-java:
    rm -rf packages/dino-ai-java/core/src/main/resources/catalog
    mkdir -p packages/dino-ai-java/core/src/main/resources
    cp -r catalog packages/dino-ai-java/core/src/main/resources/catalog

# ── Python ───────────────────────────────────────────────────────

py-install:
    cd packages/dino-ai-py && uv sync --all-extras

py-test: py-generate-models
    cd packages/dino-ai-py && uv run pytest

py-typecheck:
    cd packages/dino-ai-py && uv run mypy src/dino_ai

py-lint:
    cd packages/dino-ai-py && uv run ruff check src tests

py-check: py-lint py-typecheck py-test

py-build: py-generate-models
    cp README.md README.en.md packages/dino-ai-py/
    cd packages/dino-ai-py && uv build
    rm packages/dino-ai-py/README.md packages/dino-ai-py/README.en.md

# ── Java ─────────────────────────────────────────────────────────

java-test: catalog-copy-java
    cd packages/dino-ai-java && ./gradlew test

java-check: catalog-copy-java
    cd packages/dino-ai-java && ./gradlew check

# ── All ──────────────────────────────────────────────────────────

test: py-test java-test
check: py-check java-check
