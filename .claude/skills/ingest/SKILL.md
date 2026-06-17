---
name: ingest
description: STUB (not yet implemented). Run fetch → transform → deterministic checks for a given source id or module from sources/registry.yml, landing data in raw/ and processed/. Implemented in PLAN.md Phases 2–4.
---

# /ingest — STUB

Not yet implemented. Planned behavior: given a source `id` (or module like `curtailment`),
resolve it from `sources/registry.yml`, fetch into `raw/` (with provenance), transform into
`processed/`, and run `pipeline/checks/deterministic.py`. See PLAN.md §6 and Phases 2–4.
