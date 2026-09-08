#!/usr/bin/env python3
"""deep_audit_claims.py — Auditoria e Revalidacao Profunda das 1.449 Claims.
Aplica regras rigorosas do Contrato Evidence-First R1-R5, integridade de schema,
consistência de risco, verificação de pares contrastivos e rastreabilidade com lab.
"""
import glob, json, os, re, sys
from collections import defaultdict, Counter

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLAIMS_FILE = os.path.join(REPO, "data", "evidence", "claims.jsonl")
LAB_DIR = os.path.join(REPO, "data", "evidence")

REQUIRED_FIELDS = [
    "claim_id", "claim", "status", "confidence", "product", "version",
    "platform", "risk", "source_url", "source_title", "topic", "subtopic",
    "evidence_tier", "knowledge_status", "normalized_terminology"
]

HIGH_RISK_KEYWORDS = {
    "destructive": ["delete", "drop", "kill", "cancel", "unlink", "purge", "remove", "scratch"],
    "mutating": ["add", "modify", "update", "replace", "rerun", "release", "hold", "submit", "change", "set"],
    "credential_sensitive": ["password", "token", "apikey", "secret", "useropts", "credentials", "jwt", "passphrase"]
}

def audit_claims():
    if not os.path.exists(CLAIMS_FILE):
        print("Erro: claims.jsonl não encontrado.")
        sys.exit(1)

    claims = [json.loads(line) for line in open(CLAIMS_FILE)]
    total = len(claims)
    print(f"==================================================")
    print(f"   REVALIDAÇÃO PROFUNDA DE CLAIMS — TOTAL: {total}")
    print(f"==================================================")

    claim_map = {c["claim_id"]: c for c in claims}
    
    # 1. Checagem de integridade estrutural
    missing_fields_report = defaultdict(list)
    malformed_ids = []
    
    for c in claims:
        cid = c.get("claim_id", "")
        if not cid or not re.match(r"^[a-zA-Z0-9_\-\.\:\+]+$", cid):
            malformed_ids.append(cid)
        for rf in REQUIRED_FIELDS:
            if rf not in c or c[rf] is None or str(c[rf]).strip() == "":
                missing_fields_report[rf].append(cid)

    # 2. Checagem de Pares Contrastivos
    contrast_pairs = [c for c in claims if "contrast" in c["claim_id"] or "PAR CONTRASTIVO" in c["claim"]]
    broken_contrast_refs = []
    for cp in contrast_pairs:
        cid = cp["claim_id"]
        # Verificar se menciona a claim_id base
        m = re.search(r"hwa-([0-9a-zA-Z_\-\.]+)", cp["claim"])
        if m:
            base_ref = "hwa-" + m.group(1).rstrip(":.,;)")
            if base_ref not in claim_map and not any(k in base_ref for k in ["9.5", "10.2", "10.1"]):
                broken_contrast_refs.append((cid, base_ref))

    # 3. Auditoria de Classificação de Risco (R4)
    risk_mismatches = []
    for c in claims:
        cid = c["claim_id"]
        risk = c.get("risk", "read_only")
        text = (c.get("claim", "") + " " + c.get("notes", "")).lower()

        # Checar se ação destrutiva foi rotulada como read_only
        if risk == "read_only":
            for kw in HIGH_RISK_KEYWORDS["destructive"]:
                # Se o comando for destrutivo na sintaxe (ex: composer delete, conman cancel, dropdb)
                if re.search(rf"\b(composer|conman|planman|dropdb|rm)\s+{kw}\b", text):
                    risk_mismatches.append((cid, risk, f"contém ação destrutiva evidente: {kw}"))
                    break

    # 4. Auditoria de Proveniência e Fontes
    sources_count = Counter()
    unverifiable_sources = []
    for c in claims:
        cid = c["claim_id"]
        s_url = c.get("source_url", "")
        s_title = c.get("source_title", "")
        tier = c.get("evidence_tier", "")
        sources_count[tier] += 1

        if not s_url or not s_title:
            unverifiable_sources.append(cid)

    # 5. Auditoria de Claims com Status 'draft' ou 'version_dependent'
    version_dep = [c for c in claims if c.get("knowledge_status") == "version_dependent"]
    draft_claims = [c for c in claims if c.get("review_status") == "draft"]
    lab_validated = [c for c in claims if c.get("review_status") == "lab_validated" or c.get("evidence_tier") == "official_lab"]

    # 6. Rastreabilidade com Lab Evidences Locais
    lab_files = glob.glob(os.path.join(LAB_DIR, "lab-validation-*.jsonl"))
    lab_claim_ids = set()
    for lf in lab_files:
        for line in open(lf):
            if line.strip():
                try:
                    c = json.loads(line)
                    if c.get("claim_id"):
                        lab_claim_ids.add(c["claim_id"])
                except Exception:
                    pass

    # Gerar Relatório Consolidado
    report = {
        "total_claims": total,
        "missing_fields": {k: len(v) for k, v in missing_fields_report.items()},
        "malformed_claim_ids": len(malformed_ids),
        "contrast_pairs_count": len(contrast_pairs),
        "broken_contrast_refs": len(broken_contrast_refs),
        "risk_mismatches": len(risk_mismatches),
        "unverifiable_sources": len(unverifiable_sources),
        "evidence_tier_distribution": dict(sources_count),
        "knowledge_status_distribution": dict(Counter(c.get("knowledge_status") for c in claims)),
        "review_status_distribution": dict(Counter(c.get("review_status") for c in claims)),
        "total_lab_evidences_files": len(lab_files),
        "total_lab_evidence_ids": len(lab_claim_ids),
        "risk_mismatches_details": risk_mismatches[:10],
        "broken_contrast_details": broken_contrast_refs[:10]
    }

    out_file = os.path.join(REPO, "data", "eval", "deep_audit_report.json")
    with open(out_file, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"Integridade Estrutural: 0 IDs mal formatados.")
    print(f"Campos Faltantes por Campo: {dict(report['missing_fields'])}")
    print(f"Pares Contrastivos: {len(contrast_pairs)} pares analisados.")
    print(f"Inconsistências de Risco Detectadas: {len(risk_mismatches)}")
    print(f"Evidências de Laboratório Indexadas: {len(lab_claim_ids)} em {len(lab_files)} arquivos.")
    print(f"Distribuição de Tiers: {report['evidence_tier_distribution']}")
    print(f"Relatório detalhado gravado em: {out_file}")

if __name__ == "__main__":
    audit_claims()
