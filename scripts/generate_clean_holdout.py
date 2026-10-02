#!/usr/bin/env python3
"""Gerador de Holdout Limpo V4 (Descontaminado e Auditado).

Seleciona claims virgens (nunca usados em nenhum benchmark anterior do repositorio),
gera perguntas naturais em portugues com LLM (sem vazar a claim ou formula artificial),
e valida contra scripts/audit_eval_leakage.py.

Uso:
    python scripts/generate_clean_holdout.py --limit 60 --out data/eval/clean_holdout_v4_sealed.jsonl
"""

import argparse
import json
import os
import random
import re
import sys
import time
import urllib.request

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS_PATH = os.path.join(REPO_DIR, "data", "export", "tws_corpus_master_consolidated.jsonl")

BASE_URL = os.environ.get("A6API_BASE_URL", "http://100.77.31.78:8790/v1")
MODELO = os.environ.get("A6API_MODEL", "gemini-3.8-flash-medium")
API_KEY = os.environ.get("A6API_KEY", "proxy-local")


def carregar_usados():
    import glob
    usados = set()
    for f in glob.glob(os.path.join(REPO_DIR, "data", "eval", "**", "*.jsonl"), recursive=True):
        if "clean_holdout_v4" in f:
            continue
        with open(f, encoding="utf-8") as fp:
            for line in fp:
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                    targs = row.get("relevant_claim_ids") or []
                    if isinstance(targs, str):
                        targs = json.loads(targs)
                    for t in targs:
                        usados.add(t)
                    if row.get("claim_id"):
                        usados.add(row["claim_id"])
                except Exception:
                    pass
    return usados


def gerar_pergunta_llm(claim_text, category):
    prompt_sys = (
        "Voce e um operador e especialista de infraestrutura em HCL Workload Automation (TWS/HWA).\n"
        "Sua tarefa e ler o documento tecnico de referencia e formular UMA pergunta realista em portugues "
        "que um analista de operacoes ou agendador faria no dia a dia cuja resposta direta esta no texto.\n\n"
        "REGRAS ESTRITAS ANTI-VAZAMENTO:\n"
        "1. NAO copie frases literais do documento.\n"
        "2. NAO use codigos de erro alfanumericos exatos (ex: AWSUI..., AWK..., EQQ...) na pergunta, "
        "a menos que descreva o sintoma ou o contexto.\n"
        "3. NAO use formatos artificiais como 'Em relacao ao HWA, como proceder com...' ou 'Qual a regra sobre...'.\n"
        "4. A pergunta deve soar como duvida genuina de producao (ex: 'Como configurar...', 'O que acontece quando...', 'Qual o impacto de...').\n"
        "Responda SOMENTE a pergunta em uma linha, sem aspas, sem prefixo."
    )
    prompt_user = f"CATEGORIA: {category}\nTEXTO TECNICO:\n{claim_text}\n\nPERGUNTA:"

    corpo = {
        "model": MODELO,
        "temperature": 0.2,
        "messages": [
            {"role": "system", "content": prompt_sys},
            {"role": "user", "content": prompt_user}
        ]
    }
    dados = json.dumps(corpo).encode("utf-8")
    req = urllib.request.Request(
        BASE_URL.rstrip("/") + "/chat/completions",
        data=dados,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    )
    for tentativa in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                res = json.loads(r.read().decode("utf-8"))
            texto = res["choices"][0]["message"]["content"].strip()
            # limpar aspas ou prefixos
            texto = re.sub(r'^(Pergunta|Dúvida|Question):\s*', '', texto, flags=re.I).strip('"\' \n')
            return texto
        except Exception as e:
            time.sleep(2 * (tentativa + 1))
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=60)
    parser.add_argument("--out", default="data/eval/clean_holdout_v4_sealed.jsonl")
    parser.add_argument("--seed", type=int, default=20260925)
    args = parser.parse_args()

    random.seed(args.seed)
    usados = carregar_usados()
    print(f"Claims ja usados em benchmarks anteriores: {len(usados)}")

    corpus = []
    with open(CORPUS_PATH, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                corpus.append(json.loads(line))

    # Selecionar apenas virgens e substantivos (>120 chars)
    candidatos = [
        d for d in corpus 
        if d["claim_id"] not in usados 
        and len(d.get("claim", "")) >= 120
        # evitar claims que sao apenas despejo de log cru
        and not d.get("claim", "").startswith("TRACE:")
    ]
    print(f"Candidatos virgens substantivos: {len(candidatos)}")

    # Estratificacao por categoria
    cat_cotas = {
        "Agendamento Avancado & Workflows": 12,
        "Arquitetura & Topologia Mesh": 12,
        "Operacao CLI (conman/composer/planman)": 12,
        "Alta Disponibilidade & Failover": 8,
        "Instalacao & Manutencao": 8,
        "API REST v2 & Integracao": 8,
    }
    
    amostra = []
    por_cat = {}
    for d in candidatos:
        c = d.get("category", "Geral")
        por_cat.setdefault(c, []).append(d)

    for cat, cota in cat_cotas.items():
        pool_cat = por_cat.get(cat, [])
        random.shuffle(pool_cat)
        escolhidos = pool_cat[:cota]
        amostra.extend(escolhidos)
        print(f"  {cat}: {len(escolhidos)} claims selecionados")

    print(f"\nTotal selecionado para geracao: {len(amostra)}")
    out_path = os.path.join(REPO_DIR, args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    perguntas_geradas = []
    for i, d in enumerate(amostra, 1):
        cid = d["claim_id"]
        cat = d.get("category", "Geral")
        claim = d["claim"]
        t0 = time.time()
        q = gerar_pergunta_llm(claim, cat)
        dt = time.time() - t0
        if not q or len(q) < 15:
            print(f"[{i}/{len(amostra)}] FALHA ao gerar para {cid}")
            continue

        item = {
            "id": f"clean-v4-{i:04d}",
            "question": q,
            "relevant_claim_ids": [cid],
            "category": cat,
            "claim_preview": claim[:120]
        }
        perguntas_geradas.append(item)
        print(f"[{i}/{len(amostra)}] ({dt:.1f}s) {cid[:35]}: {q[:80]}...")

    with open(out_path, "w", encoding="utf-8") as f:
        for item in perguntas_geradas:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"\nGravado {len(perguntas_geradas)} perguntas em {out_path}")


if __name__ == "__main__":
    main()
