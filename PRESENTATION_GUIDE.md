# Presentation Guide — Utilities Knowledge Graph for BTG Private Credit

Audience: Head of Private Credit – Utilities (BTG Pactual)
Goal: show what the knowledge graph does that a folder of documents does not, using 5 use cases that were actually run.
Companion files: `PLAN_5_USE_CASES.md` (plan), `run_use_cases.py` (code), `graphify-out/use_cases_results.txt` (raw output), `raw/` (38 source files, listed in Appendix I).

---

## 0. Read this first — corrections to earlier material

While checking the graph output against `raw/`, several things in the earlier plan and in `graphify-out/btg_top10_usecases.pptx` turned out to be wrong or unsupported. Do not repeat them in the deck.

| Where | What it says | What the sources say |
|---|---|---|
| `PLAN_5_USE_CASES.md`, UC5 | "Equatorial's aggressive AMI rollout creates a moat" | `transformacao_digital_distribuidoras.md`: Equatorial is at **13%** AMI, among the laggards. **Copel leads (47%)**, then CPFL (30%). |
| `PLAN_5_USE_CASES.md`, UC2 | "Copel-DIS and CPFL face the greatest exposure; Energisa MT insulated" | `migracao_acl_impacto_distribuidoras.md`: largest net loss is **Cemig-D (-R$690M, ~9% EBITDA)**, then CPFL (-R$610M), Copel-DIS (-R$450M, ~9%). No Energisa-MT-specific claim exists. |
| `PLAN_5_USE_CASES.md`, UC3 | "Eletrobras thermals exposure" | The SBCE file names **Eneva** (outside the index) as the big thermal. Index companies are mostly hydro/wind/solar, i.e. net sellers. |
| `btg_top10_usecases.pptx` | Specific figures such as "Equatorial -R$420M RAB", "Copel-DIS loses ~R$890M", "Emborcação expiry → EBITDA loss R$680M" | None of these figures appear in `raw/` (Emborcação is R$580M in the Cemig file). They are illustrative placeholders. **Delete or replace them.** |
| Cemig source file | Scenario "100% re-leilão → EBITDA ~R$5.0bn → 3.5x" | The asset table adds up to R$1,580M at risk. R$7.6bn − R$1.58bn = **~R$6.0bn**, which gives 15.8 / 6.0 ≈ **2.6x**, not 3.5x. The source's own tables do not reconcile (see §UC1). |

The deck should use only numbers that exist in `raw/` and say which file they came from.

---

## 1. The honest pitch

Say this in the first two minutes, because the first question will be "why not just use ChatGPT / read the files?":

1. **The corpus is small.** ~27,700 words. The graph report itself notes it "fits in a single context window — you may not need a graph." For this corpus alone, the graph is not a necessity.
2. **The value is at scale and in traceability.** A credit team will not keep a handful of files; it will have thousands of pages of ANEEL resolutions, indentures, CCEE rules and filings. At that size nobody can hold it in their head or in a prompt. The graph is how it stays queryable, and every edge carries its source file and a confidence label (EXTRACTED vs INFERRED).
3. **What it adds over search:** it shows *connections between documents* that no single document states, and it tells you which ones are stated (EXTRACTED) and which are guesses (INFERRED, with a score).
4. **What it does not do:** it does not calculate covenants, forecast, or replace credit judgment. The numbers in the use cases come from the raw documents; the graph finds and links them.

This framing is more credible than "71x fewer tokens", which is a claim from the graphify README that was not measured here. Leave it out or label it vendor-reported.

---

## 2. Deck structure (12 slides + appendix)

| # | Slide | Purpose | Time |
|---|---|---|---|
| 1 | Cover | Title, date, audience | 0:15 |
| 2 | The problem | Why documents alone don't work for utilities credit | 1:00 |
| 3 | What we built | Corpus → graph → queries (numbers) | 1:30 |
| 4 | How to read a result | EXTRACTED vs INFERRED, source files, communities | 1:00 |
| 5 | UC1 — Cemig concession cliff | | 3:00 |
| 6 | UC2 — ACL 2028 opening | | 3:00 |
| 7 | UC3 — SBCE carbon + green finance | | 2:30 |
| 8 | UC4 — Hydrology (GSF/PLD) | | 3:00 |
| 9 | UC5 — AMI / quality → concession readiness | | 2:30 |
| 10 | Cross-use-case: the graph's hubs | Shows the same few nodes tie all five together | 1:00 |
| 11 | Limits and what's needed next | Builds trust | 1:30 |
| 12 | Proposal / ask | Pilot on real documents | 1:00 |
| A | Appendix A–E | Technical (section 5 below) | — |

### Slide 2 — The problem
- One credit question touches several regulators and documents. Example: "Can Cemig hold its covenant if hydro concessions are re-auctioned?" needs the concession schedule (company file), the renewal rules (ANEEL), the hydrology stress cases (ONS) and the covenant definition (debt file).
- Today an analyst reads each, builds the join by hand, and the join is not stored anywhere.
- Visual: a single question in the centre with 4–5 document icons around it.

### Slide 3 — What we built
Use these exact numbers (from `GRAPH_REPORT.md`):
- 38 source files in `raw/` (about 27,700 words) across 5 domains: regulação (7 content files), empresas (14 company files + 2 summaries), mercado (4), tecnologia (3), políticas (3), plus the credit index. Full list in Appendix I.
- 220 nodes · 304 edges · 27 communities.
- 83% of edges EXTRACTED (stated in the text), 17% INFERRED (51 edges, avg confidence 0.82).
- Companies covered: Cemig, CPFL, Copel, Equatorial, Energisa, Neoenergia, Eletrobras.
- Visual: `graphify-out/graph.png` or a screenshot of `graph.html`.

### Slide 4 — How to read a result
One example edge, annotated:
`Cemig Cliff de Concessões Hidrelétricas 2027-2030 —[conceptually_related_to, INFERRED, 0.70]→ ONS Cenários de Estresse para Crédito`
- Left node comes from `empresas/cemig/perfil_credito.md`, right node from `regulacao/ons_risco_hidrologico.md`.
- INFERRED = the model proposed it; a human should confirm it before relying on it.
- Say explicitly: "Treat INFERRED edges as leads, not facts."

### Slides 5–9 — one template per use case
Each use-case slide has four blocks, in this order:
1. **Question** (one sentence, credit language)
2. **What the graph returned** (nodes + edges, with EXTRACTED/INFERRED tags)
3. **What the source documents say** (the numbers, with file names)
4. **So what for BTG** (one decision-relevant sentence + one caveat)

---

## 3. Use-case content (what to put on each slide)

### UC1 — Cemig concession cliff (slide 5)

**Question:** If Cemig's hydro concessions (2027–2030) are re-auctioned instead of renewed, when does leverage cross the covenant, and which other documents bear on that?

**Graph returned** (from `use_cases_results.txt`, lines 1–232):
- 12 Cemig-related nodes. Best connected: `Cemig (CMIG3/CMIG4)` (8 edges), `Cemig Concessões e Contratos` (6), `Cemig Cliff…` (6).
- `Cemig Cliff` links (EXTRACTED) to: `Cemig Estrutura de Dívida e Covenants`, `ANEEL Renovação vs Re-leilão — Dilema 2028-2032`, `Equatorial Participação ~15% na Cemig`, and a rationale node "Cliff leva a covenant breach potencial".
- `Cemig Concessões e Contratos` links to `Emborcação (Re-leilão)`, `MME`, `Covenant Financeiro (DL/EBITDA / DSCR)`, `BNDES`.
- **INFERRED bridge (0.70):** `Cemig Cliff` ↔ `ONS Cenários de Estresse para Crédito`.
- **INFERRED (semantic):** `Cemig-D DEA Score e Problema de OPEX` ↔ `ANEEL DEA — Análise Envoltória de Dados`.

**Numbers from the source** (`raw/empresas/cemig/perfil_credito.md`):

| Plant | GF (MW avg) | EBITDA (R$M/yr) | Expiry |
|---|---|---|---|
| Três Marias | 178 | 320 | 2027 |
| Emborcação | 324 | 580 | 2028 |
| Nova Ponte | 216 | 390 | 2029 |
| Volta Grande | 160 | 290 | 2030 |
| **Total at risk** | **878** | **1,580** (~40% of hydro-driven EBITDA; the file says hydro ≈ 40% of consolidated) | |

Covenant: DL/EBITDA ≤ 3.5x. 2025: net debt / EBITDA 2.1x, DSCR 2.3x. Cemig-D DEA score 0.76; OPEX glosa R$720M (R$4,190M actual vs R$3,470M benchmark).

**Caveat to show (this is a strength, not a weakness):** the file's scenario table says total re-auction → EBITDA ~R$5.0bn → 3.5x. But 7.6 − 1.58 ≈ 6.0 → ~2.6x on guidance debt of R$15.8bn. Either other effects are baked in or the table is inconsistent. Also 2025 net debt equals gross debt (R$15.3bn), which looks like a data error. "This is exactly what a credit team wants flagged before it goes in a memo."

**So what:** the cliff is a real, dated, asset-level risk; the stress conclusion depends on the unresolved EBITDA assumption, so verify with Cemig's indenture and filings before using 3.5x.

**Also mention:** state control (MG, ~50%) and the October 2026 gubernatorial election appear in the same file as a governance overlay.

---

### UC2 — ACL full opening in 2028 (slide 6)

**Question:** Which distributors lose most margin when the free market fully opens, and what offsets it?

**Graph returned** (lines 233–405):
- Cluster of 4 EXTRACTED nodes (hyperedge, 0.90): migration impact, revenue mechanism, regulatory compensation (ANEEL CP 038/2025), mitigation strategies.
- Rationale node: "Distribuidoras retêm TUSD mas perdem margem de comercialização ACL."
- `CP 038/2025` ↔ `ANEEL Parcela A e Parcela B` (INFERRED).
- `Índice de Crédito BTG Utilities` has 22 EXTRACTED edges to the 7 companies, regulators and risk concepts (it is the hub of the whole graph).
- Direct company ↔ ACL edges exist only for CPFL (`CPFL Comercialização (ACL)`, `Abertura Total ACL 2028`), Copel and Equatorial (`Equatorial ACL Migration Revenue-at-Risk`). **No such edge was found for Energisa, Neoenergia or Cemig**, even though the source table covers them (see Appendix D).

**Numbers from the source** (`raw/mercado/migracao_acl_impacto_distribuidoras.md`):

| Company | Gross revenue-at-risk (R$M/yr) | TUSD retained | Net loss | % EBITDA |
|---|---|---|---|---|
| Cemig-D | 1,950 | 1,260 | **-690** | ~9% |
| CPFL Paulista+Piratininga | 1,680 | 1,070 | **-610** | ~7% |
| Copel-DIS | 1,250 | 800 | **-450** | ~9% |
| Neoenergia Elektro | 1,080 | 690 | **-390** | ~4% |
| Equatorial | 980 | 630 | **-350** | ~4% |
| Energisa | 860 | 550 | **-310** | ~4% |

Rule of thumb in the file: each MWh that migrates costs ~R$170 of margin but keeps ~R$210 of grid revenue. Market opening schedule: all consumers from Jan/2028 (Lei 14.300/2022 per the file; low-voltage rules still under study).

**Chart:** horizontal bar of net loss, coloured by % of EBITDA. Highlight Cemig-D and Copel-DIS (~9%).

**So what:** Cemig-D is the largest absolute and, with Copel-DIS, the largest relative hit. CP 038/2025 compensation is a proposal, not in force — treat as upside.

**Caveat:** table assumptions (R$150–180 margin loss, R$200–220 TUSD) drive everything; sensitivity on those two numbers is the first thing to add.

---

### UC3 — SBCE carbon market and green finance (slide 7)

**Question:** Does the carbon market create cost or opportunity for index companies, and how does it connect to green funding?

**Graph returned** (lines 406–521):
- `SBCE Mercado Brasileiro de Carbono` is the hub (11 EXTRACTED edges): Lei 15.042/2024, CBE, SINASE, I-REC, Green Bond, SLB, Taxonomia, MCTI, **Neoenergia, CPFL**.
- **INFERRED (0.70):** `Green Bond` ↔ `Debentures Incentivadas (Lei 12.431)`; `Green Bond` ↔ `SLB`; `SBCE` ↔ `NDC Brasil`.
- `Lei 15.042/2024` (regulation file) ↔ `RN 1.072/2026 — Regulamentação BESS` (INFERRED), linking carbon law to the battery rule.
- Compliance cluster (EXTRACTED, 0.92): SBCE, CBE, SINASE, MCTI, Lei 15.042.

**Numbers from the source** (`raw/politicas/carbon_market_sbce.md`):

| Source | tCO2e/MWh | Cost at R$100/tCO2e | Position |
|---|---|---|---|
| Coal | 0.95 | R$95/MWh | net buyer |
| Natural gas (CCGT) | 0.35 | R$35/MWh | net buyer |
| Hydro | 0.004 | R$0.40 | net seller |
| Solar / wind | 0 | R$0 | net seller |

Phase 1 (2026–28): 90% free allocation, price band R$80–120/tCO2e, thermal plants >50,000 tCO2e/yr obliged. Only worked example is **Eneva** (~R$180M, ~-5% EBITDA) — not an index company.

**So what:** for the current index (hydro/wind/solar/distribution) SBCE is mostly neutral-to-positive. The opportunity is financing: the graph links the carbon law to green/SLB instruments that Neoenergia and CPFL already reference. Value for BTG is as an origination lens (who can issue labelled debt), not a risk flag.

**Caveat:** the "SBCE compliance cost offset by green-debenture savings" idea in the plan is an interpretation of an INFERRED edge, not something any document says. Present it as a hypothesis to test.

---

### UC4 — Hydrology: GSF → CMO → PLD → generators (slide 8)

**Question:** How does a dry year transmit to generator credit, and who is most exposed?

**Graph returned** (lines 522–646):
- `ONS Risco Hidrológico — Impacto no Crédito de Geradoras` (7 EXTRACTED edges) fans out to reservoirs, CMO, GSF, MRR, CMSE, Itaipu, and **ONS Cenários de Estresse para Crédito**.
- Mechanism chain: `ONS CMO` →(INFERRED)→ `CCEE PLD — Cálculo e Limites`; `PLD` has three sub-nodes (volatility, structural drivers 2026–30, **basis risk between subsystems**).
- **INFERRED (0.88):** `Risco Hidrológico GSF` (market file) ↔ `CCEE GSF e MRR` (CCEE rules). Also ONS-GSF and ONS-MRR ↔ CCEE-GSF/MRR.
- Rationale node: MRR created after the 2012–2015 water crisis.
- Hydro-risk hyperedge (INFERRED, 0.88): GSF, CMO, PLD, MRR.
- The "company exposure" step of the script returned **nothing** (no company node links to GSF nodes). The company-level numbers below come from the document, not from graph traversal.

**Numbers from the source** (`raw/regulacao/ons_risco_hidrologico.md`):

| Plant | Owner | GF (MW avg) | GSF 2024 | Exposure at PLD R$89 |
|---|---|---|---|---|
| Paulo Afonso IV | Chesf/Eletrobras | 780 | 0.84 | R$112M |
| Serra da Mesa | Engie | 680 | 0.87 | R$79M |
| Furnas | Eletrobras | 850 | 0.91 | R$68M |
| Emborcação | Cemig | 324 | 0.88 | R$35M |
| Itumbiara | Engie | 390 | 0.90 | R$35M |
| Três Marias | Cemig | 178 | 0.82 | R$28M |

2021 stress: GSF 0.62, PLD R$182; Eletrobras ACL exposure ~R$3.1bn; hydro sector ~R$12bn. April 2026: South reservoirs 48% (watch item), SE/CO 62%; CMO jumped from ~R$95 (Mar) to ~R$134 SE/CO and R$165 South (Apr).

**Insight to call out:** Emborcação and Três Marias are both GSF-exposed *and* up for concession expiry (UC1). The graph links the two documents through the ONS stress node; the sources never state the combined case.

**So what:** hydrology is a sector-wide shock that hits generators first; the Cemig double-exposure (drought during a re-auction) is the tail case.

**Caveat:** exposures are 2024 estimates at one PLD; build a GSF × PLD grid before quoting a covenant breach level.

---

### UC5 — Digital/quality investment and concession readiness (slide 9)

**Question:** Which distributors are best placed on the metrics ANEEL ties to concession quality?

**Graph returned** (lines 647–870):
- `Transformação Digital das Distribuidoras` (10 EXTRACTED edges): AMI, SCADA, demand response, GD solar, V2G, PRODIST, PNT, DEC/FEC, RAB.
- Company links found: `Neoenergia` → AMI and PNT; `Copel` → AMI; `Equatorial Modelo de Turnaround` → DEC/FEC (INFERRED) and Caducidade (EXTRACTED); `Equatorial CEMAR (concession expires 2030)` → Renovação vs Re-leilão (INFERRED).
- INFERRED: PNT ↔ DEC/FEC; AMI ↔ Smart Grid.
- Rationale node: "ROI de AMI justifica CAPEX e melhora covenants."
- **Gap:** the hyperedge search for "digital" returned nothing, and CPFL, Energisa, Cemig have **no** direct tech edges even though the source covers them.

**Numbers from the source** (`raw/tecnologia/transformacao_digital_distribuidoras.md`):

| Company | AMI installed 2026 | 2028 target |
|---|---|---|
| Copel-DIS | **47%** | 75% |
| CPFL | 30% | 60% |
| Neoenergia | 18% | 45% |
| Cemig-D | 17% | 40% |
| Equatorial | 13% | 35% |
| Energisa | 13% | 30% |

Sector: 12M of 88M meters (14% of ANEEL's 2030 target), R$28–32bn still to invest; AMI benefit R$250–610M/yr per large distributor; Copel has 100% of substations automated.

**So what:** Copel and CPFL are best positioned; Energisa, Equatorial and Cemig-D must roughly 2–3x their rollout by 2028. This is a CAPEX and execution-risk list, not yet a concession-renewal ranking — the sources don't link the two.

**Caveat:** the plan's "technology mandates tied to renewal" is not supported by a document. Say "quality and investment metrics ANEEL monitors", not "renewal conditions".

---

### Slide 10 — The hubs
From the last section of the output: `Índice de Crédito BTG Utilities` (22 edges), `Riscos Políticos e Regulatórios 2026` (15), `Políticas Energéticas Brasil` (11), `ANEEL` (11), `Transformação Digital` (10). Message: the five use cases share a handful of hub nodes, so a new document attached to one of them becomes reachable from all five questions.

### Slide 11 — Limits (put this in; it earns trust)
- Corpus is small and curated; some source files contain internal inconsistencies (Cemig scenario table, net debt = gross debt).
- 17% of edges are inferred; weakest at 0.70.
- 79 nodes have ≤1 connection (graph's own gap list); many company-level facts are not linked to concepts (UC2, UC5 gaps).
- Company nodes are duplicated (e.g. `Cemig`, `Cemig (CMIG3/CMIG4)`, `Cemig Perfil de Crédito`); some have 0 edges.
- No quantitative modelling is done by the graph.

### Slide 12 — Proposal
1. Pilot on 2–3 real BTG positions: load indentures, last 3 years of ANEEL tariff resolutions, CCEE/ONS bulletins.
2. Clean entity resolution (merge duplicates), add company ↔ concept edges.
3. Add a human-review step for INFERRED edges.
4. Success measure: time to produce a covenant-risk memo, and number of cross-document issues found that the analyst had not.

---

## 4. Design notes
- Reuse the palette in `build_presentation.py` (navy `0D1B3E`, gold `C9A02B`).
- Max ~40 words per slide body; put tables in as native tables, not images.
- Tag every figure with its file name in small grey text.
- Mark INFERRED items with a dashed border or "?" icon, EXTRACTED with a solid one.
- Do not use any figure from the old `btg_top10_usecases.pptx`.

---

## 5. Appendix — technical details of what the code did

### Appendix A — The graph file
`graphify-out/graph.json` is an undirected, non-multi graph (`"directed": false`). Top level: `graph.hyperedges` (11 group relations), `nodes` (id, label, source_file, community), `links` (source, target, relation, confidence, confidence_score, source_file). Edge confidence is `EXTRACTED` (stated in a document) or `INFERRED` (proposed by the model, with a 0–1 score).

### Appendix B — What `run_use_cases.py` does
1. Loads `graph.json`; builds `nodes_by_id` and an adjacency list so each edge is reachable from both ends.
2. `find_nodes(*keywords)`: case-insensitive **substring match on node labels**. This is how each use case picks its starting nodes (e.g. "Cemig", "GSF", "SBCE", "AMI").
3. `neighbors(id)`: returns `(neighbor_id, edge)` pairs. `edge_between(a, b)` looks for a direct edge. For 2-hop checks it intersects neighbour sets.
4. Prints, per use case: matching nodes sorted by degree, each node's neighbours with confidence and relation, hyperedges whose label matches keywords, and specific "bridge" checks between named node pairs.
5. Output is written to `graphify-out/use_cases_results.txt` (895 lines).

**Bug fixed during the run:** the first version of `neighbors()` returned node dicts but callers treated them as ids, causing `AttributeError: 'dict' object has no attribute 'lower'`. It now returns ids. One list (`cemig_nb`, UC1) is computed but never used.

### Appendix C — Is this "running the graph"?
It is **traversal of the saved graph**, not natural-language querying. No LLM was called, and no semantic search was done; matches depend on label wording. The graphify CLI/`/graphify query` would do natural-language questions and could be used for a live demo; that was not run here. Traversal is deterministic and reproducible, which is why it suits the appendix, but the labels you search for determine what you find.

### Appendix D — Results and anomalies, use case by use case

| UC | Worked | Did not work / misleading |
|---|---|---|
| 1 | Found Cemig cluster (12 nodes), ANEEL renewal framework, INFERRED link to ONS stress node, DEA semantic link. | "Concession-related nodes" section lists *all* concession nodes (Energisa, CPFL, Eletrobras…), not only Cemig's, because the Cemig filter was never applied. Output is correct but noisy. |
| 2 | ACL mechanism cluster, CP 038/2025, and the index hub. | The company ↔ ACL loop matched 27 company-ish nodes, most printed "no direct ACL edge". Only CPFL, Copel, Equatorial have edges. Energisa, Neoenergia and Cemig exposures exist in the source table but are **not represented as edges** (extraction gap). The "TUSD" node (community 26) has zero edges. |
| 3 | Rich SBCE cluster; Green Bond ↔ Debentures Incentivadas inferred (0.70). | `target: ?` in the printout: edges carry `source_file` but the script read a non-existent `target_file`. The "INTERPRETATION / CREDIT IMPLICATION" text printed in this section is **hard-coded in the script**, not derived from the graph. The path "carbon_market_sbce.md → economics_renovaveis.md" is the node origin plus the edge's recorded source; confirm in `graph.json` before saying it in the room. |
| 4 | Full ONS/CCEE mechanism chain, 0.88 INFERRED cross-document bridges. | "Company exposure to GSF" printed nothing: no company node connects to a hydro-risk node within one hop. The first "bridge" check printed "No direct edge" for `Risco Hidrológico GSF/PLD` vs `CCEE GSF e MRR` (wrong node picked: two similarly named nodes exist) and then found the correct pair at 0.88. |
| 5 | Digital cluster; Neoenergia (AMI, PNT), Copel (AMI), Equatorial turnaround ↔ DEC/FEC and Caducidade. | "Hyperedge: digital transformation" printed nothing (no hyperedge exists for it). CPFL, Energisa, Cemig have no tech edges. Final "god nodes" section shows `Communities bridged: [0, 2]` for almost everything, an artefact of how the check counts neighbour communities, not a real finding. |

### Appendix E — Why "degree 0" appears for major companies
The graph has a README-level node per company (e.g. `CPFL Energia`, `Cemig`) with **zero edges**, and a separate richly-connected node (e.g. `CPFL Energia (CPFL3)`, 10 edges). That is an entity-resolution issue: the same company exists under several labels. It is why 15 of the graph's 27 communities have a single node. Fixing it (merge nodes, re-run) would improve every use case.

### Appendix F — Confidence scores seen in the run
- 0.70: Cemig Cliff ↔ ONS stress; Green Bond ↔ Debentures Incentivadas.
- 0.88: GSF market ↔ CCEE GSF/MRR; hydro-risk hyperedge.
- 0.90–0.95: EXTRACTED hyperedges (ACL cluster, RTP/WACC/RAB, SBCE compliance 0.92).
- Graph-wide: 304 edges, 83% EXTRACTED, 51 INFERRED (avg 0.82), 0% AMBIGUOUS.

### Appendix G — How to reproduce
```bash
cd Utilities-knowledge-graph
python run_use_cases.py > graphify-out/use_cases_results.txt
```
Requires only Python 3 and `graphify-out/graph.json`. To rebuild the graph after adding documents: `/graphify ./raw --update` inside Claude Code.

### Appendix H — Recommended fixes before the final deck (in priority order)
1. Merge duplicate company nodes and add company ↔ concept edges (ACL, GSF, AMI) so UC2/UC4/UC5 return per-company links from the graph.
2. Fix `target_file` (use only `source_file`) and apply the Cemig filter in UC1.
3. Remove the hard-coded interpretation text from the script, or label it "analyst note".
4. Resolve the Cemig EBITDA/leverage inconsistency in `raw/empresas/cemig/perfil_credito.md` against Cemig's filings.
5. Add a live `/graphify query` demo for 2–3 questions to complement the traversal output.
6. Add sensitivity tables (ACL margin × TUSD; GSF × PLD) as separate calculations, clearly labelled as analyst models.

### Appendix I — The 38 raw source files

**Index (1)**
- `raw/INDICE_CREDITO.md` — BTG Utilities credit index (hub of the graph)

**Empresas (16)**
- `raw/empresas/README.md`, `raw/empresas/perfis_crediticios.md` (cross-company summary)
- For each of Cemig, Copel, CPFL, Eletrobras, Energisa, Equatorial, Neoenergia (7 × 2 = 14): `perfil_credito.md` and `concessoes_contratos.md`

**Mercado (5)**
- `README.md`, `dinamicas_mercado.md`, `leiloes_historico_e_pipeline.md`, `migracao_acl_impacto_distribuidoras.md`, `pld_historico_analise.md`

**Políticas (4)**
- `README.md`, `carbon_market_sbce.md`, `politicas_energia.md`, `riscos_politicos_regulatorios_2026.md`

**Regulação (8)**
- `README.md`, `aneel_concessoes_distribuicao.md`, `aneel_framework.md`, `aneel_tarifas_rtp.md`, `ccee_regras_comercializacao.md`, `marco_regulatorio_novas_tecnologias.md`, `ons_ccee_mercado.md`, `ons_risco_hidrologico.md`

**Tecnologia (4)**
- `README.md`, `economics_renovaveis.md`, `tendencias_tech.md`, `transformacao_digital_distribuidoras.md`

Total: 1 + 16 + 5 + 4 + 8 + 4 = **38** (the empresas folder has 16 files: 1 README + 1 summary + 14 company files).

Note: the five folder `README.md` files are short index pages. About 30 files carry real content. Only the Cemig credit profile and the four files cited in UC2–UC5 were read (first 80–90 lines each) while writing this guide; the rest are known only through the graph.
