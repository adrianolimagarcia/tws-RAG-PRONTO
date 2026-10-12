# File monitor — job que aguarda criação de arquivo (lab 10.2.8)

Data: 2026-10-12. Lab: tws-hwa (MDM) 10.2.8.0. Fase 1, variação de job.

## Conceito

Não existe "job type filemon" no composer — usa-se o utilitário `filemonitor`
dentro de um job UNIX comum:

```
MDM#LAB_JOB_FILEMON
 DOCOMMAND "export LD_LIBRARY_PATH=/opt/hwa/TWS/bin:/opt/hwa/TWS/ITA/cpa/ita/lib && cd /tmp/fmrepo && /opt/hwa/TWS/bin/filemonitor -path /tmp/lab_trigger.txt -event fileCreated -timeout 120"
 STREAMLOGON wauser
 DESCRIPTION "Job file monitor - fase 1 variacao"
 TASKTYPE UNIX
 RECOVERY STOP
```

Parâmetros principais do `filemonitor`:
- `-path`: arquivo/diretório monitorado
- `-event fileCreated | fileModified`: tipo do evento
- `-timeout segundos`: tempo máximo de espera
- `-scanInterval`, `-minFileSize`: ajustes finos

## Resultado do teste

- Job ficou em EXEC monitorando por 120s
- Exit Status 4 = timeout sem detectar o evento
- Comportamento esperado: SUCC quando o arquivo é criado dentro do timeout

## Pegadinhas encontradas (importante)

| Problema | Causa | Solução |
|----------|-------|---------|
| `filemonitor: command not found` | Não está no PATH do job | Caminho absoluto `/opt/hwa/TWS/bin/filemonitor` |
| `libapr-1.so.0: cannot open` | Falta LD_LIBRARY_PATH | Exportar `/opt/hwa/TWS/bin:/opt/hwa/TWS/ITA/cpa/ita/lib` |
| `libjobManagerCore.so: cannot open` | Idem | Idem (mesmo export resolve) |
| `Cannot create ../stdlist/filemonitor: Permission denied` | filemonitor escreve estado no cwd | `cd` para diretório gravável antes de rodar |

## Limpeza

```bash
conman "cancel LAB_JS_FILEMON"              # confirma y (várias instâncias)
echo y | composer "delete js=LAB_JS_FILEMON"
echo y | composer "delete job=MDM#LAB_JOB_FILEMON"
rm -f /tmp/lab_trigger.txt; rm -rf /tmp/fmrepo
```

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|---------------|------|
| Exit 4 | Timeout sem evento | Normal se o arquivo não chegou; aumentar timeout |
| Exit 127 | Biblioteca/PATH | Ver tabela de pegadinhas acima |
| Evento não detectado | Arquivo já existia antes do monitor iniciar | Apagar o trigger antes do submit |
