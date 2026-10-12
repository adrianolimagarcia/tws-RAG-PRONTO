# DWC 10.2.8 — validacao via browser (roteiro + equivalencias CLI ja testadas)

Data: 2026-10-12. Fase 2, item 2.3 do PLANO_FECHAMENTO_LACUNAS.
Status: **PENDENTE DE DWC** — roteiro pronto para executar assim que o DWC
estiver no ar (ver `hwa-10.2.8-dwc-deploy.md`). As operacoes equivalentes via
CLI ja foram validadas no lab na Fase 1 (referencias abaixo).

## Pre-requisito

DWC acessivel em `https://<host>:9443/ibm/console`, logado como wauser,
com conexao ao engine `tws-hwa:31116` configurada.

## Roteiro de validacao web

### 1. Monitorar o plano
- DWC: Workload Monitoring -> Monitor Workload -> selecionar engine tws-hwa
- Verificar: job streams do dia com estado (SUCC/HOLD/READY), drill-down nos jobs
- CLI equivalente (Fase 1, validado): `conman "ss"` e `conman "sj <stream>"`

### 2. Submeter job ad-hoc
- DWC: Workload Submission -> Submit Ad Hoc -> escolher job definition
  (ex: `MDM#LAB_UNIX_BASICO`, mantido como referencia no banco) -> Submit
- Verificar: instancia aparece no plano e executa ate SUCC
- CLI equivalente (Fase 1 item 1.2, validado): `conman "sbs LAB_JS_BASICO"`

### 3. Responder a prompt via web
- DWC: na lista de jobs, job em espera de prompt mostra acao "Reply" ->
  responder Yes/No
- CLI equivalente (Fase 1 item 1.1, validado e documentado): a recomendacao
  para prompts orfaos e `conman "cancel <stream>"` em vez de responder,
  para nao executar job de teste sem valor. Via DWC a mesma decisao se aplica:
  so responda o prompt se a execucao do job ainda fizer sentido.

### 4. Consultar stdlist (saida do job)
- DWC: detalhe do job -> aba "Output" / job log
- CLI equivalente (Fase 1 item 1.2, validado):
  `conman "sj LAB_JS_BASICO;stdlist"`

## Criterios de aceite

| # | Checagem | Esperado |
|---|----------|----------|
| 1 | Login no DWC | 200, dashboard carrega |
| 2 | Conexao ao engine | tws-hwa:31116 "Connected" |
| 3 | Plano visivel | streams do dia listados |
| 4 | Submit ad-hoc | instancia executa ate SUCC |
| 5 | stdlist visivel | saida do job legivel no browser |

## Observacao sobre automacao

Validacao web real pode ser feita com browser automatizado (playwright/selenium)
contra `https://<host>:9443/ibm/console` apos o deploy. Nao executada nesta
fase por falta do DWC no lab.
