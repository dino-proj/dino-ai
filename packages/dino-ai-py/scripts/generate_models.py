#!/usr/bin/env python3
"""Generate models.py from catalog/ YAML files.

Usage:
    python scripts/generate_models.py

Reads all YAML files from catalog/v1/ and produces
src/dino_ai/models.py with typed Model constants grouped by provider.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CATALOG_DIR = REPO_ROOT / "catalog" / "v1"
OUTPUT = Path(__file__).resolve().parent.parent / "src" / "dino_ai" / "models.py"

HEADER = '''\
"""Auto-generated model constants from catalog/ YAML files.

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


def _format_thinking_levels(levels: list[str] | None, indent: int = 12) -> str:
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
    # If it fits on one line (within 120 chars with indent), use single line
    single = "(" + ", ".join(items) + ",)"
    if indent + len("supported_thinking_levels=") + len(single) + 1 <= 120:
        return single
    # Otherwise, multi-line
    pad = " " * indent
    inner = (",\n" + pad + "    ").join(items)
    return "(\n" + pad + "    " + inner + ",\n" + pad + ")"


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
            input={pricing.get('input', 0.0)},
            output={pricing.get('output', 0.0)},
            cache_read={pricing.get('cacheRead', 0.0)},
            cache_write={pricing.get('cacheWrite', 0.0)},
        ),
    )"""


def generate() -> str:
    lines = [HEADER]

    catalog_files = sorted(CATALOG_DIR.glob("*.yaml"))
    if not catalog_files:
        print(f"Warning: no YAML files found in {CATALOG_DIR}", file=sys.stderr)

    for path in catalog_files:
        with open(path, encoding="utf-8") as f:
            doc = yaml.safe_load(f)

        if not isinstance(doc, dict) or "models" not in doc:
            continue

        provider = doc["provider"]
        default_api = doc.get("defaultApi", "")
        base_url = doc.get("baseUrl", "")
        models_data: dict = doc["models"]

        class_name = _to_class_name(provider)
        lines.append(f"\n\nclass {class_name}:")
        lines.append(f'    """Models for {provider}."""\n')

        for model_id, model_data in models_data.items():
            lines.append(_format_model(model_id, model_data, provider, default_api, base_url))
            lines.append("")

    # Convenience: ALL_MODELS list
    lines.append("\n\nALL_MODELS: list[Model] = [")
    for path in catalog_files:
        with open(path, encoding="utf-8") as f:
            doc = yaml.safe_load(f)
        if not isinstance(doc, dict) or "models" not in doc:
            continue
        class_name = _to_class_name(doc["provider"])
        for model_id in doc["models"]:
            lines.append(f"    {class_name}.{_to_identifier(model_id)},")
    lines.append("]")
    lines.append("")

    return "\n".join(lines)


import subprocess


def main() -> None:
    content = generate()
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Generated {OUTPUT} ({content.count('Model('):d} models)")

    # Auto-fix lint (import sorting, trailing whitespace)
    subprocess.run(["ruff", "check", "--fix", "--quiet", str(OUTPUT)], check=False)


if __name__ == "__main__":
    main()
