#!/usr/bin/env python3
"""Offline Corpus Enricher usando LLM local (gemini-3.8-flash-medium).

Gera termos operacionais, sinônimos e perguntas sintéticas em PT-BR para claims
que possuem pouca ou nenhuma ancoragem textual, enriquecendo o índice BM25 de forma offline.

Uso:
  python3 scripts/enrich_corpus_offline.py --limit 10 --test-dry-run
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request

LLM_URL = os.environ.get("LLM_URL", "http://100.77.31.78:8790/v1/chat/completions")
LLM_KEY = os.environ.get("LLM_KEY", "sk-antigravity-proxy")
LLM_MODEL = os.environ.get("LLM_MODEL", "gemini-3.8-flash-medium")

CORPUS_PATH = "data/export/tws_corpus_master_consolidated.jsonl"

PROMPT_ENRICH = """Você é um especialista sênior em HCL Workload Automation (TWS/HWA 10.2.8).
Analise o claim abaixo extraído da documentação técnica e gere:
1. 3 perguntas operacionais realistas em Português do Brasil (PT-BR) que um operador, analista de suporte ou administrador faria e cuja resposta exata seja este claim.
2. Uma lista de palavras-chave, sinônimos, termos de busca e comandos correlatos em PT-BR e EN (ex: nomes de utilitários, mensagens de erro, parâmetros).

Regras rígidas:
- NÃO invente fatos nem parâmetros que não estão no texto.
- Foque em linguagem prática de quem opera o sistema no dia a dia.
- Responda EXCLUSIVAMENTE em formato JSON válido com as chaves:
  "perguntas": ["pergunta 1", "pergunta 2", "pergunta 3"],
  "keywords": ["keyword 1", "keyword 2", ...]

Texto do Claim:
{claim_text}
"""

def call_llm(prompt: str, max_retries: int = 3) -> dict:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LLM_KEY}"
    }
    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": "Responda sempre em JSON válido."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1
    }
    data = json.dumps(payload).encode("utf-8")
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(LLM_URL, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=25) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                content = res["choices"][0]["message"]["content"]
                # Limpa blocos markdown ```json ... ``` se existirem
                clean = re.sub(r"^```(?:json)?\s*", "", content.strip())
                clean = re.sub(r"\s*```$", "", clean.strip())
                return json.loads(clean)
        except Exception as e:
            if attempt == max_retries - 1:
                return {}
            time.sleep(1.0)
    return {}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--claim-id", type=str, default="")
    parser.add_argument("--out", type=str, default="data/export/enriched_samples.json")
    args = parser.parse_args()

    print(f"Lendo corpus {CORPUS_PATH}...")
    claims = [json.loads(line) for line in open(CORPUS_PATH, encoding="utf-8") if line.strip()]

    if args.claim_id:
        target_claims = [c for c in claims if c["claim_id"] == args.claim_id]
    else:
        # Prioriza claims sem synthetic_questions
        target_claims = [c for c in claims if not c.get("synthetic_questions")][:args.limit]

    print(f"Total de claims selecionados para enriquecimento: {len(target_claims)}")
    results = []
    for i, c in enumerate(target_claims):
        cid = c["claim_id"]
        txt = c["claim"]
        print(f"[{i+1}/{len(target_claims)}] Enriquecendo {cid}...")
        prompt = PROMPT_ENRICH.format(claim_text=txt)
        t0 = time.time()
        res = call_llm(prompt)
        dur = time.time() - t0
        perguntas = res.get("perguntas", [])
        keywords = res.get("keywords", [])
        print(f"   -> {len(perguntas)} perguntas, {len(keywords)} keywords ({dur:.2f}s)")
        results.append({
            "claim_id": cid,
            "perguntas": perguntas,
            "keywords": keywords
        })

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Enriquecimento salvo em {args.out}")

if __name__ == "__main__":
    main()
