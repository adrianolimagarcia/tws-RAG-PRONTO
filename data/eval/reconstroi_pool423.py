"""Reconstroi EXATAMENTE o pool de 423 a partir de lex_summary.json.

O pool original vivia em /tmp/ragexp/attrib3/pool.jsonl (volatil) e foi perdido. Ele e'
reconstruivel porque o summary do harness guarda o `id` e o texto da `question` de cada uma
das 423 entradas, e todos os 423 ids existem nos benchmarks do repo.

O summary de origem FICA NO REPO (`data/evidence/pool423-lex-summary-2026-09-21.json`) de
proposito: era a UNICA copia da composicao do pool e vivia em /tmp - foi assim que o pool
se perdeu da primeira vez. Aqui cada entrada e'
casada por (id, question) contra as fontes e re-emitida com os campos completos.

Verificacao obrigatoria depois: rodar o harness neste arquivo tem de dar
230 @1 / 287 @5 / MRR 0,6016. Se nao der, a reconstrucao esta' ERRADA e nao serve.
"""
import glob
import json
import os
import sys

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
RESUMO = (sys.argv[1] if len(sys.argv) > 1
          else os.path.join(REPO, "data/evidence/pool423-lex-summary-2026-09-21.json"))
SAIDA = sys.argv[2] if len(sys.argv) > 2 else "/tmp/ragexp/pool_recon.jsonl"

d = json.load(open(RESUMO, encoding="utf-8"))
alvo = d["details"]

fontes = {}
ordem_arq = sorted(glob.glob(os.path.join(REPO, "data/eval/decontaminated/*.jsonl"))) + [
    os.path.join(REPO, "data/eval/golden_qa_virgin_messages_expanded.jsonl")]
for f in ordem_arq:
    for l in open(f, encoding="utf-8"):
        if not l.strip():
            continue
        o = json.loads(l)
        fontes.setdefault((o.get("id"), o.get("question")), o)

faltam, saida = [], []
for x in alvo:
    o = fontes.get((x.get("id"), x.get("question")))
    if o is None:
        faltam.append(x.get("id"))
    else:
        saida.append(o)

if faltam:
    print("!! %d entradas sem fonte: %s" % (len(faltam), faltam[:10]))
    sys.exit(1)

with open(SAIDA, "w", encoding="utf-8") as fh:
    for o in saida:
        fh.write(json.dumps(o, ensure_ascii=False) + "\n")

print("reconstruido: %d entradas -> %s" % (len(saida), SAIDA))
