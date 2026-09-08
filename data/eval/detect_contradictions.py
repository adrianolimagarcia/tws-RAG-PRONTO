#!/usr/bin/env python3
"""Detector de contradicoes e conflitos no corpus TWS/HWA.
Agrupa claims por topico/subtopico e identifica potenciais inconsistencias:
- Divergencias de default em globalopts (ex: sd=0000 vs sd=0005)
- Afirmacoes sobre comandos suportados em versoes conflitantes
- Claims 'current' que colidam em afirmacoes booleanas sem nota contrastiva
"""
import json, os, re
from collections import defaultdict

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CLAIMS_FILE = os.path.join(REPO_DIR, "data", "evidence", "claims.jsonl")

def analyze_contradictions():
    if not os.path.exists(CLAIMS_FILE):
        print("Arquivo claims.jsonl nao encontrado.")
        return

    claims = [json.loads(line) for line in open(CLAIMS_FILE)]
    print(f"Total de claims analisadas: {len(claims)}")

    by_topic = defaultdict(list)
    for c in claims:
        t = c.get("topic") or "sem_topico"
        st = c.get("subtopic") or "sem_subtopico"
        by_topic[(t, st)].append(c)

    potential_conflicts = []

    # 1. Checagem de pares contrastivos orfaos
    contrasts = [c for c in claims if "PAR CONTRASTIVO" in c.get("claim", "")]
    print(f"Pares contrastivos explicitamente mapeados no corpus: {len(contrasts)}")

    # 2. Checagem de palavras-chave mutuamente exclusivas no mesmo topico
    exclusive_patterns = [
        ("suportado", "nao suportado"),
        ("exclusivo", "compartilhado"),
        ("obrigatorio", "opcional"),
        ("0000", "0005"),
        ("true", "false"),
    ]

    for (top, sub), group in by_topic.items():
        if len(group) < 2:
            continue
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                c1 = group[i]
                c2 = group[j]
                
                # Se ja e par contrastivo documentado, ok
                if "contrast" in c1.get("claim_id", "") or "contrast" in c2.get("claim_id", ""):
                    continue
                if c1.get("knowledge_status") != "current" or c2.get("knowledge_status") != "current":
                    continue

                t1 = c1.get("claim", "").lower()
                t2 = c2.get("claim", "").lower()

                for p1, p2 in exclusive_patterns:
                    if (p1 in t1 and p2 in t2) or (p2 in t1 and p1 in t2):
                        # Verificar se compartilham a mesma entidade/objeto
                        words1 = set(re.findall(r"[A-Za-z0-9_]{4,}", t1))
                        words2 = set(re.findall(r"[A-Za-z0-9_]{4,}", t2))
                        shared = words1.intersection(words2) - {"workload", "automation", "versao", "comando", "tivoli", "scheduler"}
                        if len(shared) >= 2:
                            potential_conflicts.append({
                                "topic": f"{top}/{sub}",
                                "shared_terms": list(shared)[:5],
                                "claim1": {"id": c1["claim_id"], "text": c1["claim"][:100]},
                                "claim2": {"id": c2["claim_id"], "text": c2["claim"][:100]},
                            })

    print(f"Potenciais conflitos encontrados para auditoria humana: {len(potential_conflicts)}")
    out_file = os.path.join(REPO_DIR, "data", "eval", "contradiction_audit.json")
    with open(out_file, "w") as f:
        json.dump(potential_conflicts, f, indent=2, ensure_ascii=False)
    print(f"Relatório de auditoria salvo em {out_file}")

if __name__ == "__main__":
    analyze_contradictions()
