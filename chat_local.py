import os
import json
import requests
import sys

# Constants
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4" # Updating to Gemma 4 per user specifications!

def retrieve_context(query):
    """
    Scans the local Obsidian Wiki folder for relevant markdown pages based on query keywords.
    """
    wiki_dir = os.path.join(os.path.dirname(__file__), "wiki")
    if not os.path.exists(wiki_dir):
        return "The wiki/ folder does not exist. Please run ingest_wiki.py first."
        
    words = [w.lower() for w in query.split() if len(w) > 3]
    relevant_context = []
    
    import glob
    wiki_files = glob.glob(os.path.join(wiki_dir, "*.md"))
    
    for file in wiki_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            # Basic naive retrieval matching words against file content or filename
            if any(w in content.lower() or w in os.path.basename(file).lower() for w in words):
                # Keep snippet short
                snippet = content[:1000] # just grab the first 1000 chars of the matched page
                relevant_context.append(f"--- PAGE: {os.path.basename(file)} ---\n{snippet}")
                
    if not relevant_context:
        return "No relevant pages found in your Obsidian Wiki."
        
    return "\n".join(relevant_context[:5]) # Top 5 pages

def chat():
    print(f"==================================================")
    print(f"   BTG Utilities Obsidian Wiki (Model: {MODEL})")
    print(f"==================================================")
    
    wiki_dir = os.path.join(os.path.dirname(__file__), "wiki")
    if os.path.exists(wiki_dir):
        import glob
        num_docs = len(glob.glob(os.path.join(wiki_dir, "*.md")))
        print(f"Loaded Obsidian Vault with {num_docs} Wiki Pages.")
    else:
        print("Warning: wiki/ folder not found. Run ingest_wiki.py first.")
        
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            query = input("\nQuery > ")
        except (KeyboardInterrupt, EOFError):
            break
            
        if query.strip().lower() in ['exit', 'quit']:
            break
            
        if not query.strip():
            continue
            
        print("\nSearching Obsidian Wiki...")
        context = retrieve_context(query)
        
        prompt = f"""You are a specialized Credit Analyst Assistant. 
Answer the user's question using ONLY the provided Knowledge Graph Context below. If it's not in the context, say you don't know based on the graph.

KNOWLEDGE GRAPH CONTEXT:
{context}

QUESTION:
{query}
"""
        
        payload = {
            "model": MODEL,
            "prompt": prompt,
            "stream": True
        }
        
        print(f"Sending prompt to local {MODEL}...\n")
        print("Response: ", end="", flush=True)
        
        try:
            response = requests.post(OLLAMA_URL, json=payload, stream=True)
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line)
                        if "response" in chunk:
                            print(chunk["response"], end="", flush=True)
                print()
            else:
                print(f"Error: Ollama API returned status code {response.status_code}")
                try: 
                    print(response.json())
                except: 
                    pass
                print("\nMake sure Ollama is running (`ollama serve`) and the model is pulled (`ollama pull gemma4`).")
        except requests.exceptions.ConnectionError:
            print(f"\n[ERROR] Could not connect to Ollama at {OLLAMA_URL}.")
            print("To fix: Install Ollama (https://ollama.com) and start the app/service.")

if __name__ == "__main__":
    chat()
