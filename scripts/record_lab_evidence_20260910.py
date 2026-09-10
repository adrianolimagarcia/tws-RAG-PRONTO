import json

base = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
out = f"{base}/data/evidence/lab-validation-2026-09-10-optman-users-calendar-planincident.jsonl"
today = "2026-09-10"

ev = [
{
 "claim_id": "hwa-lab-10.2.8-optman-global-options-vs-localopts-0001",
 "claim": "No laboratorio HWA 10.2.8 containerizado, 'optman ls' retorna 92 opcoes globais mantidas no banco, enquanto o arquivo localopts mantem apenas o escopo local do no. O localopts fica em /opt/hwa/TWSDATA/localopts no MDM e em /opt/hwa/TWS/TWSDATA/localopts no BMDM, cada um com thiscpu proprio. 'optman show <opcao>' expoe a descricao oficial e revela parâmetros de failover: enAutomaticFailover (af) e workstationMasterListInAutomaticFailover (wm). Quando a lista wm esta VAZIA, TODOS os backup masters tornam-se candidatos ao take-over automatico. Alteracoes via 'optman chg' tem efeito imediato para opcoes de runtime, mas enAutomaticFailover exige restart do Liberty para efetivar.",
 "result": "SUCCESS", "risk": "mutating",
 "platform": "Distributed; Linux x86_64; containers RHEL 9 UBI9; HWA 10.2.8",
 "observed_at": f"{today}T09:30:00-03:00",
 "test_procedure": "Executado 'optman ls' (92 opcoes) e 'optman show enAutomaticFailover/workstationMasterListInAutomaticFailover'. Inspecionados os localopts de tws-hwa e tws-bmdm. Testada alteracao a quente com 'optman chg companyName' e reversao.",
 "actual_output": "optman ls listou as opcoes globais do banco; show retornou descricao oficial; chg aplicou efeito imediato. Localopts confirmou caminhos distintos por no e thiscpu distinto (MDM vs MDM_BK).",
 "synthetic_questions": [
   "Qual a diferenca entre optman e o arquivo localopts no HWA?",
   "Onde fica o arquivo localopts no master domain manager e no backup master?",
   "O que acontece se workstationMasterListInAutomaticFailover estiver vazio?",
   "Quais opcoes globais do HWA controlam o failover automatico do domain manager?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Global Options (optman) e Local Options (localopts) > Interface: CLI optman / arquivo localopts > Topico: operations > configuration [optman_vs_localopts]]"
},
{
 "claim_id": "hwa-lab-10.2.8-composer-section-headers-inventory-no-users-object-0002",
 "claim": "No composer do HWA 10.2.8, os cabecalhos de secao validos sao $JOBS, $CALENDAR, $PARMS, $RESOURCE e $PROMPT; o job stream usa a keyword standalone 'SCHEDULE <nome>' (sem cifrao) e o usuario usa 'username <nome>' + 'password \"<pwd>\"' + 'end'. NAO existem $USER, $USERS, $LOGON, $PARAMETER, $WORKSTATION, $VARTABLE, $RUNCYCLEGROUP, $DOMAIN, $FOLDER ou $WSCLASS — todos retornam AWSBCZ021E 'A definition keyword was expected at this point'. Negative knowledge: nao existe objeto USER de modelagem com cabecalho $.",
 "result": "SUCCESS", "risk": "read_only",
 "platform": "Distributed; Linux x86_64; container tws-hwa; HWA 10.2.8",
 "observed_at": f"{today}T09:37:00-03:00",
 "test_procedure": "Sondagem sistematica de cabecalhos candidatos via composer add com arquivo minimo, classificando pelo codigo de erro (AWSBCZ021E = keyword invalida; AWSJOM915E/918E = cabecalho aceito com erro interno).",
 "actual_output": "Validos: $JOBS, $CALENDAR, $PARMS, $RESOURCE, $PROMPT + SCHEDULE/username standalone. Invalidos: os demais candidatos.",
 "synthetic_questions": [
   "Quais sao os cabecalhos de secao validos em um arquivo de definicao do composer HWA?",
   "Existe um objeto USER com cabecalho $USERS no composer?",
   "Como declarar um usuario em arquivo de definicao do composer?",
   "O que causa a mensagem AWSBCZ021E?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Composer (linguagem de definicao) > Interface: CLI composer add > Topico: model > syntax [section_headers]]"
},
{
 "claim_id": "hwa-lab-10.2.8-streamlogon-missing-os-user-and-conman-altjob-0003",
 "claim": "O composer do HWA 10.2.8 NAO valida na definicao se o usuario de STREAMLOGON existe no SO: o job e aceito e falha somente em runtime. Com usuario de SO inexistente o job vai para FAIL/ABEND e o log consolidado registra AWSBDW057E acompanhado de AWSBDW009E (falha ao recuperar a estrutura de senha do usuario de logon); o stdlist do job nao e gerado. Criado o usuario no SO, o mesmo job (definicao inalterada) conclui SUCC rc0. A mudanca do logon no plano usa 'conman altjob <job>;logon=<usuario>', que sobrescreve o STREAMLOGON sem tocar o composer; exige job em estado WAIT (em HOLD retorna AWSBHU085E).",
 "result": "SUCCESS", "risk": "guided_action",
 "platform": "Distributed; Linux x86_64; container tws-hwa; HWA 10.2.8",
 "observed_at": f"{today}T09:15:00-03:00",
 "test_procedure": "Criado job com STREAMLOGON para usuario de SO inexistente; composer aceitou. Submetido: FAIL/ABEND; log com AWSBDW057E+009E. Criado o usuario: mesmo job SUCC rc0. Testado 'conman altjob' em job WAIT (aceito) e HOLD (AWSBHU085E).",
 "actual_output": "Comportamento assimetrico comprovado: modelagem aceita logon inexistente, falha apenas em runtime; altjob altera o logon no plano.",
 "synthetic_questions": [
   "O composer valida se o usuario de STREAMLOGON existe no sistema operacional?",
   "O que significa AWSBDW057E no HWA?",
   "Como alterar o logon de um job ja no plano sem modificar a definicao?",
   "Em que estado um job precisa estar para aceitar conman altjob?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Job Logon / STREAMLOGON > Interface: CLI composer e conman altjob > Topico: security > job_logon [streamlogon]]"
},
{
 "claim_id": "hwa-lab-10.2.8-calendar-object-syntax-freedays-0004",
 "claim": "O objeto calendario do composer HWA 10.2.8 e declarado por '$calendar <NOME>' (nome limitado a 8 caracteres) seguido DIRETAMENTE das datas livres, uma por linha, no formato mm/dd/yy (ano com DOIS digitos) e SEM keyword prefixando as datas. Formas rejeitadas: 'HOLIDAYS <data>', 'FREEDAYS <data>', 'RUNCYCLE' e 'DESCRIPTION' como atributos do bloco, datas com ano de 4 digitos, e '$calendar <nome>' sem corpo. O calendario e consumido pela clausula 'FREEDAYS <CALENDARIO>' posicionada ANTES de 'ON RUNCYCLE' no job stream.",
 "result": "SUCCESS", "risk": "guided_action",
 "platform": "Distributed; Linux x86_64; container tws-hwa; HWA 10.2.8",
 "observed_at": f"{today}T09:39:00-03:00",
 "test_procedure": "Iteradas 7 variantes de bloco ate obter cal=LABCAL (AWSJCL003I). Validado o consumo com SCHEDULE MDM#JS_CAL_FREE com 'FREEDAYS LABCAL' antes de 'ON RUNCYCLE RC_UTEIS' (AWSJCL003I).",
 "actual_output": "'composer display cal=LABCAL' retornou as datas livres normalizadas (09/11/2026 12/25/2026 01/01/2027). O job stream com FREEDAYS validou e foi adicionado.",
 "synthetic_questions": [
   "Qual e a sintaxe exata para criar um objeto calendario no composer do HWA?",
   "Quantos caracteres pode ter o nome de um calendario?",
   "Como usar a clausula FREEDAYS em um job stream?",
   "Qual formato de data as datas livres do calendario aceitam?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Calendar Object (FREEDAYS) > Interface: CLI composer > Topico: scheduling > calendar [syntax]]"
},
{
 "claim_id": "hwa-lab-10.2.8-runcyclegroup-structure-and-fd-keywords-0005",
 "claim": "O bloco de run cycle group usa a keyword STANDALONE 'runcyclegroup <NOME>' (sem cifrao; '$runcyclegroup' retorna AWSBCZ021E) e exige um UNICO 'end' de fechamento (um segundo 'end' interno retorna AWSJOM915E). O run cycle inclusivo e declarado como 'on runcycle <NOME> \"<FREQ>\"' — 'on' sem 'runcycle' falha. As clausulas de compensacao FDNEXT, FDPREV e FDIGNORE sao keywords SEM ARGUMENTO ('FDNEXT 1' retorna AWSJOM918E). No SCHEDULE, nenhuma forma de referenciar o grupo foi aceita: 'ON RUNCYCLEGROUP <n>', 'RUN CYCLE GROUP <n>' e 'ON RUN CYCLEGROUP <n>' retornam AWSJOM915E.",
 "result": "PARTIAL", "risk": "guided_action",
 "platform": "Distributed; Linux x86_64; container tws-hwa; HWA 10.2.8",
 "observed_at": f"{today}T09:50:00-03:00",
 "test_procedure": "Criados rcg=LABRCG (fdprev) e rcg=LABRCG2 (fdnext) com AWSJCL003I. Sondadas tres formas de referencia no SCHEDULE, todas rejeitadas com AWSJOM915E. Efeito das datas avaliado com conman ss em MDM#JS_CAL_*.",
 "actual_output": "Definicao do grupo validada; referencia do grupo a partir de job stream permanece em aberto (limitacao de sintaxe documentada).",
 "synthetic_questions": [
   "Como declarar um run cycle group no composer do HWA?",
   "Quais clausulas compensam dias livres em um run cycle group?",
   "FDNEXT e FDPREV aceitam argumentos numericos?",
   "Por que '$runcyclegroup' retorna AWSBCZ021E?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Run Cycle Group > Interface: CLI composer > Topico: scheduling > calendar [free_day_compensation]]"
},
{
 "claim_id": "hwa-lab-10.2.8-incident-stuck-plan-rca-and-recovery-0006",
 "claim": "Incidente reproduzido: apos desligamento abrupto (SIGKILL) dos containers na janela de virada de plano, o plano de producao ficou STUCK. Sintomas: 'planman showinfo' com 'Production plan end time: (same as the start time of the last extension - created/extended with -for 0000)', horizonte ZERO ('Production plan time extention: 00:00'), Run number avancado de 31 para 33; 'planman ext' falhou com AWSJPL017E 'a previous action on the production plan did not complete successfully'. 'planman' num no cujo localopts thiscpu difere do domain manager no MODELO falha com AWSJPL004E. Recuperacao OK na ordem: (1) 'planman unlock' -> AWSJPL504I; (2) 'planman reset' (reset do preproduction, mantendo o plano corrente) -> AWSJCL064I; (3) 'planman crt -days 3' -> AWSJCL058I 'The production plan (Symnew) has been successfully created'; (4) SwitchPlan (comuta Symnew e reemite start do batchman); (5) 'planman ext -days 5' -> AWSJCL062I. Horizonte restaurado para 09/12/2026 21:04 com extensao 072:00.",
 "result": "SUCCESS", "risk": "mutating",
 "platform": "Distributed; Linux x86_64; containers tws-hwa/tws-bmdm; HWA 10.2.8",
 "observed_at": f"{today}T12:44:00-03:00",
 "test_procedure": "Diagnosticado com planman showinfo e planman ext (AWSJPL017E). Teste diferencial entre nos (ext OK no no dono do modelo, AWSJPL004E no outro). Executada a sequencia unlock -> reset -> crt -> SwitchPlan -> ext, verificando Run number, horizonte e batchman a cada etapa.",
 "actual_output": "Plano recuperado: end time 09/12/2026 21:04, extensao 072:00, Run number 34->35, Batchman LIVES, job streams escalonados apos a recuperacao.",
 "synthetic_questions": [
   "O que significa AWSJPL017E e como recuperar um plano de producao travado?",
   "O que indica end time igual ao inicio da ultima extensao no planman showinfo?",
   "Qual a sequencia planman para recuperar um plano corrompido apos queda abrupta do master?",
   "O que significa AWSJPL004E e como resolver a divergencia entre thiscpu e o domain manager?",
   "O que faz planman reset no preproduction plan e o que planman crt produz?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Production Plan / planner > Interface: CLI planman (unlock/reset/crt/ext) e SwitchPlan > Topico: troubleshooting > plan_recovery [stuck_plan]]"
},
{
 "claim_id": "hwa-lab-10.2.8-plan-model-divergence-switchmgr-and-switchplan-internals-0007",
 "claim": "'conman switchmgr' atua sobre o PLANO (runtime/Symphony) e pode divergir do MODELO no banco: apos failover e switchback, 'composer display domain=@' ainda exibia '*MANAGER MDM_BK' enquanto 'conman switchmgr MASTERDM;MDM' respondia AWSBHU118W 'MDM is already the manager'. O objeto DOMAIN do modelo nao e editavel para trocar manager: sem ISMASTER retorna AWSJDB313E 'A master domain cannot be modified to become a lower level domain'; com ISMASTER retorna AWSJCO025E 'It must be installed'. Comandos planman validam THISCPU contra o MODELO, nao contra o runtime. O script SwitchPlan executa: 'Batchman down', stop progressivo (agentes/pools/brokers retornam AWSBHU158E, X-agent AWSBHU058E), AWSBIS383I 'Symphony found, waiting 5 seconds', start do batchman (AWSBHU507I) e PostSwitchPlan (AWSBIS364I/361I).",
 "result": "SUCCESS", "risk": "mutating",
 "platform": "Distributed; Linux x86_64; containers tws-hwa/tws-bmdm; HWA 10.2.8",
 "observed_at": f"{today}T12:48:00-03:00",
 "test_procedure": "Comparado 'composer display domain=@' com 'conman switchmgr'. Testadas duas formas de edicao do DOMAIN. Executado SwitchPlan a partir do no autorizado pelo modelo, capturando o log interno.",
 "actual_output": "Divergencia modelo x plano comprovada; DOMAIN imutavel para troca de manager; log interno do SwitchPlan mapeado.",
 "synthetic_questions": [
   "O comando switchmgr altera o modelo do dominio ou apenas o plano?",
   "Por que o objeto DOMAIN pode mostrar um manager diferente do conman?",
   "O que significa AWSJDB313E ao modificar um DOMAIN?",
   "Quais etapas internas o SwitchPlan executa?",
   "O que significa AWSBHU158E durante a troca de plano?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: Domain Manager / SwitchPlan > Interface: conman switchmgr / composer domain / SwitchPlan > Topico: high_availability > model_plan_divergence [switchmgr]]"
},
{
 "claim_id": "hwa-lab-10.2.8-planner-warnings-variable-unresolved-and-ignore-attribute-0008",
 "claim": "Durante a criacao do plano no HWA 10.2.8, o planner emite avisos nao bloqueantes: AWSJPL523W 'The variable \"<NOME>\" was not found in the database and so could not be resolved' confirma que variavel inexistente (^VAR^) e reportada como AVISO, nao erro, na geracao do plano; o job segue com o token literal. AWSJPL208W 'not been added to the production plan because the workstation \"<Y>\" has the \"ignore\" attribute set' mostra que o atributo ignore da workstation exclui silenciosamente seus job streams. AWSJPL543I informa a quantidade de instancias processadas.",
 "result": "SUCCESS", "risk": "read_only",
 "platform": "Distributed; Linux x86_64; containers tws-hwa/tws-bmdm; HWA 10.2.8",
 "observed_at": f"{today}T12:46:00-03:00",
 "test_procedure": "Analisada a saida integral de 'planman crt -days 3' e 'planman ext', coletando os avisos AWSJPL emitidos.",
 "actual_output": "AWSJPL523W e AWSJPL208W capturados textualmente na saida do planner, correlacionando com as definicoes do lab.",
 "synthetic_questions": [
   "O que acontece se um job referenciar uma variavel inexistente ao gerar o plano?",
   "O que significa AWSJPL523W?",
   "Por que um job stream nao e incluido no plano mesmo estando definido?",
   "O que e o atributo ignore de uma workstation?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: planner / MakePlan > Interface: CLI planman crt/ext > Topico: troubleshooting > planner [warnings]]"
},
]

with open(out, "w", encoding="utf-8") as f:
    for e in ev:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")
print(f"Gravadas {len(ev)} evidencias em {out}")