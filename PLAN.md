# Implementation Plan — BTG Brazil Energy: Private-Credit Intelligence Platform

**Status:** active · **Owner:** energy private-credit team · **First module:** Solar + Wind Curtailment Monitor
**Last updated:** 2026-06-17

---

## 1. Vision

A shared, version-controlled repository that functions as the team's **single source of truth and analytical engine** for the Brazilian power sector, with a credit lens. It must:

1. **Know the domain instantly** — any team member opening Claude Code in the repo gets full context with zero re-explaining (context engineering).
2. **Stay correct** — all data flows `raw → processed` through deterministic *and* semantic validation; every number is traceable to a source.
3. **Compound over time** — analysis conversations are recorded and distilled back into the knowledge base, so the system gets smarter with use.
4. **Run anywhere** — environment-agnostic; the execution environment provides network access. No logic depends on a particular container's egress.

The platform is built **incrementally**. The first concrete deliverable is a sector-wide-data-backed **curtailment monitor** for wind (eólica) and solar (fotovoltaica) generation.

---

## 2. Design principles

- **Correctness over speed.** Data work is gated; the analytical product is iterated slowly.
- **Primary & machine-readable first.** Official open-data/APIs (ONS, ANEEL, CCEE, EPE) over scraped/secondary sources.
- **Provenance always.** Every raw artifact records source URL, retrieval timestamp, and checksum; every processed row traces to its raw origin.
- **Two-layer validation.** Deterministic checks are a hard gate (pipeline fails). Semantic checks flag for human review (don't silently block, don't silently pass).
- **Portable.** Fetch/transform/check code runs on a laptop, a CI runner, or a configured cloud env identically.
- **Self-documenting.** `CLAUDE.md` files and a data dictionary keep humans and Claude aligned.
- **PT-BR for domain content, English for interface/structure.**
- **Small, verifiable steps.** Build one thing at a time and verify it before moving on, so failures stay isolated and debuggable — never wire many moving parts at once.
- **Resumable by anyone.** Maintain a running build log so any human or AI can pick up the project mid-stream and continue without prior context.

---

## 3. System architecture

### 3.1 Repository layout (target)

```
CLAUDE.md                      # master context brief (root)
PLAN.md                        # this document
BUILD_LOG.md                   # running, append-only build/handoff log (see §9)
README.md                      # human onboarding
.claude/
  settings.json                # SessionStart + Stop hooks (feedback loop)
  skills/                      # /credit-memo, /monitor, /compare-issuers, /log-insight, /ingest
sources/
  registry.yml                 # canonical catalog of all data sources (from Perplexity research)
  registry.schema.json         # schema the registry must satisfy
research/
  perplexity_source_discovery_prompt.md   # (done) source-discovery prompt
  reports/                     # raw research outputs (Perplexity, etc.)
raw/                           # IMMUTABLE downloads + provenance, organized by source
  ons/ aneel/ ccee/ epe/ mme/ news/
  _manifest.csv                # everything fetched: source, ts, checksum, bytes
processed/                     # tidy, validated, lineage-tagged datasets
  curtailment/                 # first module's outputs
  data_dictionary.md
pipeline/
  fetch/                       # one fetcher per source; portable; provenance-logging
  transform/                   # raw -> processed normalizers
  checks/
    deterministic.py           # hard gate
    semantic.md                # semantic review routine (run by Claude)
  common/                      # provenance, io, units, registry loader
validation/
  reports/                     # per-run check reports (dated)
  quality_gate.py              # orchestrates: transform must pass deterministic checks
conversations/                 # recorded + distilled session records (the memory)
analysis/
  curtailment/REPORT.md        # the monitor output (credit lens)
  memos/ templates/
DASHBOARD.md                   # rolling cross-module credit-watch summary
```

### 3.2 Data flow

```
sources/registry.yml ──> pipeline/fetch ──> raw/ (+_manifest, +provenance)
                                              │
                                              ▼
                                   pipeline/transform ──> processed/ (tidy)
                                              │
                          ┌───────────────────┴───────────────────┐
                          ▼                                        ▼
            checks/deterministic.py (HARD GATE)        checks/semantic.md (FLAG)
                          │                                        │
                          └──────────> validation/reports/ <───────┘
                                              │
                                              ▼
                                   analysis/ + DASHBOARD.md
```

### 3.3 Context-engineering layer

- **Root `CLAUDE.md`:** what the repo is, who uses it, the credit lens (business/regulatory/financial/structural risk), house glossary (PLD, ACL/ACR, RTP/RTE, constrained-off, ressarcimento, CEG, submercado), where each data type lives, and "how to run an analysis here."
- **Per-folder `CLAUDE.md`:** conventions specific to `raw/`, `processed/`, `pipeline/`, `sources/`, `analysis/`.
- **Data dictionary:** every processed dataset, field, unit, and source.

### 3.4 Self-compounding memory loop (hybrid)

- **`Stop` hook** → auto-records each session to `conversations/YYYY-MM-DD-<topic>.md` (question, findings, sources, conclusions).
- **`/log-insight` skill** → manually promotes a finding into the durable knowledge base (updates `processed/`, `analysis/`, or domain docs).
- **`SessionStart` hook** → surfaces the latest `DASHBOARD.md` + recent insights so each session opens current.
- Loop: *analysis → recorded → distilled → promoted → next session smarter.*
- **Compliance guardrail:** the recording layer persists analytical conclusions and public-source facts; it does **not** auto-persist sensitive/MNPI deal data unless explicitly directed.

---

## 4. Data pipeline specification

### 4.1 Source registry (`sources/registry.yml`)
Built from the Perplexity Deep Research output. One entry per source:
```yaml
- id: ons_constrained_off_eolica
  name: "Restrição de Operação por Constrained-off de Usinas Eólicas"
  publisher: ONS
  category: system_operation
  url: "<landing page>"
  data_url: "<direct dataset/API>"
  provides: "Daily constrained-off energy per wind plant, with reason flag"
  format: [csv, api]
  access: open_download         # open_download | api_key | login | paid
  update_frequency: daily
  history_from: "YYYY"
  granularity: "daily; per plant; per subsystem"
  language: pt
  tier: primary                 # primary | secondary
  relevance_credit: high
  relevance_curtailment: high
  notes: "Unit MWmed; verify vs generation dataset"
```
Validated against `registry.schema.json`.

### 4.2 Fetch layer (`pipeline/fetch/`)
- One fetcher per source (or per dataset family), reading endpoints from the registry.
- **CKAN-first.** ONS, ANEEL, CCEE, and CVM expose CKAN APIs (`<portal>/api/3/action/...`); prefer the API to discover current resource URLs, then download the resource file. This survives portal path changes better than hard-coded file URLs. Non-CKAN sources (ANA HidroWebService — email registration; INMET — download-first; EPE/MME — PDF-first) get bespoke fetchers.
- **Store both layers of identity:** the human **landing page** *and* the **resource-file path**, so a fallback can re-resolve via portal metadata when filenames/resource IDs rotate (a known instability).
- **Portable:** plain HTTP via `requests`/`httpx`, configurable user-agent, retries with backoff, on-disk cache.
- **Provenance:** each download writes a sidecar `*.provenance.json` (source id, landing URL, resource URL, retrieved_at, http_status, sha256, bytes) and appends to `raw/_manifest.csv`.
- **Idempotent:** re-running skips unchanged files (checksum compare).
- Raw files are **never edited** after landing.

### 4.3 Transform layer (`pipeline/transform/`)
- Raw → tidy/normalized tables (consistent column names, ISO dates, explicit units, canonical plant IDs via CEG/ANEEL registry).
- Deterministic, pure functions; output to `processed/`.
- Emits a lineage record per output (which raw inputs + transform version produced it).

### 4.4 Validation — deterministic (HARD GATE, `pipeline/checks/deterministic.py`)
- **Schema:** required columns, dtypes, units present.
- **Domain ranges:** curtailment ≥ 0; curtailment ≤ installed capacity; percentages ∈ [0,100].
- **Temporal:** continuous dates per series; no duplicate keys; consistent timezone.
- **Reconciliation:** Σ(reason categories) == total; Σ(plants) == subsystem total (within tolerance).
- **Referential integrity:** every plant id resolves in the plant master = **ANEEL SIGA** (CEG codes, installed capacity).
- **Source fidelity:** processed row counts/totals match the raw file's reported totals; raw checksum recorded.
- **Freshness:** latest data date within expected lag for the source's cadence.
- Failure ⇒ pipeline aborts; report written to `validation/reports/`.

### 4.5 Validation — semantic (FLAG FOR REVIEW, `pipeline/checks/semantic.md`)
A Claude-run review routine that:
- Checks **trend plausibility** vs. known events (new transmission lines, seasonal wind/solar patterns).
- Performs **cross-source corroboration** (ONS volumes vs. EPE/news/CCEE).
- Verifies **narrative-vs-number consistency** for extracted figures.
- Flags **unexplained anomalies/spikes** ("explained" vs "review").
- Catches the **unit-confusion trap** (MW vs MWmed vs MWh vs GWh; EAR vs ENA vs contracted energy).
- Distinguishes **physical restricted generation** from **compensable energy-not-supplied** from **settlement adjustments** (which land months later) — the three layers must never be conflated.
- Output: a flagged report appended to `validation/reports/`; never silently blocks or passes.

### 4.6 Lineage & manifest
- `raw/_manifest.csv` — index of every fetched artifact.
- Per-output lineage in `processed/` — raw inputs + transform version + run timestamp.

---

## 5. First module — Solar + Wind Curtailment Monitor

### 5.1 Questions it answers
- How much wind/solar generation is being curtailed, over time, by **subsystem/region** and by **reason** (reliability vs. energetic)?
- Which **assets/regions** are most affected?
- What is the **compensation (ressarcimento)** framework status, and how is it evolving (ANEEL rules, dockets, litigation)?
- **Credit lens:** revenue-at-risk for financed renewable SPVs and how the compensation regime mitigates it.

### 5.2 The three-layer model (source-backed)
The source inventory (`research/reports/2026-06-17_brazil_power_source_inventory.md`) shows that curtailment is **physically transparent before it is economically transparent**. The monitor must therefore be built in three layers, plus a litigation overlay:

1. **Physical truth — ONS.** Plant-level constrained-off, with cause classification (reliability vs. energetic), normalized against generation/load/interchange/hydrology.
2. **Legal/rule layer — ANEEL.** The compensation (*ressarcimento*) rules and their evolution: REN 1.073/2023 (solar), the Dec-2024 wind improvements, the 2026 PV criterion, plus dockets/consultations and DOU publication.
3. **Settlement/cash layer — CCEE.** How rules become money: constrained-off communications, reaccounting/ressarcimento chronograms, transitional-vs-definitive methodology, Lei 15.269/2025.
4. **Litigation overlay.** STJ Jan-2025 suspension of decisions ordering full compensation — the legal perimeter is contested.

**Event classification:** every curtailment event is tagged by **reason** (reliability | energetic) *and* by **compensation status** (compensable | not compensable | under litigation | methodology-transition). This is the core analytical product, and the credit read flows from it.

### 5.3 Inputs (concrete first-wave datasets)
Physical (ONS open data, CKAN): `restricao_coff_eolica_usi`, `restricao_coff_eolica_geracao`, `restricao_coff_fotovoltaica_usi`, `restricao_coff_fotovoltaica_geracao`; denominators/context `geracao-usina-2` (hourly gen by plant), `curva-carga-horaria`, `intercambios-entre-subsistemas`, `ena-diario-subsistema`, `ear-diario-subsistema`, `balanco-energia-subsistema`; methodology docs (NT-ONS DOP 0022/2025, RT DGL-ONS 0189-2025, FAQ, RO-AO.BR.13).
Asset master (ANEEL): **SIGA** (plant identity / CEG / installed capacity) — used for referential-integrity checks.
Rule layer (ANEEL): compensation news/resolutions, Pesquisa Pública dockets, DOU.
Settlement layer (CCEE): constrained-off communications + reaccounting chronograms (Acervo / Contabilização).
Corroboration (secondary): ABEEólica, ABSOLAR, CanalEnergia, MegaWhat.

### 5.4 Outputs
- `processed/curtailment/curtailment_daily.csv` + `_monthly.csv` (tidy, validated, lineage-tagged).
- `analysis/curtailment/REPORT.md` — narrative + tables + the credit read, with sources.
- Contribution to `DASHBOARD.md`.

### 5.5 Acceptance criteria
- All deterministic checks pass; semantic review produces zero unresolved "review" flags (or each is annotated).
- Every figure in `REPORT.md` traces to a `processed/` cell and onward to a `raw/` source.
- Numbers reconcile against at least one independent secondary source.

---

## 6. Skills & hooks

- **Skills (`.claude/skills/`):** `/ingest` (run fetch+transform+checks for a source), `/monitor` (refresh a module + update dashboard), `/credit-memo`, `/compare-issuers`, `/log-insight`.
- **Hooks (`.claude/settings.json`):** `SessionStart` (load dashboard + recent insights), `Stop` (record session to `conversations/`).
- Monitoring is **on-demand** initially; a scheduled trigger is added once the routine is proven.

---

## 7. Autonomy & quality gates

- Claude runs **autonomously** to: build the registry from research, write fetch/transform/check code, acquire and structure data into `raw/`, build `processed/`, and run both check layers.
- **Gates:** deterministic failure = stop and report. Semantic flags = surface for human review.
- The **analytical product** (`REPORT.md`, methodology) is iterated deliberately with human review — quality over speed.

---

## 8. Tech stack

- **Python 3.11**: `httpx`/`requests`, `pandas`, `pyyaml`, `jsonschema`, `pyarrow` (parquet optional), `python-pptx` (decks later).
- **Node 22** available if needed.
- **graphify** (`pip install graphifyy`) for the cross-cutting knowledge graph in a later phase.
- **Claude Code** skills/hooks for routines and the memory loop.

---

## 9. Conventions

- **Language:** PT-BR for domain content/data labels; English for code, structure, READMEs.
- **Naming:** `snake_case` files/columns; ISO-8601 dates; explicit unit suffixes (`_mwmed`, `_mwh`).
- **Immutability:** never edit files under `raw/`.
- **Provenance:** no processed dataset without lineage; no raw file without a provenance sidecar.
- **Commits:** clear messages; signed; pushed to the working branch. Keep each commit to one small, verifiable step.
- **Build log (`BUILD_LOG.md`) — mandatory while building.** Append a dated entry for every meaningful step: what was done and why, key decisions, what now works, what is broken or pending, and the immediate next step. Write it so a new human or AI can read it top-to-bottom and resume the project cold. Update it in the **same commit** as the change it describes. This is the project's handoff mechanism.

---

## 10. Phased roadmap — small, verifiable steps

**Guiding rule: one small step at a time.** Each step below is intentionally tiny, independently runnable, and has an explicit **checkpoint**. We build → verify the checkpoint → log it in `BUILD_LOG.md` → commit + push → only then start the next step. **Do not advance past a step whose checkpoint hasn't passed.** The first data work is a single-source *vertical slice* (Phase 2): we take **one** dataset all the way through the pipeline before scaling to many, so a failure is one failure — not a thousand at once.

Each step's checkpoint must be observable (a file exists, a script exits 0, a check passes) — not "looks done."

### Phase 0 — Foundation (no data yet, low risk)
- **0.1** Root `CLAUDE.md` + `README.md` + `BUILD_LOG.md` with the build-log rule. — *Checkpoint:* files exist; build-log rule present in both `CLAUDE.md` and `README`. ✅ *(this commit)*
- **0.2** Folder skeleton (`raw/ processed/ pipeline/ sources/ validation/ analysis/ conversations/`) with `.gitkeep`s and per-folder `CLAUDE.md` stubs. — *Checkpoint:* tree matches §3.1; committed.
- **0.3** `.claude/` skills + hooks stubs (no behavior yet) + `sources/registry.schema.json`. — *Checkpoint:* `registry.schema.json` is valid JSON Schema; an empty `registry.yml` validates against it.

### Phase 1 — Source registry (research is in hand ✅ — see `research/reports/2026-06-17_brazil_power_source_inventory.md`)
- **1.1** Convert the research output into `sources/registry.yml`, **curtailment sources only** first — the ONS constrained-off four + denominators (`geracao-usina-2`, `curva-carga-horaria`, `intercambios-entre-subsistemas`), ANEEL SIGA, and the methodology docs. — *Checkpoint:* validates against schema; those datasets present with landing + resource URLs.
- **1.2** Add the rule/settlement layer (ANEEL compensation news+dockets, CCEE constrained-off communications, STJ/DOU) and then the remaining sector-wide sources from the inventory. — *Checkpoint:* validates; the three layers + secondary corroboration are represented.

### Phase 2 — Vertical slice: ONE source, end to end ⭐ (the anti-"thousand errors" step)
- **2.1** Fetch **one** ONS constrained-off dataset → `raw/ons/` with provenance sidecar + manifest row. — *Checkpoint:* raw file on disk; `*.provenance.json` + `_manifest.csv` updated; sha256 recorded.
- **2.2** Transform that one file → a tidy `processed/curtailment/` table. — *Checkpoint:* output has canonical columns/units; lineage record written.
- **2.3** Minimal `checks/deterministic.py` covering that one table; wire `quality_gate.py`. — *Checkpoint:* checks run and **pass**; a deliberately corrupted input makes them **fail** (proves the gate works).
- **2.4** First `BUILD_LOG.md` handoff entry summarizing the working slice. — *Checkpoint:* a reader could reproduce the slice from the log alone.

### Phase 3 — Harden deterministic checks
- **3.1** Add reconciliation (Σ reasons = total; Σ plants = subsystem), referential integrity to plant master, source-fidelity totals, freshness. — *Checkpoint:* each check has a passing case and a failing case.

### Phase 4 — Scale to all curtailment sources
- **4.1** Add fetch+transform for the remaining curtailment inputs (solar, generation, capacity, ANEEL rules). — *Checkpoint:* full `processed/curtailment/*` builds and passes all hard checks.

### Phase 5 — Semantic checks
- **5.1** Author `checks/semantic.md` routine; run first review (trend plausibility, cross-source, unit traps). — *Checkpoint:* a dated semantic report exists; every flag is annotated.

### Phase 6 — Curtailment report (the product)
- **6.1** `analysis/curtailment/REPORT.md` + `DASHBOARD.md` contribution. — *Checkpoint:* meets §5.5; every figure traces to a `processed/` cell.

### Phase 7 — Memory loop
- **7.1** `Stop` + `SessionStart` hooks; **7.2** `/log-insight` skill. — *Checkpoint:* a session auto-records to `conversations/`; an insight promotes into the KB.

### Phase 8 — Automation
- **8.1** Scheduled trigger for `/monitor`. — *Checkpoint:* curtailment refreshes on schedule and updates the dashboard.

### Phase 9 — Expand sector-wide
- New modules (PLD, auctions, issuer credit profiles) + graphify knowledge graph, each reusing the same fetch→transform→check pattern. — *Checkpoint:* a second module ships through the identical pipeline.

---

## 11. Risks & open items

- **Network/egress** varies by environment; fetchers must degrade gracefully and be runnable where access exists (e.g., user's computer). *(Mitigated by portable design.)*
- **Source instability** (gov.br/CKAN path & resource-ID rotation): CKAN-first fetching + storing landing *and* resource URLs + metadata fallback make breakage detectable and recoverable; fetchers fail loudly.
- **Economic-transparency lag:** physical curtailment (ONS) is published well before the cash consequence (ANEEL rules → CCEE settlement → litigation). The three-layer model + event classification (§5.2) is the mitigation; never infer compensation from physical data alone.
- **Unit/definition traps** (MW/MWmed/MWh/GWh, EAR/ENA, physical vs compensable vs settled): handled explicitly in transform + semantic checks.
- **PDF-first / paywalled sources:** EPE/MME and some ANEEL procedural materials are PDF; ANBIMA's full feed and ratings agencies are paid/gated — these stay secondary/manual, with CVM as the issuer system-of-record.
- **MNPI/compliance** on a shared repo: memory loop persists conclusions and public facts, not sensitive deal data, unless directed.
- **Open input:** the other team's `CLAUDE.md`/structure (to mirror conventions) — incorporate if/when shared.
- **Resolved:** Perplexity source-discovery output received and archived; Phase 1 is unblocked.

---

## 12. Decision log (locked)

- Scope: **sector-wide** Brazilian power; first module = **solar+wind curtailment**.
- Form: integrated platform — knowledge base + monitoring + analysis.
- Feedback loop: **hybrid** (auto-record + manual promote).
- Data: **mix** — public downloads/research + marked slots for BTG-internal data.
- Language: **PT-BR domain / English interface**.
- Monitoring: **on-demand first**, schedule later.
- Validation: **deterministic (hard gate) + semantic (flag)**.
- Execution: **environment-agnostic**, portable code.
