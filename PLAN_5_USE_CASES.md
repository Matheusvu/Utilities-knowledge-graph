# BTG Private Credit — Utilities Knowledge Graph: 5 Deep Use Cases
### Presentation & Execution Plan · April 2026

---

## Context

This knowledge graph ingests 40+ source files across 5 domains — regulatory filings
(ANEEL, ONS, CCEE), company credit profiles (Cemig, CPFL, Copel, Equatorial, Energisa,
Neoenergia, Eletrobras), market dynamics (PLD, ACL/ACR, leilões), technology trends,
and national energy policy (PNE, NDC, SBCE). The result is 220 nodes, 304 edges, and
27 detected communities — all queryable in plain language without re-reading source docs.

**Why this matters for BTG Private Credit — Utilities:**
The team manages a portfolio of debentures and project-finance positions across Brazilian
electricity companies. The credit risk is structurally complex: a single ANEEL resolution
can cascade through tariff methodology → company EBITDA → DSCR → covenant breach. Doing
that cross-referencing manually across 40+ documents is slow, error-prone, and expensive.
The knowledge graph compresses that into a graph query that runs in seconds.

---

## The 5 Use Cases

---

### USE CASE 1 · Cemig Concession Cliff — Full Credit Stress Chain

**The question:**
> "Map the complete credit stress chain: how does Cemig's hydro concession expiration
> (2027-2030) cascade through ANEEL's regulatory framework, their DEA efficiency score,
> and existing debt covenants — and at what point does each scenario breach covenant thresholds?"

**Why this is non-trivial:**
This is not a single-variable question. Cemig's concession risk lives in `raw/empresas/cemig/`,
but the *renewal conditions* live in `raw/regulacao/aneel_concessoes_distribuicao.md`, the *WACC
impact* is in `raw/regulacao/aneel_tarifas_rtp.md`, and the *hydro risk multiplier* lives in
`raw/regulacao/ons_risco_hidrologico.md`. Answering this manually means reading 4 documents,
cross-referencing asset-level data, running covenant math — then writing it up. The graph
does it in one query.

**Graph path traversed:**
```
Cemig (CMIG3/CMIG4)
  → Cemig Concessões e Contratos [concessoes_contratos.md]
    → ANEEL Caducidade — Risco Extremo de Concessão [aneel_concessoes_distribuicao.md]
    → ANEEL Renovação vs Re-leilão [aneel_framework.md]
  → Cemig Cliff de Concessões Hidrelétricas 2027-2030 [perfil_credito.md]
    → ONS Cenários de Estresse para Crédito [ons_risco_hidrologico.md]
    → Cemig Estrutura de Dívida e Covenants [perfil_credito.md]
  → Cemig-D DEA Score e Problema de OPEX [perfil_credito.md]
    → ANEEL DEA — Análise Envoltória de Dados [aneel_tarifas_rtp.md]
```

**Communities crossed:** `ANEEL Concessões e Distribuição` (C4) → `Regulação Tarifária RTP` (C1) → `CCEE Mercado e Liquidação` (C3)

**Expected output:**
- Concession-by-concession expiry table (MW, EBITDA, year, renewal probability)
- Covenant stress matrix: 4 scenarios × DL/EBITDA + DSCR trajectory
- Key cross-document insight: DEA score of 0.76 is a *compounding* risk — it weakens ANEEL's incentive to renew (regulatória prefers efficient operators)

---

### USE CASE 2 · ACL 2028 Full Opening — Portfolio Revenue Stress Matrix

**The question:**
> "Rank all distribuidoras in the BTG credit index by their exposure to ACL market
> liberalization in 2028. For each company, show projected revenue loss, the ANEEL
> regulatory compensation mechanism (CP 038/2025), and resulting covenant headroom."

**Why this is non-trivial:**
ACL migration data is in `raw/mercado/migracao_acl_impacto_distribuidoras.md`. The ANEEL
compensation mechanism is in `raw/regulacao/aneel_tarifas_rtp.md`. Individual company
concession profiles are in `raw/empresas/`. The BTG credit index weighting is in
`raw/INDICE_CREDITO.md`. No single document has the full picture — this requires the graph
to join 5+ sources.

**Graph path traversed:**
```
Índice de Crédito BTG Utilities [INDICE_CREDITO.md]
  → CPFL, Equatorial, Energisa, Copel, Neoenergia, Cemig [empresas/]
    → ACL (Ambiente de Contratação Livre) [migracao_acl_impacto_distribuidoras.md]
      → Abertura Total do Mercado Livre ACL 2028
      → ACL Mecanismo de Compensação Regulatória ANEEL CP 038/2025
      → ACL Mecanismo de Receita das Distribuidoras
      → Estratégias das Distribuidoras para Mitigar Perda ACL
    → TUSD (Tarifa de Uso do Sistema de Distribuição)
    → CDE (Conta de Desenvolvimento Energético)
```

**Communities crossed:** `ACL Migração e Concessões` (C0) → `Regulação Tarifária RTP` (C1) → `Estrutura do Mercado Elétrico` (C7)

**Expected output:**
- Ranked table: company × % industrial load eligible to migrate × revenue at risk (R$M)
- Offset analysis: TUSD retention + CP 038/2025 compensation → net revenue impact
- Key cross-document insight: Companies with high rural/residential mix (Energisa MT) are
  partially insulated; companies with heavy industrial A-class consumers (Copel-DIS, CPFL Paulista)
  face the greatest exposure

---

### USE CASE 3 · SBCE Carbon Compliance + ESG Financing Intersection

**The question:**
> "Brazil's new carbon market (SBCE, Lei 15.042/2024) creates compliance costs for thermal
> generation — but also creates a new market for green finance. Map which companies in the
> BTG credit index face compliance costs, which have existing green bond frameworks that could
> be repriced as SBCE-linked instruments, and what the net financing impact is."

**Why this is non-trivial:**
The SBCE framework is in `raw/politicas/carbon_market_sbce.md`. ESG financing structures
are in `raw/tecnologia/economics_renovaveis.md`. The connection between SBCE compliance
costs and green bond eligibility is *not written anywhere in the raw documents* — it is
an inferred edge in the graph (`Green Bond / Instrumento ESG Verde --semantically_similar_to-->
Debentures Incentivadas`). This is the graph's unique value: surfacing connections that exist
across documents but are never made explicit.

**Graph path traversed:**
```
SBCE Mercado Brasileiro de Carbono [carbon_market_sbce.md]
  → Lei 15.042/2024 (Marco Legal SBCE Carbono)
  → CBE (Cota Brasileira de Emissões)
  → NDC Brasil (Metas Climáticas Paris) [politicas_energia.md]
    → Descarbonização e Transição Energética
      → [INFERRED] Green Bond / Instrumento ESG Verde [economics_renovaveis.md]
        → [INFERRED] Debentures Incentivadas (Lei 12.431)
          → Project Finance Renovável
            → BNDES, DSCR, LCOE
  → Riscos Políticos e Regulatórios 2026 [riscos_politicos_regulatorios_2026.md]
    → Eletrobras (thermals exposure)
    → CPFL, Neoenergia (renewables-heavy — lower compliance cost)
```

**Communities crossed:** `ESG Carbono e Finanças Verdes` (C5) → `Políticas Energéticas e GD` (C6) → `Financiamento e Project Finance` (C10)

**Expected output:**
- SBCE compliance cost estimate per company (based on thermal exposure)
- Green finance eligibility matrix: which companies can issue SBCE-linked debentures at a premium
- Key cross-document insight: The inferred `Green Bond ↔ Debentures Incentivadas` edge means
  companies can simultaneously *pay* SBCE compliance costs and *save* on financing via green premium —
  this net-zero financing structure is not documented anywhere but is discoverable only through the graph

---

### USE CASE 4 · GSF Hydrological Risk → PLD Spike → Generator Credit Deterioration

**The question:**
> "Model the transmission mechanism from GSF deterioration (drought scenario) to CCEE
> settlement shortfall to credit metric deterioration for hydro-heavy generators in the
> BTG credit index. Which companies breach covenants first, and at what GSF level?"

**Why this is non-trivial:**
GSF mechanics are in `raw/regulacao/ons_risco_hidrologico.md`. PLD calculation is in
`raw/mercado/pld_historico_analise.md` and `raw/regulacao/ccee_regras_comercializacao.md`.
Company hydro exposure is in individual `perfil_credito.md` files. This requires a 4-hop
graph traversal: GSF → CMO → PLD spike → company settlement shortfall → DSCR deterioration.
No one reads all these documents together manually.

**Graph path traversed:**
```
Risco Hidrológico GSF — Generation Scaling Factor [dinamicas_mercado.md]
  → [INFERRED] CCEE GSF e MRR — Mecanismo de Repartição de Riscos [ccee_regras_comercializacao.md]
    → CCEE PLD — Cálculo e Limites
    → CCEE Contabilização e Ciclo de Liquidação
      → ONS Cenários de Estresse para Crédito [ons_risco_hidrologico.md]
        → [INFERRED] Cemig Cliff de Concessões Hidrelétricas 2027-2030
          → Cemig Estrutura de Dívida e Covenants
        → Eletrobras (largest hydro exposure in SIN)
        → CPFL Geração
```

**Communities crossed:** `CCEE Mercado e Liquidação` (C3) → `ACL Migração e Concessões` (C0) → `Eletrobras Pós-Privatização` (C9)

**Expected output:**
- GSF sensitivity table: GSF level (0.70 / 0.80 / 0.90 / 1.00) × company DSCR impact
- Covenant breach threshold: which GSF level triggers which company's debt covenant
- Key cross-document insight: The `Cemig Cliff + GSF` double-hit scenario (concession expiry
  in drought year) is the tail risk — both nodes are inferred to be connected via
  `ONS Cenários de Estresse`, but this connection is never made explicit in any source document.
  The graph discovered it.

---

### USE CASE 5 · Smart Grid Technology Mandates → Concession Renewal Readiness Ranking

**The question:**
> "ANEEL is tying concession renewal conditions to technology investment milestones
> (AMI deployment, DEC/FEC improvement, PNT reduction). Map which distribuidoras in the
> BTG credit index are best and worst positioned to meet these requirements, and what
> the credit implication of failing concession renewal conditions is."

**Why this is non-trivial:**
Technology mandates are in `raw/tecnologia/transformacao_digital_distribuidoras.md`.
Concession renewal framework is in `raw/regulacao/aneel_concessoes_distribuicao.md`.
DEC/FEC quality indicators are in `raw/regulacao/aneel_framework.md`. Individual company
infrastructure status is scattered across `raw/empresas/`. This is a 5-document join that
the graph condenses into a single traversal.

**Graph path traversed:**
```
Transformação Digital das Distribuidoras [transformacao_digital_distribuidoras.md]
  → AMI (Advanced Metering Infrastructure)
  → DEC/FEC (Indicadores de Continuidade de Energia)
  → PNT (Perdas Não Técnicas de Energia)
  → Resposta à Demanda (Demand Response)
    → ANEEL DEC/FEC — Indicadores de Qualidade e Penalidades [aneel_framework.md]
      → ANEEL Concessões de Distribuição — Framework e Riscos [aneel_concessoes_distribuicao.md]
        → ANEEL Renovação vs Re-leilão — Dilema 2028-2032
        → ANEEL Caducidade — Risco Extremo de Concessão
          → Cemig-D DEA Score e Problema de OPEX [perfil_credito.md]
          → Equatorial (best-in-class digitalization)
          → Energisa (mid-tier digital readiness)
          → Copel (public-sector legacy — transformation lagging)
```

**Communities crossed:** `Digitalização e Smart Grid` (C2) → `ANEEL Concessões e Distribuição` (C4) → `Regulação Tarifária RTP` (C1)

**Expected output:**
- Technology readiness scorecard: company × AMI deployment status × DEC/FEC trend × PNT level
- Concession renewal risk rating (Low / Medium / High / Critical)
- Key cross-document insight: Equatorial's aggressive AMI rollout (documented in their
  concession contracts) creates a competitive moat at renewal time — this is a *positive*
  credit differentiator not captured in standard financial ratio analysis

---

## Execution Plan

### Phase 1 — Run the Graph (this session)
For each of the 5 use cases above, run a structured query against `graphify-out/graph.json`
using `run_use_cases.py`. The script:
1. Loads `graph.json` (220 nodes, 304 edges)
2. Traverses the documented graph paths for each use case
3. Extracts the relevant subgraph, node attributes, and edge metadata
4. Outputs a structured result: key nodes, cited source files, quantified metrics,
   and the cross-document connections that make this non-trivially interesting

### Phase 2 — Presentation
Build a 7-slide deck:
- Slide 1: Cover — "BTG Utilities Knowledge Graph: Intelligence Layer for Private Credit"
- Slide 2: What it is + how it works (3-panel: documents → graph → query)
- Slides 3-7: One slide per use case (problem / graph path / real output / key insight)

### Phase 3 — Report
1-page written brief per use case, suitable for the Head of Private Credit. Each brief:
- States the credit question in plain language
- Shows the graph answer with cited sources
- Highlights the insight that was *only discoverable* via the graph (not any single document)
- Gives the actionable credit implication

---

## Why This Matters — The Core Argument for BTG

| Without the graph | With the graph |
|---|---|
| Analyst reads 4-6 documents per question | One query, cited answers in seconds |
| Cross-document connections are missed | Inferred edges surface hidden risks |
| Portfolio-wide stress testing takes weeks | Run across all positions in one query |
| Regulatory changes tracked ad hoc | Real-time: new document in → graph updates |
| 27,658 words to re-read per new question | ~71× fewer tokens per query |

The knowledge graph is not a replacement for credit judgment — it is a **research accelerator**
that ensures no document, no connection, and no regulatory cascade is missed when it matters.
