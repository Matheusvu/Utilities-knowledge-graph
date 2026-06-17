# processed/ — tidy, validated, lineage-tagged datasets

Outputs of `pipeline/transform/`. Every dataset here:
- has canonical `snake_case` columns, ISO-8601 dates, explicit unit suffixes (`_mwmed`, `_mwh`);
- carries a **lineage record** (which `raw/` inputs + transform version produced it);
- has passed `pipeline/checks/deterministic.py` (hard gate). Nothing lands here that failed a deterministic check.

`data_dictionary.md` defines every dataset, field, unit, and source.
Curtailment module outputs live in `processed/curtailment/`.

**Units trap:** never mix MW / MWmed / MWh / GWh, or physical-restricted vs compensable vs settled energy.
