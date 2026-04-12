import os
import requests
import glob

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e2b" # Adjust this to your variant (e2b, etc.)
WIKI_DIR = "wiki"

def lint_knowledge_base():
    wiki_files = glob.glob(f"{WIKI_DIR}/*.md")
    
    if not wiki_files:
        print("Wiki is empty. Run ingest_wiki.py first.")
        return

    print("Gathering Wiki Content...")
    combined_content = ""
    for file in wiki_files:
        with open(file, "r", encoding="utf-8") as f:
            combined_content += f"\n\n--- Content from {os.path.basename(file)} ---\n"
            combined_content += f.read()

    # Note: For huge knowledge bases, you'd chunk this. For our MVP, we send the whole vault.
    prompt = f"""You are a strict data-quality Linter for an Obsidian Knowledge Base.
Analyze the following compiled Wiki documents. 
Your goal is to detect:
1. Any direct CONTRADICTIONS between claims in different pages.
2. Any STALE or out-of-date information given the context.
3. Logical gaps or hanging links.

Output your findings as a numbered list. If the database is perfectly coherent, reply "No issues found."

KNOWLEDGE BASE CONTENT:
{combined_content}
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": True # We'll stream the lint report to console
    }

    try:
        print(f"Linting... (Sending vault to {MODEL})\n")
        response = requests.post(OLLAMA_URL, json=payload, stream=True)
        
        if response.status_code == 200:
            print("LINT REPORT =>")
            report_text = ""
            for line in response.iter_lines():
                if line:
                    import json
                    chunk = json.loads(line)
                    text = chunk.get("response", "")
                    print(text, end="", flush=True)
                    report_text += text
            
            # Save the report
            with open(os.path.join(WIKI_DIR, "LINT_REPORT.md"), "w") as f:
                f.write("# Automated Lint Report\n\n" + report_text)
            print("\n\nReport saved to wiki/LINT_REPORT.md")
        else:
            print(f"Ollama API Error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"[ERROR] Could not connect to Ollama. Make sure you ran `ollama run {MODEL}`")


if __name__ == "__main__":
    lint_knowledge_base()
