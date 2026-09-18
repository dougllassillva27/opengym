#!/usr/bin/env python3
"""
Translate openGym exercise names to PT-BR with search aliases.
Uses the local qwenbridge proxy to batch-translate all 1324 exercises.
Output: frontend/src/lib/exercises-pt.js
"""
import json
import urllib.request
import sys
import time
import os

QWENBRIDGE_URL = "http://127.0.0.1:50002/v1/chat/completions"
BATCH_SIZE = 80
INPUT_FILE = "/tmp/exercises-names.json"
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "../frontend/src/lib/exercises-pt.js")
CACHE_FILE = "/tmp/exercises-pt-cache.json"

# Read API key from qwenbridge .env
def get_api_key():
    env_path = os.path.join(os.path.dirname(__file__), "../../../qwenbridge/.env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith("API_KEY="):
                    return line.strip().split("=", 1)[1]
    raise RuntimeError("Cannot read API_KEY from qwenbridge .env")

API_KEY = get_api_key()

SYSTEM_PROMPT = """Voce e um tradutor especializado em fitness/musculacao.
Recebe uma lista de exercicios em ingles com {id, n}.
Retorna APENAS um array JSON (sem markdown, sem explicacao) com:
[{"id":"...","nPt":"nome em portugues brasil","aliases":["sinonimo1","sinonimo2","sinonimo3"]}]

Regras:
- Use nomes populares de academia no Brasil (ex: "bench press" = "Supino Reto", não "pressão de banco")
- aliases devem ser termos que brasileiros digitariam na busca (inclua variações como "supino", "peito máquina", etc)
- Mantenha o id EXATAMENTE como recebido
- Se o exercício já for universal/latim, mantenha similar mas adicione aliases BR
- Retorne SOMENTE o JSON array, nada mais"""

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, ensure_ascii=False)

def translate_batch(batch, cache):
    # Check cache first
    uncached = [e for e in batch if e["id"] not in cache]
    if not uncached:
        return [cache[e["id"]] for e in batch]

    prompt = json.dumps(uncached, ensure_ascii=False)

    payload = json.dumps({
        "model": "qwen3.8-max-fast[1M]",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Traduza estes exercicios:\n{prompt}"}
        ],
        "temperature": 0.3
    }).encode()

    req = urllib.request.Request(
        QWENBRIDGE_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read())
                content = result["choices"][0]["message"]["content"].strip()
                # Strip markdown fences if present
                if content.startswith("```"):
                    lines = content.split("\n")
                    content = "\n".join(lines[1:-1] if lines[-1].startswith("```") else lines[1:])
                translated = json.loads(content)

                # Index by id
                by_id = {t["id"]: t for t in translated}

                # Update cache and return
                results = []
                for e in batch:
                    if e["id"] in by_id:
                        cache[e["id"]] = by_id[e["id"]]
                        results.append(by_id[e["id"]])
                    elif e["id"] in cache:
                        results.append(cache[e["id"]])
                    else:
                        # Fallback: keep english name
                        fallback = {"id": e["id"], "nPt": e["n"], "aliases": [e["n"].lower()]}
                        cache[e["id"]] = fallback
                        results.append(fallback)

                save_cache(cache)
                return results

        except Exception as ex:
            print(f"  Tentativa {attempt+1}/{max_retries} falhou: {ex}", file=sys.stderr)
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))
            else:
                print(f"  FALHA NO BATCH, usando fallback", file=sys.stderr)
                results = []
                for e in batch:
                    if e["id"] in cache:
                        results.append(cache[e["id"]])
                    else:
                        fallback = {"id": e["id"], "nPt": e["n"], "aliases": [e["n"].lower()]}
                        cache[e["id"]] = fallback
                        results.append(fallback)
                save_cache(cache)
                return results

def main():
    with open(INPUT_FILE) as f:
        exercises = json.load(f)

    print(f"Total: {len(exercises)} exercicios")
    cache = load_cache()
    print(f"Cache: {len(cache)} ja traduzidos")

    all_translated = []
    batches = [exercises[i:i+BATCH_SIZE] for i in range(0, len(exercises), BATCH_SIZE)]
    total_batches = len(batches)

    for idx, batch in enumerate(batches):
        print(f"Batch {idx+1}/{total_batches} ({len(batch)} exercicios)...")
        results = translate_batch(batch, cache)
        all_translated.extend(results)
        if idx < total_batches - 1:
            time.sleep(1)  # Rate limit courtesy

    # Verify completeness
    missing = [e["id"] for e in exercises if e["id"] not in cache]
    if missing:
        print(f"AVISO: {len(missing)} exercicios sem traducao", file=sys.stderr)

    # Generate JS module
    js_content = "// Auto-generated by scripts/translate-exercises.py — do not edit manually\n"
    js_content += "// Exercise name translations + search aliases for PT-BR\n"
    js_content += "export const EXPT = " + json.dumps(cache, ensure_ascii=False) + "\n"

    out_path = os.path.normpath(OUTPUT_FILE)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"\nPronto! {len(cache)} exercicios traduzidos -> {out_path}")
    print(f"Tamanho: {os.path.getsize(out_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()
