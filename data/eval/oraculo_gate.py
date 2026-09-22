#!/usr/bin/env python3
"""ANALISE DE ORACULO: existe sinal que separe onde a fusao densa GANHA de onde ela PERDE?

Por que oraculo primeiro: um gate so' e' possivel se houver uma caracteristica da CONSULTA
(disponivel ANTES de recuperar) que correlacione com "a fusao ajuda nesta pergunta". Se as
distribuicoes das perguntas-ganho e perguntas-perda forem indistinguiveis, nenhum gate
mecanico existe e o trabalho para aqui - sem gastar varredura de limiar.

Features medidas no estado `off` (o de producao), portanto disponiveis em tempo real e sem
vazamento do gabarito:
  - s1        score BM25 do top-1
  - margem    (s1 - s2) / s1, normalizada
  - conf      faixa de confianca derivada da margem (alta >= 0,177 / media >= 0,05)
  - en        a consulta NAO e' portuguesa (a ponte dispara)
  - n_id      tokens que parecem identificador literal (codigo, comando, versao)
  - n_tok     tamanho da consulta em tokens

Uso: python3 data/eval/oraculo_gate.py
"""
import json
import glob
import os
import re
import statistics as st
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "mcp_server"))
VERIF = os.environ.get("RAG_VERIF_DIR", "/tmp/ragexp/verif")

RE_ID = re.compile(r"[A-Z]{2,}\d+|\b\d+\.\d+|\b[A-Z]{3,}\b|\w*\d\w*")


def main():
    import tws_expert_mcp as mcp

    offs, fus = {}, {}
    for f in glob.glob(os.path.join(VERIF, "*_off.json")):
        d = json.load(open(f))
        offs[d["conjunto"]] = {x["pos"]: x["rank"] for x in d["ranks"]}
    for f in glob.glob(os.path.join(VERIF, "*_fuse.json")):
        d = json.load(open(f))
        fus[d["conjunto"]] = {x["pos"]: x["rank"] for x in d["ranks"]}

    CONJ = [("geral_70", "golden_qa_benchmark.jsonl"),
            ("mensagens", "golden_qa_messages_benchmark.jsonl"),
            ("virgem_expandido", "golden_qa_virgin_expanded.jsonl"),
            ("virgem+mensagens", "golden_qa_virgin_messages_expanded.jsonl"),
            ("virgem_INGLES", "golden_qa_virgin_en_benchmark.jsonl"),
            ("holdout_40", "holdout_40_test.jsonl"),
            ("holdout_qa_30", "blind_holdout_qa_30.jsonl"),
            ("realistico", "realistic_blind_holdout_30.jsonl"),
            ("pure_virgin", "pure_virgin_test_40.jsonl"),
            ("holdout_100", "holdout_100_unseen.jsonl")]

    linhas = []
    for nome, arq in CONJ:
        itens = [json.loads(l) for l in open(os.path.join(RAIZ, "data/eval", arq),
                                             encoding="utf-8") if l.strip()]
        for pos, o in enumerate(itens):
            if not (o.get("relevant_claim_ids") or []):
                continue
            q = o["question"]
            toks = re.findall(r"\w+", q.lower())
            base = mcp.search_bm25(toks, top_k=5)
            if not base:
                continue
            s1 = base[0]["score"]
            s2 = base[1]["score"] if len(base) > 1 else 0.0
            margem = (s1 - s2) / s1 if s1 > 0 else 0.0
            conf = ("alta" if margem >= mcp.FAIXA_ALTA
                    else "media" if margem >= mcp.FAIXA_MEDIA else "baixa")
            en = 1 if mcp._traduz(q) else 0
            linhas.append({
                "conjunto": nome, "pos": pos, "q": q,
                "off": offs[nome].get(pos), "fuse": fus[nome].get(pos),
                "s1": s1, "margem": margem, "conf": conf, "en": en,
                "n_id": len(RE_ID.findall(q)), "n_tok": len(toks),
            })

    n = len(linhas)
    def acerta(r, k=1):
        return r is not None and r <= k
    ganha = [x for x in linhas if acerta(x["fuse"]) and not acerta(x["off"])]
    perde = [x for x in linhas if acerta(x["off"]) and not acerta(x["fuse"])]
    neutro = [x for x in linhas if acerta(x["off"]) == acerta(x["fuse"])]
    print("n=%d | ganha@1 %d | perde@1 %d | neutro %d" % (n, len(ganha), len(perde), len(neutro)))
    print()
    print("=== as perguntas que a fusao GANHA sao distinguiveis das que PERDE? ===")
    print("  %-9s %14s %14s %14s" % ("feature", "ganha(med)", "perde(med)", "neutro(med)"))
    for feat in ("s1", "margem", "n_id", "n_tok"):
        print("  %-9s %14.4f %14.4f %14.4f"
              % (feat, st.median(x[feat] for x in ganha),
                 st.median(x[feat] for x in perde),
                 st.median(x[feat] for x in neutro)))
    print()
    print("  distribuicao de CONFIANCA (o candidato a gate mais obvio):")
    for grupo, nome_g in ((ganha, "ganha"), (perde, "perde"), (neutro, "neutro")):
        c = {k: sum(1 for x in grupo if x["conf"] == k) for k in ("alta", "media", "baixa")}
        tot = max(len(grupo), 1)
        print("    %-7s alta %3d (%4.1f%%) | media %3d (%4.1f%%) | baixa %3d (%4.1f%%)"
              % (nome_g, c["alta"], 100 * c["alta"] / tot, c["media"], 100 * c["media"] / tot,
                 c["baixa"], 100 * c["baixa"] / tot))
    print()
    print("  distribuicao de IDIOMA (en = ponte disparou):")
    for grupo, nome_g in ((ganha, "ganha"), (perde, "perde"), (neutro, "neutro")):
        e = sum(1 for x in grupo if x["en"])
        tot = max(len(grupo), 1)
        print("    %-7s en %3d/%d (%4.1f%%)" % (nome_g, e, len(grupo), 100 * e / tot))
    print()
    # separabilidade: AUC de cada feature para prever "ganha" entre (ganha U perde)
    print("  separabilidade (AUC para prever 'a fusao ganha', entre ganha U perde):")
    alvo = ganha + perde
    for feat in ("s1", "margem", "n_id", "n_tok"):
        pos = [x[feat] for x in ganha]
        neg = [x[feat] for x in perde]
        if not pos or not neg:
            continue
        auc = sum((1 if a > b else 0.5 if a == b else 0) for a in pos for b in neg) / (len(pos) * len(neg))
        print("    %-9s AUC %.3f%s" % (feat, auc, "  <- util" if abs(auc - 0.5) > 0.15 else ""))

    json.dump(linhas, open("/tmp/ragexp/oraculo_feats.json", "w"), ensure_ascii=False)


if __name__ == "__main__":
    main()
