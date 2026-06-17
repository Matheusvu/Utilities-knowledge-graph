# raw/ — immutable source downloads

**Rule: never edit anything here.** Files land exactly as downloaded.

- Organized by publisher: `ons/ aneel/ ccee/ epe/ mme/ news/`.
- Every downloaded file gets a sidecar `*.provenance.json` (source id, landing URL, resource URL, retrieved_at, http_status, sha256, bytes).
- `_manifest.csv` indexes everything fetched.
- Fetchers live in `pipeline/fetch/` and read endpoints from `sources/registry.yml` (CKAN-first).

If a source looks wrong, fix it in `pipeline/transform/` or flag it in a check — do **not** edit the raw file.
