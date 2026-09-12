#!/usr/bin/env python3
"""P1c — Mescla as duas fontes e gera as claims finais do catalogo de mensagens.

Fonte A (autoritativa): catalogo compilado do produto 10.2.8 -> texto exato de TODOS os codigos.
Fonte B (enriquecimento): message help oficial da HCL -> Explanation / System action / Operator response.

Regra: a Fonte A define quais codigos existem e o texto canonico; a Fonte B enriquece quando disponivel.
Saida: data/evidence/official-verification-2026-09-11-message-catalog-full.jsonl
"""
import json, re, os

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
PROD = f"{BASE}/data/export/tws_messages_catalog_product.jsonl"
DOCS = f"{BASE}/data/export/tws_messages_catalog_v95.jsonl"
OUT = f"{BASE}/data/evidence/official-verification-2026-09-11-message-catalog-full.jsonl"

SEV = {"I": "informational", "W": "warning", "E": "error"}

FAM_LABEL = {
    "BHU": "conman", "BIA": "composer", "BIS": "plan library", "BCT": "conman/plan",
    "FAB": "installation (twsinst)", "DEM": "deployment", "DEG": "deployment engine",
    "DEO": "deployment engine", "DEA": "deployment engine", "DAB": "deployment",
    "BHT": "batchman", "JPL": "planner/planman", "ITA": "job management",
    "BDW": "dynamic workload", "BJB": "job", "BIJ": "job", "EDW": "EDWA/events",
    "CDW": "dynamic workload", "SAS": "scheduling", "BAB": "banner", "BAK": "banner",
    "UI0": "Dynamic Workload Console", "UI4": "Dynamic Workload Console",
}


def fam_label(code):
    f = code[3:6]
    return FAM_LABEL.get(f, f.lower())


def clean(t):
    t = re.sub(r"[\x00-\x1f]", " ", t or "")
    return re.sub(r"\s+", " ", t).strip()


def main():
    prod = {}
    for l in open(PROD, encoding="utf-8"):
        if l.strip():
            d = json.loads(l)
            prod[d["code"]] = d

    docs = {}
    for l in open(DOCS, encoding="utf-8"):
        if l.strip():
            d = json.loads(l)
            docs[d["code"]] = d

    n, enriched = 0, 0
    with open(OUT, "w", encoding="utf-8") as f:
        for code in sorted(prod):
            p = prod[code]
            texto = clean(p.get("text"))
            if not texto:
                continue
            sev = SEV.get(code[-1], "unknown")
            doc = docs.get(code)
            claim = (f"No HCL Workload Automation 10.2.8, a mensagem {code} "
                     f"(severidade: {sev}, familia AWS{code[3:6]} - {fam_label(code)}) "
                     f"tem o texto: \"{texto}\"")
            if doc:
                enriched += 1
                expl = clean(doc.get("explanation"))
                resp = clean(doc.get("response"))
                if expl and expl.lower() not in ("see message.", "see message"):
                    claim += f" Explicacao oficial: {expl}"
                if resp:
                    claim += f" Acao recomendada: {resp}"

            rec = {
                "claim_id": f"hwa-msgcat-{code.lower()}",
                "claim": claim,
                "status": "verified",
                "confidence": "high",
                "product": "HCL Workload Automation",
                "version": "10.2.8",
                "platform": "Distributed",
                "risk": "read_only",
                "operation_mode": "informational",
                "capability": "message_reference",
                "evidence_level": "official",
                "knowledge_status": "current",
                "message_text_source": "catalogo compilado do produto instalado (10.2.8)",
                "help_enriched_from_docs": bool(doc),
                "source_url": (doc.get("source_url") if doc
                               else p.get("source_url")),
                "source_title": (f"Message help (AWS{code[3:6]}) - HCL Workload Automation Messages and Codes"
                                 if doc else "Catalogo de mensagens do produto (10.2.8)"),
                "supporting_quote": f"{code}: {texto}",
                "retrieved_at": "2026-09-11",
                "synthetic_questions": [
                    f"O que significa a mensagem {code} no HCL Workload Automation 10.2.8?",
                    f"Qual o texto e a severidade da mensagem {code}?",
                    f"Como diagnosticar a mensagem {code}?",
                ],
                "context_prefix": (f"[Escopo: HCL Workload Automation 10.2.8 > Componente: {fam_label(code)} > "
                                   f"Interface: mensagem {code} > Topico: troubleshooting > messages [{code.lower()}]]"),
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
    print(f"claims geradas: {n} | enriquecidas com help oficial: {enriched}")
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
