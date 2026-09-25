#!/usr/bin/env python3
"""Classificacao REST: escolher 1 de 276 operacoes para uma pergunta em PT.

Pergunta que este script responde: o REST e' problema de RECUPERACAO ou de
CLASSIFICACAO? A recuperacao ja' foi medida (denso puro 25,0% @1 no rest_ops_40 com
rerank top_n=15). Aqui mede-se a classificacao no MESMO benchmark e no MESMO ground
truth, para comparar maca com maca.

Espaco de rotulos: 276 operacoes (o conjunto e' FECHADO e enumerado - e' isso que
justifica tratar como classificacao em vez de busca).

Uso:
    python scripts/classify_rest_ops_276.py --limit 5      # piloto
    python scripts/classify_rest_ops_276.py                # os 40

A chave da API e' lida do ambiente (A6API_KEY) ou, na falta, do config do HAOS. Ela
NUNCA e' impressa, nem em caso de erro.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENCH = os.path.join(REPO, "data", "eval", "rest_api_benchmark_ops_40.jsonl")
OPS = os.path.join(REPO, "data", "knowledge", "rest-api-derived-ops.jsonl")



def _modulo():
    """O classificador mora em mcp_server/tws_rest_classifier.py - fonte UNICA.

    Antes havia duas copias do prompt (aqui e no MCP), que podem divergir. Este script
    agora mede exatamente o que a producao executa.
    """
    import importlib.util
    caminho = os.path.join(REPO, "mcp_server", "tws_rest_classifier.py")
    spec = importlib.util.spec_from_file_location("tws_rest_classifier", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="0 = todos")
    ap.add_argument("--out", default="/tmp/rest_cls.json")
    args = ap.parse_args()

    bench = [json.loads(l) for l in open(BENCH, encoding="utf-8") if l.strip()]
    ops = [json.loads(l) for l in open(OPS, encoding="utf-8") if l.strip()]
    if args.limit:
        bench = bench[: args.limit]

    mod = _modulo()
    cat = mod.catalogo(ops)
    if not mod.disponivel():
        sys.exit("sem chave para o classificador (A6API_KEY ou a variavel do config do HAOS)")
    print(f"modelo={mod.MODELO}  operacoes={len(ops)}  perguntas={len(bench)}", file=sys.stderr)
    print(f"catalogo ~{len(cat)//4} tokens", file=sys.stderr)

    # espaco de rotulos: o MESMO conjunto de 276 operacoes para todas as perguntas
    idx_por_claim = {o["claim_id"]: i + 1 for i, o in enumerate(ops)}
    resultados, acertos, erros = [], 0, 0
    for n, b in enumerate(bench, 1):
        alvo = idx_por_claim.get(b["relevant_claim_ids"][0])
        txt, err = mod.chama(cat, b["question"])
        num = mod.extrai_numero(txt) if txt else None
        ok = (num == alvo)
        acertos += ok
        if err:
            erros += 1
        resultados.append({
            "id": b["id"], "family": b["family"], "question": b["question"],
            "alvo_claim": b["relevant_claim_ids"][0], "alvo_num": alvo,
            "escolhido_num": num,
            "escolhido_op": ops[num - 1]["operation"] if num and 1 <= num <= len(ops) else None,
            "acertou": ok, "erro_api": err or None,
            "resposta_bruta": (txt or "")[:300],
        })
        print(f"  [{n}/{len(bench)}] {'OK ' if ok else 'err'} alvo={alvo} escolhido={num}"
              f"{' api='+err if err else ''}", file=sys.stderr)

    acu = acertos / len(bench) if bench else 0.0
    # sem as perguntas que contem o nome da familia na propria pergunta (vazamento)
    limpo = [r for r in resultados if r["family"].lower() not in r["question"].lower()]
    acu_limpo = (sum(r["acertou"] for r in limpo) / len(limpo)) if limpo else 0.0
    res = {"modelo": mod.MODELO, "n_ops": len(ops), "n_perguntas": len(bench),
           "acuracia_top1": acu, "acertos": acertos,
           "n_vazamento_rotulo": len(resultados) - len(limpo),
           "acuracia_top1_sem_vazamento": acu_limpo, "n_sem_vazamento": len(limpo),
           "erros_api": erros, "resultados": resultados}
    json.dump(res, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"ACURACIA @1: {acertos}/{len(bench)} = {acu:.4f}")
    print(f"sem vazamento de rotulo ({len(limpo)} perguntas): {acu_limpo:.4f}")
    print(f"erros de API: {erros}")
    print(f"gravado {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
