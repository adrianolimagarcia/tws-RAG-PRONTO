#!/usr/bin/env python3
"""reconcile_claims_review_status.py — Sincroniza e normaliza review_status e integridade de claims.
"""
import json, sys

CLAIMS_FILE = "data/evidence/claims.jsonl"
claims = [json.loads(line) for line in open(CLAIMS_FILE)]

updated = 0
for c in claims:
    r_stat = c.get("review_status")
    stat = c.get("status")
    tier = c.get("evidence_tier")

    # 1. Normalizar review_status nulos
    if r_stat is None:
        if stat == "verified" and tier == "official_lab":
            c["review_status"] = "lab_validated"
            updated += 1
        elif stat == "verified" and tier in ["official_primary", "official_corroborated"]:
            c["review_status"] = "verified"
            updated += 1
        elif stat == "community_practice":
            c["review_status"] = "community_reviewed"
            updated += 1
        elif stat in ["version_dependent", "obsolete", "insufficient_evidence"]:
            c["review_status"] = "reviewed"
            updated += 1

    # 2. Promover drafts comprovados no lab
    if c["claim_id"] in [
        "hwa-10.1-real-sfinal-0017",
        "hwa-10.2.8-cliauth-conman-composer-auth-0001",
        "hwa-10.2.8-install-serverinst-install-0003",
        "hwa-10.2.8-restore-backup-mdm-0001",
        "hwa-10.2.8-useropts-useropts-connection-0001",
        "hwa-jnextplan-syntax-gap-0048"
    ]:
        c["review_status"] = "lab_validated"
        c["evidence_tier"] = "official_lab"
        updated += 1

with open(CLAIMS_FILE, "w") as f:
    for c in claims:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")

print(f"Total de claims reconciliadas: {updated}")
