#!/usr/bin/env python3
"""Expande o benchmark virgem com perguntas das familias recém-parafraseadas (BIA/BIS/BCT).

Objetivo: medir honestamente o valor de escalar a parafrase — o benchmark original de 24
so testava DAH/DBY/DCJ/DEG/BHU/FAB. Aqui adicionamos perguntas virgens (sem codigo) para
mensagens BIA (composer) e BIS (plan library) ja parafraseadas por LLM.
Saida: data/eval/golden_qa_virgin_expanded.jsonl
"""
import json, re, os

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
ORIG = f"{BASE}/data/eval/golden_qa_virgin_benchmark.jsonl"
OUT = f"{BASE}/data/eval/golden_qa_virgin_expanded.jsonl"

# (codigo, pergunta virgem)
NEW = [
    ("AWSBIA008E", "Criei um job stream no composer mas ele nao foi localizado pelo nome informado. Que mensagem o composer devolve?"),
    ("AWSBIA021E", "Referenciei um job que nao existe dentro do job stream especificado e o composer reclamou. Qual mensagem?"),
    ("AWSBIA018E", "Tentei adicionar um job que ja existe dentro do job stream e o composer recusou por duplicidade. Qual mensagem?"),
    ("AWSBIA023E", "O job que referenciei nao existe no mestre de jobs. Que mensagem o composer emite ao validar?"),
    ("AWSBIA024E", "Outro operador alterou o job enquanto eu atualizava a definicao e a gravacao foi abortada por seguranca. Qual mensagem?"),
    ("AWSBIA014E", "Tentei atualizar um calendario que outra pessoa ja havia modificado e a mudanca nao foi aplicada para evitar conflito. Qual mensagem?"),
    ("AWSBIA015I", "Como confirmo que um novo job stream foi adicionado com sucesso ao repositorio de definicoes? Qual mensagem informativa?"),
    ("AWSBIA002E", "O composer acusou que faltou um identificador obrigatorio em algum ponto da definicao. Qual mensagem?"),
    ("AWSBIA003E", "Informei um parametro onde ele nao deveria estar presente e o composer gerou erro na interpretacao. Qual mensagem?"),
    ("AWSBIA004E", "Faltou o delimitador obrigatorio na posicao atual da definicao. Que mensagem o composer emite?"),
    ("AWSBIA019E", "A validacao da sequencia de trabalhos apontou uma quantidade de erros e avisos que precisam ser revistos. Qual mensagem?"),
    ("AWSBIA010E", "A geracao automatica de documentacao nao esta habilitada para o job e a operacao foi recusada. Qual mensagem?"),
    ("AWSBIA006E", "Ocorreu um erro ao acessar o banco de dados, impedindo a conclusao da operacao no composer. Qual mensagem?"),
    ("AWSBIA034E", "Nenhuma sequencia de trabalhos foi localizada dentro da definicao informada. Que mensagem aparece?"),
    ("AWSBIA035I", "Foi localizada uma quantidade especifica de sequencias de trabalhos dentro da definicao consultada. Qual mensagem informativa?"),
]


def main():
    rows = [json.loads(l) for l in open(ORIG, encoding="utf-8") if l.strip()]
    orig_ids = {r["id"] for r in rows}
    added = 0
    for code, pergunta in NEW:
        if re.search(r"aws[a-z0-9]{3}[0-9]{3}[iwe]", pergunta, re.I):
            raise SystemExit(f"ERRO: pergunta contem codigo: {code}")
        cid = f"virgin-{code.lower()}"
        if cid in orig_ids:
            continue
        rows.append({
            "id": cid, "domain": "mensagens_virgem/escala",
            "question": pergunta, "expected_answer": code,
            "relevant_claim_ids": [f"hwa-msgcat-{code.lower()}"], "runbook_ref": None,
        })
        added += 1
    with open(OUT, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"benchmark expandido: {len(rows)} perguntas (originais {len(orig_ids)} + {added} novas BIA/BIS)")
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
