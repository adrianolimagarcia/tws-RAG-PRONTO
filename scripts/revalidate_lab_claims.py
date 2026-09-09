#!/usr/bin/env python3
"""revalidate_lab_claims.py — Promove e revalida claims canonicas com base nas evidencias
reais de laboratorio obtidas no cluster HWA 10.2.8 multi-container (MDM, BMDM, Dynamic Agent).
"""
import json, os

CLAIMS_FILE = "data/evidence/claims.jsonl"
claims = [json.loads(line) for line in open(CLAIMS_FILE)]

promotions = {
    "hwa-10.2.8-install-backup-mdm-existing-db-0004": {
        "evidence_tier": "official_lab",
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-bmdm-container-install-0001",
        "note": "Comprovado no lab container 10.2.8 (tws-bmdm): serverinst.sh configurou BKM contra banco compartilhado 172.18.0.10:5432/TWS (WAINST054I)."
    },
    "hwa-10.2.8-install-jnextplan-after-backup-0008": {
        "evidence_tier": "official_lab",
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-bmdm-fta-fullstatus-in-plan-0003",
        "note": "Comprovado no lab container 10.2.8: JnextPlan -for 0000 executado no MDM inseriu a workstation MDM_BK no plano Symphony (run #23)."
    },
    "hwa-install-1028-bkmdm-0001": {
        "evidence_tier": "official_lab",
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-bmdm-fta-fullstatus-in-plan-0003",
        "note": "Comprovado no lab container 10.2.8: MDM_BK definido como FTA full-status autolink no composer e no plano."
    },
    "hwa-install-bkmdm-1028-keys-0004": {
        "evidence_tier": "official_lab",
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-bmdm-aes-keys-copied-0002",
        "note": "Comprovado no lab container 10.2.8: copia de key.p12 e key.sth do MDM para o BMDM permitiu a leitura do Symphony de 52KB."
    },
    "hwa-10.2.8-ha-switchmgr-0001": {
        "evidence_tier": "official_lab",
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-bmdm-switchmgr-failover-e2e-0004",
        "note": "Comprovado no lab container 10.2.8: conman switchmgr MASTERDM;MDM_BK promoveu BMDM para *UNIX MASTER (AWSBHU120I) e reverteu com sucesso."
    },
    "hwa-10.2.8-install-twsinst-agent-0007": {
        "evidence_tier": "official_lab",
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-agent-docker-install-0001",
        "note": "Comprovado no lab container 10.2.8 (tws-agent): twsinst -new -agent dynamic com -tdwbhostname e -tdwbport 31116 instalou com sucesso (AWSFAB033I)."
    },
    "hwa-10.2.8-agent-auth-combinations-0002": {
        "evidence_tier": "official_lab",
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-twsinst-flags-mutual-exclusion-0001",
        "note": "Comprovado no lab container 10.2.8: exclusão mútua entre -sslkeysfolder e -wauser (AWSFAB486E) e omissão total (AWSFAB502E) validadas no binário."
    },
    "hwa-10.2.8-agent-dynamic-broker-0003": {
        "evidence_tier": "official_lab",
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-agent-docker-install-0001",
        "note": "Comprovado no lab container 10.2.8: agente dinâmico conectou na porta 31116 HTTPS do broker tws-hwa.lab com registro de recursos AWSITA083I."
    },
    "hwa-10.2.8-agent-ssl-folder-0001": {
        "evidence_tier": "official_lab",
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-agent-docker-install-0001",
        "note": "Comprovado no lab container 10.2.8: -sslkeysfolder com ca.crt, tls.key e tls.crt graváveis permitiu a geração de keystores no twsinst."
    },
    "hwa-10.2.8-dynagent-broker-0010": {
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-agent-docker-registered-plan-0002",
        "note": "Comprovado no lab container 10.2.8: broker MDM_DWB gerenciou o registro e despacho para os agentes MDMDA e TWS-AGENT."
    },
    "hwa-10.2.8-dynagent-broker-0011": {
        "review_status": "lab_validated",
        "corroborating_evidence": "hwa-lab-10.2.8-agent-docker-registered-plan-0002",
        "note": "Comprovado no lab container 10.2.8: broker instalado conjuntamente no container MDM sob a workstation MDM_DWB."
    }
}

updated = 0
for c in claims:
    cid = c.get("claim_id")
    if cid in promotions:
        p = promotions[cid]
        if "evidence_tier" in p:
            c["evidence_tier"] = p["evidence_tier"]
        if "review_status" in p:
            c["review_status"] = p["review_status"]
        
        # Adicionar nota de corroboracao com lab
        notes = c.get("notes", "")
        if p["note"] not in notes:
            c["notes"] = (notes + " [Validado em lab container 10.2.8: " + p["note"] + "]").strip()
        
        # Vincular corroborating_sources
        corrob = c.get("corroborating_sources", [])
        if isinstance(corrob, list) and p["corroborating_evidence"] not in corrob:
            corrob.append(p["corroborating_evidence"])
            c["corroborating_sources"] = corrob

        updated += 1

print(f"Total de claims revalidadas e promovidas: {updated}")
with open(CLAIMS_FILE, "w") as f:
    for c in claims:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")

print(f"Arquivo {CLAIMS_FILE} regravado com sucesso.")
