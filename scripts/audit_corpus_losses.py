#!/usr/bin/env python3
"""audit_corpus_losses.py — quanto conteudo o INGEST descarta silenciosamente.

POR QUE EXISTE
--------------
`rag_core/corpus.py` tem varios pontos de descarte que engolem conteudo com
`except: pass` ou `continue`. Cada um foi escrito por um motivo (ha' comentarios
explicando), mas nenhum era QUANTIFICADO. Sem numero, "a ingestao esta' completa"
e' uma suposicao - e foi por suposicao que a §8 do relatorio de 2026-09-19 quase
atribuiu a queda de @1 ao vazamento de evidencia, quando a causa era selecao de
pergunta.

Este script responde, por fonte: quantas linhas entraram, quantas foram
descartadas, POR QUE, e quantos caracteres de conteudo real foram junto.

Nao altera nada. Somente le.

Uso: python3 scripts/audit_corpus_losses.py
"""
from __future__ import annotations

import collections
import glob
import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from rag_core import config  # noqa: E402
from rag_core.corpus import load_documents  # noqa: E402

# Campos que o texto indexado de fato usa, por tipo de fonte. Qualquer campo fora
# desta lista e' conteudo que existe no dado e NAO entra no indice.
CAMPOS_USADOS = {
    "lab_evidence": ("claim", "result", "observations", "sanitized_output"),
    "aws_message": ("code", "component", "message", "claim"),
    "optman_option": ("name", "alias", "value", "claim"),
    "message_catalog": ("claim", "supporting_quote", "context_prefix"),
}


def conteudo_de(o, campos):
    return " ".join(str(o.get(k) or "") for k in campos)


def audit_lab():
    """Os arquivos lab-validation-*: o maior ponto de descarte."""
    linhas = emitidos = sem_cid = sem_claim = 0
    chars_perdidos = 0
    perdidos = []
    campos_ignorados = collections.Counter()
    for lf in sorted(glob.glob(os.path.join(REPO, "data", "evidence", "lab-validation-*.jsonl"))):
        try:
            f = open(lf, encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line in f:
            if not line.strip():
                continue
            linhas += 1
            try:
                c = json.loads(line)
            except Exception:
                sem_cid += 1
                continue
            cid = c.get("claim_id", "")
            if not cid:
                sem_cid += 1
                continue
            if not (c.get("claim") or "").strip():
                sem_claim += 1
                # o record e' descartado, mas outros campos tem conteudo real
                c2 = conteudo_de(c, ("command", "observations", "sanitized_output",
                                     "preconditions", "stop_criterion"))
                chars_perdidos += len(c2)
                perdidos.append((cid, len(c2)))
                for k in ("command", "preconditions", "stop_criterion", "reversibility",
                          "evidence_url", "performed_at", "performed_by", "risk"):
                    if str(c.get(k) or "").strip():
                        campos_ignorados[k] += 1
                continue
            emitidos += 1
            # campos preenchidos mas NAO indexados (mesmo nos admitidos)
            for k in ("command", "preconditions", "stop_criterion", "reversibility",
                      "evidence_url", "performed_at", "performed_by", "risk", "platform"):
                if str(c.get(k) or "").strip():
                    campos_ignorados[k] += 1
        f.close()
    return {
        "linhas": linhas, "emitidos": emitidos,
        "descartado_sem_claim": sem_claim, "descartado_sem_cid": sem_cid,
        "chars_perdidos": chars_perdidos,
        "campos_ignorados": dict(campos_ignorados),
        "exemplos": perdidos[:5],
    }


def audit_jsonl_source(path, rotulo):
    """Fontes simples: quantas linhas, quantas sem claim_id, quantas malformadas."""
    if not os.path.exists(path):
        return None
    linhas = sem_cid = mal = emitidos = 0
    for line in open(path, encoding="utf-8", errors="replace"):
        if not line.strip():
            continue
        linhas += 1
        try:
            c = json.loads(line)
        except Exception:
            mal += 1
            continue
        if not c.get("claim_id"):
            sem_cid += 1
            continue
        emitidos += 1
    return {"fonte": rotulo, "linhas": linhas, "emitidos": emitidos,
            "sem_claim_id": sem_cid, "malformadas": mal}


def audit_runbooks():
    """Runbooks: o parse pode falhar e o `except: pass` esconde o arquivo inteiro."""
    from scripts.ragflow_chunker import parse_markdown_ragflow
    rbs = sorted(glob.glob(os.path.join(config.RUNBOOKS_DIR, "*.md")))
    ok = falhou = chunks = 0
    falhas = []
    for rb in rbs:
        try:
            ch = parse_markdown_ragflow(rb)
            if ch:
                ok += 1
                chunks += len(ch)
            else:
                falhou += 1
                falhas.append((os.path.basename(rb), "0 chunks"))
        except Exception as e:
            falhou += 1
            falhas.append((os.path.basename(rb), type(e).__name__))
    return {"arquivos": len(rbs), "ok": ok, "falhou": falhou,
            "chunks": chunks, "falhas": falhas[:8]}


def main() -> int:
    docs = load_documents()
    por_id = {d["id"] for d in docs}
    tipos = collections.Counter(d.get("type") for d in docs)
    print("=" * 78)
    print("AUDITORIA DE PERDAS DO INGEST")
    print("=" * 78)
    print(f"corpus resultante: {len(docs)} docs")
    print("  " + ", ".join(f"{t}={n}" for t, n in tipos.most_common()))
    print(f"LAB_FILES ativos: {len(config.LAB_FILES)} arquivos")

    print()
    print("--- 1. lab-validation-* (maior ponto de descarte) ---")
    lab = audit_lab()
    print(f"  linhas lidas:                     {lab['linhas']}")
    print(f"  emitidas como doc:                {lab['emitidos']}")
    print(f"  DESCARTADAS sem campo 'claim':    {lab['descartado_sem_claim']}")
    print(f"  descartadas sem claim_id/malform: {lab['descartado_sem_cid']}")
    print(f"  CONTEUDO PERDIDO:                 {lab['chars_perdidos']} chars "
          f"({lab['chars_perdidos']/1024:.1f} KB)")
    print(f"  campos preenchidos e NAO indexados (contagem de records):")
    for k, n in sorted(lab["campos_ignorados"].items(), key=lambda x: -x[1]):
        print(f"     {k:<18} {n}")
    if lab["exemplos"]:
        print(f"  exemplos de records descartados (id, chars de conteudo):")
        for cid, n in lab["exemplos"]:
            print(f"     {cid[:60]:<60} {n}")

    print()
    print("--- 2. outras fontes (id ausente = descarte silencioso) ---")
    for path, rot in ((config.AWS_MSGS_FILE, "aws_message"),
                      (config.OPTMAN_FILE, "optman_option"),
                      (config.MSGCAT_FILE, "message_catalog")):
        r = audit_jsonl_source(path, rot)
        if r:
            print(f"  {r['fonte']:<18} linhas {r['linhas']:>5} | emitidos {r['emitidos']:>5} "
                  f"| sem claim_id {r['sem_claim_id']:>4} | malformadas {r['malformadas']:>4}")

    print()
    print("--- 3. runbooks (parse com except: pass) ---")
    rb = audit_runbooks()
    print(f"  arquivos: {rb['arquivos']} | parse ok: {rb['ok']} | falhou/vazio: {rb['falhou']} "
          f"| chunks: {rb['chunks']}")
    for nome, err in rb["falhas"]:
        print(f"     FALHA: {nome} ({err})")

    print()
    print("--- 4. ids referenciados pelo benchmark que NAO existem no corpus ---")
    pool = {}
    dec = os.path.join(REPO, "data", "eval", "decontaminated")
    if os.path.isdir(dec):
        for name in sorted(os.listdir(dec)):
            if not name.endswith(".jsonl") or "negatives" in name:
                continue
            for line in open(os.path.join(dec, name), encoding="utf-8"):
                if not line.strip():
                    continue
                r = json.loads(line)
                q = r.get("question", "").strip().lower()
                if q and q not in pool:
                    pool[q] = r
    refs = collections.Counter()
    orfas = set()
    for r in pool.values():
        cs = set(r.get("relevant_claim_ids", []) or [])
        if not (cs & por_id):
            orfas |= cs
        for c in cs:
            refs[c] += 1
    print(f"  perguntas distintas: {len(pool)}")
    print(f"  perguntas SEM nenhuma evidencia no corpus: "
          f"{sum(1 for r in pool.values() if not (set(r.get('relevant_claim_ids', []) or []) & por_id))}")
    print(f"  claim_ids distintos referenciados: {len(refs)}")
    print(f"  desses, AUSENTES do corpus: {sum(1 for c in refs if c not in por_id)}")
    print(f"  ids orfaos (so' aparecem em pergunta sem resposta): {len(orfas)}")

    print()
    print("VEREDITO: os descartes sao VOLUNTARIOS e o merge de ids e' ADITIVO (nunca")
    print("sobrescreve texto). O risco nao e' corrupcao - e' PERDA SILENCIOSA: conteudo")
    print("que existe no dado e nao entra no indice, sem aparecer em nenhum relatorio.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
