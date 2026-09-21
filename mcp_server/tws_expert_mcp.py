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

# Ramo denso (BGE-M3). Import TOLERANTE: o MCP nao pode deixar de subir porque o denso
# faltou. Ver o cabecalho de mcp_server/tws_dense.py para a medicao que motivou isto.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import tws_dense
except Exception:
    tws_dense = None

# MODO DENSO. OPT-IN, DEFAULT OFF - sem RAG_DENSE_MODE=fuse, nada muda.
#
# ATENCAO: `fuse` parece ganhar no pool de 423 e NAO GANHA no sistema real. Medido:
#   pool 423: off @1 209 @5 265 MRR 0,5588 -> fuse @1 222 @5 306 MRR 0,6182 (@5 p<0,0001)
#   mas nos 10 conjuntos independentes do repo (n=450): @1 309 -> 289, -20,
#   McNemar p=0,0308 CONTRA a fusao; mensagens 50->31 @1 e holdout_100 79->69 @1.
# O pool engana por COMPOSICAO: e' 54% blind_v3 (onde a fusao nao muda nada) mais uma
# fatia sintetica rest/ops onde ela ganha. E' exatamente o "pior criterio e' a media" que
# o gate de promocao v4 do repo existe para barrar. Ver o registro de evidencia
# data/evidence/lab-validation-2026-09-19-fusao-densa-na-producao-falsificada-por-conjunto.jsonl
# e o veredito anterior de 2026-09-20 (dense-fusion-pooled-verdict).
#
# ONDE a fusao ajuda de forma consistente (2 medicoes independentes): benchmark virgem de
# MENSAGEM EM INGLES (@1 +3, @5 +4) e virgem_expandido (@1 +6). E' o caso em que a pergunta
# descreve um sintoma sem citar codigo nem texto - o lexical tem pouco a casar.
# Custo em CPU: ~215ms a mais por consulta. Sem o indice denso instalado, cai em off sozinho.
DENSE_MODE = (os.environ.get("RAG_DENSE_MODE") or "off").strip().lower()
if DENSE_MODE not in ("off", "fuse"):
    raise SystemExit("RAG_DENSE_MODE=%r nao reconhecido. Use 'off' ou 'fuse'." % DENSE_MODE)
# Profundidade de candidatos de cada ramo na fusao. 30 e' o valor do laboratorio
# (data/eval/evaluate_rag_benchmark.py: k_dense=30, k_sparse=30) - replicar aqui e' o que
# torna a medicao da producao comparavel com a que ja' existe.
RRF_K = int(os.environ.get("RAG_DENSE_RRF_K", "30"))
RAG_RRF_W = float(os.environ.get("RAG_RRF_W", "0.5"))
if not (0.0 <= RAG_RRF_W <= 1.0):
    raise SystemExit("RAG_RRF_W=%s fora de [0,1]." % RAG_RRF_W)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# CORPUS_FILE aceita override por ambiente SO' para MEDICAO (comparar variantes de corpus
# no caminho real de producao). Default inalterado: sem a variavel, o arquivo de sempre.
# Existe porque, ate' agora, nao havia COMO medir a producao contra um corpus candidato -
# e foi assim que a fonte REST ficou de fora sem ninguem perceber (ver
# data/eval/augmenta_corpus_rest.py).
CORPUS_FILE = (os.environ.get("TWS_CORPUS_FILE")
               or os.path.join(BASE_DIR, "data", "export", "tws_corpus_master_consolidated.jsonl"))

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
# CONFIANCA — NUNCA descarta a resposta; informa a confiabilidade dela
# ---------------------------------------------------------------------------
# HISTORICO (o que foi tentado e por que NAO ficou assim):
# A versao anterior ABSTINHA em silencio quando a margem ficava abaixo do limiar:
# zerava `results` e mandava o LLM dizer que nao havia base. Isso foi MEDIDO e
# rejeitado pelo dono, com razao:
#   - no limiar 0,177 descartava 66 respostas CORRETAS para chegar a 84% de precisao;
#   - 0 de 423 perguntas tem zero resultados de BM25, ou seja, o "nao ha base" quase
#     nunca era literalmente verdadeiro - era um chute do classificador;
#   - falar "nao sei" sabendo e' REGRESSAO.
# Agora o sistema SEMPRE devolve os resultados e anexa a confianca medida. Quem decide
# (o LLM, com o material na mao) recebe a informacao em vez de um portao fechado.
#
# SINAL: margem normalizada = 1 - top2/top1. Medida em 423 perguntas:
#   AUC 0,842 (producao) / 0,818 (rag_core), contra 0,669 do score absoluto.
#   A margem ABSOLUTA foi testada e rejeitada: correlaciona 0,706 com o TAMANHO da
#   consulta, e fazia consulta real de producao ("AWSITA081E") cair de faixa.
#
# FAIXAS MEDIDAS (n=423; base = 47,8% de top-1 correto):
#   alta  (>= 0,177): 162 perguntas (38,3%) -> 84,0% de acerto  (+36,2 pp)
#   media (>= 0,050): 139 perguntas (32,9%) -> 29,5% de acerto  (-18,3 pp)
#   baixa (<  0,050): 122 perguntas (28,8%) -> 20,5% de acerto  (-27,3 pp)
# ESTAVEIS out-of-sample (metades independentes):
#   alta: 85,0% (n=80) x 82,9% (n=82) | media: 27,0% x 31,6% | baixa: 21,3% x 19,7%
#
# O ERRO SE CONCENTRA nao-alta: 195 de 221 erros (88,2%) caem em media+baixa, que sao
# 61,7% dos casos. E' onde o aviso ao LLM vale.
FAIXA_ALTA = 0.177
FAIXA_MEDIA = 0.05

# Marcadores de versao != 10.2.8 (o corpus mistura 9.x e 10.2.0-10.2.7).
RE_VERSAO_DIFERENTE = re.compile(r"\b9\.\d|\b10\.2\.[0-7]\b")

# Ponte EN->PT da consulta. Import tolerante: se o modulo faltar, a busca segue sem a
# ponte (o servidor nao pode deixar de subir por causa de um acrescimo opcional).
try:
    from tws_traduz import traduz_para_pt as _traduz
except Exception:  # pragma: no cover - caminho de degradacao
    def _traduz(_consulta):
        return None


def _params_confianca():
    p = {"faixa_alta": FAIXA_ALTA, "faixa_media": FAIXA_MEDIA}
    arq = os.path.join(BASE_DIR, "data", "eval", "abstention.json")
    if os.path.exists(arq):
        try:
            with open(arq, encoding="utf-8") as f:
                d = json.load(f)
            p["faixa_alta"] = float(d.get("faixa_alta", d.get("margem_norm", p["faixa_alta"])))
            p["faixa_media"] = float(d.get("faixa_media", p["faixa_media"]))
        except Exception:
            pass
    return p


MSG_CONFIANCA = {
    "alta": ("Evidencia com boa correspondencia. Responda normalmente, citando o "
             "claim_id como fonte."),
    "media": ("Correspondencia PARCIAL: o melhor candidato nao se destaca dos demais. "
              "Confirme com um termo mais especifico (codigo de erro, comando ou "
              "componente) antes de afirmar. Se o material nao cobrir a pergunta, diga "
              "que nao encontrou base verificada."),
    "baixa": ("Correspondencia FRACA: nenhum candidato corresponde bem. NAO afirme nada "
              "com base nestes resultados - trate-os como pistas, reformule a consulta "
              "ou diga que nao encontrou base verificada."),
}


def _funde_rrf(q_texto, esparsos, top_k):
    """RRF k=60 denso+esparso com o MESMO peso do laboratorio (w=2*RAG_RRF_W no denso,
    2-w no esparso). Reproduzir a escala importa: o segundo estagio soma bonus FIXOS ao
    score recebido, entao mudar a escala muda o balanco mesmo com a mesma ordem."""
    if tws_dense is None or not tws_dense.disponivel():
        return esparsos
    densos = [c for c, _ in tws_dense.busca(q_texto, top_k=RRF_K)]
    # Os DOIS ramos entram com a MESMA profundidade RRF_K (30), como no laboratorio. Isto
    # NAO e' um detalhe de desempenho: medido no pool 423, com o ramo esparso indo ate' o
    # fim (10.000 candidatos) o @5 CAI de 306 para 274, porque a cauda longa do BM25 soma
    # valores pequenos a milhares de docs e reordena o topo - o ganho dos dois ramos de
    # profundidade igual se perde. A contrapartida e' mais alvo "ausente" (a faixa 31+ sai
    # do conjunto fundido), e isso e' aceito: o que se mostra ao usuario e' o topo.
    esparsos_ids = [r["claim_id"] for r in esparsos[:RRF_K]]
    w = 2.0 * RAG_RRF_W
    rrf = {}
    for r, cid in enumerate(densos, 1):
        rrf[cid] = rrf.get(cid, 0.0) + w / (60.0 + r)
    for r, cid in enumerate(esparsos_ids, 1):
        rrf[cid] = rrf.get(cid, 0.0) + (2.0 - w) / (60.0 + r)
    por_id = {d["claim_id"]: d for d in docs}
    ordenados = sorted(rrf, key=lambda x: (-rrf[x], str(x)))[:top_k]
    # `margin` = 1o menos 2o, mesma definicao do BM25, mas em unidades RRF. NAO comparar
    # com as faixas de `_params_confianca()` (calibradas em score BM25): a confianca do
    # topo do sistema e' calculada sobre o ramo esparso, nao sobre este numero.
    margem_rrf = rrf[ordenados[0]] - rrf[ordenados[1]] if len(ordenados) > 1 else 0.0
    saida = []
    for pos, cid in enumerate(ordenados):
        d = por_id.get(cid)
        if not d:
            continue
        saida.append({
            "claim_id": d["claim_id"],
            "score": round(rrf[cid], 6),
            "margin": round(margem_rrf, 6) if pos == 0 else None,
            "category": d.get("category"),
            "claim": d["claim"],
            "context_prefix": d.get("context_prefix"),
            "platform": d.get("platform"),
        })
    return saida


def handle_tool_call(name, args):
    if name == "tws_expert_search":
        q = args.get("query", "")
        cat = args.get("category")
        top_k = int(args.get("top_k", 5))
        tokens = re.findall(r"\w+", q.lower())
        results = search_bm25(tokens, category=cat, top_k=top_k)
        base_conf = results

        # PONTE EN->PT. Motivo medido: a consulta inglesa e' a lacuna real deste sistema.
        # No proprio buscador abaixo, as 24 perguntas virgens em ingles dao @1 25,0% e
        # @5 50,0%, contra 54,2% e 70,8% quando traduzidas - o corpus e' portugues e a
        # ponte lexical nao existia. A traducao automatica empata com a manual.
        # Desenho: se a consulta NAO e' portuguesa, e' ELA que vai a busca (traduzida),
        # porque toda a evidencia de acerto esta' do lado portugues. Consulta em portugues
        # nao passa pelo tradutor (custo zero) e, sem o modelo instalado, isto vira no-op.
        #
        # NAO usar "melhor dos dois" por score: o score BM25 de duas consultas diferentes
        # nao e' comparavel (depende da IDF dos termos que cada uma contem). Medido: essa
        # comparacao perdia 2 acertos (11 contra 13) porque o score alto da consulta
        # original ganhava com a resposta errada no topo.
        traducao = _traduz(q)
        tokens_finais = tokens
        if traducao:
            tokens_t = re.findall(r"\w+", traducao.lower())
            results_t = search_bm25(tokens_t, category=cat, top_k=top_k)
            if results_t:
                results = results_t
                tokens_finais = tokens_t

        # FUSAO DENSA. Ver RAG_DENSE_MODE no topo do arquivo. Aplicada DEPOIS da ponte,
        # sobre a consulta ORIGINAL: denso multilingue nao precisa da traducao, e usar a
        # traduzida mediria a ponte duas vezes. Sem indice/deps instalados, `_funde_rrf`
        # devolve o resultado esparso intacto - a producao nao quebra, so' nao ganha.
        # O ramo esparso e' relido com PELO MENOS RRF_K candidatos: a fusao do laboratorio
        # (a que tem evidencia medida) usa esparso top-30 + denso top-30, e fundir com so'
        # `top_k` candidatos mede OUTRA coisa - foi assim que uma versao intermediaria
        # escondeu alvos (ausentes 22 -> 35) e outra os reposicionou (ausentes 7, @5 pior).
        # A CONFIANCA fica ancorada no ramo ESPARSO, nao no score fundido. Motivo medido: as
        # faixas de `_params_confianca()` foram calibradas sobre o score BM25 (AUC 0,850 no
        # `margin`), e o score RRF vive em outra escala (~0,03 contra ~5 do BM25). Rotular
        # "alta" a partir de um numero de outra escala seria uma afirmacao nao calibrada -
        # exatamente o que este sistema nao pode fazer. O RRF muda a ORDEM; a confianca
        # continua vindo do sinal que foi calibrado.
        base_conf = results
        if DENSE_MODE == "fuse":
            esparsos = search_bm25(tokens_finais, category=cat, top_k=max(top_k, RRF_K))
            base_conf = esparsos[:top_k]
            results = _funde_rrf(q, esparsos, top_k)

        # Modo antigo (portao duro). OPT-IN e DESLIGADO por padrao: descartar resposta
        # que existia e' regressao (66 acertos perdidos no limiar 0,177). Mantido apenas
        # para quem quiser medir aquele desenho.
        limiar_duro = os.environ.get("RAG_ABSTAIN_MARGIN")
        if limiar_duro is not None and results and base_conf:
            try:
                lim = float(limiar_duro)
            except ValueError:
                lim = 0.0
            if lim > 0:
                s1 = base_conf[0]["score"]
                s2 = base_conf[1]["score"] if len(base_conf) > 1 else 0.0
                mn = (s1 - s2) / s1 if s1 > 0 else 0.0
                if mn < lim:
                    return {"results": [], "count": 0, "abstained": True, "margin": round(mn, 4),
                            "message": "Abstencao DURA ativa (RAG_ABSTAIN_MARGIN); "
                                       "respostas boas sao descartadas por desenho."}

        out = {"results": results, "count": len(results)}

        if results:
            # Margem do ramo esparso (escala calibrada), nao do score fundido.
            s1 = base_conf[0]["score"] if base_conf else 0.0
            s2 = base_conf[1]["score"] if base_conf and len(base_conf) > 1 else 0.0
            margem_norm = (s1 - s2) / s1 if s1 > 0 else 0.0
            p = _params_confianca()
            if margem_norm >= p["faixa_alta"]:
                faixa = "alta"
            elif margem_norm >= p["faixa_media"]:
                faixa = "media"
            else:
                faixa = "baixa"
            out["confianca"] = faixa
            out["margin"] = round(margem_norm, 4)
            out["orientacao"] = MSG_CONFIANCA[faixa]

            # Aviso de versao: o corpus mistura 9.x/10.2.0-10.2.7 com 10.2.8. Medido:
            # quando o top-1 e' de versao diferente, ele acerta 33,3% contra 48,6% das
            # demais ocorrencias - e' sinal util de que a resposta pode nao valer.
            texto_top1 = f"{results[0].get('claim','')} {results[0].get('claim_id','')}"
            if RE_VERSAO_DIFERENTE.search(texto_top1):
                out["alerta_versao"] = (
                    "A evidencia mais bem colocada e' de versao diferente de 10.2.8. "
                    "Confirme a versao antes de afirmar."
                )
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
                                "A resposta traz `confianca` = alta|media|baixa, medida e calibrada: alta acerta ~84%, "
                                "media ~30%, baixa ~20% no benchmark. Use-a ANTES de afirmar: em `baixa`, trate os "
                                "resultados como pistas e não afirme nada; em `media`, confirme com um termo mais "
                                "específico. `alerta_versao` avisa que a evidência é de versão diferente de 10.2.8 "
                                "(o corpus mistura 9.x e 10.2.x). Sempre cite o claim_id como fonte."
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
