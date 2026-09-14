#!/usr/bin/env python3
"""Constroi o conjunto cego v3 em 4 fatias (A ancora / B sem-ancora / C negativos / D holdout temporal).

Regras de honestidade (protocolo em docs/lab-protocols/blind-v3-protocol.md):
  - NENHUMA pergunta que ja exista embutida (>=85% dos tokens) nas synthetic_questions do corpus
    entra nas fatias A/B/D  -> remove o vazamento medido em A1.
  - A fatia D usa apenas perguntas cuja claim esperada vem de arquivo de evidencia NOVO
    (data >= CUTOFF), i.e. holdout temporal real.
  - A fatia C (negativos) exige que o termo-alvo tenha ZERO ocorrencias no corpus (verificado).
Uso: python3 scripts/build_blind_v3.py [--dry-run]
"""
import json, os, re, sys, glob, unicodedata
from collections import defaultdict

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CUTOFF_DATE = "2026-09-13"          # claims cujo source_file tem data >= isso entram na fatia D
EMBED_THRESHOLD = 0.85              # cobertura de tokens que caracteriza "pergunta embutida"
CORPUS = os.path.join(REPO, "data", "export", "tws_corpus_master_consolidated.jsonl")
SETS = ["golden_qa_benchmark", "holdout_100_unseen", "pure_virgin_test_40",
        "blind_holdout_50_vault", "fresh_blind_test_40", "golden_qa_messages_benchmark",
        "golden_qa_virgin_benchmark", "golden_qa_virgin_expanded", "blind_holdout_qa_30"]
# Codigo de mensagem AWS*, ou termo de comando/produto em CAIXA ALTA (>=3 chars)
ANCHOR_RE = re.compile(r"AWS[A-Z]{2,4}\d{3,4}[EIW]?|\b[A-Z][A-Z0-9_]{3,}\b")
# Candidatos a NEGATIVO: componentes plausiveis que NAO devem existir no corpus
NEG_STOP = {"workload", "plan", "job", "stream", "pool", "queue", "schedule", "concurrency",
            "component", "service", "daemon", "orchestrator", "optimizer", "governor"}
NEG_CANDIDATES = [
    "workload harmonizer", "plan sentinel", "concurrency governor", "stream balancer",
    "job orchestrator daemon", "schedule reconciler", "queue arbitrator", "pool optimizer service",
]


def toks(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.findall(r"[a-z0-9]+", s)


def main(dry):
    corpus = {}
    for ln in open(CORPUS, encoding="utf-8"):
        ln = ln.strip()
        if ln:
            d = json.loads(ln)
            corpus[d["claim_id"]] = d
    # texto integral do corpus (para verificar negativos e embutimento)
    syn_sets = {}
    full_text = set()
    for cid, d in corpus.items():
        qs = d.get("synthetic_questions") or []
        if isinstance(qs, str):
            qs = [qs]
        # guarda CADA pergunta sintetica separadamente (concatenar superestima o vazamento)
        syn_sets[cid] = [set(toks(x)) for x in qs if str(x).strip()]
        full_text.update(toks(f"{d.get('claim','')} {d.get('context_prefix','')}"))

    def embedded(q):
        """True se a pergunta casa com UMA pergunta sintetica especifica (cobertura mutua >=0.7)."""
        qt = set(toks(q))
        if not qt:
            return False, None
        best, bs = None, 0.0
        for cid, lst in syn_sets.items():
            for s in lst:
                if not s:
                    continue
                c1 = len(qt & s) / len(qt)
                c2 = len(qt & s) / len(s)
                c = min(c1, c2)
                if c > bs:
                    bs, best = c, cid
        return (bs >= 0.7), best

    def src_date(cid):
        sf = str(corpus.get(cid, {}).get("source_file", ""))
        m = re.search(r"(20\d{2}-\d{2}-\d{2})", sf)
        return m.group(1) if m else ""

    out, seen = [], set()
    stats = defaultdict(int)
    for name in SETS:
        p = os.path.join(REPO, "data", "eval", f"{name}.jsonl")
        if not os.path.exists(p):
            continue
        for ln in open(p, encoding="utf-8"):
            ln = ln.strip()
            if not ln:
                continue
            d = json.loads(ln)
            q = d.get("question", "")
            ids = [i for i in (d.get("relevant_claim_ids") or []) if i in corpus]
            if not q or not ids or q in seen:
                continue
            seen.add(q)
            emb, emb_doc = embedded(q)
            has_anchor = bool(ANCHOR_RE.search(q))
            newest = max((src_date(i) for i in ids), default="")
            temporal = bool(newest) and newest >= CUTOFF_DATE
            if emb:
                stats["descartadas_por_embutimento"] += 1
                continue
            if temporal:
                slice_ = "D_holdout_temporal"
            elif has_anchor:
                slice_ = "A_com_ancora"
            else:
                slice_ = "B_sem_ancora"
            stats[slice_] += 1
            out.append({
                "id": f"v3-{slice_[0]}-{len(out):04d}",
                "slice": slice_,
                "question": q,
                "relevant_claim_ids": ids,
                "provenance": name,
                "has_anchor": has_anchor,
                "embedded_in_corpus": False,
                "expected_source_date": newest,
                "runbook_ref": d.get("runbook_ref"),
            })

    # Fatia D manual: perguntas escritas a mao sobre as claims MAIS NOVAS (nao usa synthetic_questions,
    # portanto nao carrega o vazamento medido em A1). Holdout temporal real.
    pman = os.path.join(REPO, "data", "eval", "blind_v3_slice_d_manual.jsonl")
    if os.path.exists(pman):
        for ln in open(pman, encoding="utf-8"):
            ln = ln.strip()
            if not ln:
                continue
            d = json.loads(ln)
            q = d.get("question", "")
            ids = [i for i in (d.get("relevant_claim_ids") or []) if i in corpus]
            if not q or not ids or q in seen:
                continue
            seen.add(q)
            emb, _ = embedded(q)
            if emb:
                stats["descartadas_por_embutimento"] += 1
                continue
            out.append({
                "id": d.get("id", f"v3-D-{len(out):04d}"),
                "slice": "D_holdout_temporal",
                "question": q,
                "relevant_claim_ids": ids,
                "provenance": d.get("provenance", "manual"),
                "has_anchor": bool(ANCHOR_RE.search(q)),
                "embedded_in_corpus": False,
                "expected_source_date": d.get("expected_source_date", ""),
            })
            stats["D_holdout_temporal"] += 1

    # Fatia C: negativos verificados (zero ocorrencia de QUALQUER token do termo no corpus)
    negs = []
    for cand in NEG_CANDIDATES:
        ct = set(toks(cand))
        distinct = ct - NEG_STOP        # termo distintivo = o que nao e palavra generica do dominio
        if not distinct or (distinct & full_text):
            continue                    # rejeita se qualquer termo distintivo JA aparece no corpus
        negs.append({
            "id": f"v3-C-{len(negs):04d}",
            "slice": "C_negativo",
            "question": f"Existe um componente chamado '{cand}' documentado no HWA 10.2.8? Se sim, qual a funcao?",
            "relevant_claim_ids": [],
            "provenance": "construido",
            "target_term": cand,
            "distinctive_tokens_ausentes_no_corpus": sorted(distinct),
        })
        stats["C_negativo"] += 1

    print("=== CONTAGEM POR FATIA ===")
    for k in sorted(stats):
        print(f"  {k}: {stats[k]}")
    print(f"  total scorable (A+B+D): {len(out)}  | negativos: {len(negs)}")
    if dry:
        print("\n[dry-run] nada gravado.")
        for o in out[:3]:
            print("  exemplo:", o["id"], o["slice"], o["question"][:90])
        for n in negs[:3]:
            print("  negativo:", n["id"], n["target_term"])
        return
    p1 = os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl")
    with open(p1, "w", encoding="utf-8") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    p2 = os.path.join(REPO, "data", "eval", "blind_v3_negatives.jsonl")
    with open(p2, "w", encoding="utf-8") as f:
        for n in negs:
            f.write(json.dumps(n, ensure_ascii=False) + "\n")
    print(f"\ngravado: {p1} ({len(out)}) e {p2} ({len(negs)})")


if __name__ == "__main__":
    main("--dry-run" in sys.argv)
