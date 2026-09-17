#!/usr/bin/env python3
"""IDF em TODA a suite (819 perguntas / 15 benchmarks) - o teste que estreita o IC.

Motivo: no blind v3 (262) o IDF deu +6, mas com IC95% [-3, +15] - largo demais para concluir.
O v3 tem 262 perguntas; a suite tem 819. Mais n = IC mais estreito.

Dois intervalos, de proposito:
  - bootstrap SIMPLES: reamostra perguntas (trata todas como independentes)
  - bootstrap ESTRATIFICADO: reamostra CONJUNTOS primeiro, depois perguntas dentro deles
    (conservador: perguntas do mesmo benchmark sao correlacionadas, entao o IC simples e' otimista)
Reporta tambem o delta POR CONJUNTO, porque um efeito que so aparece no agregado nao e' confiavel.

O IDF nao tem parametro livre, portanto NENHUM destes conjuntos foi usado para ajusta-lo - todos valem
como held-out. Ainda assim reportamos a suite separada do v3, que e' o conjunto onde a hipotese nasceu.

READ-ONLY: base usa as funcoes de producao; a variante usa copia com IDF.
"""
import sys, os, json, re, math, random, time, glob
from collections import defaultdict, Counter

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E  # noqa: E402

OUT = os.path.join(REPO, "data/eval/idf_suite_perquestion.json")
K1, B_, AVG_DL = 1.2, 0.75, 60
HWA_TERMS = ["sfinal", "jnextplan", "resetplan", "makeplan", "switchplan", "checksync", "composer",
             "conman", "planman", "joblog", "vartable", "rerun", "generic", "event1", "sbs", "opens",
             "limit", "securityutility", "resync", "twsobjectmonitor", "switcheventprocessor",
             "switchevtp", "helm", "chart", "kubernetes", "tebctl", "cwwkf0011i", "enretain", "wapl",
             "mmrresolve", "symnew", "conddep", "wa_pull_info", "baserecprompt", "aida", "carryforward"]
# conjuntos cujas perguntas sao a ORIGEM do blind v3 (evitar dupla contagem no agregado)
V3_SOURCES = {"blind_v3_slices"}


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


def make_idf_scorer(df, N):
    def sc(qt, doc_tokens, qraw, dtext, doc=None):
        if not doc_tokens:
            return 0.0
        overlap = qt.intersection(doc_tokens)
        if not overlap:
            return 0.0
        score = 0.0
        dl = len(doc_tokens)
        dl_low = dtext.lower()
        for t in sorted(overlap):
            boost = 4.0 if any(x in t for x in HWA_TERMS) else 1.0
            tf = (K1 + 1) / (1.0 + K1 * (1.0 - B_ + B_ * (dl / AVG_DL)))
            d = df.get(t, 0)
            score += boost * tf * math.log((N - d + 0.5) / (d + 0.5) + 1.0)
        q_low = qraw.lower()
        if "processador de eventos" in q_low or "event processor" in q_low:
            if "switcheventprocessor" in dl_low or "switchevtp" in dl_low:
                score += 15.0
        for code in re.findall(r"aws[a-z]{3}[0-9]{3}[iew]", qraw.lower()):
            if code in dl_low:
                score += 15.0
        if doc:
            if doc.get("type") == "message_catalog":
                m = re.search(r"aws([a-z]{3})", doc.get("id", "").lower())
                if m:
                    for fam in E.detect_families(qraw):
                        if fam.lower() == m.group(1):
                            score += E.FAMILY_BOOST
                            break
            dt = doc.get("type")
            if dt == "canonical_claim": score *= 1.25
            elif dt == "lab_evidence": score *= 1.20
            elif dt == "ragflow_runbook_chunk": score *= 1.15
            elif dt == "message_catalog": score *= 1.10
            for token in sorted(qt):
                if token.isalnum() and len(token) > 3 and token in (doc.get("id") or "").lower():
                    score += 4.0
            if doc.get("title") and qt.intersection(E.tokenize(doc["title"])):
                score *= 1.15
            if doc.get("runbook") and doc["runbook"].replace(".md", "").replace("-", "") in qraw.lower().replace("-", ""):
                score *= 1.1
            if dt == "ragflow_runbook_chunk":
                meta = doc.get("metadata", {})
                for cmd in meta.get("commands", []):
                    if cmd.lower() in qraw.lower(): score += 3.5
                for c in meta.get("aws_codes", []):
                    if c.lower() in qraw.lower(): score += 12.0
                if doc.get("path") and qt.intersection(E.tokenize(doc["path"])):
                    score *= 1.2
        return score
    return sc


def main():
    docs = E.load_documents()
    N = len(docs)
    df = Counter()
    for d in docs:
        for t in set(d["tokens"]):
            df[t] += 1
    idf_sc = make_idf_scorer(df, N)
    print(f"[suite] n_docs={N} vocab={len(df)}")

    sets = sorted(glob.glob(os.path.join(REPO, "data/eval/*.jsonl")))
    skip = {"idf_suite_perquestion", "idf_validation_perquestion", "guard_probe_records",
            "challenger_cv_perquestion", "nearmiss_diagnosis", "lexical_enrichment_exp1",
            "corpus_docs_meta_v2"}
    rows = []
    t0 = time.time()
    for p in sets:
        tag = os.path.basename(p)[:-6]
        if tag in skip:
            continue
        try:
            bench = [json.loads(l) for l in open(p) if l.strip()]
        except Exception:
            continue
        if not bench or "question" not in bench[0] or "relevant_claim_ids" not in bench[0]:
            continue
        cnt = 0
        for b in bench:
            q = b.get("question") or ""
            exp = set(b.get("relevant_claim_ids", [])); rb = b.get("runbook_ref")
            if not q:
                continue
            qt = E.tokenize(q)
            out = {}
            for nm, sc in (("base", E.compute_bm25), ("idf", idf_sc)):
                scored = []
                for d in docs:
                    s = sc(qt, d["tokens"], q, d["text"], doc=d)
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
                out[nm] = match_rank(pos, exp, rb, qt)
            # NAO gravar o texto da pergunta: e' redundante (esta nos benchmarks), duplica
            # conteudo ja versionado e faz o scanner de segredo do publish.sh abortar por
            # falso positivo em strings de VERSAO do produto (ex.: 'HWA 10.2.8'). Convencao
            # ja seguida por idf_validation_perquestion.json / challenger_cv_perquestion.json:
            # grava-se o indice dentro do conjunto, que junta com o benchmark na analise.
            rows.append({"set": tag, "i": cnt, "base": out["base"], "idf": out["idf"]})
            cnt += 1
        print(f"[suite] {tag:<34} n={cnt:<4} ({time.time()-t0:.0f}s)", flush=True)

    json.dump(rows, open(OUT, "w"))
    print(f"[suite] gravado {OUT}  total {len(rows)} perguntas")


if __name__ == "__main__":
    main()
