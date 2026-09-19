#!/usr/bin/env python3
"""Classificacao REST: escolher 1 de 276 operacoes para uma pergunta em PT.

Pergunta que este script responde: o REST e' problema de RECUPERACAO ou de
CLASSIFICACAO? A recuperacao ja' foi medida (denso puro 25,0% @1 no rest_ops_40 com
rerank top_n=15). Aqui mede-se a classificacao no MESMO benchmark e no MESMO ground
truth, para comparar maca com maca.

Espaco de rotulos: 276 operacoes (o conjunto e' FECHADO e enumerado - e' isso que
justifica tratar como classificacao em vez de busca).

Uso:
    python scripts/classify_rest_ops_276.py --limit 5      # piloto
    python scripts/classify_rest_ops_276.py                # os 40

A chave da API e' lida do ambiente (A6API_KEY) ou, na falta, do config do HAOS. Ela
NUNCA e' impressa, nem em caso de erro.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENCH = os.path.join(REPO, "data", "eval", "rest_api_benchmark_ops_40.jsonl")
OPS = os.path.join(REPO, "data", "knowledge", "rest-api-derived-ops.jsonl")

BASE_URL = os.environ.get("A6API_BASE_URL", "https://api.a6api.com/v1")
MODEL = os.environ.get("A6API_MODEL", "deepseek-v4-flash")
CONFIG_HAOS = "/root/.haos/config.yaml"


def chave() -> str:
    """Le a chave do ambiente. Nunca imprime o valor.

    Ordem: A6API_KEY -> key_env declarado no config do HAOS -> nada (aborta).
    O provedor a6api no config NAO guarda a chave no arquivo: ele declara `key_env`,
    o NOME de uma variavel de ambiente. Ler o nome e' seguro; o valor nunca sai daqui.
    """
    k = os.environ.get("A6API_KEY")
    if k:
        return k
    nome_var = None
    try:
        txt = open(CONFIG_HAOS, encoding="utf-8").read()
    except OSError:
        sys.exit("sem A6API_KEY no ambiente e sem config do HAOS legivel")
    m = re.search(r"a6api\.com/v1\s*\n\s*key_env:\s*([A-Za-z_][A-Za-z0-9_]*)", txt)
    if m:
        nome_var = m.group(1)
    else:
        # fallback: o nome convencional que o wrapper do HAOS gera para o provedor
        nome_var = "HERMES_CUSTOM_API_A6API_COM_API_KEY"
    k = os.environ.get(nome_var)
    if not k:
        sys.exit(f"variavel de ambiente {nome_var} nao definida (nome da variavel e' "
                 f"seguro; o valor nao foi lido nem impresso)")
    return k


def catalogo(ops: list[dict]) -> str:
    """Lista numerada das 276 operacoes - e' o espaco de rotulos."""
    linhas = []
    for i, o in enumerate(ops, 1):
        resumo = (o.get("claim") or "").split(":", 1)[-1].strip()
        linhas.append(f"{i}. [{o.get('resource','?')}] {o.get('operation','?')} — {resumo[:110]}")
    return "\n".join(linhas)


def pergunta_prompt(question: str) -> str:
    return (
        "Voce e' um classificador de operacoes da REST API V2 do HCL Workload Automation.\n"
        "Dado um pedido do usuario em portugues, escolha a UNICA operacao que o atende.\n\n"
        "Responda EXATAMENTE neste formato, sem nada antes ou depois:\n"
        "NUMERO: <numero da operacao>\n"
        "MOTIVO: <uma linha curta>\n\n"
        f"PEDIDO: {question}"
    )


def chama(chave_api: str, catalogo_txt: str, question: str, tentativas: int = 3) -> tuple[str, str]:
    corpo = {
        "model": MODEL,
        "temperature": 0,
        "messages": [
            {"role": "system", "content":
                "Escolha a operacao pedida na lista abaixo. A lista e' o espaco COMPLETO "
                "de respostas; nao invente numeros fora dela.\n\n" + catalogo_txt},
            {"role": "user", "content": pergunta_prompt(question)},
        ],
    }
    dados = json.dumps(corpo).encode()
    ultimo = None
    for t in range(tentativas):
        try:
            req = urllib.request.Request(
                BASE_URL.rstrip("/") + "/chat/completions", data=dados,
                headers={"Content-Type": "application/json",
                         "Authorization": "Bearer " + chave_api})
            with urllib.request.urlopen(req, timeout=180) as r:
                j = json.loads(r.read().decode())
            return j["choices"][0]["message"]["content"], ""
        except urllib.error.HTTPError as e:
            # nunca ecoar cabecalhos/corpo que possam conter a chave
            ultimo = f"HTTP {e.code}"
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 * (t + 1))
                continue
            return "", ultimo
        except Exception as e:  # noqa: BLE001
            ultimo = type(e).__name__
            time.sleep(2 * (t + 1))
    return "", ultimo or "falhou"


def extrai_numero(texto: str) -> int | None:
    m = re.search(r"NUMERO:\s*(\d+)", texto)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(\d{1,3})\b", texto)
    return int(m.group(1)) if m else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="0 = todos")
    ap.add_argument("--out", default="/tmp/rest_cls.json")
    args = ap.parse_args()

    bench = [json.loads(l) for l in open(BENCH, encoding="utf-8") if l.strip()]
    ops = [json.loads(l) for l in open(OPS, encoding="utf-8") if l.strip()]
    if args.limit:
        bench = bench[: args.limit]

    cat = catalogo(ops)
    chave_api = chave()
    print(f"modelo={MODEL}  operacoes={len(ops)}  perguntas={len(bench)}", file=sys.stderr)
    print(f"catalogo ~{len(cat)//4} tokens", file=sys.stderr)

    # espaco de rotulos: o MESMO conjunto de 276 operacoes para todas as perguntas
    idx_por_claim = {o["claim_id"]: i + 1 for i, o in enumerate(ops)}
    resultados, acertos, erros = [], 0, 0
    for n, b in enumerate(bench, 1):
        alvo = idx_por_claim.get(b["relevant_claim_ids"][0])
        txt, err = chama(chave_api, cat, b["question"])
        num = extrai_numero(txt) if txt else None
        ok = (num == alvo)
        acertos += ok
        if err:
            erros += 1
        resultados.append({
            "id": b["id"], "family": b["family"], "question": b["question"],
            "alvo_claim": b["relevant_claim_ids"][0], "alvo_num": alvo,
            "escolhido_num": num,
            "escolhido_op": ops[num - 1]["operation"] if num and 1 <= num <= len(ops) else None,
            "acertou": ok, "erro_api": err or None,
            "resposta_bruta": (txt or "")[:300],
        })
        print(f"  [{n}/{len(bench)}] {'OK ' if ok else 'err'} alvo={alvo} escolhido={num}"
              f"{' api='+err if err else ''}", file=sys.stderr)

    acu = acertos / len(bench) if bench else 0.0
    # sem as perguntas que contem o nome da familia na propria pergunta (vazamento)
    limpo = [r for r in resultados if r["family"].lower() not in r["question"].lower()]
    acu_limpo = (sum(r["acertou"] for r in limpo) / len(limpo)) if limpo else 0.0
    res = {"modelo": MODEL, "n_ops": len(ops), "n_perguntas": len(bench),
           "acuracia_top1": acu, "acertos": acertos,
           "n_vazamento_rotulo": len(resultados) - len(limpo),
           "acuracia_top1_sem_vazamento": acu_limpo, "n_sem_vazamento": len(limpo),
           "erros_api": erros, "resultados": resultados}
    json.dump(res, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"ACURACIA @1: {acertos}/{len(bench)} = {acu:.4f}")
    print(f"sem vazamento de rotulo ({len(limpo)} perguntas): {acu_limpo:.4f}")
    print(f"erros de API: {erros}")
    print(f"gravado {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
