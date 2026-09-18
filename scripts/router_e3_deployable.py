#!/usr/bin/env python3
"""ROTA E3: roteador deployavel por codigos de erro / secoes / REST API V2.

CONTROLES OBRIGATORIOS (sem eles a medicao nao vale):
  (1) lambda=0 (tudo no baseline) tem de reproduzir a PRODUCAO: v3 183/262 e externos 166/180;
  (2) ALINHAMENTO: os ids dos candidatos reconstruidos tem de bater com os do cache que gerou os
      scores do CE. Se nao baterem, os scores salvos estao desalinhados e a medicao e' invalida.

O roteador NAO usa o campo has_anchor nem nenhum rotulo do benchmark. Usa so' o texto da pergunta:
  codigos de erro (AWS*####*, DSRA####*), nomes de secao/view, e 'REST API V2'.
Medido no v3 contra o campo: acc 85,1%, precisao 100% na classe A, recall 63,6%, ZERO falsos-ancora.
Recusado de proposito: prefixos de template do benchmark ('Como solucionar ou diagnosticar...'),
que sao artefato de geracao e nao propriedade da pergunta.
"""
import importlib.util, json, os, re, time
from collections import defaultdict

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
NR = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/hermes/neural-reranker"
CE_SCORES = os.path.join(NR, "ce_scores_top20.json")
TOP_N = 20
BENCHES = [
    ("blind_v3_slices", "v3", os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl")),
    ("holdout_100_unseen", "h100", os.path.join(REPO, "data", "eval", "holdout_100_unseen.jsonl")),
    ("blind_holdout_50_vault", "h50", os.path.join(REPO, "data", "eval", "blind_holdout_50_vault.jsonl")),
    ("realistic_blind_holdout_30", "r30", os.path.join(REPO, "data", "eval", "realistic_blind_holdout_30.jsonl")),
]
PROD = {"v3": 183, "h100": 89, "h50": 49, "r30": 28, "ext": 166}
E3 = re.compile(
    r"\bAWS[A-Z]{2,4}[0-9]{3,4}[A-Z]\b"
    r"|\bDSRA[0-9]{4}[A-Z]\b"
    r"|\b(sfinal|finalpostreports|mdm_bk|bmdm|aida-es|carryforward)\b"
    r"|REST API V2",
    re.I,
)


def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    t0 = time.time()
    rs = load_mod("rs", os.path.join(REPO, "scripts", "rerank_sandbox.py"))
    ev = load_mod("ev", os.path.join(REPO, "data", "eval", "evaluate_rag_benchmark.py"))
    docs = ev.load_documents()
    print(f"[e3] n_docs={len(docs)}", flush=True)
    ce = json.load(open(CE_SCORES))

    built, align_bad, align_tot = {}, 0, 0
    for tag, short, path in BENCHES:
        cache = json.load(open(os.path.join(NR, f"rerank_cache_{tag}.json")))
        rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
        ents = []
        for i, b in enumerate(rows):
            q = b.get("question", "")
            qt = ev.tokenize(q)
            sc = []
            for d in docs:
                s = ev.compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
                if s > 0:
                    sc.append([s, d])
            sc.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
            dv, seen = [], defaultdict(int)
            for s, d in sc:
                k = d.get("runbook") or d.get("type")
                if d.get("type") == "ragflow_runbook_chunk" and seen[k] >= 2:
                    s *= 0.65
                seen[k] += 1
                dv.append((s, d))
            dv.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
            cands = [{"id": d["id"], "type": d.get("type"),
                      "ov": len(set(qt) & d["tokens"]), "doc": d} for _, d in dv[:TOP_N]]
            # controle 2: alinhamento com o cache que gerou os scores do CE
            ref = [c["id"] for c in cache[i]["cands"][:TOP_N]]
            got = [c["id"] for c in cands]
            align_tot += 1
            if ref != got:
                align_bad += 1
            ents.append({"q": q, "expected": set(b.get("relevant_claim_ids", [])),
                         "runbook": b.get("runbook_ref"), "q_tokens": qt,
                         "cands": cands, "base_top": cache[i]["base_top"],
                         "prod_id": cache[i]["base_order50"][0] if cache[i].get("base_order50") else None})
        built[tag] = ents
        print(f"[e3] {tag}: reconstruido ({len(ents)} perguntas, {time.time()-t0:.0f}s)", flush=True)

    print(f"\n[e3] CONTROLE 2 (alinhamento cache x reconstrucao): {align_tot-align_bad}/{align_tot} perguntas "
          f"com candidatos IDENTICOS -> {'OK' if align_bad == 0 else f'FALHOU ({align_bad} divergentes)'}")

    def top1_ce(ei, e):
        per = {int(k): v for k, v in ce[tag].get(str(ei), {}).items()}
        if not per:
            return None
        fb = min(per.values())
        best = max(range(len(e["cands"])), key=lambda i: (per.get(i, fb), str(e["cands"][i]["id"])))
        return e["cands"][best]

    res = {}
    for tag, short, _ in BENCHES:
        ce[tag] = ce[tag]
        h_base = h_ce = h_route = 0
        n_a = n_b = 0
        for ei, e in enumerate(built[tag]):
            # baseline: a ordem de PRODUCAO ja' esta no cache
            bt = e["base_top"][0] if e["base_top"] else None
            if bt and rs._match(bt, e):
                h_base += 1
            c = top1_ce(ei, e)
            if c and rs._match(c, e):
                h_ce += 1
            anchored = bool(E3.search(e["q"]))
            n_a += anchored
            n_b += (not anchored)
            # rota: ancora -> baseline; sem ancora -> CE
            cand = bt if anchored else c
            if cand and rs._match(cand, e):
                h_route += 1
        res[short] = {"base": h_base, "ce": h_ce, "route": h_route, "n_anc": n_a, "n_nao": n_b}
        print(f"  {short:5s} n={len(built[tag]):3d}  baseline {h_base:3d}  CE {h_ce:3d}  "
              f"ROTA-E3 {h_route:3d}  | roteadas p/ baseline {n_a}, p/ CE {n_b}", flush=True)
    res["ext"] = {k: res[k]["base"] + 0 for k in ("h100", "h50", "r30")}
    ext_b = res["h100"]["base"] + res["h50"]["base"] + res["r30"]["base"]
    ext_r = res["h100"]["route"] + res["h50"]["route"] + res["r30"]["route"]

    print(f"\n[e3] CONTROLE 1 (baseline reconstruido == producao):")
    print(f"       v3 {res['v3']['base']}/262 (esperado {PROD['v3']}) | externos {ext_b}/180 (esperado {PROD['ext']})"
          f"  -> {'OK' if (res['v3']['base'], ext_b) == (183, 166) else 'FALHOU'}")
    print(f"\n[e3] RESULTADO DA ROTA E3:")
    print(f"       v3       {PROD['v3']} -> {res['v3']['route']}  ({res['v3']['route']-PROD['v3']:+d})")
    for k in ("h100", "h50", "r30"):
        print(f"       {k:8s} {PROD[k]} -> {res[k]['route']}  ({res[k]['route']-PROD[k]:+d})")
    print(f"       externos {PROD['ext']} -> {ext_r}  ({ext_r-PROD['ext']:+d})")
    print(f"\n[e3] veredito: {'PASSA' if res['v3']['route'] > PROD['v3'] and ext_r >= PROD['ext'] else 'NAO PASSA'}"
          f"   ({time.time()-t0:.0f}s)")
    json.dump(res, open(os.path.join(REPO, "data", "eval", "router_e3_result.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
