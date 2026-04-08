# ANEEL — Revisões Tarifárias e Metodologia de Precificação

## Visão Geral do Sistema Tarifário

A ANEEL determina as tarifas das distribuidoras por dois mecanismos principais:
- **RTP (Revisão Tarifária Periódica)**: recalcula toda a estrutura de receita — ocorre a cada 4 anos
- **RTE (Reajuste Tarifário Anual)**: corrige custos não-gerenciáveis pelo IPCA entre revisões

Distribuidoras não negociam tarifas com o mercado — a ANEEL define a receita permitida. Isso torna o risco regulatório o principal driver de crédito no setor.

---

## Estrutura da Receita Permitida (RP)

```
Receita Permitida = Parcela A + Parcela B
```

### Parcela A — Custos Não-Gerenciáveis (repassados integralmente à tarifa)
| Componente | Descrição | % médio da tarifa | Risco para crédito |
|------------|-----------|-------------------|--------------------|
| Energia comprada (CCEE/contratos) | Custo da energia no ACR | ~35% | Alto — PLD e GSF |
| TUST | Uso do sistema de transmissão | ~8% | Baixo — regulado |
| CDE | Conta de Desenvolvimento Energético | ~12% | Médio — pode crescer |
| ESS/EER | Serviços do sistema + energia de reserva | ~5% | Médio |
| PROINFA | Fontes alternativas subsidiadas | ~1% | Baixo |

### Parcela B — Custos Gerenciáveis (risco da distribuidora)
| Componente | Descrição | % médio da tarifa | Risco para crédito |
|------------|-----------|-------------------|--------------------|
| TUSD — Remuneração de capital (RAB × WACC) | Retorno sobre a base de ativos | ~18% | ALTO — determinado pela RTP |
| TUSD — Cota de depreciação | Amortização dos ativos | ~7% | Médio |
| TUSD — OPEX regulatório (PMSO) | Custos operacionais benchmarkados | ~9% | ALTO — sujeito a glosa DEA |
| Perdas técnicas | Perdas na rede (benchmark regulatório) | ~5% | Médio |

---

## RAB — Base de Ativos Regulatórios

### O que é
A RAB é o valor dos ativos da distribuidora reconhecidos pela ANEEL para fins de remuneração. É o principal determinante do EBITDA regulatório.

### Como é calculada
```
RAB = Investimentos reconhecidos × Fator de depreciação acumulada
    + Ativos em construção (parcialmente reconhecidos)
    - Ativos doados por consumidores (excluídos)
```

### RAB por empresa (dez/2025, estimativa baseada em dados públicos)
| Empresa | RAB (R$ bi) | Variação esperada RTP | Ciclo RTP |
|---------|-------------|----------------------|-----------|
| Equatorial Energia (consolidado) | 42,1 | +8% (novos ativos RS/ES) | 2027 |
| Energisa (consolidado) | 28,4 | +6% | 2027 |
| CPFL (consolidado) | 31,2 | +4% | 2024–2028 vigente |
| Neoenergia (consolidado) | 35,8 | +7% (transmissão nova) | 2024–2028 vigente |
| Cemig-D | 18,9 | -2% a +1% (eficiência questionada) | **2026** |
| Copel-DIS | 12,3 | +5% | **2026** |
| Eletrobras (transmissão, RAP) | 68,4 | Estável (RAP fixo por lote) | Contratos por lote |

### Impacto do WACC na RAB
Se ANEEL aprovar redução de WACC de 8,44% para 7,9% (proposta CP 040/2025):
```
ΔReceita = ΔWACC × RAB
Equatorial: -0,54% × R$42,1 bi = -R$ 227M/ano
Cemig-D:    -0,54% × R$18,9 bi = -R$ 102M/ano
CPFL:       -0,54% × R$31,2 bi = -R$ 169M/ano
Neoenergia: -0,54% × R$35,8 bi = -R$ 193M/ano
```
Impacto total no setor de distribuição: estimado -R$1,2 bi/ano de receita.

---

## WACC Regulatório — Metodologia ANEEL

### Fórmula (WACC pré-imposto, real)
```
WACC = Ke × E/(D+E) + Kd × (1-t) × D/(D+E)
```
Onde:
- **Ke** = custo do capital próprio (CAPM: Rf + β × ERP + prêmio de tamanho/liquidez)
- **Kd** = custo da dívida (Rf + spread de crédito do setor)
- **t** = alíquota de IR/CSLL (34%)
- **D/(D+E)** = estrutura de capital de referência ANEEL (atual: 45% dívida)

### Parâmetros vigentes (2024 — revisão quinquenal)
| Parâmetro | Valor atual | Proposta CP 040/2025 |
|-----------|-------------|----------------------|
| WACC pré-imposto real | 8,44% a.a. | 7,90% a.a. |
| Taxa livre de risco (Rf) | 3,50% | 3,20% |
| Prêmio de risco de mercado (ERP) | 5,50% | 5,50% |
| Beta desalavancado | 0,35 | 0,33 |
| Prêmio de risco-país (CRP) | 2,80% | 2,60% |

### Cronograma da revisão
- Consulta Pública 040/2025: publicada set/2025
- Audiência Pública: fev/2026
- Resolução final esperada: 2º semestre 2026
- Vigência: a partir do próximo ciclo RTP de cada empresa

---

## DEA — Análise Envoltória de Dados (Eficiência Operacional)

### O que é
A DEA compara o custo operacional (PMSO — Pessoal, Material, Serviços, Outros) de cada distribuidora com um grupo de pares. Empresas menos eficientes recebem glosa (corte) nos custos reconhecidos.

### Fórmula de remuneração dos custos
```
OPEX reconhecido = min(OPEX real, OPEX benchmark DEA)
Glosa = max(0, OPEX real - OPEX benchmark)
```

### Scores DEA por empresa (ciclo 2024-2028, estimativas)
| Empresa | Score DEA | Situação | Glosa OPEX estimada |
|---------|-----------|----------|---------------------|
| CPFL Paulista | 0,92 | Eficiente | R$ 0 |
| Neoenergia Elektro | 0,89 | Eficiente | R$ 0 |
| Equatorial Pará | 0,81 | Moderada | ~R$ 85M/ano |
| Cemig-D | 0,76 | Ineficiente | ~R$ 310M/ano |
| Energisa Mato Grosso | 0,74 | Ineficiente | ~R$ 140M/ano |
| Copel-DIS | 0,84 | Moderada | ~R$ 45M/ano |

**Implicação para crédito:** Uma empresa com score DEA 0,76 pode ter 24% dos seus custos operacionais não reconhecidos pela ANEEL → redução direta do EBITDA regulatório.

---

## CVA — Conta de Variação de Ativos

### O que é
A CVA registra o descasamento entre os custos de energia (Parcela A) que a distribuidora paga e o que já está na tarifa vigente. O saldo é recuperado/devolvido no próximo reajuste tarifário.

### Situação atual (dez/2025)
- **Saldo setorial a recuperar: R$ 8,3 bi** (distribuidoras têm crédito — energia subiu mais que o reajuste tarifário incorporou)
- Prazo médio de recuperação: 18–30 meses via RTE
- Empresas com maior CVA a recuperar: Cemig (R$1,1 bi), Energisa (R$0,9 bi), Equatorial (R$1,4 bi)

### Impacto para crédito
- CVA positiva = crédito com o governo regulatório → ativo corrente
- CVA negativa = devolução no próximo RTE → reduz receita futura
- **Risco:** distribuidoras alavancadas usam a CVA como funding de curto prazo; atrasos no reconhecimento comprimem caixa

---

## Qualidade de Serviço — DEC/FEC e Penalidades

### Indicadores
- **DEC** (Duração Equivalente de Interrupção): horas totais de interrupção por consumidor/ano
- **FEC** (Frequência Equivalente de Interrupção): número de interrupções por consumidor/ano

### Metas por empresa (ciclo 2024–2028, limites anuais)
| Empresa | DEC meta (h) | FEC meta (n°) | Penalidade por excesso |
|---------|-------------|---------------|------------------------|
| CPFL Paulista | 4,2 | 3,8 | Desconto automático na tarifa |
| Neoenergia Elektro | 5,1 | 4,2 | Desconto automático |
| Cemig-D | 6,8 | 5,5 | Desconto automático |
| Copel-DIS | 5,0 | 4,0 | Desconto automático |
| Equatorial Pará | 18,5 | 12,0 | Desconto automático + embargo de novos investimentos |
| Energisa Mato Grosso | 14,2 | 9,8 | Desconto automático |

### Fórmula de penalidade
```
Compensação ao consumidor = (DEC real - DEC meta) × Tarifa × Carga
Penalidade ANEEL = % da Receita Anual (varia de 0,1% a 1,5%)
```

### Impacto anual estimado (2025)
- Cemig: ~R$ 180M em compensações e penalidades
- Equatorial Pará: ~R$ 95M (ainda em turnaround)
- Energisa Mato Grosso: ~R$ 65M

---

## Calendário de RTPs — Próximos Ciclos

| Empresa | Próxima RTP | Ciclo | Pontos de atenção |
|---------|-------------|-------|-------------------|
| Cemig-D | **2026** | 4 anos | DEA ineficiente + possível corte WACC |
| Copel-DIS | **2026** | 4 anos | Eficiência boa, impacto ACL migration |
| Equatorial (consolidado) | **2027** | 4 anos | Integração CEEE-D, novos ativos RS |
| Energisa (consolidado) | **2027** | 4 anos | MT + TO revisão favorável esperada |
| CPFL (consolidado) | 2028 | 4 anos | Ciclo em vigor, estável |
| Neoenergia (consolidado) | 2028 | 4 anos | Ciclo em vigor, transmissão crescendo |

**Sinal para crédito:** RTPs em 2026 (Cemig, Copel) e 2027 (Equatorial, Energisa) são eventos críticos. Uma revisão negativa pode reduzir EBITDA em 5–15% por 4 anos → impacto direto em covenants de dívida.

---

## Fontes
- ANEEL: Nota Técnica nº 0041/2024-SRD/ANEEL (metodologia WACC)
- ANEEL: Consulta Pública 040/2025 (proposta revisão WACC)
- ANEEL: Resolução Homologatória de RTPs 2024/2025 (por empresa)
- ABRADEE: Relatório Setorial 2025
