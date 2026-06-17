# .claude/ — shared skills & hooks for the team

These make Claude Code "know" the project and run repeatable routines. **Stubs for now** — behavior is implemented in later phases (PLAN.md §6, §10).

## Skills (`skills/`) — planned
| Skill | Purpose | Phase |
|-------|---------|-------|
| `/ingest` | Run fetch → transform → deterministic checks for a source/module | 2–4 |
| `/monitor` | Refresh a module and update `DASHBOARD.md` | 6 |
| `/credit-memo` | Generate an issuer credit memo from processed data | 9 |
| `/compare-issuers` | Build a cross-issuer comparison table | 9 |
| `/log-insight` | Promote a finding from a conversation into the knowledge base | 7 |

## Hooks (`settings.json`) — planned (Phase 7)
- `SessionStart` — surface latest `DASHBOARD.md` + recent insights so each session opens current.
- `Stop` — record the session to `conversations/` (the memory loop).

`settings.json` is currently an empty placeholder (no behavior).
