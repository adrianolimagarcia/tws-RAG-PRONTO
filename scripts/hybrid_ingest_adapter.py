"""
Adaptador de Ingestão para RAG Híbrido SOTA (HWA 10.2.8).
Gera payloads prontos para bancos vetoriais (Qdrant, pgvector, Milvus)
combinando busca vetorial densa + busca esparsa BM25 + filtragem por metadados.
"""
import json, os

def load_canonical_documents(canonical_jsonl_path):
    with open(canonical_jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            record = json.loads(line)
            
            # 1. Payload de busca híbrida (BM25 + Dense)
            # Concatena: Afirmação + Retrieval Text + Perguntas Sintéticas
            bm25_text = f"{record['claim']}\nKeywords: {record.get('retrieval_text', '')}\n"
            if record.get("synthetic_questions"):
                bm25_text += "Perguntas: " + " | ".join(record["synthetic_questions"])
            
            # 2. Metadados rígidos para pre-filtering
            metadata = {
                "id": record["claim_id"],
                "version": record.get("version", "10.2.8"),
                "platform": record.get("platform", "distributed"),
                "category": record.get("category", "Geral"),
                "evidence_level": record.get("evidence_level", "official_corroborated"),
                "knowledge_status": record.get("knowledge_status", "current"),
                "confidence": record.get("confidence", "high"),
                "source_file": record.get("source_file", "")
            }
            
            yield {
                "id": record["claim_id"],
                "text_for_embedding": record["claim"],
                "text_for_bm25": bm25_text,
                "metadata": metadata
            }

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    jsonl_path = os.path.join(base, "data", "export", "tws_canonical_knowledge_v3.jsonl")
    count = sum(1 for _ in load_canonical_documents(jsonl_path))
    print(f"Adaptador pronto: {count} documentos canônicos formatados para Ingestão Híbrida.")
