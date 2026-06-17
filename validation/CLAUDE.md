# validation/ — check reports + quality gate

- `quality_gate.py` — orchestrates the run: transform output must pass `pipeline/checks/deterministic.py` before it is accepted into `processed/`. Deterministic failure = non-zero exit = pipeline aborts.
- `reports/` — dated check reports (deterministic results + semantic-review flags).

Deterministic checks are a **hard gate**. Semantic checks **flag for human review** — they never silently pass or block.
