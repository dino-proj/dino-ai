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

# Bump version, commit, tag, push. GitHub Actions publishes to PyPI.
# Usage: just release 0.2.1
release version:
    #!/usr/bin/env bash
    set -euo pipefail

    version="{{version}}"
    if [ -z "$version" ]; then echo "Usage: just release <version>"; exit 1; fi

    # ── Pre-checks ──
    if [ -n "$(git status --porcelain)" ]; then
        echo "ERROR: Working tree is not clean. Commit or stash changes first."
        exit 1
    fi

    current_branch=$(git branch --show-current)
    if [ "$current_branch" != "main" ]; then
        echo "ERROR: Must release from main branch (currently on '$current_branch')."
        exit 1
    fi

    git pull --rebase

    # ── Validate ──
    echo "Running full check (install + lint + typecheck + test)..."
    just check

    # ── Bump version ──
    sed -i '' "s/^version = \".*\"/version = \"$version\"/" packages/dino-ai-py/pyproject.toml

    # ── Update CHANGELOG ──
    today=$(date +%Y-%m-%d)
    # Replace "## [Unreleased]" with "## [Unreleased]\n\n## [version] - date"
    sed -i '' "s/^## \[Unreleased\]/## [Unreleased]\\
\\
## [$version] - $today/" CHANGELOG.md

    # ── Build (verify packaging) ──
    just build

    # ── Commit, tag, push ──
    git add packages/dino-ai-py/pyproject.toml CHANGELOG.md
    git commit -m "release: v$version"
    git tag "v$version"
    git push && git push --tags

    # ── Create GitHub Release ──
    # Extract release notes from CHANGELOG (content between this version and next heading)
    notes=$(sed -n "/^## \[$version\]/,/^## \[/{/^## \[/!p;}" CHANGELOG.md | sed '/^$/d')
    if [ -z "$notes" ]; then notes="Release v$version"; fi
    echo "$notes" | gh release create "v$version" --title "v$version" --notes-file -

    echo ""
    echo "Released v$version. GitHub Actions will publish to PyPI."
