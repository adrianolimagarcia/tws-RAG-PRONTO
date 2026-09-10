import json, os

base_dir = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
gt_file = f"{base_dir}/data/export/tws_eval_ground_truth.jsonl"
clean_gt_file = f"{base_dir}/data/export/tws_eval_ground_truth_multilabel.jsonl"

q_map = {}
with open(gt_file, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip(): continue
        item = json.loads(line)
        q = item["question"].strip()
        tgt = item["target_claim_id"]
        cat = item.get("category", "Geral")
        if q not in q_map:
            q_map[q] = {
                "question": q,
                "relevant_claim_ids": [],
                "category": cat
            }
        if tgt not in q_map[q]["relevant_claim_ids"]:
            q_map[q]["relevant_claim_ids"].append(tgt)

with open(clean_gt_file, "w", encoding="utf-8") as f:
    for q_item in q_map.values():
        f.write(json.dumps(q_item, ensure_ascii=False) + "\n")

print(f"Exportado {len(q_map)} registros multi-label limpos em {clean_gt_file}")
