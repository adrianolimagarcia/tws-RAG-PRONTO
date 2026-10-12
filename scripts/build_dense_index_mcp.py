#!/usr/bin/env python3
"""Constroi o indice denso (BGE-M3) do corpus de PRODUCAO.

Le o corpus que o MCP realmente serve (data/export/tws_corpus_master_consolidated.jsonl),
sem tocar no `load_documents()` do laboratorio - que carrega um corpus DIFERENTE (fonts
proprias, inclusive man pages que nao entram na producao). Usar o corpus do lab aqui seria
construir o indice de outro conjunto.

O texto indexado e' EXATAMENTE o que o BM25 indexa: `claim` + `context_prefix` +
`synthetic_questions` (ver a linha do `text = f"..."` em mcp_server/tws_expert_mcp.py). Sem
essa simetria, denso e esparso estariam olhando documentos diferentes.

Uso:
    python3 scripts/build_dense_index_mcp.py
    python3 -c "import sys; sys.path.insert(0,'mcp_server'); import tws_dense,json; \
        print(tws_dense.busca('como consultar o calendario pela REST API V2', 5))"
"""
import json
import os
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.environ.get(
    "TWS_CORPUS_FILE",
    os.path.join(RAIZ, "data", "export", "tws_corpus_master_consolidated.jsonl"))

sys.path.insert(0, os.path.join(RAIZ, "mcp_server"))


def main():
    if not os.path.exists(CORPUS):
        raise SystemExit("corpus nao encontrado: %s" % CORPUS)

    docs = []
    for linha in open(CORPUS, encoding="utf-8"):
        if not linha.strip():
            continue
        o = json.loads(linha)
        cid = o.get("claim_id")
        if not cid:
            continue
        # Mesma montagem de texto do MCP - o denso e o esparso tem de olhar o mesmo doc.
        texto = "%s %s %s" % (
            o.get("claim", ""),
            o.get("context_prefix", ""),
            " ".join(o.get("synthetic_questions", []) or []),
        )
        docs.append((cid, texto))

    print("[idx] corpus: %d docs (%s)" % (len(docs), os.path.basename(CORPUS)))
    t0 = time.time()
    import tws_dense
    forma = tws_dense.constroi(docs)
    print("[idx] matriz: %s em %.1fs" % (forma, time.time() - t0))
    print("[idx] gravado: %s" % tws_dense.INDICE_PADRAO)
    print("[idx] gravado: %s" % tws_dense.META_PADRAO)


if __name__ == "__main__":
    main()
