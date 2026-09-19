"""Montagem do corpus do nucleo RAG (rag_core).

`load_documents()` foi EXTRAIDO VERBATIM de `data/eval/evaluate_rag_benchmark.py`
(fatia de refatoracao pura: mesmo comportamento). Ele monta a lista de documentos
indexaveis a partir das fontes do repo (claims canonicas, dicionario de mensagens
AWS, catalogo optman, evidencias de lab, catalogo de mensagens, chunks RAGFlow dos
runbooks e as fontes derivadas sob switch).

Os switches de MEDICAO (todos opt-in, default OFF) vivem em `rag_core.config` e
sao lidos no IMPORT - logo o corpus e' fixo por processo.
"""
import glob
import json
import os
import sys

from . import config
from .config import (
    AWS_MSGS_FILE,
    CLAIMS_FILE,
    KNOWLEDGE_DERIVED,
    KNOWLEDGE_REST_API,
    LAB_FILES,
    MSGCAT_FILE,
    OPTMAN_FILE,
    REPO_DIR,
    RUNBOOKS_DIR,
)
from .lexical import tokenize

# Garante que `scripts.ragflow_chunker` seja importavel quando o pacote e' usado
# fora do entrypoint do avaliador (que ja' faz o mesmo insert de sys.path).
if REPO_DIR not in sys.path:
    sys.path.insert(0, REPO_DIR)

from scripts.ragflow_chunker import parse_markdown_ragflow


def load_documents():
    docs = []

    # 1. Claims canonicas
    if os.path.exists(CLAIMS_FILE):
        for line in open(CLAIMS_FILE):
            if line.strip():
                c = json.loads(line)
                cid = c.get("claim_id", "")
                # Enriquecer texto indexado: context_prefix (Anthropic) + claim + notes + topico + citação oficial + terminologia normalizada + perguntas sintéticas
                nt = c.get("normalized_terminology") or {}
                nt_str = " ".join(str(v) for v in nt.values()) if isinstance(nt, dict) else str(nt)
                sq = c.get("supporting_quote") or ""
                synth_q = " ".join(c.get("synthetic_questions", []))
                ctx_pref = c.get("context_prefix", "")
                # --- Ablacoes de MEDICAO (default OFF -> comportamento inalterado) ---
                # RAG_DROP_SYNTHETIC=1: remove as perguntas sinteticas do texto indexado
                #   (mede quanto do hit depende de a pergunta estar embutida no proprio doc).
                # RAG_DROP_CTXPREFIX=1: remove o context_prefix repetido (boilerplate) do texto indexado
                #   (mede quanto do IDF e consumido por prefixo comum a muitos docs).
                if os.environ.get("RAG_DROP_SYNTHETIC") == "1":
                    synth_q = ""
                if os.environ.get("RAG_DROP_CTXPREFIX") == "1":
                    ctx_pref = ""
                text = f"{ctx_pref} {c.get('claim', '')} {c.get('notes', '')} {c.get('topic', '')} {c.get('subtopic', '')} {sq} {nt_str} {synth_q}"
                docs.append({"id": cid, "type": "canonical_claim", "text": text, "tokens": tokenize(text)})

    # 2. Dicionario de Mensagens AWS*
    if os.path.exists(AWS_MSGS_FILE):
        for line in open(AWS_MSGS_FILE):
            if line.strip():
                c = json.loads(line)
                cid = c.get("claim_id", "")
                text = f"{c.get('code', '')} {c.get('component', '')} {c.get('message', '')} {c.get('claim', '')}"
                docs.append({"id": cid, "type": "aws_message", "code": c.get("code"), "text": text, "tokens": tokenize(text)})

    # 3. Catalogo Optman
    if os.path.exists(OPTMAN_FILE):
        for line in open(OPTMAN_FILE):
            if line.strip():
                c = json.loads(line)
                cid = c.get("claim_id", "")
                text = f"{c.get('name', '')} {c.get('alias', '')} {c.get('value', '')} {c.get('claim', '')}"
                docs.append({"id": cid, "type": "optman_option", "text": text, "tokens": tokenize(text)})

    # 4. Lab validation claims
    for lf in LAB_FILES:
        for line in open(lf):
            if line.strip():
                try:
                    c = json.loads(line)
                    cid = c.get("claim_id", "")
                    # Entradas sem `claim` sao registros de EXECUCAO (result: PASS/BLOCKED),
                    # nao evidencia. Sem este filtro viram documento de texto quase vazio
                    # (' PASS ') e ainda colidem com ids de canonical_claim.
                    if cid and (c.get("claim") or "").strip():
                        text = f"{c.get('claim', '')} {c.get('result', '')} {c.get('observations', '')} {c.get('sanitized_output', '')}"
                        docs.append({"id": cid, "type": "lab_evidence", "text": text, "tokens": tokenize(text)})
                except Exception:
                    pass

    # 5. Catalogo de mensagens do produto (10.2.8) — texto canonico de TODOS os codigos
    if os.path.exists(MSGCAT_FILE):
        for line in open(MSGCAT_FILE):
            if line.strip():
                c = json.loads(line)
                cid = c.get("claim_id", "")
                if not cid:
                    continue
                _cp = "" if os.environ.get("RAG_DROP_CTXPREFIX") == "1" else c.get('context_prefix', '')
                text = f"{c.get('claim','')} {c.get('supporting_quote','')} {_cp}"
                docs.append({"id": cid, "type": "message_catalog", "text": text, "tokens": tokenize(text)})

    # 6. Chunks Estruturados RAGFlow dos Runbooks Markdown (com Breadcrumbs e Tabelas Íntegras)
    for rbf in sorted(glob.glob(os.path.join(RUNBOOKS_DIR, "*.md"))):
        fname = os.path.basename(rbf)
        try:
            rf_chunks = parse_markdown_ragflow(rbf)
            for ch in rf_chunks:
                docs.append({
                    "id": ch["id"],
                    "type": "ragflow_runbook_chunk",
                    "runbook": fname,
                    "title": ch.get("path", fname),
                    "path": ch.get("path", ""),
                    "text": ch["text"],
                    "metadata": ch.get("metadata", {}),
                    "tokens": tokenize(ch["text"])
                })
        except Exception:
            pass

    # 7. Conhecimento DERIVADO — man pages do produto (sintaxe/parafrase PT-BR) e
    #    procedimentos operacionais do lab. Fonte adicionada EXPLICITAMENTE porque o
    #    glob das outras fontes nao enxerga arquivo novo.
    #
    #    DEFAULT OFF — medido em 2026-09-15 (95 man pages + 17 procedimentos = 112 docs):
    #      com a fonte ON : corpus 7062 | 70q @1 52/70 @10 67/70 MRR 0,8105
    #                       v3  262q @1 180/262 (A 96/107 B 78/140 D 6/15), 25 pioraram, 0 melhoraram
    #      com a fonte OFF: corpus 6950 | 70q @1 53/70 @10 68/70 MRR 0,8214
    #                       v3  262q @1 183/262 (A 97/107 B 80/140 D 6/15)
    #    O custo NAO e ruido: as man pages sao vizinhas semanticas generico-autoritativas
    #    dos claims especificos do lab e ganham deles no ranking (competicao de rank).
    #    O conhecimento e correto, mas nenhum benchmark atual pergunta a sintaxe — ligar
    #    a fonte exige decisao explicita (e idealmente uma fatia de benchmark que a peca).
    if os.environ.get("RAG_INGEST_DERIVED") == "1":
        for kf in KNOWLEDGE_DERIVED:
            if not os.path.exists(kf):
                continue
            for line in open(kf, encoding="utf-8"):
                if not line.strip():
                    continue
                try:
                    c = json.loads(line)
                except Exception:
                    continue
                cid = c.get("claim_id")
                if not cid:
                    continue
                text = " ".join(
                    str(c.get(k, "")) for k in
                    ("claim", "syntax", "supporting_quote", "tool", "command", "source_title")
                )
                docs.append({"id": cid, "type": c.get("kind", "derived_knowledge"),
                             "text": text, "tokens": tokenize(text)})

    # 6b. Superficie da REST API V2 — switch PROPRIO (default OFF).
    #     Medido: a fonte entra isolada para que o efeito dela seja separavel do
    #     efeito das man pages, que ja' se mostrou negativo por competicao de rank.
    if os.environ.get("RAG_INGEST_REST_API") == "1":
        for kf in KNOWLEDGE_REST_API:
            if not os.path.exists(kf):
                continue
            for line in open(kf, encoding="utf-8"):
                if not line.strip():
                    continue
                try:
                    c = json.loads(line)
                except Exception:
                    continue
                cid = c.get("claim_id")
                if not cid:
                    continue
                # `vocab_spec` entra no texto indexado: e' o vocabulario extraido
                # mecanicamente da spec (summary/description completos, parametros,
                # schemas e campos). Ver a REGRA DECLARADA em scripts/extract_rest_api.py.
                text = " ".join(
                    str(c.get(k, "")) for k in
                    ("claim", "syntax", "resource", "supporting_quote", "source_title", "vocab_spec")
                )
                docs.append({"id": cid, "type": c.get("kind", "rest_api_surface"),
                             "text": text, "tokens": tokenize(text)})

    # Um id = um documento. Ids repetidos (canonical_claim + lab_evidence da MESMA claim)
    # sao fundidos. Sem isso, `relevant_claim_ids` do benchmark casa com qualquer copia
    # do id - inclusive uma vazia - e um acerto pode ser FALSO (metrica inflada).
    por_id = {}
    ordem = []
    fundidos = 0
    for d in docs:
        i = d["id"]
        if i not in por_id:
            por_id[i] = d
            ordem.append(i)
        else:
            base = por_id[i]
            fundidos += 1
            if d.get("text") and d["text"] not in base.get("text", ""):
                base["text"] = (base.get("text", "").rstrip() + " " + d["text"].strip()).strip()
                base["tokens"] = tokenize(base["text"])
            base.setdefault("merged_types", [base.get("type")])
            if d.get("type") not in base["merged_types"]:
                base["merged_types"].append(d.get("type"))
    if fundidos:
        docs = [por_id[i] for i in ordem]

    # Conjunto de ids que o ramo denso pode devolver (ver DENSE_MASK em config).
    if config.DENSE_MASK is not None:
        config.DENSE_MASK = {d["id"] for d in docs}

    return docs
