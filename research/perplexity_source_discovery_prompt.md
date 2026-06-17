# Perplexity Deep Research — Brazilian Power Sector Source Discovery

> Paste everything inside the code fence below into Perplexity Deep Research.

```
ROLE
You are a senior research analyst specializing in the Brazilian electricity (power) sector and its data infrastructure. You are building a comprehensive SOURCE INVENTORY / DATA CATALOG that a credit-investment team will use to feed an automated data pipeline. Accuracy, completeness, and verifiable links matter more than prose — this is a reference catalog, not an essay.

CONTEXT
The end user works in private credit focused on the Brazilian power/energy sector. They are building a knowledge-and-monitoring system covering the WHOLE sector. The very first analytical module is a CURTAILMENT MONITOR for wind (eólica) and solar (fotovoltaica) generation — i.e., "constrained-off" / "corte de geração" ordered by the ONS — so sources that quantify curtailment volumes, reasons (reliability vs. energetic/merit), affected assets/regions, and the compensation ("ressarcimento") framework deserve extra attention. But the catalog itself must be SECTOR-WIDE.

OBJECTIVE
Produce an exhaustive, well-structured catalog of authoritative and useful sources of DATA and INFORMATION about the Brazilian electricity sector. Strongly prioritize PRIMARY (official) and MACHINE-READABLE sources (open-data portals, APIs, downloadable CSV/XLSX/JSON), because they will be ingested programmatically. Then cover secondary sources (associations, specialized media, research, ratings) used for context and cross-checking.

SCOPE — cover all of these dimensions
1. System operation & physical data: generation, load/demand, dispatch, interchange between subsystems, installed capacity, hydrology (ENA, reservoir/EAR levels), wind/solar generation, CURTAILMENT / constrained-off of wind & solar.
2. Market & commercial: spot price (PLD), settlement, contracts, ACL vs. ACR, consumer migration to the free market, energy auctions (leilões) results and pipeline, supply/demand balance.
3. Regulation: ANEEL resolutions (REN), despachos, tariff reviews (RTP/RTE), concessions, generation registry/capacity (SIGA), distributed generation (GD), inspection/fiscalização, the curtailment-compensation rule-making.
4. Planning & policy: EPE (PDE, PNE, Balanço Energético Nacional), MME programs and monitoring bulletins, CNPE decisions, decarbonization/NDC, carbon market (SBCE).
5. Financial & credit (issuer level): listed-company filings and material facts (CVM), debênture / fixed-income data and secondary-market prices (B3, ANBIMA), credit ratings (Fitch, Moody's, S&P and Brazilian scales), investor-relations pages of major utilities, financial-data providers.
6. Generation projects & technology: project pipelines, capacity additions, sector association datasets (wind, solar, distributors, traders), market intelligence reports.
7. Meteorology & water: rainfall/inflow forecasts and hydrology relevant to dispatch and curtailment.
8. News & specialized media: Brazilian energy-sector trade press for timely events and corroboration.
9. Legal/regulatory tracking: official gazette, regulatory dockets, and litigation relevant to the sector (especially constrained-off compensation disputes).

FOR EACH SOURCE, capture this structured metadata (use a table):
- Source name (and the Portuguese name if different)
- Publisher / owner (e.g., ONS, ANEEL, CCEE, EPE, MME, CVM, B3, ANBIMA, association, media outlet)
- Category (from the scope list above)
- Direct URL to the landing page AND, when applicable, the direct dataset/API/download URL
- What data or information it provides — be specific (e.g., "daily constrained-off energy by wind plant, with reason flag: reliability vs. energetic")
- Format(s): API / CSV / XLSX / JSON / PDF / HTML / dashboard
- Access method: open download • REST API (give base endpoint + docs link if available) • requires registration/login • paid/subscription
- Update frequency (real-time / daily / monthly / annual / irregular)
- Historical coverage (earliest available data, if discoverable)
- Granularity (hourly/daily/monthly; by plant/submarket/region/state; by issuer)
- Language (PT / EN)
- Authentication & cost (free / API key needed / paid)
- Reliability tier: PRIMARY (authoritative/official) or SECONDARY (context/corroboration)
- Relevance to CREDIT analysis (High / Medium / Low)
- Relevance to the CURTAILMENT module specifically (High / Medium / Low)
- Notes / known gotchas (data quirks, unit conventions e.g. MWmed vs MWh, rate limits, broken links)

OUTPUT FORMAT
1. Executive summary (5–10 lines): the landscape and the most important primary data hubs.
2. One section per category, each with a metadata TABLE as defined above. Be exhaustive — aim for the full breadth of relevant sources (target several dozen overall), not a short list.
3. "TOP MUST-INTEGRATE SOURCES" — a prioritized shortlist (~15) of the highest-value, machine-readable primary sources to wire into a pipeline first, each with its direct dataset/API URL.
4. "CURTAILMENT QUICK-START" — a focused subsection listing the EXACT datasets and documents needed to quantify wind/solar constrained-off in Brazil and to understand the compensation framework: ONS open-data datasets (with direct links), the relevant ANEEL resolutions/despachos and dockets, CCEE settlement references, and the best news/association trackers. Include direct URLs.
5. "APIs & PROGRAMMATIC ACCESS" — a consolidated list of every source offering an API or bulk download, with base endpoints, whether an API key is required, and a link to documentation.
6. "GAPS & CAVEATS" — note where data is hard to get, paywalled, inconsistent, or where units/definitions commonly cause errors.

REQUIREMENTS
- Focus exclusively on Brazil; ensure information is current as of 2026.
- Verify links exist; provide direct, specific URLs (not just homepages) wherever possible.
- Distinguish clearly between official/primary sources and secondary ones.
- Cite every source. Prefer official Portuguese-language portals for primary data.
- Where a portal (e.g., a CKAN open-data portal) hosts many datasets, list the specific dataset names/URLs relevant to the scope, not just the portal root.
- Do not invent URLs or datasets; if uncertain whether something exists, say so explicitly rather than guessing.
```
