#!/usr/bin/env python3
"""Harness de Avaliacao Automatica do RAG TWS/HWA com Indexacao Hibrida Enriquecida.
Indexa:
- 1.449 claims canonicas (claims.jsonl)
- 335 mensagens canonicas AWS* (aws_messages_dictionary.jsonl)
- 92 opcoes globais do optman (optman_global_options_catalog.jsonl)
- Todas as evidencias de laboratorio (lab-validation-*.jsonl)
- Runbooks estruturados por secoes funcionais com boost ponderado

Mede:
- Hit Rate @ 1, @ 3, @ 5, @ 10
- Mean Reciprocal Rank (MRR)
"""
import glob, json, math, os, re, sys
from collections import defaultdict

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_DIR not in sys.path:
    sys.path.insert(0, REPO_DIR)

from scripts.ragflow_chunker import parse_markdown_ragflow

# ---------------------------------------------------------------------------
# NUCLEO COMPARTILHADO (rag_core): a tokenizacao, a expansao de consulta, o BM25
# e a montagem do corpus vivem num pacote unico, para que o benchmark e a
# producao possam usar o MESMO recuperador. Este arquivo continua sendo o
# ENTRYPOINT executavel (`python data/eval/evaluate_rag_benchmark.py`) e
# RE-EXPORTA os nomes historicos, porque varios scripts fazem
# `import evaluate_rag_benchmark as engine` e usam engine.tokenize,
# engine.load_documents, engine.compute_bm25, engine.detect_families, etc.
#
# FATIA DE REFATORACAO PURA: nada de scorer mudou. O controle obrigatorio tem de
# reproduzir identico ao HEAD. Medido (mesmo env/benchmark, HEAD vs refatorado):
#   6732 docs / @1 172-262 / @10 218-262 / MRR 0.7134  ->  eval_summary.json
#   byte-identico (mesmo sha256) nos dois. ATENCAO: o controle declarado no card
#   citava MRR 0,7133; o valor que o HEAD reproduz e' 0.7134 (0.7134243778091006).
#   A divergencia de 1 digito existe SEM a refatoracao - nao foi ela que a criou.
# ---------------------------------------------------------------------------
from rag_core import config
from rag_core.config import (
    BENCHMARK_FILE, CLAIMS_FILE, AWS_MSGS_FILE, OPTMAN_FILE, MSGCAT_FILE,
    LAB_FILES, RUNBOOKS_DIR, KNOWLEDGE_DERIVED, KNOWLEDGE_REST_API,
    KNOWLEDGE_REST_OPS, HYBRID_INDEX, HYBRID_META, FAMILY_BOOST,
)
from rag_core.lexical import (
    SYNONYMS, TERM_EXPAND, FAMILY_LEXICON,
    tokenize, _expand_tokens, expand_query, compute_bm25, extract_ngrams,
    detect_families,
)
from rag_core.corpus import load_documents


# ---------------------------------------------------------------------------
# MODO HIBRIDO (RAG_HYBRID=1) — mede o benchmark pelo caminho que a PRODUCAO usa.
#
# POR QUE EXISTE: o caminho padrao deste avaliador e' BM25 puro. A PRODUCAO usa
# busca hibrida (denso BGE-M3 + BM25) fundida por RRF k=60, conforme
# `scripts/evaluate_pure_virgin_hybrid_cpu.py`. Medir o benchmark REST em BM25 puro
# media uma fonte SEM vetor denso com METADE do recuperador real - e o problema
# medido (cobertura de tokens pergunta<->registro de apenas 26%) e' exatamente do
# tipo que o ramo denso cobre: a pergunta diz 'contagem de objetos' e o registro
# diz 'object count'.
#
# A FUSAO replica a producao: denso top-30 + BM25 top-30 -> RRF 1/(60+r) -> top-20.
# O `top_n` do segundo estagio fica IGUAL ao do caminho BM25 (20) de proposito:
# assim o UNICO delta entre as duas medicoes e' o ramo denso, e o efeito da fonte
# nao se confunde com mudanca de fluxo.
# ---------------------------------------------------------------------------
HYBRID = os.environ.get("RAG_HYBRID") == "1"
# MODO DENSO-PURO (opt-in, DEFAULT OFF). Isola o ramo denso para medir a travessia
# PT->EN: 'raw' devolve o ranking do proprio BGE-M3 sem o segundo estagio (mede o
# sinal cross-lingual do embedding); 'rerank' passa o denso pelo mesmo
# second_stage_rerank da producao. VALIDACAO EXPLICITA: valor nao reconhecido
# levanta erro - a licao do RAG_REST_GRANULARITY, onde um valor errado silenciava
# e produzia um falso negativo que parecia resultado.
DENSE_ONLY = os.environ.get("RAG_DENSE_ONLY", "").strip().lower()
if DENSE_ONLY and DENSE_ONLY not in ("raw", "rerank"):
    raise SystemExit(
        f"RAG_DENSE_ONLY={os.environ['RAG_DENSE_ONLY']!r} nao reconhecido. Use 'raw' ou 'rerank'.")
DENSE_ONLY_TOP = int(os.environ.get("RAG_DENSE_TOP", "30"))
# Quantos candidatos o segundo estagio processa (default 20 = comportamento de sempre).
RERANK_TOP = int(os.environ.get("RAG_RERANK_TOP", "20"))
# MASCARA DO RAMO DENSO: definida em `rag_core.config` (DENSE_MASK), porque quem a
# PREENCHE e' `rag_core.corpus.load_documents()`. Aqui le-se SEMPRE via `config.`
# (atributo do modulo), nunca por valor - senao a mutacao feita pelo corpus nao
# seria vista por _dense_top30.
# PESO DA FUSAO RRF (default 0.5 = peso igual, comportamento de sempre): peso do ramo
# DENSO; o esparso recebe 1-w. Ver o docstring de _rrf_fuse.
RRF_W = float(os.environ.get("RAG_RRF_W", "0.5"))
if not (0.0 <= RRF_W <= 1.0):
    raise SystemExit(f"RAG_RRF_W={RRF_W} fora de [0,1].")
_DENSE: dict = {}


def _dense_init():
    """Carrega matriz densa + BGE-M3. So' executa no modo hibrido."""
    if _DENSE:
        return _DENSE
    import torch
    from transformers import AutoModel, AutoTokenizer

    cache = os.environ.get("HF_HOME") or os.path.join(
        os.path.dirname(REPO_DIR), "neural-reranker", "cache")
    device = torch.device("cpu")
    matriz = torch.load(HYBRID_INDEX, map_location=device, weights_only=False).float()
    with open(HYBRID_META) as f:
        ids = json.load(f)
    tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=cache)
    mod = AutoModel.from_pretrained("BAAI/bge-m3", cache_dir=cache, use_safetensors=True).to(device)
    mod.eval()
    _DENSE.update(matriz=matriz, ids=ids, tok=tok, mod=mod, device=device)
    return _DENSE


def _dense_top30(q_text, k=30):
    """Top-k do ramo denso, identico a producao: CLS normalizado, cosseno.

    RAG_DENSE_MASK_TO_CORPUS=1 (opt-in, default OFF): zera o score de qualquer doc do
    indice que NAO esteja no corpus carregado. Sem isso, um indice construido sobre um
    corpus maior pode devolver candidatos que o ramo lexical nem enxerga - e a
    comparacao denso x lexical deixa de ser sobre o MESMO conjunto de documentos.
    """
    import torch

    d = _dense_init()
    with torch.no_grad():
        qi = d["tok"]([q_text], padding=True, truncation=True, max_length=128,
                      return_tensors="pt").to(d["device"])
        qo = d["mod"](**qi)
        qe = torch.nn.functional.normalize(qo.last_hidden_state[:, 0, :], p=2, dim=1).float()
        sc = torch.mm(qe, d["matriz"].T).squeeze(0)
        if config.DENSE_MASK:
            for i, did in enumerate(d["ids"]):
                if did not in config.DENSE_MASK:
                    sc[i] = float("-inf")
        k = min(k, int((sc > float("-inf")).sum().item()))
        if k <= 0:
            return []
        top = torch.topk(sc, k=k).indices.tolist()
    return [d["ids"][i] for i in top]


def _rrf_fuse(q_text, sparse_docs, docs, k_dense=30, k_sparse=30, top=20):
    """Fusao RRF k=60 do ramo denso com o esparso, como na producao.

    RAG_RRF_W (default 0.5 = RRF de peso igual, comportamento de sempre): peso do ramo
    DENSO; o esparso recebe 1-w. Existe porque foi medido que a fusao de peso igual
    aterrissa ENTRE os dois ramos e perde o melhor, nos DOIS sentidos (corpus REST, onde
    o fraco e' o esparso; corpus geral, onde o fraco e' o denso). O ponto do switch NAO e'
    achar um peso bom: e' medir a CURVA e ver se o peso otimo e' ESTAVEL entre conjuntos.
    Se nao for, a fusao ponderada herda o mesmo defeito da particao - nao existe peso
    global que sirva.
    """
    dense_ids = _dense_top30(q_text, k_dense)
    sparse_ids = [d["id"] for _, d in sparse_docs[:k_sparse]]
    # 2*w e 2*(1-w): com w=0.5 isto da' 1.0 nos DOIS ramos, reproduzindo EXATAMENTE a
    # escala do RRF anterior. Nao usar w/(1-w) direto - com w=0.5 ele daria metade da
    # escala, e como o segundo estagio SOMA bonus fixos ao score recebido, mudar a escala
    # muda o balanco mesmo quando a ordem dos candidatos e' a mesma.
    w = 2.0 * RRF_W
    rrf: dict = {}
    for r, did in enumerate(dense_ids, 1):
        rrf[did] = rrf.get(did, 0.0) + w / (60.0 + r)
    for r, did in enumerate(sparse_ids, 1):
        rrf[did] = rrf.get(did, 0.0) + (2.0 - w) / (60.0 + r)
    fundidos = sorted(rrf.keys(), key=lambda x: (-rrf[x], str(x)))[:top]
    por_id = {d["id"]: d for d in docs}
    return [(rrf[i], por_id[i]) for i in fundidos if i in por_id]


def second_stage_rerank(query_raw, candidates, top_n=20):
    """Segundo Estágio de Re-ranking: Proximidade de Termos, N-grams Exatos e Cobertura.
    Desempata candidatos do primeiro estágio avaliando frases contíguas e densidade.
    """
    clean_words = [w.strip(".,;:?!'\"()[]{}").lower() for w in re.findall(r"[A-Za-z0-9_\-]+", query_raw) if len(w) > 2]
    unique_q_terms = set(clean_words) - {"qual", "quais", "como", "onde", "por", "que", "para", "com", "dos", "das", "uma", "não", "mais"}
    bigrams = extract_ngrams(clean_words, 2)
    trigrams = extract_ngrams(clean_words, 3)

    reranked = []
    # Processar os top_n candidatos para refinar precisão no Top 1-3
    for s, doc in candidates[:top_n]:
        text_lower = doc["text"].lower()
        title_lower = (doc.get("title") or "").lower()
        score = s

        # 1. Bônus de Bigrams Contíguos da Pergunta
        for bg in bigrams:
            if len(bg) > 6 and bg in text_lower:
                score += 8.0
            if len(bg) > 6 and bg in title_lower:
                score += 12.0

        # 2. Bônus de Trigrams Contíguos da Pergunta
        for tg in trigrams:
            if len(tg) > 10 and tg in text_lower:
                score += 15.0
            if len(tg) > 10 and tg in title_lower:
                score += 20.0

        # 3. Cobertura de Termos Únicos (Coverage Ratio)
        doc_tokens = doc["tokens"]
        if unique_q_terms:
            covered = len(unique_q_terms.intersection(doc_tokens))
            cov_ratio = covered / len(unique_q_terms)
            if cov_ratio >= 0.80:
                score *= 1.25
            elif cov_ratio >= 0.60:
                score *= 1.12

        # 4. Exact Technical Entity Match (Boost para entidade única no ID e comandos)
        doc_id_lower = doc.get("id", "").lower()
        ignore_meta_terms = {"opcao", "global", "regra", "documentada", "ambiente", "distribuida", "distributed", "workload", "automation", "sobre", "conforme", "oficial", "documentacao", "neste", "para", "como"}
        for term in sorted(unique_q_terms):  # ordem deterministica (set -> hash-seed)
            clean_term = term.replace("-", "").replace("_", "")
            if len(clean_term) >= 5 and clean_term not in ignore_meta_terms:
                if clean_term in doc_id_lower.replace("-", "").replace("_", ""):
                    score += 32.0
            # Códigos de erro canônicos (AWS* ou AWK*)
            if re.match(r"^[a-z]{3,6}[0-9]{3,5}[a-z]?$", clean_term):
                if clean_term in doc_id_lower.replace("-", ""):
                    # Se for a claim oficial de troubleshooting daquele erro, boost de Top-1
                    if "trouble" in doc_id_lower or "messages" in doc_id_lower or "incident" in doc_id_lower:
                        score += 55.0
                    else:
                        score += 45.0
                elif clean_term in text_lower:
                    score += 25.0
            # Casamento por sufixo numérico de erro (ex: 0100e, 001e, 035w)
            num_match = re.search(r"[0-9]{3,5}[a-z]$", clean_term)
            if num_match and num_match.group(0) in doc_id_lower:
                score += 25.0

        # 5. Exact Command & Subcommand Pairing Boost (ex: 'composer add', 'conman start', 'optman ls', 'planman showinfo')
        cli_pairs = [
            ("composer", "add"), ("composer", "extract"), ("composer", "delete"), ("composer", "modify"),
            ("conman", "start"), ("conman", "stop"), ("conman", "fence"), ("conman", "limit"),
            ("conman", "confirm"), ("conman", "release"), ("conman", "rerun"), ("conman", "showjobs"),
            ("conman", "status"), ("conman", "switcheventprocessor"),
            ("planman", "showinfo"), ("planman", "checksync"), ("planman", "resync"), ("planman", "resetplan"),
            ("optman", "ls"), ("optman", "chg"), ("optman", "cf")
        ]
        q_raw_lower = query_raw.lower()
        for cmd, sub in cli_pairs:
            if cmd in q_raw_lower and sub in q_raw_lower:
                if (cmd in doc_id_lower and sub in doc_id_lower) or (f"{cmd} {sub}" in text_lower[:200]):
                    score += 35.0

        reranked.append((score, doc))

    # Reordenar os top_n re-rankeados
    # Desempate deterministico por id do documento: sem isso, empates de score sao resolvidos
    # pela ordem de insercao (que vem de glob.glob, dependente do filesystem) -> metrica nao reprodutivel.
    reranked.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    # Manter o restante da cauda na ordem original
    return [r[1] for r in reranked] + [c[1] for c in candidates[top_n:]]

def run_evaluation():
    if not os.path.exists(BENCHMARK_FILE):
        print(f"Erro: {BENCHMARK_FILE} nao encontrado.")
        return

    benchmark = [json.loads(line) for line in open(BENCHMARK_FILE)]
    docs = load_documents()
    print(f"Total de documentos indexados no corpus RAG: {len(docs)}")

    top_k_hits = {1: 0, 3: 0, 5: 0, 10: 0, 15: 0}
    reciprocal_ranks = []
    # RECALL@15 (metrica propria, nao derivavel do rank): fracao dos documentos
    # relevantes que aparecem no top-15. Hit@15 diz "achou ALGUM"; recall@15 diz
    # "achou QUANTOS". A producao entrega 15 documentos ao LLM, entao o que limita a
    # resposta e' a fracao que chega, nao a existencia de um acerto.
    recalls15 = []
    results = []

    for b in benchmark:
        qid = b.get("id")
        q_text = b.get("question", "")
        expected_cids = set(b.get("relevant_claim_ids", []))
        expected_runbook = b.get("runbook_ref")
        q_tokens = tokenize(q_text)

        scored = []
        for doc in docs:
            score = compute_bm25(q_tokens, doc["tokens"], q_text, doc["text"], doc=doc)
            if score > 0:
                scored.append([score, doc])

        # Desempate deterministico por id do documento (ver nota em second_stage_rerank)
        scored.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))

        # RAGFlow MMR / Source Diversity: Evitar que múltiplos chunks do mesmo runbook
        # monopolizem o top-K empurrando claims e respostas alternativas para baixo
        diversified_docs = []
        seen_sources = defaultdict(int)
        for s, doc in scored:
            src_key = doc.get("runbook") or doc.get("type")
            count = seen_sources[src_key]
            # Se for chunk de runbook e já tiver 2 chunks desse mesmo runbook no topo,
            # adia ou penaliza chunks repetidos para dar espaço à diversidade de evidência
            if doc.get("type") == "ragflow_runbook_chunk" and count >= 2:
                s *= 0.65
            seen_sources[src_key] += 1
            diversified_docs.append((s, doc))

        # Reordenar após penalização de repetição de fonte
        # Desempate deterministico por id (mesma classe de bug dos outros sorts: sem ele,
        # empates caiam na ordem de insercao e a metrica variava entre processos).
        diversified_docs.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))

        # MODO HIBRIDO: funde o ramo esparso com o denso (RRF k=60) antes do
        # segundo estagio. Sem o switch, o comportamento e' o de sempre (BM25 puro).
        # MODO DENSO-PURO (RAG_DENSE_ONLY): isola o ramo denso para medir a travessia
        # PT->EN. 'raw' = o ranking do proprio BGE-M3, SEM o segundo estagio (mede o
        # sinal cross-lingual do embedding, que e' a pergunta); 'rerank' = o denso
        # passando pelo mesmo second_stage_rerank da producao (mede a forma final).
        if DENSE_ONLY:
            _por_id = {d["id"]: d for d in docs}
            _dids = _dense_top30(q_text, DENSE_ONLY_TOP)
            # NOTA: o score e' so' um portador de ORDEM (1.0, 0.999999, ...) - o que
            # vale aqui e' a posicao do BGE-M3. Nomear os dois lados do enumerate
            # separadamente nao e' estilo: `for i, i in ...` sombreia o INDICE com a
            # string do id e quebra em `i * 1e-6` (TypeError, ja' aconteceu).
            candidatos = [(1.0 - _r * 1e-6, _por_id[_did])
                          for _r, _did in enumerate(_dids) if _did in _por_id]
        elif HYBRID:
            candidatos = _rrf_fuse(q_text, diversified_docs, docs)
        else:
            candidatos = diversified_docs

        # Segundo Estágio de Re-ranking: Desempate por N-Grams contíguos e Cobertura Semântica
        # RAG_RERANK_TOP (default 20 = comportamento de sempre): o reranker processa
        # SOMENTE candidates[:top_n] - ou seja, ele CORTA o pool, nao so' reordena.
        if DENSE_ONLY == "raw":
            retrieved_docs = [d for _, d in candidatos[:20]]
        else:
            retrieved_docs = second_stage_rerank(q_text, candidatos, top_n=RERANK_TOP)

        rank = None
        for idx, d in enumerate(retrieved_docs):
            is_match = False
            # Match 1: claim id exato
            if d["id"] in expected_cids:
                is_match = True
            # Match 2: match por codigo de mensagem se houver
            elif d["type"] == "aws_message":
                for ecid in expected_cids:
                    if d.get("code", "").lower() in ecid.lower():
                        is_match = True
            # Match 3: match por chunk estruturado de runbook com overlap substantivo (>= 2 tokens ou >= 25% da query)
            elif (d["type"] == "ragflow_runbook_chunk" or d["type"] == "runbook_section") and expected_runbook and d.get("runbook") == expected_runbook:
                overlap_count = len(q_tokens.intersection(d["tokens"]))
                if overlap_count >= 2 and (overlap_count / max(1, len(q_tokens))) >= 0.25:
                    is_match = True

            if is_match:
                rank = idx + 1
                break

        if rank is not None:
            reciprocal_ranks.append(1.0 / rank)
            if rank <= 1: top_k_hits[1] += 1
            if rank <= 3: top_k_hits[3] += 1
            if rank <= 5: top_k_hits[5] += 1
            if rank <= 10: top_k_hits[10] += 1
            if rank <= 15: top_k_hits[15] += 1
        else:
            reciprocal_ranks.append(0.0)

        # recall@15: fracao dos relevantes presentes no top-15 (o que a producao entrega)
        _top15 = {d.get("id") for d in retrieved_docs[:15]}
        recalls15.append(len(_top15.intersection(expected_cids)) / max(1, len(expected_cids)))

        results.append({
            "id": qid,
            "domain": b.get("domain"),
            "question": q_text,
            "rank": rank,
            "expected_claims": list(expected_cids),
            "expected_runbook": expected_runbook,
            "top_3_retrieved": [d["id"] for d in retrieved_docs[:3]]
        })

    total = len(benchmark)
    mrr = sum(reciprocal_ranks) / total if total else 0.0

    print("==================================================")
    print("      RELATÓRIO DE AVALIAÇÃO DO RAG BENCHMARK     ")
    print("==================================================")
    print(f"Total de Perguntas Avaliadas: {total}")
    print(f"Hit Rate @ 1:  {top_k_hits[1]}/{total} ({top_k_hits[1]/total*100:.1f}%)")
    print(f"Hit Rate @ 3:  {top_k_hits[3]}/{total} ({top_k_hits[3]/total*100:.1f}%)")
    print(f"Hit Rate @ 5:  {top_k_hits[5]}/{total} ({top_k_hits[5]/total*100:.1f}%)")
    print(f"Hit Rate @ 10: {top_k_hits[10]}/{total} ({top_k_hits[10]/total*100:.1f}%)")
    print(f"Hit Rate @ 15: {top_k_hits[15]}/{total} ({top_k_hits[15]/total*100:.1f}%)")
    print(f"Recall @ 15:   {sum(recalls15)/max(1,len(recalls15)):.4f}")
    print(f"Mean Reciprocal Rank (MRR):    {mrr:.4f}")
    print("==================================================")

    out_file = os.path.join(REPO_DIR, "data", "eval", "eval_summary.json")
    with open(out_file, "w") as f:
        json.dump({
            "total": total,
            "hit_rate_at_1": top_k_hits[1] / total,
            "hit_rate_at_3": top_k_hits[3] / total,
            "hit_rate_at_5": top_k_hits[5] / total,
            "hit_rate_at_10": top_k_hits[10] / total,
            "hit_rate_at_15": top_k_hits[15] / total,
            "recall_at_15": sum(recalls15) / max(1, len(recalls15)),
            "mrr": mrr,
            "details": results
        }, f, indent=2, ensure_ascii=False)
    print(f"Sumário de avaliação gravado em {out_file}")

if __name__ == "__main__":
    run_evaluation()
