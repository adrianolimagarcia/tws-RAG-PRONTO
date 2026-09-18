#!/usr/bin/env python3
"""Gera o benchmark REST com ground truth por OPERACAO (40 perguntas).

POR QUE ESTE BENCHMARK EXISTE
-----------------------------
O benchmark de familia satura: com um registro por familia, "rotear para a familia" e'
aritmeticamente identico a acertar a classificacao (medido: 94,4%), e NAO existe o que
escolher dentro da familia - logo nenhuma melhoria de RANKING e' mensuravel. Aqui o
ground truth e' a OPERACAO: o recuperador tem de escolher entre 276 candidatos.

DIVISAO DE RESPONSABILIDADE (e' o que evita tautologia)
-------------------------------------------------------
- A PERGUNTA e' escrita por mim, em PT-BR, descrevendo a INTENCAO OPERACIONAL.
- O GROUND TRUTH e' resolvido MECANICAMENTE: (metodo, path) -> claim_id do registro
  derivado da spec. Eu nao digito id nenhum, entao nao ha' como errar nem de escolher.
- O TEXTO do registro alvo vem SO' da spec (ver scripts/extract_rest_api.py).

CHECAGENS ANTI-TAUTOLOGIA (rodadas na geracao, falham alto)
-----------------------------------------------------------
1. Nenhuma pergunta contem o PATH da propria operacao.
2. Nenhuma pergunta contem o SUMMARY da propria operacao de forma literal.
3. A cobertura de tokens pergunta<->registro alvo e' MEDIDA e reportada - se fosse alta
   demais, a pergunta estaria repetindo o registro e a medicao nao valeria.
4. As 40 operacoes alvo sao DISTINTAS.

LIMITE DECLARADO: operacoes da mesma familia diferem por detalhes sutis ("por filtro"
vs "por id"). A pergunta PRECISA carregar essa distincao para ser respondivel - isso
nao e' vazamento, e' o que o operador realmente sabe. Mas e' uma facilidade que a
pergunta de familia nao tinha, e por isso o numero aqui NAO e' comparavel ao de la'.

USO
    python3 scripts/build_ops_benchmark.py            # gera
    python3 scripts/build_ops_benchmark.py --check    # so' valida, nao escreve
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPS = os.path.join(REPO, "data", "knowledge", "rest-api-derived-ops.jsonl")
OUT = os.path.join(REPO, "data", "eval", "rest_api_benchmark_ops_40.jsonl")

# (pergunta, metodo, path). O id do alvo e' RESOLVIDO do arquivo derivado - nunca digitado.
CASOS: list[tuple[str, str, str]] = [
    ("Quero travar varios calendarios de uma vez, aplicando um filtro, sem precisar ir um por um.",
     "PUT", "/twsd/api/v2/model/calendar/action/lock"),
    ("Preciso destravar um calendario especifico que ficou travado, e eu tenho o identificador dele.",
     "PUT", "/twsd/api/v2/model/calendar/{calendar_id}/action/unlock"),
    ("Quero consultar um calendario especifico pelo identificador, e nao a lista toda.",
     "GET", "/twsd/api/v2/model/calendar/{calendar_id}"),
    ("Preciso cadastrar uma credencial nova no modelo, com usuario e senha, para um job usar depois.",
     "POST", "/twsd/api/v2/model/credentials"),
    ("Quero remover uma credencial especifica do modelo, informando o identificador dela.",
     "DELETE", "/twsd/api/v2/model/credentials/{credentials_id}"),
    ("Quero travar todos os dominios de uma vez, por filtro, para ninguem alterar enquanto eu mexo.",
     "PUT", "/twsd/api/v2/model/domain/action/lock"),
    ("Preciso obter um token de acesso ao servidor de licenca para falar com ele.",
     "GET", "/twsd/api/v2/engine/licenseServerAccessToken"),
    ("Quero disparar o comando de um componente do motor a partir da API, sem abrir sessao no servidor.",
     "PUT", "/twsd/api/v2/engine/run-component-command"),
    ("Quero disparar um comando no executor do motor pela API, remotamente.",
     "PUT", "/twsd/api/v2/engine/run-executor-command"),
    ("Preciso listar os nomes de usuario que existem no motor.",
     "GET", "/twsd/api/v2/engine/users"),
    ("Quero pegar um arquivo que esta no plano pelo identificador dele.",
     "GET", "/twsd/api/v2/plan/file/{file_id}"),
    ("Preciso travar uma pasta especifica do modelo, informando o identificador dela.",
     "PUT", "/twsd/api/v2/model/folder/{folder_id}/action/lock"),
    ("Quero apenas a contagem de objetos que estao dentro de uma pasta do plano, sem trazer a lista.",
     "GET", "/twsd/api/v2/plan/folder/objects-count"),
    ("Quero destravar uma definicao de job especifica do modelo, pelo identificador dela.",
     "PUT", "/twsd/api/v2/model/jobdefinition/{jobDefinition_id}/action/unlock"),
    ("Preciso consultar uma definicao de job do modelo pelo identificador, para ver como ela esta.",
     "GET", "/twsd/api/v2/model/jobdefinition/{jobDefinition_id}"),
    ("Um job terminou com sucesso e eu tratei a causa; quero confirmar esse sucesso no plano pela API.",
     "PUT", "/twsd/api/v2/plan/job/action/confirm-succ"),
    ("Um job terminou anormal e eu ja' corrigi; quero confirmar esse termino anormal no plano pela API.",
     "PUT", "/twsd/api/v2/plan/job/action/confirm-abend"),
    ("Preciso reexecutar um job que esta no plano, sem esperar o ciclo seguinte.",
     "PUT", "/twsd/api/v2/plan/job/action/rerun"),
    ("Quero matar um job que esta em execucao no plano, forcando o encerramento.",
     "PUT", "/twsd/api/v2/plan/job/action/kill"),
    ("Quero segurar um job no plano para que ele nao seja lancado ate' eu liberar.",
     "PUT", "/twsd/api/v2/plan/job/action/hold"),
    ("Preciso ver o log de um job do plano para entender por que ele falhou.",
     "GET", "/twsd/api/v2/plan/job/joblog"),
    ("Quero so' o numero de jobs que estao no plano, sem trazer a lista deles.",
     "GET", "/twsd/api/v2/plan/job/count"),
    ("Quero mandar executar um comando qualquer dentro de um job que esta no plano.",
     "PUT", "/twsd/api/v2/plan/job/action/run-command"),
    ("Preciso submeter um comando avulso para rodar como job, sem criar definicao antes.",
     "POST", "/twsd/api/v2/plan/job/submit-ad-hoc-job"),
    ("Quero o log de uma execucao especifica de um job do plano, identificando a execucao pelo run.",
     "GET", "/twsd/api/v2/plan/job/run/{run_id}/joblog"),
    ("Antes de agendar, quero calcular quais instancias de execucao um fluxo teria, a partir da definicao dele.",
     "POST", "/twsd/api/v2/model/jobstream/rc-evaluation"),
    ("Preciso aplicar uma acao em varios fluxos do modelo de uma vez, em lote.",
     "POST", "/twsd/api/v2/model/jobstream/bulk"),
    ("Quero segurar um fluxo que ja' esta no plano, para que nao seja lancado ate' eu liberar.",
     "PUT", "/twsd/api/v2/plan/jobstream/action/hold"),
    ("Quero submeter um fluxo do plano para execucao agora.",
     "POST", "/twsd/api/v2/plan/jobstream/submit"),
    ("Preciso desfazer as dependencias de um fluxo do plano para ele poder andar sozinho.",
     "PUT", "/twsd/api/v2/plan/jobstream/action/release-dependencies"),
    ("Quero descobrir quais acoes a API oferece para os objetos, para montar meu cliente.",
     "GET", "/twsd/api/v2/objects-info"),
    ("Um prompt esta esperando resposta e travando o fluxo; quero responder sim ou nao pela API.",
     "PUT", "/twsd/api/v2/plan/prompt/action/reply"),
    ("Quero ajustar quantas unidades de um recurso estao disponiveis no plano, aplicando um filtro.",
     "PUT", "/twsd/api/v2/plan/resource/action/update-quantity"),
    ("Preciso alterar um recurso especifico que esta no plano, informando o identificador.",
     "PATCH", "/twsd/api/v2/plan/resource/{resource_id}"),
    ("Quero calcular quais instancias de execucao um grupo de ciclos de execucao teria.",
     "POST", "/twsd/api/v2/model/runcyclegroup/rc-evaluation"),
    ("Quero consultar uma tabela de variaveis do modelo pelo identificador dela.",
     "GET", "/twsd/api/v2/model/variabletable/{variableTable_id}"),
    ("Preciso promover um no do plano a Master Domain Manager pela API.",
     "PUT", "/twsd/api/v2/plan/workstation/action/become-mdm"),
    ("Quero ajustar o valor de fence de varios nos do plano de uma vez, aplicando um filtro.",
     "PUT", "/twsd/api/v2/plan/workstation/action/update-fence"),
    ("Preciso tirar um no especifico do plano de circulacao, informando o identificador dele.",
     "PUT", "/twsd/api/v2/plan/workstation/{workstation_id}/action/set-offline"),
    ("Quero renovar o certificado do agente de um no especifico do plano, pelo identificador.",
     "PUT", "/twsd/api/v2/plan/workstation/{workstation_id}/action/update-cert"),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s).lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="nao escreve; so' valida")
    args = ap.parse_args()

    if not os.path.exists(OPS):
        print(f"ERRO: {OPS} nao existe. Rode: extract_rest_api.py --granularity operacao")
        return 2
    registros = [json.loads(l) for l in open(OPS, encoding="utf-8")]
    por_op = {r["operation"]: r for r in registros}

    linhas = []
    faltando = []
    for i, (pergunta, metodo, path) in enumerate(CASOS, 1):
        chave = f"{metodo} {path}"
        r = por_op.get(chave)
        if r is None:
            faltando.append(chave)
            continue
        linhas.append({
            "id": f"ops-{i:04d}",
            "question": pergunta,
            "relevant_claim_ids": [r["claim_id"]],
            "operation": chave,
            "family": r["resource"],
        })

    if faltando:
        print("ERRO: operacoes alvo nao encontradas no derivado:", file=sys.stderr)
        for f in faltando:
            print(f"  {f}", file=sys.stderr)
        return 2

    # ---- checagem 4: alvos distintos ----
    ids = [l["relevant_claim_ids"][0] for l in linhas]
    if len(set(ids)) != len(ids):
        print("ERRO: operacao alvo repetida entre as perguntas", file=sys.stderr)
        return 2

    # ---- checagens 1 e 2: a pergunta nao pode conter o path nem o summary literal ----
    vaz_path, vaz_summary = [], []
    for l in linhas:
        q = norm(l["question"])
        if norm(l["operation"]) in q:
            vaz_path.append(l["id"])
        alvo = por_op[l["operation"]]
        s = norm(alvo["supporting_quote"])
        # summary literal: qualquer sequencia de 4+ palavras do summary dentro da pergunta
        palavras = s.split()
        for j in range(len(palavras) - 3):
            if " ".join(palavras[j:j + 4]) in q:
                vaz_summary.append(l["id"])
                break

    # ---- checagem 3: cobertura de tokens pergunta<->registro alvo ----
    def toks(t: str) -> set[str]:
        return {w for w in re.findall(r"[a-z0-9_\-\.]+", norm(t)) if len(w) > 2}

    cob = []
    for l in linhas:
        alvo = por_op[l["operation"]]
        texto = " ".join(str(alvo.get(k, "")) for k in ("claim", "syntax", "supporting_quote"))
        qt = toks(l["question"])
        cob.append(len(qt & toks(texto)) / max(1, len(qt)))
    cob.sort()

    print(f"perguntas geradas      : {len(linhas)}")
    print(f"operacoes alvo distintas: {len(set(ids))}")
    print(f"familias cobertas       : {len({l['family'] for l in linhas})}")
    print(f"CHECK 1 - pergunta contem o path      : {len(vaz_path)} {vaz_path}")
    print(f"CHECK 2 - pergunta contem summary 4+  : {len(vaz_summary)} {vaz_summary}")
    print(f"CHECK 3 - cobertura de tokens: min={cob[0]:.2f} mediana={cob[len(cob)//2]:.2f} max={cob[-1]:.2f}")
    if vaz_path or vaz_summary:
        print("ERRO: vazamento detectado - benchmark DESCARTADO", file=sys.stderr)
        return 3
    if args.check:
        return 0

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        for l in linhas:
            fh.write(json.dumps(l, ensure_ascii=False) + "\n")
    print(f"gravado {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
