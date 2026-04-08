# Brazil Energy & Utilities — Knowledge Graph

A knowledge graph for the Brazilian energy and utilities sector, built with [graphify](https://github.com/safishamsi/graphify).

## How to use

### 1. Drop your research materials into `raw/`

| Folder | What goes here |
|--------|---------------|
| `raw/regulacao/` | ANEEL resolutions, ONS/CCEE rules, tariff reviews |
| `raw/empresas/` | Annual reports, investor decks, concession contracts |
| `raw/mercado/` | PLD reports, auction results, market data |
| `raw/tecnologia/` | Papers on renewables, smart grids, storage |
| `raw/politicas/` | PNE, NDC, government energy plans |

Supported formats: `.md`, `.txt`, `.pdf`, `.png`, `.jpg`, `.webp`

### 2. Build the knowledge graph

Open Claude Code in this directory and run:

```
/graphify ./raw
```

This produces `graphify-out/`:
- `graph.html` — interactive graph (click nodes, filter by community)
- `GRAPH_REPORT.md` — plain-English audit of all concepts found
- `graph.json` — queryable JSON for follow-up queries
- `cache/` — SHA256 cache so re-runs only process changed files

### 3. Ask questions

After the graph is built, subsequent queries read `graph.json` — not your full raw files. This gives ~71x fewer tokens per query.

Example queries:
- "What are the main regulatory risks for distribution companies in Brazil?"
- "How does the ACL market differ from ACR for large consumers?"
- "Which companies have the most exposure to hydrology risk?"
- "What technology trends are reshaping the Brazilian grid?"

### 4. Keep it updated

```
/graphify ./raw --update   # add new files incrementally
/graphify ./raw --wiki     # generate Wikipedia-style articles per concept
```

## Installation (first time)

```bash
pip install graphifyy && graphify install
```

## Source

- GitHub: [safishamsi/graphify](https://github.com/safishamsi/graphify)
