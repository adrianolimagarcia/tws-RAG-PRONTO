import os, glob, json, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify_taxonomy import classify as classify_claim  # noqa: E402

base_dir = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
evidence_dir = os.path.join(base_dir, "data", "evidence")
export_dir = os.path.join(base_dir, "data", "export")
os.makedirs(export_dir, exist_ok=True)

master_file = os.path.join(export_dir, "tws_corpus_master_consolidated.jsonl")
eval_gt_file = os.path.join(export_dir, "tws_eval_ground_truth.jsonl")
taxonomy_report_file = os.path.join(export_dir, "tws_taxonomy_audit_report.json")

claims_by_id = {}
all_questions = []
taxonomy_counter = Counter()

evidence_files = sorted(glob.glob(os.path.join(evidence_dir, "*.jsonl")))
print(f"Lendo {len(evidence_files)} arquivos de evidencia em {evidence_dir}...")

for fpath in evidence_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except Exception as e:
                print(f"Erro no parsing JSON {fname}:{line_num}: {e}")
                continue
            # Higienizar bytes nulos (binarios do HWA embutem \x00 em claims)
            if isinstance(item, str):
                pass
            else:
                for k, v in item.items():
                    if isinstance(v, str) and "\x00" in v:
                        item[k] = v.replace("\x00", "")
            
            cid = item.get("claim_id") or item.get("id")
            if not cid:
                continue
            
            # Normalizar objeto
            claim_text = item.get("claim") or item.get("content") or item.get("title") or ""
            prefix = item.get("context_prefix") or ""
            questions = item.get("synthetic_questions") or item.get("questions") or []
            
            # Taxonomia (classificador externo, regras ordenadas — ver classify_taxonomy.py)
            category = classify_claim(prefix, claim_text)
            
            taxonomy_counter[category] += 1
            
            record = {
                "claim_id": cid,
                "claim": claim_text,
                "context_prefix": prefix,
                "category": category,
                "result": item.get("result", "SUCCESS"),
                "platform": item.get("platform", "HWA 10.2.8 Distributed"),
                "source_file": fname,
                "synthetic_questions": questions
            }
            claims_by_id[cid] = record
            
            for q in questions:
                all_questions.append({
                    "question": q,
                    "target_claim_id": cid,
                    "category": category
                })

# Gravar Master Consolidated
with open(master_file, "w", encoding="utf-8") as f:
    for cid in sorted(claims_by_id.keys()):
        f.write(json.dumps(claims_by_id[cid], ensure_ascii=False) + "\n")

# Gravar Eval Ground Truth
with open(eval_gt_file, "w", encoding="utf-8") as f:
    for q_item in all_questions:
        f.write(json.dumps(q_item, ensure_ascii=False) + "\n")

# Relatorio Taxonomico
# BUGFIX: taxonomy_counter era incrementado por LINHA LIDA, contando claim_ids duplicados
# entre arquivos de evidencia e divergindo do master (que deduplica). Recontar a partir do
# conjunto deduplicado garante que a distribuicao reflita exatamente o corpus publicado.
taxonomy_counter = Counter(rec["category"] for rec in claims_by_id.values())

taxonomy_report = {
    "total_unique_claims": len(claims_by_id),
    "total_synthetic_questions": len(all_questions),
    "total_evidence_files": len(evidence_files),
    "distribution_by_category": dict(taxonomy_counter),
    "export_artifacts": {
        "master_corpus": master_file,
        "eval_ground_truth": eval_gt_file
    }
}

with open(taxonomy_report_file, "w", encoding="utf-8") as f:
    json.dump(taxonomy_report, f, indent=2, ensure_ascii=False)

print(f"\nConsolidacao concluida com sucesso:")
print(f"- Total de claims unicas: {len(claims_by_id)}")
print(f"- Total de perguntas sinteticas indexadas: {len(all_questions)}")
print(f"- Distribuicao por categoria:")
for cat, count in taxonomy_counter.most_common():
    print(f"  {count:4d}x {cat}")
print(f"\nArtefatos gerados em {export_dir}")
