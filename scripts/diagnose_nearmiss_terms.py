#!/usr/bin/env python3
"""Analise detalhada dos QUASE-ACERTOS (doc certo em rank 2-10) e teste da hipotese de IDF.

Mecanismo suspeito (lido no scorer): `compute_bm25` NAO tem fator IDF - o termo contribui so com
saturacao de TF:

    score += boost * ((k1 + 1) / (1 + k1 * (1 - b + b * (dl / avg_dl))))

Logo um termo presente em TODOS os documentos pesa igual a um termo presente em UM. Em claims
quase-duplicadas (que compartilham quase todos os termos), o termo que DISCRIMINA nao recebe peso
nenhum - e o desempate vira comprimento de documento.

O que este script mede, para decidir se IDF e' a alavanca:
  (1) df (document frequency) real dos termos que o doc CERTO casa e o rank-1 ERRADO nao casa,
      e vice-versa. Se os termos do lado certo sao RAROS e os do lado errado sao COMUNS, IDF separa.
  (2) avg_dl REAL do corpus, contra o avg_dl=60 hardcoded.
  (3) o que decide hoje: correlacao entre ganhar o rank-1 e comprimento do documento / boost de tipo.

READ-ONLY: nao altera nada. Apenas mede e grava o diagnostico.
"""
import sys, os, json, math, argparse, time
from collections import defaultdict, Counter

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E  # noqa: E402

OUT = os.path.join(REPO, "data/eval/nearmiss_diagnosis.json")


def match_rank(ranked, exp, exp_rb, qt):
    for i, d in enumerate(ranked):
        if d["id"] in exp:
            return i + 1
        if d["type"] == "aws_message":
            if any(d.get("code", "").lower() in c.lower() for c in exp):
                return i + 1
        elif d["type"] in ("ragflow_runbook_chunk", "runbook_section") and exp_rb \
                and d.get("runbook") == exp_rb:
            ov = len(qt.intersection(d["tokens"]))
            if ov >= 2 and (ov / max(1, len(qt))) >= 0.25:
                return i + 1
    return None


def main():
    docs = E.load_documents()
    n_docs = len(docs)
    print(f"[nm] n_docs = {n_docs}")

    # --- (2) estatisticas de comprimento ---
    dls = [len(d["tokens"]) for d in docs]
    avg_dl = sum(dls) / len(dls)
    print(f"[nm] avg_dl REAL = {avg_dl:.2f}  (mediana {sorted(dls)[len(dls)//2]}, "
          f"min {min(dls)}, max {max(dls)}) | HARDCODED no scorer = 60")

    # --- (1) document frequency de todo termo do corpus ---
    t0 = time.time()
    df = Counter()
    for d in docs:
        for t in set(d["tokens"]):
            df[t] += 1
    print(f"[nm] vocabulario = {len(df)} termos ({time.time()-t0:.1f}s)")

    bench = [json.loads(l) for l in open(os.path.join(REPO, "data/eval/blind_v3_slices.jsonl")) if l.strip()]
    cases = []
    for b in bench:
        q = b["question"]; exp = set(b.get("relevant_claim_ids", [])); rb = b.get("runbook_ref")
        qt = E.tokenize(q)
        scored = []
        for d in docs:
            s = E.compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
            if s > 0:
                scored.append([s, d])
        scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        div = []
        seen = defaultdict(int)
        for s, d in scored:
            kk = d.get("runbook") or d.get("type")
            if d.get("type") == "ragflow_runbook_chunk" and seen[kk] >= 2:
                s *= 0.65
            seen[kk] += 1
            div.append((s, d))
        div.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        pos = E.second_stage_rerank(q, div, top_n=20)
        r = match_rank(pos, exp, rb, qt)
        if r is None or not (2 <= r <= 10) or len(pos) < 2:
            continue
        correct = pos[r - 1]; wrong = pos[0]
        smap = {d["id"]: s for s, d in div}
        only_c = sorted(qt & correct["tokens"] - wrong["tokens"])
        only_w = sorted(qt & wrong["tokens"] - correct["tokens"])
        cases.append({
            "q": q[:100], "slice": b["slice"], "rank": r,
            "correct_id": correct["id"], "correct_type": correct["type"],
            "wrong_id": wrong["id"], "wrong_type": wrong["type"],
            "score_correct": round(smap.get(correct["id"], 0.0), 3),
            "score_wrong": round(smap.get(wrong["id"], 0.0), 3),
            "dl_correct": len(correct["tokens"]), "dl_wrong": len(wrong["tokens"]),
            "only_correct_terms": only_c,
            "only_wrong_terms": only_w,
            "df_only_correct": sorted(df[t] for t in only_c),
            "df_only_wrong": sorted(df[t] for t in only_w),
        })
    print(f"[nm] quase-acertos analisados: {len(cases)}")

    # --- agregacao ---
    tot_c = sum(len(c["df_only_correct"]) for c in cases)
    tot_w = sum(len(c["df_only_wrong"]) for c in cases)
    dfc = [v for c in cases for v in c["df_only_correct"]]
    dfw = [v for c in cases for v in c["df_only_wrong"]]

    def med(v):
        return sorted(v)[len(v)//2] if v else 0

    print(f"\n  TERMOS QUE SO O DOC CERTO CASA : {tot_c}  (df mediano {med(dfc)}, media {sum(dfc)/max(1,len(dfc)):.1f})")
    print(f"  TERMOS QUE SO O RANK-1 ERRADO CASA: {tot_w}  (df mediano {med(dfw)}, media {sum(dfw)/max(1,len(dfw)):.1f})")
    if dfc:
        raros = sum(1 for v in dfc if v <= 50)
        comuns = sum(1 for v in dfc if v > 1000)
        print(f"  dos termos do lado CERTO: {raros} sao RAROS (df<=50) e {comuns} sao COMUNS (df>1000)")
    if dfw:
        raros_w = sum(1 for v in dfw if v <= 50)
        comuns_w = sum(1 for v in dfw if v > 1000)
        print(f"  dos termos do lado ERRADO: {raros_w} sao RAROS (df<=50) e {comuns_w} sao COMUNS (df>1000)")

    # --- (3) o que decide hoje: comprimento e tipo ---
    print(f"\n  O QUE DECIDE HOJE (rank-1 errado vs doc certo):")
    lt = sum(1 for c in cases if c["dl_wrong"] < c["dl_correct"])
    gt = sum(1 for c in cases if c["dl_wrong"] > c["dl_correct"])
    print(f"    rank-1 errado e MAIS CURTO que o certo: {lt} | MAIS LONGO: {gt} | igual: {len(cases)-lt-gt}")
    tps = Counter((c["wrong_type"], c["correct_type"]) for c in cases)
    print(f"    pares (errado -> certo) mais comuns:")
    for (w, c), n in tps.most_common(5):
        print(f"      {w} -> {c}: {n}")

    print(f"\n  EXEMPLOS (o que o lado certo casa e o errado nao):")
    for c in cases[:5]:
        print(f"    [r{c['rank']}] {c['q'][:62]}")
        print(f"        certo={c['correct_type']} dl={c['dl_correct']} score={c['score_correct']} "
              f"termos_exclusivos={c['only_correct_terms'][:5]} df={c['df_only_correct'][:5]}")
        print(f"        errado={c['wrong_type']} dl={c['dl_wrong']} score={c['score_wrong']} "
              f"termos_exclusivos={c['only_wrong_terms'][:5]} df={c['df_only_wrong'][:5]}")

    json.dump({"n_docs": n_docs, "avg_dl_real": avg_dl, "hardcoded_avg_dl": 60,
               "n_cases": len(cases), "cases": cases}, open(OUT, "w"))
    print(f"\n[nm] gravado {OUT}")


if __name__ == "__main__":
    main()
