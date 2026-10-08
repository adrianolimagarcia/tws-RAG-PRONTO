#!/usr/bin/env python3
"""Batch Offline Corpus Enricher com Concorrência e Checkpointing.

Executa enriquecimento de claims usando gemini-3.8-flash-medium via proxy local:
- Gera 3 perguntas operacionais em PT-BR
- Extrai termos operacionais e sinônimos
- Salva incrementalmente em data/export/enriched_claims_store.jsonl

Uso:
  python3 scripts/batch_enrich_corpus.py --workers 6 --limit 50
"""
import argparse
import concurrent.futures
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
STORE_PATH = "data/export/enriched_claims_store.jsonl"

PROMPT_ENRICH = """Você é um especialista sênior em HCL Workload Automation (TWS/HWA 10.2.8).
Analise o claim abaixo extraído da documentação técnica e gere:
1. 3 perguntas operacionais realistas em Português do Brasil (PT-BR) que um operador ou administrador faria e cuja resposta exata seja este claim.
2. Uma lista de palavras-chave, sinônimos, termos de busca e comandos correlatos em PT-BR e EN (ex: utilitários, mensagens de erro, parâmetros).

Regras rígidas:
- NÃO invente fatos nem parâmetros que não estejam fundamentados no texto.
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
            {"role": "system", "content": "Responda sempre em JSON estrito sem markdown ao redor."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1
    }
    data = json.dumps(payload).encode("utf-8")
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(LLM_URL, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                content = res["choices"][0]["message"]["content"]
                clean = re.sub(r"^```(?:json)?\s*", "", content.strip())
                clean = re.sub(r"\s*```$", "", clean.strip())
                return json.loads(clean)
        except Exception:
            if attempt == max_retries - 1:
                return {}
            time.sleep(1.0 + attempt * 0.5)
    return {}

def enrich_single(claim: dict) -> dict:
    cid = claim["claim_id"]
    txt = claim["claim"]
    prompt = PROMPT_ENRICH.format(claim_text=txt)
    t0 = time.time()
    res = call_llm(prompt)
    dur = time.time() - t0
    perguntas = res.get("perguntas", [])
    keywords = res.get("keywords", [])
    return {
        "claim_id": cid,
        "perguntas": perguntas,
        "keywords": keywords,
        "dur": round(dur, 2)
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--only-missing", action="store_true", default=False)
    args = parser.parse_args()

    # Carrega existentes
    ja_processados = set()
    if os.path.exists(STORE_PATH):
        with open(STORE_PATH, "r", encoding="utf-8") as f:
            for l in f:
                if l.strip():
                    try:
                        d = json.loads(l)
                        ja_processados.add(d["claim_id"])
                    except Exception:
                        pass
    print(f"Enriquecimentos já existentes no checkpoint: {len(ja_processados)}")

    # Lê corpus
    claims = [json.loads(l) for l in open(CORPUS_PATH, encoding="utf-8") if l.strip()]

    # Filtra alvos
    pendentes = []
    for c in claims:
        cid = c["claim_id"]
        if cid in ja_processados:
            continue
        if args.only_missing:
            if not c.get("synthetic_questions"):
                pendentes.append(c)
        else:
            pendentes.append(c)

    if args.limit > 0:
        pendentes = pendentes[:args.limit]

    print(f"Total de claims a processar neste lote: {len(pendentes)} (workers: {args.workers})")
    if not pendentes:
        print("Nenhum claim pendente.")
        return

    os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)
    t_start = time.time()
    concluidos = 0

    with open(STORE_PATH, "a", encoding="utf-8") as f_out:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            future_to_claim = {executor.submit(enrich_single, c): c for c in pendentes}
            for future in concurrent.futures.as_completed(future_to_claim):
                res = future.result()
                cid = res["claim_id"]
                p_cnt = len(res["perguntas"])
                k_cnt = len(res["keywords"])
                concluidos += 1
                if p_cnt > 0 or k_cnt > 0:
                    f_out.write(json.dumps(res, ensure_ascii=False) + "\n")
                    f_out.flush()
                dur_total = time.time() - t_start
                rate = concluidos / dur_total if dur_total > 0 else 0.0
                print(f"[{concluidos}/{len(pendentes)}] {cid} -> {p_cnt} perguntas, {k_cnt} keywords ({res['dur']}s) | vel: {rate*60:.1f} claims/min")

    print(f"\nLote finalizado em {time.time()-t_start:.1f}s. Resultados salvos em {STORE_PATH}")

if __name__ == "__main__":
    main()
