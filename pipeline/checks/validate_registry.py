#!/usr/bin/env python3
"""Validate sources/registry.yml against sources/registry.schema.json.

Deterministic check (PLAN.md §4.1, Phase 0.3 / 1.1). Exits 0 on success, 1 on failure.
Also enforces a few registry-level invariants beyond the JSON Schema:
  - source ids are unique
  - every curtailment-category source declares a `layer`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "sources" / "registry.yml"
SCHEMA = ROOT / "sources" / "registry.schema.json"


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))

    errors: list[str] = []

    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.path) or "<root>"
        errors.append(f"[schema] {loc}: {err.message}")

    sources = (data or {}).get("sources", []) if isinstance(data, dict) else []

    ids = [s.get("id") for s in sources if isinstance(s, dict)]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        errors.append(f"[invariant] duplicate source ids: {sorted(dupes)}")

    for s in sources:
        if isinstance(s, dict) and s.get("category") == "curtailment" and "layer" not in s:
            errors.append(f"[invariant] curtailment source '{s.get('id')}' must declare a `layer`")

    if errors:
        print(f"FAIL: registry invalid ({len(errors)} problem(s)):")
        for e in errors:
            print("  -", e)
        return 1

    print(f"OK: registry valid — {len(sources)} source(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
