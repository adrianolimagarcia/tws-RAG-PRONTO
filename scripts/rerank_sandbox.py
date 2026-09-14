#!/usr/bin/env python3
"""Sandbox de re-ranking (NAO altera o avaliador).

Fase 1 (--build): replica o pipeline do avaliador (bm25 -> sort -> diversidade), guarda o top-50
por pergunta com as FEATURES de cada candidato, e VALIDA a replicacao reproduzindo o baseline.
Fase 2 (--tune): grade de pesos sobre a fatia A (tune), depois valida em B e D (holdout).

Features por candidato (todas normalizadas):
  f_base      score do 1o estagio / max do pool
  f_rarecov   soma de IDF dos termos da pergunta presentes no doc / soma de IDF da pergunta
  f_minidf    IDF do termo MAIS RARO da pergunta presente no doc / maior IDF da pergunta
  f_entity    1 se codigo/entidade da pergunta casa com o id do doc (senao 0)
  f_type      prior por tipo: lab_evidence 1.0 | canonical_claim 0.6 | runbook 0.3 | msgcat 0.0
  f_contig    bigramas/trigramas contiguos da pergunta presentes no texto (normalizado)
"""
import importlib.util, json, math, os, re, sys
from collections import defaultdict

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CACHE = "/tmp/ha_fm/rerank_cache.json"
TOP_N = 50
STOP = {"qual", "quais", "como", "onde", "por", "que", "para", "com", "dos", "das", "uma",
        "nao", "não", "mais", "este", "essa", "esse", "seu", "sua", "the", "and", "for"}
TYPE_PRIOR = {"lab_evidence": 1.0, "canonical_claim": 0.6, "runbook_section": 0.3,
              "ragflow_runbook_chunk": 0.3, "optman_option": 0.3, "aws_message": 0.0,
              "message_catalog": 0.0}


def load_ev():
    spec = importlib.util.spec_from_file_location(
        "ev", os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py"))
    if spec is None or spec.loader is None:
        raise RuntimeError("nao foi possivel carregar data/eval/evaluate_rag_benchmark.py")
    ev = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ev)
    return ev


def build_idf(docs):
    df = defaultdict(int)
    for d in docs:
        for t in d["tokens"]:
            df[t] += 1
    N = len(docs)
    return {t: math.log((N - c + 0.5) / (c + 0.5) + 1.0) for t, c in df.items()}, N


def pipeline(ev, docs, q_text):
    q_tokens = ev.tokenize(q_text)
    scored = []
    for doc in docs:
        s = ev.compute_bm25(q_tokens, doc["tokens"], q_text, doc["text"], doc=doc)
        if s > 0:
            scored.append([s, doc])
    scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    div, seen = [], defaultdict(int)
    for s, doc in scored:
        k = doc.get("runbook") or doc.get("type")
        c = seen[k]
        if doc.get("type") == "ragflow_runbook_chunk" and c >= 2:
            s *= 0.65
        seen[k] += 1
        div.append((s, doc))
    div.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    return div, q_tokens


def rank_of(docs_list, expected, expected_runbook, q_tokens):
    for i, d in enumerate(docs_list):
        if d["id"] in expected:
            return i + 1
        if d["type"] == "aws_message":
            for e in expected:
                if d.get("code", "").lower() in e.lower():
                    return i + 1
        if d["type"] in ("ragflow_runbook_chunk", "runbook_section") and expected_runbook and d.get("runbook") == expected_runbook:
            ov = len(q_tokens & d["tokens"])
            if ov >= 2 and ov / max(1, len(q_tokens)) >= 0.25:
                return i + 1
    return None


def features(q_text, q_tokens, doc, s, max_s, idf):
    qt = {t for t in q_tokens if t not in STOP and len(t) > 2}
    dt = doc["tokens"]
    matched = qt & dt
    idf_q = sum(idf.get(t, 0.0) for t in qt) or 1.0
    f_rarecov = sum(idf.get(t, 0.0) for t in matched) / idf_q
    f_minidf = (min((idf.get(t, 0.0) for t in matched), default=0.0) /
                (max((idf.get(t, 0.0) for t in qt), default=1.0) or 1.0)) if matched else 0.0
    # entidade: codigo AWS*#### ou termo >=5 chars casando com o id do doc
    doc_id_n = doc.get("id", "").lower().replace("-", "").replace("_", "")
    f_entity = 0.0
    for t in sorted(qt):
        ct = t.replace("-", "").replace("_", "")
        if len(ct) >= 5 and ct in doc_id_n:
            f_entity = 1.0
            break
        if re.match(r"^[a-z]{3,6}[0-9]{3,5}[a-z]?$", ct) and ct in doc_id_n:
            f_entity = 1.0
            break
    # contiguidade (bigramas/trigramas da pergunta no texto)
    words = [w for w in re.findall(r"[A-Za-z0-9_\-]+", q_text.lower()) if len(w) > 2]
    text_l = doc["text"].lower()
    hits = 0
    tot = 0
    for n in (2, 3):
        for i in range(len(words) - n + 1):
            g = " ".join(words[i:i + n])
            if len(g) > (6 if n == 2 else 10):
                tot += 1
                if g in text_l:
                    hits += 1
    f_contig = hits / tot if tot else 0.0
    return {
        "f_base": s / max_s if max_s else 0.0,
        "f_rarecov": f_rarecov,
        "f_minidf": f_minidf,
        "f_entity": f_entity,
        "f_type": TYPE_PRIOR.get(doc.get("type"), 0.3),
        "f_contig": f_contig,
        "ov": len(set(q_tokens) & dt),   # overlap cru com os tokens da pergunta (match de chunk)
    }


def build(ev, docs, bench_path, out_path):
    bench = [json.loads(l) for l in open(bench_path, encoding="utf-8") if l.strip()]
    idf, N = build_idf(docs)
    print(f"docs={len(docs)} | perguntas={len(bench)} | cache -> {out_path}")
    cache = []
    for b in bench:
        q = b.get("question", "")
        div, q_tokens = pipeline(ev, docs, q)
        max_s = div[0][0] if div else 0.0
        # baseline: replica a segunda etapa do avaliador
        base_order = ev.second_stage_rerank(q, div, top_n=20)
        exp = set(b.get("relevant_claim_ids", []))
        rbase = rank_of(base_order, exp, b.get("runbook_ref"), q_tokens)
        top = []
        for s, doc in div[:TOP_N]:
            f = features(q, q_tokens, doc, s, max_s, idf)
            top.append({"id": doc["id"], "type": doc.get("type"), "score": s, **f})
        cache.append({"id": b.get("id"), "slice": b.get("slice"), "question": q,
                      "expected": list(exp), "runbook": b.get("runbook_ref"),
                      "q_tokens": sorted(q_tokens), "rank_baseline": rbase,
                      "base_top": [{"id": d["id"], "type": d.get("type"),
                                    "ov": len(set(q_tokens) & d["tokens"])}
                                   for d in base_order[:10]],
                      "base_order50": [d["id"] for d in base_order[:TOP_N]],
                      "cands": top})
    json.dump(cache, open(out_path, "w"), ensure_ascii=False)
    # validacao da replicacao
    hits = {1: 0, 3: 0, 5: 0, 10: 0}
    mrr = 0.0
    for c in cache:
        r = c["rank_baseline"]
        if r:
            mrr += 1.0 / r
            for k in hits:
                if r <= k:
                    hits[k] += 1
    n = len(cache)
    print(f"BASELINE REPLICADO: @1 {hits[1]}/{n} ({100*hits[1]/n:.1f}%) @3 {hits[3]} @5 {hits[5]} @10 {hits[10]} MRR {mrr/n:.4f}")


FEATS = ["f_base", "f_rarecov", "f_minidf", "f_entity", "f_type", "f_contig"]


def _rb_of(cand):
    """Nome do runbook de um chunk (id no formato ragflow:<arquivo>:<n>)."""
    rid = str(cand.get("id", ""))
    if rid.startswith("ragflow:") and rid.count(":") >= 2:
        return rid.split(":")[1]
    return ""


def _match(cand, entry):
    """Mesma regra de match do avaliador (id exato | codigo de mensagem | chunk do runbook esperado)."""
    if cand["id"] in entry["expected"]:
        return True
    if cand.get("type") == "aws_message":
        code = str(cand["id"]).split("-")[-1].lower()
        for e in entry["expected"]:
            if code and code in e.lower():
                return True
    if cand.get("type") in ("ragflow_runbook_chunk", "runbook_section") and entry.get("runbook"):
        if _rb_of(cand) == entry["runbook"]:
            ov = cand.get("ov", 0)
            nq = max(1, len(entry["q_tokens"]))
            if ov >= 2 and ov / nq >= 0.25:
                return True
    return False


def _rank(entry, w, top_n=TOP_N):
    """Rank do 1o acerto. w=None => ordem do 1o estagio (sem re-rank)."""
    cs = entry["cands"][:top_n]
    if w is None:
        order = cs
    else:
        scored = [(sum(w.get(k, 0.0) * c.get(k, 0.0) for k in FEATS), c) for c in cs]
        scored.sort(key=lambda x: (-x[0], str(x[1]["id"])))
        order = [c for _, c in scored]
    for i, c in enumerate(order):
        if _match(c, entry):
            return i + 1
    return None


def _metrics(entries, w, top_n=TOP_N):
    h = {1: 0, 3: 0, 5: 0, 10: 0}
    mrr = 0.0
    for e in entries:
        r = _rank(e, w, top_n)
        if r:
            mrr += 1.0 / r
            for k in h:
                if r <= k:
                    h[k] += 1
    n = len(entries) or 1
    return {"n": len(entries), "@1": h[1] / n, "@3": h[3] / n, "@5": h[5] / n,
            "@10": h[10] / n, "mrr": mrr / n}


def _fmt(tag, m):
    return (f"  {tag:26s} n={m['n']:>3d} @1 {100*m['@1']:5.1f}% @3 {100*m['@3']:5.1f}% "
            f"@5 {100*m['@5']:5.1f}% @10 {100*m['@10']:5.1f}% MRR {m['mrr']:.4f}")


SPEC_FEATS = ["f_rarecov", "f_minidf", "f_type", "f_contig", "f_entity"]


def _rank_boost(entry, wspec):
    """Preserva a ordem do baseline (top-50) e soma um boost de especificidade em unidades de 'posicao'.
    wspec=0 reproduz exatamente a ordem baseline."""
    order_base = entry.get("base_order50") or [c["id"] for c in entry["cands"]]
    by_id = {c["id"]: c for c in entry["cands"]}
    scored = []
    for i, cid in enumerate(order_base):
        c = by_id.get(cid)
        if c is None:
            continue
        spec = sum(wspec.get(k, 0.0) * c.get(k, 0.0) for k in SPEC_FEATS)
        scored.append((-(i + 1) + spec, c))
    scored.sort(key=lambda x: (-x[0], str(x[1]["id"])))
    for i, (_, c) in enumerate(scored):
        if _match(c, entry):
            return i + 1
    return None


def _metrics_boost(entries, wspec):
    h = {1: 0, 3: 0, 5: 0, 10: 0}
    mrr = 0.0
    for e in entries:
        r = _rank_boost(e, wspec)
        if r:
            mrr += 1.0 / r
            for k in h:
                if r <= k:
                    h[k] += 1
    n = len(entries) or 1
    return {"n": len(entries), "@1": h[1] / n, "@3": h[3] / n, "@5": h[5] / n,
            "@10": h[10] / n, "mrr": mrr / n}


def tune(cache_path):
    cache = json.load(open(cache_path))
    by = defaultdict(list)
    for e in cache:
        by[e["slice"] or "?"].append(e)
    A, B, D = by["A_com_ancora"], by["B_sem_ancora"], by["D_holdout_temporal"]
    print(f"cache: {len(cache)} perguntas | A={len(A)} B={len(B)} D={len(D)}\n")

    # -1. VALIDACAO do meu _match contra o rank_baseline (calculado pelas funcoes do avaliador)
    ok = bad = 0
    for e in cache:
        r = None
        for i, c in enumerate(e.get("base_top", [])):
            if _match(c, e):
                r = i + 1
                break
        if e["rank_baseline"] is not None and e["rank_baseline"] <= 10:
            if r == e["rank_baseline"]:
                ok += 1
            else:
                bad += 1
    print(f"validacao do match: {ok} coincidem | {bad} divergem (esperado 0)\n")

    # 0. validacao: ordem do 1o estagio vs o baseline registrado (deve ser pior ou igual)
    for tag, ents in (("A", A), ("B", B), ("D", D)):
        print(_fmt(f"1o estagio (sem rerank) {tag}", _metrics(ents, None)))
    print()
    base = {tag: sum(1 for e in ents if e["rank_baseline"] == 1) / (len(ents) or 1)
            for tag, ents in (("A", A), ("B", B), ("D", D))}
    print(f"  baseline registrado (2a etapa do avaliador): A {100*base['A']:.1f}% "
          f"B {100*base['B']:.1f}% D {100*base['D']:.1f}% @1\n")

    # 1. SEPARACAO DE FEATURES: candidato CORRETO vs o top-1 do 1o estagio
    print("=== separacao de features (perguntas em que o correto NAO e o top-1 do 1o estagio) ===")
    acc = defaultdict(lambda: [0.0, 0.0, 0])
    for e in A + B + D:
        corr = next((c for c in e["cands"] if _match(c, e)), None)
        top1 = e["cands"][0] if e["cands"] else None
        if not corr or not top1 or corr["id"] == top1["id"]:
            continue
        for f in FEATS:
            acc[f][0] += corr.get(f, 0.0)
            acc[f][1] += top1.get(f, 0.0)
            acc[f][2] += 1
    for f in FEATS:
        s, t, n = acc[f]
        if n:
            print(f"  {f:12s} correto {s/n:6.3f} | top-1 {t/n:6.3f} | delta {(s-t)/n:+.3f}  (n={n})")
    print()

    # 2. VARIANTES (tune em A, valida em B/D)
    variants = {
        "paridade (base+ent+cont)": {"f_base": 1.0, "f_entity": 4.0, "f_contig": 1.0},
        "especificidade": {"f_rarecov": 1.0, "f_minidf": 1.0, "f_type": 1.0},
        "esp+paridade": {"f_base": 1.0, "f_entity": 4.0, "f_contig": 1.0,
                         "f_rarecov": 1.0, "f_minidf": 1.0, "f_type": 1.0},
    }
    print("=== variantes (tune=A | validacao=B,D) ===")
    for name, w in variants.items():
        print(_fmt(f"{name} [A]", _metrics(A, w)))
        print(_fmt(f"{name} [B]", _metrics(B, w)))
        print(_fmt(f"{name} [D]", _metrics(D, w)))
        print()

    # 3. BOOST DE ESPECIFICIDADE SOBRE A ORDEM BASELINE (tune em A, valida em B/D)
    print("=== boost de especificidade sobre a ordem baseline ===")
    w0 = {k: 0.0 for k in SPEC_FEATS}
    for tag, ents in (("A", A), ("B", B), ("D", D)):
        print(_fmt(f"w=0 (=baseline) [{tag}]", _metrics_boost(ents, w0)))
    print()
    print("--- efeito isolado de cada feature (peso 2) ---")
    for f in SPEC_FEATS:
        w1 = {k: 0.0 for k in SPEC_FEATS}
        w1[f] = 2.0
        print(_fmt(f"so {f} [A]", _metrics_boost(A, w1)))
        print(_fmt(f"so {f} [B]", _metrics_boost(B, w1)))
        print(_fmt(f"so {f} [D]", _metrics_boost(D, w1)))
    print()
    w = dict(w0)
    best = _metrics_boost(A, w)["@1"]
    for _ in range(3):
        improved = False
        for f in SPEC_FEATS:
            for v in (0.5, 1.0, 2.0, 4.0, 8.0, 16.0):
                w2 = dict(w)
                w2[f] = v
                m = _metrics_boost(A, w2)["@1"]
                if m > best + 1e-9:
                    best, w, improved = m, w2, True
        if not improved:
            break
    print("--- ascensao coordenada em A ---")
    print("  melhor em A:", {k: v for k, v in w.items() if v}, f"| @1(A)={100*best:.1f}%")
    for tag, ents in (("A", A), ("B", B), ("D", D)):
        print(_fmt(f"tuneado-em-A [{tag}]", _metrics_boost(ents, w)))


if __name__ == "__main__":
    ev = load_ev()
    docs = ev.load_documents()
    if "--build" in sys.argv:
        i = sys.argv.index("--build")
        bench = sys.argv[i + 1]
        out = sys.argv[i + 2] if len(sys.argv) > i + 2 else CACHE
        build(ev, docs, bench, out)
    elif "--tune" in sys.argv:
        i = sys.argv.index("--tune")
        tune(sys.argv[i + 1] if len(sys.argv) > i + 1 else CACHE)
