# Graph Report - ./raw  (2026-04-08)

## Corpus Check
- Corpus is ~27,658 words - fits in a single context window. You may not need a graph.

## Summary
- 220 nodes · 304 edges · 27 communities detected
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 51 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Índice de Crédito BTG Utilities` - 22 edges
2. `Riscos Políticos e Regulatórios 2026` - 15 edges
3. `Políticas Energéticas Brasil` - 11 edges
4. `SBCE Mercado Brasileiro de Carbono` - 11 edges
5. `ANEEL (Agência Nacional de Energia Elétrica)` - 11 edges
6. `Transformação Digital das Distribuidoras` - 10 edges
7. `Tendências Tecnológicas Setor Elétrico Brasileiro` - 10 edges
8. `CPFL Energia (CPFL3)` - 10 edges
9. `Neoenergia (NEOE3)` - 9 edges
10. `Cemig (CMIG3/CMIG4)` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Green Bond / Instrumento ESG Verde` --semantically_similar_to--> `Debentures Incentivadas (Lei 12.431)`  [INFERRED] [semantically similar]
  raw/politicas/carbon_market_sbce.md → raw/tecnologia/economics_renovaveis.md
- `ONS Cenários de Estresse para Crédito` --conceptually_related_to--> `Cemig Cliff de Concessões Hidrelétricas 2027-2030`  [INFERRED]
  raw/regulacao/ons_risco_hidrologico.md → raw/empresas/cemig/perfil_credito.md
- `Cemig-D DEA Score e Problema de OPEX` --semantically_similar_to--> `ANEEL DEA — Análise Envoltória de Dados Eficiência Operacional`  [INFERRED] [semantically similar]
  raw/empresas/cemig/perfil_credito.md → raw/regulacao/aneel_tarifas_rtp.md
- `Risco Hidrológico GSF — Generation Scaling Factor` --semantically_similar_to--> `CCEE GSF e MRR — Mecanismo de Repartição de Riscos`  [INFERRED] [semantically similar]
  raw/mercado/dinamicas_mercado.md → raw/regulacao/ccee_regras_comercializacao.md
- `ONS e CCEE — Operação e Comercialização` --semantically_similar_to--> `CCEE Regras de Comercialização e Mecânica de Mercado`  [INFERRED] [semantically similar]
  raw/regulacao/ons_ccee_mercado.md → raw/regulacao/ccee_regras_comercializacao.md

## Hyperedges (group relationships)
- **Renewable Energy Technologies** — tecnologia_solar_fotovoltaica, tecnologia_eolica, tecnologia_hidreletricas, tecnologia_hidrogenio_verde, tecnologia_bess [INFERRED 0.90]
- **Energy Transition and Climate Policy Cluster** — politicas_pne, politicas_descarbonizacao, politicas_ndc_brasil, politicas_cnpe, politicas_epe [INFERRED 0.85]
- **Major Brazilian Energy Utilities** — empresas_eletrobras, empresas_cpfl, empresas_equatorial, empresas_energisa, empresas_enel_brasil, empresas_neoenergia, empresas_cemig, empresas_copel, empresas_engie_brasil, empresas_aes_brasil [EXTRACTED 1.00]
- **Brazilian Energy Market Environments** — mercado_acr, mercado_acl, mercado_livre, mercado_pld [EXTRACTED 1.00]
- **Brazilian Energy Regulatory Bodies** — regulacao_aneel, regulacao_ons, regulacao_ccee, regulacao_mme [EXTRACTED 1.00]
- **Distribuidoras sob Revisão Tarifária ANEEL (WACC + DEA + RAB)** — entity_aneel, concept_rtp, concept_wacc, concept_dea, concept_rab, entity_equatorial, entity_energisa, entity_cpfl, entity_neoenergia, entity_cemig, entity_copel [EXTRACTED 0.95]
- **Compliance de Carbono SBCE para Geração Termelétrica** — concept_sbce, concept_cbe, concept_sinase, entity_mcti, concept_lei_15042 [EXTRACTED 0.92]
- **Estrutura de Project Finance Renovável (BNDES + Debentures + DSCR)** — concept_project_finance, entity_bndes, concept_debenture_incentivada, concept_dscr, concept_lcoe [INFERRED 0.82]
- **Risco Hidrológico — GSF, CMO, PLD e Impacto nas Geradoras** — ons_gsf_detalhamento, ons_cmo_conceito, ccee_pld_calculo, ons_mrr_mecanismo [INFERRED 0.88]
- **RTP — WACC, RAB e DEA determinam EBITDA Regulatório das Distribuidoras** — aneel_wacc_regulatorio, aneel_rab, aneel_dea_eficiencia, aneel_calendario_rtps [EXTRACTED 0.92]
- **Abertura ACL — Migração, Perda de Receita e Estratégias de Mitigação** — mercado_acl_migracao, acl_mecanismo_receita, acl_compensacao_regulatoria, acl_estrategias_distribuidoras [EXTRACTED 0.90]

## Communities

### Community 0 - "ACL Migração e Concessões"
Cohesion: 0.08
Nodes (48): Cemig Concessões e Contratos, ACL (Ambiente de Contratação Livre — Mercado Livre), Abertura Total do Mercado Livre ACL 2028, ACR (Ambiente de Contratação Regulada), Angra 3 (Eletronuclear — Risco CAPEX), CDE (Conta de Desenvolvimento Energético), Concessões Hidrelétricas Cemig (Cliff 2027-2030), Copel Telecom (Ativo de Fibra Ótica) (+40 more)

### Community 1 - "Regulação Tarifária RTP"
Cohesion: 0.09
Nodes (25): ACL Mecanismo de Compensação Regulatória ANEEL CP 038/2025, Estratégias das Distribuidoras para Mitigar Perda ACL, ACL Mecanismo de Receita das Distribuidoras, ANEEL Calendário de RTPs — Próximos Ciclos, ANEEL CVA — Conta de Variação de Ativos, ANEEL DEA — Análise Envoltória de Dados Eficiência Operacional, ANEEL DEC/FEC — Indicadores de Qualidade e Penalidades, ANEEL Encargos Setoriais — CDE, TUST, TUSD, ESS, EER (+17 more)

### Community 2 - "Digitalização e Smart Grid"
Cohesion: 0.14
Nodes (23): AMI (Advanced Metering Infrastructure), BESS (Battery Energy Storage System), DEC/FEC (Indicadores de Continuidade de Energia), Resposta à Demanda (Demand Response), Hidrogênio Verde (H2V), Lei 14.827/2024 (Marco Legal Offshore Wind), Eólica Offshore, PNT (Perdas Não Técnicas de Energia) (+15 more)

### Community 3 - "CCEE Mercado e Liquidação"
Cohesion: 0.11
Nodes (21): CCEE Estrutura ACR e ACL — Ambientes de Contratação, CCEE Contabilização e Ciclo de Liquidação, CCEE Encargos Setoriais — CDE, ESS, EER, CCEE GSF e MRR — Mecanismo de Repartição de Riscos, CCEE PLD — Cálculo e Limites, CCEE Regras de Comercialização e Mecânica de Mercado, ONS e CCEE — Operação e Comercialização, ONS Cenários de Estresse para Crédito (+13 more)

### Community 4 - "ANEEL Concessões e Distribuição"
Cohesion: 0.13
Nodes (19): ANEEL Caducidade — Risco Extremo de Concessão, ANEEL Concessões de Distribuição — Framework e Riscos, ANEEL Fundo de Garantia e Reversão, ANEEL Cláusula de Mudança de Controle, ANEEL Renovação vs Re-leilão — Dilema 2028-2032, Cemig Cliff de Concessões Hidrelétricas 2027-2030, Cemig-D DEA Score e Problema de OPEX, Cemig Estrutura de Dívida e Covenants (+11 more)

### Community 5 - "ESG Carbono e Finanças Verdes"
Cohesion: 0.16
Nodes (17): SBCE Mercado Brasileiro de Carbono, CBE (Cota Brasileira de Emissões), Green Bond / Instrumento ESG Verde, I-REC (Certificado Internacional de Energia Renovável), Lei 15.042/2024 (Marco Legal SBCE Carbono), Programa Luz para Todos (Fase III), NDC Brasil (Metas Climáticas Paris), Plano Nacional de Energia 2050 (+9 more)

### Community 6 - "Políticas Energéticas e GD"
Cohesion: 0.15
Nodes (13): Geração Distribuída, CNPE (Conselho Nacional de Política Energética), Descarbonização e Transição Energética, EPE (Empresa de Pesquisa Energética), NDC Brasil (Metas Climáticas), Plano Nacional de Energia 2050 (PNE), MME (Ministério de Minas e Energia), Medição Inteligente (AMI/AMR) (+5 more)

### Community 7 - "Estrutura do Mercado Elétrico"
Cohesion: 0.2
Nodes (10): Ambiente de Contratação Livre (ACL), Ambiente de Contratação Regulada (ACR), Leilões de Energia (A-3, A-5, A-6), Mercado Livre (Consumidores Livres), Preço de Liquidação das Diferenças (PLD), ANEEL (Agência Nacional de Energia Elétrica), CCEE (Câmara de Comercialização de Energia Elétrica), Procedimentos de Distribuição (PRODIST) (+2 more)

### Community 8 - "Novas Tecnologias e Legislação"
Cohesion: 0.24
Nodes (10): Lei 14.827/2024 — Eólica Offshore, Lei 15.042/2024 — SBCE Mercado Brasileiro de Carbono, Leilão A-3 2025 — Primeiro Offshore Comercial, Leilão A-5 — Estrutura e Histórico, Perfil de Risco de Contrato A-5 — Análise de Crédito, Leilões de Energia — Histórico e Pipeline 2019-2028, Leilões de Transmissão 2019-2025, Marco Regulatório de Novas Tecnologias — Setor Elétrico (+2 more)

### Community 9 - "Eletrobras Pós-Privatização"
Cohesion: 0.32
Nodes (8): Eletrobras Angra 3 — Risco de CAPEX Nuclear, Eletrobras Compulsório e Obrigações da Privatização, Eletrobras Concessões e Contratos, Eletrobras Eficiência Compulsória e Desinvestimentos, Eletrobras Perfil de Crédito, Eletrobras Privatização 2022, Eletrobras RGR — Reserva Global de Reversão, Rationale: Eficiência Compulsória como Condição da Privatização Eletrobras

### Community 10 - "Financiamento e Project Finance"
Cohesion: 0.33
Nodes (7): Debentures Incentivadas (Lei 12.431), DSCR (Debt Service Coverage Ratio), Energia Eólica Onshore, LCOE (Levelized Cost of Energy), Project Finance Renovável, Rationale: Debentures Incentivadas Reduzem Custo de Capital, Economia das Energias Renováveis

### Community 11 - "ONS e Operação do SIN"
Cohesion: 0.67
Nodes (3): Sistema Interligado Nacional (SIN), ONS (Operador Nacional do Sistema Elétrico), Procedimentos de Rede ONS

### Community 12 - "Privatizações do Setor"
Cohesion: 1.0
Nodes (2): Eletrobras, Privatizações e Concessões

### Community 13 - "Hidrelétricas"
Cohesion: 1.0
Nodes (1): PCH e UHE (Hidrelétricas)

### Community 14 - "Luz Para Todos"
Cohesion: 1.0
Nodes (1): Programa Luz para Todos

### Community 15 - "Marco do Saneamento"
Cohesion: 1.0
Nodes (1): Marco Legal do Saneamento

### Community 16 - "CPFL Energia"
Cohesion: 1.0
Nodes (1): CPFL Energia

### Community 17 - "Equatorial Energia"
Cohesion: 1.0
Nodes (1): Equatorial Energia

### Community 18 - "Energisa"
Cohesion: 1.0
Nodes (1): Energisa

### Community 19 - "Enel Brasil"
Cohesion: 1.0
Nodes (1): Enel Brasil

### Community 20 - "Neoenergia"
Cohesion: 1.0
Nodes (1): Neoenergia

### Community 21 - "Cemig"
Cohesion: 1.0
Nodes (1): Cemig

### Community 22 - "Copel"
Cohesion: 1.0
Nodes (1): Copel

### Community 23 - "Engie Brasil"
Cohesion: 1.0
Nodes (1): ENGIE Brasil

### Community 24 - "AES Brasil"
Cohesion: 1.0
Nodes (1): AES Brasil

### Community 25 - "ONS Operador"
Cohesion: 1.0
Nodes (1): ONS (Operador Nacional do Sistema)

### Community 26 - "TUSD"
Cohesion: 1.0
Nodes (1): TUSD (Tarifa de Uso do Sistema de Distribuição)

## Knowledge Gaps
- **79 isolated node(s):** `Medição Inteligente (AMI/AMR)`, `Energia Eólica Onshore/Offshore`, `PCH e UHE (Hidrelétricas)`, `Hidrogênio Verde`, `Programa Luz para Todos` (+74 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Privatizações do Setor`** (2 nodes): `Eletrobras`, `Privatizações e Concessões`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Hidrelétricas`** (1 nodes): `PCH e UHE (Hidrelétricas)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Luz Para Todos`** (1 nodes): `Programa Luz para Todos`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Marco do Saneamento`** (1 nodes): `Marco Legal do Saneamento`
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
- **Thin community `Engie Brasil`** (1 nodes): `ENGIE Brasil`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `AES Brasil`** (1 nodes): `AES Brasil`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `ONS Operador`** (1 nodes): `ONS (Operador Nacional do Sistema)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `TUSD`** (1 nodes): `TUSD (Tarifa de Uso do Sistema de Distribuição)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Índice de Crédito BTG Utilities` connect `ACL Migração e Concessões` to `Digitalização e Smart Grid`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **What connects `Medição Inteligente (AMI/AMR)`, `Energia Eólica Onshore/Offshore`, `PCH e UHE (Hidrelétricas)` to the rest of the system?**
  _79 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `ACL Migração e Concessões` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
- **Should `Regulação Tarifária RTP` be split into smaller, more focused modules?**
  _Cohesion score 0.09 - nodes in this community are weakly interconnected._
- **Should `Digitalização e Smart Grid` be split into smaller, more focused modules?**
  _Cohesion score 0.14 - nodes in this community are weakly interconnected._
- **Should `CCEE Mercado e Liquidação` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._
- **Should `ANEEL Concessões e Distribuição` be split into smaller, more focused modules?**
  _Cohesion score 0.13 - nodes in this community are weakly interconnected._