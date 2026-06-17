# pipeline/ — fetch → transform → check

- `fetch/` — one fetcher per source/family; reads `sources/registry.yml`; **CKAN-first** (resolve current resource via `<portal>/api/3/action/`); writes to `raw/` with provenance. Portable HTTP, retries, cache. Network is provided by the execution environment.
- `transform/` — pure functions: `raw/` → tidy `processed/`; canonical columns/units/IDs; emit lineage.
- `checks/`
  - `validate_registry.py` — validates `sources/registry.yml` against the schema.
  - `deterministic.py` — HARD GATE (schema, ranges, reconciliation, referential integrity, source fidelity, freshness). Failure aborts the pipeline.
  - `semantic.md` — Claude-run review routine (flags for human review; never silently passes/blocks).
- `common/` — provenance, io, units, registry loader (shared helpers).

Run order is orchestrated by `validation/quality_gate.py`. See PLAN.md §4.
