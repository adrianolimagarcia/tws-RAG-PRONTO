"""Constantes de caminho e de ambiente do nucleo RAG (rag_core).

Centraliza os caminhos de arquivo e os switches de MEDICAO lidos do ambiente, de
modo que o avaliador e o nucleo compartilhem a MESMA definicao. Este modulo nao
contem logica de recuperacao: so' constantes.

Regras do repo respeitadas aqui:
- sem paths absolutos de usuario: tudo e' derivado de REPO_DIR (a raiz do repo,
  um nivel acima deste arquivo);
- todos os switches sao OPT-IN e default OFF (= comportamento inalterado).
"""
import glob
import os

# Raiz do repo: rag_core/config.py -> rag_core/ -> <repo>
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BENCHMARK_FILE = os.environ.get(
    "RAG_BENCHMARK_FILE",
    os.path.join(REPO_DIR, "data", "eval", "golden_qa_benchmark.jsonl"))
CLAIMS_FILE = os.path.join(REPO_DIR, "data", "evidence", "claims.jsonl")
AWS_MSGS_FILE = os.path.join(REPO_DIR, "data", "evidence", "aws_messages_dictionary.jsonl")
OPTMAN_FILE = os.path.join(REPO_DIR, "data", "evidence", "optman_global_options_catalog.jsonl")
MSGCAT_FILE = os.path.join(REPO_DIR, "data", "evidence",
                           "official-verification-2026-09-11-message-catalog-full.jsonl")
LAB_FILES = sorted(glob.glob(os.path.join(REPO_DIR, "data", "evidence", "lab-validation-*.jsonl")))
# SWITCH DE MEDICAO (opt-in, DEFAULT OFF = comportamento inalterado):
# `RAG_MEASURE_EXCLUDE_EVIDENCE=1` exclui os arquivos lab-validation-* do corpus.
#
# POR QUE EXISTE: sem isto, o corpus e' funcao da PROPRIA SAIDA do agente - cada
# evidencia que ele registra entra no corpus e move as metricas. Medido: remover os 171
# documentos lab_evidence muda o BM25 @1 de 4/40 para 6/40 e o @10 de 12/40 para 14/40
# (hibrido: 6->8 e 25->27). Ou seja, o ATO DE REGISTRAR A MEDICAO PERTURBA O OBJETO
# MEDIDO, e um numero publicado deixa de valer no instante em que e' gravado.
#
# Isto NAO e' uma decisao sobre a producao: as evidencias sao conteudo legitimo e
# continuam ingeridas por default. O switch serve a REPRODUTIBILIDADE DA MEDICAO - rodar
# o benchmark sobre um corpus estavel e comparavel ao longo do tempo.
if os.environ.get("RAG_MEASURE_EXCLUDE_EVIDENCE") == "1":
    LAB_FILES = []
RUNBOOKS_DIR = os.path.join(REPO_DIR, "data", "runbooks")
# 7. Conhecimento DERIVADO (adicionado explicitamente: glob nao pega arquivo novo):
#    (a) man-pages-derived.jsonl  — sintaxe/parafrase PT-BR das 95 man pages do produto,
#        gerado por scripts/extract_man_pages.py (texto cru NAO versionado — licenca);
#    (b) lab-procedures-derived.jsonl — procedimentos operacionais observados no lab.
#    (c) rest-api-derived.jsonl — superficie funcional da REST API V2 (24 familias,
#        276 operacoes), gerado por scripts/extract_rest_api.py. Switch PROPRIO
#        (RAG_INGEST_REST_API) para poder medir esta fonte isolada das man pages:
#        as duas tem efeito de competicao de rank e nao devem ser ligadas em bloco.
KNOWLEDGE_DERIVED = [
    os.path.join(REPO_DIR, "data", "knowledge", "man-pages-derived.jsonl"),
    os.path.join(REPO_DIR, "data", "knowledge", "lab-procedures-derived.jsonl"),
]
KNOWLEDGE_REST_API = [
    os.path.join(REPO_DIR, "data", "knowledge", "rest-api-derived.jsonl"),
]
# GRANULARIDADE DA FONTE REST (opt-in, DEFAULT = familia, comportamento inalterado):
# `RAG_REST_GRANULARITY=operation` troca os 24 registros (um por familia) pelos 276 (um
# por operacao). POR QUE EXISTE: com um registro por familia o benchmark SATURA na
# acuracia do classificador - nao ha' o que escolher dentro da familia, entao nenhuma
# melhoria de RANKING e' mensuravel (medido: rotear para a familia prevista da 94,4% e e'
# aritmeticamente identico a acertar a classificacao). Com um registro por operacao o
# ground truth passa a ser a OPERACAO e a medicao de ranking fica possivel.
# Os dois arquivos tem ids disjuntos, entao nao ha' colisao - mas so' um entra por vez.
KNOWLEDGE_REST_OPS = [
    os.path.join(REPO_DIR, "data", "knowledge", "rest-api-derived-ops.jsonl"),
]
if os.environ.get("RAG_REST_GRANULARITY"):
    # VALIDACAO EXPLICITA: um valor nao reconhecido tem de GRITAR, nao silenciar. Sem
    # isto, escrever 'operacao' (PT) em vez de 'operation' (EN) nao ativava nada, o corpus
    # ficava com os 24 registros de familia, os ids de operacao do benchmark NAO existiam
    # e a medicao dava 0/40 em todas as configuracoes - um falso negativo que parece
    # resultado. Aconteceu exatamente assim na primeira rodada.
    _gran = os.environ["RAG_REST_GRANULARITY"].strip().lower()
    if _gran in ("operation", "operacao", "ops", "op"):
        KNOWLEDGE_REST_API = KNOWLEDGE_REST_OPS
    elif _gran not in ("familia", "family", "fam"):
        raise SystemExit(
            f"RAG_REST_GRANULARITY={os.environ['RAG_REST_GRANULARITY']!r} nao reconhecido. "
            "Use 'operation' (276 registros) ou 'familia' (24 registros, default).")

# Boost aditivo aplicado a cada doc de catalogo da familia detectada na query.
# Configuravel via env RAG_FAMILY_BOOST (default 4): varredura 0-12 mostrou que
# 4 e o ponto de maior ganho no virgem SEM regressao no baseline.
# ATENCAO (metrica DEPENDENTE DO CORPUS): o baseline de referencia NAO e um numero
# fixo. No HEAD d942790 (6869 docs) o baseline 70 e 53/70 @1, 68/70 @10, MRR 0.8214.
# O valor 54/70 (MRR 0.8336) foi medido em 547d53b (corpus menor) e caiu para 53/70
# em d742037 por CRESCIMENTO DE CORPUS (chunks novos competindo no rank 1 em eval-0029),
# nao por nao-determinismo. Cite sempre o numero COM (HEAD, n_docs).
# Ver docs/BENCHMARK_METRIC_PROVENANCE.md.
FAMILY_BOOST = float(os.environ.get("RAG_FAMILY_BOOST", "4"))

# Tamanho medio de documento usado no termo de normalizacao do BM25 (compute_bm25).
AVG_DL = 60

# ---------------------------------------------------------------------------
# Caminhos do indice denso (BGE-M3) usados pelo modo hibrido/denso-puro.
# ---------------------------------------------------------------------------
HYBRID_INDEX = os.environ.get("RAG_DENSE_INDEX") or os.path.join(
    REPO_DIR, "data", "indexes", "corpus_bge_m3_v5.pt")
HYBRID_META = os.environ.get("RAG_DENSE_META") or os.path.join(
    REPO_DIR, "data", "indexes", "corpus_docs_meta_v5.json")

# MASCARA DO RAMO DENSO (opt-in, DEFAULT OFF): quando ligada, o ramo denso so' pode
# devolver documentos que estejam no corpus CARREGADO. Sem isso, um indice construido
# sobre um corpus maior (com evidencia e fontes extra) devolve candidatos que o ramo
# lexical nem enxerga, e a comparacao denso x lexical deixa de ser sobre o MESMO
# conjunto. Preenchida por load_documents(); `set()` vazio = ligada mas ainda nao cheia.
DENSE_MASK = set() if os.environ.get("RAG_DENSE_MASK_TO_CORPUS") == "1" else None
