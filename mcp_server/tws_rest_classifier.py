#!/usr/bin/env python3
"""Classificador de operacoes REST (HWA 10.2.8) - o caso REST e' CLASSIFICACAO.

POR QUE ISTO EXISTE E NAO E' RECUPERACAO. Medido em 19/09 no MESMO benchmark e no mesmo
ground truth (`rest_api_benchmark_ops_40.jsonl`):

    recuperacao, melhor ramo (denso puro + rerank)   @1 25,0%
    classificacao (catalogo das 276 ops no contexto) @1 92,5%   (91,9% sem vazamento)

O espaco de resposta do REST e' FECHADO e ENUMERADO (276 operacoes com estrutura conhecida:
metodo, path, familia). Isso nao e' um problema de busca - e' de escolha entre alternativas
conhecidas. Na recuperacao o indice precisa aproximar a pergunta PT do registro EN (e o ramo
esparso nao consegue: cobertura lexical mediana 0,00); na classificacao o catalogo inteiro
esta' no contexto e a decisao e' direta. Fator 3,7x.

Evidencia: data/evidence/lab-validation-2026-09-19-rest-e-classificacao-nao-recuperacao-276-classes-a-92-5-por-cento-contra-25-por-cento.jsonl
Script de medicao: scripts/classify_rest_ops_276.py (mesmo prompt, mesmo catalogo).

Este modulo e' a UNICA implementacao da chamada: o script de medicao passou a usa-lo, para
nao haver duas copias do prompt que possam divergir.

CHAVE. A chave NAO vive aqui nem no config em texto. Resolve-se de, em ordem: A6API_KEY no
ambiente; o `key_env` declarado para o provedor a6api no config do HAOS (le-se o NOME da
variavel, nunca o valor); senao, o nome convencional do wrapper. Sem chave, `disponivel()`
devolve False e o chamador DEGRADA para recuperacao - o MCP nao pode deixar de responder
porque falta credencial. O valor da chave nunca e' impresso, nem em mensagem de erro.
"""
from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request

DIR = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(DIR)
OPS_PADRAO = os.path.join(RAIZ, "data", "knowledge", "rest-api-derived-ops.jsonl")

BASE_URL = os.environ.get("A6API_BASE_URL", "https://api.a6api.com/v1")
MODELO = os.environ.get("A6API_MODEL", "deepseek-v4-flash")
CONFIG_HAOS = os.environ.get("HAOS_CONFIG", "/root/.haos/config.yaml")

OPS = None           # cache: lista de operacoes (o espaco de rotulos)
CATALOGO = None      # cache: o catalogo como texto


def _chave():
    """Le a chave do ambiente. Nunca imprime o valor."""
    k = os.environ.get("A6API_KEY")
    if k:
        return k
    try:
        txt = open(CONFIG_HAOS, encoding="utf-8").read()
    except OSError:
        return None
    m = re.search(r"a6api\.com/v1\s*\n\s*key_env:\s*([A-Za-z_][A-Za-z0-9_]*)", txt)
    nome_var = m.group(1) if m else "HERMES_CUSTOM_API_A6API_COM_API_KEY"
    return os.environ.get(nome_var)


def disponivel():
    """Ha' chave para classificar? Sem ela, o chamador degrada para recuperacao."""
    return bool(_chave())


def _carrega(ops_path=OPS_PADRAO):
    global OPS, CATALOGO
    if OPS is None:
        OPS = [json.loads(l) for l in open(ops_path, encoding="utf-8") if l.strip()]
        CATALOGO = catalogo(OPS)
    return OPS


def catalogo(ops):
    """Lista numerada das operacoes - e' o espaco de rotulos. Mesmo formato do medidor."""
    linhas = []
    for i, o in enumerate(ops, 1):
        resumo = (o.get("claim") or "").split(":", 1)[-1].strip()
        linhas.append(f"{i}. [{o.get('resource', '?')}] {o.get('operation', '?')} — {resumo[:110]}")
    return "\n".join(linhas)


def pergunta_prompt(pergunta):
    return (
        "Voce e' um classificador de operacoes da REST API V2 do HCL Workload Automation.\n"
        "Dado um pedido do usuario em portugues, escolha a UNICA operacao que o atende.\n\n"
        "Responda EXATAMENTE neste formato, sem nada antes ou depois:\n"
        "NUMERO: <numero da operacao>\n"
        "MOTIVO: <uma linha curta>\n\n"
        f"PEDIDO: {pergunta}"
    )


def chama(catalogo_txt, pergunta, tentativas=3):
    """Uma chamada de classificacao. Devolve (texto, erro); erro '' quando deu certo."""
    chave_api = _chave()
    if not chave_api:
        return "", "sem_chave"
    corpo = {
        "model": MODELO,
        "temperature": 0,
        "messages": [
            {"role": "system", "content":
                "Escolha a operacao pedida na lista abaixo. A lista e' o espaco COMPLETO "
                "de respostas; nao invente numeros fora dela.\n\n" + catalogo_txt},
            {"role": "user", "content": pergunta_prompt(pergunta)},
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


def extrai_numero(texto):
    m = re.search(r"NUMERO:\s*(\d+)", texto or "")
    if m:
        return int(m.group(1))
    m = re.search(r"\b(\d{1,3})\b", texto or "")
    return int(m.group(1)) if m else None


def classifica(pergunta, ops_path=OPS_PADRAO):
    """Classifica uma pergunta em 1 das 276 operacoes.

    Devolve dict com `operation`/`claim`/`claim_id` da operacao escolhida (o chamador ja'
    tem a forma da resposta de busca, entao troca o metodo sem trocar o contrato), ou None
    se nao houver chave, a API falhar, ou o numero vier fora do espaco. Nunca inventa: um
    numero fora de [1, 276] e' tratado como falha, nao como resposta.
    """
    ops = _carrega(ops_path)
    texto, erro = chama(CATALOGO, pergunta)
    if erro or not texto:
        return None
    n = extrai_numero(texto)
    if not n or not (1 <= n <= len(ops)):
        return None
    o = ops[n - 1]
    return {
        "claim_id": o["claim_id"],
        "resumo": (o.get("claim") or "").split(":", 1)[-1].strip(),
        "operation": o.get("operation"),
        "resource": o.get("resource"),
        "claim": o.get("claim"),
        "syntax": o.get("syntax"),
        "supporting_quote": o.get("supporting_quote"),
        "source_title": o.get("source_title"),
        "escolhido_num": n,
        "nota": "escolha entre as 276 operacoes - nao e' recuperacao",
    }


if __name__ == "__main__":  # teste rapido de encanamento
    print("chave disponivel:", disponivel())
    print("operacoes carregadas:", len(_carrega()))
