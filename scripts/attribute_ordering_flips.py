#!/usr/bin/env python3
"""FASE 1 - Atribuicao por componente das inversoes de ordenacao.

Pergunta que este script responde: nos quase-acertos (doc certo em rank 2-10), QUAL
componente do score fez o documento ERRADO vencer?

CONTROLE (duplo, obrigatorio):
  (1) a ordenacao instrumentada tem de reproduzir o @1 de producao (183/262);
  (2) o score instrumentado de CADA documento tem de ser IDENTICO ao de producao
      (max|diff| < 1e-9). Sem (2), a atribuicao seria de um scorer que nao e' o real.

Read-only: nao altera o avaliador, o corpus nem o lab.
"""
import sys, os, re, json, time, argparse
from collections import defaultdict, Counter

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
import evaluate_rag_benchmark as E

HWA_TERMS = ["sfinal", "jnextplan", "resetplan", "makeplan", "switchplan", "checksync", "composer",
             "conman", "planman", "joblog", "vartable", "rerun", "generic", "event1", "sbs", "opens",
             "limit", "securityutility", "resync", "twsobjectmonitor", "switcheventprocessor",
             "switchevtp", "helm", "chart", "kubernetes", "tebctl", "cwwkf0011i", "enretain", "wapl",
             "mmrresolve", "symnew", "conddep", "wa_pull_info", "baserecprompt", "aida", "carryforward"]

K1, B, AVG_DL = 1.2, 0.75, 60


def bm25_parts(query_tokens, doc_tokens, query_raw, doc_text, doc=None, avg_dl=AVG_DL):
    """Copia FIEL de compute_bm25, registrando o score apos cada etapa."""
    p = {}
    if not doc_tokens:
        return 0.0, {"vazio": 0.0}
    overlap = query_tokens.intersection(doc_tokens)
    if not overlap:
        return 0.0, {"sem_overlap": 0.0}
    score = 0.0
    dl = len(doc_tokens)
    doc_lower = doc_text.lower()
    denom = (1.0 + K1 * (1.0 - B + B * (dl / avg_dl)))

    # 1. base + boost HWA (separados)
    base_sum = 0.0
    hwa_extra = 0.0
    for t in sorted(overlap):
        unit = (K1 + 1) / denom
        if any(term in t for term in HWA_TERMS):
            hwa_extra += 3.0 * unit
            base_sum += 1.0 * unit
        else:
            base_sum += 1.0 * unit
    score = base_sum + hwa_extra
    p["bm25_base"] = base_sum
    p["hwa_boost"] = hwa_extra

    # 1.1 frases operacionais
    q_low = query_raw.lower()
    if "processador de eventos" in q_low or "event processor" in q_low:
        if "switcheventprocessor" in doc_lower or "switchevtp" in doc_lower:
            score += 15.0
            p["frase_operacional"] = 15.0

    # 2. codigos de erro exatos
    codes_in_query = re.findall(r"aws[a-z]{3}[0-9]{3}[iew]", query_raw.lower())
    c15 = 0.0
    for code in codes_in_query:
        if code in doc_lower:
            c15 += 15.0
    if c15:
        score += c15
        p["codigo_erro_+15"] = c15

    # 2.1 familia de mensagem AWS
    if doc and doc.get("type") == "message_catalog":
        doc_fam = re.search(r"aws([a-z]{3})", doc.get("id", "").lower())
        if doc_fam:
            for fam in E.detect_families(query_raw):
                if fam.lower() == doc_fam.group(1):
                    score += E.FAMILY_BOOST
                    p["familia_aws"] = E.FAMILY_BOOST
                    break

    pre_type = score
    if doc:
        dtype = doc.get("type")
        mult = 1.0
        if dtype == "canonical_claim":
            mult = 1.25
        elif dtype == "lab_evidence":
            mult = 1.20
        elif dtype == "ragflow_runbook_chunk":
            mult = 1.15
        elif dtype == "message_catalog":
            mult = 1.10
        score *= mult
        p["tipo_x%.2f" % mult] = score - pre_type

        # token no id
        id_add = 0.0
        for token in sorted(query_tokens):
            if token.isalnum() and len(token) > 3 and token in (doc.get("id") or "").lower():
                id_add += 4.0
        if id_add:
            score += id_add
            p["token_no_id_+4"] = id_add

        # titulo
        if doc.get("title") and query_tokens.intersection(E.tokenize(doc["title"])):
            pre = score
            score *= 1.15
            p["titulo_x1.15"] = score - pre
        # nome do runbook
        if doc.get("runbook") and doc.get("runbook").replace(".md", "").replace("-", "") in query_raw.lower().replace("-", ""):
            pre = score
            score *= 1.1
            p["nome_runbook_x1.1"] = score - pre

        # 4. RAGFlow
        if dtype == "ragflow_runbook_chunk":
            meta = doc.get("metadata", {})
            a = 0.0
            for cmd in meta.get("commands", []):
                if cmd.lower() in query_raw.lower():
                    a += 3.5
            if a:
                score += a
                p["ragflow_cmd_+3.5"] = a
            a = 0.0
            for c_code in meta.get("aws_codes", []):
                if c_code.lower() in query_raw.lower():
                    a += 12.0
            if a:
                score += a
                p["ragflow_codigo_+12"] = a
            if doc.get("path") and query_tokens.intersection(E.tokenize(doc["path"])):
                pre = score
                score *= 1.2
                p["breadcrumbs_x1.2"] = score - pre
    return score, p


def ss_parts(query_raw, s_in, doc, top_n=20):
    """Copia FIEL da parte por-candidato de second_stage_rerank, com breakdown."""
    p = {}
    clean_words = [w.strip(".,;:?!'\"()[]{}").lower() for w in re.findall(r"[A-Za-z0-9_\-]+", query_raw) if len(w) > 2]
    unique_q_terms = set(clean_words) - {"qual", "quais", "como", "onde", "por", "que", "para", "com",
                                         "dos", "das", "uma", "não", "mais"}
    bigrams = E.extract_ngrams(clean_words, 2)
    trigrams = E.extract_ngrams(clean_words, 3)

    text_lower = doc["text"].lower()
    title_lower = (doc.get("title") or "").lower()
    score = s_in

    a = 0.0
    for bg in bigrams:
        if len(bg) > 6 and bg in text_lower:
            a += 8.0
        if len(bg) > 6 and bg in title_lower:
            a += 12.0
    if a:
        score += a
        p["ss_bigram"] = a

    a = 0.0
    for tg in trigrams:
        if len(tg) > 10 and tg in text_lower:
            a += 15.0
        if len(tg) > 10 and tg in title_lower:
            a += 20.0
    if a:
        score += a
        p["ss_trigram"] = a

    doc_tokens = doc["tokens"]
    if unique_q_terms:
        covered = len(unique_q_terms.intersection(doc_tokens))
        cov = covered / len(unique_q_terms)
        if cov >= 0.80:
            pre = score
            score *= 1.25
            p["ss_cobertura_x1.25"] = score - pre
        elif cov >= 0.60:
            pre = score
            score *= 1.12
            p["ss_cobertura_x1.12"] = score - pre

    doc_id_lower = doc.get("id", "").lower()
    ignore = {"opcao", "global", "regra", "documentada", "ambiente", "distribuida", "distributed",
              "workload", "automation", "sobre", "conforme", "oficial", "documentacao", "neste",
              "para", "como"}
    a = 0.0
    for term in sorted(unique_q_terms):
        ct = term.replace("-", "").replace("_", "")
        if len(ct) >= 5 and ct not in ignore:
            if ct in doc_id_lower.replace("-", "").replace("_", ""):
                a += 32.0
        if re.match(r"^[a-z]{3,6}[0-9]{3,5}[a-z]?$", ct):
            if ct in doc_id_lower.replace("-", ""):
                if "trouble" in doc_id_lower or "messages" in doc_id_lower or "incident" in doc_id_lower:
                    a += 55.0
                else:
                    a += 45.0
            elif ct in text_lower:
                a += 25.0
        nm = re.search(r"[0-9]{3,5}[a-z]$", ct)
        if nm and nm.group(0) in doc_id_lower:
            a += 25.0
    if a:
        score += a
        p["ss_entidade_id"] = a

    cli_pairs = [("composer", "add"), ("composer", "extract"), ("composer", "delete"), ("composer", "modify"),
                 ("conman", "start"), ("conman", "stop"), ("conman", "fence"), ("conman", "limit"),
                 ("conman", "confirm"), ("conman", "release"), ("conman", "rerun"), ("conman", "showjobs"),
                 ("conman", "status"), ("conman", "switcheventprocessor"),
                 ("planman", "showinfo"), ("planman", "checksync"), ("planman", "resync"), ("planman", "resetplan"),
                 ("optman", "ls"), ("optman", "chg"), ("optman", "cf")]
    qrl = query_raw.lower()
    a = 0.0
    for cmd, sub in cli_pairs:
        if cmd in qrl and sub in qrl:
            if (cmd in doc_id_lower and sub in doc_id_lower) or (f"{cmd} {sub}" in text_lower[:200]):
                a += 35.0
    if a:
        score += a
        p["ss_par_cli"] = a
    return score, p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", default=os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl"))
    a = ap.parse_args()

    t0 = time.time()
    docs = E.load_documents()
    bench = [json.loads(l) for l in open(a.bench) if l.strip()]
    print(f"[atrib] n_docs={len(docs)} perguntas={len(bench)}  ({time.time()-t0:.0f}s)", flush=True)

    hit1 = 0
    hit1_inst = 0
    maxdiff = 0.0
    cases = []
    rank_hist = Counter()

    for b in bench:
        q = b.get("question", "")
        exp = set(b.get("relevant_claim_ids", []))
        rb = b.get("runbook_ref")
        qt = E.tokenize(q)

        # ---- passada de PRODUCAO (controle 1) ----
        scored = []
        for d in docs:
            s = E.compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
            if s > 0:
                scored.append([s, d])
        scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        div = []
        seen = defaultdict(int)
        for s, d in scored:
            k = d.get("runbook") or d.get("type")
            if d.get("type") == "ragflow_runbook_chunk" and seen[k] >= 2:
                s *= 0.65
            seen[k] += 1
            div.append((s, d))
        div.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        pos = E.second_stage_rerank(q, div, top_n=20)

        def match(d):
            if d["id"] in exp:
                return True
            if d["type"] == "aws_message":
                for e in exp:
                    if d.get("code", "").lower() in e.lower():
                        return True
            elif (d["type"] == "ragflow_runbook_chunk" or d["type"] == "runbook_section") and rb and d.get("runbook") == rb:
                oc = len(qt.intersection(d["tokens"]))
                if oc >= 2 and (oc / max(1, len(qt))) >= 0.25:
                    return True
            return False

        r_prod = next((i + 1 for i, d in enumerate(pos) if match(d)), None)
        if r_prod == 1:
            hit1 += 1
        rank_hist[r_prod if r_prod and r_prod <= 10 else (">10" if r_prod else "miss")] += 1

        # ---- passada INSTRUMENTADA (controle 2) ----
        # ATENCAO: ids NAO sao unicos no corpus (~117 duplicados) -> indexar/comparar por
        # IDENTIDADE do objeto (id()), nunca pelo campo "id". Foi exatamente esse o falso
        # "DIVERGIU" da primeira rodada.
        inscored = []
        for d in docs:
            s, p = bm25_parts(qt, d["tokens"], q, d["text"], doc=d)
            s_p = E.compute_bm25(qt, d["tokens"], q, d["text"], doc=d)
            maxdiff = max(maxdiff, abs(s_p - s))
            if s > 0:
                inscored.append([s, d])
        inscored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))

        idiv = []
        seen2 = defaultdict(int)
        for s, d in inscored:
            k = d.get("runbook") or d.get("type")
            if d.get("type") == "ragflow_runbook_chunk" and seen2[k] >= 2:
                s *= 0.65
            seen2[k] += 1
            idiv.append((s, d))
        idiv.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
        ipos = E.second_stage_rerank(q, idiv, top_n=20)
        r_inst = next((i + 1 for i, d in enumerate(ipos) if match(d)), None)
        if r_inst == 1:
            hit1_inst += 1

        if r_inst != r_prod:
            print(f"[atrib] AVISO divergencia de rank em {b.get('id')}: prod={r_prod} inst={r_inst}")

        # ---- se e' quase-acerto, decompoe ----
        if r_inst and 2 <= r_inst <= 10:
            certo = ipos[r_inst - 1]
            errado = ipos[0]
            div_score = {id(d): s for s, d in idiv}
            s_div_c = div_score.get(id(certo), 0.0)
            s_div_w = div_score.get(id(errado), 0.0)
            f_c, pc = ss_parts(q, s_div_c, certo)
            f_w, pw = ss_parts(q, s_div_w, errado)
            cases.append({
                "qid": b.get("id"), "question": q[:90],
                "rank": r_inst,
                "certo_id": certo["id"], "certo_tipo": certo["type"], "certo_score": round(f_c, 3),
                "errado_id": errado["id"], "errado_tipo": errado["type"], "errado_score": round(f_w, 3),
                "s_div_certo": round(s_div_c, 3), "s_div_errado": round(s_div_w, 3),
                "demotado": s_div_c > s_div_w,
                "parts_certo": {k: round(v, 3) for k, v in pc.items()},
                "parts_errado": {k: round(v, 3) for k, v in pw.items()},
            })

    print(f"\n[atrib] CONTROLE 1 (ordenacao): prod @1 = {hit1}/{len(bench)}  |  instrumentada @1 = {hit1_inst}/{len(bench)}")
    print(f"[atrib] CONTROLE 2 (fidelidade do score): max|diff| = {maxdiff:.3e}  -> {'IDENTICO' if maxdiff < 1e-9 else 'DIVERGIU'}")
    print(f"[atrib] histograma de rank (prod): {dict(sorted(rank_hist.items(), key=lambda x: str(x[0])))}")
    print(f"[atrib] quase-acertos decompostos: {len(cases)}")

    dem = [c for c in cases if c["demotado"]]
    print(f"[atrib]   -> DEMOTADOS pelo 2o estagio (score maior e rank pior): {len(dem)}")
    print(f"[atrib]   -> erro real do scorer: {len(cases)-len(dem)}")

    # qual componente da' a margem ao ERRADO?
    print("\n=== componente com maior delta A FAVOR do documento ERRADO (por caso) ===")
    comp_win = Counter()
    for c in cases:
        keys = set(c["parts_certo"]) | set(c["parts_errado"])
        deltas = {k: c["parts_errado"].get(k, 0.0) - c["parts_certo"].get(k, 0.0) for k in keys}
        top = max(deltas.items(), key=lambda x: x[1]) if deltas else ("(sem_componente)", 0.0)
        comp_win[top[0]] += 1
    for k, v in comp_win.most_common():
        print(f"  {k:24s} {v:3d} caso(s)  ({v/len(cases)*100:.0f}%)")

    print("\n=== o mesmo, SO' nos demotados ===")
    comp_win_d = Counter()
    for c in dem:
        keys = set(c["parts_certo"]) | set(c["parts_errado"])
        deltas = {k: c["parts_errado"].get(k, 0.0) - c["parts_certo"].get(k, 0.0) for k in keys}
        top = max(deltas.items(), key=lambda x: x[1]) if deltas else ("(sem_componente)", 0.0)
        comp_win_d[top[0]] += 1
    for k, v in comp_win_d.most_common():
        print(f"  {k:24s} {v:3d} caso(s)")

    print("\n=== delta medio por componente (errado - certo), casos com |delta|>0 ===")
    agg = defaultdict(lambda: [0.0, 0])
    for c in cases:
        keys = set(c["parts_certo"]) | set(c["parts_errado"])
        for k in keys:
            dv = c["parts_errado"].get(k, 0.0) - c["parts_certo"].get(k, 0.0)
            if abs(dv) > 1e-9:
                agg[k][0] += dv
                agg[k][1] += 1
    for k, (s, n) in sorted(agg.items(), key=lambda x: -abs(x[1][0])):
        print(f"  {k:24s} soma={s:9.2f}  n={n:3d}  media={s/n:8.2f}")

    out = os.path.join(REPO, "data", "eval", "ordering_attribution.json")
    json.dump({"n_docs": len(docs), "hit1_prod": hit1, "hit1_inst": hit1_inst,
               "maxdiff": maxdiff, "n_cases": len(cases), "n_demotados": len(dem),
               "cases": cases}, open(out, "w"))
    print(f"\n[atrib] gravado {out}  ({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main()
