#!/usr/bin/env python3
# ATENCAO (2026-09-11): este benchmark e TAUTOLOGICO para medicao de retrieval.
# As perguntas contem o codigo literal e o harness da +15.0 de boost para match exato de codigo,
# logo Hit@1=100% mede lookup de codigo, NAO compreensao. Usar golden_qa_virgin_benchmark.jsonl
# (perguntas sem codigo) para medir retrieval real: la o Hit@1 e 0/24 e a mediana da posicao da
# mensagem correta e 837.
"""Gera um benchmark focado em MENSAGENS para medir o ganho do catalogo completo.

Perguntas naturais sobre codigos de mensagem; a resposta esperada e a claim do catalogo
(`hwa-msgcat-<codigo>`). Inclui deliberadamente as familias que NAO existiam na
documentacao publica (DEG, DEO, DAB, SAS, DFD...) — e onde o ganho deve aparecer.

Saida: data/eval/golden_qa_messages_benchmark.jsonl
"""
import json, random, os

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
CAT = f"{BASE}/data/evidence/official-verification-2026-09-11-message-catalog-full.jsonl"
OUT = f"{BASE}/data/eval/golden_qa_messages_benchmark.jsonl"

# familias que NAO existiam na doc publica (o ganho real do catalogo do produto)
NOVAS = ["DEG", "DEO", "DAB", "SAS", "DFD", "DCJ", "DEQ", "DBY", "DEP", "DEL", "DEH", "DES", "DAH"]
# familias classicas (baseline: ja estavam documentadas)
CLASSICAS = ["BHU", "BIA", "BIS", "BCT", "FAB", "JPL", "BHT"]

TEMPLATES = [
    "O que significa a mensagem {code} no HCL Workload Automation 10.2.8?",
    "Qual o texto exato da mensagem {code}?",
    "Como interpretar a mensagem {code} do HWA?",
]


def main():
    msgs = [json.loads(l) for l in open(CAT, encoding="utf-8") if l.strip()]
    byfam = {}
    for m in msgs:
        byfam.setdefault(m["claim_id"].split("-")[-1][3:6].upper(), []).append(m)

    random.seed(20260911)  # reprodutibilidade
    picked = []
    for fam in NOVAS:
        pool = byfam.get(fam, [])
        if pool:
            picked.extend(random.sample(pool, min(3, len(pool))))
    for fam in CLASSICAS:
        pool = byfam.get(fam, [])
        if pool:
            picked.extend(random.sample(pool, min(2, len(pool))))

    seen, rows = set(), []
    for i, m in enumerate(picked, 1):
        cid = m["claim_id"]
        if cid in seen:
            continue
        seen.add(cid)
        code = cid.split("-")[-1].upper()
        fam = code[3:6]
        tmpl = TEMPLATES[i % len(TEMPLATES)]
        rows.append({
            "id": f"msg-{code.lower()}",
            "domain": f"mensagens/{fam}",
            "question": tmpl.format(code=code),
            "expected_answer": m["supporting_quote"],
            "relevant_claim_ids": [cid],
            "runbook_ref": None,
        })

    with open(OUT, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"geradas {len(rows)} perguntas -> {OUT}")
    print("por familia:", json.dumps(
        {k: sum(1 for r in rows if f"/{k}" in r['domain']) for k in NOVAS + CLASSICAS}))


if __name__ == "__main__":
    main()
