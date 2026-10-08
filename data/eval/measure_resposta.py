#!/usr/bin/env python3
"""Primeiro benchmark de NIVEL-RESPOSTA do projeto (o que antecede: so' havia ranking).

POR QUE ISTO EXISTE. Todo numero do projeto era Hit@k/MRR - posicao do alvo no ranking. Mas
Hit@1 nao e' "a resposta esta certa": e' "o alvo chegou ao topo". Sao coisas diferentes, e a
diferenca importa para o requisito "responder sem alucinar". Nenhum benchmark media a RESPOSTA.

O QUE O SISTEMA ENTREGA. O MCP NAO gera texto: devolve a `claim` do corpus, VERBATIM, com
`claim_id`. Entao "alucinacao" aqui nao e' texto inventado - e' EVIDENCIA ERRADA no topo. A
garantia anti-alucinacao deste sistema e' estrutural (nao ha geracao livre) e e' conferivel:

  * `evidencia_verbatim` - a claim entregue existe, byte a byte, no corpus? (deve ser sempre
    True por construcao; se algum dia for False, houve invencao e isso e' alarme)
  * `suporte_lexical`  - a claim entregue compartilha termos de conteudo com a pergunta? Se
    NAO compartilha, o sistema esta' afirmando com evidencia que nao sustenta o pedido. E'
    um LIMITE INFERIOR de abstencoes indevidas (ver ressalva abaixo).

DESFECHOS por pergunta (mutuamente exclusivos, objetivo onde da'):
  acertou   - o claim entregue e' um dos relevantes (a evidencia sustenta a resposta certa)
  errou     - o alvo existe no topo amplo, mas o top-1 e' outro (recuperou, ranqueou errado)
  ausente   - o alvo NAO aparece nem no topo amplo (nao encontrou a evidencia)
  absteve   - nenhuma evidencia... (o sistema sempre devolve algo; reservado p/ futura abstencao)

RESSALVA HONESTA (nao vender como mais do que e'). `suporte_lexical` e' NECESSARIO mas NAO
SUFICIENTE para a resposta estar certa: uma claim com sobreposicao lexical ainda pode estar
errada. Logo ele e' um LIMITE INFERIOR do problema de abstencao, nao a taxa de alucinacao. A
taxa de alucinacao exata exige julgar a pertinencia da evidencia contra a pergunta, o que
requer um LLM - e este benchmark NAO chama LLM nenhum (roda offline, deterministico, sem
custo, sem chave). Fica `UNKNOWN` a taxa exata; fica MEDIDO o desfecho e o suporte lexical.

Uso:
    python3 data/eval/measure_resposta.py                        # pool 423
    python3 data/eval/measure_resposta.py --bench data/eval/rest_api_benchmark_ops_40.jsonl
    python3 data/eval/measure_resposta.py --limit 20             # sanity
"""
from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "mcp_server"))

POOL_PADRAO = os.path.join(RAIZ, "data/eval/decontaminated/pool423_reconstruido_2026-09-21.jsonl")
CORPUS_PADRAO = os.path.join(RAIZ, "data/export/tws_corpus_master_consolidated.jsonl")

# topo amplo: o suficiente para dizer "a recuperacao encontrou o alvo?" sem inflar o custo.
# Medido: apenas 1 das 423 perguntas tem alvo fora do corpus; "ausente" e' falha de ranking/
# cobertura lexical, nao lacuna de corpus.
TOPO_AMPLO = 50

STOP = set("""a o e de da do das dos em no na nos nas um uma uns umas para por com sem sob sobre
que qual quais quando como onde porque se ao aos ao à às pelo pela é sao são ser esta está estão
este esta esse essa isso aquilo seu sua seus suas meu minha nosso nossa ha há tem têm foi eram
the of and to in on for with is are be a an or as at by from this that these those it its
quaisquer qualquer outro outra mesmo mesma""".split())


def toks(txt):
    return {w for w in re.findall(r"\w+", (txt or "").lower()) if len(w) >= 4 and w not in STOP}


def suporte_lexical(claim, pergunta):
    tc, tp = toks(claim), toks(pergunta)
    if not tc:
        return 0.0
    return len(tc & tp) / len(tc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", default=POOL_PADRAO)
    ap.add_argument("--corpus", default=CORPUS_PADRAO)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--top-k", type=int, default=1, help="o que e' ENTREGUE (a resposta)")
    ap.add_argument("--out", default="/tmp/resposta.json")
    args = ap.parse_args()

    import tws_expert_mcp as mcp
    try:
        import tws_dense
    except Exception:  # noqa: BLE001
        tws_dense = None

    bench = [json.loads(l) for l in open(args.bench, encoding="utf-8") if l.strip()]
    if args.limit:
        bench = bench[: args.limit]
    corpus = {}
    for l in open(args.corpus, encoding="utf-8"):
        if l.strip():
            d = json.loads(l)
            corpus[d["claim_id"]] = d["claim"]

    def golds(o):
        v = o.get("relevant_claim_ids")
        return set(v if isinstance(v, list) else json.loads(v or "[]"))

    linhas, t0 = [], time.time()
    for o in bench:
        g = golds(o)
        if not g:
            continue
        res = mcp.handle_tool_call("tws_expert_search",
                                   {"query": o["question"], "top_k": max(args.top_k, TOPO_AMPLO)})
        achados = [x["claim_id"] for x in res.get("results", [])]
        entregue = achados[: args.top_k]
        top1 = entregue[0] if entregue else None
        no_topo = next((i + 1 for i, c in enumerate(achados) if c in g), None)

        if top1 in g:
            desfecho = "acertou"
        elif no_topo is not None:
            desfecho = "errou"
        else:
            desfecho = "ausente"

        claim_entregue = next((x.get("claim") for x in res.get("results", [])
                               if x["claim_id"] == top1), None)
        linhas.append({
            "id": o["id"], "top1": top1, "desfecho": desfecho, "pos_alvo": no_topo,
            "metodo": res.get("metodo", "recuperacao"),
            "evidencia_verbatim": (claim_entregue in corpus.values()) if claim_entregue else False,
            "suporte_lexical": round(suporte_lexical(claim_entregue, o["question"]), 4),
            "confianca": res.get("confianca"),
        })

    n = len(linhas)
    if not n:
        raise SystemExit("nenhuma pergunta com gabarito")
    dur = time.time() - t0

    def conta(d):
        return sum(1 for x in linhas if x["desfecho"] == d)

    acertou, errou, ausente = conta("acertou"), conta("errou"), conta("ausente")
    verbatim_ok = sum(1 for x in linhas if x["evidencia_verbatim"])
    # abstencao indevida: o sistema afirma (top-1) com evidencia que quase nao toca a pergunta
    sem_suporte = [x for x in linhas if x["suporte_lexical"] < 0.05]
    sup = [x["suporte_lexical"] for x in linhas]

    # A CONFIGURACAO entra no cabecalho: sem isso o numero nao e' interpretavel. Medido:
    # o denso so' esta' disponivel com torch+indice; sem eles, isto roda em lexical puro.
    # SMOKE TEST, nao presenca de arquivo. Medido nesta sessao: `disponivel()` devolve True
    # quando o indice existe e torch importa, mas o CARREGAMENTO do modelo pode falhar em
    # runtime (cache partido) - e ai' a run roda em BM25 puro enquanto o cabecalho diz
    # "denso disponivel". A unica prova de que o ramo denso esta' vivo e' ele devolver algo.
    def _denso_vivo():
        try:
            return bool(tws_dense and tws_dense.alinhado(d["claim_id"] for d in mcp.docs)
                        and tws_dense.busca("probe de disponibilidade", top_k=1))
        except Exception:  # noqa: BLE001
            return False

    denso_ok = _denso_vivo()
    denso_declarado = bool(tws_dense is not None and tws_dense.disponivel())
    print("=" * 78)
    print("BENCHMARK DE RESPOSTA (nivel-resposta) - %d perguntas" % n)
    if denso_declarado and not denso_ok:
        print("ATENCAO: denso DECLARADO disponivel mas o smoke test FALHOU - a run e' BM25 puro.")
    print("config: DENSE_MODE=%s | denso %s | corpus %d docs | RESTO_CLASS=%s"
          % (mcp.DENSE_MODE, "VIVO" if denso_ok else "AUSENTE (lexical puro)",
             len(mcp.docs), mcp.RESTO_CLASS))
    print("entrega: top_k=%d do MCP (o que o usuario recebe) | %.1f ms/pergunta"
          % (args.top_k, 1000 * dur / n))
    print("=" * 78)
    print("  acertou (evidencia == alvo) : %4d/%d (%5.1f%%)" % (acertou, n, 100 * acertou / n))
    print("  errou   (achou, ranqueou mal): %4d/%d (%5.1f%%)" % (errou, n, 100 * errou / n))
    print("  ausente (nao achou o alvo)  : %4d/%d (%5.1f%%)" % (ausente, n, 100 * ausente / n))
    print()
    print("  evidencia verbatim no corpus: %4d/%d (%5.1f%%)  <- garantia estrutural"
          % (verbatim_ok, n, 100 * verbatim_ok / n))
    print("  suporte lexical do top-1: mediana %.3f | min %.3f | max %.3f"
          % (statistics.median(sup), min(sup), max(sup)))
    print("  afirmou com suporte < 0,05 : %4d/%d (%5.1f%%)  <- LIMITE INFERIOR de abstencao"
          % (len(sem_suporte), n, 100 * len(sem_suporte) / n))
    print()
    print("  RESSALVA: suporte lexical e' necessario, NAO suficiente. A taxa exata de")
    print("  alucinacao exige julgar pertinencia (LLM) e fica UNKNOWN neste benchmark.")

    json.dump({"n": n, "top_k": args.top_k, "dense_mode": mcp.DENSE_MODE,
               "denso_disponivel": denso_ok, "corpus_docs": len(mcp.docs),
               "acertou": acertou, "errou": errou,
               "ausente": ausente, "evidencia_verbatim": verbatim_ok,
               "sem_suporte_lexical": len(sem_suporte),
               "suporte_mediana": round(statistics.median(sup), 4),
               "linhas": linhas},
              open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("\n  gravado em %s" % args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
