#!/usr/bin/env python3
"""Auditor de vazamento dos benchmarks de avaliação (P0-5 do RUNBOOK RAG V4).

Fail-closed: um benchmark que sai FAIL nao pode entrar em score oficial.

Checagens implementadas (numeracao do runbook):
  1. pergunta exata dentro de `synthetic_questions` do corpus indexado;
  2. n-grama longo coincidente entre pergunta e synthetic_questions;
  3. similaridade lexical alta (Jaccard de tokens) pergunta x synthetic_questions;
  4. (NAO implementada: similaridade semantica exige modelo; fica para o gate V4)
  5. codigo/ID alvo explicito na pergunta;
  6. texto literal copiado da claim para a pergunta;
  7. mesma pergunta em mais de um arquivo de benchmark (splits);
  8. near-duplicate entre arquivos de benchmark;
  9. templates identicos com apenas a entidade trocada;
 10. conjunto de relevancia tao amplo que Hit@1 deixa de ser informativo.

Deterministico, offline, stdlib apenas. Nao altera nenhum dado.

Uso:
    python scripts/audit_eval_leakage.py                      # audita data/eval/*.jsonl
    python scripts/audit_eval_leakage.py --benchmarks data/eval/blind_v3_slices.jsonl
    python scripts/audit_eval_leakage.py --json saida.json    # relatorio legivel por maquina

Exit code: 0 = PASS/WARN, 1 = FAIL (fail-closed).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EVAL_DIR = REPO / "data" / "eval"
CORPUS_DEFAULT = REPO / "data" / "export" / "tws_corpus_master_consolidated.jsonl"

# --- limiares (explicitar no relatorio; mudar aqui muda o veredito) -----------------
JACCARD_FAIL = 0.80   # pergunta x synthetic_question: praticamente a mesma frase
JACCARD_WARN = 0.60
NGRAM_FAIL = 12       # n-grama contiguo de 12 tokens coincidente = copia
NGRAM_WARN = 8
DUP_FAIL = 0.90       # near-duplicate entre arquivos de benchmark
DUP_WARN = 0.75
RELEVANCIA_AMPLA = 20  # >= 20 claims relevantes torna Hit@1 pouco informativo
TEMPLATE_MIN = 3       # >= 3 perguntas com a mesma "casca" = template repetido

STOP = {
    "de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "com", "na", "os",
    "no", "se", "por", "mais", "as", "dos", "como", "mas", "ao", "das", "tem",
    "qual", "quais", "onde", "ser", "sao", "entre", "este", "esta", "pode", "deve",
    "utilizar", "usar", "quando", "apos", "antes", "atraves", "isso", "pela", "sem",
    "uso", "existe", "apenas", "exemplo", "faco", "consigo", "ha", "eh", "ou",
}

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_.:\-/+]*")
# codigos tecnicos do dominio: AWS/AWK/CWWK... e ids com hifen/versao
CODE_RE = re.compile(r"\b(?:AW[A-Z0-9]{2,}|CW[A-Z0-9]{2,}|[A-Z]{2,}[0-9]{3,})\b")
VERSION_RE = re.compile(r"\b\d+\.\d+(?:\.\d+)*\b")


def norm(text: str) -> str:
    """Minusculas sem acento, espacos colapsados — comparacao entre fontes distintas."""
    if not text:
        return ""
    folded = unicodedata.normalize("NFKD", text.lower())
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", folded).strip()


def toks(text: str) -> list[str]:
    return [t for t in TOKEN_RE.findall(norm(text)) if t not in STOP and len(t) > 1]


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def ngrams(seq: list[str], n: int) -> set[tuple[str, ...]]:
    return {tuple(seq[i:i + n]) for i in range(max(0, len(seq) - n + 1))}


def longest_common_ngram(a: list[str], b: list[str]) -> int:
    """Comprimento do maior n-grama contiguo comum (deterministico)."""
    if not a or not b:
        return 0
    bset = {tuple(b[i:i + 12]) for i in range(max(0, len(b) - 11))}
    best = 0
    for n in (12, 8):
        if n <= best:
            break
        aset = ngrams(a, n)
        if aset and aset & {tuple(b[i:i + n]) for i in range(max(0, len(b) - n + 1))}:
            best = n
    for n in (6, 4):
        if best >= n:
            break
        aset = ngrams(a, n)
        if aset & {tuple(b[i:i + n]) for i in range(max(0, len(b) - n + 1))}:
            best = n
    return best


def template_shape(question: str) -> str:
    """Casca da pergunta: entidades/codigos/numeros viram marcador."""
    q = norm(question)
    q = CODE_RE.sub("<CODE>", q)
    q = VERSION_RE.sub("<VER>", q)
    q = re.sub(r"\b[a-z_][a-z0-9_.\-]{3,}\b", "<TOK>", q)
    return re.sub(r"\s+", " ", q).strip()


def carrega_benchmarks(paths: list[Path]) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for p in paths:
        rows = []
        for ln, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError as exc:
                print(f"  AVISO: {p.name}:{ln} JSON invalido ({exc})", file=sys.stderr)
                continue
            q = d.get("question") or d.get("query") or ""
            if not q:
                continue
            d["_qid"] = str(d.get("id") or f"{p.stem}-{ln}")
            d["_q"] = q
            d["_rel"] = d.get("relevant_claim_ids") or d.get("relevant_ids") or []
            rows.append(d)
        out[p.name] = rows
    return out


def carrega_synthetic(corpus_path: Path) -> tuple[dict[str, list[str]], dict[str, str]]:
    """{claim_id: [perguntas sinteticas]} e {claim_id: claim}."""
    syn: dict[str, list[str]] = {}
    claims: dict[str, str] = {}
    if not corpus_path.exists():
        return syn, claims
    for line in corpus_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        cid = str(d.get("claim_id") or "")
        if not cid:
            continue
        sq = d.get("synthetic_questions") or []
        if isinstance(sq, str):
            sq = [sq]
        syn[cid] = [str(s) for s in sq if s]
        claims[cid] = str(d.get("claim") or "")
    return syn, claims


def audita(benchmarks: dict[str, list[dict]], syn: dict[str, list[str]],
           claims: dict[str, str]) -> dict:
    achados: list[dict] = []

    def add(nivel: str, check: str, msg: str, **extra) -> None:
        achados.append({"nivel": nivel, "check": check, "msg": msg, **extra})

    # indice invertido das synthetic_questions (check 1, 2, 3)
    syn_norm: dict[str, tuple[str, str]] = {}   # normalizado -> (claim_id, original)
    syn_toks: dict[str, set[str]] = {}
    syn_seq: dict[str, list[str]] = {}
    for cid, qs in syn.items():
        for q in qs:
            nq = norm(q)
            if nq:
                syn_norm.setdefault(nq, (cid, q))
                t = toks(q)
                syn_toks[nq] = set(t)
                syn_seq[nq] = t

    # --- checks 1/2/3: pergunta x synthetic_questions ---------------------------
    for fname, rows in benchmarks.items():
        for d in rows:
            nq = norm(d["_q"])
            if not nq:
                continue
            if nq in syn_norm:
                cid, _ = syn_norm[nq]
                add("FAIL", "1-exato",
                    f"{fname}:{d['_qid']} e' IDENTICA a uma synthetic_question indexada",
                    arquivo=fname, qid=d["_qid"], claim_id=cid)
                continue
            qt = set(toks(d["_q"]))
            melhor_j, melhor_q = 0.0, ""
            for sq, st in syn_toks.items():
                j = jaccard(qt, st)
                if j > melhor_j:
                    melhor_j, melhor_q = j, sq
            if melhor_j >= JACCARD_WARN:
                nivel = "FAIL" if melhor_j >= JACCARD_FAIL else "WARN"
                add(nivel, "3-jaccard",
                    f"{fname}:{d['_qid']} Jaccard {melhor_j:.2f} com synthetic_question",
                    arquivo=fname, qid=d["_qid"], similar=melhor_q[:120])
            qseq = toks(d["_q"])
            melhor_n = 0
            for sq, sseq in syn_seq.items():
                n = longest_common_ngram(qseq, sseq)
                if n > melhor_n:
                    melhor_n = n
            if melhor_n >= NGRAM_WARN:
                nivel = "FAIL" if melhor_n >= NGRAM_FAIL else "WARN"
                add(nivel, "2-ngrama",
                    f"{fname}:{d['_qid']} n-grama contiguo de {melhor_n} tokens com synthetic_question",
                    arquivo=fname, qid=d["_qid"])

    # --- check 7: mesma pergunta em mais de um arquivo --------------------------
    onde: dict[str, list[str]] = defaultdict(list)
    for fname, rows in benchmarks.items():
        for d in rows:
            nq = norm(d["_q"])
            if nq:
                onde[nq].append(f"{fname}:{d['_qid']}")
    for nq, locais in onde.items():
        arquivos = {x.split(":")[0] for x in locais}
        if len(arquivos) > 1:
            add("FAIL", "7-split",
                f"pergunta em {len(arquivos)} arquivos de benchmark: {sorted(arquivos)}",
                qid=locais[0])

    # --- check 8: near-duplicate entre arquivos ---------------------------------
    lista = [(f, d) for f, rows in benchmarks.items() for d in rows]
    for i in range(len(lista)):
        fi, di = lista[i]
        ti, qi = set(toks(di["_q"])), norm(di["_q"])
        for j in range(i + 1, len(lista)):
            fj, dj = lista[j]
            if fi == fj:
                continue
            if abs(len(qi) - len(norm(dj["_q"]))) > 120:
                continue
            sim = jaccard(ti, set(toks(dj["_q"])))
            if sim >= DUP_WARN:
                nivel = "FAIL" if sim >= DUP_FAIL else "WARN"
                add(nivel, "8-duplicata",
                    f"{fi}:{di['_qid']} ~ {fj}:{dj['_qid']} similaridade {sim:.2f}",
                    arquivo=fi, qid=di["_qid"], par=f"{fj}:{dj['_qid']}")

    # --- check 5: codigo/ID explicito na pergunta -------------------------------
    for fname, rows in benchmarks.items():
        for d in rows:
            codigos = CODE_RE.findall(d["_q"])
            if codigos:
                add("WARN", "5-codigo",
                    f"{fname}:{d['_qid']} contem codigo explicito {codigos[:3]} — "
                    f"se a tarefa nao for exact lookup, e' vazamento de chave",
                    arquivo=fname, qid=d["_qid"])

    # --- check 10: relevancia ampla demais --------------------------------------
    for fname, rows in benchmarks.items():
        for d in rows:
            n = len(d["_rel"])
            if n >= RELEVANCIA_AMPLA:
                add("WARN", "10-relevancia-ampla",
                    f"{fname}:{d['_qid']} tem {n} claims relevantes — Hit@1 pouco informativo",
                    arquivo=fname, qid=d["_qid"])

    # --- check 9: templates repetidos -------------------------------------------
    shapes: dict[str, list[str]] = defaultdict(list)
    for fname, rows in benchmarks.items():
        for d in rows:
            shapes[template_shape(d["_q"])].append(f"{fname}:{d['_qid']}")
    for shape, qids in shapes.items():
        if len(qids) >= TEMPLATE_MIN:
            add("WARN", "9-template",
                f"{len(qids)} perguntas com a mesma casca: {qids[:4]}",
                shape=shape[:120], qids=qids)

    # --- check 6: texto da claim copiado na pergunta ----------------------------
    for fname, rows in benchmarks.items():
        for d in rows:
            qseq = toks(d["_q"])
            if len(qseq) < NGRAM_WARN:
                continue
            for cid in d["_rel"]:
                cl = claims.get(str(cid))
                if not cl:
                    continue
                n = longest_common_ngram(qseq, toks(cl))
                if n >= NGRAM_FAIL:
                    add("FAIL", "6-copia-da-claim",
                        f"{fname}:{d['_qid']} copia {n} tokens contiguos da claim {cid}",
                        arquivo=fname, qid=d["_qid"], claim_id=cid)
                    break

    por_nivel = Counter(a["nivel"] for a in achados)
    por_check = Counter(a["check"] for a in achados)
    veredito = "FAIL" if por_nivel["FAIL"] else ("WARN" if por_nivel["WARN"] else "PASS")

    return {
        "veredito": veredito,
        "resumo": {
            "arquivos": len(benchmarks),
            "perguntas": sum(len(r) for r in benchmarks.values()),
            "synthetic_questions_indexadas": sum(len(v) for v in syn.values()),
            "claims": len(claims),
            "FAIL": por_nivel["FAIL"], "WARN": por_nivel["WARN"],
        },
        "por_check": dict(sorted(por_check.items())),
        "limiares": {"jaccard_fail": JACCARD_FAIL, "jaccard_warn": JACCARD_WARN,
                     "ngram_fail": NGRAM_FAIL, "ngram_warn": NGRAM_WARN,
                     "dup_fail": DUP_FAIL, "dup_warn": DUP_WARN,
                     "relevancia_ampla": RELEVANCIA_AMPLA, "template_min": TEMPLATE_MIN},
        "achados": achados,
        "nao_implementado": ["4-similaridade-semantica (exige modelo; gate V4)"],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--benchmarks", nargs="*", default=None,
                    help="arquivos de benchmark (default: data/eval/*.jsonl)")
    ap.add_argument("--corpus", default=str(CORPUS_DEFAULT))
    ap.add_argument("--json", dest="json_out", default=None)
    ap.add_argument("--max-achados", type=int, default=40)
    args = ap.parse_args()

    if args.benchmarks:
        paths = [Path(p) for p in args.benchmarks]
    else:
        paths = sorted(EVAL_DIR.glob("*.jsonl"))
    paths = [p for p in paths if p.exists()]
    if not paths:
        print("erro: nenhum benchmark encontrado", file=sys.stderr)
        return 1

    print(f"benchmarks: {len(paths)} arquivo(s)")
    benchmarks = carrega_benchmarks(paths)
    corpus = Path(args.corpus)
    print(f"corpus:     {corpus.name} ({'ok' if corpus.exists() else 'AUSENTE'})")
    syn, claims = carrega_synthetic(corpus)

    res = audita(benchmarks, syn, claims)

    print()
    print(f"VEREDITO: {res['veredito']}")
    print(f"  arquivos={res['resumo']['arquivos']}  perguntas={res['resumo']['perguntas']}  "
          f"synthetic_questions={res['resumo']['synthetic_questions_indexadas']}  "
          f"claims={res['resumo']['claims']}")
    print(f"  FAIL={res['resumo']['FAIL']}  WARN={res['resumo']['WARN']}")
    if res["por_check"]:
        print("  por check: " + ", ".join(f"{k}={v}" for k, v in res["por_check"].items()))
    print()
    for a in res["achados"][:args.max_achados]:
        print(f"  [{a['nivel']}] {a['check']}: {a['msg']}")
    resto = len(res["achados"]) - args.max_achados
    if resto > 0:
        print(f"  ... +{resto} achado(s) (use --json para o relatorio completo)")

    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nrelatorio: {args.json_out}")

    return 1 if res["veredito"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
