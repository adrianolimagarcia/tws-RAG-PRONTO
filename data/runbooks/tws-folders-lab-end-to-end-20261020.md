# Runbook: folders HWA 10.2.8 — validação ponta a ponta (20/10/2026)

## Escopo e ambiente
- Host: `cachyos-x8664` (disco sdb1), projeto `projetos/tws-RAG-PRONTO`
- MDM: container `tws-hwa`, usuário aplicativo `wauser`; TWS/HWA 10.2.8.0.
- Somente laboratório. Nenhum job foi submetido ao plano; job stream foi definido como `DRAFT`.
- Testes de banco com `composer`. Não confundir definição no banco com instância ativa no plano `conman`.

## Objetos de teste criados
- Folder pai: `/LAB_FOLDERS_20261020/`
- Subfolder: `/LAB_FOLDERS_20261020/QA/`
- Job: `MDM_DWB#/LAB_FOLDERS_20261020/QA/JOB_FOLDER_SMOKE`
- Job stream: `MDM_DWB#/LAB_FOLDERS_20261020/QA/JS_FOLDER_SMOKE`
- Job executaria `/bin/true` como `wauser`, mas **não foi executado**.
- Job stream tem `DRAFT` e `ON EVERYDAY` na definição; DRAFT foi confirmado na leitura.

## Pré-check
```sh
docker ps --format '{{.Names}} {{.Status}}'
docker exec -u wauser tws-hwa bash -lc 'printf "listfolder /@\nexit\n" | composer'
```
Resultado inicial: lista com raiz `/` somente (1 objeto); processos `netman`, `batchman` e `writer` ativos.

## Criação da hierarquia
Arquivo `/tmp/tws-folder-lab-20261020.def` **dentro do container**:
```text
FOLDER /LAB_FOLDERS_20261020
END
FOLDER /LAB_FOLDERS_20261020/QA
END
```
Execução:
```text
composer> add /tmp/tws-folder-lab-20261020.def
```
**Evidência:** AWSJCL003I para os dois objetos; AWSBIA090I errors 0 warnings 0; AWSBIA288I Total objects updated: 2.

## Definição do job
Arquivo separado `/tmp/tws-folder-lab-jobs-20261020.def`:
```text
$JOBS
MDM_DWB#/LAB_FOLDERS_20261020/QA/JOB_FOLDER_SMOKE
  DOCOMMAND "/bin/true"
  STREAMLOGON wauser
  TASKTYPE UNIX
  RECOVERY STOP
```
**Evidência:** AWSJCL003I `jd=MDM_DWB#/LAB_FOLDERS_20261020/QA/JOB_FOLDER_SMOKE`; 1 objeto atualizado; 0 errors/warnings.

## Definição do job stream (schedule)
Arquivo separado `/tmp/tws-folder-lab-stream-20261020.def`:
```text
SCHEDULE MDM_DWB#/LAB_FOLDERS_20261020/QA/JS_FOLDER_SMOKE
DESCRIPTION "Folder structure validation - no automatic execution"
DRAFT
ON EVERYDAY
:
MDM_DWB#/LAB_FOLDERS_20261020/QA/JOB_FOLDER_SMOKE
END
```
**Evidência:** AWSJCL003I `js=MDM_DWB#/LAB_FOLDERS_20261020/QA/JS_FOLDER_SMOKE`; 1 objeto atualizado; 0 errors/warnings.

## Consultas confirmadas (somente leitura)
```text
listfolder /@
display jd=MDM_DWB#/LAB_FOLDERS_20261020/QA/JOB_FOLDER_SMOKE
display sched=MDM_DWB#/LAB_FOLDERS_20261020/QA/JS_FOLDER_SMOKE
```
- `listfolder /@` retornou `/`, `/LAB_FOLDERS_20261020/`, `/LAB_FOLDERS_20261020/QA/` (3 objetos).
- `display jd` mostrou `DOCOMMAND "/bin/true"`, `STREAMLOGON wauser`, `TASKTYPE UNIX`, `RECOVERY STOP`.
- `display sched` mostrou `DRAFT`, runcycle diário e vínculo com o job do mesmo subfolder.

## Erros e descobertas de parser/retrieval
1. Arquivo de jobs sem `$JOBS` → `AWSBCZ021E A definition keyword was expected`; 0 objetos alterados.
2. Misturar job e `SCHEDULE` no mesmo arquivo do tipo `$JOBS` → `AWSJOM915E unexpected token SCHEDULE`; 0 objetos alterados.
3. Após `chfolder /LAB_FOLDERS_20261020/QA`, as consultas `display jd=MDM_DWB#JOB_FOLDER_SMOKE` e `display sched=MDM_DWB#JS_FOLDER_SMOKE` retornaram `AWSJCL017W` (nenhum objeto). Consultas qualificadas com caminho completo funcionaram. **Não assumir que chfolder automaticamente reescreva todos os seletores `display`.**
4. Os exemplos de caminho entre workstation e objeto dependem da sintaxe e categoria do objeto. O formato confirmado para este lab é `MDM_DWB#/LAB_FOLDERS_20261020/QA/OBJETO`; colocar o folder antes do nome da workstation no cabeçalho do job falhou no parser.
5. Pastas e workstations são entidades distintas. A workstation observada para este teste é `MDM_DWB`.

## Segurança/limites
- Não executar `rmfolder` sem alvo: manual avisa que pode excluir toda hierarquia vazia.
- `rmfolder` só deve excluir árvores sem objetos de scheduling; **não testado destrutivamente**.
- A função de renomear e as permissões foram inspecionadas na man page, **não testadas em mutação**.
- A existência de definição `DRAFT` não prova submissão/execução via conman; nenhuma execução foi feita.
- Diretório temporário do container pode ser removido posteriormente; objetos do banco foram **mantidos no laboratório** para reconsulta. Limpeza exige autorização e sequência de remoção dos objetos antes dos folders.

## Evidência e manual de referência
`/opt/hwa/TWS/man/composer/cat1/{add,mkfolder,listfolder,chfolder,renamefolder,rmfolder,display}.1`
`/opt/hwa/TWS/templates/{folder,job,jobstream}.template`
Comandos executados de dentro do container via `docker exec -u wauser ... bash -lc`, sem alterar o sistema operacional do host.

## Teste adicional: escopo de listfolder
Consultas no mesmo composer:
- `listfolder /LAB_FOLDERS_20261020`: retornou **somente** `/LAB_FOLDERS_20261020/` (1 objeto), sem QA.
- `listfolder /LAB_FOLDERS_20261020/@`: retornou pai e QA (2 objetos).
- Após `chfolder /LAB_FOLDERS_20261020/QA`, `listfolder /@` retornou raiz e toda árvore (3 objetos): caminho absoluto não fica limitado ao folder atual.
**Regra:** para recuperar uma subárvore inteira, especificar `/@` no caminho. Não generalizar automaticamente listagem simples como recursiva.

## Segunda rodada: submissão real em conman, 20/10/2026 11:51–11:56 -03

### Teste negativo — DRAFT
- `sbs MDM_DWB#/LAB_FOLDERS_20261020/QA/JS_FOLDER_SMOKE;noask`
- Retorno `AWSBHU614E`: nenhum job stream enviado a batchman; documentação cita workstation ignorada ou stream em `DRAFT`.
- `ss` e `sj` pelo identificador simples imediatamente após retornaram `AWSBHU072E`, nenhum objeto encontrado.

### Teste negativo — workstation broker
- Atualização explícita somente de `JS_FOLDER_SMOKE`: retirado `DRAFT` via composer add e confirmação de substituição, 0 erros.
- `sbs MDM_DWB#/LAB_FOLDERS_20261020/QA/JS_FOLDER_SMOKE;noask` retornou instância `(0AAAAAAAAAAAABPZ)`.
- Logs `20261020_TWSMERGE.log`, 11:51:58–11:51:59: transições READY → EXEC → ABEND; `AWKJDE180E` / `AWKSED102E`: broker procurou definição `/bin/true` no banco. Não houve execução UNIX com sucesso.
- `composer display ws=MDM_DWB` confirmou `TYPE BROKER`, `OS OTHER`. **Não usar como workstation de execução de DOCOMMAND UNIX**.

### Teste positivo — job UNIX isolado
- `composer display ws=MDM`: `TYPE MANAGER`, `OS UNIX`.
- Criado `MDM#/LAB_FOLDERS_20261020/QA/JOB_FOLDER_UNIX`, `DOCOMMAND "/bin/true"`, `STREAMLOGON wauser`, `TASKTYPE UNIX`.
- `sbj MDM#/LAB_FOLDERS_20261020/QA/JOB_FOLDER_UNIX;alias=FOLDER_UNIX_ONCE;noask`: submissão para `MDM#JOBS.FOLDER_UNIX_ONCE`.
- `sj MDM#JOBS.FOLDER_UNIX_ONCE;std`: `Job Number: 446863`, `Exit Status: 0`, 11:54:43 -03.
- `ss MDM#JOBS;showid`: `SUCC`, 1 job, 1 OK.
- **Nuance fundamental:** sem `into=`, a execução isolada usa job stream `JOBS` na raiz, apesar de a definição estar em `QA`. Manual `submit.1` confirma essa transformação do contexto de folder em plano.

### Teste positivo — job stream completo no folder
- Criado `MDM#/LAB_FOLDERS_20261020/QA/JS_FOLDER_UNIX` inicialmente com `DRAFT`; atualizado somente esse stream para retirar `DRAFT`.
- `sbs MDM#/LAB_FOLDERS_20261020/QA/JS_FOLDER_UNIX;noask` submetido como instância `(0AAAAAAAAAAAABP2)`.
- `ss /@/@;showid`: listou `/LAB_FOLDERS_20261020/QA/`, `MDM#JS_FOLDER_UNIX`, `SUCC`, 1 job, 1 OK.
- `sj /@/@.@`: `JOB_FOLDER_UNIX` status `SUCC`, Job Number `447121` às 11:55:47 -03.
- Log `20261020_TWSMERGE.log`: JOBMAN lançou `MDM#/LAB_FOLDERS_20261020/QA/JS_FOLDER_UNIX...JOB_FOLDER_UNIX`, completou `SUCCESSFULLY`; stream mudou para `SUCC`.
- **Atenção:** na consulta `ss`, o output pode mostrar um cabeçalho de folder `>> /LAB_FOLDERS_20261020/QA/` separado da linha da workstation; um parser RAG/agente deve manter esse contexto ao interpretar as linhas seguintes.

### Contraste de namespaces
- `composer` consulta **definições no banco**; `conman` consulta **instâncias no plano**.
- `conman listfolder /@` retornou `/` e `/LAB_FOLDERS_20261020/QA/`, condizente com folders com instâncias no plano; não equivale necessariamente à árvore de todas as definições em composer.
- Consultas com caminho incompleto podem produzir `AWSBHU072E` apesar da submissão; a busca ampla `ss /@/@;showid` e `sj /@/@.@` foi confirmada.
- `DRAFT` evita a submissão via `sbs` no lab; remover `DRAFT` exige alteração explícita e controlada da definição.

### Estado deixado no lab
Os dois job streams de teste foram atualizados para **sem DRAFT** e não foram excluídos. Como possuem `ON EVERYDAY`, recomenda-se recolocá-los em `DRAFT` ao concluir testes, para evitar inclusão futura pelo plano automático. As execuções já observadas permanecem como evidência no plano/logs.


## Encerramento seguro e publicação dos dados (20/10/2026)
- Restaurado `DRAFT` em `MDM_DWB#/LAB_FOLDERS_20261020/QA/JS_FOLDER_SMOKE` e `MDM#/LAB_FOLDERS_20261020/QA/JS_FOLDER_UNIX` via composer `add`; confirmação `AWSJCL003I`, 0 erros.
- Reconsulta `composer display sched` das duas definições confirmou `DRAFT`. Instâncias históricas de plano/log não foram apagadas.
- Evidência persistida: `data/evidence/lab-validation-2026-10-20-folders-execution.jsonl` (5 claims).
- `scripts/consolidate_corpus.py` concluído: 7.494 → 7.499 claims sem perda. **O índice denso gerado antes desta rodada tem 7.494 documentos e precisa de reconstrução para refletir as novas cinco claims.** Não tratar busca densa como atualizada até essa etapa.
- As execuções bem-sucedidas são evidência de laboratório e não validam automaticamente todos os tipos de workstation, condições de acesso ou sintaxes de seleção.
