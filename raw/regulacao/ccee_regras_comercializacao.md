# CCEE — Regras de Comercialização e Mecânica de Mercado

## Estrutura do Mercado de Energia

O mercado de energia elétrica brasileiro é dividido em dois ambientes:
- **ACR** (Ambiente de Contratação Regulada): distribuidoras compram energia em leilões centralizados; custo repassado à tarifa
- **ACL** (Ambiente de Contratação Livre): consumidores elegíveis compram diretamente de geradores via contratos bilaterais

A CCEE liquida a diferença entre o contratado e o consumido/gerado de cada agente no mercado de curto prazo (MCP), ao preço **PLD**.

---

## PLD — Preço de Liquidação das Diferenças

### Como é calculado
1. ONS roda os modelos **NEWAVE** (médio prazo, 5 anos) e **DECOMP** (curto prazo, 12 meses) semanalmente
2. Os modelos calculam o **CMO** (Custo Marginal de Operação) por subsistema
3. O PLD = min(CMO, Preço Teto) e max(CMO, Preço Piso)

### Limites 2026
| Subsistema | Preço Piso (R$/MWh) | Preço Teto (R$/MWh) |
|-----------|---------------------|---------------------|
| SE/CO | 69,04 | 904,76 |
| S | 69,04 | 904,76 |
| NE | 69,04 | 904,76 |
| N | 69,04 | 904,76 |

### Histórico PLD (média SE/CO)
| Ano | PLD Médio (R$/MWh) | Evento principal |
|-----|-------------------|-----------------|
| 2019 | R$ 145 | Normal |
| 2020 | R$ 134 | Covid (redução demanda) |
| 2021 | R$ 182 | Crise hídrica severa |
| 2022 | R$ 157 | Recuperação parcial |
| 2023 | R$ 98 | La Niña favorável |
| 2024 | R$ 89 | Mínimo recente — solar/eólica expandindo |
| 2025 | R$ 112 | El Niño moderado |
| 2026 YTD | R$ 134 | Seca Sul + demanda aquecida |

### Volatilidade e risco
- Desvio padrão histórico (2019-2025): ~R$ 28/MWh por mês
- Máximo histórico intra-semana: R$ 528/MWh (ago/2021)
- Correlação PLD × reservatórios: -0,78 (forte negativa)

---

## GSF — Generation Scaling Factor

### O que é
O GSF mede a razão entre a geração hidrelétrica efetiva e a geração física garantida (GF) dos contratos. Quando o GSF < 1, os geradores entregam menos do que contrataram e precisam comprar a diferença no MCP ao PLD.

```
GSF = Geração hidrelétrica efetiva / Garantia Física total
Exposição financeira = (1 - GSF) × GF contratada × PLD
```

### Histórico GSF
| Ano | GSF médio | PLD médio | Exposição típica (R$M, gerador médio) |
|-----|-----------|-----------|--------------------------------------|
| 2019 | 0,91 | R$ 145 | R$ 35M |
| 2020 | 0,88 | R$ 134 | R$ 50M |
| 2021 | 0,62 | R$ 182 | **R$ 320M** |
| 2022 | 0,79 | R$ 157 | R$ 120M |
| 2023 | 0,87 | R$ 98 | R$ 50M |
| 2024 | 0,91 | R$ 89 | R$ 25M |
| 2025 | 0,85 | R$ 112 | R$ 80M |

### MRR — Mecanismo de Repartição de Riscos (pós-2017)
Antes de 2017, o GSF era 100% risco do gerador. Após a MP 688/2015 e regulamentação da ANEEL:
- Distribuidoras no ACR assumem parte do risco hidrológico
- Geradores com contratos no ACR são parcialmente protegidos do GSF
- Porcentagem de proteção: varia por contrato (tipicamente 50–70% da exposição)

**Implicação para crédito:** Geradores hidrelétricos com contratos 100% no ACR têm menor risco GSF pós-2017. Geradores com maior parcela no ACL mantêm exposição total → diferencial importante na análise de crédito de projetos de geração.

---

## Contabilização CCEE — Balanço de Energia

Mensalmente, a CCEE apura o balanço de cada agente:
```
Posição de curto prazo = Geração/Consumo real - Volume contratado
  Superávit: vende no MCP ao PLD → receita adicional
  Déficit:   compra no MCP ao PLD → custo adicional
```

### Ciclo de liquidação
- Semana 1: CCEE calcula PLD para a semana seguinte
- Semana 4: fechamento da contabilização mensal
- Dia 15 do mês seguinte: liquidação financeira (pagamento entre agentes)
- Garantias financeiras: agentes precisam depositar garantia equivalente a 3 meses de posição máxima

### Default e cascata
Se um agente não paga a CCEE:
1. Garantias são executadas
2. Rateio entre os demais agentes superavitários (mutualization)
3. Restrição de acesso ao mercado (suspensão de certificados)

**Risco para crédito:** Distribuidoras inadimplentes com a CCEE têm encargos setoriais bloqueados pela ANEEL → risco de intervenção na concessão.

---

## Contratos no ACL — Estrutura

### Tipos de contrato bilateral
| Tipo | Característica | Risco típico |
|------|---------------|-------------|
| Contrato por quantidade | Volume fixo, preço fixo | Baixo para a distribuidora; gerador assume GSF |
| Contrato por disponibilidade | Gerador disponível; comprador paga se usar | Médio — pay-or-take |
| Contrato take-or-pay | Comprador paga mesmo se não usar | Alto para o comprador — penalidade por não despacho |
| Contrato índice | Preço indexado ao PLD +/- spread | Alto — exposição à volatilidade do spot |

### Indexadores típicos dos contratos ACL
- **IPCA**: mais comum em contratos de longo prazo (>3 anos)
- **IGP-M**: contratos antigos (antes de 2018, hoje em queda de uso)
- **PLD forward**: contratos especulativos de curto prazo
- **Spread fixo + PLD médio**: contratos de comercialização

### Sazonalização e Modulação
- Sazonalização: cliente pode variar volume mês a mês (dentro de limites contratados)
- Modulação: variação hora a hora no mesmo dia
- Flexibilidade de sazonalização: ±15% do volume mensal (típico em contratos standard)

---

## ACL — Migração e Impacto para Distribuidoras

### Critérios de elegibilidade
| Período | Demanda mínima | Fonte |
|---------|---------------|-------|
| Até 2022 | 3.000 kW | Qualquer |
| 2023–2024 | 1.000 kW | Qualquer |
| 2025–2026 | 500 kW | Qualquer |
| 2028+ | Sem limite (previsão) | Qualquer |

### Processo de migração
1. Consumidor notifica a distribuidora com 6 meses de antecedência (ANEEL RN 1.000)
2. Distribuidora libera o consumidor (não pode recusar)
3. Consumidor passa a pagar TUSD (uso da rede) mas compra energia no ACL
4. Distribuidora perde a margem de comercialização mas mantém receita de distribuição

### Receita retida pela distribuidora (TUSD)
```
Receita retida = TUSD × Demanda do consumidor migrado
Receita perdida = Margem de comercialização (energia)
```
Estimativa: para cada 1.000 MW que migra para o ACL:
- Receita bruta perdida: ~R$ 350M/ano
- Receita retida via TUSD: ~R$ 210M/ano
- **Perda líquida: ~R$ 140M/ano**

---

## Encargos Setoriais — Gestão pela CCEE/ANEEL

### CDE — Conta de Desenvolvimento Energético
- Fonte de subsídios para: Proinfa, baixa renda, irrigação rural, geração remota
- Custo 2025: R$ 28,4 bi (repartido entre todos consumidores via tarifa)
- Distribuidoras repassam integralmente → não afeta EBITDA, apenas caixa

### ESS — Encargo de Serviços do Sistema
- Cobre custo de despacho fora da ordem de mérito (termelétricas para estabilidade)
- Crescente com expansão de renováveis intermitentes: +23% em 2025 vs 2024
- Risco: ESS alto = pressão tariffária = inadimplência de consumidores de baixa renda

### EER — Energia de Reserva
- Contratação obrigatória de capacidade termelétrica de reserva
- Custo 2025: R$ 4,2 bi/ano
- Distribuidoras repassam à tarifa (Parcela A)

---

## Fontes
- CCEE: Regras de Comercialização (publicadas em www.ccee.org.br)
- CCEE: Boletim de Preços Semanais
- ANEEL: Resolução Normativa 1.000/2021 (Módulo de Distribuição)
- ONS: Nota de Operação — NEWAVE/DECOMP Methodology
