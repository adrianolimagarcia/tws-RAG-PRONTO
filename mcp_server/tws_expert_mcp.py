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
    # `margin` = score do 1o menos o do 2o. E' o melhor preditor de "o top-1 e' a claim
    # certa" que foi MEDIDO neste scorer: AUC 0,850 contra 0,669 do score absoluto
    # (medido em 423 perguntas; ver scripts/calibrate_abstention.py). Intuicao: score alto
    # pode ser so' coincidencia de termos raros; score alto E destacado dos concorrentes
    # e' evidencia de que existe uma claim que responde.
    ordenados = [doc_scores[i] for i in top_indices]
    margem = (ordenados[0] - ordenados[1]) if len(ordenados) > 1 else ordenados[0] if ordenados else 0.0
    return [
        {
            "claim_id": docs[i]["claim_id"],
            "score": round(doc_scores[i], 3),
            "margin": round(margem, 3) if j == 0 else None,
            "category": docs[i].get("category"),
            "claim": docs[i]["claim"],
            "context_prefix": docs[i].get("context_prefix"),
            "platform": docs[i].get("platform")
        }
        for j, i in enumerate(top_indices)
    ]


# ---------------------------------------------------------------------------
# ABSTENCAO — "responder certo ou admitir que nao sabe"
# ---------------------------------------------------------------------------
# Sem isto, a busca SEMPRE devolvia top_k documentos com um score, e nao havia nenhum
# caminho para o consumidor distinguir "achei a evidencia" de "preenchi 5 vagas". O LLM
# recebia 5 resultados sempre e escrevia em cima do errado - esse era o mecanismo da
# alucinacao.
#
# DOIS SINAIS, porque um so' nao cobre os DOIS formatos de consulta que a producao recebe:
#
# 1) MARGEM NORMALIZADA = 1 - top2/top1, em [0,1).  Medido em 423 perguntas naturais:
#      score absoluto   AUC 0,669   (quase inutil)
#      margem absoluta  AUC 0,850   mas correlaciona 0,706 com o TAMANHO da consulta
#      margem normal.   AUC 0,842   correlacao so' 0,171  <- adotada
#    A margem ABSOLUTA foi rejeitada por um defeito medido: uma consulta valida de
#    producao ("AWSITA081E") abstinha, porque consulta curta acumula pouca massa de
#    BM25. O limiar tem de ser livre de escala.
#    Com margem_norm >= 0,177: precisao 47,8% -> 84,0%, evitando 88% dos erros,
#    cobrindo 67,3% dos acertos.
#
# 2) ESCAPE DE BUSCA CURTA (so' para consulta <= 5 tokens):
#    se a consulta e' CURTA e casou no indice, ela e' um LOOKUP, nao uma pergunta. O
#    documento devolvido contem o termo -> a resposta fica ancorada nele, e nao ha' como
#    alucinar sobre um termo que o indice confirma existir. Nao abstem.
#    Motivo: "AWSITA081E" (1 token) aparece em 3 docs com scores quase iguais, entao a
#    margem e' ~0,06 - mas aqui empate NAO e' ambiguidade, e' prova de que existe. O mesmo
#    vale para jargao de produto (planman, switchmgr, conman), que tem idf 2,2-5,1.
#
#    O corte de idf foi calibrado nos DOIS sentidos (21 consultas curtas REAIS do dominio
#    x 16 FORA do dominio):
#      corte idf  falso-abster  abstem-certo
#        6,0        18/21          9/16     <- rejeitado: inutilizavel
#        2,0         2/21          7/16
#        1,0         1/21          7/16     <- adotado
#    O corte 6,0 (so' identificador de mensagem) foi REJEITADO por medicao: destruia
#    consultas legitimas de jargao. Em pergunta natural o escape NUNCA dispara (0/423),
#    inclusive no corte 2,0 - verificado. Ou seja: cobre o formato curto sem afetar o
#    comportamento medido no benchmark.
#
# LIGADO POR DEFAULT. `RAG_ABSTAIN_MARGIN=0` desliga; `data/eval/abstention.json`
# (gravado por `calibrate_abstention.py --mcp --aplicar`) sobrescreve os parametros.
MARGEM_NORM_DEFAULT = 0.177
IDF_RARO_DEFAULT = 1.0
TOKENS_CURTOS_DEFAULT = 5


def _params_abstencao():
    p = {"margem_norm": MARGEM_NORM_DEFAULT, "idf_raros": IDF_RARO_DEFAULT,
         "tokens_curtos": TOKENS_CURTOS_DEFAULT}
    arq = os.path.join(BASE_DIR, "data", "eval", "abstention.json")
    if os.path.exists(arq):
        try:
            with open(arq, encoding="utf-8") as f:
                p.update(json.load(f))
        except Exception:
            pass
    env = os.environ.get("RAG_ABSTAIN_MARGIN")
    if env is not None:
        try:
            p["margem_norm"] = float(env)
        except ValueError:
            pass
    return p


MSG_ABSTER = (
    "Nao ha' base verificada no material para esta consulta. Responda exatamente que "
    "nao encontrou base verificada e sugira refrasear (codigo de erro, comando ou "
    "componente). NAO responda com conhecimento proprio nem use os candidatos abaixo "
    "como se fossem evidencia."
)


def handle_tool_call(name, args):
    if name == "tws_expert_search":
        q = args.get("query", "")
        cat = args.get("category")
        top_k = int(args.get("top_k", 5))
        tokens = re.findall(r"\w+", q.lower())
        results = search_bm25(tokens, category=cat, top_k=top_k)
        out = {"results": results, "count": len(results)}

        p = _params_abstencao()
        if p["margem_norm"] > 0:
            s1 = results[0]["score"] if results else 0.0
            s2 = results[1]["score"] if len(results) > 1 else 0.0
            margem_norm = ((s1 - s2) / s1) if s1 > 0 else 0.0
            # idf do termo mais raro da consulta que casou no indice
            casados = [idf[t] for t in set(tokens) if t in postings]
            max_idf = max(casados) if casados else 0.0
            escape = (len(tokens) <= p["tokens_curtos"]) and (max_idf >= p["idf_raros"])

            out["margin"] = round(margem_norm, 4)
            out["abstain_margin"] = p["margem_norm"]
            out["matched_rare_idf"] = round(max_idf, 2)
            if margem_norm < p["margem_norm"] and not escape:
                out["abstained"] = True
                out["results"] = []
                out["count"] = 0
                out["message"] = MSG_ABSTER
            else:
                out["abstained"] = False
        return out

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
                            "description": (
                                "Busca contextual em alta precisão (BM25) no corpus de claims canônicas do HWA 10.2.8. "
                                "A resposta pode conter `abstained: true`: isso significa que NÃO há base verificada no "
                                "material para a consulta. Nesse caso responda que não há base verificada e sugira "
                                "refrasear (código de erro, comando ou componente) — NÃO responda com conhecimento "
                                "próprio e NÃO trate os candidatos como evidência. O campo `margin` mede a confiança: "
                                "quanto maior, mais destacada é a claim que responde."
                            ),
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
