# Brazilian Electricity Sector — Source Inventory

> **Source:** Perplexity Deep Research, run 2026-06-17, using `research/perplexity_source_discovery_prompt.md`.
> **Status:** raw research output (archived verbatim except Perplexity's internal citation tokens, which were removed for readability — all source URLs are preserved in the tables).
> **Use:** this is the input for `sources/registry.yml` (PLAN.md Phase 1). Treat URLs as candidates to verify at fetch time; portal paths can rotate.

---

## Executive summary

A relatively small set of primary hubs does most of the heavy lifting for a credit-grade monitoring pipeline:
- **ONS** — system operation and curtailment (physical truth).
- **ANEEL** — regulatory acts, generation registries (SIGA), tariffs, GD, concessions, distributor datasets (legal/rule layer + asset master).
- **CCEE** — market, PLD, contracts, migration, commercial settlement (settlement/cash layer).
- **EPE / MME / CNPE** — planning and policy.
- **CVM / B3 / ANBIMA** — issuer, debenture, listed-company monitoring (credit layer).
- **ANA / INMET / INPE** — hydrology and weather.

ONS's open-data portal + curtailment documentation are the single most important starting point for the wind/solar constrained-off monitor (plant-level restricted-generation datasets + operator explanation of reliability-vs-energetic logic). ANEEL and CCEE provide the **economic consequence layer**: rulemaking, compensation methodology, settlement implementation, litigation. CKAN portals (ONS, ANEEL, CCEE, CVM) materially improve ingestability, but historical coverage, field dictionaries, and endpoint stability vary by source.

---

## System operation & physical data (ONS)

| id (proposed) | Dataset | URL | Provides | Format/Access | Tier / Curtailment relevance | Notes |
|---|---|---|---|---|---|---|
| ons_open_data | ONS Dados Abertos (hub) | https://dados.ons.org.br/ | Official open-data hub: operation, hydrology, transmission/interchange, generation, load, curtailment | CKAN; bulk + API | PRIMARY / High | Highest-value operational hub |
| ons_geracao_usina_horaria | Geração por Usina (horária) | https://dados.ons.org.br/dataset/geracao-usina-2 | Hourly generation by plant | CSV/XLSX/Parquet | PRIMARY / High | Core denominator for plant-level curtailment intensity |
| ons_curva_carga_horaria | Curva de Carga Horária | https://dados.ons.org.br/dataset/curva-carga-horaria | Hourly load curve | CSV/XLSX/Parquet | PRIMARY / Medium | Distinguishes energetic surplus vs local reliability |
| ons_balanco_energia_subsistema | Balanço de Energia nos Subsistemas | https://dados.ons.org.br/dataset/balanco-energia-subsistema | Supply-demand/energy balance by subsystem | CSV/XLSX/Parquet | PRIMARY / High | Regional surplus diagnostics |
| ons_intercambios_subsistemas | Intercâmbios Entre Subsistemas | https://dados.ons.org.br/dataset/intercambios-entre-subsistemas | Subsystem interchange flows | XLSX/CSV | PRIMARY / High | NE/N→SE/CO export-bottleneck diagnostics |
| ons_ena_diario_subsistema | ENA Diário por Subsistema | https://dados.ons.org.br/dataset/ena-diario-subsistema | Daily natural inflow energy by subsystem | CSV/XLSX/Parquet | PRIMARY / Medium | Hydrologic scarcity, dispatch, PLD |
| ons_ear_diario_subsistema | EAR Diário por Subsistema | https://dados.ons.org.br/dataset/ear-diario-subsistema | Daily stored-energy/reservoir by subsystem | CSV/XLSX/Parquet | PRIMARY / Medium | Reservoir risk |
| ons_coff_eolica_usi | **Constrained-off eólica por usina** | https://dados.ons.org.br/dataset/restricao_coff_eolica_usi | Restricted wind generation by plant + cause classification | CSV/XLSX/Parquet | PRIMARY / **High** | One of the most important datasets in the catalog; history ≥ 2022 |
| ons_coff_eolica_geracao | Constrained-off eólica detalhada | https://dados.ons.org.br/dataset/restricao_coff_eolica_geracao | Detailed wind constrained-off records | CSV/XLSX/Parquet | PRIMARY / **High** | Best detail layer (published Dec-2022) |
| ons_coff_fotovoltaica_usi | **Constrained-off fotovoltaica por usina** | https://dados.ons.org.br/dataset/restricao_coff_fotovoltaica_usi | Restricted solar generation by plant + cause | CSV/XLSX/Parquet | PRIMARY / **High** | Solar counterpart to wind series |
| ons_coff_fotovoltaica_geracao | Constrained-off fotovoltaica detalhada | https://dados.ons.org.br/dataset/restricao_coff_fotovoltaica_geracao | Detailed solar constrained-off records | CSV/XLSX/Parquet | PRIMARY / **High** | Forensic/settlement support |
| ons_tempo_real | ONS Dados em Tempo Real | https://www.ons.org.br/paginas/resultados-da-operacao/dados-em-tempo-real | Real-time load/generation/reservoir dashboards | HTML/dashboard | PRIMARY / Medium | Event detection, not warehousing |

**ONS curtailment methodology docs (PDF/HTML, PRIMARY / High):**
- FAQ / hub: https://www.ons.org.br/Paginas/faq_curtailment.aspx
- NT-ONS DOP 0022/2025 — Critérios para Gestão de Excedentes Energéticos: https://www.ons.org.br/AcervoDigitalDocumentosEPublicacoes/NT-ONS%20DOP%200022.2025%20-%20Crit%C3%A9rios%20para%20Gest%C3%A3o%20de%20Excedentes%20Energ%C3%A9ticos.pdf
- RT DGL-ONS 0189-2025 — GT Curtailment (diagnostic/prospective): https://www.ons.org.br/AcervoDigitalDocumentosEPublicacoes/RT%20DGL-ONS%200189-2025%20-%20GT%20Curtailment%20rev1.pdf
- RO-AO.BR.13 — network procedure: https://www.ons.org.br/paginas/sobre-o-sin/procedimentos-de-rede/vigentes/submodulos-operacao/ro-ao-br-13.pdf

---

## Market & commercial data (CCEE)

| id (proposed) | Dataset | URL | Provides | Tier / Relevance | Notes |
|---|---|---|---|---|---|
| ccee_open_data | Dados Abertos CCEE (hub) | https://dadosabertos.ccee.org.br/ | Market, consumption, contracts, PLD, generation, migration | PRIMARY / High | Core market-data complement |
| ccee_pld_horario | PLD Horário | https://dadosabertos.ccee.org.br/dataset/pld_horario | Hourly spot price by submarket | PRIMARY / Medium | Merchant exposure, scarcity pricing |
| ccee_pld_media_diaria_mensal | PLD média diária/mensal | https://dadosabertos.ccee.org.br/dataset/pld_media_diaria_mensal | Daily/monthly PLD aggregates | PRIMARY / Low | Valuation/backfill |
| ccee_consumo_ambiente | Consumo mensal por ambiente (ACL/ACR) | https://dadosabertos.ccee.org.br/dataset/consumo_mensal_ambiente_comercializacao | Monthly consumption ACL vs ACR | PRIMARY / Low | Free-market migration indicator |
| ccee_varejista_consumidor | Mercado varejista / migração | https://dadosabertos.ccee.org.br/dataset/varejista_consumidor | Consumer migration, retail agents | PRIMARY / Low | Distributor-credit views |
| ccee_geracao | Geração (dataset family) | https://dadosabertos.ccee.org.br/dataset/?tags=gera%C3%A7%C3%A3o | Hourly generation (Mar-2024+), historical ZIPs 2018–2024 | PRIMARY / Medium | Commercial-side reconciliation vs ONS |
| ccee_leilao_gf | Leilão GF disponibilidade | https://dadosabertos.ccee.org.br/dataset/disponibilidade_leilao_gf_geracao | Generation adequacy/guarantee items | PRIMARY / Low | |
| ccee_leilao_receita | Leilão disponibilidade de receita | https://dadosabertos.ccee.org.br/dataset/disponibilidade_leilao_receita | Availability/revenue auction data | PRIMARY / Low | |
| ccee_acervo | Acervo CCEE (docs) | https://www.ccee.org.br/acervo-ccee | InfoPLD, InfoMercado, InfoContratos, rules, communiqués | PRIMARY / High | InfoContratos useful for ACR exposure mapping |
| ccee_contabilizacao | Contabilização / settlement | https://www.ccee.org.br/contabilizacao | Accounting/settlement process + calendars | PRIMARY / High | Where compensation reaccounting is operationalized |

**CCEE constrained-off / compensation communications (HTML + linked reports, PRIMARY / High):**
- Wind definitive-methodology package: https://www.ccee.org.br/-/co-ccee-divulga-pacote-de-relatorios-relacionados-a-metodologia-definitiva-do-constrained-off-para-usinas-eolicas.-confira-o-que-muda-
- Wind reaccounting/ressarcimento schedule: https://www.ccee.org.br/-/cronograma-de-operacionalizacao-das-recontabilizacoes-e-ressarcimentos-associados-ao-constrained-off-para-usinas-eolicas-metodologia-definitiva-
- Solar definitive-period (from Apr-2024): https://www.ccee.org.br/-/co-apuracao-dos-ressarcimentos-para-usinas-solares-fotovoltaicas-vinculadas-a-leiloes-do-mercado-regulado-para-o-periodo-definitivo-do-constrained-off-a-partir-de-abril-2024-
- Lei 15.269/2025 apurações/reapurações (wind+solar): https://www.ccee.org.br/-/informacoes-sobre-as-apuracoes-e-reapuracoes-dos-ressarcimentos-associados-a-constrained-off-usinas-eolicas-e-solares-lei-15.269-2025

---

## Regulation, registry, planning & policy (ANEEL / EPE / MME)

| id (proposed) | Source | URL | Provides | Tier / Relevance | Notes |
|---|---|---|---|---|---|
| aneel_open_data | ANEEL Dados Abertos (hub) | https://dadosabertos.aneel.gov.br/ | Generation, tariffs, GD, distribution, transmission, inspection | PRIMARY / High | Central regulatory data hub; CKAN API |
| aneel_siga | **SIGA** (generation registry) | https://dadosabertos.aneel.gov.br/dataset/siga-sistema-de-informacoes-de-geracao-da-aneel | Plant registry, technology, location, status, installed capacity | PRIMARY / Medium | **Official asset master** (plant identity / CEG) |
| aneel_gd | Geração Distribuída registry | https://dadosabertos.aneel.gov.br/dataset/relacao-de-empreendimentos-de-geracao-distribuida | GD project-level registry | PRIMARY / Low | Distributor bypass / migration |
| aneel_tarifas | Tarifas de aplicação distribuidoras | https://dadosabertos.aneel.gov.br/dataset/tarifas-de-aplicacao-das-distribuidoras-de-energia-eletrica | Distributor tariff tables | PRIMARY / Low | Distributor cash-flow |
| aneel_siget | SIGET (transmission geo) | https://dadosabertos.aneel.gov.br/dataset/siget-sistema-de-gestao-da-transmissao | Transmission geospatial/asset info | PRIMARY / Medium | Bottleneck mapping near export corridors |
| aneel_leiloes | Resultado de leilões de geração | https://dadosabertos.aneel.gov.br/dataset/resultado-dos-leiloes-de-geracao | Generation-auction results | PRIMARY / Low | Contracted revenues, sponsor mapping |
| aneel_bdgd | BDGD (distribution geodata) | https://dadosabertos.aneel.gov.br/dataset/base-de-dados-geografica-da-distribuidora-bdgd | Georeferenced distribution network | PRIMARY / Low | |
| aneel_samp | SAMP (distribution market) | https://dadosabertos.aneel.gov.br/dataset/samp-sistema-de-acompanhamento-de-informacoes-de-mercado-para-regulacao-e-fiscalizacao-do-segmento-de-distribuicao | Consumer classes, market supervision | PRIMARY / Low | Distributor-market trends |
| aneel_fiscalizacao | Fiscalização / sanctions | https://dadosabertos.aneel.gov.br/group/fiscalizacao | Notificações, autos de infração | PRIMARY / Low | Covenant/compliance screens |
| aneel_reunioes | Reuniões Públicas / decisões | https://www.gov.br/aneel/pt-br/reunioes-publicas | Pautas, atas, monocratic decisions | PRIMARY / High | Fastest official track of regulatory decisions |
| aneel_pesquisa_publica | Pesquisa Pública / SEI / Sicnet2 | https://www.gov.br/aneel/pt-br/canais_atendimento/processo-eletronico/pesquisa-publica | Process/docket files | PRIMARY / High | Following compensation dockets/litigation |
| aneel_agenda | Agenda Regulatória | https://www.gov.br/aneel/pt-br/assuntos/governanca-regulatoria/agenda-regulatoria | Regulatory agenda / priority themes | PRIMARY / Medium | |
| epe_portal | EPE portal | https://www.epe.gov.br/ | Planning outlooks, auction studies, statistics | PRIMARY / Medium | Canonical planning counterpart to ONS |
| epe_pde_2035 | PDE 2035 | https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/plano-decenal-de-expansao-de-energia-2035 | Ten-year expansion plan | PRIMARY / Medium | Capacity/network/curtailment-sensitivity scenarios |
| epe_ben | BEN séries históricas | https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/balanco-energetico-nacional-ben-series-historicas-completas | Long historical energy balances | PRIMARY / Low | Macro reference |
| epe_anuario | Anuário Estatístico EE | https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/anuario-estatistico-de-energia-eletrica | Annual electricity statistics | PRIMARY / Low | Market sizing/benchmarking |
| epe_webmap | Webmap EPE | https://gisepeprd2.epe.gov.br/WebMapEPE/ | Geospatial project/infrastructure mapping | PRIMARY / Medium | Limited programmatic export |
| epe_demanda | Caderno de Demanda de Eletricidade | https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/caderno-de-demanda-de-eletricidade | Demand outlook workbook | PRIMARY / Low | |
| mme_boletim | MME Boletim de Monitoramento | https://www.gov.br/mme/pt-br/assuntos/secretarias/see/monitoramento-do-sistema-eletrico/boletim-de-monitoramento-do-sistema-eletrico | Monthly electricity-system bulletin (since 2009) | PRIMARY / Medium | Macro-operational overlay |
| cnpe | CNPE resolutions | https://www.gov.br/mme/pt-br/assuntos/cnpe | CNPE decisions (auctions, supply security) | PRIMARY / Low | |
| ndc | Brazil NDC | https://www.gov.br/mma/pt-br/composicao/secex/cgclima/ndc | Climate commitments | PRIMARY / Low | Transition context |
| sbce | SBCE carbon-market tracker | https://www.gov.br/fazenda/pt-br/assuntos/sustentabilidade/sistema-brasileiro-de-comercio-de-emissoes | Brazilian ETS framework | PRIMARY / Low | Long-term renewable valuation |

---

## Financial / issuer / projects / meteorology / water

| id (proposed) | Source | URL | Provides | Tier / Relevance | Notes |
|---|---|---|---|---|---|
| cvm_open_data | CVM Dados Abertos (hub) | https://dados.cvm.gov.br/ | Listed-company filings, public offers | PRIMARY / High | Primary machine-readable issuer source; CKAN |
| cvm_itr | ITR (quarterly statements) | https://dados.cvm.gov.br/dataset/cia_aberta-doc-itr | Quarterly financials (history to 2011) | PRIMARY / High | ZIP bulk, stable naming (e.g. `.../itr_cia_aberta_2026.zip`) |
| cvm_dfp | DFP (annual statements) | https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp | Standardized annual statements | PRIMARY / High | |
| cvm_fre | FRE (reference forms) | https://dados.cvm.gov.br/dataset/cia_aberta-doc-fre | Business, risk, governance, debt, projects | PRIMARY / High | Debt structure, contracted energy, portfolio |
| cvm_ipe | IPE (material events) | https://dados.cvm.gov.br/dataset/cia_aberta-doc-ipe | Relevant events / eventual docs | PRIMARY / High | Material-fact surveillance |
| cvm_ofertas | Ofertas Públicas | https://dados.cvm.gov.br/group/ofertas-publicas | Debenture & securities offers | PRIMARY / High | Infra debt issuance tracking |
| b3_listadas | B3 Empresas Listadas | https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm | Listed-company disclosures | PRIMARY(exchange) / Low | Secondary to CVM for bulk |
| b3_fatos | B3 Fatos Relevantes por período | https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/acoes/consultas/informacoes-por-periodo/fatos-relevantes/ | Time-bounded relevant-fact search | PRIMARY(exchange) / Low | Alert source for corporate actions |
| anbima_data | ANBIMA Data | https://data.anbima.com.br/ | Debenture search, indicative prices, analytics | SECONDARY (industry std) / Low | Best debenture price layer; full API paid (Feed) |
| debentures_snd | Debentures.com.br (SND) | https://www.debentures.com.br/ | Issuance & document repository | SECONDARY / Low | Documentary backstop for older terms |
| fitch | Fitch Ratings | https://www.fitchratings.com/ | Corporate/project ratings, utilities outlooks | SECONDARY / Medium | Linked BR price/GSF/curtailment in 2026 commentary |
| sp | S&P Global Ratings | https://www.spglobal.com/ratings/en | Ratings & issuer reports | SECONDARY / Medium | Registration often required |
| moodys | Moody's | https://www.moodys.com/ | Ratings & issuer reports | SECONDARY / Medium | Mostly gated |
| abeeolica | ABEEólica Dados | https://abeeolica.org.br/energia-eolica/dados-abeeolica/ | Wind bulletins, annual reports, pipeline | SECONDARY / High | Wind-sector stress benchmark |
| absolar | ABSOLAR Infográfico / Solar em Dados | https://www.absolar.org.br/mercado/infografico/ | Solar infographics, georeferenced map | SECONDARY / High | Solar fleet growth & congestion geography |
| abraceel | Abraceel | https://abraceel.com.br/ | Free-market migration analyses | SECONDARY / Low | Interpreting CCEE migration |
| abradee | Abradee benchmarking | https://abradee.org.br/programa-de-benchmarking/ | Distributor benchmarking | SECONDARY / Low | Distributor peer analysis |
| ana_open_data | ANA Dados Abertos / Hidroweb | https://dadosabertos.ana.gov.br/ · https://www.snirh.gov.br/hidroweb/ | Hydrometeorological station data | PRIMARY / Medium | Best non-ONS hydrology |
| ana_hidrowebservice | ANA HidroWebService API | https://www.ana.gov.br/hidrowebservice/manual | API for hydromet data | PRIMARY / Medium | Registration by email required |
| inmet | INMET historical/station | https://portal.inmet.gov.br/dadoshistoricos · https://bdmep.inmet.gov.br/ | Historical & automatic-station weather | PRIMARY / Medium | Download-first, not API-first |
| inmet_alertas | INMET alerts/station map | https://alertas2.inmet.gov.br/ | Weather alerts, station map | PRIMARY / Medium | Event tagging |
| cptec_inpe | CPTEC/INPE | https://www.cptec.inpe.br/ · https://enos.cptec.inpe.br/ | Forecasts, ENSO outlooks | PRIMARY / Medium | Regime-level overlays |

---

## News, specialized media & legal tracking

| id (proposed) | Source | URL | Provides | Tier / Relevance | Notes |
|---|---|---|---|---|---|
| canalenergia | CanalEnergia | https://www.canalenergia.com.br/ | Broad trade coverage | SECONDARY / High | Strong on curtailment & network expansion |
| megawhat | MegaWhat | https://megawhat.energy/ | Regulation/market intelligence | SECONDARY / High | Often ahead on regulatory detail |
| eixos | eixos | https://eixos.com.br/home-2/ | Energy/policy coverage | SECONDARY / Medium | Policy & transition |
| epbr | epbr | https://epbr.com.br/ | Energy policy & business | SECONDARY / Medium | Ministerial/legislative corroboration |
| dou | Diário Oficial da União (search) | https://pesquisa.in.gov.br/ | Official gazette (laws, despachos) | PRIMARY / High | Verify effective publication |
| stj_coff | STJ news on constrained-off | https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2025/22012025-STJ-suspende-decisoes-que-obrigavam-ressarcimento-integral-de-cortes-de-geracao-de-energia-eolica-e-solar.aspx | Jan-2025 suspension of full-compensation decisions | PRIMARY / **High** | Must-watch legal milestone |
| aneel_news_coff | ANEEL curtailment rulemaking news | (2026 PV) https://www.gov.br/aneel/pt-br/assuntos/noticias/2026/consumidores-terao-novo-criterio-de-ressarcimento-para-o-constrained-off-de-usinas-fotovoltaicas · (2024 wind) https://www.gov.br/aneel/pt-br/assuntos/noticias/2025/aprovadas-melhorias-no-criterio-de-ressarcimento-de-constrained-off-para-eolicas · (2023 solar REN 1.073) https://www.gov.br/aneel/pt-br/assuntos/noticias/2023/aneel-aprova-regras-relacionadas-ao-constrained-off-de-usinas-fotovoltaicas | Official compensation-decision summaries | PRIMARY / **High** | Fastest official summary of changes |

---

## Top must-integrate sources (first wave — 15)

1. ONS constrained-off eólica por usina — https://dados.ons.org.br/dataset/restricao_coff_eolica_usi
2. ONS constrained-off eólica detalhada — https://dados.ons.org.br/dataset/restricao_coff_eolica_geracao
3. ONS constrained-off fotovoltaica por usina — https://dados.ons.org.br/dataset/restricao_coff_fotovoltaica_usi
4. ONS constrained-off fotovoltaica detalhada — https://dados.ons.org.br/dataset/restricao_coff_fotovoltaica_geracao
5. ONS geração por usina horária — https://dados.ons.org.br/dataset/geracao-usina-2
6. ONS curva de carga horária — https://dados.ons.org.br/dataset/curva-carga-horaria
7. ONS intercâmbios entre subsistemas — https://dados.ons.org.br/dataset/intercambios-entre-subsistemas
8. ONS ENA diário por subsistema — https://dados.ons.org.br/dataset/ena-diario-subsistema
9. ONS EAR diário por subsistema — https://dados.ons.org.br/dataset/ear-diario-subsistema
10. ANEEL SIGA (plant master) — https://dadosabertos.aneel.gov.br/dataset/siga-sistema-de-informacoes-de-geracao-da-aneel
11. ANEEL GD registry — https://dadosabertos.aneel.gov.br/dataset/relacao-de-empreendimentos-de-geracao-distribuida
12. CCEE PLD horário — https://dadosabertos.ccee.org.br/dataset/pld_horario
13. CCEE ACL/ACR consumption split — https://dadosabertos.ccee.org.br/dataset/consumo_mensal_ambiente_comercializacao
14. CCEE varejista / migration — https://dadosabertos.ccee.org.br/dataset/varejista_consumidor
15. CVM ITR/DFP/FRE/IPE — https://dados.cvm.gov.br/dataset/cia_aberta-doc-itr (+ dfp/fre/ipe)

Systems-of-record: **ONS** = physical/operational; **ANEEL** = regulatory + asset registry (SIGA); **CCEE** = market + settlement; **CVM** = listed-credit/issuer.

---

## APIs & programmatic access

| Source | Method | Base endpoint / pattern | Auth | Notes |
|---|---|---|---|---|
| ONS Dados Abertos | CKAN API + bulk | `https://dados.ons.org.br/api/3/action/` (inferred CKAN) | None indicated | CKAN conventions; not live-tested in research pass |
| ANEEL Dados Abertos | CKAN API + bulk | `https://dadosabertos.aneel.gov.br/api/3/action/` (inferred) | None indicated | Portal shows "API do CKAN" |
| CCEE Dados Abertos | Portal API + bulk | `https://dadosabertos.ccee.org.br/…` (CKAN-style likely) | None shown | Dataset pages reference API docs; exact root unverified |
| CVM Dados Abertos | CKAN API + bulk ZIP/CSV | `https://dados.cvm.gov.br/api/3/action/` (inferred) | None indicated | Stable annual file naming — pipeline-friendly |
| ANA HidroWebService | Dedicated API | per manual | **Registration by email** | One of few non-CKAN official APIs |
| ANA open data/metadata | Bulk + geoservices | `https://dadosabertos.ana.gov.br/` · `https://metadados.snirh.gov.br/` | Open (many) | WMS links in metadata |
| INMET | Bulk annual downloads | `https://portal.inmet.gov.br/dadoshistoricos` | Open (BDMEP may need login) | Download-first, not API-first |
| EPE | Bulk files/annexes | publication-specific PDF/XLSX | Open | Publication-driven ingestion |
| B3 | Page monitoring/scraping | page-level HTML | Open | CVM is better source-of-record |
| ANBIMA Feed | Commercial API | product-specific | Paid | Best debenture pricing API |

---

## Gaps & caveats

1. **Physical truth precedes economic truth.** ONS publishes plant-level wind/solar constrained-off with methodology, but the **cash-compensation side is fragmented** across ANEEL rule changes, CCEE reprocessing notices, transitional-vs-definitive methods, and litigation. → **Three-layer architecture required: ONS physical → ANEEL rule/docket → CCEE settlement.**
2. **Not perfectly machine-ready.** CKAN portals (ONS/ANEEL/CCEE/CVM) are good for ingestion, but field dictionaries, naming consistency, and coverage visibility vary. EPE/MME and some ANEEL procedural materials are **PDF-first**. INMET/ANA need a mix of APIs/portals/manual downloads.
3. **Units & definitions are a recurring error source.** Teams mix **MW, MWmed, MWh, GWh, EAR, ENA, contracted-energy**. For curtailment specifically, distinguish **physical restricted generation** vs **compensable energy-not-supplied** vs **settlement adjustments** (months later). Treat ONS = physical truth, CCEE = settlement, ANEEL = legal rule.
4. **Financial side:** cleanest pipelineable issuer data = **CVM**; **ANBIMA** best for debenture prices (commercial feed for full power); B3 for corporate-event monitoring; ratings agencies valuable but partly gated.
5. **Link/portal stability:** pages live as of 2026-06-17, but gov.br/CKAN paths rotate. **Store both the human landing page and the resource-file path**, and build a fallback that re-reads portal metadata when filenames/resource IDs change.
