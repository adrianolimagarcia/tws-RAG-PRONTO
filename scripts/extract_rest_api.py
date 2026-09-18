#!/usr/bin/env python3
"""Extrai a superficie da REST API do produto HWA (spec OpenAPI) e gera um DERIVADO
em PT-BR no padrao do dataset do RAG.

LICENCA — LEIA ANTES DE MEXER
-----------------------------
A spec OpenAPI e material do produto (HCL). Este script NAO grava a spec no
repositorio. O que vai ao git:
  (i)  este script (versionado);
  (ii) um jsonl DERIVADO por familia de recurso contendo: descricao PT-BR escrita
       por nos, a superficie funcional (metodo + path + resumo curto de cada
       operacao — fato de interface) e o source_url.
A spec crua nunca e escrita no repo: a leitura acontece do caminho externo e o
que nao vira superficie/resumo curto e descartado em memoria.

AGRUPAMENTO: um registro por TAG (familia de recurso), nao por operacao. Medido:
212 paths / 276 operacoes em 24 familias. Um registro por operacao inundaria o
corpus e repetiria a competicao de rank ja observada com as man pages.

Uso:  python3 scripts/extract_rest_api.py [--check] [--spec CAMINHO]
      --check  nao escreve; so reporta quantos registros seriam gerados
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys

DEFAULT_SPEC = os.environ.get(
    "REST_API_SPEC",
    "/root/workspace/tws-docs-raw/WA_API3_v2.json",
)
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(REPO, "data", "knowledge", "rest-api-derived.jsonl")
# Granularidade por OPERACAO (opt-in no corpus via RAG_REST_GRANULARITY=operation):
OUT_OPS = os.path.join(REPO, "data", "knowledge", "rest-api-derived-ops.jsonl")

METODOS = ("get", "post", "put", "delete", "patch")
QUOTE_LIMIT = 160
OPS_LIMIT = 40  # operacoes listadas por registro; o resto vira contagem

# Descricao PT-BR por familia de recurso. Escrita por nos, nao e' traducao da spec.
#
# ACENTUACAO OBRIGATORIA (medido, nao estetica): o tokenizador do avaliador usa
# [A-Za-z0-9_...] e QUEBRA palavras no acento. Texto derivado em ASCII contra
# pergunta em PT-BR acentuado nunca casa ('producao' vs 'produção' -> 'produ').
# Medido no benchmark REST: @1 1/40 (ASCII) -> 3/40 (acentuado), @10 7 -> 9, e sem
# custo nos outros benchmarks (blind v3 184 e 70q 53 inalterados). Corrigir o
# tokenizador em vez do dado foi testado e REGRIDE: normalizar acento derruba
# singular/plural de 8/8 para 0/8 e custa -5 no blind v3; com stem volta a 6/6 mas
# custa -7. O acento aqui e' o fix correto.
DESC: dict[str, str] = {
    "V2 APIs - Engine": "Estado e operação do próprio motor: informações do engine, grupos, usuários e acesso ao servidor de licença. É por aqui que se consulta a saúde do motor pela API, sem usar o conman.",
    "V2 APIs - Calendar": "Calendários do modelo: consulta, criação, alteração, remoção e as ações de travar/destravar um calendário antes de editá-lo. O par lock/unlock é o que evita que duas sessões escrevam no mesmo objeto.",
    "V2 APIs - Credentials": "Objetos de credencial do modelo (usuário/senha usados por jobs): CRUD mais as ações de lock/unlock. A senha nunca é lida de volta pela API.",
    "V2 APIs - Domain": "Domínio do modelo: consulta e as ações de lock/unlock. Descreve a topologia de domínio que o motor usa.",
    "V2 APIs - Folder": "Pastas do modelo: CRUD e lock/unlock. Pastas são o mecanismo de organização e de permissão dos objetos de agendamento.",
    "V2 APIs - Job Definition": "Definições de job no MODELO (o que o composer manipula): CRUD e lock/unlock. Não confundir com 'Job In Plan', que é a instância em execução.",
    "V2 APIs - Job In Plan": "Jobs no PLANO de produção (a instância agendada, equivalente ao que o conman mostra): consulta, alteração, cancelamento, re-execução e manipulação de dependências. É a maior família da API.",
    "V2 APIs - Job Stream": "Job streams no MODELO: CRUD e lock/unlock das definições de fluxo.",
    "V2 APIs - Job Stream In Plan": "Job streams no PLANO: consulta e operação das instâncias agendadas — liberar, cancelar, re-executar e inspecionar o estado.",
    "V2 APIs - Prompt": "Prompts do modelo: CRUD e lock/unlock das definições de prompt.",
    "V2 APIs - Prompt In Plan": "Prompts no plano: consulta e resposta a prompts que estão aguardando (o equivalente API do 'conman reply').",
    "V2 APIs - Resource": "Recursos do modelo: CRUD e lock/unlock. Recursos são os contadores de unidades que limitam concorrência.",
    "V2 APIs - Resource In Plan": "Recursos no plano: consulta e alteração do número de unidades disponíveis em produção.",
    "V2 APIs - Run Cycle Group": "Grupos de ciclos de execução: consulta e operação dos grupos que agrupam instâncias de job stream em produção.",
    "V2 APIs - Variable": "Variáveis do modelo: CRUD e lock/unlock.",
    "V2 APIs - Variable Table": "Tabelas de variáveis do modelo: CRUD e lock/unlock.",
    "V2 APIs - Workload Application Template": "Templates de aplicação de workload: CRUD e lock/unlock dos modelos reutilizáveis de aplicação.",
    "V2 APIs - Workstation": "Workstations no MODELO: CRUD e lock/unlock das definições de nó.",
    "V2 APIs - Workstation Class": "Classes de workstation no modelo: CRUD e lock/unlock.",
    "V2 APIs - Workstation In Plan": "Workstations no PLANO: consulta de estado, link/unlink, fence e limite de jobs concorrentes — o equivalente API do que o conman mostra em showcpus.",
    "V2 APIs - File In Plan": "Dependências de ARQUIVO no plano: consulta das dependências de arquivo das instâncias agendadas.",
    "V2 APIs - Workspace": "Workspaces: agrupamento de nível mais alto para os objetos de agendamento.",
    "V2 APIs - Objects Info": "Informações consolidadas sobre objetos: consulta agregada que atravessa vários tipos.",
    "V2 APIs - Folder plan": "Pastas no plano de produção: consulta e navegação das pastas na instância em execução.",
}


def carregar(spec_path: str) -> dict:
    if not os.path.exists(spec_path):
        sys.exit(
            f"spec nao encontrada em {spec_path}\n"
            "a spec e material do produto e nao fica no repo; aponte --spec ou "
            "exporte REST_API_SPEC para o caminho externo."
        )
    with open(spec_path, encoding="utf-8") as fh:
        return json.load(fh)


def resumo_curto(op: dict) -> str:
    """Resumo curto da operacao: o summary do produto, truncado.

    Preferimos `summary` a `description`: o summary e' uma linha funcional
    ('Queries calendar definitions'), o description e' prosa do manual.
    """
    s = (op.get("summary") or "").strip()
    if not s:
        s = (op.get("description") or "").strip().split(".")[0]
    s = " ".join(s.split())
    return s[:QUOTE_LIMIT]


MAX_CAMPOS_SCHEMA = 25  # campos de schema por familia (limita o tamanho do texto)


def vocab_da_spec(spec: dict, tag: str, brutos: list[tuple[str, str, dict]]) -> str:
    """Vocabulario da familia extraido MECANICAMENTE da spec OpenAPI do produto.

    REGRA DECLARADA (e' o que torna este enriquecimento legitimo, e nao tautologia):
    este texto vem SO' da spec. Nenhum termo e' escrito a mao, e nenhum foi escolhido
    olhando a redacao das perguntas do benchmark. Qualquer terceiro que re-execute
    este extrator sobre a mesma spec obtem exatamente o mesmo texto - a regra e'
    VERIFICAVEL por re-execucao, nao uma promessa.

    Motivo: a cobertura de tokens pergunta<->registro-alvo medida era de 26%, e a
    pergunta usa o vocabulario do operador enquanto o registro trazia apenas o resumo
    curto da operacao. Aqui entram os textos que a PROPRIA spec ja' trazia e que
    ficavam de fora: descricao da tag, summary e description COMPLETOS de cada
    operacao, nomes de parametro, e nomes de schema e de campo dos schemas
    referenciados por essas operacoes.
    """
    partes: list[str] = []

    for t in spec.get("tags") or []:
        if isinstance(t, dict) and t.get("name") == tag and t.get("description"):
            partes.append(str(t["description"]))

    schemas = ((spec.get("components") or {}).get("schemas") or {})
    nomes_schema: set[str] = set()

    for _path, _metodo, op in brutos:
        if op.get("summary"):
            partes.append(str(op["summary"]))
        if op.get("description"):
            partes.append(str(op["description"]))
        for par in op.get("parameters") or []:
            if isinstance(par, dict) and par.get("name"):
                partes.append(str(par["name"]))
        for m in re.findall(r"#/components/schemas/([A-Za-z0-9_.\-]+)",
                            json.dumps(op, ensure_ascii=False)):
            nomes_schema.add(m)

    for nome in sorted(nomes_schema):
        partes.append(nome)
        props = ((schemas.get(nome) or {}).get("properties") or {})
        for campo in list(props)[:MAX_CAMPOS_SCHEMA]:
            partes.append(str(campo))

    return " ".join(dict.fromkeys(" ".join(partes).split()))


def slug_operacao(metodo: str, path: str) -> str:
    """Id estavel para uma operacao. `operationId` existe em apenas 1 das 276 operacoes da
    spec, entao o id vem de METODO+PATH, que e' unico por construcao."""
    bruto = f"{metodo}-{path}"
    return re.sub(r"[^a-z0-9]+", "-", bruto.lower()).strip("-")[:90]


def build_por_operacao(spec_path: str) -> list[dict]:
    """UM REGISTRO POR OPERACAO (276 na spec), em vez de um por familia (24).

    POR QUE EXISTE: com um registro por familia o benchmark SATURA na acuracia do
    classificador - nao ha' o que escolher dentro da familia, entao nenhuma melhoria de
    RANKING e' mensuravel. Medido: rotear para a familia prevista da 94,4% e e'
    aritmeticamente identico a acertar a classificacao. Com um registro por operacao o
    recuperador tem de escolher entre 276 candidatos e o ground truth passa a ser a
    OPERACAO, o que torna a medicao de ranking possivel.

    REGRA DECLARADA (mesma dos outros derivados): o texto do registro vem SO' da spec -
    summary e description da propria operacao, mais metodo e path. Nada e' escrito a mao
    e nada vem da redacao das perguntas do benchmark. Qualquer terceiro re-executa o
    extrator sobre a mesma spec e obtem o mesmo texto.

    GRANULARIDADE E' OPT-IN: este arquivo so' entra no corpus com
    RAG_REST_GRANULARITY=operation. O default continua sendo um registro por familia.
    """
    spec = carregar(spec_path)
    info = spec.get("info") or {}
    versao = str(info.get("version") or "?")
    records: list[dict] = []
    vistos: set[str] = set()

    for path, item in sorted((spec.get("paths") or {}).items()):
        if not isinstance(item, dict):
            continue
        for metodo, op in item.items():
            if metodo not in METODOS or not isinstance(op, dict):
                continue
            tags = op.get("tags") or ["(sem tag)"]
            recurso = str(tags[0]).replace("V2 APIs - ", "").strip()
            resumo = " ".join(str(op.get("summary") or "").split())
            descricao = " ".join(str(op.get("description") or "").split())
            m = metodo.upper()
            oid = f"hwa-10.2.8-rest-op-{slug_operacao(m, path)}-0001"
            if oid in vistos:
                raise SystemExit(f"COLISAO de id de operacao: {oid} ({m} {path})")
            vistos.add(oid)
            texto = f"REST API V2 — {recurso} — {m} {path}: {resumo}. {descricao}".strip()
            records.append({
                "claim_id": oid,
                "kind": "rest_api_operation",
                "resource": recurso,
                "operation": f"{m} {path}",
                "claim": texto,
                "syntax": f"{m} {path}",
                "supporting_quote": resumo[:QUOTE_LIMIT],
                "source_title": f"REST API V2 — {recurso} (HWA 10.2.8, spec v{versao})",
                "source_url": f"/twsd/api/v2 — {m} {path}",
                "status": "documented_not_exercised_in_lab",
                "result": "SUCCESS",
            })
    return records


def build(spec_path: str, incluir_vocab: bool = False) -> list[dict]:
    """Monta os registros derivados. `incluir_vocab` e' OPT-IN e default OFF.

    POR QUE O DEFAULT E' OFF — MEDIDO E REJEITADO: enriquecer os registros com o
    vocabulario da spec elevou a cobertura de tokens pergunta<->registro de 26,0%
    para 31,6% e mesmo assim PIOROU a recuperacao: benchmark REST @1 5/40 -> 3/40,
    @10 12/40 -> 7/40, MRR 0,1942 -> 0,1077. Causa: os registros passaram de ~50
    tokens para mediana de 754 caracteres, e o vocabulario acrescentado e'
    COMPARTILHADO entre as familias ('REST API', 'model', 'plan', 'object', 'id'),
    logo tem IDF baixo, nao discrimina, e a normalizacao por tamanho do BM25 pune.
    Mesmo padrao ja' observado nas man pages. Fica atras do flag para que a
    regeneracao padrao produza a versao BOA e o experimento siga reproduzivel.
    """
    spec = carregar(spec_path)
    paths = spec.get("paths") or {}
    info = spec.get("info") or {}
    versao = str(info.get("version") or "?")

    familias: dict[str, list[tuple[str, str, str]]] = collections.defaultdict(list)
    brutos: dict[str, list[tuple[str, str, dict]]] = collections.defaultdict(list)
    sem_tag = 0
    for path, item in sorted(paths.items()):
        for metodo, op in item.items():
            if metodo not in METODOS or not isinstance(op, dict):
                continue
            tags = op.get("tags") or []
            if not tags:
                sem_tag += 1
                tags = ["(sem tag)"]
            for t in tags:
                familias[t].append((metodo.upper(), path, resumo_curto(op)))
                brutos[t].append((path, metodo, op))

    if sem_tag:
        print(f"AVISO: {sem_tag} operacoes sem tag", file=sys.stderr)

    records: list[dict] = []
    for tag in sorted(familias):
        ops = familias[tag]
        recurso = tag.replace("V2 APIs - ", "").strip()
        desc = DESC.get(tag)
        if not desc:
            desc = f"Familia de recurso '{recurso}' da API V2 (documentada no produto; descricao PT-BR pendente)."
        listadas = ops[:OPS_LIMIT]
        superficie = " | ".join(f"{m} {p}" for m, p, _ in listadas)
        if len(ops) > OPS_LIMIT:
            superficie += f" | (+{len(ops) - OPS_LIMIT} operacoes)"
        records.append({
            "claim_id": f"hwa-10.2.8-rest-{recurso.lower().replace(' ', '-')}-0001",
            "kind": "rest_api_surface",
            "resource": recurso,
            "claim": f"REST API V2 — {recurso}: {desc}",
            "syntax": superficie,
            "vocab_spec": (vocab_da_spec(spec, tag, brutos[tag]) if incluir_vocab else ""),
            "operations": [
                {"method": m, "path": p, "summary": s} for m, p, s in listadas
            ],
            "supporting_quote": (listadas[0][2] if listadas else "")[:QUOTE_LIMIT],
            "source_title": f"REST API V2 — {recurso} (HWA 10.2.8, spec v{versao})",
            "source_url": f"/twsd/api/v2 — tag '{tag}'",
            "n_operations": len(ops),
            "status": "documented_not_exercised_in_lab",
            "result": "SUCCESS",
        })
    return records


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="nao escreve; so reporta")
    ap.add_argument("--spec", default=DEFAULT_SPEC, help="caminho da spec OpenAPI")
    ap.add_argument("--vocab-spec", action="store_true",
                    help="enriquece com o vocabulario da spec. MEDIDO E REJEITADO: "
                         "melhora a cobertura de tokens mas piora a recuperacao "
                         "(REST @1 5/40 -> 3/40). Default OFF de proposito.")
    ap.add_argument("--granularity", choices=("familia", "operacao"), default="familia",
                    help="'familia' (default) = 24 registros, um por familia - o corpus "
                         "atual. 'operacao' = 276 registros, um por operacao, com ground "
                         "truth por OPERACAO, que e' o unico jeito de medir RANKING "
                         "(com um registro por familia o benchmark satura na acuracia do "
                         "classificador). O arquivo de operacao e' opt-in no corpus: "
                         "RAG_REST_GRANULARITY=operation.")
    args = ap.parse_args()

    if args.granularity == "operacao":
        recs = build_por_operacao(args.spec)
        destino = OUT_OPS
        if args.check:
            recursos = {r["resource"] for r in recs}
            ids = {r["claim_id"] for r in recs}
            print(f"seriam gerados {len(recs)} registros (granularidade=operacao)")
            print(f"  ids unicos         : {len(ids)}")
            print(f"  familias cobertas  : {len(recursos)}")
            print(f"  sem summary        : {sum(1 for r in recs if not r['supporting_quote'].strip())}")
            return 0
    else:
        recs = build(args.spec, incluir_vocab=args.vocab_spec)
        destino = OUT
        if args.check:
            tot_ops = sum(r["n_operations"] for r in recs)
            print(f"seriam gerados {len(recs)} registros (granularidade=familia)")
            print(f"  operacoes cobertas : {tot_ops}")
            print(f"  com descricao PT-BR: {sum(1 for r in recs if 'pendente' not in r['claim'])}")
            print(f"  com sintaxe        : {sum(1 for r in recs if r['syntax'])}")
            print(f"  quote > {QUOTE_LIMIT} chars  : {sum(1 for r in recs if len(r['supporting_quote']) > QUOTE_LIMIT)}")
            return 0

    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"gravado {destino} com {len(recs)} registros")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
