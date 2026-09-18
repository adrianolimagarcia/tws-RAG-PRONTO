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
import sys

DEFAULT_SPEC = os.environ.get(
    "REST_API_SPEC",
    "/root/workspace/tws-docs-raw/WA_API3_v2.json",
)
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(REPO, "data", "knowledge", "rest-api-derived.jsonl")

METODOS = ("get", "post", "put", "delete", "patch")
QUOTE_LIMIT = 160
OPS_LIMIT = 40  # operacoes listadas por registro; o resto vira contagem

# Descricao PT-BR por familia de recurso. Escrita por nos, nao e' traducao da spec.
DESC: dict[str, str] = {
    "V2 APIs - Engine": "Estado e operacao do proprio motor: informacoes do engine, grupos, usuarios e acesso ao servidor de licenca. E por aqui que se consulta a saude do motor pela API, sem usar o conman.",
    "V2 APIs - Calendar": "Calendarios do modelo: consulta, criacao, alteracao, remocao e as acoes de travar/destravar um calendario antes de edita-lo. O par lock/unlock e o que evita que duas sessoes escrevam no mesmo objeto.",
    "V2 APIs - Credentials": "Objetos de credencial do modelo (usuario/senha usados por jobs): CRUD mais as acoes de lock/unlock. A senha nunca e' lida de volta pela API.",
    "V2 APIs - Domain": "Dominio do modelo: consulta e as acoes de lock/unlock. Descreve a topologia de dominio que o motor usa.",
    "V2 APIs - Folder": "Pastas do modelo: CRUD e lock/unlock. Pastas sao o mecanismo de organizacao e de permissao dos objetos de agendamento.",
    "V2 APIs - Job Definition": "Definicoes de job no MODELO (o que o composer manipula): CRUD e lock/unlock. Nao confundir com 'Job In Plan', que e' a instancia em execucao.",
    "V2 APIs - Job In Plan": "Jobs no PLANO de producao (a instancia agendada, equivalente ao que o conman mostra): consulta, alteracao, cancelamento, re-execucao e manipulacao de dependencias. E a maior familia da API.",
    "V2 APIs - Job Stream": "Job streams no MODELO: CRUD e lock/unlock das definicoes de fluxo.",
    "V2 APIs - Job Stream In Plan": "Job streams no PLANO: consulta e operacao das instancias agendadas — liberar, cancelar, re-executar e inspecionar o estado.",
    "V2 APIs - Prompt": "Prompts do modelo: CRUD e lock/unlock das definicoes de prompt.",
    "V2 APIs - Prompt In Plan": "Prompts no plano: consulta e resposta a prompts que estao aguardando (o equivalente API do 'conman reply').",
    "V2 APIs - Resource": "Recursos do modelo: CRUD e lock/unlock. Recursos sao os contadores de unidades que limitam concorrencia.",
    "V2 APIs - Resource In Plan": "Recursos no plano: consulta e alteracao do numero de unidades disponiveis em producao.",
    "V2 APIs - Run Cycle Group": "Grupos de ciclos de execucao: consulta e operacao dos grupos que agrupam instancias de job stream em producao.",
    "V2 APIs - Variable": "Variaveis do modelo: CRUD e lock/unlock.",
    "V2 APIs - Variable Table": "Tabelas de variaveis do modelo: CRUD e lock/unlock.",
    "V2 APIs - Workload Application Template": "Templates de aplicacao de workload: CRUD e lock/unlock dos modelos reutilizaveis de aplicacao.",
    "V2 APIs - Workstation": "Workstations no MODELO: CRUD e lock/unlock das definicoes de no.",
    "V2 APIs - Workstation Class": "Classes de workstation no modelo: CRUD e lock/unlock.",
    "V2 APIs - Workstation In Plan": "Workstations no PLANO: consulta de estado, link/unlink, fence e limite de jobs concorrentes — o equivalente API do que o conman mostra em showcpus.",
    "V2 APIs - File In Plan": "Dependencias de ARQUIVO no plano: consulta das dependencias de arquivo das instancias agendadas.",
    "V2 APIs - Workspace": "Workspaces: agrupamento de nivel mais alto para os objetos de agendamento.",
    "V2 APIs - Objects Info": "Informacoes consolidadas sobre objetos: consulta agregada que atravessa varios tipos.",
    "V2 APIs - Folder plan": "Pastas no plano de producao: consulta e navegacao das pastas na instancia em execucao.",
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


def build(spec_path: str) -> list[dict]:
    spec = carregar(spec_path)
    paths = spec.get("paths") or {}
    info = spec.get("info") or {}
    versao = str(info.get("version") or "?")

    familias: dict[str, list[tuple[str, str, str]]] = collections.defaultdict(list)
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
    args = ap.parse_args()

    recs = build(args.spec)
    if args.check:
        tot_ops = sum(r["n_operations"] for r in recs)
        print(f"seriam gerados {len(recs)} registros")
        print(f"  operacoes cobertas : {tot_ops}")
        print(f"  com descricao PT-BR: {sum(1 for r in recs if 'pendente' not in r['claim'])}")
        print(f"  com sintaxe        : {sum(1 for r in recs if r['syntax'])}")
        print(f"  quote > {QUOTE_LIMIT} chars  : {sum(1 for r in recs if len(r['supporting_quote']) > QUOTE_LIMIT)}")
        return 0

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"gravado {OUT} com {len(recs)} registros")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
