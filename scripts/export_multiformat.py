#!/usr/bin/env python3
"""Exportador Universal de Corpus TWS/HWA 10.2.8.

Gera 4 formatos prontos para uso:
1. RAG Chunks Markdown/Documentos (.md): Ideal para upload no Custom GPT (OpenAI), Claude Projects, NotebookLM, Perplexity Spaces.
2. LlamaIndex / LangChain Document format (.jsonl): Formato canônico de ingestão (page_content + metadata).
3. Fine-Tuning / Few-shot Chat format (.jsonl): Estilo OpenAI/Anthropic messages (system + user query + assistant response).
4. FAQ / Knowledge Base CSV (.csv): Para importar em ServiceNow, Jira Service Desk, Zendesk ou planilhas.
"""
import argparse
import csv
import json
import os

CORPUS_DEFAULT = "data/export/tws_corpus_enriched_safe.jsonl"
OUT_DIR = "data/export/dist"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", default=CORPUS_DEFAULT)
    parser.add_argument("--out-dir", default=OUT_DIR)
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    items = []
    with open(args.corpus, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                items.append(json.loads(line))

    print(f"Total de registros a exportar: {len(items)}")

    # 1. RAG Markdown unificado em volumes temáticos (Ideal para ChatGPT / Perplexity / NotebookLM / Claude)
    # Dividir em arquivos de ~500-1000 claims para respeitar limites de upload por arquivo (ex: 10-20MB)
    chunk_size = 1500
    for i in range(0, len(items), chunk_size):
        part = (i // chunk_size) + 1
        md_path = os.path.join(args.out_dir, f"tws_hwa_knowledge_base_part_{part}.md")
        with open(md_path, "w", encoding="utf-8") as f_md:
            f_md.write(f"# Base de Conhecimento HCL Workload Automation (TWS/HWA 10.2.8) - Parte {part}\n\n")
            for item in items[i:i + chunk_size]:
                cid = item.get("claim_id")
                claim = item.get("claim", "").strip()
                cat = item.get("category", "Geral")
                prefix = item.get("context_prefix", "").strip()
                sq = item.get("synthetic_questions", [])

                f_md.write(f"## [{cid}] {cat}\n")
                if prefix:
                    f_md.write(f"**Contexto:** {prefix}\n\n")
                f_md.write(f"**Instrução Técnica / Resolução:**\n{claim}\n\n")
                if sq:
                    f_md.write("**Perguntas Frequentes / Casos de Uso:**\n")
                    for q in sq:
                        f_md.write(f"- {q}\n")
                    f_md.write("\n")
                f_md.write("---\n\n")
        print(f"-> Gerado Markdown: {md_path}")

    # 2. Formato Canônico RAG (LangChain / LlamaIndex Documents)
    rag_doc_path = os.path.join(args.out_dir, "tws_rag_documents_langchain.jsonl")
    with open(rag_doc_path, "w", encoding="utf-8") as f_rag:
        for item in items:
            cid = item.get("claim_id")
            claim = item.get("claim", "").strip()
            prefix = item.get("context_prefix", "").strip()
            sq = item.get("synthetic_questions", [])
            cat = item.get("category", "")
            
            # Conteúdo para busca e recuperação semântica
            content_lines = []
            if prefix:
                content_lines.append(f"Contexto: {prefix}")
            content_lines.append(f"Conteúdo: {claim}")
            if sq:
                content_lines.append("Perguntas Relacionadas: " + " | ".join(sq))
            
            doc = {
                "id": cid,
                "text": "\n".join(content_lines),
                "metadata": {
                    "claim_id": cid,
                    "category": cat,
                    "platform": item.get("platform", "Distributed"),
                    "source_file": item.get("source_file", ""),
                    "num_synthetic_questions": len(sq)
                }
            }
            f_rag.write(json.dumps(doc, ensure_ascii=False) + "\n")
    print(f"-> Gerado Formato LangChain/LlamaIndex: {rag_doc_path}")

    # 3. Formato Fine-Tuning / Conversacional (OpenAI / Anthropic format)
    ft_path = os.path.join(args.out_dir, "tws_conversational_dataset_openai.jsonl")
    with open(ft_path, "w", encoding="utf-8") as f_ft:
        for item in items:
            claim = item.get("claim", "").strip()
            sq = item.get("synthetic_questions", [])
            for q in sq:
                conv = {
                    "messages": [
                        {
                            "role": "system",
                            "content": "Você é o especialista sênior em HCL Workload Automation (TWS/HWA 10.2.8). Responda com base na documentação oficial com precisão técnica e sem alucinar."
                        },
                        {"role": "user", "content": q},
                        {"role": "assistant", "content": claim}
                    ]
                }
                f_ft.write(json.dumps(conv, ensure_ascii=False) + "\n")
    print(f"-> Gerado Formato Conversacional/Fine-tuning: {ft_path}")

    # 4. Formato Tabela / FAQ CSV
    csv_path = os.path.join(args.out_dir, "tws_knowledge_base_faq.csv")
    with open(csv_path, "w", encoding="utf-8", newline="") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["ID", "Categoria", "Pergunta Principal", "Outras Perguntas", "Instrucao / Resposta", "Contexto"])
        for item in items:
            cid = item.get("claim_id")
            cat = item.get("category", "")
            claim = item.get("claim", "").strip()
            prefix = item.get("context_prefix", "").strip()
            sq = item.get("synthetic_questions", [])
            p_principal = sq[0] if sq else ""
            outras_p = " | ".join(sq[1:]) if len(sq) > 1 else ""
            writer.writerow([cid, cat, p_principal, outras_p, claim, prefix])
    print(f"-> Gerado Formato FAQ CSV: {csv_path}")

    print(f"\nTodos os formatos foram gerados com sucesso na pasta: {args.out_dir}/")

if __name__ == "__main__":
    main()
