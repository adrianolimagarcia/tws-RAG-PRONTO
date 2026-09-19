"""rag_core — nucleo compartilhado de recuperacao do tws-RAG-PRONTO.

Existe para que o BENCHMARK e a PRODUCAO usem o MESMO recuperador. Antes desta
fatia, `data/eval/evaluate_rag_benchmark.py` definia o scorer lexical e a montagem
do corpus, enquanto `mcp_server/tws_expert_mcp.py` implementava um BM25 proprio e
diferente - logo o benchmark media um recuperador que a producao nao servia.

Submodulos:
- `rag_core.config`  — caminhos de arquivo e switches de ambiente (opt-in, OFF).
- `rag_core.lexical` — tokenizacao, expansao de consulta, BM25, n-grams, familias.
- `rag_core.corpus`  — montagem do corpus indexavel (`load_documents`).

Esta fatia e' REFATORACAO PURA: o codigo foi extraido verbatim do avaliador, sem
melhorias de scorer. `rag_core.corpus` nao e' importado aqui de proposito - ele
depende de `scripts.ragflow_chunker` (que exige a raiz do repo no sys.path).
"""
from . import config, lexical
from .config import AVG_DL, FAMILY_BOOST
from .lexical import (
    FAMILY_LEXICON,
    SYNONYMS,
    TERM_EXPAND,
    _expand_tokens,
    compute_bm25,
    detect_families,
    expand_query,
    extract_ngrams,
    tokenize,
)

__all__ = [
    "config",
    "lexical",
    "AVG_DL",
    "FAMILY_BOOST",
    "FAMILY_LEXICON",
    "SYNONYMS",
    "TERM_EXPAND",
    "tokenize",
    "_expand_tokens",
    "expand_query",
    "compute_bm25",
    "extract_ngrams",
    "detect_families",
]
