#!/usr/bin/env python3
"""FASE 1b - conserto do boost de entidade no ID (ss_entidade_id).

Achado da FASE 1 (data/eval/ordering_attribution.json, controles OK):
  nos 19 quase-acertos DEMOTADOS pelo 2o estagio, o componente que da' a margem ao
  documento ERRADO e' ss_entidade_id em 16/19 (84%). Em 14/19 o CERTO levou ZERO.
  Dois defeitos de desenho:
    (a) o boost GENERICO (+32 por termo da pergunta que aparece no ID do doc) ACUMULA
        por termo, sem teto (medido +64 e +102);
    (b) chaveia no ID, que e' artefato de nomenclatura (message_catalog tem o codigo
        AWS no ID por construcao).

ALVO: manter o ganho que o 2o estagio ja tem na fatia A (+12,2 - e' de la que vem o
ganho de ancora) E recuperar as demissoes. Nao basta "desligar": e' preciso ver o que cai.

Variantes (base = producao, controle obrigatorio 183/262):
  base            producao, sem alteracao
  ent_cap1        teto de UMA aplicacao no boost generico (+32 max); codigos intactos
  ent_codes_only  remove o boost generico; mantem so' os de codigo/sufixo numerico
  ent_off         remove o bloco de entidade inteiro
  ent_cap_all     teto de uma aplicacao no generico E nos codigos (max, nao soma)

Read-only: nao altera o avaliador nem o corpus.
"""
import sys, os, re, json, time, argparse
from collections import defaultdict

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E

BENCHES = [
    ("v3", os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl")),
    ("h100", os.path.join(REPO, "data", "eval", "holdout_100_unseen.jsonl")),
    ("h50", os.path.join(REPO, "data", "eval", "blind_holdout_50_vault.jsonl")),
    ("r30", os.path.join(REPO, "data", "eval", "realistic_blind_holdout_30.jsonl")),
]
IGNORE = {"opcao", "global", "regra", "documentada", "ambiente", "distribuida", "distributed",
          "workload", "automation", "sobre", "conforme", "oficial", "documentacao", "neste",
          "para", "como"}


def second_stage(q, cands, top_n=20, mode="base"):
    """Copia FIEL de second_stage_rerank, com o bloco de entidade parametrizado."""
    clean = [w.strip(".,;:?!'\"()[]{}").lower() for w in re.findall(r"[A-Za-z0-9_\-]+", q) if len(w) > 2]
    uq = set(clean) - {"qual", "quais", "como", "onde", "por", "que", "para", "com", "dos", "das",
                       "uma", "não", "mais"}
    bigrams = E.extract_ngrams(clean, 2)
    trigrams = E.extract_ngrams(clean, 3)
    out = []
    for s, doc in cands[:top_n]:
        tl = doc["text"].lower()
        ttl = (doc.get("title") or "").lower()
        score = s
        for bg in bigrams:
            if len(bg) > 6 and bg in tl:
                score += 8.0
            if len(bg) > 6 and bg in ttl:
                score += 12.0
        for tg in trigrams:
            if len(tg) > 10 and tg in tl:
                score += 15.0
            if len(tg) > 10 and tg in ttl:
                score += 20.0
        if uq:
            cov = len(uq.intersection(doc["tokens"])) / len(uq)
            if cov >= 0.80:
                score *= 1.25
            elif cov >= 0.60:
                score *= 1.12
        did = doc.get("id", "").lower()
        if mode != "ent_off":
            gen_total = 0.0
            code_total = 0.0
            for term in sorted(uq):
                ct = term.replace("-", "").replace("_", "")
                if mode == "ent_codes_only":
                    pass
                elif len(ct) >= 5 and ct not in IGNORE:
                    if ct in did.replace("-", "").replace("_", ""):
                        if mode == "ent_cap1":
                            gen_total = max(gen_total, 32.0)
                        elif mode == "ent_cap_all":
                            gen_total = max(gen_total, 32.0)
                        else:
                            gen_total += 32.0
                if re.match(r"^[a-z]{3,6}[0-9]{3,5}[a-z]?$", ct):
                    if ct in did.replace("-", ""):
                        if "trouble" in did or "messages" in did or "incident" in did:
                            v = 55.0
                        else:
                            v = 45.0
                        if mode == "ent_cap_all":
                            code_total = max(code_total, v)
                        else:
                            code_total += v
                    elif ct in tl:
                        code_total += 25.0
                nm = re.search(r"[0-9]{3,5}[a-z]$", ct)
                if nm and nm.group(0) in did:
                    code_total += 25.0
            score += gen_total + code_total
        qrl = q.lower()
        for cmd, sub in [("composer", "add"), ("composer", "extract"), ("composer", "delete"),
                         ("composer", "modify"), ("conman", "start"), ("conman", "stop"),
                         ("conman", "fence"), ("conman", "limit"), ("conman", "confirm"),
                         ("conman", "release"), ("conman", "rerun"), ("conman", "showjobs"),
                         ("conman", "status"), ("conman", "switcheventprocessor"),
                         ("planman", "showinfo"), ("planman", "checksync"), ("planman", "resync"),
                         ("planman", "resetplan"), ("optman", "ls"), ("optman", "chg"), ("optman", "cf")]:
            if cmd in qrl and sub in qrl:
                if (cmd in did and sub in did) or (f"{cmd} {sub}" in tl[:200]):
                    score += 35.0
        out.append((score, doc))
    out.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    return [d for _, d in out] + [d for _, d in cands[top_n:]]


def pipeline(q, docs, mode):
    qt = E.tokenize(q)
    sc = []
    for d in docs:
        s = E.compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
        if s > 0:
            sc.append([s, d])
    sc.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    dv = []
    seen = defaultdict(int)
    for s, d in sc:
        k = d.get("runbook") or d.get("type")
        if d.get("type") == "ragflow_runbook_chunk" and seen[k] >= 2:
            s *= 0.65
        seen[k] += 1
        dv.append((s, d))
    dv.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    if mode == "base":
        return E.second_stage_rerank(q, dv, top_n=20), qt
    return second_stage(q, dv, top_n=20, mode=mode), qt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    modes = ["base", "copy_asis", "ent_cap1", "ent_codes_only", "ent_off", "ent_cap_all"]
    if a.only:
        modes = [m for m in modes if m in a.only.split(",")]

    t0 = time.time()
    docs = E.load_documents()
    print(f"[fix] n_docs={len(docs)}", flush=True)
    data = {}
    for tag, path in BENCHES:
        data[tag] = [json.loads(l) for l in open(path) if l.strip()]

    def match(d, exp, rb, qt):
        if d["id"] in exp:
            return True
        if d["type"] == "aws_message":
            for e in exp:
                if d.get("code", "").lower() in e.lower():
                    return True
        elif d["type"] in ("ragflow_runbook_chunk", "runbook_section") and rb and d.get("runbook") == rb:
            oc = len(qt.intersection(d["tokens"]))
            if oc >= 2 and (oc / max(1, len(qt))) >= 0.25:
                return True
        return False

    res = {}
    for mode in modes:
        res[mode] = {}
        for tag, rows in data.items():
            h1 = 0
            for b in rows:
                q = b.get("question", "")
                exp = set(b.get("relevant_claim_ids", []))
                pos, qt = pipeline(q, docs, mode)
                if any(match(d, exp, b.get("runbook_ref"), qt) for d in pos[:1]):
                    h1 += 1
            res[mode][tag] = h1
        r = res[mode]
        tot = sum(r.values())
        print(f"  {mode:16s} v3 {r['v3']:3d}/262   h100 {r['h100']:3d}/100   h50 {r['h50']:2d}/50   "
              f"r30 {r['r30']:2d}/30   externos {r['h100']+r['h50']+r['r30']:3d}/180   ({time.time()-t0:.0f}s)",
              flush=True)

    print(f"\n  delta vs base (v3 / externos):")
    b = res["base"]
    for mode in modes[1:]:
        r = res[mode]
        dv = r["v3"] - b["v3"]
        de = (r["h100"] + r["h50"] + r["r30"]) - (b["h100"] + b["h50"] + b["r30"])
        print(f"    {mode:16s} v3 {dv:+3d}   externos {de:+3d}   -> {'PASSA' if dv > 0 and de >= 0 else 'nao'}")
    json.dump(res, open(os.path.join(REPO, "data", "eval", "entity_boost_fix_sweep.json"), "w"))
    print(f"[fix] {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
