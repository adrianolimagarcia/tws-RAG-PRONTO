"""O EXPERIMENTO QUE FALTAVA: fusao ASSIMETRICA guiada por confianca.

ESTADO DA ARTE (ja' medido por este projeto, evidencia de 2026-09-17):
  recall@50: lex 83,5% | denso 83,8% | UNIAO 93,8%  (fatia D: denso 93,8%, uniao 100%)
  mas a fusao RRF de peso igual DESTROI a fatia com ancora: A 97 -> 57 no @1.
  RRF cego: 149/262 @1 contra 183/262 do lexical.
  Conclusao registrada: "o denso JA' acha 93,8% da fatia D - o trabalho que resta nao e'
  trazer candidato, e' ORDENAR."

A PERGUNTA: a fusao de peso igual falha porque nao sabe QUANDO usar cada ramo. Mas nos
temos o sinal de confianca medido (margem normalizada, AUC 0,842) que diz exatamente
onde o lexical e' cego. A HIPOTESE: em consulta de confianca ALTA, o lexical esta' certo
e o denso so' atrapalha -> nao funde. Em media/baixa, o lexical esta' perdido -> o denso
e' a unica chance -> funde. Fundir de forma ASSIMETRICA, nao cega.

Baseline: o lexical do harness (o que a producao executa).
"""
import os
import sys
import json
from collections import defaultdict

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
sys.path.insert(0, os.path.join(REPO, "data", "eval"))
sys.path.insert(0, REPO)
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["RAG_INGEST_REST_API"] = "1"
os.environ["RAG_DENSE_MASK_TO_CORPUS"] = "1"
os.environ["RAG_DENSE_INDEX"] = os.path.join(REPO, "data/indexes/corpus_bge_m3_v6.pt")
os.environ["RAG_DENSE_META"] = os.path.join(REPO, "data/indexes/corpus_docs_meta_v6.json")

import torch  # noqa: E402
import evaluate_rag_benchmark as eng  # noqa: E402
from rag_core.lexical import tokenize, compute_bm25  # noqa: E402

BENCH = "/tmp/ragexp/attrib3/pool.jsonl"
LIMIAR_ALTA, LIMIAR_MEDIA = 0.177, 0.05

docs = eng.load_documents()
por_id = {d["id"]: d for d in docs}
corpus_ids = set(por_id)
bench = [json.loads(l) for l in open(BENCH, encoding="utf-8") if l.strip()]
print("corpus: %d docs | benchmark: %d perguntas" % (len(docs), len(bench)))


def acha_rank(seq_ids, expected_cids):
    """posicao (1-based) do primeiro doc que casa; None se nao achar. Replica o harness."""
    for i, did in enumerate(seq_ids, 1):
        if did in expected_cids:
            return i
        d = por_id.get(did)
        if d is not None and d.get("type") == "aws_message":
            for ec in expected_cids:
                if d.get("code", "").lower() in ec.lower():
                    return i
    return None


# ---------------- PASSO 1: lexical + denso por pergunta ----------------
print("\n[1/2] rodando lexical (baseline do harness)...")
dados = []
qtextos = []
for b in bench:
    q = b.get("question", "")
    exp = set(b.get("relevant_claim_ids", []) or [])
    toks = tokenize(q)
    scored = []
    for d in docs:
        s = compute_bm25(toks, d["tokens"], q, d["text"], doc=d)
        if s > 0:
            scored.append((s, d))
    scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    lex_ids = [d["id"] for _, d in scored]
    s1 = scored[0][0] if scored else 0.0
    s2 = scored[1][0] if len(scored) > 1 else 0.0
    margem = (s1 - s2) / s1 if s1 > 0 else 0.0
    dados.append({"q": q, "exp": exp, "lex": lex_ids, "margem": margem})
    qtextos.append(q)

print("[2/2] encodando as %d queries no BGE-M3 (CPU)..." % len(qtextos))
# Inicializacao propria: o cache do projeto tem config.json e model.safetensors em snapshots
# DIFERENTES, entao o _dense_init do harness nao resolve. Aqui uso /tmp/ragexp/bge-m3 (os
# arquivos reunidos) - validado contra o indice v6 com cos=1.00000.
import torch  # noqa: E402
import torch.nn.functional as F  # noqa: E402
from transformers import AutoModel, AutoTokenizer  # noqa: E402

_tok = AutoTokenizer.from_pretrained("/tmp/ragexp/bge-m3")
_mod = AutoModel.from_pretrained("/tmp/ragexp/bge-m3", dtype=torch.float32).eval()
_matriz = torch.load(os.path.join(REPO, "data/indexes/corpus_bge_m3_v6.pt"),
                     map_location="cpu", weights_only=False).float()
_ids = json.load(open(os.path.join(REPO, "data/indexes/corpus_docs_meta_v6.json")))
print("   indice: %s  meta: %d ids" % (tuple(_matriz.shape), len(_ids)))

denso = []
with torch.no_grad():
    for i in range(0, len(qtextos), 16):
        enc = _tok(qtextos[i:i + 16], padding=True, truncation=True,
                   max_length=128, return_tensors="pt")
        h = _mod(**enc).last_hidden_state[:, 0, :]
        qe = F.normalize(h, p=2, dim=1).float()
        sc = torch.mm(qe, _matriz.T)
        for j in range(sc.shape[0]):
            row = sc[j].clone()
            for k, did in enumerate(_ids):
                if did not in corpus_ids:
                    row[k] = float("-inf")
            top = torch.topk(row, k=60).indices.tolist()
            denso.append([_ids[t] for t in top if row[t] > float("-inf")])
        print("   %d/%d" % (min(i + 16, len(qtextos)), len(qtextos)), flush=True)
for dd, dn in zip(dados, denso):
    dd["dense"] = dn


# ---------------- PASSOS 3+: politicas ----------------
def faixa(m):
    return "alta" if m >= LIMIAR_ALTA else ("media" if m >= LIMIAR_MEDIA else "baixa")


def funde(lex, dense, w_dense, top=15):
    """RRF: peso w_dense no denso, (2-w_dense) no lexical (mesma escala do harness)."""
    rrf = {}
    for r, did in enumerate(dense, 1):
        rrf[did] = rrf.get(did, 0.0) + w_dense / (60.0 + r)
    for r, did in enumerate(lex, 1):
        rrf[did] = rrf.get(did, 0.0) + (2.0 - w_dense) / (60.0 + r)
    return sorted(rrf, key=lambda x: (-rrf[x], str(x)))[:top]


def avalia(nome, seq_por_pergunta):
    h1 = sum(1 for r in seq_por_pergunta if r == 1)
    h5 = sum(1 for r in seq_por_pergunta if r is not None and r <= 5)
    h15 = sum(1 for r in seq_por_pergunta if r is not None and r <= 15)
    rr = [1.0 / r if r else 0.0 for r in seq_por_pergunta]
    n = len(seq_por_pergunta)
    return {"pol": nome, "h1": h1, "h5": h5, "h15": h15,
            "mrr": sum(rr) / n, "n": n}


politicas = {}

# L: lexical puro (baseline)
politicas["L: lexical (baseline)"] = [acha_rank(dd["lex"][:15], dd["exp"]) for dd in dados]
# D: denso puro
politicas["D: denso puro"] = [acha_rank(dd["dense"][:15], dd["exp"]) for dd in dados]
# RRF de peso igual (o que a evidencia diz que piora)
politicas["RRF cego w=1.0"] = [acha_rank(funde(dd["lex"], dd["dense"], 1.0), dd["exp"]) for dd in dados]

# ASSIMETRICA: funde so' onde o lexical nao tem confianca alta
for w in (0.6, 0.8, 1.0, 1.2, 1.4):
    seq = []
    for dd in dados:
        if faixa(dd["margem"]) == "alta":
            seq.append(acha_rank(dd["lex"][:15], dd["exp"]))
        else:
            seq.append(acha_rank(funde(dd["lex"], dd["dense"], w), dd["exp"]))
    politicas["ASSIM: alta=lex, resto=RRF w=%.1f" % w] = seq

# ASSIMETRICA v2: sempre lexical no topo, denso so' preenche as vagas de baixo
def preenche(lex, dense, n_lex=5, top=15, w=0.8):
    cabeca = lex[:n_lex]
    resto = [x for x in funde(lex, dense, w, top=60) if x not in set(cabeca)]
    return (cabeca + resto)[:top]


for nl in (3, 5, 7):
    seq = []
    for dd in dados:
        if faixa(dd["margem"]) == "alta":
            seq.append(acha_rank(dd["lex"][:15], dd["exp"]))
        else:
            seq.append(acha_rank(preenche(dd["lex"], dd["dense"], n_lex=nl), dd["exp"]))
    politicas["ASSIM v2: alta=lex, resto=lex%d+denso" % nl] = seq

# SO' denso onde o lexical e' cego (margem ~0), lexical em todo o resto
for lim in (0.001, 0.01, 0.03):
    seq = []
    for dd in dados:
        if dd["margem"] < lim:
            seq.append(acha_rank(funde(dd["lex"], dd["dense"], 0.8), dd["exp"]))
        else:
            seq.append(acha_rank(dd["lex"][:15], dd["exp"]))
    politicas["ASSIM v3: margem<%.3f -> funde" % lim] = seq

print()
print("=" * 92)
print("%-42s %12s %12s %12s %10s" % ("politica", "Hit@1", "Hit@5", "Hit@15", "MRR"))
print("=" * 92)
res = [avalia(k, v) for k, v in politicas.items()]
base = res[0]
for r in res:
    marca = ""
    if r["h1"] > base["h1"]:
        marca = "  <== +%d" % (r["h1"] - base["h1"])
    elif r["h1"] < base["h1"]:
        marca = "  <== %d" % (r["h1"] - base["h1"])
    print("%-42s %5d/%d %5d/%d %5d/%d %10.4f%s"
          % (r["pol"], r["h1"], r["n"], r["h5"], r["n"], r["h15"], r["n"], r["mrr"], marca))

# diagnostico: a hipotese se sustenta por faixa?
print()
print("POR FAIXA (a hipotese diz: denso ajuda em media/baixa, atrapalha em alta)")
print("  %-10s %6s %10s %10s %10s" % ("faixa", "n", "L hit@1", "D hit@1", "RRF hit@1"))
for f in ("alta", "media", "baixa"):
    idx = [i for i, dd in enumerate(dados) if faixa(dd["margem"]) == f]
    if not idx:
        continue
    l = sum(1 for i in idx if politicas["L: lexical (baseline)"][i] == 1)
    dn = sum(1 for i in idx if politicas["D: denso puro"][i] == 1)
    rr = sum(1 for i in idx if politicas["RRF cego w=1.0"][i] == 1)
    print("  %-10s %6d %4d (%3.0f%%) %4d (%3.0f%%) %4d (%3.0f%%)"
          % (f, len(idx), l, 100 * l / len(idx), dn, 100 * dn / len(idx), rr, 100 * rr / len(idx)))

json.dump({"dados": [{k: (list(v) if isinstance(v, set) else v) for k, v in dd.items()} for dd in dados],
           "politicas": {k: v for k, v in politicas.items()}},
          open("/tmp/ragexp/fusao_resultado.json", "w"), ensure_ascii=False)
print("\nsalvo /tmp/ragexp/fusao_resultado.json")
