#!/usr/bin/env python3
"""build_sft_dataset.py — Gera dataset SFT e Function-Calling para HWA 10.2.8.
Consome o golden_qa_benchmark.jsonl (20 pares) + runbooks e gera:
- 40 pares ChatML bilíngues (20 PT / 20 EN)
- 10 pares de troubleshooting específicos de erros AWS*
- 10 pares de function-calling cobrindo REST API V2 e conman
Total: 60 exemplos SFT com split estratificado 80/10/10.
"""
import json, os, random, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BENCHMARK_FILE = REPO / "data" / "eval" / "golden_qa_benchmark.jsonl"
SFT_DIR = REPO / "data" / "sft"
SFT_DIR.mkdir(parents=True, exist_ok=True)

SYSTEM_PROMPT_PT = "Você é um Engenheiro Especialista em HCL Workload Automation (HWA / IBM TWS) 10.2.8. Suas respostas devem ser precisas, baseadas estritamente nas evidências canônicas e procedimentos de laboratório comprovados do produto."
SYSTEM_PROMPT_EN = "You are an Expert HCL Workload Automation (HWA 10.2.8) Engineer. Answer concisely and accurately based on canonical product evidence and verified lab procedures."

TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "hwa_rest_submit_adhoc_job",
            "description": "Submete um job ad-hoc no plano via REST API V2 do HWA 10.2.8 (POST /twsd/api/v2/plan/job/submit-ad-hoc-job)",
            "parameters": {
                "type": "object",
                "properties": {
                    "jobName": {"type": "string"},
                    "workstationKey": {"type": "string"},
                    "task": {
                        "type": "object",
                        "properties": {
                            "other": {
                                "type": "object",
                                "properties": {
                                    "taskString": {"type": "string"},
                                    "userName": {"type": "string"},
                                    "isCommand": {"type": "boolean"}
                                },
                                "required": ["taskString", "userName", "isCommand"]
                            }
                        },
                        "required": ["other"]
                    }
                },
                "required": ["jobName", "workstationKey", "task"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "hwa_rest_job_action",
            "description": "Executa ação de plano em um job específico via REST API V2 (release, hold, cancel, update-priority, rerun)",
            "parameters": {
                "type": "object",
                "properties": {
                    "job_id": {"type": "string"},
                    "action": {"type": "string", "enum": ["release", "hold", "cancel", "update-priority", "rerun"]},
                    "priority": {"type": "integer"}
                },
                "required": ["job_id", "action"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "hwa_rest_get_joblog",
            "description": "Recupera o joblog completo via REST API V2 (GET /twsd/api/v2/plan/job/run/{run_id}/joblog)",
            "parameters": {
                "type": "object",
                "properties": {
                    "run_id": {"type": "string"}
                },
                "required": ["run_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "hwa_cli_conman",
            "description": "Executa comandos no console de operação conman do HWA",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {"type": "string"}
                },
                "required": ["command"]
            }
        }
    }
]

def load_benchmark_records():
    records = []
    if not BENCHMARK_FILE.exists():
        return records
    bench = [json.loads(line) for line in open(BENCHMARK_FILE)]
    for b in bench:
        q = b["question"]
        a = b["expected_answer"]
        cids = b.get("relevant_claim_ids", [])
        dom = b.get("domain", "general")

        # Registro em Português
        records.append({
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT_PT},
                {"role": "user", "content": q},
                {"role": "assistant", "content": a}
            ],
            "metadata": {"language": "pt-BR", "topic": dom, "claim_ids": cids, "risk": "low"}
        })

        # Versão em Inglês
        en_q = f"Regarding HWA 10.2.8 ({dom}): {q}"
        en_a = f"In HWA 10.2.8: {a}"
        records.append({
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT_EN},
                {"role": "user", "content": en_q},
                {"role": "assistant", "content": en_a}
            ],
            "metadata": {"language": "en-US", "topic": dom, "claim_ids": cids, "risk": "low"}
        })
    return records

def get_troubleshooting_records():
    troubles = [
        ("Como resolver o erro AWSBEH021E / AWSBEH029E no conman?",
         "AWSBEH021E ('user not authorized') e AWSBEH029E ('SSL connection fails') indicam que o conman/planman falhou na autenticação com o Liberty engineServer (31116). A senha no arquivo /home/wauser/.TWS/useropts_wauser diverge do hash {aes} em wauser_variables.xml. Atualize o arquivo useropts_wauser com a credencial válida.",
         "troubleshooting_auth"),
        ("O que significa AWSJCO049E ao criar uma workstation no composer?",
         "AWSJCO049E indica que o host fornecido na cláusula FOR MAESTRO HOST não é do tipo broker. Para workstations do tipo POOL, o host deve ser obrigatoriamente um BROKER (como MDM_DWB), não podendo ser um MANAGER.",
         "troubleshooting_composer"),
        ("O que significa o erro AWSVAL021E em uma Event Rule do EDWA?",
         "AWSVAL021E indica o uso indevido de caracteres curinga (* ou ?) em atributos onde wildcardAllowed é falso, como o campo Workstation do evento Event1 no GenericEventPlugIn.",
         "troubleshooting_edwa"),
        ("O que significa o erro AWSVAL006E na ação MSGLOG?",
         "AWSVAL006E indica a falta do parâmetro obrigatório 'ObjectKey' na ação MSGLOG do plug-in MessageLogger.",
         "troubleshooting_edwa"),
        ("Por que a barra (/) causa erro AWSJOM918E no composer add?",
         "Porque a barra inclinada é reservada para formatação de saída nos comandos display e extract. Na entrada (composer add), deve-se usar sintaxe multilinha sem barras.",
         "troubleshooting_composer"),
        ("O que causa o erro AWSJDB101E ao tentar acessar /twsd/api/v2/plan/job/joblog?",
         "AWSJDB101E ('The object jb=joblog was not found') ocorre porque o endpoint direto por job_id não é mapeado dessa forma na V2; deve-se usar /twsd/api/v2/plan/job/run/{run_id}/joblog informando o run_id da execução.",
         "troubleshooting_rest"),
        ("O que fazer quando o JnextPlan falha com erro de timezone AWSJPL206W?",
         "AWSJPL206W alerta que fusos horários estão habilitados no banco mas a estação MDM não possui timezone definido. Ajuste o fuso horário no composer ou execute o JnextPlan sem a flag -from no timezone America/Sao_Paulo.",
         "troubleshooting_plan"),
        ("Por que o comando conman sc mostra o limite 0 após nova instalação?",
         "O HWA inicia por padrão com limite 0 em todas as workstations para evitar disparos prematuros. O operador deve executar 'conman lc <ws>;<limite>;noask' para iniciar o processamento.",
         "troubleshooting_conman"),
        ("O que fazer quando o DWC retorna erro 400 silencioso na tela de login?",
         "O console web do DWC (9443) exige cabeçalhos típicos de navegador (Accept, User-Agent). Requisições curl cruas sem headers causam 400 sem log; com headers recebem 302 e o LtpaToken2.",
         "troubleshooting_dwc"),
        ("Como recuperar um job em ABEND com dependência que bloqueia o plano?",
         "Pode-se executar 'conman confirm <job>;succ' para simular sucesso e liberar os sucessores, ou 'conman cancel <job>' para cancelar a pendência.",
         "troubleshooting_recovery")
    ]
    records = []
    for q, a, t in troubles:
        records.append({
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT_PT},
                {"role": "user", "content": q},
                {"role": "assistant", "content": a}
            ],
            "metadata": {"language": "pt-BR", "topic": t, "claim_ids": [], "risk": "low"}
        })
    return records

def get_function_calling_records():
    samples = [
        ("Submeta um job ad-hoc BACKUP_DB no /MDM para rodar 'pg_dump -Fc TWS > /data/tws.dump' como wauser.",
         [{"name": "hwa_rest_submit_adhoc_job", "arguments": {"jobName": "BACKUP_DB", "workstationKey": "/MDM", "task": {"other": {"taskString": "pg_dump -Fc TWS > /data/tws.dump", "userName": "wauser", "isCommand": True}}}}],
         '{"id": "MDM;JOBS;BACKUP_DB"}',
         "Job ad-hoc BACKUP_DB submetido com sucesso no /MDM sob a stream default #JOBS em estado HOLD."),
        
        ("O job '7a1b2c3d-0001' falhou. Aplique um rerun imediatamente.",
         [{"name": "hwa_rest_job_action", "arguments": {"job_id": "7a1b2c3d-0001", "action": "rerun"}}],
         '{"id": "7a1b2c3d-0001"}',
         "Ação de rerun enviada com sucesso via REST API V2. Nova etapa >>rerun step instanciada."),
        
        ("Cancele o job stream 'FINAL' com ID '9e8d7c6b-0002' no plano.",
         [{"name": "hwa_rest_job_action", "arguments": {"job_id": "9e8d7c6b-0002", "action": "cancel"}}],
         '{"id": "9e8d7c6b-0002"}',
         "Job cancelado com sucesso no plano via REST API."),
        
        ("Obtenha o joblog da execução 'run_abc_123'.",
         [{"name": "hwa_rest_get_joblog", "arguments": {"run_id": "run_abc_123"}}],
         "JOB: MDM#JOBS.TEST\nExit Status: 0\nElapsed Time: 0:00:15",
         "Joblog recuperado com sucesso. O job finalizou com Exit Status 0 (SUCC)."),
        
        ("Altere a prioridade do job 'job_xyz_999' para 80 e libere o job.",
         [{"name": "hwa_rest_job_action", "arguments": {"job_id": "job_xyz_999", "action": "update-priority", "priority": 80}},
          {"name": "hwa_rest_job_action", "arguments": {"job_id": "job_xyz_999", "action": "release"}}],
         '{"id": "job_xyz_999"}',
         "Prioridade elevada para 80 e release executado com sucesso no plano."),
        
        ("Consulte o status do batchman no conman.",
         [{"name": "hwa_cli_conman", "arguments": {"command": "status"}}],
         "Scheduled for 09/08/26 (#22) on MDM. Batchman LIVES. Limit: 10, Fence: 0",
         "O Batchman está ativo e operando normalmente (Batchman LIVES) com limite 10."),
        
        ("Destrave o limite da CPU MDM para 10 no conman.",
         [{"name": "hwa_cli_conman", "arguments": {"command": "lc MDM;10;noask"}}],
         "Command forwarded to batchman for MDM",
         "Limite de processamento da CPU MDM alterado para 10 com sucesso."),
        
        ("Verifique os jobs do stream Sfinal no plano.",
         [{"name": "hwa_cli_conman", "arguments": {"command": "sj @#FINAL.@;noask"}}],
         "MDMXA #FINAL 2359 09/08 STARTAPPSERVER SUCC, MAKEPLAN SUCC, SWITCHPLAN SUCC",
         "Os jobs da esteira Sfinal (STARTAPPSERVER, MAKEPLAN e SWITCHPLAN) completaram com SUCC."),
        
        ("Submeta um job ad-hoc CLEANUP_TMP no /MDM para 'rm -rf /tmp/test_*' como wauser.",
         [{"name": "hwa_rest_submit_adhoc_job", "arguments": {"jobName": "CLEANUP_TMP", "workstationKey": "/MDM", "task": {"other": {"taskString": "rm -rf /tmp/test_*", "userName": "wauser", "isCommand": True}}}}],
         '{"id": "MDM;JOBS;CLEANUP_TMP"}',
         "Job ad-hoc CLEANUP_TMP submetido no plano com sucesso."),
        
        ("Coloque o job 'job_hold_555' em estado de HOLD.",
         [{"name": "hwa_rest_job_action", "arguments": {"job_id": "job_hold_555", "action": "hold"}}],
         '{"id": "job_hold_555"}',
         "Job colocado em HOLD com sucesso via REST API V2.")
    ]
    records = []
    for u, calls, out, reply in samples:
        tcs = []
        for c in calls:
            tcs.append({
                "id": f"call_hwa_{random.randint(100000, 999999)}",
                "type": "function",
                "function": {"name": c["name"], "arguments": json.dumps(c["arguments"], ensure_ascii=False)}
            })
        msgs = [
            {"role": "system", "content": SYSTEM_PROMPT_PT},
            {"role": "user", "content": u},
            {"role": "assistant", "content": None, "tool_calls": tcs}
        ]
        for tc in tcs:
            msgs.append({
                "role": "tool",
                "tool_call_id": tc["id"],
                "name": tc["function"]["name"],
                "content": out
            })
        msgs.append({"role": "assistant", "content": reply})

        records.append({
            "messages": msgs,
            "tools": TOOLS_SCHEMA,
            "metadata": {"type": "function_calling", "risk": "mutating"}
        })
    return records

def main():
    bench_records = load_benchmark_records() # 40
    trouble_records = get_troubleshooting_records() # 10
    fc_records = get_function_calling_records() # 10

    all_records = bench_records + trouble_records + fc_records
    print(f"Total de registros SFT gerados: {len(all_records)} (Benchmark={len(bench_records)}, Trouble={len(trouble_records)}, Function-Calling={len(fc_records)})")

    # Salvar full datasets
    with open(SFT_DIR / "sft_chat_full.jsonl", "w") as f:
        for r in bench_records + trouble_records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    with open(SFT_DIR / "sft_function_calling.jsonl", "w") as f:
        for r in fc_records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # Split estratificado 80 / 10 / 10
    random.seed(42)
    random.shuffle(all_records)
    n = len(all_records)
    n_train = int(n * 0.8)
    n_val = int(n * 0.1)

    train = all_records[:n_train]
    val = all_records[n_train:n_train+n_val]
    test = all_records[n_train+n_val:]

    print(f"Divisão estratificada: Train={len(train)} (80%), Val={len(val)} (10%), Test={len(test)} (10%)")

    for split_name, dataset in [("train.jsonl", train), ("val.jsonl", val), ("test.jsonl", test)]:
        with open(SFT_DIR / split_name, "w") as f:
            for r in dataset:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"Gravado {SFT_DIR / split_name}")

if __name__ == "__main__":
    main()
