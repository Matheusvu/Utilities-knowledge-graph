# PLD — Histórico, Análise e Implicações para Crédito

## Série Histórica por Subsistema (R$/MWh, médias anuais)

| Ano | SE/CO | Sul | Nordeste | Norte | Evento relevante |
|-----|-------|-----|----------|-------|-----------------|
| 2015 | R$ 388 | R$ 388 | R$ 388 | R$ 388 | Crise hídrica; piso = teto setorial |
| 2016 | R$ 198 | R$ 195 | R$ 195 | R$ 195 | Recuperação parcial reservatórios |
| 2017 | R$ 289 | R$ 285 | R$ 290 | R$ 285 | Segundo pior ano hídrico da série |
| 2018 | R$ 161 | R$ 159 | R$ 162 | R$ 158 | Eleições + demanda estável |
| 2019 | R$ 145 | R$ 143 | R$ 148 | R$ 142 | Normal |
| 2020 | R$ 134 | R$ 130 | R$ 136 | R$ 131 | Pandemia (demanda -4%) |
| 2021 | R$ 182 | R$ 177 | R$ 185 | R$ 175 | **Crise hídrica severa** (El Niño) |
| 2022 | R$ 157 | R$ 152 | R$ 160 | R$ 154 | Pós-crise; gás/guerra Ucrânia |
| 2023 | R$ 98 | R$ 94 | R$ 101 | R$ 96 | La Niña favorável; solar expandiu |
| 2024 | R$ 89 | R$ 85 | R$ 93 | R$ 88 | Mínimo recente; solar >40 GW |
| 2025 | R$ 112 | R$ 108 | R$ 116 | R$ 109 | El Niño moderado |
| 2026 YTD (Q1) | R$ 134 | R$ 165 | R$ 128 | R$ 115 | Seca Sul; Sul acima de SE/CO |

---

## Análise de Volatilidade

### Estatísticas descritivas (2015-2026)
| Métrica | SE/CO | Sul |
|---------|-------|-----|
| Média | R$ 178 | R$ 175 |
| Mediana | R$ 155 | R$ 152 |
| Desvio padrão | R$ 84 | R$ 90 |
| Máximo | R$ 388 | R$ 388 |
| Mínimo (piso de mercado) | R$ 69 | R$ 69 |
| Coef. de variação | 47% | 51% |

**O Sul tem maior variabilidade** → impacta fortemente Copel (geração predominantemente no Sul).

### Correlações com variáveis macro
| Variável | Correlação com PLD SE/CO |
|----------|--------------------------|
| Nível reservatório SE/CO (t-1) | -0,78 |
| Afluência natural energia | -0,72 |
| IPCA (inflação) | +0,31 |
| Preço gás natural (Henry Hub) | +0,48 |
| Geração solar + eólica (GWh) | -0,55 |

A correlação negativa crescente com geração renovável (solar/eólica) indica que a expansão das renováveis está **deprimindo estruturalmente o PLD** → risco para geradores hidrelétricos com contratos curtos.

---

## Impacto Financeiro do PLD por Tipo de Player

### Gerador hidrelétrico puro (1 GW de GF, contratos ACL 50%)
| PLD Cenário | Impacto vs. PLD R$ 100 base |
|-------------|------------------------------|
| PLD R$ 80 (baixo) | -R$ 52M/ano (vende excedente mais barato) |
| PLD R$ 100 (base) | Neutro |
| PLD R$ 150 (alto) | +R$ 130M/ano |
| PLD R$ 300 (estresse) | +R$ 520M/ano |

### Distribuidora (compra no ACR, PLD afeta via CVA)
- PLD alto → energia comprada no ACR ficou mais cara do que previsto → CVA cresce → comprime caixa
- PLD baixo → energia comprada ficou mais barata → CVA negativa → distribuidora devolve na tarifa
- **Impacto anual:** +/- R$ 100M para cada R$ 30/MWh de variação no PLD para uma distribuidora média

### Gerador termelétrico (despacho fora da ordem de mérito)
- Despacha quando PLD > custo variável (CVU) da termelétrica
- Termelétrica a gás ciclo combinado: CVU ~R$ 180–250/MWh
- Rentabilidade: apenas quando PLD > CVU → anos como 2021 são muito lucrativos para termoelétricas

### Consumidor livre (ACL)
- Compra a preço forward ACL (~PLD médio esperado + spread comercializador)
- Com PLD médio 2024 de R$ 89, muitos contratos ACL renovaram a R$ 95–110/MWh
- Se PLD sobe para R$ 200 em 2027: consumidor que migrou economizou R$ 90-110/MWh vs. tarifa cativa

---

## Drivers Estruturais 2026-2030

### Fator 1: Expansão Solar e Eólica (PLD-depressivo)
- Cada 10 GW de solar/eólica adicionado ao sistema reduz PLD médio em ~R$ 8–12/MWh (estimativa EPE)
- Pipeline de expansão 2026-2030: +40-50 GW renováveis → pressão estrutural de queda no PLD
- Projeção EPE: PLD médio 2030 ~R$ 75–90/MWh (em cenário de hidrologia normal)

### Fator 2: Crescimento da Demanda (PLD-positivo)
- Datacenters: +28% de crescimento de carga em 2025 → vai continuar
- Mineração de criptoativos: +15% a.a. de carga
- Indústria de fertilizantes (substitutição de importação): +8% a.a.
- Veículos elétricos: ainda pequeno, mas crescendo (420.000 EVs, demanda noturna)

### Fator 3: BESS e Arbitragem (suaviza picos)
- Cada GW de BESS instalado reduz a volatilidade intraday do PLD em ~15%
- Com 5 GW de BESS previstos até 2030 (meta CNPE), picos de PLD acima de R$ 400 serão mais raros

### Fator 4: Hidrologia (dominante no curto prazo)
- Padrão El Niño/La Niña: alternância a cada 2-3 anos
- La Niña: desfavorável para SE/CO (seca) → PLD alto
- El Niño: favorável para SE/CO, mas prejudica Sul → PLD Sul pode subir enquanto SE/CO cai

---

## Basis Risk — Diferencial entre Subsistemas

O basis risk é o diferencial de preço entre subsistemas. Em 2026 (Q1):
- Sul: R$ 165/MWh vs. SE/CO: R$ 134/MWh → diferencial de R$ 31/MWh
- Geradores no Sul (Copel, Tractebel/Engie) sofrem quando Sul > SE/CO (entregam no Sul mas contratam no SE/CO)
- Consumidores livres no Sul podem se beneficiar comprando energia de fora do subsistema

**Impacto Copel GeT em 2026 Q1:** com 780 MW médios no Sul e PLD Sul R$ 165, ganho adicional vs. base de R$ 134 = +R$ 39M no trimestre.

---

## Fontes
- CCEE: Boletim de Preços PLD (semanal — www.ccee.org.br)
- ONS: Nota de Operação — Resultado NEWAVE/DECOMP
- EPE: PDEE 2034 — Projeções de Carga e Expansão
- CMSE: Relatório de Avaliação de Risco de Déficit
