#!/usr/bin/env python3
"""Generate models.py from models.dev API + catalog YAML fallback.

Usage:
    python scripts/generate_models.py

Primary source: https://models.dev/api.json (community-maintained model registry).
Fallback: YAML files in catalog/v1/ for providers not covered by models.dev.

Produces src/dino_ai/models.py with typed Model constants grouped by provider.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.request import Request, urlopen

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CATALOG_DIR = REPO_ROOT / "catalog" / "v1"
MODELS_DIR = Path(__file__).resolve().parent.parent / "src" / "dino_ai" / "models"
# Old single-file output — remove if exists
OLD_OUTPUT = Path(__file__).resolve().parent.parent / "src" / "dino_ai" / "models.py"

MODELS_DEV_URL = "https://models.dev/api.json"

# ---------------------------------------------------------------------------
# npm → API protocol mapping (derived from models.dev provider metadata)
# ---------------------------------------------------------------------------
NPM_TO_API: dict[str, str] = {
    "@ai-sdk/anthropic": "anthropic-messages",
    "@ai-sdk/openai": "openai-completions",
    "@ai-sdk/openai-compatible": "openai-completions",
    "@ai-sdk/google": "google-generative-ai",
    "@ai-sdk/google-vertex": "google-vertex",
    "@ai-sdk/google-vertex/anthropic": "anthropic-messages",
    "@ai-sdk/mistral": "mistral-conversations",
    "@ai-sdk/amazon-bedrock": "bedrock-converse-stream",
    "@ai-sdk/cohere": "openai-completions",
    "@ai-sdk/cerebras": "openai-completions",
    "@ai-sdk/groq": "openai-completions",
    "@ai-sdk/xai": "openai-completions",
    "@ai-sdk/deepinfra": "openai-completions",
    "@ai-sdk/togetherai": "openai-completions",
    "@ai-sdk/azure": "azure-openai-responses",
    "@ai-sdk/vercel": "openai-completions",
    "@openrouter/ai-sdk-provider": "openai-completions",
    "ai-gateway-provider": "openai-completions",
    "gitlab-ai-provider": "openai-completions",
    "venice-ai-sdk-provider": "openai-completions",
    "@aihubmix/ai-sdk-provider": "openai-completions",
    "@jerome-benoit/sap-ai-provider-v2": "openai-completions",
}

# ---------------------------------------------------------------------------
# Provider mapping: models.dev key → dino-ai provider name
# API type and base URL are auto-derived from models.dev metadata.
# ---------------------------------------------------------------------------
PROVIDER_MAP: dict[str, str] = {
    "anthropic": "anthropic",
    "openai": "openai",
    "google": "google",
    "google-vertex": "google-vertex",
    "groq": "groq",
    "cerebras": "cerebras",
    "xai": "xai",
    "mistral": "mistral",
    "amazon-bedrock": "amazon-bedrock",
    "fireworks-ai": "fireworks",
    "togetherai": "together",
    "huggingface": "huggingface",
    "minimax": "minimax",
    "minimax-cn": "minimax-cn",
    "moonshotai": "moonshotai",
    "moonshotai-cn": "moonshotai-cn",
    "xiaomi": "xiaomi",
    "xiaomi-token-plan-cn": "xiaomi-token-plan-cn",
    "xiaomi-token-plan-ams": "xiaomi-token-plan-ams",
    "xiaomi-token-plan-sgp": "xiaomi-token-plan-sgp",
    "kimi-for-coding": "kimi",
    "cloudflare-workers-ai": "cloudflare-workers-ai",
    "opencode": "opencode",
    "opencode-go": "opencode-go",
    "github-copilot": "github-copilot",
    "zai-coding-plan": "zhipu",
    "zhipuai": "zhipu",
    "deepseek": "deepseek",
    "openrouter": "openrouter",
    "stepfun": "stepfun",
    "alibaba": "alibaba",
    "alibaba-cn": "alibaba-cn",
}

# Providers covered by models.dev — these YAML files are NOT needed as fallback
MODELS_DEV_COVERED = frozenset(PROVIDER_MAP.keys())

# dino-ai provider names covered by models.dev (used to skip YAML fallback)
_MODELS_DEV_DINO_NAMES = frozenset(PROVIDER_MAP.values())

# ---------------------------------------------------------------------------
# Hardcoded providers — additional protocol variants not in models.dev.
# Each entry borrows model list from a models.dev source but overrides API/URL.
# ---------------------------------------------------------------------------
HARDCODED_PROVIDERS: list[dict] = [
    {
        "dino_provider": "xiaomi-anthropic",
        "api": "anthropic-messages",
        "base_url": "https://api.xiaomimimo.com/anthropic",
        "source_dev_key": "xiaomi",
    },
    {
        "dino_provider": "xiaomi-token-plan-cn-anthropic",
        "api": "anthropic-messages",
        "base_url": "https://token-plan-cn.xiaomimimo.com/anthropic",
        "source_dev_key": "xiaomi-token-plan-cn",
    },
    {
        "dino_provider": "xiaomi-token-plan-ams-anthropic",
        "api": "anthropic-messages",
        "base_url": "https://token-plan-ams.xiaomimimo.com/anthropic",
        "source_dev_key": "xiaomi-token-plan-ams",
    },
    {
        "dino_provider": "xiaomi-token-plan-sgp-anthropic",
        "api": "anthropic-messages",
        "base_url": "https://token-plan-sgp.xiaomimimo.com/anthropic",
        "source_dev_key": "xiaomi-token-plan-sgp",
    },
]

# ---------------------------------------------------------------------------
# Thinking level inference
# ---------------------------------------------------------------------------
DEFAULT_THINKING_LEVELS: tuple[str, ...] = (
    "off",
    "low",
    "medium",
    "high",
)
NO_THINKING_LEVELS: tuple[str, ...] = ()

PROVIDER_FILE_HEADER = '''\
"""Auto-generated models for {provider}.

DO NOT EDIT — run `python scripts/generate_models.py` to regenerate.
"""

from __future__ import annotations

from dino_ai.model import (
    Model,
    ModelCapabilities,
    ModelLimits,
    ModelPricing,
    ModelThinkingLevel,
)
'''

INIT_HEADER = '''\
"""Auto-generated model catalog.

DO NOT EDIT — run `python scripts/generate_models.py` to regenerate.
"""

from __future__ import annotations

from dino_ai.model import Model
'''


def _to_identifier(s: str) -> str:
    """Convert model id to a valid Python identifier (UPPER_SNAKE_CASE)."""
    s = s.replace("/", "__").replace(".", "_").replace("-", "_").replace(":", "_")
    s = re.sub(r"[^a-zA-Z0-9_]", "_", s)
    s = s.strip("_").upper()
    if s and s[0].isdigit():
        s = "M_" + s
    return s


def _to_class_name(provider: str) -> str:
    """Convert provider name to PascalCase class name."""
    parts = provider.replace("-", "_").split("_")
    return "".join(p.capitalize() for p in parts)


def _safe_filename(provider: str) -> str:
    """Convert provider name to a safe Python module filename."""
    return f"_{provider.replace('-', '_')}.py"


def _format_thinking_levels(levels: tuple[str, ...] | None, indent: int = 12) -> str:
    if not levels:
        return "()"
    mapping = {
        "off": "ModelThinkingLevel.OFF",
        "minimal": "ModelThinkingLevel.MINIMAL",
        "low": "ModelThinkingLevel.LOW",
        "medium": "ModelThinkingLevel.MEDIUM",
        "high": "ModelThinkingLevel.HIGH",
        "xhigh": "ModelThinkingLevel.XHIGH",
    }
    items = [mapping[l] for l in levels if l in mapping]
    single = "(" + ", ".join(items) + ",)"
    if indent + len("supported_thinking_levels=") + len(single) + 1 <= 120:
        return single
    pad = " " * indent
    inner = (",\n" + pad + "    ").join(items)
    return "(\n" + pad + "    " + inner + ",\n" + pad + ")"


def _fmt_float(v: float) -> str:
    """Format a float, stripping trailing zeros but keeping at least one decimal."""
    return f"{v:g}"


def _infer_thinking_levels(reasoning: bool) -> tuple[str, ...]:
    """Infer supported thinking levels from reasoning capability."""
    return DEFAULT_THINKING_LEVELS if reasoning else NO_THINKING_LEVELS


# ---------------------------------------------------------------------------
# models.dev fetcher
# ---------------------------------------------------------------------------

MODELS_DEV_USER_AGENT = "dino-ai/1.0 (model-catalog-generator)"


def _build_request(url: str) -> Request:
    return Request(url, headers={"User-Agent": MODELS_DEV_USER_AGENT})


def fetch_models_dev() -> tuple[dict, dict[str, dict[str, dict]]]:
    """Fetch models.dev registry.

    Returns (raw_data, {provider_key: {model_id: model_data}}).
    raw_data is the full provider-level metadata keyed by models.dev provider id.
    """
    print(f"Fetching models from {MODELS_DEV_URL} ...", file=sys.stderr)
    try:
        req = _build_request(MODELS_DEV_URL)
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
    except Exception as exc:
        print(f"Warning: failed to fetch models.dev: {exc}", file=sys.stderr)
        return {}, {}

    result: dict[str, dict[str, dict]] = {}
    for dev_key, dev_provider in data.items():
        if not isinstance(dev_provider, dict):
            continue
        models_raw = dev_provider.get("models")
        if not isinstance(models_raw, dict):
            continue
        models: dict[str, dict] = {}
        for model_id, model_data in models_raw.items():
            if not isinstance(model_data, dict):
                continue
            if model_data.get("tool_call") is not True:
                continue
            models[model_id] = model_data
        if models:
            result[dev_key] = models

    total = sum(len(v) for v in result.values())
    print(f"Fetched {total} tool-capable models across {len(result)} providers", file=sys.stderr)
    return data, result


def _get_bedrock_base_url(model_id: str) -> str:
    """EU bedrock models use the Frankfurt endpoint."""
    return (
        "https://bedrock-runtime.eu-central-1.amazonaws.com"
        if model_id.startswith("eu.")
        else "https://bedrock-runtime.us-east-1.amazonaws.com"
    )


def _resolve_api(dev_provider: dict) -> str:
    """Resolve API protocol from models.dev provider-level npm metadata."""
    npm = dev_provider.get("npm", "")
    return NPM_TO_API.get(npm, "openai-completions")


def _resolve_base_url(dev_provider: dict) -> str:
    """Resolve base URL from models.dev provider-level api metadata."""
    api_url = dev_provider.get("api", "")
    if isinstance(api_url, str) and api_url:
        return api_url.rstrip("/")
    return ""


def _get_defaults_per_provider(
    dev_key: str, dev_provider: dict
) -> tuple[str, str, str]:
    """Return (dino_provider, api, base_url) for a models.dev provider entry."""
    dino_name = PROVIDER_MAP[dev_key]
    api = _resolve_api(dev_provider)
    base_url = _resolve_base_url(dev_provider)
    return dino_name, api, base_url


def _convert_models_dev_model(
    dev_provider: dict,
    model_id: str,
    m: dict,
    default_api: str,
    default_base_url: str,
    dino_provider: str,
) -> dict | None:
    """Convert a models.dev model entry to dino-ai internal dict."""
    caps = m.get("capabilities", {}) if isinstance(m.get("capabilities"), dict) else {}
    reasoning = bool(m.get("reasoning", caps.get("reasoning", False)))

    limit = m.get("limit") if isinstance(m.get("limit"), dict) else {}
    cost = m.get("cost") if isinstance(m.get("cost"), dict) else {}
    modalities = m.get("modalities") if isinstance(m.get("modalities"), dict) else {}
    input_modalities: list = modalities.get("input", []) if isinstance(modalities, dict) else []
    vision = "image" in input_modalities

    supported_thinking_levels: tuple[str, ...] = _infer_thinking_levels(reasoning)

    return {
        "name": str(m.get("name") or model_id),
        "api": default_api,
        "provider": dino_provider,
        "baseUrl": default_base_url,
        "capabilities": {
            "reasoning": reasoning,
            "vision": vision,
            "toolCalling": True,
            "streaming": True,
            "supportedThinkingLevels": supported_thinking_levels,
        },
        "limits": {
            "contextWindow": int(limit.get("context", 0)),
            "maxOutputTokens": int(limit.get("output", 0)),
        },
        "pricing": {
            "input": float(cost.get("input", 0)),
            "output": float(cost.get("output", 0)),
            "cacheRead": float(cost.get("cache_read", 0)),
            "cacheWrite": float(cost.get("cache_write", 0)),
        },
    }


def _load_yaml_fallback() -> dict[str, dict[str, dict]]:
    """Load YAML catalog files for providers NOT covered by models.dev."""
    result: dict[str, dict[str, dict]] = {}
    for path in sorted(CATALOG_DIR.glob("*.yaml")):
        with open(path, encoding="utf-8") as f:
            doc = yaml.safe_load(f)

        if not isinstance(doc, dict) or "models" not in doc:
            continue

        provider = doc["provider"]
        default_api = doc.get("defaultApi", "")
        base_url = doc.get("baseUrl", "")
        models_raw: dict = doc["models"]

        # If models.dev already covers this provider (by dino-ai name), skip YAML
        if provider in _MODELS_DEV_DINO_NAMES:
            continue

        converted: dict[str, dict] = {}
        for model_id, model_data in models_raw.items():
            entry = dict(model_data)
            if "api" not in entry and default_api:
                entry["api"] = default_api
            if "baseUrl" not in entry and base_url:
                entry["baseUrl"] = base_url
            if "provider" not in entry:
                entry["provider"] = provider
            converted[model_id] = entry

        if converted:
            result[provider] = converted

    return result


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------
def _format_model(model_id: str, data: dict, provider: str, default_api: str, base_url: str) -> str:
    caps = data.get("capabilities", {})
    limits = data.get("limits", {})
    pricing = data.get("pricing", {})

    api = data.get("api", default_api)
    model_base_url = data.get("baseUrl", base_url)
    thinking_levels = _format_thinking_levels(caps.get("supportedThinkingLevels"))

    return f"""    {_to_identifier(model_id)} = Model(
        id="{model_id}",
        name="{data.get('name', model_id)}",
        api="{api}",
        provider="{provider}",
        base_url="{model_base_url}",
        capabilities=ModelCapabilities(
            reasoning={caps.get('reasoning', False)},
            vision={caps.get('vision', False)},
            tool_calling={caps.get('toolCalling', True)},
            streaming={caps.get('streaming', True)},
            supported_thinking_levels={thinking_levels},
        ),
        limits=ModelLimits(
            context_window={limits.get('contextWindow', 0)},
            max_output_tokens={limits.get('maxOutputTokens', 0)},
        ),
        pricing=ModelPricing(
            input={_fmt_float(pricing.get('input', 0.0))},
            output={_fmt_float(pricing.get('output', 0.0))},
            cache_read={_fmt_float(pricing.get('cacheRead', 0.0))},
            cache_write={_fmt_float(pricing.get('cacheWrite', 0.0))},
        ),
    )"""


def _generate_provider_file(
    provider: str,
    class_name: str,
    models: list[tuple[str, dict]],
    default_api: str,
    default_base_url: str,
) -> str:
    """Generate one provider's Python file content."""
    lines = [PROVIDER_FILE_HEADER.format(provider=provider)]
    lines.append(f"\n\nclass {class_name}:")
    lines.append(f'    """Models for {provider}."""\n')

    for model_id, model_data in models:
        lines.append(
            _format_model(model_id, model_data, provider, default_api, default_base_url)
        )
        lines.append("")

    return "\n".join(lines)


def generate() -> dict[str, str]:
    """Generate all model files.

    Returns {relative_filename: content}.
    """
    # --- Primary: models.dev ---
    raw_data, models_dev = fetch_models_dev()

    # Build per-provider model dicts from models.dev
    all_providers: dict[str, tuple[str, str, list[tuple[str, dict]]]] = {}

    for dev_key, models in sorted(models_dev.items()):
        if dev_key not in PROVIDER_MAP:
            continue
        dev_provider = raw_data.get(dev_key, {})
        dino_provider, default_api, default_base_url = _get_defaults_per_provider(dev_key, dev_provider)

        converted: list[tuple[str, dict]] = []
        for model_id, raw in sorted(models.items()):
            model_dict = _convert_models_dev_model(
                dev_provider, model_id, raw, default_api, default_base_url, dino_provider
            )
            if model_dict is None:
                continue
            converted.append((model_id, model_dict))

        if converted:
            all_providers[dino_provider] = (default_api, default_base_url, converted)

    # --- Hardcoded: alternate protocol variants ---
    for hc in HARDCODED_PROVIDERS:
        source_key = hc["source_dev_key"]
        if source_key not in models_dev:
            continue
        dino_provider = hc["dino_provider"]
        api = hc["api"]
        base_url = hc["base_url"]

        converted: list[tuple[str, dict]] = []
        for model_id, raw in sorted(models_dev[source_key].items()):
            model_dict = _convert_models_dev_model(
                {}, model_id, raw, api, base_url, dino_provider
            )
            if model_dict is None:
                continue
            model_dict["api"] = api
            model_dict["baseUrl"] = base_url
            model_dict["provider"] = dino_provider
            converted.append((model_id, model_dict))

        if converted:
            all_providers[dino_provider] = (api, base_url, converted)

    # --- Fallback: YAML files for uncovered providers ---
    yaml_fallback = _load_yaml_fallback()
    models_dev_provider_names = set(all_providers.keys())
    for provider, models in sorted(yaml_fallback.items()):
        if provider in models_dev_provider_names:
            continue
        first = next(iter(models.values()))
        default_api_yaml = first.get("api", "")
        default_base_yaml = first.get("baseUrl", "")
        converted = [(mid, data) for mid, data in sorted(models.items())]
        all_providers[provider] = (default_api_yaml, default_base_yaml, converted)

    # --- Generate per-provider files ---
    files: dict[str, str] = {}
    model_count = 0
    init_imports: list[str] = []
    all_models_refs: list[str] = []

    for provider in sorted(all_providers.keys()):
        default_api, default_base_url, models = all_providers[provider]
        class_name = _to_class_name(provider)
        filename = _safe_filename(provider)

        content = _generate_provider_file(provider, class_name, models, default_api, default_base_url)
        files[filename] = content
        model_count += len(models)

        safe_name = _safe_filename(provider).removesuffix(".py")
        init_imports.append(f"from dino_ai.models.{safe_name} import {class_name}")
        for model_id, _model_data in models:
            all_models_refs.append(f"    {class_name}.{_to_identifier(model_id)},")

    # --- Generate __init__.py ---
    init_lines = [INIT_HEADER]
    init_lines.extend(init_imports)
    init_lines.append("")
    init_lines.append("ALL_MODELS: list[Model] = [")
    init_lines.extend(all_models_refs)
    init_lines.append("]")
    init_lines.append("")
    files["__init__.py"] = "\n".join(init_lines)

    print(f"Total models to generate: {model_count}", file=sys.stderr)
    return files


def main() -> None:
    # Remove old single-file output if it exists
    if OLD_OUTPUT.exists():
        OLD_OUTPUT.unlink()
        print(f"Removed old {OLD_OUTPUT}", file=sys.stderr)

    # Create output directory
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    files = generate()

    for rel_name, content in files.items():
        path = MODELS_DIR / rel_name
        path.write_text(content, encoding="utf-8")
        model_count = content.count("Model(")
        print(f"Generated {path} ({model_count} models)")

    # Auto-fix lint on all generated files
    ruff = str(Path(sys.executable).parent / "ruff")
    subprocess.run(
        [ruff, "check", "--fix", "--quiet", str(MODELS_DIR)],
        check=False,
    )


if __name__ == "__main__":
    main()
