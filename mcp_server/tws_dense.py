"""Ramo DENSO (BGE-M3) para o MCP de producao. OPT-IN: default NAO carrega nada.

POR QUE EXISTE (medido, nao suposto): a fatia rest/ops do pool tem alvo em texto de spec
OpenAPI em INGLES e pergunta em PT-BR, com mediana de sobreposicao de tokens 0,00 e 21/40
casos ZERADOS entre pergunta e alvo. Sem termo compartilhado o BM25 nao tem sinal, por
construcao. O proprio repo ja' mediu, no MESMO conjunto e nas MESMAS 40 perguntas, que o
denso puro (BGE-M3) faz 13/40 @1 contra 1/40 do BM25 (registro de 2026-09-18). A producao,
porem, era BM25 puro - o achado nunca chegou ao buscador.

Receita IDENTICA a' do indice do laboratorio (scripts/build_dense_index_v2.py), para os
vetores ficarem comparaveis: texto truncado, CLS (last_hidden_state[:, 0, :]) + normalize L2,
max_length=128, cosseno. Qualquer desvio aqui invalida a comparacao com o que ja' foi medido.

Nao confundir com a FUSAO densa global: aquela foi testada e PIORA no conjunto grande
(202x181 em 296, p=0,0111, registro de 2026-09-20). Este modulo existe para medir o desenho
que NUNCA foi testado - denso aplicado como RECUPERADOR, nao fundido no ranking lexical.
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDICE_PADRAO = os.path.join(RAIZ, "data", "indexes", "mcp_bge_m3.pt")
META_PADRAO = os.path.join(RAIZ, "data", "indexes", "mcp_docs_meta.json")

_CACHE = {}


def _cache_dir():
    # Mesma convencao do harness do laboratorio: HF_HOME, senao o cache do reranker.
    return os.environ.get("HF_HOME") or os.path.join(
        os.path.dirname(RAIZ), "hermes", "neural-reranker", "hf_cache")


def disponivel(indice=None, meta=None):
    """Ha' deps E artefatos? Nunca levanta - o MCP nao pode quebrar por causa do denso."""
    indice = indice or os.environ.get("RAG_DENSE_INDEX") or INDICE_PADRAO
    meta = meta or os.environ.get("RAG_DENSE_META") or META_PADRAO
    if not (os.path.exists(indice) and os.path.exists(meta)):
        return False
    try:
        import torch  # noqa: F401
        import transformers  # noqa: F401
    except Exception:
        return False
    return True


def _carrega(indice=None, meta=None):
    if _CACHE:
        return _CACHE
    import torch
    from transformers import AutoModel, AutoTokenizer

    indice = indice or os.environ.get("RAG_DENSE_INDEX") or INDICE_PADRAO
    meta = meta or os.environ.get("RAG_DENSE_META") or META_PADRAO
    cache = _cache_dir()
    device = torch.device("cpu")
    matriz = torch.load(indice, map_location=device, weights_only=False).float()
    with open(meta, encoding="utf-8") as f:
        ids = json.load(f)
    tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=cache)
    mod = AutoModel.from_pretrained("BAAI/bge-m3", cache_dir=cache,
                                    use_safetensors=True).to(device)
    mod.eval()
    _CACHE.update(matriz=matriz, ids=ids, tok=tok, mod=mod, device=device)
    return _CACHE


def busca(query, top_k=30):
    """[(claim_id, score_cosseno)] ordenado. Lista vazia se o denso nao estiver disponivel."""
    import torch

    d = _carrega()
    with torch.no_grad():
        qi = d["tok"]([query], padding=True, truncation=True, max_length=128,
                      return_tensors="pt").to(d["device"])
        qo = d["mod"](**qi)
        qe = torch.nn.functional.normalize(qo.last_hidden_state[:, 0, :], p=2,
                                           dim=1).float()
        sc = torch.mm(qe, d["matriz"].T).squeeze(0)
    k = min(top_k, sc.shape[0])
    val, idx = torch.topk(sc, k)
    return [(d["ids"][int(i)], float(v)) for v, i in zip(val, idx)]


def constroi(docs, indice=None, meta=None, lote=64, max_chars=500, dtype=None):
    """Constroi o indice a partir de [(claim_id, texto)]. Mesma receita do lab.

    `docs` e' uma lista de pares - de proposito NAO importamos o MCP aqui para evitar
    ciclo de import e para o construtor poder rodar sobre qualquer corpus.
    """
    import torch
    from transformers import AutoModel, AutoTokenizer

    indice = indice or INDICE_PADRAO
    meta = meta or META_PADRAO
    cache = _cache_dir()
    device = "cpu"
    tok = AutoTokenizer.from_pretrained("BAAI/bge-m3", cache_dir=cache)
    mod = AutoModel.from_pretrained("BAAI/bge-m3", cache_dir=cache,
                                    use_safetensors=True).to(device)
    mod.eval()

    ids = [cid for cid, _ in docs]
    textos = [(t or "")[:max_chars].replace("\n", " ").strip() for _, t in docs]
    partes = []
    with torch.no_grad():
        for i in range(0, len(textos), lote):
            ent = tok(textos[i:i + lote], padding=True, truncation=True,
                      max_length=128, return_tensors="pt").to(device)
            saida = mod(**ent)
            cls = saida.last_hidden_state[:, 0, :]
            partes.append(torch.nn.functional.normalize(cls, p=2, dim=1).cpu())
    emb = torch.cat(partes, dim=0)
    os.makedirs(os.path.dirname(indice), exist_ok=True)
    torch.save(emb.cpu(), indice)
    with open(meta, "w", encoding="utf-8") as f:
        json.dump(ids, f)
    return emb.shape
