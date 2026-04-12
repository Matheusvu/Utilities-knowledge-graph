import os
import json
import requests
import glob

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e2b" # Adjust this to your variant (e2b, etc.)
RAW_DIR = "raw"
WIKI_DIR = "wiki"

def summarize_to_wiki(file_path):
    print(f"Reading: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Could not read {file_path}: {e}")
        return None

    prompt = f"""You are maintaining an Obsidian Markdown Wiki.
Summarize the core facts from the following text. 
Create an Obsidian-compatible markdown page structure with:
1. A concise title/header
2. Use [[Double Brackets]] for key entities, topics, or concepts you think should be dedicated wiki pages.
3. Bullet points of the most critical information, avoiding fluff.

SOURCE TEXT:
{content}
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            print(f"Ollama API Error: {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        print(f"[ERROR] Could not connect to Ollama. Make sure you ran `ollama run {MODEL}`")
        return None

def process_all_raw():
    os.makedirs(WIKI_DIR, exist_ok=True)
    raw_files = glob.glob(f"{RAW_DIR}/**/*.md", recursive=True) + glob.glob(f"{RAW_DIR}/**/*.txt", recursive=True)
    
    if not raw_files:
        print("No raw files found.")
        return

    print(f"Found {len(raw_files)} files. Ingesting to Wiki...")
    for idx, filepath in enumerate(raw_files):
        print(f"[{idx+1}/{len(raw_files)}] Processing {filepath}...")
        wiki_content = summarize_to_wiki(filepath)
        
        if wiki_content:
            # Generate a safe filename based on original path
            filename = os.path.basename(filepath)
            safe_name = filename.replace(".txt", "").replace(".md", "")
            out_file = os.path.join(WIKI_DIR, f"{safe_name}_Wiki.md")
            
            with open(out_file, "w", encoding="utf-8") as out:
                out.write(wiki_content)
            print(f"  -> Saved to {out_file}\n")
        else:
            print(f"  -> Failed to ingest {filepath}\n")

if __name__ == "__main__":
    process_all_raw()
    print("Ingestion complete. Open your `wiki` folder in Obsidian!")
