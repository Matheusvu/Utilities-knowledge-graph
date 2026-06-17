# Build Log

> **Purpose:** a running, append-only record of how this project was built, so any human or AI can read it top-to-bottom and resume the work cold.
>
> **How to use it (mandatory while building):** for every meaningful step, append a dated entry below with: **What** you did · **Why** · **Decisions** · **Works now** · **Broken/Pending** · **Next step**. Commit the log entry in the *same commit* as the change it describes. Newest entries go at the bottom. The **Current state** marker at the very bottom always reflects where things stand.

---

## 2026-06-17 — Project framing & planning

**What:** Reset the repo to a clean slate (previous knowledge-graph content removed, preserved in git history). Defined the project and produced the implementation plan.
**Why:** Starting fresh to build a context-engineered, self-compounding credit-intelligence platform for the Brazilian power sector, replicating a proven pattern from another BTG team.
**Decisions (locked — see `PLAN.md §12`):** sector-wide scope; first module = solar+wind curtailment monitor; integrated platform (KB + monitoring + analysis); hybrid feedback loop (auto-record + manual promote); data = public downloads/research + slots for internal data; PT-BR domain / English interface; on-demand monitoring first; deterministic (hard gate) + semantic (flag) validation; environment-agnostic/portable code.
**Works now:** `PLAN.md` (full plan, granular phased roadmap, decision log); `research/perplexity_source_discovery_prompt.md` (Deep Research prompt for sector-wide source discovery), committed & pushed.
**Broken/Pending:** awaiting the Perplexity source-discovery output to build `sources/registry.yml` (unblocks Phase 1). Optional input: the other team's `CLAUDE.md`/structure to mirror conventions.
**Next step:** Phase 0.1 — create root `CLAUDE.md`, `README.md`, and this `BUILD_LOG.md` with the build-log rule.

## 2026-06-17 — Phase 0.1: foundation docs

**What:** Created root `CLAUDE.md` (project context + mandatory build protocol), `README.md` (onboarding + the keep-the-build-log rule), and this `BUILD_LOG.md`. Added the build-log convention and "small, verifiable steps" principle to `PLAN.md`, and broke the roadmap into granular, checkpoint-driven micro-phases (incl. the Phase 2 single-source *vertical slice* to avoid many failures at once).
**Why:** User wants the project broken into small phases (so errors stay isolated) and wants a handoff log so other humans/AI can continue the work.
**Decisions:** build log lives in `BUILD_LOG.md`, updated in the same commit as each change; checkpoints must be observable (file exists / script exits 0 / check passes).
**Works now:** foundation docs exist; build-log rule is stated in both `CLAUDE.md` and `README.md`; `PLAN.md §10` now lists micro-phases 0.1 → 9.
**Broken/Pending:** repo skeleton folders not yet created (Phase 0.2); `.claude/` skills+hooks and `registry.schema.json` not yet created (Phase 0.3).
**Next step:** Phase 0.2 — create the folder skeleton with `.gitkeep`s and per-folder `CLAUDE.md` stubs.

## 2026-06-17 — Source inventory received; plan made source-backed

**What:** Archived the Perplexity Deep Research source inventory to `research/reports/2026-06-17_brazil_power_source_inventory.md` (full sector-wide catalog with URLs, formats, access methods, tiers). Updated `PLAN.md` to be source-driven.
**Why:** User provided the deep-research output and asked to update the plan based on sources.
**Decisions:**
- Adopted the **three-layer curtailment architecture** (PLAN §5.2): **ONS** physical truth → **ANEEL** legal/rule layer → **CCEE** settlement/cash layer, + **litigation overlay** (STJ Jan-2025). Core product = events tagged by reason (reliability|energetic) AND compensation status (compensable|not|under-litigation|methodology-transition).
- **Systems-of-record:** ONS = physical; ANEEL = regulatory + asset master (**SIGA**, used for referential-integrity / CEG); CCEE = market + settlement; CVM = issuer/credit.
- **Fetch is CKAN-first** (ONS/ANEEL/CCEE/CVM `api/3/action/`), storing both landing page and resource URL with a metadata fallback (PLAN §4.2) — handles known portal/path rotation.
- Sharpened semantic checks & risks for the units trap and the physical-vs-compensable-vs-settled distinction.
**Works now:** source inventory archived; `PLAN.md` §4.2/§4.4/§4.5/§5/§10/§11 updated; first-wave curtailment datasets enumerated (the four ONS constrained-off datasets + denominators + SIGA + methodology docs).
**Broken/Pending:** repo skeleton not yet created (Phase 0.2); `registry.schema.json` not yet created (Phase 0.3); `sources/registry.yml` not yet built (Phase 1, now unblocked).
**Next step:** Phase 0.2 — folder skeleton + per-folder `CLAUDE.md` stubs; then 0.3 (schema) and 1.1 (build registry curtailment-first from the archived inventory).

## 2026-06-17 — Phases 0.2, 0.3, 1.1: skeleton, schema, curtailment-first registry

**What:** Built the repo skeleton, the registry schema + validator, and the first registry.
- **0.2** Folder tree per PLAN §3.1 (`raw/{ons,aneel,ccee,epe,mme,news}`, `processed/curtailment`, `pipeline/{fetch,transform,checks,common}`, `validation/reports`, `conversations`, `analysis/{curtailment,memos,templates}`, `sources`, `.claude/skills`) with `.gitkeep`s and per-folder `CLAUDE.md` stubs (`raw/ processed/ pipeline/ sources/ analysis/ validation/ conversations/`).
- **0.3** `.claude/settings.json` (empty placeholder, no behavior), `.claude/README.md` + five skill stubs (`/ingest /monitor /credit-memo /compare-issuers /log-insight`), and `sources/registry.schema.json` (JSON Schema draft 2020-12). Added `requirements.txt` (pyyaml, jsonschema, requests, pandas) and installed pyyaml+jsonschema.
- **1.1** `sources/registry.yml` — **15 curtailment-first sources**: the 4 ONS constrained-off datasets + denominators/context (geração horária, curva de carga, intercâmbios, ENA, EAR, balanço), ANEEL SIGA (asset master), and 4 ONS methodology docs. Built `pipeline/checks/validate_registry.py` (schema + invariants: unique ids; curtailment sources must declare `layer`).
**Why:** Continue the low-risk scaffold and stand up the machine-readable source backbone before any network work.
**Decisions:** registry is a `{version, updated, sources[]}` doc; CKAN datasets leave `data_url` empty (resolved via CKAN API at fetch); curtailment sources carry a `layer` (physical/rule/settlement/litigation/context).
**Works now:** `python pipeline/checks/validate_registry.py` → exit 0, "15 sources"; injected-error test detects problems (gate works); all JSON valid.
**Broken/Pending:** registry still missing the **rule layer** (ANEEL compensation), **settlement layer** (CCEE), **litigation overlay** (STJ/DOU), and remaining sector-wide sources — that's **Phase 1.2**. No data fetched yet (Phase 2). Skills/hooks are stubs only.
**Next step:** Phase 1.2 (extend registry with rule/settlement/litigation + sector-wide), then Phase 2.1 (vertical slice: fetch one ONS constrained-off dataset) — note fetch needs network, which runs where egress is available.

---

### Current state
**Phases 0.1, 0.2, 0.3, 1.1 complete.** Repo skeleton, per-folder context stubs, registry schema + validator, and a validated 15-source curtailment-first `sources/registry.yml` are in place (`validate_registry.py` exits 0). Next actionable step: **Phase 1.2** — add the ANEEL rule layer, CCEE settlement layer, STJ/DOU litigation overlay, and remaining sector-wide sources to the registry. Then **Phase 2** (vertical slice) begins the first network fetch.
