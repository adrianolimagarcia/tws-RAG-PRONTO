# -*- coding: utf-8 -*-
"""tws_reranker.py - Segundo estagio neural (Cross-Encoder) para o MCP TWS Expert.

Modelos suportados (armazenados localmente no cache do neural-reranker):
  - BAAI/bge-reranker-large (modo 'large')
  - BAAI/bge-reranker-base  (modo 'base')

Configuracao via ambiente:
  - RAG_RERANK_MODE: 'off' (default seguro), 'large', 'base'
  - RAG_RERANK_TOP_N: numero de candidatos do 1o estagio a reordenar (default: 15)
  - RAG_RERANK_GATE: '0' (default: reordena puro), '1' (protege top-1 se confianca == 'alta')
  - RAG_RERANK_DEVICE: 'auto' (default: cuda se disponivel, senao cpu), 'cpu', 'cuda'
  - RAG_RERANK_CACHE: caminho para hf_cache (padrao aponta para o cache local do hermes)

Garantia de robustez:
  - Nunca lanca excecao para o chamador (MCP). Se deps ou modelo faltarem,
    devolve os candidatos originais intactos.
"""
import os
import sys
from typing import List, Dict, Any, Optional

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS = {
    "large": "BAAI/bge-reranker-large",
    "base": "BAAI/bge-reranker-base",
}

_CACHE = {}
_WARNED = set()


def _cache_dir() -> str:
    return (
        os.environ.get("RAG_RERANK_CACHE")
        or os.environ.get("HF_HOME")
        or os.path.join(os.path.dirname(os.path.dirname(RAIZ)), "hermes", "neural-reranker", "hf_cache")
    )


def modo() -> str:
    return os.environ.get("RAG_RERANK_MODE", "off").strip().lower()


def top_n() -> int:
    try:
        return max(2, int(os.environ.get("RAG_RERANK_TOP_N", "15")))
    except ValueError:
        return 15


def gate_ativo() -> bool:
    return os.environ.get("RAG_RERANK_GATE", "0").strip() in ("1", "true", "yes")


def disponivel() -> bool:
    m = modo()
    if m not in MODELS:
        return False
    try:
        import torch
        from transformers import AutoTokenizer, AutoModelForSequenceClassification
        return os.path.exists(_cache_dir())
    except ImportError:
        return False


def ativo() -> bool:
    return modo() in MODELS


def _obter_modelo():
    m = modo()
    if m not in MODELS:
        return None, None, None

    dev_str = os.environ.get("RAG_RERANK_DEVICE", "auto").strip().lower()
    key = (m, dev_str)
    if key in _CACHE:
        return _CACHE[key]

    try:
        import torch
        from transformers import AutoTokenizer, AutoModelForSequenceClassification

        if dev_str == "auto":
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        else:
            device = torch.device(dev_str)

        model_name = MODELS[m]
        cache = _cache_dir()
        tok = AutoTokenizer.from_pretrained(model_name, cache_dir=cache, local_files_only=True)
        mod = AutoModelForSequenceClassification.from_pretrained(model_name, cache_dir=cache, local_files_only=True)
        mod.to(device)
        mod.eval()
        _CACHE[key] = (tok, mod, device)
        return tok, mod, device
    except Exception as e:
        if m not in _WARNED:
            sys.stderr.write(f"[tws_reranker] falha ao carregar {m}: {e}; operando em no-op\n")
            _WARNED.add(m)
        return None, None, None


def rerank(query: str, candidates: List[Dict[str, Any]], confianca: str = "baixa") -> List[Dict[str, Any]]:
    """Reordena candidatos com cross-encoder neural.
    
    Parametros:
      query: pergunta do usuario
      candidates: lista de dicionarios com campo 'claim'
      confianca: nivel de confianca calculado pelo 1o estagio ('alta', 'media', 'baixa')
      
    Retorno:
      Lista de candidatos reordenados. Em caso de falha ou modo='off',
      devolve `candidates` intacto.
    """
    if not candidates or len(candidates) <= 1:
        return candidates

    if not ativo():
        return candidates

    if gate_ativo() and confianca == "alta":
        # Gate de protecao: 1o estagio com alta margem nao e' perturbado
        return candidates

    tok, mod, dev = _obter_modelo()
    if tok is None or mod is None or dev is None:
        return candidates

    try:
        import torch

        n = min(len(candidates), top_n())
        alvo = candidates[:n]
        restante = candidates[n:]

        pairs = [(query, c.get("claim", "")) for c in alvo]
        inputs = tok(pairs, padding=True, truncation=True, max_length=256, return_tensors="pt")
        inputs = {k: v.to(dev) for k, v in inputs.items()}

        with torch.no_grad():
            logits = mod(**inputs).logits.squeeze(-1)
            if logits.ndim == 0:
                logits = logits.unsqueeze(0)
            scores = logits.cpu().tolist()

        scored_pairs = []
        for c, s in zip(alvo, scores):
            c_copy = dict(c)
            c_copy["rerank_score"] = round(float(s), 4)
            scored_pairs.append((c_copy, s))

        scored_pairs.sort(key=lambda x: x[1], reverse=True)
        reordered = [c for c, _ in scored_pairs]
        return reordered + restante
    except Exception as e:
        if "infer" not in _WARNED:
            sys.stderr.write(f"[tws_reranker] erro na inferencia: {e}; mantendo ordem original\n")
            _WARNED.add("infer")
        return candidates
