import json

base = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
out = f"{base}/data/evidence/lab-validation-2026-09-10-stuck-plan-rootcause-switchplan-dwb.jsonl"

ev = [
{
 "claim_id": "hwa-lab-10.2.8-stuck-plan-rootcause-switchplan-broker-abort-0009",
 "claim": "Causa raiz reproduzivel de plano travado (AWSJPL017E) no HWA 10.2.8 com Dynamic Workload Broker habilitado: o script SwitchPlan executa a parada do plano ('Batchman down') e, durante a sequencia de stop, tenta parar a workstation do broker MDM_DWB; essa parada FALHA com 'CONMAN:AWSBHU076E Conman cannot process the issued command. The following error occurred: stop MDM_DWB for AWSBCT041I Service 2008 started on MDM_DWB'. Com o aborto do SwitchPlan, o flag 'previous action on the production plan did not complete successfully' permanece setado e o batchman fica DOWN, de modo que toda operacao subsequente de plano (planman ext / crt) falha com AWSJPL017E. A liberacao do lock orfao do planner com 'planman unlock' (AWSJPL504I) limpa o flag e o 'planman ext' volta a funcionar imediatamente (AWSJCL062I), o que caracteriza AWSJPL017E como consequencia de lock/fluxo interrompido e NAO de corrupcao do arquivo Symphony. O batchman e restaurado com 'conman start&link @!/@/@;noask' (AWSBHU507I); quando o no local ja nao e o domain manager, os subcomandos de link retornam AWSBHU537E ('neither is the domain manager'), sem impedir o start.",
 "result": "SUCCESS", "risk": "mutating",
 "platform": "Distributed; Linux x86_64; containers tws-hwa/tws-bmdm; HWA 10.2.8",
 "observed_at": "2026-09-10T15:36:00-03:00",
 "test_procedure": "Executado SwitchPlan a partir do no autorizado, capturando o log completo. Observado o aborto no stop de MDM_DWB. Em seguida: (a) 'planman ext' -> AWSJPL017E; (b) 'planman unlock' -> AWSJPL504I; (c) 'planman ext -days 2' -> AWSJCL062I; (d) 'conman status' -> Batchman down; (e) 'conman start&link @!/@/@;noask' -> Batchman LIVES. Ciclo repetido duas vezes com o mesmo resultado.",
 "actual_output": "Cadeia causal completa comprovada: SwitchPlan aborta no stop do DWB -> flag 'did not complete' + batchman down -> AWSJPL017E -> unlock limpa o flag e ext volta a funcionar -> start&link restaura o batchman.",
 "synthetic_questions": [
   "O que causa AWSJPL017E no HWA e como resolver definitivamente?",
   "Por que o SwitchPlan falha ao parar o plano quando existe um Dynamic Workload Broker?",
   "O que significa a mensagem AWSBHU076E com AWSBCT041I durante a troca de plano?",
   "Basta executar planman unlock para resolver AWSJPL017E?",
   "Como subir o batchman apos uma troca de plano que abortou?",
   "O que significa AWSBHU537E ao executar conman link depois de um failover?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: SwitchPlan / Dynamic Workload Broker > Interface: script SwitchPlan e CLI conman > Topico: troubleshooting > plan_recovery [stuck_plan_rootcause]]"
},
{
 "claim_id": "hwa-lab-10.2.8-conman-showcpu-role-flip-after-plan-operations-0010",
 "claim": "No HWA 10.2.8, o asterisco na coluna STATE do 'conman sc @' marca o no LOCAL, nao o domain manager, e as letras adicionais sao bandeiras de estado (J = jobman ativo, M = disponivel como manager, E/A/D/W = estados adicionais). Apos failover e operacoes de plano executadas pelo backup, os papeis se invertem de forma consistente no runtime: 'MDM_BK' passa a exibir 'UNIX MASTER' e 'MDM' (no local) exibe '*UNIX FTA'. Como o script SwitchPlan deve ser executado pelo no que o MODELO do banco considera domain manager, e esse modelo tambem passa a indicar o backup, runtime e modelo podem convergir para o backup como master. Consequencia pratica: comandos de link/unlink emitidos do no que deixou de ser domain manager retornam AWSBHU537E 'neither is the domain manager: This is not allowed'.",
 "result": "SUCCESS", "risk": "read_only",
 "platform": "Distributed; Linux x86_64; containers tws-hwa/tws-bmdm; HWA 10.2.8",
 "observed_at": "2026-09-10T15:38:00-03:00",
 "test_procedure": "Coletada a saida de 'conman sc @' em ambos os nos antes e depois das operacoes de plano, cruzando com 'composer display domain=@' (MASTERDM MANAGER MDM_BK) e com a execucao de link de um no que nao e mais domain manager.",
 "actual_output": "Tabela de CPUs comparada nos dois nos evidenciou que o '*' e o marcador de no local; a inversao de papeis MDM/MDM_BK e a mensagem AWSBHU537E ficaram registradas.",
 "synthetic_questions": [
   "O que significa o asterisco na coluna STATE do comando conman showcpus?",
   "O que significam as letras J, M, E, A na coluna STATE do conman showcpus?",
   "Por que MDM_BK aparece como UNIX MASTER e MDM como UNIX FTA apos um failover?",
   "O que significa AWSBHU537E ao tentar linkar uma workstation?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: conman showcpus / Domain Manager > Interface: CLI conman sc > Topico: monitoring > cpu_states [role_flip]]"
},
]

with open(out, "w", encoding="utf-8") as f:
    for e in ev:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")
print(f"Gravadas {len(ev)} evidencias em {out}")
