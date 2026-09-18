#!/usr/bin/env python3
"""Medicao do ROTEAMENTO familia -> recuperacao no benchmark REST (40 perguntas).

PERGUNTA: se o LLM identifica a familia de recurso (medido: 94,4% honesto), isso se
CONVERTE em recuperacao melhor?

O QUE ESTA MEDICAO MOSTRA, E O QUE ELA NAO PODE MOSTRAR
------------------------------------------------------
O corpus derivado da REST tem 24 familias e 24 registros - EXATAMENTE UM REGISTRO POR
FAMILIA (verificado por este script). Portanto "rotear para a familia prevista" e'
aritmeticamente IDENTICO a acertar a classificacao: nao existe o que escolher dentro
da familia. O roteamento aqui e' um RELABELING, nao um ganho de recuperacao, e reportar
"recuperacao de 94,4%" seria enganoso.

Pior: o ground truth do benchmark e' a FAMILIA. Com um registro por familia o benchmark
SATURA na acuracia do classificador e NAO CONSEGUE distinguir "achou a familia" de
"achou o registro". Medir roteamento de verdade exigiria ground truth por OPERACAO -
que este benchmark nao tem.

O QUE A MEDICAO ENTREGA SEM ENGANAR
-----------------------------------
1. O TETO do roteamento (= acuracia do classificador) e o MODO DE FALHA dele: quando a
   classificacao erra, o roteamento devolve o registro ERRADO - falha total, sem
   fallback, ao contrario da recuperacao plana.
2. O CONTROLE QUE SEPARA AS DUAS CAUSAS da falha da recuperacao plana: corpus
   competitivo (6876 documentos que nao sao o alvo) ou ranking ruim. Para isso mede a
   recuperacao PLANA num corpus LIMPO (so' os 24 registros). Se no corpus limpo ela
   acerta quase tudo, entao a causa e' COMPETICAO DE CORPUS, nao ranking - e o
   roteamento "funciona" porque LIMPA O CORPUS, nao porque roteia.
3. O CUSTO: o roteamento gasta chamadas de API pagas; a recuperacao plana nao gasta
   nada.

USO
    python3 scripts/measure_routing_family_to_retrieval.py \
        --predictions data/eval/rest_api_zeroshot_variantB.jsonl \
        --rank-bm25 /tmp/rank_bm25.json --rank-hybrid /tmp/rank_hybrid.json
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import sys
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AVALIADOR = os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py")
BENCH = os.path.join(REPO, "data", "eval", "rest_api_benchmark_40.jsonl")
DERIVADOS = os.path.join(REPO, "data", "knowledge", "rest-api-derived.jsonl")


def sem_acento(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s).lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def carregar_avaliador():
    spec = importlib.util.spec_from_file_location("ev", AVALIADOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--predictions", default=os.path.join(
        REPO, "data", "eval", "rest_api_zeroshot_variantB.jsonl"))
    ap.add_argument("--rank-bm25", default="/tmp/rank_bm25.json")
    ap.add_argument("--rank-hybrid", default="/tmp/rank_hybrid.json")
    args = ap.parse_args()

    bench = [json.loads(l) for l in open(BENCH, encoding="utf-8")]
    preds = {p["id"]: p for p in (json.loads(l) for l in open(args.predictions, encoding="utf-8"))}
    derivados = [json.loads(l) for l in open(DERIVADOS, encoding="utf-8")]

    # ---- o vazamento de rotulo ja' conhecido: 4 perguntas contem o nome da familia ----
    vazadas = {b["id"] for b in bench if sem_acento(b["family"]) in sem_acento(b["question"])}

    print("=" * 78)
    print("1. FORMA DO CORPUS - decide se 'roteamento' significa alguma coisa")
    print("=" * 78)
    por_fam: dict[str, int] = {}
    for d in derivados:
        por_fam[d.get("resource")] = por_fam.get(d.get("resource"), 0) + 1
    print(f"  registros derivados da REST : {len(derivados)}")
    print(f"  familias distintas          : {len(por_fam)}")
    print(f"  registros por familia       : min={min(por_fam.values())} max={max(por_fam.values())}")
    multiplas = [k for k, v in por_fam.items() if v > 1]
    print(f"  familias com mais de 1      : {multiplas if multiplas else 'NENHUMA'}")
    if not multiplas:
        print("  => 1 registro por familia. ROTEAR PARA A FAMILIA NAO ESCOLHE NADA:")
        print("     e' aritmeticamente identico a acertar a classificacao.")

    print()
    print("=" * 78)
    print("2. ROTEAMENTO: teto e modo de falha")
    print("=" * 78)
    acertos = [b for b in bench if preds.get(b["id"], {}).get("acerto")]
    erros = [b for b in bench if not preds.get(b["id"], {}).get("acerto")]
    print(f"  roteamento @1 (todos)        : {len(acertos)}/{len(bench)} "
          f"({100 * len(acertos) / len(bench):.1f}%)")
    limpos = [b for b in bench if b["id"] not in vazadas]
    al = sum(1 for b in limpos if preds.get(b["id"], {}).get("acerto"))
    print(f"  roteamento @1 (sem as {len(vazadas)} vazadas): {al}/{len(limpos)} "
          f"({100 * al / len(limpos):.1f}%)")
    print("  modo de falha: quando a classificacao erra, o roteamento devolve o registro")
    print("  ERRADO - falha TOTAL, sem fallback. A recuperacao plana ao menos tenta.")
    for b in erros:
        p = preds[b["id"]]
        print(f"    {b['id']}  GT={b['family']:22s} roteado para={str(p['predito']):22s}")

    print()
    print("=" * 78)
    print("3. CONTROLE: a falha da recuperacao plana e' corpus ou ranking?")
    print("=" * 78)
    ev = carregar_avaliador()
    orig = ev.load_documents
    resumo = os.path.join(REPO, "data", "eval", "eval_summary.json")
    backup = resumo + ".preservado"
    tinha = os.path.exists(resumo)
    if tinha:
        shutil.copy2(resumo, backup)

    # O corpus marca os registros derivados da REST com type='rest_api_surface'. Filtrar
    # por TIPO e' mais robusto que por id: os registros derivados no arquivo nao tem campo
    # `id` (tem `claim_id`), e o id final e' atribuido pelo loader.
    def so_rest():
        return [d for d in orig() if d.get("type") == "rest_api_surface"]

    def medir(carregador):
        """Mede um cenario. rank=None e' estado proprio, NAO vira zero.

        run_evaluation() NAO retorna as metricas - so' grava eval_summary.json -, entao
        ler o arquivo recem-gravado e' o unico caminho. O stdout dele tambem e' usado,
        por isso o resultado nao pode ser despejado la'.
        """
        ev.load_documents = carregador
        try:
            ev.run_evaluation()
            with open(resumo, encoding="utf-8") as f:
                m = json.load(f)
        finally:
            ev.load_documents = orig
        ranks = [d.get("rank") for d in (m.get("details") or [])]
        tot = len(ranks)
        return {
            "total": tot,
            "hit@1": sum(1 for r in ranks if r is not None and r <= 1),
            "hit@10": sum(1 for r in ranks if r is not None and r <= 10),
            "nunca": sum(1 for r in ranks if r is None),
        }

    # RAG_HYBRID e' lido no IMPORT do avaliador: nao da' para alternar aqui dentro.
    # Este script mede o retriever do PROCESSO (env), e o chamador roda duas vezes.
    retriever = "hibrido" if os.environ.get("RAG_HYBRID") == "1" else "BM25"
    os.environ["RAG_INGEST_REST_API"] = "1"
    os.environ["RAG_BENCHMARK_FILE"] = BENCH
    resultados = {}
    try:
        for cenario, carregador in (("corpus completo", orig), ("corpus LIMPO (24 registros)", so_rest)):
            resultados[cenario] = medir(carregador)
    finally:
        if tinha:
            shutil.move(backup, resumo)

    print(f"  retriever: {retriever}")
    print(f"  {'cenario':30s} {'total':>6s} {'@1':>5s} {'@10':>5s} {'nunca':>6s}")
    for cenario, r in resultados.items():
        print(f"  {cenario:30s} {r['total']:6d} {r['hit@1']:5d} {r['hit@10']:5d} {r['nunca']:6d}")
    a = resultados["corpus completo"]["hit@1"]
    b_ = resultados["corpus LIMPO (24 registros)"]["hit@1"]
    print(f"  LEITURA: no corpus LIMPO o @1 vai a {b_}/40 contra {a}/40 no completo.")
    print("  Se no LIMPO a recuperacao quase acerta tudo, a causa da falha e' COMPETICAO DE")
    print("  CORPUS - e o roteamento 'funciona' porque limpa o corpus, nao porque roteia.")

    print()
    print("=" * 78)
    print("4. LIMITE DECLARADO DESTA MEDICAO")
    print("=" * 78)
    print("  O ground truth do benchmark e' a FAMILIA. Com 1 registro por familia o")
    print("  benchmark SATURA na acuracia do classificador e NAO distingue 'achou a")
    print("  familia' de 'achou o registro'. Medir roteamento de verdade exigiria ground")
    print("  truth por OPERACAO - que este benchmark nao tem. Portanto o numero da secao 2")
    print("  NAO deve ser lido como ganho de recuperacao.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
