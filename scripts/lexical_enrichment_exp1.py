#!/usr/bin/env python3
"""Plano de enriquecimento lexical - EXPERIMENTO 1: escala dos boosts + IDF.

Dois achados do diagnostico dos 49 quase-acertos:
  (A) 19/49 sao DEFEITO DE ORDENACAO: o scorer lexical ja tinha o doc certo em 1o e o
      `second_stage_rerank` inverteu. Mecanismo medido: os boosts dele sao ABSOLUTOS e enormes
      (+32 id, +45/+55 codigo de erro, +35 par CLI, +15/+20 trigram) contra uma base BM25 de ~5-20.
      Um unico +45 domina o score lexical.
  (B) 30/49 sao ERRO REAL DO SCORER. `compute_bm25` NAO tem IDF: termo presente em todos os 6969
      documentos pesa igual a termo presente em um. O doc certo casa 110 termos exclusivos contra 40
      do errado e mesmo assim perde.

Variantes (tudo lexical, ZERO treino - dataset de produto so para indexacao/avaliacao):
  base        : producao como esta (controle; TEM de dar 183/262)
  b<a>        : boosts do second_stage multiplicados por <a> (0 = desliga-los)
  idf         : compute_bm25 com fator IDF classico ln((N-df+0.5)/(df+0.5)+1)
  idf+b<a>    : combinacao

Avalia em v3 (262) e nos 3 externos (180). READ-ONLY: nao altera o modulo de producao.
"""
import sys, os, json, re, math, argparse, time
from collections import defaultdict, Counter

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E  # noqa: E402

SETS = [
    ("v3", "data/eval/blind_v3_slices.jsonl"),
    ("h100", "data/eval/holdout_100_unseen.jsonl"),
    ("h50", "data/eval/blind_holdout_50_vault.jsonl"),
    ("r30", "data/eval/realistic_blind_holdout_30.jsonl"),
]
ALPHAS = [1.0, 0.5, 0.25, 0.1, 0.0]
OUT = os.path.join(REPO, "data/eval/lexical_enrichment_exp1.json")

# --- constantes copiadas da producao (para replicar a base sem tocar no modulo) ---
K1, B_ = 1.2, 0.75
AVG_DL = 60
HWA_TERMS = ["sfinal", "jnextplan", "resetplan", "makeplan", "switchplan", "checksync", "composer",
             "conman", "planman", "joblog", "vartable", "rerun", "generic", "event1", "sbs", "opens",
             "limit", "securityutility", "resync", "twsobjectmonitor", "switcheventprocessor",
             "switchevtp", "helm", "chart", "kubernetes", "tebctl", "cwwkf0011i", "enretain", "wapl",
             "mmrresolve", "symnew", "conddep", "wa_pull_info", "baserecprompt", "aida", "carryforward"]


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


def make_scorer(df, N, use_idf):
    """Replica compute_bm25 da producao; com use_idf adiciona o fator IDF classico.
    use_idf is None -> devolve a FUNCAO DE PRODUCAO (base fiel por construcao)."""
    if use_idf is None:
        return E.compute_bm25

    def sc(qt, doc_tokens, qraw, dtext, doc=None):
        if not doc_tokens:
            return 0.0
        overlap = qt.intersection(doc_tokens)
        if not overlap:
            return 0.0
        score = 0.0
        dl = len(doc_tokens)
        doc_lower = dtext.lower()
        for t in sorted(overlap):
            boost = 1.0
            if any(x in t for x in HWA_TERMS):
                boost = 4.0
            tf = (K1 + 1) / (1.0 + K1 * (1.0 - B_ + B_ * (dl / AVG_DL)))
            if use_idf:
                d = df.get(t, 0)
                idf = math.log((N - d + 0.5) / (d + 0.5) + 1.0)
                tf *= idf
            score += boost * tf
        q_low = qraw.lower()
        if "processador de eventos" in q_low or "event processor" in q_low:
            if "switcheventprocessor" in doc_lower or "switchevtp" in doc_lower:
                score += 15.0
        for code in re.findall(r"aws[a-z]{3}[0-9]{3}[iew]", qraw.lower()):
            if code in doc_lower:
                score += 15.0
        if doc:
            # 2.1 FAMILY_LEXICON (estava FALTANDO na 1a versao: foi o que fez a base dar 178 em vez de 183)
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


def second_stage(query_raw, candidates, top_n=20, alpha=1.0):
    """Replica second_stage_rerank da producao, com TODOS os boosts aditivos multiplicados por alpha."""
    clean = [w.strip(".,;:?!'\"()[]{}").lower() for w in re.findall(r"[A-Za-z0-9_\-]+", query_raw) if len(w) > 2]
    uq = set(clean) - {"qual", "quais", "como", "onde", "por", "que", "para", "com", "dos", "das", "uma", "não", "mais"}
    bigrams = E.extract_ngrams(clean, 2)
    trigrams = E.extract_ngrams(clean, 3)
    out = []
    for s, doc in candidates[:top_n]:
        tl = doc["text"].lower(); til = (doc.get("title") or "").lower()
        score = s
        for bg in bigrams:
            if len(bg) > 6 and bg in tl: score += 8.0 * alpha
            if len(bg) > 6 and bg in til: score += 12.0 * alpha
        for tg in trigrams:
            if len(tg) > 10 and tg in tl: score += 15.0 * alpha
            if len(tg) > 10 and tg in til: score += 20.0 * alpha
        if uq:
            cov = len(uq.intersection(doc["tokens"])) / len(uq)
            if cov >= 0.80: score *= 1.25
            elif cov >= 0.60: score *= 1.12
        did = doc.get("id", "").lower()
        ig = {"opcao", "global", "regra", "documentada", "ambiente", "distribuida", "distributed",
              "workload", "automation", "sobre", "conforme", "oficial", "documentacao", "neste", "para", "como"}
        for term in sorted(uq):
            ct = term.replace("-", "").replace("_", "")
            if len(ct) >= 5 and ct not in ig:
                if ct in did.replace("-", "").replace("_", ""): score += 32.0 * alpha
            if re.match(r"^[a-z]{3,6}[0-9]{3,5}[a-z]?$", ct):
                if ct in did.replace("-", ""):
                    score += (55.0 if ("trouble" in did or "messages" in did or "incident" in did) else 45.0) * alpha
                elif ct in tl:
                    score += 25.0 * alpha
            nm = re.search(r"[0-9]{3,5}[a-z]$", ct)
            if nm and nm.group(0) in did: score += 25.0 * alpha
        ql = query_raw.lower()
        for cmd, sub in [("composer", "add"), ("composer", "extract"), ("composer", "delete"),
                         ("composer", "modify"), ("conman", "start"), ("conman", "stop"),
                         ("conman", "fence"), ("conman", "limit"), ("conman", "confirm"),
                         ("conman", "release"), ("conman", "rerun"), ("conman", "showjobs"),
                         ("conman", "status"), ("conman", "switcheventprocessor"),
                         ("planman", "showinfo"), ("planman", "checksync"), ("planman", "resync"),
                         ("planman", "resetplan"), ("optman", "ls"), ("optman", "chg"), ("optman", "cf")]:
            if cmd in ql and sub in ql:
                if (cmd in did and sub in did) or (f"{cmd} {sub}" in tl[:200]):
                    score += 35.0 * alpha
        out.append((score, doc))
    out.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    return [r[1] for r in out] + [c[1] for c in candidates[top_n:]]


def main():
    import argparse as _ap
    p = _ap.ArgumentParser()
    p.add_argument("--only", default="")
    _a = p.parse_args()
    docs = E.load_documents()
    N = len(docs)
    df = Counter()
    for d in docs:
        for t in set(d["tokens"]):
            df[t] += 1
    print(f"[exp] n_docs={N}  vocab={len(df)}")

    benches = {}
    for tag, path in SETS:
        benches[tag] = [json.loads(l) for l in open(os.path.join(REPO, path)) if l.strip()]

    variants = [("base", None, 1.0)]
    for a in ALPHAS[1:]:
        variants.append((f"b{a}", False, a))
    variants.append(("idf", True, 1.0))
    variants.append(("idf+b0.25", True, 0.25))
    if _a.only:
        keep = {x.strip() for x in _a.only.split(",") if x.strip()}
        variants = [v for v in variants if v[0] in keep]

    results = {}
    for name, use_idf, alpha in variants:
        sc = make_scorer(df, N, use_idf)
        results[name] = {}
        t0 = time.time()
        for tag, bench in benches.items():
            h1 = n = 0
            for b in bench:
                q = b.get("question") or ""
                exp = set(b.get("relevant_claim_ids", [])); rb = b.get("runbook_ref")
                if not q:
                    continue
                qt = E.tokenize(q)
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
                pos = (E.second_stage_rerank(q, div, top_n=20) if use_idf is None
                       else second_stage(q, div, 20, alpha))
                n += 1
                if match_rank(pos, exp, rb, qt) == 1:
                    h1 += 1
            results[name][tag] = (h1, n)
        v3 = results[name]["v3"]
        ext = sum(results[name][t][0] for t in ("h100", "h50", "r30"))
        extn = sum(results[name][t][1] for t in ("h100", "h50", "r30"))
        print(f"  {name:<12} v3 {v3[0]:>3}/{v3[1]} ({100*v3[0]/v3[1]:5.1f}%)   "
              f"ext {ext:>3}/{extn} ({100*ext/extn:5.1f}%)   [{time.time()-t0:.0f}s]")

    json.dump({k: {t: list(v) for t, v in d.items()} for k, d in results.items()}, open(OUT, "w"))
    print(f"[exp] gravado {OUT}")


if __name__ == "__main__":
    main()
