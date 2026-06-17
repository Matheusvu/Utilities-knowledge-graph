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

---

### Current state
**Phase 0.1 complete.** Planning and foundation docs are in place. Next actionable step: **Phase 0.2 — folder skeleton + per-folder `CLAUDE.md` stubs.** Phase 1 (build `sources/registry.yml`) is blocked on the Perplexity source-discovery output.
