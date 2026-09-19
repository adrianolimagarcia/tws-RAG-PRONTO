#!/usr/bin/env python3
"""Gate de promocao do RAG v4 - implementa os 11 criterios do runbook (§17).

Regra: NAO existe score unico que promova uma configuracao. O gate avalia cada
criterio e o veredito final e' o PIOR criterio, nunca a media.

Vereditos possiveis (runbook §16):
  ACCEPTED      ganho util + sem regressao critica + controles passam
  REJECTED      regressao material
  INCONCLUSIVE  efeito pequeno / IC95% cruza zero / amostra insuficiente
  INVALID       controle, corpus, indice ou leakage falhou

Criterios que dependem de artefato que ainda nao existe (sealed holdout, suite de
hard negatives, medicao de latencia) sao reportados UNKNOWN - e UNKNOWN NAO promove.
Fail-closed: na duvida, o veredito e' pior, nunca melhor.

Uso:
  # so' os controles (sem A/B)
  scripts/gate_rag_v4.py --summary data/eval/eval_summary.json

  # comparacao A -> B com estatistica
  scripts/gate_rag_v4.py --run-a /tmp/a.json --run-b /tmp/b.json
"""

from __future__ import annotations

import argparse
import json
import random
import statistics
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# Controle obrigatorio do blind v3 com o corpus congelado (runbook, Regra zero).
# NAO e' o w=0.0 da varredura: zerar o peso denso ainda passa pelo caminho hibrido
# e pelo reranker (@10 217 vs 218). Este e' o lexical puro.
CONTROLE = {
    "n_docs": 6732,
    "total": 262,
    "at_1": "172/262",
    "at_10": "218/262",
    "at_15": "221/262",
    "mrr": 0.7134,
}

BOOTSTRAP_N = 10000
SEED = 20260919


def carrega_summary(caminho: Path) -> dict:
    d = json.loads(caminho.read_text(encoding="utf-8"))
    det = d.get("details") or []
    return {
        "n": d.get("total") or len(det),
        "at_1": d.get("hit_rate_at_1"),
        "at_10": d.get("hit_rate_at_10"),
        "mrr": d.get("mrr"),
        "por_qid": {str(x.get("id")): x for x in det},
        "cru": d,
    }


def hit15(detail: dict) -> int:
    """Binario: a pergunta tem pelo menos um acerto na janela de 15?"""
    r = detail.get("rank")
    if r is None:
        return 0
    if isinstance(r, (list, tuple)):
        return 1 if any(isinstance(x, int) and x <= 15 for x in r) else 0
    try:
        return 1 if int(r) <= 15 else 0
    except (TypeError, ValueError):
        return 0


def rr(detail: dict) -> float:
    r = detail.get("rank")
    if isinstance(r, (list, tuple)):
        r = r[0] if r else None
    if r is None:
        return 0.0
    try:
        v = int(r)
        return 1.0 / v if v > 0 else 0.0
    except (TypeError, ValueError):
        return 0.0


def mcnemar(a: list[int], b: list[int]) -> dict:
    """McNemar exato para metricas binarias pareadas (hit@15 A vs B)."""
    b01 = sum(1 for x, y in zip(a, b) if x == 0 and y == 1)
    b10 = sum(1 for x, y in zip(a, b) if x == 1 and y == 0)
    n = b01 + b10
    if n == 0:
        return {"b01": 0, "b10": 0, "p": 1.0, "nota": "sem discordancias"}
    # binomial exata, p=0.5, bicaudal
    k = min(b01, b10)
    from math import comb
    p = 2.0 * sum(comb(n, i) for i in range(0, k + 1)) / (2.0 ** n)
    return {"b01": b01, "b10": b10, "p": min(1.0, p)}


def bootstrap_pareado(a: list[float], b: list[float], n: int = BOOTSTRAP_N,
                       seed: int = SEED) -> dict:
    """Bootstrap pareado da diferenca de medias, com IC95%."""
    if not a or len(a) != len(b):
        return {"delta": None, "ic95": None, "nota": "amostra vazia ou desalinhada"}
    rnd = random.Random(seed)
    N = len(a)
    deltas = []
    for _ in range(n):
        idx = [rnd.randrange(N) for _ in range(N)]
        deltas.append(statistics.mean(b[i] - a[i] for i in idx))
    deltas.sort()
    lo = deltas[int(0.025 * n)]
    hi = deltas[int(0.975 * n)]
    real = statistics.mean(y - x for x, y in zip(a, b))
    return {"delta": real, "ic95": [lo, hi], "cruza_zero": lo <= 0.0 <= hi}


def roda(cmd: list[str]) -> tuple[int, str]:
    p = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--summary", default=str(REPO / "data" / "eval" / "eval_summary.json"))
    ap.add_argument("--run-a")
    ap.add_argument("--run-b")
    ap.add_argument("--pular-instrumentos", action="store_true",
                    help="nao reexecuta leakage/paridade (usa so' os summaries)")
    args = ap.parse_args()

    crit: dict[str, dict] = {}

    # --- 1. controle reproduz exatamente -----------------------------------
    try:
        s = carrega_summary(Path(args.summary))
        ok = (s["n"] == CONTROLE["total"] and s["mrr"] is not None
              and abs(s["mrr"] - CONTROLE["mrr"]) < 1e-4)
        detalhe = f"n={s['n']} MRR={s['mrr']}"
        # n=262 com MRR batendo e' o sinal do blind v3; o corpus e' conferido a parte
        crit["controle_reproduz"] = {"estado": "PASS" if ok else "FAIL", "detalhe": detalhe}
    except Exception as e:  # noqa: BLE001
        crit["controle_reproduz"] = {"estado": "FAIL", "detalhe": f"erro: {e}"}

    # --- 2. corpus/index manifest ------------------------------------------
    idx = REPO / "data" / "indexes" / "corpus_bge_m3_v2.pt"
    crit["manifest_corpus_indice"] = {
        "estado": "UNKNOWN",
        "detalhe": f"indice denso presente={idx.exists()}; manifest por execucao ainda nao existe (Fase 0)",
    }

    # --- 3. leakage scan PASS ----------------------------------------------
    if args.pular_instrumentos:
        crit["leakage_scan"] = {"estado": "UNKNOWN", "detalhe": "instrumentos pulados"}
    else:
        rc, out = roda([sys.executable, "scripts/audit_eval_leakage.py",
                        "--json", "/tmp/gate_leakage.json"])
        veredito = "PASS" if rc == 0 else "FAIL"
        ult = [ln for ln in out.splitlines() if "VEREDITO" in ln]
        crit["leakage_scan"] = {"estado": veredito,
                                "detalhe": ult[-1].strip() if ult else f"rc={rc}"}

    # --- 9. producao/evaluator ranking identico ----------------------------
    if args.pular_instrumentos:
        crit["paridade_producao"] = {"estado": "UNKNOWN", "detalhe": "instrumentos pulados"}
    else:
        rc, out = roda([sys.executable, "scripts/measure_prod_eval_parity.py",
                        "--top", "15", "--json", "/tmp/gate_paridade.json"])
        linhas = [ln.strip() for ln in out.splitlines() if "paridade EXATA" in ln]
        exatos = linhas[-1].split(":")[-1].strip() if linhas else "?"
        crit["paridade_producao"] = {
            "estado": "PASS" if rc == 0 else "FAIL",
            "detalhe": f"paridade exata {exatos} (precisa 262/262)",
        }

    # --- A/B: estatistica (§16) --------------------------------------------
    if args.run_a and args.run_b:
        A = carrega_summary(Path(args.run_a))
        B = carrega_summary(Path(args.run_b))
        comuns = sorted(set(A["por_qid"]) & set(B["por_qid"]))
        hA = [hit15(A["por_qid"][q]) for q in comuns]
        hB = [hit15(B["por_qid"][q]) for q in comuns]
        rA = [rr(A["por_qid"][q]) for q in comuns]
        rB = [rr(B["por_qid"][q]) for q in comuns]
        mc = mcnemar(hA, hB)
        bs = bootstrap_pareado(rA, rB)
        ganhos = sum(1 for x, y in zip(hA, hB) if x == 0 and y == 1)
        perdas = sum(1 for x, y in zip(hA, hB) if x == 1 and y == 0)
        empates = len(comuns) - ganhos - perdas
        est = {
            "n_pareado": len(comuns),
            "hit15_ganhos_perdas_empates": [ganhos, perdas, empates],
            "mcnemar": mc,
            "mrr_bootstrap": bs,
        }
        print("=== A/B (§16) ===")
        print(f"  n pareado: {len(comuns)}  ganhos/perdas/empates: {ganhos}/{perdas}/{empates}")
        print(f"  McNemar p={mc['p']:.4f}  (b01={mc['b01']} b10={mc['b10']})")
        if bs["delta"] is not None:
            print(f"  MRR delta={bs['delta']:+.4f} IC95=[{bs['ic95'][0]:+.4f},{bs['ic95'][1]:+.4f}]"
                  f"{' CRUZA ZERO' if bs['cruza_zero'] else ''}")
        crit["ab_estatistica"] = {"estado": "UNKNOWN", "detalhe": json.dumps(est)[:200]}
    else:
        est = None
        crit["ab_estatistica"] = {"estado": "UNKNOWN", "detalhe": "sem --run-a/--run-b"}

    # --- criterios ainda sem artefato: UNKNOWN explicito --------------------
    for nome, motivo in [
        ("recall15_global_nao_regride", "exige par A/B com Recall@15 por pergunta"),
        ("recall15_macro_por_dominio", "exige par A/B com rotulo de dominio"),
        ("hard_negative_suite", "suite de hard negatives ainda nao existe (runbook §12)"),
        ("validacao_externa", "os held-outs atuais NAO sao independentes (medido: 20-28% de sobreposicao com o blind v3)"),
        ("latencia_e_memoria", "nao medido"),
        ("sealed_holdout_apos_freeze", "sealed holdout nao existe; exige perguntas de fora do corpus"),
    ]:
        crit[nome] = {"estado": "UNKNOWN", "detalhe": motivo}

    # --- veredito: o PIOR criterio, nunca a media --------------------------
    ordem = {"FAIL": 3, "UNKNOWN": 2, "PASS": 1}
    pior = max(crit.values(), key=lambda c: ordem[c["estado"]])["estado"]
    veredito = {"FAIL": "INVALID", "UNKNOWN": "INCONCLUSIVE", "PASS": "ACCEPTED"}[pior]

    print()
    print("=== GATE §17 — criterio por criterio ===")
    for nome, c in crit.items():
        marca = {"PASS": "PASS   ", "FAIL": "FAIL   ", "UNKNOWN": "UNKNOWN"}[c["estado"]]
        print(f"  [{marca}] {nome}")
        print(f"             {c['detalhe']}")
    print()
    print(f"  VEREDITO: {veredito}")
    if veredito != "ACCEPTED":
        print("  UNKNOWN nao promove. Fail-closed: na duvida o veredito e' pior, nunca melhor.")
        if veredito == "INCONCLUSIVE":
            print("  Para ACCEPTED: todos os 11 criterios precisam de PASS explicito.")

    res = {"veredito": veredito, "criterios": crit, "ab": est, "controle": CONTROLE}
    Path("/tmp/gate_rag_v4.json").write_text(json.dumps(res, ensure_ascii=False, indent=2),
                                             encoding="utf-8")
    print("  relatorio: /tmp/gate_rag_v4.json")
    return 0 if veredito == "ACCEPTED" else 1


if __name__ == "__main__":
    sys.exit(main())
