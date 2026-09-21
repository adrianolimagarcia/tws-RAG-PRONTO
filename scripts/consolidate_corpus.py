import os, glob, json, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify_taxonomy import classify as classify_claim  # noqa: E402

# Caminho do proprio arquivo, nao hardcoded: o repositorio pode estar em qualquer
# lugar (o usuario o mantem em /run/media/adriano/..., que nao existe em outra maquina).
# `scripts/` fica na raiz, entao subir um nivel chega na raiz.
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

# 1b. Fonte REST API V2 — superficie funcional (data/knowledge/rest-api-derived.jsonl).
# POR QUE ENTRA AQUI: o switch RAG_INGEST_REST_API so' existe no carregador do LABORATORIO
# (rag_core/corpus.py). A fonte entrou na medicao em 2026-09-18 e NUNCA neste artefato, que
# e' o que a PRODUCAO consome - resultado medido: os alvos de 40 perguntas `rest-*` e 40
# `ops-*` nao existiam no indice de producao e pontuavam 0 por construcao.
# `synthetic_questions` fica vazio, mas NAO por supressao: a propria fonte REST nao traz
# esse campo (verificado - 0 dos 300 docs). Deixar assim e' o correto; se a fonte ganhar
# perguntas sinteticas, elas entram como expansao de vocabulario. ATENCAO: um registro de
# 2026-09-19 mediu que SUPRIMIR esse campo custa recall real (2,67pt de @1 em dado limpo) e
# esta' REJEITADO como correcao - o vies se corrige no BENCHMARK, nunca tirando dado do indice.
# O risco aqui e' o oposto do que parece: uma pergunta de benchmark que coincida com uma
# synthetic_question indexada seria gabarito no corpus, entao a varredura de vazamento e'
# obrigatoria a cada mudanca de fonte.
#
# As DUAS granularidades entram (familia + operacao), com ids DISJUNTOS - verificado: 24
# ids de familia e 276 de operacao, intersecao vazia. O laboratorio nao pode carregar as
# duas ao mesmo tempo (RAG_REST_GRANULARITY troca uma pela outra), entao a familia sozinha
# deixa as 40 perguntas `ops-*` sem alvo. A producao nao tem essa restricao: um documento de
# operacao serve quem pergunta o detalhe, o de familia serve quem pergunta o geral.
rest_files = [
    os.path.join(base_dir, "data", "knowledge", "rest-api-derived.jsonl"),
    os.path.join(base_dir, "data", "knowledge", "rest-api-derived-ops.jsonl"),
]
n_rest = 0
for rest_file in rest_files:
    if not os.path.exists(rest_file) or os.environ.get("SKIP_REST_API") == "1":
        continue
    with open(rest_file, "r", encoding="utf-8") as f:
        for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    c = json.loads(line)
                except Exception:
                    continue
                cid = c.get("claim_id")
                if not cid or cid in claims_by_id:
                    continue
                # Mesmo texto que o laboratorio indexa (rag_core/corpus.py): claim, syntax,
                # resource, supporting_quote, source_title e vocab_spec (o vocabulario extraido
                # da spec OpenAPI). `claim` recebe tudo porque e' o campo que o MCP indexa.
                texto = " ".join(str(c.get(k, "")) for k in
                                 ("claim", "syntax", "resource", "supporting_quote",
                                  "source_title", "vocab_spec"))
                prefix = c.get("source_title") or ""
                categoria = classify_claim(prefix, texto)
                taxonomy_counter[categoria] += 1
                claims_by_id[cid] = {
                    "claim_id": cid,
                    "claim": texto,
                    "context_prefix": prefix,
                    "category": categoria,
                    "result": c.get("result", "SUCCESS"),
                    "platform": "HWA 10.2.8 Distributed",
                    "source_file": os.path.basename(rest_file),
                    "synthetic_questions": [],
                }
                n_rest += 1

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
print(f"- Documentos REST API V2 acrescentados: {n_rest}")
print(f"- Distribuicao por categoria:")
for cat, count in taxonomy_counter.most_common():
    print(f"  {count:4d}x {cat}")
print(f"\nArtefatos gerados em {export_dir}")
