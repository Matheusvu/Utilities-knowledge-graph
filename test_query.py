import json

with open("graphify-out/graph.json", "r") as f:
    data = json.load(f)

# Find edges involving Cemig with actual logic extracted
results = []
for link in data.get("links", []):
    src = str(link.get("source", "")).lower()
    tgt = str(link.get("target", "")).lower()
    desc = str(link.get("description", ""))
    
    if "cemig" in src or "cemig" in tgt:
        if desc and desc != "N/A" and desc != "None":
            results.append(f"• [{link.get('source')}] ↔️ [{link.get('target')}]\n   AI Logic: {desc}")

# Find any inferred relationships globally
inferred = []
for link in data.get("links", []):
    if link.get("is_inferred", False) or link.get("inference_type") == "conceptually_related_to":
        src = str(link.get("source", ""))
        tgt = str(link.get("target", ""))
        if "Cemig" in src or "Cemig" in tgt or "WACC" in src or "WACC" in tgt or "ACL" in src or "ACL" in tgt:
            inferred.append(f"🧠 INFERRED: [{src}] ↔️ [{tgt}]\n   Why: {link.get('description', 'Conceptually linked')}")

print(f"--- DETAILED CONNECTIONS FOR CEMIG ---")
for r in results[:3]: 
    print(r)

print(f"\n--- AI INFERRED RELATIONSHIPS (Not explicitly stated in one doc) ---")
for i in inferred[:3]:
    print(i)
