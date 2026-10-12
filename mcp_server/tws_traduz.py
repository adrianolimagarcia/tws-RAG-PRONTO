"""Ponte EN->PT para a busca do MCP.

PROBLEMA MEDIDO (no buscador do proprio MCP, corpus de 7.019 claims):
  pergunta inglesa   @1  6/24 (25,0%)  @5 12/24 (50,0%)  MRR 0,342
  mesma pergunta PT  @1 13/24 (54,2%)  @5 17/24 (70,8%)  MRR 0,612
A pergunta em ingles nao acha o documento portugues - nao por falta de conhecimento do
corpus, mas porque a ponte lexical EN->PT nao existe: o glossario curado do projeto
(data/ontology/hwa_bilingual_terms.json, 104 termos) cobre jargao de topico, nao a
linguagem de sintoma que a pergunta virgem usa (3 de 166 palavras inglesas das perguntas).

SOLUCAO: traduzir a consulta para portugues antes de buscar. Modelo dedicado
Helsinki-NLP/opus-mt-tc-big-en-pt (938 MB), CPU. Medido com traducao AUTOMATICA:
  pergunta traduzida  @1 13/24 (54,2%)  @5 17/24 (70,8%)  MRR 0,605   [p=0,0215 @1]
A traducao automatica EMPATA com a traducao humana (13 @1 nos dois) - o mecanismo
funciona sem LLM de grande porte.

CUSTO: ~1,8 s por consulta em CPU (batch 8), ~938 MB de modelo carregado sob demanda.
Por isso o desenho abaixo: a traducao so' acontece quando a consulta NAO e' portuguesa, e
o import do torch/transformers e' PREGUICOSO - consulta em portugues nao paga nada.

DEPENDENCIA (opcional; sem ela a ponte simplesmente nao liga):
    pip install transformers torch sentencepiece sacremoses
Na primeira execucao o modelo e' baixado do HuggingFace (938 MB) e fica em cache. Depois
disso, rodar com HF_HUB_OFFLINE=1 (o modelo e' local). Para desligar a ponte:
RAG_TRADUZ_EN=0. Para trocar de modelo: RAG_TRADUZ_MODELO=<repo HF>.

DEGRADACAO GRACIOSA: se o modelo ou as bibliotecas nao estiverem disponiveis, o modulo
devolve None e o MCP segue exatamente como antes. A ponte e' um acrescimo, nunca um
caminho obrigatorio.
"""
import os
import re
import threading

MODELO = os.environ.get("RAG_TRADUZ_MODELO", "Helsinki-NLP/opus-mt-tc-big-en-pt")
LIGADO = os.environ.get("RAG_TRADUZ_EN", "1") != "0"

# Marcadores de portugues. Servem so' para DECIDIR se vale traduzir: uma consulta ja' em
# portugues nao deve passar pelo tradutor (o modelo e' en->pt, traduzir PT daria lixo) e
# nem pagar a latencia.
PT_MARCADORES = {
    "de", "da", "do", "das", "dos", "uma", "que", "nao", "para", "com", "como", "qual",
    "quais", "onde", "esta", "estao", "foi", "sera", "pelo", "pela", "porque", "erro",
    "mensagem", "produto", "comando", "arquivo", "servidor", "nao", "e", "o", "a",
}
EN_MARCADORES = {
    "the", "is", "are", "was", "were", "does", "did", "what", "which", "how", "when",
    "where", "why", "not", "from", "with", "this", "that", "it", "its", "has", "have",
    "been", "after", "before", "because", "while", "when", "message", "command", "job",
}
RE_ACENTO_PT = re.compile(r"[ãõçáéíóúâêôà]", re.I)

_estado = {"modelo": None, "tok": None, "falhou": False, "traducoes": {}}
_trava = threading.Lock()


def parece_portugues(texto):
    """Heuristica barata: decide se a consulta NAO precisa de traducao."""
    palavras = re.findall(r"[a-zà-ÿ]+", texto.lower())
    if not palavras:
        return True
    pt = sum(1 for p in palavras if p in PT_MARCADORES)
    en = sum(1 for p in palavras if p in EN_MARCADORES)
    if RE_ACENTO_PT.search(texto):
        pt += 1
    return pt >= en


def _carrega():
    """Carrega o modelo uma unica vez, sob demanda. Falha vira `None`, nao excecao."""
    if _estado["modelo"] is not None or _estado["falhou"]:
        return _estado["modelo"]
    try:
        from transformers import MarianMTModel, MarianTokenizer
        _estado["tok"] = MarianTokenizer.from_pretrained(MODELO)
        _estado["modelo"] = MarianMTModel.from_pretrained(MODELO)
        _estado["modelo"].eval()
    except Exception:
        _estado["falhou"] = True
    return _estado["modelo"]


def traduz_para_pt(consulta):
    """Traducao EN->PT da consulta, ou `None` se nao aplicavel/indisponivel.

    Devolve `None` (e o chamador segue com a consulta original) quando: a ponte esta
    desligada, a consulta ja' parece portuguesa, o modelo nao carrega, ou a traducao sai
    vazia. Em nenhum caso levanta excecao - busca nao pode quebrar por causa da ponte.
    """
    if not LIGADO or not consulta or parece_portugues(consulta):
        return None
    with _trava:
        if consulta in _estado["traducoes"]:
            return _estado["traducoes"][consulta]
        mod = _carrega()
        if mod is None:
            return None
        try:
            import torch
            tok = _estado["tok"]
            with torch.no_grad():
                b = tok([consulta], return_tensors="pt", padding=True, truncation=True,
                        max_length=256)
                saida = tok.batch_decode(mod.generate(**b), skip_special_tokens=True)[0]
        except Exception:
            return None
        saida = saida.strip()
        if not saida:
            return None
        _estado["traducoes"][consulta] = saida
        return saida
