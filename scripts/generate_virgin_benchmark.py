#!/usr/bin/env python3
"""Benchmark VIRGEM de mensagens: perguntas sem citar o codigo e sem copiar o texto literal.

Motivo: o benchmark anterior continha o codigo na propria pergunta e o harness da boost +15.0
para match exato de codigo -> Hit@1=100% era TAUTOLOGICO. Aqui a pergunta descreve o cenario
operacional em linguagem natural; a recuperacao tem que vir do CONTEUDO da mensagem.

Criterios:
- A pergunta NUNCA contem o codigo (verificado por assercao).
- A pergunta parafraseia o sintoma/cenario, nao cita o texto da mensagem verbatim.
- Mix de familias que NAO existiam na doc publica (DAH/DBY/DCJ/DEG) e classicas (BHU/FAB) como controle.

Saida: data/eval/golden_qa_virgin_benchmark.jsonl
"""
import json, re, os

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
OUT = f"{BASE}/data/eval/golden_qa_virgin_benchmark.jsonl"

# (codigo, familia_nova?, pergunta virgem)
Q = [
    # --- familias que NAO existiam na documentacao publica ---
    ("AWSDAH002E", True,  "O produto parou de funcionar e acusa que o periodo de demonstracao da licenca terminou. Qual e a mensagem?"),
    ("AWSDAH003E", True,  "O binario nao roda no processador deste servidor porque e incompativel. Que mensagem o produto emite?"),
    ("AWSDAH007E", True,  "A licenca de aluguel do produto venceu e ele parou. Qual mensagem e reportada?"),
    ("AWSDAH011E", True,  "Ao executar um programa, o produto diz que ele nao faz parte da instalacao atual. Que mensagem e essa?"),
    ("AWSDAH012E", True,  "O software nao possui licenca valida para o processador desta maquina. Qual a mensagem?"),
    ("AWSDBY002E", True,  "Ao rodar um comando de execucao de programa, o produto reclama que foi passado um numero excessivo de parametros. Qual a mensagem?"),
    ("AWSDCJ014E", True,  "Uma funcionalidade de fluxo de erro aparece como nao habilitada no ambiente. Que mensagem indica isso?"),
    ("AWSDEG001E", True,  "Uma rotina interna falha porque a area de memoria compartilhada entre processos ainda nao foi criada. Qual a mensagem?"),
    ("AWSDEG002E", True,  "A area de memoria compartilhada informada nao serve para acesso a arquivos indexados. Que mensagem aponta isso?"),
    ("AWSDEG003W", True,  "O produto avisa que uma operacao de acesso a arquivo indexado nao foi implementada. Qual o aviso?"),

    # --- familias classicas (controle: ja estavam documentadas) ---
    ("AWSBHU159E", False, "Emiti um comando de parada para um no que atua como intermediario de outro dominio e o console recusou, alegando que aquele tipo de estacao nao aceita o comando. Qual a mensagem?"),
    ("AWSBHU004E", False, "Submeti um job informando um logon que nao existe no sistema e o console rejeitou a submissao. Que mensagem apareceu?"),
    ("AWSBHU016E", False, "Passei um texto onde o comando exigia um valor numerico e ele foi recusado. Qual a mensagem?"),
    ("AWSBHU022E", False, "Informei um horario fora do formato de quatro digitos entre meia-noite e 23:59 e o comando rejeitou. Qual a mensagem?"),
    ("AWSBHU023E", False, "Usei sintaxe incorreta ao informar um qualificador de job do tipo opens. Que mensagem o console devolve?"),
    ("AWSBHU024E", False, "O diretorio mozart esta inacessivel ou faltam arquivos dentro dele. Qual a mensagem?"),
    ("AWSBHU025E", False, "O console nao encontrou o job stream no arquivo Symphony. Qual a mensagem?"),
    ("AWSBHU021E", False, "Tentei subir o agente de uma estacao, mas ele esta com uma versao desatualizada do arquivo Symphony. Que mensagem impede a partida?"),
    ("AWSBHU009E", False, "O console encontrou um problema ao tentar ler o arquivo Symphony. Qual a mensagem?"),
    ("AWSBHU013I", False, "Emiti um comando de parada para algo que ja estava parado. Qual a mensagem informativa?"),
    ("AWSBHU026I", False, "O comando pede a quantidade de recursos e espera um numero entre 1 e 32. Qual a mensagem que solicita isso?"),
    ("AWSBHU027I", False, "O comando esta pedindo o nome de um recurso. Que mensagem solicita esse dado?"),
    ("AWSBHU019I", False, "O comando de parada foi executado com sucesso sobre uma estacao. Qual a mensagem informativa?"),
    ("AWSFAB033I", False, "Como sei que a instalacao do produto terminou com exito? Qual a mensagem informativa final?"),
]


def main():
    rows, bad = [], []
    for code, nova, pergunta in Q:
        # assercao: a pergunta NAO pode conter o codigo
        if re.search(r"aws[a-z0-9]{3}[0-9]{3}[iwe]", pergunta, re.I):
            bad.append(code)
            continue
        rows.append({
            "id": f"virgin-{code.lower()}",
            "domain": "mensagens_virgem/" + ("novas" if nova else "classicas"),
            "question": pergunta,
            "expected_answer": code,
            "relevant_claim_ids": [f"hwa-msgcat-{code.lower()}"],
            "runbook_ref": None,
        })
    if bad:
        raise SystemExit(f"ERRO: perguntas contendo codigo: {bad}")
    with open(OUT, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    n_novas = sum(1 for r in rows if "novas" in r["domain"])
    print(f"geradas {len(rows)} perguntas virgens ({n_novas} de familias novas, "
          f"{len(rows)-n_novas} classicas) -> {OUT}")
    print("verificacao: nenhuma pergunta contem codigo AWS. OK")


if __name__ == "__main__":
    main()
