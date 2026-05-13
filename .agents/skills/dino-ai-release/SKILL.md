---
name: dino-ai-release
version: 0.1.0
description: Release a new version of dino-ai Python SDK. Use when the user asks to release, publish, or bump the version of dino-ai.
requires:
  bins: ["just", "git", "uv"]
---

# dino-ai Release Skill

Execute a release of the dino-ai Python SDK package.

## Prerequisites

- Must be on `main` branch with clean working tree
- All changes for the release already merged and documented in CHANGELOG.md under `## [Unreleased]`

## Release Steps

### 1. Determine version number

Ask the user for the target version if not provided. Follow semver:
- Patch (0.2.0 → 0.2.1): bug fixes, new models, minor additions
- Minor (0.2.1 → 0.3.0): breaking API changes

Check current version:
```bash
grep '^version' packages/dino-ai-py/pyproject.toml
```

### 2. Review changes since last release

Get the diff between the last version tag and HEAD:
```bash
last_tag=$(git describe --tags --abbrev=0)
git log "$last_tag"..HEAD --oneline
git diff "$last_tag"..HEAD --stat
```

### 3. Update README files if needed

Compare README.md and README.en.md against actual code changes. Check for:
- **Model count** — if models were added/removed, update the "822 个预置模型" / "822 built-in models" number:
  ```bash
  # Count actual models
  grep -r "^[A-Z_]* = Model(" packages/dino-ai-py/src/dino_ai/models/ | wc -l
  ```
- **Provider count** — if providers were added/removed, update "30+ 厂商" / "30+ providers"
- **New features** — if new major features were added (new middleware, new content types, etc.), add them to the feature list in both README files
- **Install extras** — if new optional dependency groups were added, update the install examples

Make the same semantic changes in both README.md (Chinese) and README.en.md (English), keeping translations consistent.

### 4. Write CHANGELOG if empty

```bash
sed -n '/^## \[Unreleased\]/,/^## \[/p' CHANGELOG.md | head -30
```

If the `[Unreleased]` section has no content, **auto-generate it** from the git log:

1. Get commits since last tag:
   ```bash
   git log "$last_tag"..HEAD --oneline --no-merges
   ```
2. Read the actual diffs to understand what changed
3. Write a proper CHANGELOG section using these categories (only include sections with content):
   - `### Changed` — modifications to existing behavior
   - `### Added` — new features, providers, models
   - `### Fixed` — bug fixes
   - `### Removed` — removed features or files

Write entries in Chinese, matching the existing CHANGELOG style. Each entry should describe the user-visible impact, not the implementation detail.

### 5. Run the release

```bash
just release <version>
```

This single command will:
1. Verify clean git state and main branch
2. Pull latest changes
3. Run full check (install + lint + typecheck + test)
4. Bump version in `pyproject.toml`
5. Update CHANGELOG (`[Unreleased]` → `[version] - date`)
6. Build the package (verify it packages correctly)
7. Commit, tag, and push

GitHub Actions will then automatically publish to PyPI when it sees the `v*` tag.

**Important**: Steps 3-4 (README + CHANGELOG) must be committed BEFORE running `just release`, since the release command requires a clean working tree. Commit them with:
```bash
git add README.md README.en.md CHANGELOG.md
git commit -m "docs: prepare release v<version>"
```

### 6. Verify (optional)

```bash
# Check GitHub Actions status
gh run list --limit 3
```

## Error Recovery

| Error | Action |
|-------|--------|
| "Working tree is not clean" | Run `git status`, commit or stash pending changes |
| "Must release from main" | Switch to main: `git checkout main && git pull` |
| `just check` fails | Fix lint/type/test errors before retrying |
| Push rejected | `git pull --rebase` then `git push && git push --tags` |
| Tag already exists | Delete with `git tag -d v<ver>` and re-run |

## Post-Release

After GitHub Actions completes the publish:
- Verify on PyPI: https://pypi.org/project/dino-ai-py/
- The `[Unreleased]` section in CHANGELOG.md is ready for the next cycle
