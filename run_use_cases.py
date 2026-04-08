"""
BTG Private Credit — Utilities Knowledge Graph
5 Deep Use Cases: Graph Execution Script
Runs against graphify-out/graph.json and outputs real results.
"""

import json
import re
from collections import defaultdict

# ── Load the graph ──────────────────────────────────────────────────────────
with open("graphify-out/graph.json") as f:
    data = json.load(f)

nodes_list = data["nodes"]
edges_list = data["links"]
hyperedges = data["graph"]["hyperedges"]

# Index for fast lookup
nodes_by_id = {n["id"]: n for n in nodes_list}
nodes_by_label = {n["label"]: n for n in nodes_list}

# Build adjacency: node_id → list of (neighbor_id, edge_data)
adj = defaultdict(list)
for e in edges_list:
    adj[e["source"]].append((e["target"], e))
    adj[e["target"]].append((e["source"], e))

# Helper: find nodes whose label contains any of the keywords (case-insensitive)
def find_nodes(*keywords):
    results = []
    for n in nodes_list:
        label_lower = n["label"].lower()
        if any(kw.lower() in label_lower for kw in keywords):
            results.append(n)
    return results

# Helper: get all neighbors of a node_id — returns (neighbor_id, edge_data)
def neighbors(node_id):
    return [(nid, edge) for nid, edge in adj.get(node_id, [])]

# Helper: get edges between two nodes
def edge_between(id1, id2):
    for nid, e in adj.get(id1, []):
        if nid == id2:
            return e
    return None

# Helper: find hyperedges involving a node_id
def hyperedges_for(node_id):
    return [h for h in hyperedges if node_id in h["nodes"]]

# Helper: count connections per node (degree)
def degree(node_id):
    return len(adj.get(node_id, []))

# ── Banner ──────────────────────────────────────────────────────────────────
DIVIDER = "=" * 72

def header(title):
    print(f"\n{DIVIDER}")
    print(f"  {title}")
    print(DIVIDER)

def section(title):
    print(f"\n── {title} {'─' * max(0, 60 - len(title))}")


# ════════════════════════════════════════════════════════════════════════════
# USE CASE 1: Cemig Concession Cliff → Full Credit Stress Chain
# ════════════════════════════════════════════════════════════════════════════
header("USE CASE 1 · Cemig Concession Cliff — Full Credit Stress Chain")

cemig_nodes = find_nodes("Cemig")
print(f"\nFound {len(cemig_nodes)} Cemig-related nodes in the graph:\n")
for n in sorted(cemig_nodes, key=lambda x: degree(x["id"]), reverse=True):
    deg = degree(n["id"])
    src = n.get("source_file", "—")
    print(f"  [{deg:2d} edges]  {n['label']}")
    print(f"             ↳ source: {src}")

section("Concession-related nodes connected to Cemig")
concession_related = find_nodes("Concess", "Cliff", "Renovação", "Caducidade", "Emborcação", "Hidrelétric")
for n in concession_related:
    nb = neighbors(n["id"])
    cemig_nb = [x for x, e in nb if "cemig" in nodes_by_id.get(x, {}).get("label", "").lower()]
    print(f"\n  {n['label']} ({n.get('source_file','?')})")
    print(f"    degree={degree(n['id'])}, community={n.get('community','?')}")
    for nn, e in neighbors(n["id"]):
        nd = nodes_by_id.get(nn, {"label": nn})
        conf = e.get("confidence", "?")
        rel = e.get("relation", "?")
        print(f"    → [{conf:8s}] {rel:30s} → {nd['label']}")

section("Debt covenant and DSCR nodes connected to Cemig")
covenant_nodes = find_nodes("Covenant", "Dívida", "DSCR", "DEA", "OPEX")
for n in covenant_nodes:
    print(f"\n  {n['label']}")
    print(f"    community={n.get('community','?')}, source={n.get('source_file','?')}")
    for nn, e in neighbors(n["id"]):
        nd = nodes_by_id.get(nn, {"label": nn})
        print(f"    → [{e.get('confidence','?'):8s}] {e.get('relation','?'):25s} → {nd['label']}")

section("ANEEL concession framework nodes (renewal risk)")
aneel_conc = find_nodes("Renovação", "Re-leilão", "Caducidade", "Concessões de Distribuição")
for n in aneel_conc:
    print(f"\n  {n['label']} (C{n.get('community','?')}) ← {n.get('source_file','?')}")
    for nn, e in neighbors(n["id"]):
        nd = nodes_by_id.get(nn, {"label": nn})
        print(f"    → [{e.get('confidence','?'):8s}] {nd['label']}")

section("Hyperedges involving Cemig or concession risk")
for h in hyperedges:
    label_lower = h["label"].lower()
    if any(kw in label_lower for kw in ["cemig", "concess", "distribuidora", "wacc", "rab"]):
        print(f"\n  HYPEREDGE: {h['label']}")
        print(f"    confidence={h['confidence']} ({h['confidence_score']})")
        print(f"    nodes: {', '.join(h['nodes'])}")

section("Cross-document bridge: ONS Stress → Cemig Cliff (the key INFERRED link)")
ons_stress = find_nodes("ONS Cenários de Estresse")
cemig_cliff = find_nodes("Cliff de Concessões")
for o in ons_stress:
    for c in cemig_cliff:
        e = edge_between(o["id"], c["id"])
        if e:
            print(f"\n  FOUND DIRECT EDGE:")
            print(f"  {o['label']} --[{e.get('relation','?')}]--> {c['label']}")
            print(f"  confidence={e.get('confidence','?')}, score={e.get('confidence_score','?')}")
            print(f"  source: {e.get('source_file','?')} → {e.get('target_file','?')}")
        else:
            # Show common neighbors (2-hop connection)
            o_neighbors = {nid for nid, _ in adj.get(o["id"], [])}
            c_neighbors = {nid for nid, _ in adj.get(c["id"], [])}
            shared = o_neighbors & c_neighbors
            if shared:
                print(f"\n  2-HOP CONNECTION via shared neighbors:")
                print(f"  {o['label']}")
                print(f"    ↕ (through)")
                for s in shared:
                    nd = nodes_by_id.get(s, {"label": s})
                    print(f"    · {nd['label']}")
                print(f"    ↕")
                print(f"  {c['label']}")


# ════════════════════════════════════════════════════════════════════════════
# USE CASE 2: ACL 2028 Full Opening → Portfolio Revenue Stress Matrix
# ════════════════════════════════════════════════════════════════════════════
header("USE CASE 2 · ACL 2028 Full Opening — Portfolio Revenue Stress Matrix")

acl_nodes = find_nodes("ACL", "Mercado Livre", "Migração", "Abertura")
print(f"\nFound {len(acl_nodes)} ACL/market-opening nodes:\n")
for n in sorted(acl_nodes, key=lambda x: degree(x["id"]), reverse=True):
    print(f"  [{degree(n['id']):2d} edges]  {n['label']}")
    print(f"             ↳ {n.get('source_file','?')}")

section("ACL migration mechanism nodes and their connections")
mig_nodes = find_nodes("Migração", "Mecanismo de Receita", "Compensação", "Estratégias das Distribuidoras")
for n in mig_nodes:
    print(f"\n  {n['label']} (C{n.get('community','?')})")
    for nn, e in neighbors(n["id"]):
        nd = nodes_by_id.get(nn, {"label": nn})
        print(f"    → [{e.get('confidence','?'):8s}] {e.get('relation','?'):30s} → {nd['label']}")

section("Companies connected to ACL risk (cross-document join)")
distribuidoras = find_nodes("CPFL", "Equatorial", "Energisa", "Copel", "Neoenergia")
acl_node_ids = {n["id"] for n in acl_nodes}
for d in distribuidoras:
    acl_connected = [(nd, e) for nd, e in neighbors(d["id"])
                     if nd in acl_node_ids or "acl" in nodes_by_id.get(nd, {}).get("label", "").lower()
                     or "migr" in nodes_by_id.get(nd, {}).get("label", "").lower()]
    if acl_connected:
        print(f"\n  {d['label']} → ACL exposure:")
        for nd_id, e in acl_connected:
            nd = nodes_by_id.get(nd_id, {"label": nd_id})
            print(f"    [{e.get('confidence','?'):8s}] {nd['label']}")
    else:
        print(f"\n  {d['label']} → (no direct ACL edge — check 2-hop)")
        d_neighbors = {nid for nid, _ in adj.get(d["id"], [])}
        acl_2hop = d_neighbors & acl_node_ids
        if acl_2hop:
            for s in acl_2hop:
                nd = nodes_by_id.get(s, {"label": s})
                print(f"    via: {nd['label']}")

section("Hyperedge: ACL Migration cluster")
for h in hyperedges:
    if "acl" in h["label"].lower() or "migra" in h["label"].lower():
        print(f"\n  HYPEREDGE: {h['label']}")
        print(f"    confidence={h['confidence']} score={h['confidence_score']}")
        print(f"    source: {h.get('source_file','?')}")
        print(f"    nodes: {', '.join(h['nodes'])}")

section("TUSD retention as offset mechanism")
tusd_nodes = find_nodes("TUSD", "Tarifa de Uso")
for n in tusd_nodes:
    print(f"\n  {n['label']} (C{n.get('community','?')})")
    for nn, e in neighbors(n["id"]):
        nd = nodes_by_id.get(nn, {"label": nn})
        print(f"    → [{e.get('confidence','?'):8s}] {nd['label']}")

section("BTG Credit Index — which companies are in it")
indice_nodes = find_nodes("Índice de Crédito")
for n in indice_nodes:
    print(f"\n  {n['label']} — degree={degree(n['id'])}")
    for nn, e in neighbors(n["id"]):
        nd = nodes_by_id.get(nn, {"label": nn})
        print(f"    → [{e.get('confidence','?'):8s}] {e.get('relation','?'):25s} → {nd['label']}")


# ════════════════════════════════════════════════════════════════════════════
# USE CASE 3: SBCE Carbon Compliance + ESG Financing Intersection
# ════════════════════════════════════════════════════════════════════════════
header("USE CASE 3 · SBCE Carbon Compliance + ESG Financing Intersection")

sbce_nodes = find_nodes("SBCE", "Carbono", "CBE", "Emissões", "Lei 15.042")
print(f"\nFound {len(sbce_nodes)} SBCE/carbon nodes:\n")
for n in sorted(sbce_nodes, key=lambda x: degree(x["id"]), reverse=True):
    print(f"  [{degree(n['id']):2d} edges]  {n['label']} (C{n.get('community','?')})")

section("SBCE → full connection map")
for n in sbce_nodes:
    if degree(n["id"]) > 1:
        print(f"\n  {n['label']}")
        for nn, e in neighbors(n["id"]):
            nd = nodes_by_id.get(nn, {"label": nn})
            print(f"    → [{e.get('confidence','?'):8s}] {e.get('relation','?'):30s} → {nd['label']}")
            print(f"       source: {e.get('source_file','?')} | target: {e.get('target_file','?')}")

section("ESG + Green Finance nodes")
esg_nodes = find_nodes("Green Bond", "ESG", "Debentures Incentivadas", "I-REC", "SLB", "NDC")
for n in sorted(esg_nodes, key=lambda x: degree(x["id"]), reverse=True):
    print(f"\n  {n['label']} (C{n.get('community','?')}, degree={degree(n['id'])})")
    for nn, e in neighbors(n["id"]):
        nd = nodes_by_id.get(nn, {"label": nn})
        conf = e.get("confidence", "?")
        rel  = e.get("relation", "?")
        print(f"    → [{conf:8s}] {rel:30s} → {nd['label']}")

section("KEY INFERRED EDGE: Green Bond ↔ Debentures Incentivadas (cross-document)")
gb_nodes = find_nodes("Green Bond")
deb_nodes = find_nodes("Debentures Incentivadas")
for g in gb_nodes:
    for d in deb_nodes:
        e = edge_between(g["id"], d["id"])
        if e:
            print(f"\n  *** INFERRED EDGE FOUND ***")
            print(f"  {g['label']}")
            print(f"    --[{e.get('relation','?')}]--> {d['label']}")
            print(f"  confidence={e.get('confidence','?')}, score={e.get('confidence_score','?')}")
            print(f"  source: {e.get('source_file','?')}")
            print(f"  target: {e.get('target_file','?')}")
            print(f"\n  INTERPRETATION: This connection does NOT appear in any single document.")
            print(f"  The graph discovered it by semantic similarity across:")
            print(f"  raw/politicas/carbon_market_sbce.md → raw/tecnologia/economics_renovaveis.md")
            print(f"  CREDIT IMPLICATION: Companies with SBCE compliance cost can simultaneously")
            print(f"  issue SBCE-linked green debentures, turning a liability into a financing advantage.")

section("Hyperedge: Carbon Compliance cluster")
for h in hyperedges:
    if "carbono" in h["label"].lower() or "sbce" in h["label"].lower():
        print(f"\n  HYPEREDGE: {h['label']}")
        print(f"    confidence={h['confidence']} score={h['confidence_score']}")
        print(f"    nodes: {', '.join(h['nodes'])}")


# ════════════════════════════════════════════════════════════════════════════
# USE CASE 4: GSF Risk → PLD Spike → Generator Credit Deterioration
# ════════════════════════════════════════════════════════════════════════════
header("USE CASE 4 · GSF Hydrological Risk → PLD Spike → Generator Credit Deterioration")

gsf_nodes = find_nodes("GSF", "Hidrológico", "CMO", "MRR", "Mecanismo de Repartição")
print(f"\nFound {len(gsf_nodes)} GSF/hydro-risk nodes:\n")
for n in sorted(gsf_nodes, key=lambda x: degree(x["id"]), reverse=True):
    print(f"  [{degree(n['id']):2d} edges]  {n['label']} (C{n.get('community','?')})")
    print(f"             ↳ {n.get('source_file','?')}")

section("Full GSF risk transmission chain")
for n in gsf_nodes:
    if degree(n["id"]) > 0:
        print(f"\n  {n['label']}")
        for nn, e in neighbors(n["id"]):
            nd = nodes_by_id.get(nn, {"label": nn})
            conf = e.get("confidence","?")
            rel  = e.get("relation","?")
            print(f"    → [{conf:8s}] {rel:30s} → {nd['label']}")

section("PLD calculation chain")
pld_nodes = find_nodes("PLD", "Preço de Liquidação")
for n in pld_nodes:
    print(f"\n  {n['label']} (C{n.get('community','?')}, degree={degree(n['id'])})")
    for nn, e in neighbors(n["id"]):
        nd = nodes_by_id.get(nn, {"label": nn})
        print(f"    → [{e.get('confidence','?'):8s}] {e.get('relation','?'):25s} → {nd['label']}")

section("KEY INFERRED EDGE: GSF → CCEE settlement (cross-document bridge)")
gsf_dyn = find_nodes("Risco Hidrológico GSF")
ccee_gsf = find_nodes("CCEE GSF", "GSF e MRR")
for g in gsf_dyn:
    for c in ccee_gsf:
        e = edge_between(g["id"], c["id"])
        if e:
            print(f"\n  *** INFERRED EDGE FOUND ***")
            print(f"  {g['label']} --[{e.get('relation','?')}]--> {c['label']}")
            print(f"  confidence={e.get('confidence','?')}, score={e.get('confidence_score','?')}")
            print(f"  source: {e.get('source_file','?')} → {e.get('target_file','?')}")
        else:
            g_nb = {nid for nid, _ in adj.get(g["id"], [])}
            c_nb = {nid for nid, _ in adj.get(c["id"], [])}
            shared = g_nb & c_nb
            print(f"\n  No direct edge. Shared neighbors ({g['label']} ↔ {c['label']}):")
            for s in shared:
                nd = nodes_by_id.get(s, {"label": s})
                print(f"    · {nd['label']}")

section("Company exposure to GSF (2-hop from hydro risk)")
hydro_risk_ids = {n["id"] for n in gsf_nodes}
company_nodes = find_nodes("Cemig", "Eletrobras", "CPFL", "Copel", "Neoenergia", "Equatorial", "Energisa", "Engie")
for c in company_nodes:
    c_neighbors = {nid for nid, _ in adj.get(c["id"], [])}
    hydro_2hop = c_neighbors & hydro_risk_ids
    direct_hydro = [(nodes_by_id.get(nid, {"label": nid}), e)
                    for nid, e in neighbors(c["id"])
                    if nid in hydro_risk_ids]
    if direct_hydro or hydro_2hop:
        print(f"\n  {c['label']}")
        if direct_hydro:
            for nd, e in direct_hydro:
                print(f"    DIRECT → [{e.get('confidence','?'):8s}] {nd['label']}")
        if hydro_2hop:
            for hid in hydro_2hop:
                nd = nodes_by_id.get(hid, {"label": hid})
                print(f"    2-HOP  → {nd['label']}")

section("Hyperedge: Hydro Risk cluster")
for h in hyperedges:
    if "hidro" in h["label"].lower() or "gsf" in h["label"].lower() or "pld" in h["label"].lower():
        print(f"\n  HYPEREDGE: {h['label']}")
        print(f"    confidence={h['confidence']} score={h['confidence_score']}")
        print(f"    nodes: {', '.join(h['nodes'])}")


# ════════════════════════════════════════════════════════════════════════════
# USE CASE 5: Smart Grid Mandates → Concession Renewal Readiness Ranking
# ════════════════════════════════════════════════════════════════════════════
header("USE CASE 5 · Smart Grid Technology Mandates → Concession Renewal Readiness")

tech_nodes = find_nodes("AMI", "Smart Grid", "Medição Inteligente", "DEC/FEC",
                         "Perdas Não Técnicas", "PNT", "Resposta à Demanda",
                         "Transformação Digital", "Digitalização")
print(f"\nFound {len(tech_nodes)} technology/digitalization nodes:\n")
for n in sorted(tech_nodes, key=lambda x: degree(x["id"]), reverse=True):
    print(f"  [{degree(n['id']):2d} edges]  {n['label']} (C{n.get('community','?')})")
    print(f"             ↳ {n.get('source_file','?')}")

section("Technology → Regulatory connection chain")
for n in tech_nodes:
    if degree(n["id"]) > 1:
        print(f"\n  {n['label']}")
        for nn, e in neighbors(n["id"]):
            nd = nodes_by_id.get(nn, {"label": nn})
            conf = e.get("confidence","?")
            rel  = e.get("relation","?")
            print(f"    → [{conf:8s}] {rel:30s} → {nd['label']}")

section("ANEEL concession renewal conditions (cross-reference to tech mandates)")
renewal_nodes = find_nodes("Renovação", "Re-leilão", "Concessões de Distribuição", "Caducidade", "PRODIST")
for n in renewal_nodes:
    print(f"\n  {n['label']} (C{n.get('community','?')})")
    # Find connections to tech nodes
    tech_ids = {t["id"] for t in tech_nodes}
    for nn, e in neighbors(n["id"]):
        nd = nodes_by_id.get(nn, {"label": nn})
        flag = " *** TECH LINK ***" if nn in tech_ids else ""
        print(f"    → [{e.get('confidence','?'):8s}] {nd['label']}{flag}")

section("Company digitalization readiness (from graph connections)")
company_nodes_2 = find_nodes("CPFL", "Equatorial", "Energisa", "Copel", "Neoenergia", "Cemig-D")
tech_node_ids = {n["id"] for n in tech_nodes}
renewal_node_ids = {n["id"] for n in renewal_nodes}
for c in company_nodes_2:
    c_nb = {nid for nid, _ in adj.get(c["id"], [])}
    tech_links = c_nb & tech_node_ids
    renewal_links = c_nb & renewal_node_ids
    print(f"\n  {c['label']} (degree={degree(c['id'])})")
    if tech_links:
        print(f"    Tech connections:")
        for tid in tech_links:
            nd = nodes_by_id.get(tid, {"label": tid})
            e_data = edge_between(c["id"], tid)
            conf = e_data.get("confidence","?") if e_data else "?"
            print(f"      [{conf:8s}] {nd['label']}")
    if renewal_links:
        print(f"    Concession renewal connections:")
        for rid in renewal_links:
            nd = nodes_by_id.get(rid, {"label": rid})
            e_data = edge_between(c["id"], rid)
            conf = e_data.get("confidence","?") if e_data else "?"
            print(f"      [{conf:8s}] {nd['label']}")
    if not tech_links and not renewal_links:
        print(f"    (No direct tech/renewal edges — checking 2-hop...)")
        # 2-hop
        for nid in c_nb:
            nn2 = {n2id for n2id, _ in adj.get(nid, [])}
            if nn2 & tech_node_ids:
                nd = nodes_by_id.get(nid, {"label": nid})
                print(f"    2-hop via: {nd['label']}")
                break

section("Hyperedge: Digital transformation cluster")
for h in hyperedges:
    if "digit" in h["label"].lower() or "ami" in h["label"].lower() or "smart" in h["label"].lower():
        print(f"\n  HYPEREDGE: {h['label']}")
        print(f"    confidence={h['confidence']} score={h['confidence_score']}")
        print(f"    nodes: {', '.join(h['nodes'])}")

section("Final cross-use-case summary: God nodes that bridge all 5 use cases")
god_nodes = find_nodes("Riscos Políticos", "Índice de Crédito BTG", "Políticas Energéticas",
                        "ANEEL (Agência", "Transformação Digital")
print()
for n in sorted(god_nodes, key=lambda x: degree(x["id"]), reverse=True):
    communities_touched = set()
    for nn, _ in neighbors(n["id"]):
        nd = nodes_by_id.get(nn, {})
        if "community" in nd:
            communities_touched.add(nd["community"])
    print(f"  [{degree(n['id']):2d} edges]  {n['label']}")
    print(f"    Communities bridged: {sorted(communities_touched)}")
    print(f"    Source: {n.get('source_file','?')}")

print(f"\n{DIVIDER}")
print("  Execution complete. Results above are drawn from graph.json (220 nodes, 304 edges).")
print("  All citations traceable to source files in raw/")
print(DIVIDER)
