# sources/ — the data source registry

- `registry.yml` — canonical catalog of every data/information source. The pipeline reads endpoints from here.
- `registry.schema.json` — the schema each entry must satisfy.
- Validate: `python pipeline/checks/validate_registry.py` (must exit 0).

Each entry stores the **human landing page** (`url`) and, when known, the **resource URL** (`data_url`). For CKAN portals (ONS/ANEEL/CCEE/CVM) leave `data_url` empty and let the fetcher resolve the current resource via the CKAN API — this survives portal path/resource-id rotation.

Curtailment sources carry a `layer` (`physical | rule | settlement | litigation | context`) implementing the three-layer model (PLAN §5.2). Provenance for the entries: `research/reports/2026-06-17_brazil_power_source_inventory.md`.
