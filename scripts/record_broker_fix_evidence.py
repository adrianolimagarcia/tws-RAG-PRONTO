import json
base = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
out = f"{base}/data/evidence/lab-validation-2026-09-10-switchplan-broker-fix-verified.jsonl"
ev = {
 "claim_id": "hwa-lab-10.2.8-switchplan-broker-fix-verified-0014",
 "claim": "Corrigida e VERIFICADA a causa raiz do aborto do SwitchPlan no HWA 10.2.8 com Dynamic Workload Broker. A correcao (opcao a) edita o script SwitchPlan em duas partes: (1) substitui o 'conman stop ;progressive' por um laco que para apenas workstations que NAO sejam broker agent, iterando a lista de 'conman sc @' e filtrando nos em que a coluna NODE contem BROKER (awk com $2 numerico + NODE sem BROKER); (2) adiciona '|| true' ao 'conman stop $cpu' dentro do laco porque o SwitchPlan usa 'set -e' (linha 171) e o 'stop' do proprio master retorna rc=13, o que abortava o script antes da fase de switch. Resultado verificado: SwitchPlan executa o ciclo COMPLETO — rc=0, 'AWSBIS364I Running PostSwitchPlan' e 'AWSBIS361I Ending SwitchPlan', sem AWSBHU076E/AWSBCT041I; o plano gira (Run number avanca), 'planman ext' retorna AWSJCL062I SEM AWSJPL017E apos a troca, o horizonte do plano volta a ser real (ex.: end time 09/20/2026 21:04) e o broker MDM_DWB permanece intacto e linkado na malha. O patch foi aplicado em ambos os nos (MDM /opt/hwa/TWS/SwitchPlan e BMDM /opt/hwa/TWS/TWS/SwitchPlan) com backup do original em SwitchPlan.orig-20260910.",
 "result": "SUCCESS", "risk": "mutating",
 "platform": "Distributed; Linux x86_64; containers tws-hwa/tws-bmdm; HWA 10.2.8",
 "observed_at": "2026-09-11T12:01:00-03:00",
 "test_procedure": "Patchado o SwitchPlan (skip broker-agent no stop + '|| true' no laco por causa do set -e). Executado SwitchPlan no BMDM com saída completa capturada: rc=0 com AWSBIS360I->363I->375I->364I->376I (stopping)->start (AWSBHU507I)->AWSBIS364I PostSwitchPlan->AWSBIS361I Ending SwitchPlan. Verificado apos: conman status (Batchman LIVES), planman showinfo (horizonte 09/20/2026 21:04), planman ext (AWSJCL062I sem AWSJPL017E) e conman sc (MDM_DWB OTHR BROKER intacto). Reaplicado o patch no MDM.",
 "actual_output": "SwitchPlan completo limpo (rc=0, AWSBIS361I); plano com horizonte real; planman ext sem AWSJPL017E; broker preservado. Fechamento do incidente AWSJPL017E na raiz.",
 "synthetic_questions": [
   "Como corrigir definitivamente o SwitchPlan para nao abortar quando existe um Dynamic Workload Broker?",
   "Por que o SwitchPlan usa 'set -e' e como isso afeta o laco de stop das workstations?",
   "Qual a evidencia de que o SwitchPlan completou a troca de plano com sucesso?",
   "Apos a correcao, planman ext funciona imediatamente apos o SwitchPlan?",
   "O que significa AWSBIS361I Ending SwitchPlan?"
 ],
 "context_prefix": "[Escopo: HCL Workload Automation 10.2.8 (Distributed) > Componente: SwitchPlan / Dynamic Workload Broker > Interface: script SwitchPlan (patch) > Topico: troubleshooting > plan_recovery [broker_fix_verified]]"
}
with open(out, "w", encoding="utf-8") as f:
    f.write(json.dumps(ev, ensure_ascii=False) + "\n")
print("OK")