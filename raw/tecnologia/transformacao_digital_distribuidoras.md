# Transformação Digital das Distribuidoras — AMI, Smart Grids e GD

## AMI — Advanced Metering Infrastructure

### Estado do Mercado (Abril 2026)
- **Meta ANEEL:** 100% dos consumidores com medidor inteligente até 2030
- **Instalados hoje:** 12 milhões (de 88 milhões total) = apenas **14% da meta**
- **Investimento necessário restante:** R$ 28–32 bi (2026–2030)
- **Prazo de retorno regulatório:** 5–8 anos (CAPEX reconhecido na RAB e amortizado)

### Cronograma por distribuidora (ANEEL Módulo 3 do PRODIST)
| Empresa | Medidores totais | Instalados (2026) | % | Meta 2028 | Meta 2030 |
|---------|-----------------|-------------------|---|----------|----------|
| CPFL | 9,2M | 2,8M | 30% | 60% | 100% |
| Neoenergia | 11,8M | 2,1M | 18% | 45% | 100% |
| Equatorial | 10,4M | 1,4M | 13% | 35% | 100% |
| Energisa | 7,2M | 0,9M | 13% | 30% | 100% |
| Cemig-D | 9,2M | 1,6M | 17% | 40% | 100% |
| Copel-DIS | 3,8M | 1,8M | 47% | 75% | 100% |

**Copel lidera** por ter iniciado o programa AMI em 2018 (mais cedo que as demais).

### Benefícios operacionais do AMI (por distribuidora)
| Benefício | Impacto quantificado |
|-----------|---------------------|
| Redução de perdas comerciais (PNT) | -3 a -6 p.p. nas perdas → R$ 80–200M/ano por distribuidora grande |
| Redução de DEC/FEC (detecção remota de falhas) | -15 a -25% nas interrupções → evita R$ 80–180M/ano em penalidades ANEEL |
| Corte de custos de leitura manual | -R$ 40–80M/ano (leituristas) |
| Detecção de furto de energia | -R$ 50–150M/ano (recuperação de receita) |
| **Total impacto positivo** | **R$ 250–610M/ano por distribuidora grande** |

---

## Automação de Redes

### SCADA — Supervisory Control and Data Acquisition
- **Função:** monitoramento e controle da rede em tempo real (subestações, alimentadores)
- **Cobertura atual:** ~65% das subestações monitoradas em tempo real (vs. meta 100%)
- **Benefício crédito:** distribuidoras com SCADA avançado têm DEC/FEC menores → menos penalidades ANEEL

### Reconectadores Automáticos e Seccionalizadores
- Dispositivos que isolam falhas e reconfigurem a rede automaticamente
- Impacto: reduz duração das interrupções em 40–60% na área com o dispositivo
- CAPEX: ~R$ 120K/equipamento; payback: 3–5 anos via redução de penalidades

### Automação Subestações
- Protocolo IEC 61850 (padrão internacional para comunicação em subestações)
- Reduz tempo de resposta a falhas de 30 minutos para 5 minutos
- **Copel:** 100% das subestações automatizadas — benchmark do setor

---

## Impacto da Geração Distribuída nas Redes

### O Problema da Saturação de Alimentadores
Com 28,1 GW de solar GD instalados, alguns alimentadores (redes de baixa tensão) estão atingindo capacidade máxima de injeção de energia.

| Situação | % de alimentadores (estimativa 2026) |
|---------|--------------------------------------|
| Sem saturação (<70% da capacidade) | 58% |
| Atenção (70–90% da capacidade) | 24% |
| Saturados (>90% — novas conexões bloqueadas) | 12% |
| Críticos (>100% — retorno de fluxo na rede) | 6% |

**Consequência regulatória:** ANEEL permite bloqueio de novas conexões GD em alimentadores saturados → reduz crescimento GD e melhora a situação da distribuidora (menos erosão de receita).

### Tensão na Rede — Problema Técnico
- GD solar injeta energia no meio do dia → sobe a tensão da rede
- ANEEL limita tensão: máximo 1,05 p.u. (5% acima do nominal)
- Quando tensão sobe acima do limite: distribuidora pode ser penalizada
- Solução: compensadores de reativos (custo R$ 80–150K por alimentador) ou BESS local

### Resposta à Demanda (Demand Response)
- Distribuidoras com AMI podem sinalizar preços horários aos consumidores
- Consumidor reduz carga nos picos → distribuidora evita reforços de rede caros
- Programa piloto CPFL (2025): 40.000 consumidores residenciais com tarifa branca
- Resultado: redução de 12% no pico de demanda nos horários críticos

---

## Retorno Financeiro da Digitalização

### ROI do investimento em AMI para uma distribuidora de 4M de consumidores

| Item | CAPEX (R$M) | Receita/Economia anual (R$M) | Payback (anos) |
|------|------------|------------------------------|---------------|
| Medidores inteligentes (hardware) | 1.200 | — | — |
| Infraestrutura de comunicação (SIM/LPWAN) | 480 | — | — |
| Sistema de gestão de dados (MDM) | 180 | — | — |
| **Total CAPEX AMI** | **1.860** | — | — |
| Redução perdas comerciais (PNT -4 p.p.) | — | 160 | — |
| Redução penalidades DEC/FEC (-20%) | — | 120 | — |
| Economia de leituristas e cobrança manual | — | 65 | — |
| Recuperação de furto de energia | — | 95 | — |
| **Total benefícios anuais** | — | **440** | **~4 anos** |

**Conclusão para crédito:** investimento em digitalização tem retorno claro em 4–6 anos e é reconhecido pela ANEEL na RAB → aumenta o valor regulatório da concessão, justifica CAPEX e melhora covenants a médio prazo.

---

## V2G — Vehicle-to-Grid (Perspectiva 2028+)

### Contexto
Frota de EVs projetada para 2030: ~3 milhões de veículos no Brasil. Se cada EV tiver bateria de 60 kWh e puder injetar 7 kW na rede por 4 horas:
- Capacidade de resposta à demanda do V2G: ~21 GW / 84 GWh
- É equivalente a construir 42 usinas de 500 MW de gás para flexibilização

### Regulamentação
- ANEEL publicará consulta pública sobre V2G em 2027 (confirmado em planejamento regulatório)
- Framework esperado: proprietário recebe crédito de energia + serviços de ancillary via CCEE
- Distribuidoras precisam modernizar redes (smart inverters bidirecionais) para suportar V2G

### Impacto para crédito de distribuidoras
- Positivo: nova fonte de receita (gestão de V2G como serviço)
- Negativo: requer CAPEX adicional de rede para comunicação bidirecional e proteção
- Neutro no curto prazo (2026-2028): escala ainda insignificante

---

## Fontes
- ANEEL: Procedimentos de Distribuição — Módulo 3 (AMI e Medição)
- CPFL: Relatório de Sustentabilidade 2025 (digitalização e resultados)
- Copel: Plano de Negócios 2025-2029 (smart grid roadmap)
- IEA: Smart Grids in Brazil — Status Report 2025
- ABRADEE: Relatório de Indicadores de Qualidade 2025
