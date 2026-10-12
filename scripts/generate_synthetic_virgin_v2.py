#!/usr/bin/env python3
"""generate_synthetic_virgin_v2.py — amplia o benchmark VIRGEM de mensagens (pergunta que
descreve o sintoma sem citar o codigo nem copiar o texto da mensagem).

POR QUE ESTE CONJUNTO E O QUE IMPORTA
-------------------------------------
Medido (data/evidence/lab-validation-2026-09-20-dense-fusion-pooled-verdict.jsonl):
no pool de 296 perguntas limpas a fusao densa REGRIDE (-21, p=0,0111). O UNICO bucket onde
ela ganha de forma consistente e' o benchmark virgem de mensagem (2 conjuntos, +5 e +6) -
pergunta que descreve o sintoma em linguagem natural, sem citar codigo nem texto. E'
exatamente o caso de uso do MCP. Mas n=63 no total e' pequeno demais para decidir. Este
script amplia ESSE bucket, que e' onde a decisao realmente vive.

COMO AS PERGUNTAS FORAM ESCRITAS (e por que nao por template)
-------------------------------------------------------------
A descricao de cada mensagem foi lida pelo autor (LLM) e a pergunta foi REDIGIDA a mao no
estilo dos benchmarks virgem existentes. NAO ha troca automatica de sinonimos: este repo ja'
registrou que gerar pergunta do corpus produz pergunta TAUTOLOGICA. Os campos de controle
(codigo, produto, parametro, verbo operacional) foram extraidos AUTOMATICAMENTE para servir
de ASSERCAO de nao-vazamento, nao para montar o texto:

  1. a pergunta NAO contem o codigo (AWS...)           -> assercao dura, o script falha se violar
  2. a pergunta NAO contem sequencia contigua >= 6 palavras do texto da mensagem
     (nem do texto EN, nem da traducao PT)             -> assercao dura, falha se violar
  3. a pergunta NAO contem o nome do produto nem o placeholder (!1, %s)

Essas 3 assercoes sao o que impede o conjunto de virar tautologico - a mesma classe de erro
que ja' inflou um Hit@1 anterior neste repo (benchmark com o codigo dentro da pergunta).

Saida: data/eval/golden_qa_virgin_messages_expanded.jsonl
"""
import json
import os
import re
import sys

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
OUT = os.path.join(REPO, "data/eval/golden_qa_virgin_messages_expanded.jsonl")

# (codigo, pergunta redigida a mao a partir da descricao do catalogo)
# Bloco por FAMILIA funcional, para que o conjunto nao fique concentrado num componente so'
# (familias novas e classicas misturadas, como nos benchmarks virgem anteriores).
Q = [
    # --- instalacao / licenciamento (FAB) ---
    ("AWSFAB134E", "O instalador recusou as credenciais porque a senha informada para aquele usuario nao confere com a senha valida da conta. Qual mensagem foi emitida?"),
    ("AWSFAB040E", "Rodei o script de instalacao a partir do diretorio home de outro usuario e a execucao foi bloqueada. Que mensagem o produto devolve?"),
    ("AWSFAB318E", "A instalacao em cluster falhou ao interpretar os nomes dos nos que eu passei na operacao. Qual mensagem aponta esse erro interno?"),
    ("AWSFAB227I", "Quero saber qual valor de biblioteca de kernel o sistema esta exigindo para prosseguir. Qual mensagem informativa traz esse requisito?"),

    # --- conman / plano (BHU) ---
    ("AWSBHU065E", "Tentei promover uma estacao a novo gerenciador de dominio, mas ela nao esta no status completo exigido para assumir o papel. Que mensagem impede a promocao?"),
    ("AWSBHU077E", "Emiti um comando de exibicao sem dizer o que eu queria ver e o produto reclamou que faltou indicar os objetos. Qual mensagem apareceu?"),
    ("AWSBHU560E", "Tentei iniciar o monitoramento de eventos e o comando foi recusado porque o recurso de automacao orientada a eventos esta desligado. Qual mensagem explica isso?"),

    # --- composer (BIA) ---
    ("AWSBIA110E", "Tentei consultar uma escala de trabalho especifica e fui barrado por falta de autorizacao sobre ela. Que mensagem o composer devolve?"),
    ("AWSBIA267W", "A definicao de usuario que validei gerou alertas que o operador deveria revisar, sem impedir a operacao. Qual mensagem de aviso foi emitida?"),
    ("AWSBIA036I", "Confirmei a remocao de uma escala de trabalho e o produto avisou que ela foi eliminada em definitivo. Qual mensagem informativa confirma isso?"),

    # --- plan library / biblioteca de planos (BIS) ---
    ("AWSBIS201E", "Tentei criar um calendario com um nome que ja' existe no banco de dados e o produto recusou por duplicidade. Qual mensagem apareceu?"),
    ("AWSBIS020E", "A instalacao nao conseguiu continuar porque o diretorio raiz apontado como home do produto nao existe. Que mensagem aponta o caminho invalido?"),
    ("AWSBIS287E", "Uma maquina do ambiente nao consegue estabelecer conexao com o sistema remoto indicado, travando a comunicacao. Qual mensagem reporta essa falha de conexao?"),

    # --- validacao de definicoes (BCT) ---
    ("AWSBCT026E", "O valor que informei num campo de configuracao foi recusado porque esse campo precisa comecar com uma letra do alfabeto. Qual mensagem aponta essa regra?"),
    ("AWSBCT875E", "Pedi uma operacao que depende do servico remoto, mas esqueci de indicar onde ele fica e o comando foi rejeitado. Que mensagem cobra essa informacao?"),
    ("AWSBCT721E", "A busca por arquivos que combinavam com um padrao informado terminou em erro e o produto reportou a falha com o codigo do sistema. Qual mensagem e' essa?"),
    ("AWSBCT017E", "Durante a leitura da entrada padrao ocorreu um erro reportado pelo sistema operacional. Que mensagem o produto emite ao detectar isso?"),

    # --- mailman / comunicacao (BCV) ---
    ("AWSBCV036W", "O processo de comunicacao nao conseguiu se ligar a estacao pai porque o arquivo de plano da estacao e' incompativel com a versao local. Qual aviso foi emitido?"),
    ("AWSBCV087I", "Uma nova estacao foi incorporada a tabela de estacoes com o no, servidor, tipo de vinculo e flags informados. Qual mensagem informativa registra essa inclusao?"),
    ("AWSBCV130I", "Quero registrar o instante em que a comunicacao comecou a retransmitir para outra estacao os contadores remotos acumulados. Qual mensagem informativa marca esse comeco?"),

    # --- banco de dados interno / bib (BIB) ---
    ("AWSBIB237E", "O nome de uma dependencia condicional usado na definicao tem sintaxe invalida e precisa ser corrigido. Que mensagem de erro aponta isso?"),
    ("AWSBIB230E", "Usei uma palavra-chave numa posicao indevida da definicao e o validador acusou erro de posicionamento. Qual mensagem detalha o problema?"),
    ("AWSBIB229E", "Forneci uma definicao de calendario no formato de intercambio totalmente vazia e o analisador recusou por falta de conteudo. Qual mensagem aponta o problema?"),

    # --- batchman / execucao (BHT) ---
    ("AWSBHT061E", "O gerenciador recebeu um registro de caixa de mensagens avisando que um job terminou de forma inesperada. Que mensagem reporta essa parada anormal?"),

    # --- mensagens informativas de rotina (controle de severidade I) ---
    ("AWSBHU057I", "O arquivo de plano em uso estava desatualizado e o produto avisou que estava migrando automaticamente para a nova versao. Qual mensagem informativa registra essa troca?"),
    ("AWSBIA059I", "Preciso saber quantos recursos existem cadastrados no banco de dados no momento. Qual mensagem informativa traz essa contagem?"),
    ("AWSBHT126I", "Quero consultar a hora corrente no fuso horario da CPU do ambiente. Qual mensagem informativa exibe esse valor?"),
    ("AWSBCT017E", None),  # placeholder removido abaixo
]
Q = [(c, q) for c, q in Q if q]


def blocos(s):
    return re.findall(r"\w+", s.lower())


def contem_ngrama(pergunta, texto, n=6):
    p = blocos(pergunta)
    c = blocos(texto)
    for i in range(len(p) - n + 1):
        alvo = tuple(p[i:i + n])
        for j in range(len(c) - n + 1):
            if tuple(c[j:j + n]) == alvo:
                return " ".join(alvo)
    return None


def main():
    sys.path.insert(0, REPO)
    from rag_core.corpus import load_documents
    docs = load_documents()
    cat = {d["id"]: d for d in docs if d.get("type") == "message_catalog"}

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    rows, falhas = [], []
    vistos = set()
    for code, pergunta in Q:
        cid = "hwa-msgcat-" + code.lower()
        if cid in vistos:
            falhas.append((code, "codigo repetido no bloco Q"))
            continue
        vistos.add(cid)
        d = cat.get(cid)
        if d is None:
            falhas.append((code, "id ausente no corpus: " + cid))
            continue
        texto = d.get("text", "")

        # assercao 1: sem o codigo
        if re.search(r"aws[a-z0-9]{3}[0-9]{3}[iwe]?", pergunta, re.I):
            falhas.append((code, "pergunta contem o codigo"))
            continue
        # assercao 2: sem trecho contiguo >= 6 palavras do doc (que inclui EN e traducao PT)
        trecho = contem_ngrama(pergunta, texto, 6)
        if trecho:
            falhas.append((code, "vaza trecho do doc: '%s'" % trecho))
            continue
        # assercao 3: sem nome do produto nem placeholder
        if re.search(r"workload automation|hcl|!\d|%s", pergunta, re.I):
            falhas.append((code, "pergunta cita produto ou placeholder"))
            continue

        rows.append({
            "id": "virgem2-" + code.lower(),
            "domain": "mensagens_virgem2",
            "question": pergunta,
            "expected_answer": code,
            "relevant_claim_ids": [cid],
            "runbook_ref": None,
            "provenance": "pergunta redigida a mao a partir da descricao do catalogo; "
                          "codigo/produto/placeholder/ngrama>=6 verificados ausentes",
        })

    print("geradas %d perguntas virgens" % len(rows))
    print("rejeitadas %d:" % len(falhas))
    for c, m in falhas:
        print("   %-14s %s" % (c, m))
    if falhas:
        raise SystemExit("ABORTADO: ha pergunta violando as assercoes de nao-vazamento")
    with open(OUT, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("->", OUT)
    print("verificacao: nenhuma pergunta contem codigo, produto, placeholder ou n-grama>=6 do doc")


if __name__ == "__main__":
    main()
