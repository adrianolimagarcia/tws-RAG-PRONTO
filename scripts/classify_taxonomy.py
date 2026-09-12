#!/usr/bin/env python3
"""P2 — Classificador de taxonomia melhorado (teste offline).

Regras ordenadas do mais especifico ao mais generico, aplicadas sobre prefixo + texto da claim.
Troubleshooting fica por ULTIMO entre as categorias uteis (e catch-all de mensagens/erros),
evitando que ele capture claims que pertencem a categorias mais especificas.
Objetivo: reduzir "Outros" sem inflar artificialmente nenhuma categoria.
"""
import json
import re
from collections import Counter

RULES = [
    ("Alta Disponibilidade & Failover",
     ["high_availability", "high availability", "alta disponibilidade", "failover", "fail-over",
      "switchmgr", "switch manager", "standby", "active/standby", "ativo/standby", "takeover",
      "quorum", "hot standby", "cold standby", "redundan"]),

    ("API REST v2 & Integracao",
     ["rest api", "api rest", "rest v2", "/twsd/", "openapi", "swagger", "endpoint", "webhook",
      "integracao", "integration", "json payload", "oauth", "token de api", "curl -x",
      "postman", "apikey", "api key"]),

    ("Operacao CLI (conman/composer/planman)",
     ["conman", "composer", "planman", "optman", "batchman", "mailman", "netman", "startmon",
      "linha de comando", "command line", "ocli", "orchestration cli",
      "mgr ", "dumpsec", "makesec", "switchplan", "jnextplan"]),

    ("Agendamento Avancado & Workflows",
     ["scheduling", "agendamento", "runcycle", "run cycle", "calendario", "calendar", "vartable",
      "prompt", "job stream", "jobstream", "workflow", "dependenc", "dependencia", "at dependency",
      "follows", "needs", "recovery", "recuperacao", "carryforward", "carry forward", "time zone",
      "fuso horario", "critical path", "caminho critico", "resource", "recurso",
      "workstation", "estacao de trabalho", "opens", "requires"]),

    ("Instalacao & Manutencao",
     ["install", "instalacao", "upgrade", "atualizacao", "fix pack", "fixpack", "patch",
      "manutencao", "maintenance", "backup", "restore", "migra", "silent install", "prereq",
      "requisito", "db2", "postgres", "oracle", "database", "banco de dados", "tablespace", "jdbc",
      "uninstall", "desinstal", "license", "licenca"]),

    ("Arquitetura & Topologia Mesh",
     ["architecture", "arquitetura", "topologia", "topology", "mesh", "fta", "fault tolerant",
      "dynamic agent", "dynamic workload", "broker", "domain manager", "master domain manager",
      "mdm", "dwc", "dynamic workload console", "engine", "modelo de dominio", "domain model",
      "protocolo", "protocol", "componente", "component", "cluster", "nodo", "node ",
      "agente", "agent ", "z/os", "zcentric", "caminho de comunicacao", "certificad", "handshake",
      "localopts"]),

    # Catch-all de mensagens/erros — por ultimo, so pega o que nao casou acima
    ("Troubleshooting & Mensagens de Erro",
     ["troubleshoot", "error", "erro", "mensagem", "message", "diagnos", "abend", "falha",
      "failure", "symptom", "sintoma", "stack trace", "exception", "codigo de erro", "aws"]),
]


def classify(prefix, claim):
    t = f"{prefix} {claim}".lower()
    # Prioridade ALTA para HA/failover: mensagens de failover (contem codigo AWS + 'mensagem')
    # nao devem cair na regra de catalogo de mensagens (Troubleshooting) abaixo.
    ha_strong = ["failover", "fail-over", "alta disponibilidade", "high availab", "switchmgr",
                 "backup master", "standby", "switch domain manager", "takeover",
                 "unavailable master", "promote", "demote"]
    if any(k in t for k in ha_strong):
        return "Alta Disponibilidade & Failover"
    # Alta prioridade: claim que E SOBRE uma mensagem de erro (catalogo de mensagens),
    # independentemente do componente citado no prefixo.
    if re.search(r"\baws[a-z]{3}\d{3}[iwe]\b", t) and ("mensagem" in t or "message" in t):
        return "Troubleshooting & Mensagens de Erro"
    for cat, kws in RULES:
        for k in kws:
            if k in t:
                return cat
    return "Outros"


def main():
    rows = [json.loads(l) for l in open(
        '/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/'
        'data/export/tws_corpus_master_consolidated.jsonl', encoding='utf-8') if l.strip()]
    old, new = Counter(), Counter()
    changed = 0
    for r in rows:
        o = r.get('category', 'Outros')
        n = classify(r.get('context_prefix') or '', r.get('claim') or '')
        old[o] += 1
        new[n] += 1
        if o != n:
            changed += 1
    print(f"total: {len(rows)} | claims reclassificadas: {changed} ({100*changed/len(rows):.1f}%)\n")
    cats = sorted(set(old) | set(new))
    print(f"{'CATEGORIA':<45} {'ANTES':>8} {'DEPOIS':>8} {'%':>7}")
    for c in cats:
        print(f"{c:<45} {old.get(c,0):>8} {new.get(c,0):>8} {100*new.get(c,0)/len(rows):>6.1f}%")
    print(f"\nOutros: {old.get('Outros',0)} ({100*old.get('Outros',0)/len(rows):.1f}%)"
          f" -> {new.get('Outros',0)} ({100*new.get('Outros',0)/len(rows):.1f}%)")


if __name__ == "__main__":
    main()
