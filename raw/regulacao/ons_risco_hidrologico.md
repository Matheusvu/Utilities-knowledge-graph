# ONS e Risco Hidrológico — Impacto no Crédito de Geradoras

## O Sistema Hidrelétrico Brasileiro

O Brasil opera o maior sistema hidrelétrico interligado do mundo:
- **Capacidade hidrelétrica instalada:** 109,4 GW (30,1% da matriz total de 364 GW)
- **Energia assegurada hidrelétrica:** ~55% de toda a energia garantida do SIN
- **Número de reservatórios relevantes:** 159 (operados pelo ONS)
- **Volume útil total:** ~400 km³ (maior do mundo exceto sistema Columbia/EUA-Canadá)

O risco hidrológico é o principal risco sistêmico para geradores e para o custo de energia das distribuidoras no Brasil.

---

## Reservatórios — Nível e Sazonalidade

### Subsistemas e capacidade de regularização
| Subsistema | Capacidade útil (km³) | Regularização | Estados principais |
|-----------|----------------------|--------------|-------------------|
| Sudeste/Centro-Oeste | 216 | Alta (>12 meses) | MG, SP, GO, MS |
| Sul | 30 | Baixa (2-4 meses) | PR, SC, RS |
| Nordeste | 62 | Média (6-8 meses) | BA, PI, PE, CE |
| Norte | 45 | Média (4-6 meses) | PA, TO, AM |

### Nível de reservatórios (histórico e atual)
| Data | SE/CO | S | NE | N | Situação |
|------|-------|---|----|---|---------|
| Jan 2021 | 17% | 38% | 28% | 44% | Crise severa |
| Jan 2022 | 32% | 55% | 51% | 62% | Recuperação |
| Jan 2023 | 58% | 72% | 65% | 71% | Normal |
| Jan 2024 | 65% | 80% | 72% | 75% | Bom |
| Jan 2025 | 59% | 61% | 68% | 70% | Moderado |
| Abr 2026 | 62% | 48% | 71% | 73% | Normal/Sul preocupante |

### Padrão sazonal
- **Cheia:** janeiro a abril (chuvas no Sudeste/Centro-Oeste)
- **Seca:** junho a novembro (crítico para geração)
- **Risco máximo:** setembro-outubro em anos El Niño ou La Niña adverso

---

## CMO — Custo Marginal de Operação

### Conceito
O CMO é o custo de produzir a próxima unidade de energia no sistema. Em um sistema predominantemente hidrelétrico:
- Reservatórios cheios → CMO baixo (água tem custo zero)
- Reservatórios vazios → CMO alto (precisa despachar termelétrica cara)

### Drivers do CMO
```
CMO = f(nível reservatório, afluência prevista, carga demandada,
        disponibilidade termelétrica, preço do gás, interconexão com AR/UY)
```

### CMO por subsistema 2025-2026 (médias mensais R$/MWh)
| Mês | SE/CO | S | NE | N |
|-----|-------|---|----|---|
| Jan 2026 | 98 | 112 | 105 | 87 |
| Fev 2026 | 89 | 105 | 98 | 82 |
| Mar 2026 | 95 | 118 | 102 | 90 |
| Abr 2026 | 134 | 165 | 128 | 115 |

---

## GSF — Generation Scaling Factor (Detalhamento)

### Cálculo formal
```
GSF = Σ (Geração efetiva de todas as usinas hidro) / Σ (Garantia Física de todas as usinas hidro)
```

### Garantia Física vs. Energia Assegurada
- **Garantia Física (GF):** montante máximo que um gerador pode contratar (MW médios)
- **Energia Assegurada:** parcela da GF que o sistema garante entregar com 95% de probabilidade

Quando o GSF < 1, a soma das GF supera a energia efetivamente disponível → geradores ficam "descobertos".

### GSF por usina (estimativa 2024)
| Usina | Empresa | GF (MW médios) | GSF 2024 | Exposição (R$M, PLD R$89) |
|-------|---------|----------------|----------|--------------------------|
| Emborcação | Cemig | 324 | 0,88 | R$ 35M |
| Furnas | Eletrobras | 850 | 0,91 | R$ 68M |
| Paulo Afonso IV | Chesf/Eletrobras | 780 | 0,84 | R$ 112M |
| Serra da Mesa | Engie | 680 | 0,87 | R$ 79M |
| Itumbiara | Engie | 390 | 0,90 | R$ 35M |
| Três Marias | Cemig | 178 | 0,82 | R$ 28M |

**Em 2021 (GSF 0,62, PLD R$182):**
- Exposição da Eletrobras apenas em contratos ACL: ~R$ 3,1 bi
- Setor de geração hidrelétrica: ~R$ 12 bi de exposição total

---

## MRR — Mecanismo de Repartição de Riscos Hidrológicos

### Origem
Criado pela MP 688/2015 e regulamentado pela ANEEL, após a crise de 2012-2015 que gerou bilhões em perdas para geradores e ameaçou o equilíbrio financeiro do setor.

### Funcionamento
Para contratos de geração no ACR (leilões A-3, A-5, A-6 e reserva de capacidade):
1. Se o GSF cair, as distribuidoras (compradores) assumem parte do descasamento
2. A distribuidora pagará pela energia contratada MESMO que o gerador não entregue
3. O custo adicional entra na Parcela A da distribuidora → repassado à tarifa
4. O gerador fica parcialmente protegido

**Proteção típica:** 50–80% da exposição ao GSF é transferida para distribuidoras em contratos pós-2015

### Impacto para crédito de geradores
- **Contratos pré-2015 (sem MRR):** gerador suporta 100% do risco GSF → alta volatilidade de EBITDA
- **Contratos pós-2015 (com MRR):** gerador suporta ~20–50% do risco GSF → EBITDA mais estável
- **Monitoramento:** analisar mix de contratos de cada gerador é essencial para avaliar o risco hidrológico líquido

---

## CMSE — Comitê de Monitoramento do Setor Elétrico

### Função
O CMSE (criado pela Lei 10.848/2004) monitora o risco de déficit de energia e pode recomendar:
- Contratação emergencial de termelétrica
- Sinalização de risco de racionamento ao MME
- Curva de aversão ao risco (quando acionar termelétrica cara)

### Curva de Aversão ao Risco (CAR)
A CAR define o nível mínimo de reservatório para cada mês. Abaixo da curva:
- ONS despacha termelétricas compulsoriamente (mesmo que caro)
- CMO sobe abruptamente → PLD aumenta
- Geradores com GF acima da geração física ficam expostos

### Historico de acionamentos
| Período | Situação | Ação CMSE | Custo estimado |
|---------|---------|-----------|----------------|
| 2012-2015 | Reservatórios baixos | Despacho contínuo termelétrica | R$ 35 bi |
| Jul-Nov 2021 | Crise severa | Escassez (bandeira vermelha 2) | R$ 12 bi |
| 2022-2024 | Normal | Despacho mínimo | - |
| Abr 2026 | Sul preocupante | Monitoramento elevado | Em avaliação |

---

## Interconexões Internacionais

### Itaipu (BR-PY)
- Capacidade: 14.000 MW (7.000 MW para cada país)
- Contrato: Tratado de 1973, renovado automaticamente
- Energia garantida para o Brasil: 40 GWh médios/ano (~6% da carga)
- Preço: fixo por tratado — previsível e barato (~R$ 58/MWh all-in)
- **Relevância:** Itaipu é âncora de energia barata — sua disponibilidade reduz o CMO do sistema SE/CO

### Interligação com Argentina e Uruguai
- Intercâmbio máximo: ~2.000 MW (importação emergencial)
- Ativado em situações de risco extremo
- Custo: PLD do mercado Argentino (CAMMESA) + spread de transmissão

---

## Cenários de Estresse para Crédito

### Cenário 1 — La Niña Severa (probabilidade 20% a.a.)
- Reservatórios SE/CO abaixo de 30% em setembro
- PLD atinge R$ 400–600/MWh
- Geradores sem MRR: exposição ~R$ 500M+ para cada 1 GW de GF
- Distribuidoras: CVA cresce R$ 5–8 bi, comprime caixa por 18-24 meses

### Cenário 2 — Normal/Favorável (probabilidade 50%)
- Reservatórios >55% no período seco
- PLD médio anual R$ 80–130/MWh
- Geradores confortáveis; distribuidoras com CVA neutra ou levemente positiva

### Cenário 3 — Crise como 2021 (probabilidade 5% a.a.)
- PLD próximo do teto (~R$ 900/MWh) por 4+ meses
- Geradores sem proteção MRR: R$ 1–3 bi de perda por empresa grande
- Setor de distribuição: CVA acumula R$ 15–25 bi → risco de iliquidez sistêmica

---

## Fontes
- ONS: Boletim de Acompanhamento do Sistema (semanal)
- ONS: Procedimentos de Rede — Módulo 10 (Planejamento da Expansão)
- CCEE: Nota Técnica — GSF e MRR (2025)
- CMSE: Relatórios Mensais de Avaliação do Risco de Déficit
