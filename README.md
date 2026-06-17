# BTG Brazil Energy — Private-Credit Intelligence Platform

A shared, version-controlled platform for monitoring and analyzing the **Brazilian power (electricity) sector** through a **private-credit lens**. It pairs a curated knowledge base with a correctness-first data pipeline and analysis outputs, and is designed to **compound over time** — analysis conversations are recorded and distilled back into the knowledge base.

> **Scope:** sector-wide. **First module:** a curtailment monitor for wind (*eólica*) and solar (*fotovoltaica*) generation — *constrained-off* volumes, reasons, regions, affected assets, and the compensation (*ressarcimento*) framework, framed for credit impact.

## Start here
- **`PLAN.md`** — the full implementation plan, architecture, and decision log (*what* and *why*).
- **`BUILD_LOG.md`** — the running handoff log (*what's done* and *what's next*). Read this to pick up the project mid-stream.
- **`CLAUDE.md`** — context + working rules for AI agents (and humans).

## Layout
| Path | Purpose |
|------|---------|
| `sources/` | `registry.yml` — canonical catalog of data sources |
| `raw/` | **Immutable** downloads + provenance (never edit) |
| `processed/` | Tidy, validated, lineage-tagged datasets |
| `pipeline/` | `fetch/`, `transform/`, `checks/` (deterministic + semantic) |
| `validation/` | Check reports + quality gate |
| `analysis/` | Reports, memos, the credit read |
| `conversations/` | Recorded + distilled session memory |
| `research/` | Research prompts and raw research outputs |

## Data quality model
Data flows `raw → processed` through two gates:
- **Deterministic checks** (code) — schema, ranges, reconciliation, referential integrity, source fidelity, freshness. A failure **stops** the pipeline.
- **Semantic checks** (LLM judgment) — trend plausibility, cross-source corroboration, unit-confusion traps. Findings are **flagged for human review**.

Every processed number traces back to a raw source.

## How we build (and how to contribute) — keep the build log
This project is built in **small, verifiable steps** (see `PLAN.md §10`), and **every meaningful step is recorded in `BUILD_LOG.md`** so any human or AI can take over and continue without prior context.

**If you (human or AI) make changes, you must:**
1. Make one small, verifiable change at a time.
2. Append a dated entry to `BUILD_LOG.md` — what you did, why, key decisions, what now works, what's pending, and the next step.
3. Commit that log entry **together with** the change, and push.

Treat the build log as the project's memory and handoff mechanism.

## Status
Early scaffolding. Current state and next step are always at the bottom of `BUILD_LOG.md`.
