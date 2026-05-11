# dino-ai task runner

# ── Catalog ──────────────────────────────────────────────────────

# Generate Python model constants from catalog/ YAML
generate-models:
    cd packages/dino-ai-py && uv run --extra dev python scripts/generate_models.py

# ── Python ───────────────────────────────────────────────────────

# Copy root README into package dir (needed for editable install / build)
_copy-readme:
    cp -f README.md README.en.md packages/dino-ai-py/ 2>/dev/null || true

install: _copy-readme
    cd packages/dino-ai-py && uv sync --all-extras

test: generate-models
    cd packages/dino-ai-py && uv run pytest

typecheck:
    cd packages/dino-ai-py && uv run mypy src/dino_ai

lint:
    cd packages/dino-ai-py && uv run ruff check src tests

check: install lint typecheck test

build: _copy-readme generate-models
    cd packages/dino-ai-py && uv build

# ── Release ──────────────────────────────────────────────────────

# Bump version, commit, and tag. Usage: just release 0.2.0
release version:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ -z "{{version}}" ]; then echo "Usage: just release <version>"; exit 1; fi
    # Update pyproject.toml
    sed -i'' -e 's/^version = ".*"/version = "{{version}}"/' packages/dino-ai-py/pyproject.toml
    # Update CHANGELOG heading
    today=$(date +%Y-%m-%d)
    sed -i'' -e "s/^## \[Unreleased\]/## [Unreleased]\n\n## [{{version}}] - ${today}/" CHANGELOG.md
    git add packages/dino-ai-py/pyproject.toml CHANGELOG.md
    git commit -m "release: v{{version}}"
    git tag "v{{version}}"
    echo "Done. Run 'git push && git push --tags' to publish."
