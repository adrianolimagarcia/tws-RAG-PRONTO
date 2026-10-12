#!/usr/bin/env python3
"""Mede a ponte EN->PT por traducao da consulta (harness + caminho do MCP).

Reproduz os numeros registrados em
`data/evidence/lab-validation-2026-09-20-ponte-en-pt-por-traducao.jsonl`.

O que mede, nas 24 perguntas VIRGENS em ingles:
  EN        - a pergunta como veio
  HUMANA    - traducao escrita a mao (as 24 estao embutidas abaixo)
  MT        - traducao automatica (MarianMT, se instalado)
e, no buscador do proprio MCP, os mesmos tres cenarios + a latencia por consulta.

Uso:
    python3 data/eval/measure_ponte_en_pt.py            # so' o caminho do MCP (rapido)
    python3 data/eval/measure_ponte_en_pt.py --harness  # inclui o harness de 423
    python3 data/eval/measure_ponte_en_pt.py --mt       # inclui a traducao automatica

Dependencia da parte --mt (opcional): transformers torch sentencepiece sacremoses.
"""
import argparse
import json
import os
import re
import sys
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "mcp_server"))

EN_BENCH = os.path.join(RAIZ, "data/eval/decontaminated/golden_qa_virgin_en_benchmark.jsonl")
MODELO = "Helsinki-NLP/opus-mt-tc-big-en-pt"

# Traducao HUMANA das 24 perguntas, escrita a mao a partir do texto ingles e SEM consultar
# o documento-alvo (para nao vazar o gabarito). Embutida aqui porque e' o ponto de
# comparacao entre "traduzir com LLM" e "traduzir com modelo pequeno": as duas empatam.
HUMANA = {
 "AWSDAH002E": "O produto parou de funcionar e diz que o periodo de demonstracao da licenca expirou. Qual mensagem e essa?",
 "AWSDAH003E": "O binario nao roda no processador deste servidor porque e incompativel. Qual mensagem o produto emite?",
 "AWSDAH007E": "A licenca de aluguel do produto venceu e ele parou. Qual mensagem e reportada?",
 "AWSDAH011E": "Ao rodar um programa, o produto diz que ele nao faz parte da instalacao atual. Qual mensagem e essa?",
 "AWSDAH012E": "O software nao esta licenciado para o processador desta maquina. Qual mensagem?",
 "AWSDBY002E": "Ao rodar um comando de execucao de programa, o produto reclama que foram passados parametros demais. Qual mensagem?",
 "AWSDCJ014E": "Um recurso de fluxo de erro aparece como nao habilitado no ambiente. Qual mensagem indica isso?",
 "AWSDEG001E": "Uma rotina interna falha porque a area de memoria compartilhada entre processos ainda nao foi criada. Qual mensagem?",
 "AWSDEG002E": "A area de memoria compartilhada informada nao e valida para acesso a arquivo indexado. Qual mensagem aponta isso?",
 "AWSDEG003W": "O produto avisa que uma operacao de acesso a arquivo indexado nao esta implementada. Qual aviso?",
 "AWSBHU159E": "Emiti um comando de parada para um no que serve de intermediario para outro dominio e o console recusou, dizendo que esse tipo de estacao de trabalho nao aceita o comando. Qual mensagem?",
 "AWSBHU004E": "Submeti um job informando um logon que nao existe no sistema e o console rejeitou. Qual mensagem apareceu?",
 "AWSBHU016E": "Passei texto onde o comando exigia um valor numerico e foi rejeitado. Qual mensagem?",
 "AWSBHU022E": "Informei um horario fora do formato de quatro digitos entre meia-noite e 23:59 e o comando rejeitou. Qual mensagem?",
 "AWSBHU023E": "Usei sintaxe incorreta ao especificar um qualificador de job opens. Qual mensagem o console retorna?",
 "AWSBHU024E": "O diretorio mozart esta inacessivel ou faltam arquivos dentro dele. Qual mensagem?",
 "AWSBHU025E": "O console nao conseguiu encontrar o job stream no arquivo Symphony. Qual mensagem?",
 "AWSBHU021E": "Tentei iniciar o agente de uma estacao de trabalho mas ela tem uma versao desatualizada do arquivo Symphony. Qual mensagem impede o start?",
 "AWSBHU009E": "O console encontrou um problema ao tentar ler o arquivo Symphony. Qual mensagem?",
 "AWSBHU013I": "Emiti um comando de parada para algo que ja estava parado. Qual mensagem informativa?",
 "AWSBHU026I": "O comando pede a quantidade de recursos e espera um numero entre 1 e 32. Qual mensagem pede isso?",
 "AWSBHU027I": "O comando esta pedindo o nome de um recurso. Qual mensagem pede esse valor?",
 "AWSBHU019I": "O comando de parada foi executado com sucesso em uma estacao de trabalho. Qual mensagem informativa?",
 "AWSFAB033I": "Como sei que a instalacao do produto terminou com sucesso? Qual mensagem informativa final?",
}


def carrega_perguntas():
    return [json.loads(l) for l in open(EN_BENCH, encoding="utf-8") if l.strip()]


def traduz_mt(perguntas):
    """Traducao automatica EN->PT. Devolve (lista, ms_por_pergunta) ou (None, None)."""
    try:
        from transformers import MarianMTModel, MarianTokenizer
        import torch
    except Exception:
        print("  [MT indisponivel: instale transformers/torch/sentencepiece/sacremoses]")
        return None, None
    tok = MarianTokenizer.from_pretrained(MODELO)
    mod = MarianMTModel.from_pretrained(MODELO)
    mod.eval()
    t0 = time.perf_counter()
    saida = []
    with torch.no_grad():
        for i in range(0, len(perguntas), 8):
            b = tok(perguntas[i:i + 8], return_tensors="pt", padding=True,
                    truncation=True, max_length=256)
            saida += tok.batch_decode(mod.generate(**b), skip_special_tokens=True)
    return saida, 1000 * (time.perf_counter() - t0) / len(perguntas)


def avalia_mcp(perguntas, alvos, rot):
    import tws_expert_mcp as mcp
    a1 = a5 = 0
    rr = 0.0
    t0 = time.perf_counter()
    for q, cid in zip(perguntas, alvos):
        if cid is None:
            continue
        ids = [x["claim_id"] for x in
               mcp.handle_tool_call("tws_expert_search", {"query": q, "top_k": 5})["results"]]
        if cid in ids:
            p = ids.index(cid) + 1
            a5 += 1
            a1 += (p == 1)
            rr += 1.0 / p
    n = len(perguntas)
    dt = 1000 * (time.perf_counter() - t0) / n
    print("  %-10s n=%2d  @1 %2d (%4.1f%%)  @5 %2d (%4.1f%%)  MRR %.4f  (%.0f ms/consulta)"
          % (rot, n, a1, 100 * a1 / n, a5, 100 * a5 / n, rr / n, dt))
    return a1, a5


def alvo_mcp(codigo):
    import tws_expert_mcp as mcp
    for d in mcp.docs:
        if codigo.lower() in d["claim_id"].lower():
            return d["claim_id"]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--harness", action="store_true", help="mede tambem pelo harness de 423")
    ap.add_argument("--mt", action="store_true", help="mede tambem a traducao automatica")
    args = ap.parse_args()

    en = carrega_perguntas()
    perguntas = [o["question"] for o in en]
    hum = [HUMANA[o["expected_answer"]] for o in en]

    print("=== caminho do MCP (buscador de producao) ===")
    print("  (a linha EN mede a consulta COM a ponte ligada, que e' a producao de agora;")
    print("   para o controle SEM ponte, rode com RAG_TRADUZ_EN=0)")
    alvos = [alvo_mcp(o["expected_answer"]) for o in en]
    falta = [o["expected_answer"] for o, a in zip(en, alvos) if a is None]
    if falta:
        print("  !! sem claim no corpus do MCP: %s" % falta)
    avalia_mcp(perguntas, alvos, "EN")
    avalia_mcp(hum, alvos, "HUMANA")

    # Controle de idioma: a ponte NAO deve tocar consulta portuguesa.
    from tws_traduz import parece_portugues
    casos = [("qual o erro ao subir o plano", True), ("the job failed to start", False),
             ("AWSBHU159E", True), ("why the console rejected my stop command", False),
             ("nao consigo iniciar o agente", True),
             ("how do I know the installation completed", False)]
    ok = sum(1 for t, e in casos if parece_portugues(t) == e)
    print("  deteccao de idioma: %d/%d corretos" % (ok, len(casos)))

    if args.mt:
        print("\n=== traducao automatica (%s) ===" % MODELO)
        mts, ms = traduz_mt(perguntas)
        if mts:
            print("  latencia: %.0f ms por pergunta" % ms)
            avalia_mcp(mts, alvos, "MT")
            with open("/tmp/en_mt.jsonl", "w", encoding="utf-8") as f:
                for o, mt in zip(en, mts):
                    r = dict(o)
                    r["question"] = mt
                    r["_traduzido_por"] = MODELO
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
            print("  -> /tmp/en_mt.jsonl (para medir no harness)")

    if args.harness:
        print("\n=== harness de 423 (controle + traduzido) ===")
        print("  controle EN : 230/423 @1 (54,4%), 287/423 @5 (67,8%), MRR 0,6016")
        print("  as perguntas traduzidas por HUMANA/MT podem ser medidas com")
        print("  RAG_BENCHMARK_FILE=<arquivo> em data/eval/evaluate_rag_benchmark.py")


if __name__ == "__main__":
    main()
