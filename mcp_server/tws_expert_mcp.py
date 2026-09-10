#!/usr/bin/env python3
"""
TWS/HWA 10.2.8 Expert MCP Server
Provides high-precision retrieval over 2,548 canonical verified claims,
API schemas, and operational lab procedures.
"""

import sys
import json
import re
import math
import os
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS_FILE = os.path.join(BASE_DIR, "data", "export", "tws_corpus_master_consolidated.jsonl")

# Index state
docs = []
doc_ids = []
doc_lens = []
postings = defaultdict(list)
categories = Counter = defaultdict(int)

if os.path.exists(CORPUS_FILE):
    with open(CORPUS_FILE, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if not line.strip(): continue
            item = json.loads(line)
            docs.append(item)
            doc_ids.append(item["claim_id"])
            categories[item.get("category", "Geral")] += 1
            
            text = f"{item['claim']} {item.get('context_prefix', '')} {' '.join(item.get('synthetic_questions', []))}"
            tokens = re.findall(r"\w+", text.lower())
            doc_lens.append(len(tokens))
            
            tf_map = defaultdict(int)
            for t in tokens:
                tf_map[t] += 1
            for t, count in tf_map.items():
                postings[t].append((idx, count))

N = len(doc_ids)
avgdl = sum(doc_lens) / N if N > 0 else 0.0
k1 = 1.5
b = 0.75

idf = {}
for term, p_list in postings.items():
    df = len(p_list)
    idf[term] = math.log((N - df + 0.5) / (df + 0.5) + 1.0)


def search_bm25(query_tokens, category=None, top_k=5):
    doc_scores = defaultdict(float)
    q_terms = [t for t in query_tokens if t in postings]
    if not q_terms:
        return []
    for q in q_terms:
        q_idf = idf[q]
        for doc_idx, tf in postings[q]:
            if category and docs[doc_idx].get("category") != category:
                continue
            dl = doc_lens[doc_idx]
            num = tf * (k1 + 1.0)
            den = tf + k1 * (1.0 - b + b * (dl / avgdl))
            doc_scores[doc_idx] += q_idf * (num / den)
            
    top_indices = sorted(doc_scores.keys(), key=lambda i: doc_scores[i], reverse=True)[:top_k]
    return [
        {
            "claim_id": docs[i]["claim_id"],
            "score": round(doc_scores[i], 3),
            "category": docs[i].get("category"),
            "claim": docs[i]["claim"],
            "context_prefix": docs[i].get("context_prefix"),
            "platform": docs[i].get("platform")
        }
        for i in top_indices
    ]


def handle_tool_call(name, args):
    if name == "tws_expert_search":
        q = args.get("query", "")
        cat = args.get("category")
        top_k = int(args.get("top_k", 5))
        tokens = re.findall(r"\w+", q.lower())
        results = search_bm25(tokens, category=cat, top_k=top_k)
        return {"results": results, "count": len(results)}

    elif name == "tws_get_claim":
        cid = args.get("claim_id", "").strip()
        for d in docs:
            if d["claim_id"] == cid:
                return {"found": True, "claim": d}
        return {"found": False, "error": f"Claim ID '{cid}' não encontrada."}

    elif name == "tws_list_categories":
        return {"total_claims": N, "categories": dict(categories)}

    raise ValueError(f"Unknown tool: {name}")


def main():
    # Minimal stdio JSON-RPC loop for MCP
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        req_id = req.get("id")
        method = req.get("method")

        if method == "tools/list":
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": [
                        {
                            "name": "tws_expert_search",
                            "description": "Busca contextual em alta precisão (BM25) no corpus de 2.548 claims canônicas do HWA 10.2.8.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "query": {"type": "string", "description": "Termo de busca, comando ou código de erro (ex: AWSITA081E, switchmgr, planman)"},
                                    "category": {"type": "string", "description": "Opcional: filtrar por categoria taxonômica"},
                                    "top_k": {"type": "integer", "description": "Número de resultados (padrão: 5)"}
                                },
                                "required": ["query"]
                            }
                        },
                        {
                            "name": "tws_get_claim",
                            "description": "Recupera o registro completo de uma evidência/claim pelo claim_id exato.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "claim_id": {"type": "string", "description": "Identificador da claim (ex: hwa-lab-10.2.8-switchmgr-failover-switchback-0001)"}
                                },
                                "required": ["claim_id"]
                            }
                        },
                        {
                            "name": "tws_list_categories",
                            "description": "Lista todas as categorias taxonômicas disponíveis e contagem de claims indexadas.",
                            "inputSchema": {"type": "object", "properties": {}}
                        }
                    ]
                }
            }
        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})
            try:
                out = handle_tool_call(name, args)
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(out, ensure_ascii=False, indent=2)}]
                    }
                }
            except Exception as e:
                resp = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32000, "message": str(e)}}
        elif method == "initialize":
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "tws-hwa-expert-mcp", "version": "1.0.0"}
                }
            }
        else:
            resp = {"jsonrpc": "2.0", "id": req_id, "result": {}}

        sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
