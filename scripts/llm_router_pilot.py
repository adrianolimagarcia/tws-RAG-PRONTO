#!/usr/bin/env python3
"""PILOTO do roteador zero-shot por LLM (60 perguntas estratificadas).

CONTEXTO (medido, runbook 5ac): o CE LARGE ganha +13 na fatia B e perde -28 na A. Um roteador
confiavel e' a UNICA via restante para explorar esse sinal. Medido tambem que:
  - o campo has_anchor do benchmark E' a propria fatia (A=True, B/D=False), correlacao PERFEITA;
  - um regex de ancora da' 67,2% (precisao 59,6% na classe A) - quase o baseline 'sempre nao' (59,2%);
  - so' codigos de erro (D1) dao 100% de precisao mas 51,4% de recall -> roteamento ~neutro.
Logo regex nao resolve. Testando classificacao zero-shot por LLM.

CUSTO: 60 chamadas. Medido antes: ~700 prompt_tokens por chamada (o proxy local injeta system
prompt proprio) e 1 token de saida no modelo '-none'. Teto: NAO escalar para as 442 perguntas
sem antes ver a acuracia e o gasto deste piloto.

REGRA DO DONO: isto e' INFERENCIA, nao treino. Nenhum dataset de produto e' usado para treinar
nada; o LLM so' classifica texto de pergunta em tempo de consulta.
"""
import json, os, re, sys, time
import urllib.request

REPO = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
URL = os.environ.get("ROUTER_URL", "http://localhost:8790/v1/chat/completions")
MODEL = os.environ.get("ROUTER_MODEL", "gemini-3.8-flash-none")
N_PER_CLASS = int(os.environ.get("PILOT_N", "30"))
OUT = os.path.join(REPO, "data", "eval", "llm_router_pilot.json")

PROMPT = """Voce classifica perguntas tecnicas sobre HCL Workload Automation (TWS/HWA) em dois tipos.

TIPO A: a pergunta aponta para um FATO PONTUAL E EXATO documentado. Tipicamente contem um
identificador preciso - codigo de erro (ex.: AWSJPL017E, AWSMRC019E, AWSJDB801E), nome de secao
ou arquivo (ex.: Sfinal, FINALPOSTREPORTS, MDM_BK), porta, endpoint, nome de usuario ou
proprietario de arquivo. A resposta e' um valor ou uma acao especifica.

TIPO B: a pergunta e' EXPLICATIVA, CONCEITUAL ou PROCEDIMENTAL - pergunta "por que", "como
funciona", "qual a diferenca", "qual o fluxo", ou descreve um cenario de troubleshooting SEM
citar um identificador exato. A resposta exige sintese ou explicacao.

Pergunta: {q}

Responda apenas A ou B."""


def call(q, retries=2):
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": PROMPT.format(q=q)}],
        "max_tokens": 2048, "temperature": 0,
    }).encode()
    for a in range(retries + 1):
        try:
            req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                d = json.loads(r.read())
            txt = (d["choices"][0]["message"].get("content") or "").strip()
            u = d.get("usage", {})
            return txt, u.get("prompt_tokens", 0), u.get("completion_tokens", 0)
        except Exception as e:
            if a == retries:
                return f"ERRO:{e}", 0, 0
            time.sleep(2)


def main():
    rows = [json.loads(l) for l in open(os.path.join(REPO, "data", "eval", "blind_v3_slices.jsonl"), encoding="utf-8") if l.strip()]
    A = [r for r in rows if r["slice"] == "A_com_ancora"][:N_PER_CLASS]
    B = [r for r in rows if r["slice"] == "B_sem_ancora"][:N_PER_CLASS]
    sample = A + B
    print(f"[pilot] modelo={MODEL}  n={len(sample)} (A={len(A)} B={len(B)})", flush=True)

    recs, tp = [], 0
    fp = fn = tn = 0
    pt = ct = 0
    for i, r in enumerate(sample):
        real = r["slice"] == "A_com_ancora"
        raw, p, c = call(r["question"])
        pt += p
        ct += c
        # normaliza: aceita "A"/"B", "TIPO A", "SIM"/"NAO", com ruido
        up = raw.upper().strip()
        if up.startswith("SIM"):
            pred = True
        elif up.startswith("NAO") or up.startswith("NÃO"):
            pred = False
        else:
            mm = re.search(r"\b([AB])\b", up)
            if mm:
                pred = mm.group(1) == "A"
            else:
                pred = ("A" in up) and ("B" not in up)
        if pred and real:
            tp += 1
        elif pred and not real:
            fp += 1
        elif real and not pred:
            fn += 1
        else:
            tn += 1
        recs.append({"i": i, "slice": r["slice"], "pred": pred, "real": real, "raw": raw[:40]})
        if (i + 1) % 10 == 0:
            print(f"  {i+1}/{len(sample)}  acc parcial {(tp+tn)/(i+1)*100:.1f}%  tokens={pt+ct}", flush=True)

    n = len(sample)
    acc = (tp + tn) / n
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    print(f"\n[pilot] ACURACIA {acc*100:.1f}%  | classe A: precisao {prec*100:.1f}% recall {rec*100:.1f}%"
          f"  (tp={tp} fp={fp} fn={fn} tn={tn})")
    print(f"[pilot] tokens: prompt={pt} completion={ct} total={pt+ct} em {n} chamadas"
          f" -> projecao p/ 442: {(pt+ct)/n*442:.0f} tokens")
    print(f"[pilot] comparacao: regex D1 = 80,2% (precisao A 100%, recall 51,4%) | 'sempre nao' = 59,2%")
    json.dump({"model": MODEL, "n": n, "acc": acc, "prec_A": prec, "recall_A": rec,
               "tp": tp, "fp": fp, "fn": fn, "tn": tn, "prompt_tokens": pt,
               "completion_tokens": ct, "records": recs}, open(OUT, "w"), indent=1)
    print(f"[pilot] gravado {OUT}")


if __name__ == "__main__":
    main()
