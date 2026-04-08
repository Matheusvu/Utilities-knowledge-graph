# Graph Report - ./raw  (2026-04-08)

## Corpus Check
- Corpus is ~274 words - fits in a single context window. You may not need a graph.

## Summary
- 40 nodes · 24 edges · 18 communities detected
- Extraction: 42% EXTRACTED · 58% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Descarbonização e Transição Energética` - 6 edges
2. `CCEE (Câmara de Comercialização de Energia Elétrica)` - 4 edges
3. `Plano Nacional de Energia 2050 (PNE)` - 4 edges
4. `ANEEL (Agência Nacional de Energia Elétrica)` - 3 edges
5. `Ambiente de Contratação Regulada (ACR)` - 3 edges
6. `ONS (Operador Nacional do Sistema Elétrico)` - 2 edges
7. `Ambiente de Contratação Livre (ACL)` - 2 edges
8. `Energia Solar Fotovoltaica` - 2 edges
9. `Armazenamento de Energia (BESS)` - 2 edges
10. `Redes Inteligentes (Smart Grids)` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Descarbonização e Transição Energética` --conceptually_related_to--> `Energia Solar Fotovoltaica`  [INFERRED]
  raw/politicas/README.md → raw/tecnologia/README.md
- `Descarbonização e Transição Energética` --conceptually_related_to--> `Energia Eólica Onshore/Offshore`  [INFERRED]
  raw/politicas/README.md → raw/tecnologia/README.md
- `Descarbonização e Transição Energética` --conceptually_related_to--> `Armazenamento de Energia (BESS)`  [INFERRED]
  raw/politicas/README.md → raw/tecnologia/README.md
- `Descarbonização e Transição Energética` --conceptually_related_to--> `Hidrogênio Verde`  [INFERRED]
  raw/politicas/README.md → raw/tecnologia/README.md
- `ANEEL (Agência Nacional de Energia Elétrica)` --references--> `Ambiente de Contratação Regulada (ACR)`  [INFERRED]
  raw/regulacao/README.md → raw/mercado/README.md

## Hyperedges (group relationships)
- **Brazilian Energy Regulatory Bodies** — regulacao_aneel, regulacao_ons, regulacao_ccee, regulacao_mme [EXTRACTED 1.00]
- **Brazilian Energy Market Environments** — mercado_acr, mercado_acl, mercado_livre, mercado_pld [EXTRACTED 1.00]
- **Renewable Energy Technologies** — tecnologia_solar_fotovoltaica, tecnologia_eolica, tecnologia_hidreletricas, tecnologia_hidrogenio_verde, tecnologia_bess [INFERRED 0.90]
- **Major Brazilian Energy Utilities** — empresas_eletrobras, empresas_cpfl, empresas_equatorial, empresas_energisa, empresas_enel_brasil, empresas_neoenergia, empresas_cemig, empresas_copel, empresas_engie_brasil, empresas_aes_brasil [EXTRACTED 1.00]
- **Energy Transition and Climate Policy Cluster** — politicas_pne, politicas_descarbonizacao, politicas_ndc_brasil, politicas_cnpe, politicas_epe [INFERRED 0.85]

## Communities

### Community 0 - "Energy Transition & Renewables"
Cohesion: 0.22
Nodes (9): Geração Distribuída, Descarbonização e Transição Energética, NDC Brasil (Metas Climáticas), Medição Inteligente (AMI/AMR), Armazenamento de Energia (BESS), Energia Eólica Onshore/Offshore, Hidrogênio Verde, Redes Inteligentes (Smart Grids) (+1 more)

### Community 1 - "Free Market & CCEE Settlement"
Cohesion: 0.4
Nodes (5): Ambiente de Contratação Livre (ACL), Mercado Livre (Consumidores Livres), Preço de Liquidação das Diferenças (PLD), CCEE (Câmara de Comercialização de Energia Elétrica), Regras de Comercialização CCEE

### Community 2 - "Regulated Market & ANEEL"
Cohesion: 0.4
Nodes (5): Ambiente de Contratação Regulada (ACR), Leilões de Energia (A-3, A-5, A-6), ANEEL (Agência Nacional de Energia Elétrica), Procedimentos de Distribuição (PRODIST), Resolução Normativa ANEEL

### Community 3 - "National Energy Planning"
Cohesion: 0.5
Nodes (4): CNPE (Conselho Nacional de Política Energética), EPE (Empresa de Pesquisa Energética), Plano Nacional de Energia 2050 (PNE), MME (Ministério de Minas e Energia)

### Community 4 - "Grid Operations & ONS"
Cohesion: 0.67
Nodes (3): Sistema Interligado Nacional (SIN), ONS (Operador Nacional do Sistema Elétrico), Procedimentos de Rede ONS

### Community 5 - "Eletrobras & Privatization"
Cohesion: 1.0
Nodes (2): Eletrobras, Privatizações e Concessões

### Community 6 - "CPFL Energia"
Cohesion: 1.0
Nodes (1): CPFL Energia

### Community 7 - "Equatorial Energia"
Cohesion: 1.0
Nodes (1): Equatorial Energia

### Community 8 - "Energisa"
Cohesion: 1.0
Nodes (1): Energisa

### Community 9 - "Enel Brasil"
Cohesion: 1.0
Nodes (1): Enel Brasil

### Community 10 - "Neoenergia"
Cohesion: 1.0
Nodes (1): Neoenergia

### Community 11 - "Cemig"
Cohesion: 1.0
Nodes (1): Cemig

### Community 12 - "Copel"
Cohesion: 1.0
Nodes (1): Copel

### Community 13 - "ENGIE Brasil"
Cohesion: 1.0
Nodes (1): ENGIE Brasil

### Community 14 - "AES Brasil"
Cohesion: 1.0
Nodes (1): AES Brasil

### Community 15 - "Hydropower (PCH/UHE)"
Cohesion: 1.0
Nodes (1): PCH e UHE (Hidrelétricas)

### Community 16 - "Rural Electrification"
Cohesion: 1.0
Nodes (1): Programa Luz para Todos

### Community 17 - "Sanitation Framework"
Cohesion: 1.0
Nodes (1): Marco Legal do Saneamento

## Knowledge Gaps
- **30 isolated node(s):** `MME (Ministério de Minas e Energia)`, `Resolução Normativa ANEEL`, `Procedimentos de Distribuição (PRODIST)`, `Procedimentos de Rede ONS`, `Regras de Comercialização CCEE` (+25 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Eletrobras & Privatization`** (2 nodes): `Eletrobras`, `Privatizações e Concessões`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `CPFL Energia`** (1 nodes): `CPFL Energia`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Equatorial Energia`** (1 nodes): `Equatorial Energia`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Energisa`** (1 nodes): `Energisa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Enel Brasil`** (1 nodes): `Enel Brasil`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Neoenergia`** (1 nodes): `Neoenergia`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Cemig`** (1 nodes): `Cemig`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Copel`** (1 nodes): `Copel`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `ENGIE Brasil`** (1 nodes): `ENGIE Brasil`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `AES Brasil`** (1 nodes): `AES Brasil`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Hydropower (PCH/UHE)`** (1 nodes): `PCH e UHE (Hidrelétricas)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Rural Electrification`** (1 nodes): `Programa Luz para Todos`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Sanitation Framework`** (1 nodes): `Marco Legal do Saneamento`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Descarbonização e Transição Energética` connect `Energy Transition & Renewables` to `National Energy Planning`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Why does `Plano Nacional de Energia 2050 (PNE)` connect `National Energy Planning` to `Energy Transition & Renewables`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Why does `CCEE (Câmara de Comercialização de Energia Elétrica)` connect `Free Market & CCEE Settlement` to `Regulated Market & ANEEL`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `Descarbonização e Transição Energética` (e.g. with `Plano Nacional de Energia 2050 (PNE)` and `NDC Brasil (Metas Climáticas)`) actually correct?**
  _`Descarbonização e Transição Energética` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Plano Nacional de Energia 2050 (PNE)` (e.g. with `MME (Ministério de Minas e Energia)` and `Descarbonização e Transição Energética`) actually correct?**
  _`Plano Nacional de Energia 2050 (PNE)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Ambiente de Contratação Regulada (ACR)` (e.g. with `Leilões de Energia (A-3, A-5, A-6)` and `ANEEL (Agência Nacional de Energia Elétrica)`) actually correct?**
  _`Ambiente de Contratação Regulada (ACR)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `MME (Ministério de Minas e Energia)`, `Resolução Normativa ANEEL`, `Procedimentos de Distribuição (PRODIST)` to the rest of the system?**
  _30 weakly-connected nodes found - possible documentation gaps or missing edges._