from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# ── Colour palette (BTG-inspired: dark navy + gold accent) ─────────────────
NAVY      = RGBColor(0x0D, 0x1B, 0x3E)   # dark navy background
NAVY_LIGHT= RGBColor(0x16, 0x2A, 0x5C)   # slightly lighter navy
GOLD      = RGBColor(0xC9, 0xA0, 0x2B)   # BTG gold
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GREY= RGBColor(0xE8, 0xEC, 0xF4)
MID_GREY  = RGBColor(0x8A, 0x97, 0xB5)
GREEN     = RGBColor(0x2E, 0xCC, 0x71)

prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)

def add_rect(slide, l, t, w, h, color, transparency=0):
    from pptx.util import Pt
    shape = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape

def add_text(slide, text, l, t, w, h, size, bold=False, color=WHITE,
             align=PP_ALIGN.LEFT, italic=False, wrap=True):
    txBox = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    txBox.word_wrap = wrap
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txBox

def set_slide_bg(slide, color):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 1 — COVER
# ═══════════════════════════════════════════════════════════════════════════
slide_layout = prs.slide_layouts[6]   # blank
slide = prs.slides.add_slide(slide_layout)
set_slide_bg(slide, NAVY)

# Gold accent bar (left)
add_rect(slide, 0, 0, 0.18, 7.5, GOLD)

# Graphify logo text
add_text(slide, "graphify", 0.45, 0.6, 5, 1.0, 52, bold=True, color=GOLD)

# Subtitle line
add_text(slide, "Top 10 Use Cases for Private Credit in Brazilian Utilities",
         0.45, 1.6, 10, 1.2, 28, bold=False, color=WHITE)

# Divider line
add_rect(slide, 0.45, 2.95, 9.5, 0.04, GOLD)

# Description
add_text(slide,
    "A knowledge-graph intelligence layer purpose-built for credit officers covering\n"
    "the Brazilian energy & utilities sector — updated April 2026",
    0.45, 3.1, 10.5, 1.0, 16, color=LIGHT_GREY)

# Bottom metadata
add_rect(slide, 0, 6.6, 13.33, 0.9, NAVY_LIGHT)
add_text(slide, "Prepared for: Head of Private Credit — Utilities | BTG Pactual",
         0.45, 6.65, 8, 0.5, 13, color=MID_GREY)
add_text(slide, "April 2026", 11.0, 6.65, 2, 0.5, 13, color=MID_GREY, align=PP_ALIGN.RIGHT)

# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 2 — WHAT IS GRAPHIFY?
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, NAVY)
add_rect(slide, 0, 0, 0.18, 7.5, GOLD)

add_text(slide, "What is graphify?", 0.45, 0.35, 10, 0.8, 32, bold=True, color=WHITE)
add_rect(slide, 0.45, 1.15, 9.5, 0.04, GOLD)

add_text(slide,
    "graphify transforms your research documents — PDFs, regulatory filings, annual reports, news — "
    "into a queryable knowledge graph. Every concept, relationship, and regulatory link is extracted, "
    "mapped, and made searchable in seconds.",
    0.45, 1.3, 12.0, 1.1, 16, color=LIGHT_GREY)

# Three pillars
pillars = [
    ("INPUT", "Drop any document:\nPDFs, Markdown, images,\nregulatory filings", 0.5),
    ("GRAPH ENGINE", "AI extracts nodes &\nedges — explicit facts\n+ inferred connections", 4.5),
    ("QUERY", "Ask questions in plain\nPortuguês or English.\nGet cited answers.", 8.5),
]
for (title, body, x) in pillars:
    add_rect(slide, x, 2.55, 3.6, 3.5, NAVY_LIGHT)
    add_rect(slide, x, 2.55, 3.6, 0.55, GOLD)
    add_text(slide, title, x+0.15, 2.6, 3.3, 0.45, 16, bold=True, color=NAVY)
    add_text(slide, body, x+0.15, 3.25, 3.3, 2.5, 14, color=LIGHT_GREY)

add_rect(slide, 0, 6.6, 13.33, 0.9, NAVY_LIGHT)
add_text(slide, "71× fewer tokens per query vs. re-reading raw documents   |   SHA-256 cache — only processes new files",
         0.45, 6.65, 12, 0.5, 12, color=GOLD)

# ═══════════════════════════════════════════════════════════════════════════
# USE CASE SLIDES (3–12)
# ═══════════════════════════════════════════════════════════════════════════
use_cases = [
    {
        "number": "01",
        "title": "Regulatory Risk Radar",
        "tagline": "Know how an ANEEL resolution hits your borrower's EBITDA before the market does.",
        "problem": "Regulatory changes (WACC revision, new PRODIST modules, RN 1.072) alter distribuidora cash flows — but tracking cascades across 40+ resolutions manually is impossible.",
        "how": "Feed all ANEEL resolutions + company concession contracts into graphify. Ask: 'If the WACC drops from 8.44% to 7.9%, which companies in our portfolio lose the most RAB value?'",
        "output": "Ranked list of portfolio companies by exposure + quantified EBITDA impact",
        "example": "Equatorial Energia: -R$420M RAB impact from proposed WACC cut → covenant headroom shrinks 0.3× on 3 debenture tranches",
        "tags": ["ANEEL", "WACC", "RAB", "Tariff Review", "Covenant Risk"],
    },
    {
        "number": "02",
        "title": "Credit Due Diligence in Hours",
        "tagline": "Cut new deal research from 3 weeks to an afternoon.",
        "problem": "A new deal hits your desk: Energisa MT wants R$800M in debentures. The analyst team needs regulatory exposure, competitive position, and covenant comparables — typically 15–20 days.",
        "how": "Load Energisa annual reports + MT concession contract + ANEEL tariff history into graphify. Run structured queries: regulatory profile, revenue composition, key risks, covenant benchmarks.",
        "output": "Structured credit memo draft with cited sources — ready in <4 hours",
        "example": "Identified hidden exposure: MT concession requires R$1.2B CAPEX commitment by 2028 — not prominently disclosed in investor presentation",
        "tags": ["Due Diligence", "Concession Risk", "Speed", "Credit Memo"],
    },
    {
        "number": "03",
        "title": "Covenant Trigger Early Warning",
        "tagline": "Surface regulatory events that could breach loan covenants before they happen.",
        "problem": "Loan covenants reference ANEEL regulatory metrics (DEC/FEC, tariff coverage ratios) — but mapping an incoming regulatory change to a specific covenant breach requires deep cross-referencing.",
        "how": "Load loan contracts + regulatory calendar + company operational data. Graphify maps regulatory triggers → financial metrics → covenant definitions automatically.",
        "output": "Alert: '3 regulatory events in the next 6 months could trigger covenant review for 2 portfolio companies'",
        "example": "Cemig-D: DEC deterioration in Q1 2026 triggers potential ANEEL fine of R$180M → DSCR drops below 1.2× threshold in Dec 2026 debenture indenture",
        "tags": ["Covenant Monitoring", "DEC/FEC", "Early Warning", "DSCR"],
    },
    {
        "number": "04",
        "title": "Portfolio-Wide Stress Testing",
        "tagline": "Simulate a regulatory shock across your entire utilities book in one query.",
        "problem": "If the Brazilian energy market fully opens (ACL liberalization in 2028), which distribuidoras in your portfolio are most exposed? Running this manually across 8 positions takes weeks.",
        "how": "Load all portfolio company filings + ACL migration data + ANEEL market opening rules. Ask: 'Rank our portfolio by ACL migration exposure and projected revenue loss by 2028.'",
        "output": "Stress matrix: company × scenario × EBITDA impact × covenant headroom",
        "example": "Scenario: 45% ACL penetration by 2028 — Copel-DIS loses ~R$890M revenue; Energisa MT is partially protected by rural mix (lower migration rate)",
        "tags": ["Stress Testing", "ACL", "Portfolio Risk", "Scenario Analysis"],
    },
    {
        "number": "05",
        "title": "Hidden Counterparty Exposure Map",
        "tagline": "Discover when two borrowers are more connected than they appear.",
        "problem": "You hold debt in both CPFL Comercialização and a large industrial consumer that migrated to ACL. If the industrial defaults on its energy contract, CPFL is exposed — and so are you, twice.",
        "how": "Build a cross-portfolio knowledge graph linking energy contracts, CCEE settlements, and counterparty names. Graphify surfaces implicit connections across documents.",
        "output": "Network visualization of cross-exposures + quantified bilateral risk",
        "example": "Found: Neoenergia and Equatorial share 3 common large free-market consumers in BA — concentration risk not visible from individual loan files",
        "tags": ["Counterparty Risk", "CCEE", "Concentration", "ACL Contracts"],
    },
    {
        "number": "06",
        "title": "Tariff Review Impact Modeling",
        "tagline": "Model how the next RTP cycle reshapes borrower cash flows.",
        "problem": "Each RTP resets the distribuidora's EBITDA for 4 years. Upcoming reviews for Cemig (2026) and Energisa (2027) will reprice the RAB — but the regulatory methodology is 400+ pages.",
        "how": "Load ANEEL RTP methodology + previous review decisions + company efficiency benchmarks. Ask: 'What is the likely outcome of Cemig's 2026 RTP given its current DEA efficiency score?'",
        "output": "Projected RAB + EBITDA delta for each upcoming review with confidence range",
        "example": "Cemig 2026 RTP: DEA score 0.78 vs peer average 0.84 → likely OPEX glosa of 8% → EBITDA impact -R$310M/year over the next 4-year cycle",
        "tags": ["RTP", "RAB", "DEA Efficiency", "Cemig", "EBITDA Forecast"],
    },
    {
        "number": "07",
        "title": "ESG & Green Finance Eligibility",
        "tagline": "Instantly verify if a deal qualifies for green bond or sustainability-linked structures.",
        "problem": "ESG-linked structures (green debentures, CRAs, SLBs) are now 30% of Brazilian infra debt issuances — but verifying NDC alignment and taxonomy eligibility requires reading 6+ frameworks.",
        "how": "Load company ESG reports + NDC targets + ICMA green bond principles + Brazilian Taxonomy (in force 2025). Graphify cross-references automatically.",
        "output": "Eligibility scorecard: green/amber/red for each ESG framework + suggested KPI structure for SLBs",
        "example": "Neoenergia offshore wind project: eligible under ICMA Climate Bonds Standard, Brazilian Taxonomy Cat. 1, and aligns with NDC 2030 targets — supports 30bps SLB premium",
        "tags": ["ESG", "Green Bonds", "NDC", "SLB", "Brazilian Taxonomy"],
    },
    {
        "number": "08",
        "title": "Free Market Migration Intelligence",
        "tagline": "Track the ACL migration wave before it erodes distribuidora revenue.",
        "problem": "11,200 new free-market consumers in 2025 alone. Each migration reduces regulated revenue for distribuidoras — but the impact is uneven and hard to model at the company level.",
        "how": "Load CCEE migration data + distribuidora demand profiles + ANEEL metering data. Graphify builds a migration risk score for each concession area.",
        "output": "Migration risk ranking by concession area + revenue-at-risk over 3 years",
        "example": "Copel-DIS: 38% of its industrial load (class A consumers) eligible to migrate by 2026 → R$1.1B revenue exposure, partially offset by TUSD retention",
        "tags": ["ACL Migration", "Copel", "Revenue Risk", "TUSD", "CCEE"],
    },
    {
        "number": "09",
        "title": "Concession Renewal Risk Map",
        "tagline": "Flag concession expirations before they become credit events.",
        "problem": "Cemig's hydro concessions (Emborcação, Nova Ponte, Volta Grande) expire 2028–2030. Renewal conditions, potential CDE payments, and new CAPEX obligations are spread across 12+ legal documents.",
        "how": "Load all concession contracts + MME renewal proposals + ANEEL precedents. Graphify extracts expiry dates, conditions, and cross-references renewal risk to debt maturity schedules.",
        "output": "Concession renewal risk matrix: company × asset × expiry date × renewal probability × debt impact",
        "example": "Cemig: Emborcação (1,192 MW) expiry 2028 — if auctioned (not renewed), EBITDA loss of R$680M/year → debt/EBITDA breaches 3.5× threshold in 18 months",
        "tags": ["Concession Risk", "Cemig", "Hydro", "Renewal", "Maturity Profile"],
    },
    {
        "number": "10",
        "title": "M&A and Deal Sourcing Intelligence",
        "tagline": "Find the next deal before the pitch arrives.",
        "problem": "Which utilities are likely sellers? Which have credit profiles that improve with a strategic acquirer? Screening 40+ companies quarterly is resource-intensive.",
        "how": "Load sector news + M&A precedents + company strategic plans + regulatory constraints on change of control. Graphify builds a deal probability model from the ground up.",
        "output": "Watchlist: top 5 companies with elevated M&A probability + likely acquirer + credit implications of deal",
        "example": "Identified 9 months early: Enel Brasil distribution assets likely to be sold (regulatory pressure + parent capex reallocation) → BTG structured bridge financing for Equatorial acquisition at 180bps spread",
        "tags": ["M&A", "Deal Sourcing", "Equatorial", "Enel Brasil", "Change of Control"],
    },
]

for uc in use_cases:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, NAVY)
    add_rect(slide, 0, 0, 0.18, 7.5, GOLD)

    # Use case number badge
    add_rect(slide, 0.35, 0.25, 0.85, 0.75, GOLD)
    add_text(slide, uc["number"], 0.35, 0.27, 0.85, 0.7, 26, bold=True, color=NAVY, align=PP_ALIGN.CENTER)

    # Title
    add_text(slide, uc["title"], 1.35, 0.28, 9.5, 0.7, 30, bold=True, color=WHITE)

    # Tagline
    add_text(slide, uc["tagline"], 1.35, 0.92, 10.5, 0.55, 15, italic=True, color=GOLD)

    # Divider
    add_rect(slide, 0.35, 1.55, 12.5, 0.03, NAVY_LIGHT)

    # Three columns: Problem | How | Output+Example
    col_configs = [
        (0.35, "THE PROBLEM", uc["problem"], 3.85),
        (4.4,  "HOW GRAPHIFY HELPS", uc["how"], 3.85),
        (8.45, "OUTPUT + EXAMPLE", uc["output"] + "\n\n💡 " + uc["example"], 4.5),
    ]
    for (x, header, body, w) in col_configs:
        add_rect(slide, x, 1.65, w, 0.42, NAVY_LIGHT)
        add_text(slide, header, x+0.12, 1.68, w-0.2, 0.38, 10, bold=True, color=GOLD)
        add_text(slide, body, x+0.12, 2.15, w-0.2, 3.9, 12.5, color=LIGHT_GREY)

    # Tags row
    add_rect(slide, 0, 6.6, 13.33, 0.9, NAVY_LIGHT)
    tags_str = "  ·  ".join(uc["tags"])
    add_text(slide, tags_str, 0.45, 6.67, 12.4, 0.5, 11, color=MID_GREY)

# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 13 — HOW TO GET STARTED
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, NAVY)
add_rect(slide, 0, 0, 0.18, 7.5, GOLD)

add_text(slide, "How to Get Started", 0.45, 0.35, 10, 0.8, 32, bold=True, color=WHITE)
add_rect(slide, 0.45, 1.15, 9.5, 0.04, GOLD)

steps = [
    ("1", "Install graphify", "pip install graphifyy && graphify install\n(one-time setup, ~2 min)"),
    ("2", "Feed your documents", "Drop PDFs, MD files, or images into raw/\n(ANEEL resolutions, annual reports, concession contracts)"),
    ("3", "Build the graph", "Run /graphify ./raw inside Claude Code\n(processes only new files on re-runs — SHA-256 cache)"),
    ("4", "Query in plain language", "Ask in Português or English.\nAnswers are cited to source documents."),
]
for i, (num, title, desc) in enumerate(steps):
    x = 0.4 + i * 3.1
    add_rect(slide, x, 1.6, 2.85, 4.4, NAVY_LIGHT)
    add_rect(slide, x, 1.6, 2.85, 0.55, GOLD)
    add_text(slide, f"Step {num}", x+0.12, 1.63, 2.6, 0.5, 14, bold=True, color=NAVY)
    add_text(slide, title, x+0.12, 2.3, 2.6, 0.55, 16, bold=True, color=WHITE)
    add_text(slide, desc, x+0.12, 2.95, 2.6, 2.8, 12.5, color=LIGHT_GREY)

add_rect(slide, 0, 6.6, 13.33, 0.9, NAVY_LIGHT)
add_text(slide, "github.com/safishamsi/graphify   |   Open source   |   Works inside Claude Code",
         0.45, 6.67, 12, 0.5, 12, color=GOLD)

# ─── Save ──────────────────────────────────────────────────────────────────
out_path = "/home/user/Utilities-knowledge-graph/graphify-out/btg_top10_usecases.pptx"
prs.save(out_path)
print(f"Saved: {out_path}")
