# CLAUDE.md — Project context for AI agents

> Read this first, every session. It tells you what this repo is, how to work in it, and the rules you must follow. The full design lives in `PLAN.md`; what has actually been done lives in `BUILD_LOG.md`.

## What this is
A shared, version-controlled **intelligence platform for the Brazilian power (electricity) sector, with a private-credit lens**, for the BTG energy private-credit team. It combines a curated knowledge base, a validated data pipeline, and analysis outputs — and it is designed to **compound** (analysis conversations are recorded and distilled back into the knowledge base).

**First module being built:** a sector-wide-data-backed **curtailment monitor** for wind (*eólica*) and solar (*fotovoltaica*) generation — i.e. ONS *constrained-off* volumes by reason (reliability vs. energetic), region and asset, plus the compensation (*ressarcimento*) framework, framed for credit impact on renewable SPVs.

## The lens
Everything is ultimately about **credit risk**: business, regulatory, financial, and structural risk of the issuers/assets the team lends to. When analyzing, connect findings back to revenue-at-risk, cash-flow stability, and debt-service capacity.

## Repo map (see PLAN.md §3 for the full target)
- `PLAN.md` — the implementation plan and decision log (source of truth for *what* and *why*).
- `BUILD_LOG.md` — running handoff log (source of truth for *what's done / what's next*).
- `sources/` — `registry.yml`: canonical catalog of data sources (+ its schema).
- `raw/` — **immutable** downloads + provenance. Never edit.
- `processed/` — tidy, validated, lineage-tagged datasets.
- `pipeline/` — `fetch/`, `transform/`, `checks/` (deterministic + semantic), `common/`.
- `validation/` — check reports + the quality gate.
- `analysis/` — reports, memos, the credit read.
- `conversations/` — recorded + distilled session memory.
- `research/` — research prompts and raw research outputs (e.g. Perplexity).

## How to work here — the build protocol (MANDATORY)
1. **One small step at a time.** Build a single thing, verify its checkpoint (a file exists / a script exits 0 / a check passes), then stop. Never wire many moving parts at once. Follow the phased roadmap in `PLAN.md §10`; do not skip ahead past a failing checkpoint.
2. **Keep the build log.** For **every meaningful step**, append a dated entry to `BUILD_LOG.md`: what you did and why, key decisions, what now works, what is broken/pending, and the immediate next step. Write it so a different human or AI can read it top-to-bottom and **resume the project cold**. Update the log in the **same commit** as the change.
3. **Correctness over speed.** Data flows `raw → processed` through deterministic checks (hard gate — pipeline fails) and semantic checks (flag for human review). No processed dataset without lineage; no raw file without a provenance sidecar.
4. **Commit + push each verified step** to the working branch with a clear message.
5. **Portable code.** Don't hard-code anything to one execution environment; the environment provides network access.

## Conventions
- **Language:** PT-BR for domain content/data labels; English for code, structure, and docs like this one.
- **Naming:** `snake_case`; ISO-8601 dates; explicit unit suffixes (`_mwmed`, `_mwh`). Watch the MWmed vs MWh vs GWh trap.
- **Glossary:** PLD (spot price), ACL/ACR (free/regulated market), RTP/RTE (tariff reviews), constrained-off (curtailment), ressarcimento (compensation), CEG (plant registry code), submercado (subsystem: N/NE/S/SE-CO).

## Compliance
This is a shared repo. The memory loop persists analytical conclusions and public-source facts — **not** sensitive/MNPI deal data — unless explicitly directed otherwise.
