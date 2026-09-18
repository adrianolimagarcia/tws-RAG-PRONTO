#!/usr/bin/env python3
"""Classificacao zero-shot por LLM: pergunta operacional -> familia de recurso REST.

OBJETIVO
    Medir se um LLM classifica corretamente, SEM TREINO e sem exemplos (zero-shot),
    a familia de recurso a que uma pergunta operacional se refere. E' a alternativa
    ao problema de RECUPERACAO que estava sendo medido: hoje a pergunta tem de achar
    o registro certo entre ~6900 documentos; aqui ela so' precisa ser rotulada.

GROUND TRUTH
    O campo `family` de data/eval/rest_api_benchmark_40.jsonl, que veio das TAGS da
    spec OpenAPI - nunca do texto derivado. Nao ha vazamento: o LLM nunca viu este
    benchmark e nao recebe nenhuma pergunta de exemplo.

ANTI-TAUTOLOGIA (o que sustenta a medicao)
    1. Zero-shot de verdade: o prompt tem SO' a lista de familias (e, na variante B,
       a descricao que a PROPRIA spec da' para a tag). Nenhum exemplo rotulado.
    2. As perguntas do benchmark nao entram no prompt de nenhuma outra pergunta.
    3. A acuracia e' medida contra ground truth que o LLM nao pode ter visto.
    4. O conjunto de rotulos e' fechado e declarado - o LLM nao pode inventar familia.

CUSTO
    API PAGA. Teto embutido: MAX_CHAMADAS. O script aborta ao atingir o teto em vez
    de seguir gastando. 1 chamada por pergunta por variante.

USO
    python3 scripts/classify_rest_api_zero_shot.py --pilot      # 1 chamada, valida
    python3 scripts/classify_rest_api_zero_shot.py --variant A  # so' nomes
    python3 scripts/classify_rest_api_zero_shot.py --variant B  # nomes + descricao da spec
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

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG = "/root/.haos/config.yaml"
BENCH = os.path.join(REPO, "data", "eval", "rest_api_benchmark_40.jsonl")
OUT = os.path.join(REPO, "data", "eval", "rest_api_zeroshot_results.jsonl")

PROVIDER = "Api.a6api.com"
MODELO = "deepseek-v4-flash"
MAX_CHAMADAS = 200          # teto de gasto: aborta em vez de continuar
# ATENCAO (medido): `deepseek-v4-flash` e' modelo de RACIOCINIO. O campo
# `reasoning_content` e' gerado ANTES do `content` e consome o mesmo orcamento de
# `max_tokens`. Com max_tokens=24 o resultado e' content='' e finish_reason='length' -
# a resposta sai vazia e a medicao mediria o teto, nao o modelo. Medido: 123 dos 125
# tokens de uma resposta curta sao de reasoning, e com max_tokens=2048 ainda houve 4
# de 40 perguntas truncadas (resposta vazia). Por isso o teto e' folgado E o
# `finish_reason` e' gravado: truncamento tem de ficar VISIVEL, nao virar erro do
# modelo na contabilidade.
MAX_TOKENS_RESPOSTA = 8192
MAX_SUMMARIES_POR_FAMILIA = 8  # contexto da variante B: quantos summaries da spec por familia


def credencial() -> tuple[str, str]:
    """Le base_url e a credencial do provider no config.

    O config pode trazer a chave de duas formas: `key: <valor>` (inline) ou
    `key_env: <NOME_DA_VAR>` (o padrao deste host - o valor vive no ambiente, nao no
    config). A chave NAO e' impressa nem logada em lugar nenhum deste script.
    """
    txt = open(CONFIG, encoding="utf-8").read()
    linhas = txt.splitlines()
    ini = None
    for i, l in enumerate(linhas):
        if PROVIDER in l:
            ini = i
            break
    if ini is None:
        raise SystemExit(f"provider {PROVIDER} nao encontrado em {CONFIG}")
    fim = len(linhas)
    for j in range(ini + 1, len(linhas)):
        if re.match(r"\s*-\s*name:", linhas[j]):
            fim = j
            break
    bloco = "\n".join(linhas[ini:fim])
    m_url = re.search(r"base_url:\s*(\S+)", bloco)
    if not m_url:
        raise SystemExit("base_url ausente no bloco do provider")
    base = m_url.group(1).rstrip("/")

    m_inline = re.search(r"^\s*key:\s*(\S+)", bloco, re.M)
    if m_inline:
        return base, m_inline.group(1)
    m_env = re.search(r"^\s*key_env:\s*(\S+)", bloco, re.M)
    if m_env:
        nome = m_env.group(1)
        val = os.environ.get(nome)
        if not val:
            raise SystemExit(f"a variavel de ambiente {nome} (key_env) nao esta definida")
        return base, val
    raise SystemExit("nem key nem key_env no bloco do provider")


def chamar(base: str, key: str, mensagens: list[dict]) -> tuple[str, dict, str]:
    """Uma chamada de chat completion. Devolve (texto, uso_de_tokens, finish_reason).

    O `finish_reason` e' devolvido de proposito: 'length' significa que o modelo gastou
    o orcamento em `reasoning_content` e NAO chegou a emitir `content`. Tratar isso como
    erro de classificacao contamina a metrica - e' falha do instrumento, nao do modelo.
    """
    corpo = json.dumps({
        "model": MODELO,
        "messages": mensagens,
        "temperature": 0.0,
        "max_tokens": MAX_TOKENS_RESPOSTA,
    }).encode()
    req = urllib.request.Request(
        base + "/chat/completions",
        data=corpo,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.loads(r.read())
    escolha = d["choices"][0]
    return escolha["message"]["content"], d.get("usage", {}), escolha.get("finish_reason") or "?"


def familias_do_bench() -> tuple[list[str], list[dict]]:
    bench = [json.loads(l) for l in open(BENCH, encoding="utf-8") if l.strip()]
    return sorted({b["family"] for b in bench}), bench


def descricoes_da_spec() -> dict[str, str]:
    """Contexto que a PROPRIA spec da' para cada familia. Vazio se a spec nao estiver acessivel.

    CORRECAO IMPORTANTE (medida): a spec NAO tem descricao de tag - o array `tags` traz
    SO' `name` (verificado: 24 tags, chaves=['name']). Uma primeira rodada da variante B
    rodou com `descricoes da spec disponiveis: 0/24`, ou seja, SEM descricao nenhuma, e a
    conclusao tirada dali ("a descricao da spec nao ajuda") era sobre um prompt que nunca
    teve descricao - foi RETIRADA.

    O que a spec de fato oferece e' o `summary` de cada operacao. Aqui a familia recebe os
    summaries das suas operacoes, que e' texto da propria spec - zero contato com a redacao
    das perguntas do benchmark.
    """
    spec_path = os.environ.get("REST_API_SPEC", "")
    if not spec_path or not os.path.exists(spec_path):
        return {}
    spec = json.load(open(spec_path, encoding="utf-8"))

    # a spec nomeia as tags como 'V2 APIs - Calendar'; o benchmark usa 'Calendar'
    def curto(nome: str) -> str:
        return re.sub(r"^V2 APIs\s*-\s*", "", str(nome)).strip()

    out: dict[str, list[str]] = {}
    for t in spec.get("tags") or []:
        if isinstance(t, dict) and t.get("name"):
            out.setdefault(curto(t["name"]), [])
    for _path, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for metodo, op in item.items():
            if metodo.lower() not in ("get", "post", "put", "delete", "patch") or not isinstance(op, dict):
                continue
            for tag in op.get("tags") or []:
                resumo = str(op.get("summary") or "").strip()
                if resumo:
                    out.setdefault(curto(tag), []).append(" ".join(resumo.split()))

    return {k: "; ".join(v[:MAX_SUMMARIES_POR_FAMILIA])[:220] for k, v in out.items() if v}


def prompt(variant: str, familias: list[str], descs: dict[str, str], pergunta: str) -> list[dict]:
    if variant == "A":
        lista = "\n".join(f"- {f}" for f in familias)
    else:
        lista = "\n".join(
            f"- {f}" + (f": {descs[f]}" if descs.get(f) else "") for f in familias
        )
    sistema = (
        "Voce classifica perguntas de operadores de um produto de agendamento de jobs "
        "em UMA familia de recurso da API REST do produto.\n"
        "Responda APENAS com o nome exato de uma das familias da lista. "
        "Sem explicacao, sem pontuacao, sem texto extra.\n\n"
        f"Familias:\n{lista}"
    )
    return [{"role": "system", "content": sistema}, {"role": "user", "content": pergunta}]


def normalizar(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def casar(resposta: str, familias: list[str]) -> str | None:
    """Mapeia a resposta crua para uma familia declarada; None se nao casar."""
    n = normalizar(resposta)
    for f in familias:
        if normalizar(f) == n:
            return f
    for f in sorted(familias, key=lambda x: -len(x)):   # resposta com ruido em volta
        if normalizar(f) and normalizar(f) in n:
            return f
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", action="store_true", help="1 chamada so', para validar")
    ap.add_argument("--variant", default="A", choices=["A", "B"])
    args = ap.parse_args()

    base, key = credencial()
    familias, bench = familias_do_bench()
    descs = descricoes_da_spec() if args.variant == "B" else {}
    print(f"provider ok: {PROVIDER} modelo={MODELO}")
    print(f"familias ({len(familias)}): {', '.join(familias)}")
    if args.variant == "B":
        print(f"descricoes da spec disponiveis: {len(descs)}/{len(familias)}")
    print(f"teto de chamadas: {MAX_CHAMADAS}")

    alvo = bench[:1] if args.pilot else bench
    if args.pilot:
        print("\n--- PILOTO: 1 chamada ---")

    chamadas = 0
    tokens_in = tokens_out = 0
    linhas: list[dict] = []
    for b in alvo:
        if chamadas >= MAX_CHAMADAS:
            print(f"TETO DE {MAX_CHAMADAS} CHAMADAS ATINGIDO - abortando sem completar")
            break
        msgs = prompt(args.variant, familias, descs, b["question"])
        t0 = time.time()
        try:
            resp, uso, finish = chamar(base, key, msgs)
        except urllib.error.HTTPError as e:
            corpo = e.read()[:300].decode("utf-8", "replace")
            print(f"  ERRO HTTP {e.code}: {corpo}")
            return 2
        except Exception as e:  # noqa: BLE001
            print(f"  ERRO: {type(e).__name__}: {e}")
            return 2
        chamadas += 1
        tokens_in += int(uso.get("prompt_tokens") or 0)
        tokens_out += int(uso.get("completion_tokens") or 0)
        truncado = finish == "length" or not resp.strip()
        pred = casar(resp, familias)
        ok = pred == b["family"]
        linhas.append({
            "id": b["id"], "question": b["question"], "family": b["family"],
            "predito": pred, "resposta_crua": resp.strip()[:80], "acerto": ok,
            "finish_reason": finish, "truncado": truncado,
            "variante": args.variant, "modelo": MODELO,
        })
        if args.pilot:
            print(f"  pergunta   : {b['question'][:90]}")
            print(f"  familia GT : {b['family']}")
            print(f"  resposta   : {resp.strip()[:90]}")
            print(f"  casada em  : {pred}  -> {'ACERTO' if ok else 'ERRO'}")
            print(f"  tokens     : in={uso.get('prompt_tokens')} out={uso.get('completion_tokens')}")
            print(f"  latencia   : {time.time()-t0:.1f}s")
            print("\n--- PILOTO OK: caminho validado ---")

    if args.pilot:
        return 0

    acertos = sum(1 for l in linhas if l["acerto"])
    truncados = sum(1 for l in linhas if l["truncado"])
    validos = [l for l in linhas if not l["truncado"]]
    acertos_validos = sum(1 for l in validos if l["acerto"])
    print(f"\n=== RESULTADO variante {args.variant} ===")
    print(f"acuracia zero-shot (todos)      : {acertos}/{len(linhas)} "
          f"({100*acertos/max(1,len(linhas)):.1f}%)")
    print(f"TRUNCADOS (falha do instrumento): {truncados}  "
          f"- reasoning consumiu o orcamento antes do content")
    print(f"acuracia sobre os NAO truncados : {acertos_validos}/{len(validos)} "
          f"({100*acertos_validos/max(1,len(validos)):.1f}%)")
    print(f"chamadas: {chamadas}  tokens: in={tokens_in} out={tokens_out}")

    acertos_por_fam = {}
    tot_por_fam = {}
    for l in linhas:
        tot_por_fam[l["family"]] = tot_por_fam.get(l["family"], 0) + 1
        if l["acerto"]:
            acertos_por_fam[l["family"]] = acertos_por_fam.get(l["family"], 0) + 1
    print("\npor familia (GT):")
    for f in sorted(tot_por_fam):
        print(f"  {f:28s} {acertos_por_fam.get(f,0)}/{tot_por_fam[f]}")

    with open(OUT, "w", encoding="utf-8") as fh:
        for l in linhas:
            fh.write(json.dumps(l, ensure_ascii=False) + "\n")
    print(f"\ngravado {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
