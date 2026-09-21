#!/usr/bin/env python3
"""Gera data/export/tws_corpus_master_with_rest.jsonl = corpus de producao + fonte REST API.

POR QUE: o corpus que a PRODUCAO consome (`tws_corpus_master_consolidated.jsonl`, gerado
em 2026-09-14) e' ANTERIOR a' fonte REST API (commit de 2026-09-18, `1de2308`). O switch
`RAG_INGEST_REST_API` so' afeta o carregador do LABORATORIO (`rag_core/corpus.py`), entao a
fonte entrou na medicao e NUNCA no artefato que a producao usa. Resultado medido: 80 das 423
perguntas do pool (as 40 `rest-*` e as 40 `ops-*`) tem alvo AUSENTE no indice de producao -
pontuam 0 por construcao, nao por falha de recuperacao.

Este script so' ACRESCENTA. Nao reescreve, nao reordena e nao toca nos registros
existentes: a comparacao entre o corpus de base e o aumentado isola a fonte REST.

Uso:
    python3 data/eval/augmenta_corpus_rest.py            # familia (24) - default, casa com o lab
    python3 data/eval/augmenta_corpus_rest.py --ops      # operacao (276)
    python3 data/eval/augmenta_corpus_rest.py --both     # uniao (300) - cobertura total

Sobre `--both`: as duas fontes tem ids DISJUNTOS (24 + 276 = 300) e os benchmarks usam as
duas (`rest-*` aponta para familia, `ops-*` para operacao). Medido: a familia sozinha cobre
os 24 alvos de familia, as operacoes sozinhas cobrem os 40 de operacao, e a UNIAO cobre
todos. O lab nao pode ligar as duas ao mesmo tempo (o switch de granularidade troca uma pela
outra), mas a producao nao tem essa restricao."""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(RAIZ, "data/export/tws_corpus_master_consolidated.jsonl")
FAMILIA = os.path.join(RAIZ, "data/knowledge/rest-api-derived.jsonl")
OPS = os.path.join(RAIZ, "data/knowledge/rest-api-derived-ops.jsonl")


def main():
    if "--both" in sys.argv:
        fontes, sufixo = [FAMILIA, OPS], "with_rest_both"
    elif "--ops" in sys.argv:
        fontes, sufixo = [OPS], "with_rest_ops"
    else:
        fontes, sufixo = [FAMILIA], "with_rest"
    destino = os.path.join(RAIZ, "data/export/tws_corpus_master_%s.jsonl" % sufixo)

    if not os.path.exists(BASE):
        raise SystemExit("corpus de base nao encontrado: %s" % BASE)
    for f in fontes:
        if not os.path.exists(f):
            raise SystemExit("fonte REST nao encontrada: %s" % f)

    base = [l for l in open(BASE, encoding="utf-8") if l.strip()]
    novos, ids_base = [], set()
    for l in base:
        try:
            ids_base.add(json.loads(l)["claim_id"])
        except Exception:
            pass

    # Mesma construcao de texto que o laboratorio usa em rag_core/corpus.py, para que o
    # documento indexado pela producao seja igual ao que o lab mediu (inclusive vocab_spec).
    for fonte in fontes:
      for l in open(fonte, encoding="utf-8"):
        if not l.strip():
            continue
        c = json.loads(l)
        cid = c.get("claim_id")
        if not cid or cid in ids_base:
            continue
        ids_base.add(cid)
        texto = " ".join(str(c.get(k, "")) for k in
                         ("claim", "syntax", "resource", "supporting_quote",
                          "source_title", "vocab_spec"))
        novos.append({
            "claim_id": cid,
            "claim": c.get("claim", ""),
            "context_prefix": c.get("source_title", ""),
            "category": "REST API V2",
            "result": "SUCCESS",
            "platform": "Distributed",
            "source_file": os.path.basename(fonte),
            "synthetic_questions": [],
            "text": texto,
        })

    with open(destino, "w", encoding="utf-8") as fh:
        for l in base:
            fh.write(l if l.endswith("\n") else l + "\n")
        for d in novos:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")

    print("base:    %5d docs  %s" % (len(base), os.path.basename(BASE)))
    print("fontes:  %5d docs  %s" % (len(novos), " + ".join(os.path.basename(f) for f in fontes)))
    print("total:   %5d docs  %s" % (len(base) + len(novos), destino))
    print("\nmedir com:")
    print("  TWS_CORPUS_FILE=%s python3 data/eval/measure_producao_pool423.py" % destino)


if __name__ == "__main__":
    main()
