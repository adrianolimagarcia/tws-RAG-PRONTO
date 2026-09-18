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
