#!/usr/bin/env python3
"""P1 — Gera claims canonicas a partir do catalogo de mensagens extraido (HCL docs).

Saida: data/evidence/official-verification-2026-09-11-message-catalog.jsonl
Uma claim por codigo de mensagem, preservando o texto original em ingles (fonte autoritativa),
com marcacao explicita de versao da fonte (9.5) e do catalogo do produto (10.2.8).
"""
import json, re, os

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
SRC = f"{BASE}/data/export/tws_messages_catalog_v95.jsonl"
OUT = f"{BASE}/data/evidence/official-verification-2026-09-11-message-catalog.jsonl"
PROD = "/tmp/real_codes.txt"

SEV = {"I": "informational", "W": "warning", "E": "error"}
FAM_NAME = {
    "BHU": "conman", "BIA": "composer", "BIS": "plan library", "BCT": "conman/plan",
    "FAB": "installation/agent", "DEM": "deployment", "DEG": "deployment", "DEO": "deployment",
    "BHT": "batchman", "JPL": "planner/planman", "ITA": "ITA/agent", "BDW": "dynamic workload",
    "BJB": "job", "BIJ": "job", "EDW": "EDWA/events", "CDW": "dynamic workload",
    "BIN": "plan libraries", "BHV": "conman", "BIU": "job", "BDC": "dynamic workload",
}


def fam_label(code):
    f = code[3:6]
    return FAM_NAME.get(f, f.lower())


def main():
    prod = set(l.strip() for l in open(PROD) if l.strip())
    msgs = [json.loads(l) for l in open(SRC, encoding="utf-8") if l.strip()]
    n = 0
    with open(OUT, "w", encoding="utf-8") as f:
        for m in msgs:
            code = m["code"]
            sev = SEV.get(code[-1], "unknown")
            texto = m.get("text", "").strip()
            expl = (m.get("explanation") or "").strip()
            resp = (m.get("response") or "").strip()
            if not texto:
                continue
            in_prod = code in prod
            claim = (
                f"No HCL Workload Automation, a mensagem {code} (severidade: {sev}, "
                f"familia AWS{code[3:6]} - {fam_label(code)}) indica: \"{texto}\""
            )
            if expl and expl.lower() not in ("see message.", "see message"):
                claim += f" Explicacao oficial: {expl}"
            if resp:
                claim += f" Acao recomendada ao usuario: {resp}"
            if not in_prod:
                claim += (" [Observacao: codigo nao localizado no catalogo do produto 10.2.8 "
                          "deste laboratorio; pode ser de outro componente ou versao.]")

            rec = {
                "claim_id": f"hwa-msgcat-{code.lower()}",
                "claim": claim,
                "status": "verified",
                "confidence": "high" if in_prod else "medium",
                "product": "HCL Workload Automation",
                "version": "9.5 (fonte) / 10.2.8 (produto)",
                "platform": "Distributed",
                "risk": "read_only",
                "operation_mode": "informational",
                "capability": "message_reference",
                "evidence_level": "official",
                "knowledge_status": "current",
                "code_in_product_1028": in_prod,
                "source_url": m.get("source_url"),
                "source_title": f"Message help (AWS{code[3:6]}) - HCL Workload Automation Messages and Codes",
                "source_version": "9.5",
                "supporting_quote": f"{code}: {texto}",
                "retrieved_at": "2026-09-11",
                "synthetic_questions": [
                    f"O que significa a mensagem {code} no HCL Workload Automation?",
                    f"Como resolver ou diagnosticar o erro {code}?",
                    f"Qual a severidade e a familia da mensagem {code}?",
                ],
                "context_prefix": (f"[Escopo: HCL Workload Automation > Componente: {fam_label(code)} > "
                                   f"Interface: mensagem {code} > Topico: troubleshooting > messages [{code.lower()}]]"),
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
    print(f"geradas {n} claims -> {OUT}")


if __name__ == "__main__":
    main()
