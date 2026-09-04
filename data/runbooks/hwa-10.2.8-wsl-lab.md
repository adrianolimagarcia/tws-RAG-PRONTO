# HWA 10.2.8 MDM Lab Runbook

Status: executed in WSL2 Ubuntu 22.04 on 2026-08-17.

This is a laboratory procedure, not a production installation guide. Do not
reuse the laboratory password or self-signed certificates in a real environment.

## Tested Components

- HCL Workload Automation MDM 10.2.8.00 Linux x86_64.
- PostgreSQL 18.6 from the PostgreSQL Global Development Group repository.
- Open Liberty 26.0.0.3.
- System Java 21.0.11 from Ubuntu 22.04 updates.
- HWA embedded Java 21.0.11 IBM Semeru OpenJ9, used by the installed HWA
  processes.
- Installation directory: `/opt/hwa`.
- Liberty directory: `/opt/liberty/wlp`.
- Operating-system installation user: `wauser`.
- Recommended identification convention: use the base workstation name with
  an incremental suffix for a dynamic agent on the same host, for example
  `MDM` and `MDM_1`.
- Database: `TWS`, local PostgreSQL on port 5432.

## Procedure

1. Extract the HWA image and verify `buildinfo.properties` before installing.
2. Install PostgreSQL and start the local cluster.
3. Install Java 21 and download Open Liberty 26.0.0.3 from IBM's public
   distribution site. The HWA image reported minimum Liberty version
   `26.0.0.3`. The downloaded Liberty archive SHA-256 was
   `bf394f83897a5aa4d0564604637e934c8f64b9fcb06a8dfcec2a49feed951778`.
4. Create an operating-system account for the HWA installation user.
5. Generate lab-only CA/server certificates and pass their directory with
   `--sslkeysfolder` and `--sslpassword`. HWA 10.2.8 rejected installation
   without both SSL parameters.
6. Run `configureDb.sh` with `POSTGRESQL`, `MDM`, database host, port, admin
   credentials and the HWA database user. The command created and populated
   the HWA schemas successfully.
7. Run `serverinst.sh` with `--inst_dir /opt/hwa`, `--wlpdir /opt/liberty/wlp`,
   `--componenttype MDM`, PostgreSQL parameters, SSL parameters and distinct
   values for `--thiscpu` and `--displayname` in this specific `-agent both`
   laboratory invocation, because the nested `twsinst` rejected equal values.
8. If Liberty files were extracted as root, ensure the Liberty tree is readable
   and executable by the HWA installation user. The installer specifically
   failed when `wlp/lib/versions` was not accessible.
9. Run `JnextPlan -for 0000` after installation. It created the preproduction
   plan, production plan and `Symphony` in this lab.
10. Validate with `conman showcpus`, `conman status`, `planman showinfo`,
    `composer version` and a database schema query.
11. Source `/opt/hwa/TWS/tws_env.sh` from the installation user's login profile.
    The HWA 10.2.8 image provides `tws_env.sh`; it does not provide a separate
    `twa_env.sh` file in this installation.

## Observed Results

- `configureDb.sh` completed successfully.
- `serverinst.sh` completed after correcting Liberty permissions, distinct
  workstation/display names, and supplying certificates.
- `conman showcpus` reported `Batchman LIVES` for MDM.
- The database contained HWA schemas including `mdl`, `dwb`, `evt`, `log` and
  `pln` with scheduling tables.
- `JnextPlan -for 0000` completed and loaded the Symphony file into the database.
- The installer/post-configure log showed `composer add Sfinal` completing with
  zero errors and eight objects updated: six jobs and the `FINAL` and
  `FINALPOSTREPORTS` job streams on `MDMXA`.
- `JnextPlan -for 2400` then produced two planned streams with three jobs each;
  the jobs were visible in `conman showjobs` in `HOLD` at their scheduled time.
- A login shell for `wauser` loaded `tws_env.sh` from `/home/wauser/.profile`.
  The validated environment included `TWS_TISDIR`, `TISDIR`, `UNISONHOME`,
  `UNISONWORK`, `JAVA_HOME`, `PATH` and `LD_LIBRARY_PATH`.

## Known Lab Limitations

- WSL does not provide a normal systemd service lifecycle by default; PostgreSQL
  was started explicitly with `pg_ctlcluster`.
- The generated certificates are self-signed and have a laboratory CN.
- Open Liberty was downloaded from
  `https://public.dhe.ibm.com/ibmdl/export/pub/software/openliberty/runtime/release/26.0.0.3/openliberty-26.0.0.3.zip`
  and extracted to `/opt/liberty/wlp`. Its top-level ownership remained root,
  so the Liberty tree was made readable/executable for HWA.
- The system Java is HotSpot, but HWA used its embedded IBM Semeru OpenJ9
  runtime at `/opt/hwa/TWS/JavaExt/jre/jre/bin/java`; these are distinct facts.
- The PostgreSQL 18 choice was the newest package available from PGDG during
  the run. Production compatibility must be confirmed against the target HWA
  software requirements report.
- The first job definition test still needs to be executed through a clean
  Composer input file; PowerShell quoting corrupted the first shell attempt.

### P27 — PRIORITY não é keyword válida em $JOBS (2026-08-22)

**Descoberta**: durante a validação prática no TWS 10.2.8, o comando `composer validate` rejeitou `PRIORITY n` em definições `$JOBS` com erro `AWSJOM915E` em **todas as posições testadas** (4 combinações: PRIORITY 10/HI/99 antes/depois de RECOVERY STOP).

**Fonte oficial HCL** (awsrgjobdefn.html): `PRIORITY` NÃO está na lista de keywords válidas de `$JOBS`. Keywords válidas: `scriptname`, `streamlogon`, `docommand`, `task`, `description`, `tasktype`, `interactive`, `succoutputcond`, `outputcond`, `recovery`.

**Advertência crítica**: "Wrongly typed keywords used in job definitions lead to truncated job definitions stored in the database. The wrong keyword is considered extraneous to the job definition and so it is interpreted as the job name of an additional job definition." — ou seja, usar PRIORITY em $JOBS não causa só erro, pode **corromper silenciosamente** a definição no banco.

**Onde PRIORITY funciona (válido)**:
1. `$SCHEDULES` — no schedule (stream level) e no job dentro da schedule
2. `sbd "cmd";alias=JOB;priority=10` e `sbj = STREAM;alias=STREAM_001;priority=HI`
3. `chgjob WS#STREAM.JOB;priority=30`

**Correção aplicada**:
- Synthetic chunks 2372 (PT) e 2373 (EN) no corpus — abordagem contrastiva (certo × errado)
- Claim `hwa-10.2.8-composer-priority-in-jobs-0124` — verified/high com lab_validation de 6 comandos
- 8 SFT records (4 PT + 4 EN) em approved/candidates/train/eval_independent
- Evidência em `evidence/lab-validation-2026-08-22-job-creation-gaps.jsonl` (6 registros)

## P28 — Dependencies em job streams: OPENS/PROMPT/VARTABLE (2026-08-22)

**Testes executados no TWS 10.2.8** (baseados somente no dataset) e lacunas encontradas:

### Lacunas confirmadas em laboratório (claims 0125-0129)

| # | Lacuna | Erro no lab | Correção |
|---|---|---|---|
| 1 | `OPENS` exige workstation qualificada na prática | `AWSJOM115E` | `OPENS MDMDA#arquivo` (não só `OPENS "arquivo"`) |
| 2 | Nome de PROMPT limitado a 8 bytes | `AWSJOM012E` | Nomes curtos (ex.: `PROMPT1`, `PRMT3`) |
| 3 | PROMPT referenciada precisa existir no banco | `AWSJDB311E` | Definir com `$PROMPT PROMPT1 "texto?"` antes |
| 4 | VARTABLE referenciada precisa existir no banco | `AWSJDB322E` | Definir com `$VARTABLE` antes |
| 5 | Ordem de keywords no job statement importa | `AWSJOM915E` | Ordem: follows → needs → opens → priority → prompt → nop |

### Sintaxe oficial confirmada (fontes HCL 10.2.8)
- **Prompt definition**: `$prompt[folder/]promptname "[: | !]text?"` — **sem DESCRIPTION** (o dataset não ensinava isso)
- **Vartable definition**: `vartable [folder/]table_name [description "desc"] members variablename "value" end`
- **Job stream keywords**: ordem canônica follows → needs → opens → priority → prompt → nop (nível stream: ... → onoverlap)
- Fonte: `awsrgjsdefn.html`, `awsrgpromptdefn.html`, `awsrgvartable.html`

### ocli (Orchestration CLI) — observação
- `ocli` 2.1.6.0 falhava com `AWSMRC019E` com host/port corretos e contextroot `/twsd` — **RESOLVIDO na P29** (contextroot correto é `/,/twsd/cli` + API key)
- O engine server exige **API Key** (`twsd/api/v2/apikey` no server.xml) — **setup completo concluído na P29** (senha `{aes}` decriptada → `padrao`, JWT gerado, `connection.jwt` no config.yaml, job `OCLI_TESTE_05` criado via ocli)
- **Não bloqueia mais a validação** — ocli validado de ponta a ponta (ver P29)

### Correção aplicada
- Chunks sintéticos 2374 (PT) + 2375 (EN) — regras práticas de dependencies por contraste
- Claims 0125-0129 registradas (verified/high/official_lab)
- 10 SFT records (5 PT + 5 EN) em approved/candidates/train/eval_independent
- Evidência: `evidence/lab-validation-2026-08-22-job-creation-gaps.jsonl` (+5 registros)

## P29 — Lacuna `into=` multi-instância + API key do ocli validada (2026-08-22)

### Lacuna `into=` — submissão ad-hoc para job stream com múltiplas instâncias (claim 0130)

**Descoberta**: ao submeter job ad hoc com `sbd ...;into=JOBS`, se existir **mais de uma instância** da job stream no plano (ex.: JOBS com instâncias de dias diferentes, ou instâncias ABEND de dias anteriores), o comando falha com `AWSBHU152E` "There is more than one job stream instance with the given name".

**Solução oficial** (awsrgsubmitjob.html) — duas formas de qualificar a instância:
1. `into=STREAM([hhmm[date]])` — ex.: `into=JOBS(0300)` ou `into=JOBS(0300 08/22)` — **recomendada** (resolve a ambiguidade sozinha)
2. `into=jobstream_id;schedid` — separador **`;`** (não `#`)

**Testes no lab** (evidência records 25-27):
| Comando | Resultado |
|---|---|
| `sbd ...;into=JOBS` (2 instâncias) | ❌ AWSBHU152E |
| `sbd ...;into=JOBS#CF26233AAAAAAAAA` (ID com `#`) | ❌ AWSBHU025E (sintaxe inválida) |
| `sbd ...;schedtime=0300` (keyword separada) | ❌ AWSBHU152E persiste — `schedtime=` não é keyword de `sbd` (é de `sbs`) |
| `sbd ...;into=JOBS(0300 08/22)` | ✅ SUCC |
| `sbd ...;into=JOBS(0300)` (só hora) | ✅ SUCC |

**Correção aplicada**: chunks sintéticos 2376 (PT) + 2377 (EN) (`conman-into-instance`), claim `-0130` (verified/high/official_lab), 2 SFT records (PT+EN), propagação completa nos splits do corpus.

### Claims 0131-0133 — fechamento de rastreabilidade (P29)

| Claim | Lacuna/validação | Chunks | SFT |
|---|---|---|---|
| `-0131` (at= nextday) | `at=HHMM` agenda para próxima ocorrência válida; pode cair no dia seguinte | 2378/2379 | ✅ 2 records |
| `-0132` (until/deadline) | `until=` limita execução; `deadline=` tem carryforward (nota `<data>`) | 2380/2381 | ✅ 2 records |
| `-0133` (runcycle weekly/every) | Validação positiva — dataset correto | 2382/2383 | ✅ 2 records |
| `-0134` (follows-hold) | Validação positiva — `follows` coloca job em HOLD até dependência | — | — (claim + evidência) |

### 🔑 API key do ocli — validação de ponta a ponta (SUCESSO)

**Contexto**: a P28 registrou que o `ocli` falhava com `AWSMRC019E` e que o setup de autenticação estava pendente. **Isso foi resolvido** — o ocli agora funciona de ponta a ponta.

**Jornada da senha `{aes}` decriptada**:
- Senha alvo em `wauser_variables.xml` (`{aes}ARCdAmMKFEMmI5XN...`), chave `wlp.password.encryption.key=1786984332` em `passphrase_variables.xml`
- `securityUtility` do Liberty só faz `encode` (sem decode)
- Mini-programa Java `DecryptAES.java` + inspeção de bytecode do `AESKeyManager` revelou: `decipher(byte[], String)` recebe o **algoritmo** ("aes"), não a chave; a chave vem de um `KeyStringResolver` (SPI) registrável via `setKeyStringResolver()` (método público estático)
- Resolver customizado retornando `1786984332` → `decipher(data, "aes")` → **`padrao`** 🎉

**API key criada via REST**:
| Passo | Resultado |
|---|---|
| `GET /twsd/api/v2/apikey` com `wauser:padrao` | ✅ 200 `{"count":0}` |
| Sem auth (controle) | ✅ 401 |
| `POST /twsd/api/v2/apikey` `{"type":"PERSONAL","label":"ocli-lab"}` | ✅ **201** — JWT RS256 |

**Configuração do ocli**:
- Config em `/home/wauser/.OCLI/config.yaml` — campo `connection.jwt`
- **Contextroot**: `/,/twsd/cli` (default documentado) — o `contextroot: /twsd` sozinho causava AWSMRC019E (EOF)
- Workstations reais: `MDM` (UNIX MASTER), `MDMDA` (UNIX AGENT), `MDMXA`, `MASTERAGENTS`, `MDM_DWB` — o default `TEST_AGENT` do config.yaml não existe (AWSJCO032E)
- `ocli model new job` abre editor Vim com template schedlang; usado `EDITOR=/tmp/ocli_editor.sh` (editor fake) para automatizar

**🎉 Job criado via ocli**:
```
AWSMRP001I You have successfully run the command "new" on the item "/MDM#/OCLI_TESTE_05".
errors 0, warnings 0. Total items updated: 1
```
Confirmado no banco via composer: `MDM#OCLI_TESTE_05` existe, criado em 08/22/2026. **A API key funciona de ponta a ponta.**

### Correção aplicada (P29)
- Chunks sintéticos 2378-2383 (0131/0132/0133, PT+EN) + propagação completa
- Claims 0131-0134 registradas (verified/high/official_lab); claims.jsonl 956 → **957**
- 6 SFT records (2 por claim 0131/0132/0133) em approved/candidates + splits regenerados (train 9598 / val 2438 / test 1147) + eval_independent 3190
- Evidência: `evidence/lab-validation-2026-08-22-job-creation-gaps.jsonl` (records 19-27, IDs alinhados)

### Correção do candidates.jsonl — review_status alinhado (P29)
- **Problema**: 18 records em `candidates.jsonl` tinham `review_status: "approved"` (duplicatas de promoção adicionadas com status errado), fazendo `validate_sft.py` reportar 18 avisos "review_status deve ser candidate" (exit 1)
- **Raiz**: o padrão correto é candidates.jsonl manter histórico com status `candidate`; approved.jsonl tem as cópias aprovadas. Os 18 records (0125-0133) foram adicionados direto com status `approved`
- **Correção**: `review_status` dos 18 records alterado de `approved` → `candidate` (mantendo `reviewed_at`/`review_batch` como metadados). Backup: `candidates.jsonl.bak-20260822-statusfix`
- **Resultado**: `validate_sft.py` (candidates) **PASS exit 0** (2421 candidatos, 0 avisos); `validate_sft.py` (approved) PASS exit 0 (13183); `validate_evidence.py` PASS exit 0 (957); `audit_dataset.py` PASS exit 0

## P30 — Expansão sintética v2-001: 618 candidatos novos (2026-08-22)

### Contexto
Batch `hwa-synthetic-expansion-v2-001` adicionou **618 records** em `candidates.jsonl` (linhas 2422-3039), cobrindo 37 claims-alvo (`target_claims_p30.jsonl` / `target_claims_p30b.jsonl`): incident checksync/conwinlog/evtsize/fab164e, dwc-eventrule-rest, dwc-restv2 (jwt-cli/payload/model-query/oql), composer lock-unlock/rename/add-file/update-js/delete-noask.

### P30a — Promoção inicial (463)
- **463 records** com full-message idêntico a records já em `approved.jsonl` (duplicatas de geração) → promovidos direto via `review_manifest_synthetic_expansion_p30_2026_08_22.json`
- approved: 13.183 → **13.646**

### P30b — Correção de prompts conflitantes + promoção dos 155 novos (22/08, tarde/noite)
- **Diagnóstico**: dos 618, **155 eram truly new** (não em approved). Destes, **82 tinham user prompt genérico vazado** ("Qual o comportamento de rest_api_v2?" / "troubleshooting" placeholder) — mesmo input respondido de formas diferentes em approved vs novos → **contradição de treinamento**
- **Correção**: os 82 prompts foram reescritos com tópico específico por claim (PT/EN), via `/tmp/p30_fixed.json`; verificado **0 colisões** vs approved e **0 prompts genéricos** restantes
- **Manifest**: `review_manifest_synthetic_expansion_p30b_2026_08_22.json` com **155 accepted** (73 sem conflito + 82 corrigidos)
- **Promoção**: `promote_sft.py --review-manifest p30b` → 155 promovidos; approved 13.646 → **13.801** (sha256 f55d722f...)
- **Splits regenerados**: train **10.063** / validation **2.512** / test **1.226** (split por famílias connected claim+paraphrase); eval_independent regenerado via `build_eval_gold.py` → **3.404** (anti-vazamento ativo)
- **Validações**: `validate_sft.py` candidates PASS (3.039) e approved PASS (13.801, `--status approved`); `validate_evidence.py` PASS (1.006 claims); `audit_dataset.py` PASS
- **Fix no validador de evidências**: `validate_evidence.py` quebrava com `AttributeError` em 10 claims que usam `corroborating_sources` como **strings = referência cruzada a claim_ids internos** (padrão legítimo de corroboração). Validador atualizado: pré-passada coleta todos os ids; strings são validadas como claim_id existente; dicts continuam validando domínio oficial. Claim `fab164e-0025` corrigido: referência inexistente `hwa-10.2.8-wsl-lab` substituída por bloco `lab_validation` real (serverinst com -thiscpu=-displayname → AWSFAB164E)
- **Backups**: `*.bak-20260822-223823-p30b` (approved/candidates/train/test/validation/eval_independent), `*.bak-20260822-p30bfix` (candidates pré-correção de prompts), `validate_evidence.py.bak-20260822-p30b`

### P30c — Zeragem dos 58 prompts genéricos restantes em approved (22/08, noite)
- **Motivação**: medição do ganho real da P30b revelou que ela só corrigiu os **82 prompts que colidiam** com approved. Restavam **58 prompts genéricos** (0.42% de approved) com texto único que **não colidiam** e por isso escaparam da checagem de duplicatas — claims: `apikey-0001` (13), `apikey-expiry-0002` (16), `abend-recovery-0030` (7), `awsjcl070i-0023` (6), `restv2-filter-0007` (5), `engine-restart-0016` (3), `apikey-oidc-0003` (2), `bhu025e-0019` (2), `https-tls-0018`/`bhu152e-0018`/`bhv082e-0009`/`conwinlog-0015` (1 cada)
- **Correção**: mapeamento claim → tópico específico (PT/EN) usando campo `language` do record (detector por regex falhava em PT sem acento). Ex.: `apikey-expiry-0002` → "expiracao de API Keys (365 dias, propriedade com.ibm.tws.util.jwt.apikey.expiration.date)"; `awsjcl070i-0023` → "mensagem AWSJCL070I na sincronizacao banco/Symphony"; `abend-recovery-0030` → "recuperacao de jobs em ABEND (stdlist, rerun/release)"
- **Aplicação**: 58 em `approved.jsonl` + 58 sincronizados em `candidates.jsonl` (approved = fonte da verdade; os 155 da P30b permanecem idênticos entre os dois arquivos)
- **Splits regenerados**: train 10.063 / validation 2.512 / test 1.226 (inalterados — hashing por família estável)
- **Validações**: `validate_sft.py` approved (13.801) + candidates (3.039) PASS; `validate_evidence.py` PASS (1.006); `validate_eval.py` PASS (3.404); `audit_dataset.py` PASS — **prompts genéricos: 0 em approved e 0 em candidates (0.00%)**
- **Backups**: `approved.jsonl.bak-20260822-p30c`, `candidates.jsonl.bak-20260822-p30c`
- **Lição**: placeholder com texto único escapa da validação de duplicatas — a métrica correta é **% de prompts genéricos**, não só colisões → criado `scripts/validate_generic_prompts.py` para checagem automática no pipeline

### P30d — Correção dos 23 prompts EN residuais pegos pelo novo validador (22/08, noite)
- **Contexto**: ao rodar o recém-criado `validate_generic_prompts.py` pela primeira vez, ele detectou **23 prompts genéricos residuais** (11 EN de `abend-recovery-0030`/`awsjcl070i-0023`/`bhu152e-0018` + 12 variantes) que a P30c deixou passar — padrão "troubleshooting **in** HWA" (EN) não casava com o detector antigo (que procurava "no hwa" em PT)
- **Correção**: substituição `troubleshooting`/`rest_api_v2` → tópico específico da claim (PT/EN por campo `language`) em `approved.jsonl` (23) + `candidates.jsonl` (23)
- **Validação**: `validate_generic_prompts.py` → **PASS 0/16.840** (0.00%); `validate_sft.py` approved (13.801) + candidates (3.039) PASS; `validate_evidence.py` PASS (1.006); `validate_eval.py` PASS (3.404); splits regenerados (train 10.063 / val 2.512 / test 1.226 — inalterados)
- **Backups**: `*.bak-20260822-p30d`
- **Prova de valor do validador**: pegou em minutos o que a checagem manual de duplicatas deixou passar por 3 rodadas — agora é parte obrigatória do pipeline

### P31 — Rodada 7: validação lab dos comandos conman de manipulação de plano (23/08, madrugada)

- **Objetivo**: fechar o gap de `lab_validation` dos 9 comandos conman de operação de plano (fence, limitcpu, rerun, rerunsucc, release job, release sched, submit job, submit sched, altjob) — todas as claims eram `verified`/`high` mas sem evidência lab.
- **Setup no lab**: 2 job definitions criadas via composer (`R7JOB1` = echo, `R7JOB2` = echo hold test; sleep 2) + 1 job stream (`R7JS1` = ON RUNCYCLE DAILY → R7JOB1). Formato confirmado na prática:
  - **Arquivo de job**: `$JOBS` + `MDMDA#JOB / DOCOMMAND "..." / STREAMLOGON wauser / DESCRIPTION / TASKTYPE UNIX / RECOVERY STOP` — **sem `END` por bloco**
  - **Arquivo de stream**: `SCHEDULE MDMDA#JS / DESCRIPTION / ON RUNCYCLE RC1 "FREQ=DAILY;" / : / MDMDA#JOB / END` — **sem header `$SCHEDULES`** (o Sfinal real não usa o header)
  - **Arquivos separados** obrigatórios (job e stream juntos → AWSJOM915E/918E)
- **Comandos validados (todos com confirmação y quando exigida)**:
  | Comando | Sintaxe testada | Resultado |
  |---|---|---|
  | `fence` (f) | `conman "f MDMDA;5"` → `f MDMDA;0` | forwarded + restaurado (Fence: 0) |
  | `limitcpu` (lc) | `conman "lc MDMDA;5"` → `lc MDMDA;20` | forwarded + restaurado (Limit: 20) |
  | `rerun` (rr) | `echo y \| conman "rr = MDMDA#JOBS.R7JOB1"` | job SUCC → rerun criado e executado SUCC (#J406941425) |
  | `rerunsucc` (rrs) | `echo y \| conman "rerunsucc = MDMDA#R7JS1.R7JOB1"` | lista successors internos + rerun do job |
  | `release job` (rj) | `echo y \| conman "rj = MDMDA#JOBS.AT_TEST_001"` | HOLD → READY [Released] (idem R7JOB2/R7JOB2B) |
  | `release sched` (rs) | `conman "rs = MDMDA#R7JS1;noask"` | stream HOLD → READY [Released] |
  | `submit job` (sbj) | `conman "sbj = MDMDA#R7JOB2;noask"` | Submitted as MDMDA#JOBS.R7JOB2; duplicata → **AWSBHU510E** (use `rerun` ou `alias=`); `alias=R7JOB2B` aceito |
  | `submit sched` (sbs) | `conman "sbs = MDMDA#R7JS1;noask"` | Submitted as MDMDA#R7JS1[(0028 08/23/26)] |
  | `altjob` (aj) | `echo y \| conman "aj = MDMDA#JOBS.R7JOB2B;streamlogon=wauser"` | forwarded; keywords: LOGON/STREAMLOGON/DOCOMMAND/SCRIPT/NOASK (**PRIORITY rejeitado**); exige job HOLD/READY (SUCC → AWSBHU085E) |
- **Descobertas novas**:
  - `sbj` **não aceita `hold=`** (keywords: NEEDS/OPENS/PROMPT/FOLLOWS/AT/UNTIL/EVERY/PRIORITY/CONFIRMED/RECOVERY/INTO/ALIAS/RECOVERYJOB/AFTER/ABENDPROMPT/RECOVERYPROMPT/ONUNTIL/DEADLINE/RCCONDSUCC/VARTABLE/VT/CRITICAL/MAXDUR/ONMAXDUR/MINDUR/ONMINDUR) — HOLD é comando separado (`h`) ou via `at=` futuro
  - `rs` **não aceita seleção por instância** `[hhmm,data]` (AWSBHU039E) — só seletores por atributos (NEEDS/OPENS/PROMPT/FOLLOWS/AT/UNTIL/PRIORITY/LIMIT/CARRYFORWARD/NOASK/ONUNTIL/DEADLINE)
  - `aj` **não aceita `priority=`** (AWSBHU039E) — só LOGON/STREAMLOGON/DOCOMMAND/SCRIPT
  - `rerun` de job ad hoc em stream default `MDMDA#JOBS` gera `>>rerun as JOB` (HOLD → SUCC)
- **Claims**: `lab_validation` adicionado a **9 claims** (fence-0001, limitcpu-0001, rerun-0001, rerunsucc-0005, release-job-0006, release-sched-0001, submit-job-0002, submit-sched-0007, altjob-0003) — claims.jsonl continua com **1.006** (mesmo total, 39 agora com lab_validation)
- **Evidência**: `data/evidence/lab-validation-2026-08-22-r7-conman-ops.jsonl` (9 records)
- **Validação**: `validate_evidence.py` PASS (1.006, observed_in_lab=9)
- **Backup**: `claims.jsonl.bak-20260822-r7`
- **Limpeza**: jobs/streams de teste (R7JOB1/R7JOB2/R7JS1) deixados no banco para reuso; fence/limit restaurados (Fence: 0, Limit: 20)

# Downloads And Links

| Component | Source / URL | Used in lab |
| --- | --- | --- |
| HWA MDM 10.2.8 Linux x86_64 | Local image `/root/hwa/HWA_10.2.8_MDM_LINUX_X86_64.zip` | Yes |
| Open Liberty 26.0.0.3 | `https://public.dhe.ibm.com/ibmdl/export/pub/software/openliberty/runtime/release/26.0.0.3/openliberty-26.0.0.3.zip` | Yes |
| System Java 21 (OpenJDK) | Ubuntu `openjdk-21-jdk` package (apt) | Yes |
| HWA embedded Java | IBM Semeru OpenJ9 21, bundled under `/opt/hwa/TWS/JavaExt/jre/jre` | Yes (used by HWA) |
| PostgreSQL 18 | PostgreSQL Global Development Group apt repo (PGDG) | Yes |
| DWC 10.2.8 | IBM Fix Central (login/entitlement required): `https://www.ibm.com/support/fixcentral/` | Not installed |

IBM Semeru OpenJ9 21 standalone downloads:
`https://www.ibm.com/semeru-runtimes/downloads/`

Note: The DWC is a separate component requiring its own installer image
(`dwcinst`), obtained from IBM Fix Central with a valid entitlement. The MDM
image used here does not include the DWC installer.

## Errors And Corrections Learned

- `/hwa` was not the actual WSL path; the image was under `/root/hwa`.
- Passing `/opt/liberty` instead of `/opt/liberty/wlp` failed Liberty validation.
- Liberty extraction permissions initially blocked `wlp/lib/versions` and later
  blocked `ws-server.jar`; making the tree readable/executable fixed it.
- HWA 10.2.8 required both `--sslkeysfolder` and `--sslpassword` in this fresh
  installation flow.
- `wauser` had to exist before `serverinst.sh` could install the component.
- In this lab's `serverinst` invocation, the nested `twsinst -agent both`
  rejected equal `-thiscpu` and `-displayname` values (`AWSFAB164E`). This is
  recorded as an invocation-specific observed constraint, not a universal
  rule. The official 10.2.8 reference describes `--thiscpu` as the workstation
  name and `--displayname` as the dynamic-agent name; for agent installation,
  `--thiscpu` must not equal the master workstation name.
- PowerShell expanded `$(hostname)` incorrectly when nested inside the WSL
  command; the lab used the explicit hostname `MDMHOST` instead.
- `JnextPlan -for 0000` creates a zero-duration plan and does not show the
  Sfinal instances; `JnextPlan -for 2400` showed both streams and their jobs.
- `composer list Sfinal` is not a valid way to inspect the Sfinal file after
  import. The imported objects were inspected as `MDMXA#FINAL` and
  `MDMXA#FINALPOSTREPORTS`.
- `MDM_1` is a recommended naming convention for identification and uniqueness,
  not a universal HWA syntax requirement. The lab's `MDMDA` name is valid but
  less descriptive of the relationship to `MDM`.

## Sfinal Conclusion

The absence of jobs after the first `JnextPlan -for 0000` was caused by the
zero-hour plan horizon, not by a missing Sfinal import. The installer had
already imported Sfinal. The official HCL procedure distinguishes the Sfinal
file/database definitions from the runtime Symphony plan: `composer add Sfinal`
adds the definitions, and `JnextPlan` includes them in the current plan.

Official reference: `https://help.hcl-software.com/workloadautomation/v101/distr/src_ref/awsrgautomateprodplan.html`

Official parameter references:

- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstparams.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiagentparams.html`

## ResetPlan Laboratory Observation

`ResetPlan` without `-scratch` was executed after saving the current Symphony
and plan outputs under `/root/hwa/lab-backups/resetplan-latest`. It archived the
Symphony, updated statistics and reset production-plan information while
preserving the preproduction plan. A new `JnextPlan` was required before
`conman` could inspect the plan again.

The rebuild command used `-from 08/17/2026 0000 -for 2400` without an explicit
timezone. The resulting plan reported `03:00 America/Sao_Paulo`, demonstrating
that an unqualified `-from` can be shifted by timezone interpretation. Always
specify and verify the intended timezone in production plan recovery commands.

## Ad Hoc JOBS Stream Date

After `JnextPlan -for 2400`, `planman showinfo` showed the production plan
ending on 08/18 and ad hoc submissions without `into=` appeared in
`MDMDA#JOBS` at `0000 08/18`. This is the implicit JOBS stream instance selected
by the current plan, not a tomorrow schedule in the ad hoc job definition.

For a controlled test, target an existing current-plan stream instance with
`into=` and its exact scheduled time/date. Do not run another `JnextPlan` merely
to move an ad hoc job to today; that changes the production plan and restarts
workstations. In this lab, `at=absolute` was also rejected by `conman` with
`AWSBHU141E`, so it is not a confirmed immediate-submit form here.

## Dynamic-Agent READY Root Cause

The root cause of the apparent dispatch failure was the workstation job limit.
`conman sc MDMDA` initially reported `LIMIT 0`, while the test jobs had
priority `10`. HCL documents that limit zero allows only `HI` and `GO` jobs from
a `READY` stream; it does not mean unlimited execution. The successful fix was:

```bash
conman 'lc MDMDA;10'
```

After the change, the dynamic-agent jobs moved from `READY` to execution and
the JobManager log recorded `AWSITA031I` followed by `AWSITA034I` with success.
The command `limit cpu MDMDA;10` was ambiguous in this conman session; the
short form `lc MDMDA;10` worked.

The first ad hoc command then failed with `AWSITA066E` because the executor
rejected a privileged user. A second submission with `logon=wauser` completed
successfully with return code zero:

```bash
conman 'sbd MDMDA#"ls -la /tmp";alias=ADHOC_LIMIT_LOGON;logon=wauser;noask'
```

Official reference for workstation limits:
`https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrglimitcpu.html`

Official fence reference:
`https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgfence.html`

The complex stream validation was followed by a real ad hoc execution on
`MDMDA`. `CPLXSTRM` completed `SUCC`; `CPLX_01`, `CPLX_02`, `CPLX_03` and
`CPLX_04` completed successfully in `FOLLOWS` order. The run used `LIMIT 2`
and priorities `10`, `20`, `HI` and `GO`, with start/completion evidence in
`JobManager_message.log`.

### LIMIT/FENCE Reference Table

| Setting | Meaning | Lab implication |
| --- | --- | --- |
| `LIMIT 0` | Only `HI`/`GO` jobs can launch from a `READY` stream | Ordinary priority `10` jobs remain `READY` |
| `LIMIT 10` | Up to ten concurrent jobs | Used successfully on `MDMDA` |
| `LIMIT SYSTEM` | No concurrency limit on normal workstations | Special behavior exists for extended agents |
| `FENCE 0` | Jobs with priority greater than zero may pass | Lab baseline |
| `FENCE 20` | Jobs with priority `20` or below are blocked | Requires deliberate operations control |
| `FENCE SYSTEM` | Resets fence to zero | Not equivalent to unlimited `LIMIT` |

Limit and fence changes are carried forward by preproduction processing to the
next production plan, so both the current plan and the next generated plan
must be checked.

## Complex Composer Validation Without Persistence

Temporary complex definitions can be tested without changing the database or
the plan by using `composer validate` only. The laboratory validated seven
objects containing:

- stream-level `( AT ... EVERY 0002 EVERYENDTIME ... )`;
- job-level `EVERY 0002`;
- `UNTIL`, `LIMIT 2` and `ONOVERLAP ENQUEUE`;
- four dependent jobs using `FOLLOWS`;
- numeric, `HI` and `GO` priorities.

The temporary file was not added, and `composer display` confirmed that the
objects were absent from the database. The first validation also captured two
parser lessons: stream names must fit the 16-byte limit, and the tested job
syntax required `RECOVERY` before `PRIORITY`.

The validated job-level `EVERY 0002` was then executed through `CPLXJOB2M`.
The first `CPLX_EVERY` run completed at 14:59 and the second `every run` at
15:01; both returned `SUCC` with code zero and produced the expected JobManager
start/completion notifications.

## Mandatory Post-Installation Workstation Check

Immediately after the first plan is generated, inspect every workstation that
will execute workload:

```bash
conman 'sc MDM'
conman 'sc MDMDA'
conman 'showcpus'
```

Record at least `LIMIT`, `FENCE`, link state and the `J` JobManager flag.
Fresh installations can expose a workstation limit of zero. Do not interpret
zero as unlimited: for a `READY` stream, only `HI` and `GO` priority jobs can
launch at limit zero. Set an intentional laboratory or production value, for
example:

```bash
conman 'lc MDMDA;10'
```

Also inspect the fence. A fence value prevents jobs with priority less than or
equal to the fence from launching. For a new lab workstation, the expected
baseline is normally `FENCE 0`; any nonzero value must be deliberate and
documented. Validate with:

```bash
conman 'sc MDMDA'
```

This check must happen before diagnosing a job stuck in `READY` as a broker,
JobManager, TLS or Resource Advisor failure.

### Priority / LIMIT / FENCE Validation

`PRIO_TEST` used `LIMIT 2` and confirmed:

- priority `0`: `HOLD`, never launched;
- priorities `10`, `20`, `50`: `SUCC`, run normally;
- priority `HI` and `GO`: `SUCC` and run even under the CPU limit;
- the stream displayed `STUCK` with `LIMIT 2` while concurrent jobs queued.

`FENCE_TEST` set `FENCE 20` on `MDMDA` and confirmed:

- priority `10` and `20`: `FENCE` state, blocked;
- priority `30`, `HI` and `GO`: `SUCC`, allowed.

The fence was restored to `0` afterward. A high-priority job stream does not
bypass a restrictive workstation fence, but `HI`/`GO` jobs do bypass the CPU
limit.

### Folders And modify/replace

A folder `LAB` was created with `composer mkfolder LAB` and navigated with
`composer chfolder`. A job `JOB_A` was added inside the folder. `composer
replace` successfully changed `JOB_A` from `lab_ls.sh`/`RECOVERY STOP` to
`fail_continue.sh`/`RECOVERY CONTINUE`. `composer modify` failed in batch
because it is an interactive command; `replace` is the batch update command.
Job definition
files placed in a folder still require the `$jobs` prefix.

### Variables And Variable Tables

A variable table `LABTAB` was created with:

```text
vartable LABTAB
  description "Lab variable table"
  members
    VARMARK "LAB_VALUE_OK"
  end
```

The variable table is assigned to a job stream with `VARTABLE` placed before
`ON RUNCYCLE`. A native UNIX `docommand` job referenced the variable. Using
`${VARMARK}` produced no substitution, while `^VARMARK^` resolved to
`LAB_VALUE_OK`. Native job types require the caret syntax; `${var}` is for
dynamic-agent integration jobs. The variable table syntax uses the lowercase
keyword `vartable`, `members` and `end`.

### Restart And Recovery

`ShutDownLwa` and `StartUpLwa` were used to restart the dynamic agent. After
the restart, `MDMDA` reconnected with the `J` (JobManager) flag preserved,
`LIMIT 10` and `FENCE 0` maintained, and resource registration (`AWSITA083I`)
continued normally. Restarting the agent does not reset the workstation limit
or fence values set with `conman lc` and `conman f`.

## JnextPlan Production Safety

`JnextPlan` is not a harmless refresh command. The official 10.2.8 reference
states that every execution stops and restarts all workstations while moving
from the old Symphony to the new production plan.

- `JnextPlan -for 0000` removes successfully completed job-stream instances
  from the new plan by default.
- `JnextPlan -for 0000 -noremove` preserves successfully completed instances.
- The `enCarryForward` global option controls incomplete job-stream carryforward.
- Preserving a completed instance does not by itself mean that the job will
  automatically execute again. The operational risk is accidental rerun,
  carryforward of incomplete/error work, duplicate submission, or confusion
  caused by accumulated instances.

Before production execution, capture plan state, inspect RUNNING/READY/WAIT/
ABEND/SUPPR instances, verify `enCarryForward`, ensure no concurrent plan
operation is active, run once from the active MDM, and compare the resulting
plan and logs. Use `-noremove` only for an explicitly approved purpose.

Official reference:
`https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgJnextPlan.html`

## Naming Convention

Prefer names such as `MDM` for the base workstation and `MDM_1` for a dynamic
agent installed on the same host. The suffix makes the relationship obvious
while preserving workstation-name uniqueness. This is an operational
convention, not an official requirement that every dynamic agent use `_1`.

## Host And Gateway Validation

The WSL hostname is `DESKTOP-298GT47.localdomain`. `MDMHOST` is a deliberate
lab alias mapped to loopback and is the name used consistently by the MDM
workstation NODE and direct `ResourceAdvisorUrl`. It is not the operating-system
hostname. Replacing it requires coordinated NODE, URL, DNS and certificate-SAN
changes.

`JobManagerGW.ini` has `autostart = no`, which is correct for the current direct
Resource Advisor topology. Enabling gateway autostart without changing the
agent URL to the gateway endpoint would mix two topologies and is not a safe
correction.

The dynamic agent was restarted with `ShutDownLwa` and `StartUpLwa`. It returned
with the JobManager flag and resumed resource registration, but a fresh ad hoc
submission with a unique alias remained `READY`. Restart alone did not resolve
the dispatch problem.

The four initial `AWKRRP086E_DOMAIN_NOT_CREATED` entries were followed by
continuous `AWSITA083I` resource-registration messages. This supports a
startup-race hypothesis for the registration episode, but does not prove that
the agent is fully capable of executing workload; the ad hoc job still remained
`READY`.

## Composer EVERY Test

The laboratory validated the stream-level syntax:

```text
SCHEDULE MDMXA#LAB_EVERY2M ON RUNCYCLE RULE1 "FREQ=DAILY;"
( AT 1351 EVERY 0002 EVERYENDTIME 1400 ) :
```

The first attempt placed `EVERY` outside the parenthesized time restriction and
was rejected by Composer. The corrected file validated and added five objects.
The MDMXA test was an extended-agent test and jobs remained `READY`; it was not
treated as dynamic-agent execution.

The corresponding MDMDA definitions also validated and were submitted, but
remained `READY` during the observation window. JobManager logged resource
registration but no execution request. This is an unresolved dynamic-agent
dispatch issue, not a successful execution result.

The later status comparison confirmed that the schedule syntax itself is valid:
the submitted MDMDA instance reached `READY`, so the investigation should focus
on JobManager/ResourceAdvisor/broker dispatch and agent configuration rather than
on `AT ... EVERY ... EVERYENDTIME` parsing.

An immediate ad hoc test further isolated the issue. The command
`conman 'sbj = MDMDA#LAB_DA_SCRIPT_01;noask'` was accepted and placed the job in
`MDMDA#JOBS`, but the job remained `READY` and no execution request appeared in
`JobManager_message.log`. Therefore the issue is not the run cycle or date
selection; dynamic-agent dispatch/configuration remains unresolved.

Official submit-job reference:
`https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsubmitjob.html`

## Conclusion

The HWA laboratory exercise validated the end-to-end installation and
Composer/runtime behaviour of HCL Workload Automation 10.2.8.00 on WSL2
Ubuntu 22.04 with PostgreSQL 18 and Open Liberty 26.0.0.3.

### Validated Outcome

- Installation succeeded after correcting the Liberty directory (`/opt/liberty/wlp`),
  certificate setup, ownership/permissions and `--thiscpu`/`--displayname`
  distinct values.
- `Batchman`, `JnextPlan`, `Symphony` and the JobManager REST endpoint all
  started correctly.
- The full Composer feature set exercised against the dynamic agent `MDMDA`
  succeeded: complex jobs, `EVERY` (stream and job), recovery, `FOLLOWS`,
  `OPENS`, `NEEDS`, priorities, `LIMIT`, `FENCE`, folders, `modify`,
  `replace` and variable tables.
- Variable substitution in native UNIX `docommand` jobs requires the caret
  syntax `^VARMARK^`; `${var}` is for dynamic-agent integration jobs.
- `JnextPlan`, `ResetPlan` and timezone semantics were consolidated as
  evidence and runbook notes.
- A dynamic-agent restart (`ShutDownLwa` / `StartUpLwa`) preserved the
  `LIMIT 10`, `FENCE 0` and `J` flag, and resource registration continued.

### Schema And Database

- HWA on PostgreSQL uses multi-schema separation: `dwb` (29 tables), `evt`
  (4), `log` (2), `mdl` (48), `pln` (13). Total: 96 tables.
- The `DB` schema structure is owned by `postgres` with `twsuser=U/postgres`
  (privilege to use, not ownership).
- The role `twsuser` exists; the role `twsdbuser` does not. The term
  `twsuser` is a role, not a schema.

### wauser Permissions

- `wauser` is not in `sudoers`; `sudo -l -U wauser` returns "not allowed".
  Test scripts in `/home/wauser/bin` run as `wauser` directly because they
  are owned by `wauser:wauser` and mode `755`. No sudo is required for the
  HWA laboratory.

### Known Gaps

- **DWC (Graphical Designer)**: not installed. The DWC is a separate
  component requiring its own installer image obtained from IBM Fix Central
  with a valid entitlement. The MDM image used here does not include the
  DWC installer.
- **JnextPlan -scratch** and **dbrunstats**: not executed; would erase the
  preproduction plan and require database statistics refresh.
- **JSDL schema `TASK`**: rejected with `AWSJCS029E`; not corrected.
- **Production hardening**: self-signed certificate, password `padrao`,
  WSL2 cluster and Open Liberty 26.0.0.3 are not production-ready.

## One-Shot Feature Validation

Autonomous one-shot validation of the remaining short-, medium-, and special-term feature backlog on the MDM direct topology (10.2.8, WSL2 lab). Each item was exercised via Composer/Conman/Planman and the outcome recorded as evidence JSONL (`data/evidence/lab-validation-2026-08-17-*.jsonl`).

### Validated (working)

- **STARTCOND FILECREATED / FILEMODIFIED**: start-condition job triggered via file event monitor (FILEMOD worked; FILECR hit `AWSITA030E` on unresolved `bin-path` in generated JSDL).
- **PROMPT**: inline `PROMPT "..."` job goes to HOLD and blocks the stream (reply requires a named prompt, 1-8 bytes).
- **CONFIRMED**: job held until `conman confirm <job>;SUCC` (SUCC|ABEND required); resolves as `[Confirmed]`.
- **KEYJOB**: accepted and runs (SUCC).
- **CARRYFORWARD**: accepted; completed with `[Carry]` behavior.
- **DEADLINE**: `DEADLINE <time> ONLATE KILL` enforced; late job went `[Suppressed][Late]` and was killed.
- **MAXDUR**: `MAXDUR <min> ONMAXDUR KILL` enforced; ABEND rc 143 `[MaxDurationExceeded][KillSubmitted]`.
- **MINDUR**: `MINDUR <time>` accepted; `[MinDurationNotReached][Continue]` noted.
- **ONOVERLAP**: OOVPAR/OOVDN accepted and ran SUCC.
- **Calendar**: `$calendar LABCAL` (max 8 chars) + `FREEDAYS LABCAL` (before `ON RUNCYCLE`) works.
- **Job types**: `TASKTYPE DB`, `WEB`, `FTP` all validate, add, and run SUCC.
- **Conman ops**: `rerun job` (creates successor WAIT), `confirm job;SUCC`, `cancel sched` (CANCL `[Cancelled]`); `kill` validates state (`AWSBHU085E` on completed job).
- **Planman**: `showinfo` (plan/run details), `confirm` (run number update `AWSJCL065I`).
- **REST**: JobManager REST endpoint reachable over HTTPS; auth issues LtpaToken2; returns `AWSJMR011E ServiceUnavailable` (GW not active in direct topology).

### Syntax limitations (rejected by this engine in direct topology)

- **STARTCOND JOB <agent>#<job>**: rejected at the STARTCOND token (only FILECREATED/FILEMODIFIED accepted).
- **CRITICAL**: rejected in every tested position (job line / jobstream). Likely needs WSA; use KEYJOB for WSA.
- **JOIN / ENDJOIN**: rejected in all tested forms.
- **IF conditional** (IF rc, IF SUCC, IF condname, OUTCOND): rejected in all Composer forms tested.
- **TASK / JSDL inline**: rejected (`AWSJOM918E`).
- **Runcyclegroup**: validates but `composer add` fails `AWSBCZ021E`; the literal `$` must be written via file (shell expands `$`).
- **Tooling**: no standalone `audit`, `report`, `fbcount`, `dataextract`, or workload-app export/import commands; `dbrunstats.sh` is a DB2-only script. These require the broker/gateway or Dynamic Workload Console.

### Notes

- Correct job line order is required: `JOBNAME DOCOMMAND "cmd" STREAMLOGON wauser TASKTYPE UNIX RECOVERY STOP [attrs]`. `TASKTYPE` before `DOCOMMAND` fails.
- Evidence artifacts: `lab-validation-2026-08-17-{startcond-filemonitor-0053, prompt-block-0054, confirmed-0055, deadline-0056, calendar-0057, keyjob-0058, maxdur-0059, carryforward-0060, mindur-0061, onoverlap-0062, rest-api-0063, jobtypes-0064, conman-ops-0065, planman-0066, tooling-0067, conman-manip-0068}.jsonl`.

## Enrichment P1-P8 (2026-08-17/18)

Follow-up enrichment that re-resolved every "syntax limitation" from the One-Shot section with the **correct** Composer/Conman syntax, plus REST V2, runtime behavior, cross-version scoping, SFT generation, and an independent audit. Each finding was validated in the lab (`added`/`SUCC`) and recorded as evidence.

### P1 — Syntax blockers resolved (all validated / SUCC in lab)

- **JOIN**: `join <name> <n|ALL> of description "..." ... follows <ws>#<stream>.<job> if <cond> ... endjoin`. Name ≤ 16 chars, max 4 joins/object; predecessor must be a full `workstation#jobstream.job` reference.
- **IF conditional**: `follows <ws>#<stream>.<job> if <cond>`. Status conditions for jobs: `SUCC|FAIL|ABEND|SUPPR` (**EXEC is not documented**; removed after audit). Output conditions are defined in the JOB definition via `succoutputcond <name> "<val>"` / `outputcond <name> "<val>"`.
- **CRITICAL**: keyword `critical` inline in the job statement (e.g. `DEADLINE 2359 CRITICAL` → jobs <23:59). Requires WSA (`enWorkloadServiceAssurance`, default YES) and a deadline.
- **TASK / JSDL**: `TASK <?xml ...><jsdl:jobDefinition xmlns:jsdl="...jsdl" xmlns:jsdle="...jsdle">...<jsdle:script>date</jsdle:script>...</jsdl:jobDefinition>` + `TASKTYPE UNIX` (also WINDOWS/OTHER/BROKER). XML only, max 4095 chars. Embedded JSON/YAML jobs = 10.2.3+, **not** supported by composer/dataextract/dataimport.
- **runcyclegroup**: keyword `runcyclegroup <name>` (no `$`) + mandatory `vartable [folder/]tablename` + `on runcycle <name> "FREQ=DAILY;"` + `end`; name ≤ 8 chars starting with a letter. `$runcyclegroup`/`$RCG` causes `AWSBCZ021E` (the `$` must be written via file, not shell).

### P2 — Broker / REST API V2

- REST API V2 is active at **`https://MDMHOST:31116/twsd/`** (Swagger UI) with spec `WA_API3_v2.json` (OpenAPI 3.1.0). **Not** `/JobManagerRESTWeb/` (legacy returns AWSJMR011E).
- **Live (curl -v)**: TLS 1.3, cert `CN=HWA-LAB` (issuer `HWA Lab CA`), `GET /twsd/` → HTTP 200 serving `XSRF-TOKEN`. Basic auth (`wauser`) accepted. Response envelope is `{"count":N,"results":[...]}`.
- Endpoints validated: `/twsd/api/v2/model/jobstream` (count 17), `/model/jobdefinition` (66), `/plan/job` (count 90), `/plan/job/{id}` (200). **Actions use PUT** (not POST): `PUT /plan/job/{job_id}/action/{confirm-succ,kill,hold,release,rerun,cancel,confirm-abend}` — a PUT to confirm-succ on a terminal job returned `AWSBIN076E` (valid state guard), confirming the handler runs. **Full lifecycle validated**: `POST /plan/job/submit-ad-hoc-job` with `{"workstationKey":"/MDMDA","task":{"UNIX":{"taskString":"sleep 120","isCommand":"true","userName":"wauser"}}}` → HTTP 200 `{"id":"MDMDA;JOBS;SLEEP"}`; the returned id is a composite job key — the plan UUID is read from `GET /plan/job`; then `PUT /plan/job/{uuid}/action/{hold,kill,confirm-succ}` all returned **HTTP 200** (clean, non-error). Using the composite key instead of the UUID caused `AWSBIO006E SCHED-NAME null`. Submit endpoints: `POST /plan/job/submit`, `/plan/job/submit-ad-hoc-job`. REST V2 introduced in 10.1 FP1; 9.5 has V1 only.
- Broker: workstation `MDM_DWB` (type B) is **active and LINKED to the master**. `conman sc` shows `MDM_DWB 6 OTHR BROKER 0 0 08/17/26 15:18 LTI JW MASTERDM` — state `LTI JW`: **L**=LINKED, **J**=JobManager/gateway up, **W**=WAGENT/broker runtime up. **The REST API V2 on /twsd:31116 is served by this broker's gateway**; it is not independent of the broker. (Earlier the broker was assessed as down because `JobManagerGW` had `autostart=no`; it is now running.)

### P3 — Runtime behavior (Conman/Planman)

- **HOLD by LIMIT**: submitted streams went HOLD because dynamic agents have **LIMIT 0** post-install; jobs launched once the limit cleared (BLK4 EXEC, SUC4 SUCC). The earlier `release job ...;FOLLOWS` AWSBHU043E confusion was a limit-HOLD, not a missing dependency. Internal `follows` resolves correctly (JSC SUCC after JSA).
- **RECOVERY RERUN**: `recovery rerun [same_workstation] [repeatevery hhmm] [for number attempts]`; no `rerun <n>`. `recovery rerun` validated; on `exit 5` the job ABEND rc5 then `>>rerun as J1` (new id) also ABEND rc5. `RECOVERY RERUN 2` / `SAME_WORKSTATION FOR 2 ATTEMPTS` rejected inline.
- **limit cpu / fence**: `{limit cpu|lc} wks;limit;noask` (0–1024, system); `{fence|f} wks;pri;noask` (0–99, hi, go, system). `lc MDMDA;5;noask` accepted. Post-install banner shows `Limit: 0, Fence: 0`.
- **ONLATE** accepts only `kill`; there is **no** `resumecond` keyword/command (recusal example generated in SFT).

### P4 — Cross-version matrix

Full matrix in `data/incoming/research/harness/shard-version-matrix-9findings.jsonl` (10 claims). Core features (JOIN, IF, CRITICAL/WSA, TASK, runcyclegroup, RECOVERY RERUN, ONLATE, limit cpu/fence) are identical in 10.2.0 and 10.2.8. **Version-dependent**: embedded JSON/YAML jobs (10.2.3+); onoverlap enqueue 39-dependency limit + `AWSJOM138E` and donotstart domain limit (10.2.7+, KB0128221/IJ56794); REST API V2 (10.1 FP1+, 9.5 V1 only).

### P5 — SFT generation

34 version-aware candidates (17 EN / 17 PT; read_only 28 / mutating 2 / destructive 2 / credential 2) saved to `data/sft/candidates/sft-candidates-syntax-rest-2026-08-17.jsonl`, including 10 automation/recusal examples (conman_show_jobs, rerun, cancel, ocli_plan_submit_docommand credential-refusal, 9.5 V2-unsupported refusal).

### P6 — Independent audit (ADU)

`hwa-dataset-auditor` verdict: **APPROVED WITH CAVEATS** (safe for experimental; no security leak — lab password absent, `<REDACTED>` correct — no version leakage). MAJOR M1 (claim `hwa-10.2.8-composer-if-conddep-0001` listed EXEC as a valid condition, contradicting the correct SFT response and official docs) was **fixed in place** in `shard-composer-join-if.jsonl`. Remaining: M2 (automation candidates cite non-entailing evidence — repoint claims to action allowlist/schema), M3 (topic imbalance, automation 30%). Evidence: `lab-validation-2026-08-17-sft-audit.jsonl`.

### P7 — Test cleanup

Removed persisted test job streams via `echo y | composer delete MDMDA#<stream>` (interactive confirm required): HR_TEST3/4/5, JOIN_OK2, IF_OK2, CRIT_OK, TASK_OK, PRIO_TEST, REC1, REST_HOLD, MAXDUR_TEST, MINDUR_TEST, CALEND_TEST, OOVPAR_TEST, OOVDN_TEST, WS_TEST, DB_TEST, FTP_TEST, START_FILE, START_FILEMOD. Evidence: `lab-validation-2026-08-17-cleanup-test.jsonl`.

### Evidence added this batch

- `data/evidence/lab-validation-2026-08-17-{syntax-resolved-0069, broker-topology-0070, rest-api-v2-0071, recovery-rerun-0072, limit-follows-hold-0073, limit-cpu-0074, sft-audit-0075, cleanup-test-0076, rest-v2-port-live-0077, rest-v2-action-put-0078, broker-active-0079, broker-correction-0080, rest-v2-submit-action-0082, cleanup-orphans-0083}.jsonl`
- `data/evidence/lab-validation-2026-08-17-rest-api-corpus.jsonl` (0081, REST spec corpus incorporation)
- `data/incoming/research/harness/shard-version-matrix-9findings.jsonl`
- `data/sft/candidates/sft-candidates-syntax-rest-2026-08-17.jsonl`
- `data/raw/WA_API3_v2.json` (OpenAPI 3.1.0 spec, 1.73 MB) and `data/raw/WA_API3_v2_REST_API.md` (structured REST API doc, 376 KB) — both incorporated into the corpus (see P9)
- `data/evidence/lab-validation-2026-08-18-{bmevents-config-0084, edwa-rules-0085, edwa-cleanup-0086}.jsonl`

### P9 — REST API V2 corpus incorporation (2026-08-18)

- Captured the live OpenAPI spec `WA_API3_v2.json` (OpenAPI 3.1.0, spec version 2.1.6.0, 212 paths, security JWT+Basic) from `https://127.0.0.1:31116/twsd/WA_API3_v2.json`.
- Added `data/raw/WA_API3_v2.json` (875 chunks) and a generated structured `data/raw/WA_API3_v2_REST_API.md` (304 chunks) documenting every endpoint/method/param/response.
- Extended `extract_docs.py` valid_extensions to include `.json`; mapped `wa_api3_v2` doc to version 10.2.8 in `infer_version`.
- Curation pipeline verdict **APROVADO COM RESSALVAS** (not REPROVADO). `unknown_version_share` dropped 0.0441→0.0106; 563 REST chunks in train_full; `synthetic_in_training=0`, no security hits, no token-limit violations.
- Note: the API spec version `2.1.6.0` is matched by the IP-redaction regex and becomes `[IP_ADDRESS]` in some chunks (acceptable pipeline behavior).

### P10 — BmEvents.conf + EDWA event rules (2026-08-18)

**Terminology trap (important).** In official HCL 10.2.8 docs, "BmEvents" is the *event-reporting* config file `TWA_DATA_DIR/BmEvents.conf` for `batchman`/`mailman` (status events to FILE/JSON/PIPE). Event-*driven job launching* is a different feature: **EDWA (event-driven workload automation)** with **event rules** (`monman` agent monitoring engine + `ssmagent` + event processing server in the app server).

**BmEvents.conf validation** (evidence 0084):
- Location: `TWA_DATA_DIR` = `/opt/hwa/TWSDATA/BmEvents.conf` (NOT the sample `/opt/hwa/TWS/config/BmEvents.conf`).
- Configured: `OPTIONS=MASTER`, `LOGGING=ALL`, `SYMEVNTS=YES`, `CHSCHED=HIGH`, `EVENT=51 101 102 103 104 105 106 151 152 154 155 156 201 202 203 204 251 252`, `FILE=/opt/hwa/TWSDATA/event.log`, `JSON=/opt/hwa/TWSDATA/event.json`, `PIPE=UNISONWORK/MAGENT.P`.
- **Paths must be absolute**: `FILE=UNISONWORK/event.log` fails with `AWSBDD003E BmEvents error opening ... No such file or directory` (relative UNISONWORK is not a real dir in cwd).
- **Apply requires a production restart**: `conman stop MDM` + `conman start MDM` (batchman/mailman/jobman restart; netman/monman/writer stay). `JnextPlan` alone does NOT recycle batchman.
- **fd caveat**: batchman opens the FILE/JSON files once at startup and keeps the fd — deleting the file sends events to the deleted inode until process restart.
- `EVENT=` completely overrides defaults. The default list `51 101 102 105 151 152 155 201 202 203 204 251 252` does NOT include job launch/done (103/104) or schedule submit/done (156/154) — add them explicitly to see full lifecycle.
- Validated output (submitting MDMDA#EVTJS_TEST): `51 ProcessReset`, `251 LinkDropped`, `106 JobSubmit`, `156 SchedSubmit`, `103 JobLaunch`, `104 JobDone`, `154 SchedDone` — in both `event.log` (ASCII) and `event.json` (structured).

**EDWA validation** (evidence 0085):
- State in lab: `monman` running on MDM/MDMDA (flag `M` in `conman showcpus`); EDWA `ssmagent.bin` running from `/opt/hwa/TWSDATA/EDWA/ssm/config`; event processing server inside Open Liberty `engineServer`; 3 default rules (UPDATEFAILURE/STATUS/SUCCESS = GenericEventPlugIn `Upgrade`).
- Rule management = `composer` XML (`add <file>`, `validate <file>;syntax`, `list EVENTRULE`, `display EVENTRULE <name>`); validate must be `validate <file>;syntax` (no type prefix). Rule XML validated against `EventRules.xsd` (`eventRuleSet`/`eventRule`/`eventCondition`/`filteringPredicate`/`action`).
- Deployment: non-draft (`isDraft=no`) rules become **active** via the internal rule builder within `deploymentFrequency` (default 5 min, global option). Status goes `activation pending` → `active`; the generated monitoring config appears in `/opt/hwa/TWSDATA/EDWA/monconf/` (`FileMonitor.cfg`, `activeRules.txt`, `deployconf.zip`) and the EDWA ssmagent reloads it.
- Event providers: `TWSObjectsMonitor`, `TWSApplicationMonitor` (FT agents only), `FileMonitor` (FileCreated/FileDeleted/ModificationCompleted/LogMessageWritten), `DatasetMonitor`, `GenericEventPlugIn` (custom via `evtdef`/`sendevent`). FileMonitor NOT supported on pools/dynamic pools/remote engine.
- Actions: `MessageLogger` (MSGLOG → internal auditing DB, `AWSMSL101I`), `TWSAction` (sbj/sbs/sbd/reply), `GenericAction`, `MailSender`, `TECEventForwarder`, `TWSForZosAction`.
- Validated end-to-end: (1) `FileCreated /tmp/hwa_oneshot/trigger.txt` → MessageLogger `AWSMSL101I "The message ... has been successfully logged"`; (2) `FileCreated /tmp/hwa_oneshot/trigger2.txt` → TWSAction `sbs` → `AWSTAP101I The job stream "EVTJS_TEST" has been successfully submitted` → job EVTJOB1 actually ran (pln.pjor_job_runs status E, JobManager archive zip with script.sh/out.log).
- REST V2 (`WA_API3_v2.json`) has only EDWA *action* endpoints: `PUT /plan/workstation/action/{start,stop,switch}-event-{monitoring,processor}` and `GET monitoring-configuration`. Event rule CRUD is via composer/DWC or the separate `/eventrule/engine/*` REST application (MessageLogRecordEventRuleResource, AuditRecordEventRuleResource, etc. seen in engineServer messages.log). `GET monitoring-configuration` returned `AWSBIN091E` for MDMDA/MDMXA even with monman running (REST read failing on broker, monitoring itself active).
- Caveats: FileCreated only fires on new file creation — delete+recreate of same filename was not re-detected (filemon caches). `composer delete EVENTRULE <name>` and stream delete are interactive — feed `y` via stdin (`echo y | composer delete ...`).

### P11 — Evidence consolidation + SFT rework + recovery incident (2026-08-18)

- **Consolidated all lab evidence into `claims.jsonl`**: 79 lab records (batch 0005-0086) merged via a consolidation script; the file reached 736 records.
- **`claims.jsonl` truncation incident + recovery**: a consolidation script rewrite failed partway, truncating `claims.jsonl` from 736 to 115 records (write not atomic). Recovered 678 valid records from intact sources: preserved prefix (115) + lab files (79) + research shards `data/incoming/research/**/*.jsonl` (524, schema-complete drafts) + staging/other evidence (15) + recusal record. Validated: `verify` OK (621 verified). ~59 previously-integrated canonical records were unrecoverable (source shards consumed); recorded in evidence 0088.
- **New safe consolidation process**: use `consolidate_safe.py` (timestamped `.bak-*` backup + temp file + `os.replace`) — never rewrite `claims.jsonl` in place.
- **M2 (SFT claim_ids)**: 12 ghost claim_ids (`hwa-10.2.8-composer-{join,if-conddep,outputcond,critical,task,runcyclegroup,recovery,onlate,resumecond}-*`) cited by the 34 syntax-rest candidates were repointed to verified lab/official claims; after rework every candidate claim_id resolves to `claims.jsonl` (including 3 orphans post-recovery: fence-0001→fence-validation-0044, limit-cpu-0001→limit-cpu-0074, rest-api-v2-endpoint-0011→rest-v2-port-31116-live-0077).
- **M3 (topic balance)**: 20 new bilingual EDWA/BmEvents candidates (`data/sft/candidates/sft-candidates-edwa-2026-08-18.jsonl`) generated from verified evidence covering bmevents-config, edwa-rules, composer-order, conddep-status, limit-cpu, rest-submit, destructive-cancel, credential-submit, recusal-resumecond, version-awareness. Final candidate corpus: 54 records (27 EN/27 PT).
- **m1**: matrix `vm-9f-0002` EXEC note qualified (official docs use `IF EXEC` in JOIN examples for external job streams; EXEC is not a documented job status condition).
- **m2**: `resumecond` registered as `insufficient_evidence` (`hwa-10.2.8-recusal-resumecond-0001`) and confined to recusal-only SFT use.
- **Orphan re-verification**: all 93 SFT-referenced claim_ids lost in the truncation were re-verified via 4 parallel research batches (Perplexity URL discovery + official-page fetch) and consolidated back; claims.jsonl = 775 valid (718 verified). 9 were recovered from the unified dataset rag_corpus (original verified_claim text/source) and returned to verified; `dwc-mdm-distinct-0008` was upgraded to verified via the official DWC 10.2.0 Release Notes interoperability table. Evidence 0090, 0091.
- **Composer corpus expansion**: 42 official 10.2.8 Composer / job-definition pages downloaded to `data/raw/HCL-HWA-10.2.8/` (composer CLI + all scheduling object definitions + conditional logic/onoverlap/deadline/workflowtrigger); pipeline verdict APROVADO COM RESSALVAS, 211 composer/job-def chunks in train_full, unknown_version_share 0.0104 (evidence 0092).
- **EDWA lab validation (2026-08-19)**: after two WSL reboots the environment was brought back up (startAppServer.sh → conman start MDM → conman startmon MDM/MDMDA + /etc/hosts MDMHOST re-add). Validated end-to-end: **sendevent/GenericEventPlugIn** (Upgrade event → UPDATESUCCESS MessageLogger → AWSMSL101I; uses -sslport 31131, evidence 0093), **TWSObjectsMonitor JobStatusChanged** (rule → monman EIF event → AWSEVP001/007 → AWSMSL101I; Status values are Running/Successful, not SUCC; monman does NOT auto-start after reboot, evidence 0094), and documented the **restart procedure** + `/eventrule/engine` REST 404s + `AWSBIN091E` monitoring-configuration behavior (evidence 0095).

### P13 — Final insufficient_evidence resolution + DWC install corpus (2026-08-19)

- **Final 6 `insufficient_evidence` resolved → 0 insufficient** (evidence consolidated, claims.jsonl = 780 valid | 757 verified | 0 insufficient):
  - `hwa-10.2.8-awsjpl526w-0001` → **verified**: AWSJPL526W is a MakePlan WARNING ("An external dependency in job stream ... cannot be resolved because the matching criteria could not be satisfied"); the planner ignores the job/job stream (e.g. after FOLLOWS) not scheduled for the plan-extension day. Sources: IBM Support page node/7248487 (IWS 10.1.0/10.2.0) + Troubleshooting Guide 10.2.8 (awstrmst.pdf).
  - `hwa-10.2.8-recusal-resumecond-0001` → **verified** negative claim: no `resumecond` keyword/composer-conman-OCLI command in IWS/HWA 8.6/9.2/10.1/10.2.8; documented SUPPR-resumption mechanisms are start conditions, FOLLOWS…IF (SUCC/FAIL/ABEND/SUPPR), conman rerun/release, RECOVERY RERUN. Recusal SFT stays valid.
  - `hwa-lab-10.2.8-adhoc-dynamic-submit-ready-0018`, `hwa-lab-10.2.8-agent-restart-ready-0020`, `hwa-lab-10.2.8-dynamic-agent-dispatch-pending-0011` → **verified** contextual: READY/sem-dispatch tinha causa raiz = **LIMIT 0** pós-instalação em MDMDA; após `conman lc MDMDA;10` o dispatch funcionou (cross-ref `-0027`, `-0036`, `-0064`, `-0048`).
  - `hwa-lab-10.2.8-dwc-not-installed-0049` → **verified** negativo de lab (DWC é componente separado com instalador próprio `dwcinst`; sem imagem no lab, validação GUI pendente).
- **3 new verified DWC 10.2.8 install claims** added: `hwa-10.2.8-dwc-install-0020` (dwcinst script / dwcinst.properties), `-0021` (prereqs WebSphere/Open Liberty + DB, System Requirements KB0125168), `-0022` (default paths /opt/wa/DWC e %ProgramFiles%\wa\DWC; nós master/backup/separados).
- **5 official DWC 10.2.8 pages downloaded** to `data/raw/HCL-HWA-10.2.8/`: awspitypicalfullstack, awspiinstallDWC, awspiinstallDWCupgr, awspidwcinstsyntax, eqqi1dwcprereq.
- **Corpus pipeline re-run**: extract_docs.py regenerated clean corpus (21967 chunks, +50 vs previous 21917); sync_claims_to_corpus.py added 768 verified/community claim chunks; dedup_and_split.py (optimized, candidate cap 1024) → 17443 eligible_full / 16788 train source-holdout / 15381 train. Verdict **APROVADO** (0 critical, 0 warnings), unknown_version_share 0.0101, synthetic_in_training 0, 0 security hits.
- **Fix**: `simulate_dataset_quality.py` security regex false positive (bare `apikey`/`sslpassword`/`wapassword` in prose matched without a flag/`=`); now requires `-` flag for the space-separated form, `=`-form unchanged. (No real credentials in corpus.)

### P14 — Composer SFT + gold/eval cycle (2026-08-19)

- **Composer SFT candidates**: generated `data/sft/candidates/sft-candidates-composer-2026-08-19.jsonl` — **68 bilingual candidates (34 PT / 34 EN)**, 19 composer claims (verified), covering topics composer-add, composer-commands, composer-delete, composer-extract, composer-if-conddep, composer-join, composer-notcommands, composer-onlate, composer-onoverlap, composer-outputcond, composer-recovery, composer-recovery-rerun (lab), composer-runcyclegroup (x2 claims), composer-task (x3 claims), composer-validate (x2 claims). Risk coverage: read_only 40, mutating 20, destructive 8. PT/EN parity per topic. Generated via `C:\Users\User\AppData\Local\Temp\opencode\generate_composer_sft.py`.
- **Validation**: `validate_sft.py` OK (68 candidatos, 19 claims) and `audit_sft_metadata.py` OK (68 registros, claims verified + official sources). No leakage into candidates.jsonl/approved (separate thematic batch, follow-up promote/split step).
- **Gold/eval cycle closed**: `build_eval_gold.py` regenerated `data/sft/eval_independent.jsonl` from 757 verified claims (lab-prefix excluded) → **672 cases (336 PT / 336 EN)**, anti-leak gate active; `validate_eval.py` OK (>=100 cases, >=50 per language). Was 640 cases before P13.
- **Append incident (fixed)**: a naive `open(tmp,'a')` append of evidence 0096 to `claims.jsonl` created a tmp file containing ONLY the new record and `os.replace` truncated the file to 1 record. Recovered from the pre-append backup (`claims.jsonl.bak-20260819-211956`, 780 records) and re-applied the append as a full read+write (780→781). **Rule: never append to claims.jsonl via `open(tmp,'a')`+`os.replace`; always read full file, append in memory, write whole content.** claims.jsonl = 781 valid | 758 verified | 0 insufficient.
- **P14 final state**: corpus re-synced (20086 records, +1 claim chunk), dedup/split → 17444 eligible_full / 16789 train source-holdout / 15382 train, verdict **APROVADO** (0 critical/0 warnings), unknown_version_share 0.0101. Evidence 0096 recorded the composer-SFT + gold pipeline state.

### P15 — EDWA eventrule REST discovery (2026-08-19)

- **Problem (from 0095)**: `/eventrule/engine/*` REST resource classes registered in the Liberty engineServer but direct GET/POST on camelCase paths (`messageLog`, `auditRecord`, `ruleInstance`, `actionRun`, `pluginConfiguration`, `deploy`) returned 404/401.
- **Method**: decompiled the resource classes from `TWSdRESTWeb-SNAPSHOT.war/WEB-INF/classes` (EventRuleEngineApplication, MessageLogRecordEventRuleResource, AuditRecordEventRuleResource, RuleInstanceEventRuleResource, ActionRunEventRuleResource, PluginConfigurationEventRuleResource) using `javap -p -v` + `strings` on `.class` files to extract `@Path` annotations and method signatures.
- **Discovered real subpaths (underscore, NOT camelCase)**:
  - `POST /twsd/eventrule/engine/{message_log_record|audit_record|rule_instance|action_run}/header/query` — **requires `How-Many` header (e.g. 10) + Basic auth wauser**. Returns 200 with JSON array of records (e.g., message_log_record: `{"id":"...000904","eventType":"UPGRADE","ruleName":"UPDATESUCCESS","message":"Update agent MDMDA: Update successfully completed."}`; rule_instance: llrc 903; audit_record: full CONMAN/DATABASE history).
  - `POST /twsd/eventrule/engine/{message_log_record|rule_instance|audit_record|action_run}/header/query_next` — pagination (POST with `QueryEventRuleEngineContext` body + `objectsKeys` + `howMany`).
  - `GET /twsd/eventrule/engine/message_log_record/{messagelogrecordId}` — 200 (header + ruleId UUID).
  - `GET /twsd/eventrule/engine/rule_instance/{ruleinstanceId}` — 200.
  - `GET /twsd/eventrule/engine/action_plugin_configuration` — 200 XML (action definitions).
  - `GET /twsd/eventrule/engine/event_plugin_configuration` — 200 XML (event definitions).
  - `GET /twsd/eventrule/deployment/active_rules` — 200 (`{"listMessages":["AWSJCO119I No event rules are deployed."]}`). **Caveat (P20)**: always reports AWSJCO119I even when 3 rules are ACTIVE (reads deployment config, not real rule state); confirm real state via `composer list EVENTRULE`.
  - `PUT /twsd/eventrule/deployment/rule_builder/{start,stop}` — **PUT, NOT POST** (the original 405 was caused by using POST; contract verified by decompile + live test). Returns 204 No Content; `start` triggers build of pending rules (AWSJCO125I ... ACTIVE). See P20.
  - `POST /twsd/eventrule/engine/action_run/action/run` — declared "POST operation for run a List of ActionRun" but **always HTTP 400 in 10.2.8.00** (NoSuchMethodException: ActionRun.fromJsonList). See P20.
- **Auth**: Basic auth `wauser:padrao` works for these endpoints (WAJWTRequestFilter at application level but LTPA/basic auth passes). The `How-Many` header is `@HeaderParam("How-Many") Integer` — without it the endpoint returns 400.
- **Evidence**: 0097.

### P16 — AWSBIN091E root cause (2026-08-19)

- **Finding**: `GET /twsd/api/v2/plan/workstation/{ws}/action/monitoring-configuration` returns HTTP 500 with `AWSJSY404E` wrapping `AWSBIN091E "The workstation does not support monitoring."` for ALL workstations (MDM, MDMDA, MDMXA, MDM_DWB).
- **Root cause**: confirmed via `conman showcpus` (with correct env: `source tws_env.sh + UNISONWORK=/opt/hwa/TWSDATA`) that **both MDM and MDMDA have the monman flag M** in the Symphony (`MDM ... I J M EA`, `MDMDA ... LBI J M`). The error is NOT caused by lack of monitoring — the REST V2 endpoint reads the monitoring configuration via `readFromScribner` (Symphony plan operation), which is **unsupported for broker-managed workstations**. The event processing, monman, ssmagent EDWA, FileMonitor rules and TWSObjectsMonitor rules all function normally.
- **Caveat**: conman without the correct env (`source /opt/hwa/TWS/tws_env.sh && export UNISONWORK=/opt/hwa/TWSDATA`) tries to open `/opt/hwa/TWS/Symphony` (wrong path) and fails with `AWSBHU001E/AWSBCU035E`; the real Symphony is at `/opt/hwa/TWSDATA/Symphony`.
- **Evidence**: 0098.

### P17 — Plan rollover fix (virada de plano) (2026-08-19)

- **Symptom**: `conman sc` mostrava MDM no dia 08/18/26 enquanto o host já era 08/19/26; o plano não virava de dia. `planman showinfo` mostrava "created or extended with -for 0000", Production plan start of last extension 08/19 03:00, e `sj @#@FINAL@` só tinha a instância `#FINAL 2359 08/17` (SUCC) — nenhuma instância para 08/18→08/19.
- **Root cause (important lesson)**: a virada automática depende do jobstream **MDMXA#FINAL** (`ON RUNCYCLE RC1 "FREQ=DAILY;" AT 2359 CARRYFORWARD` com STARTAPPSERVER → MAKEPLAN → SWITCHPLAN, seguido de MDMXA#FINALPOSTREPORTS com CHECKSYNC/CREATEPOSTREPORTS/UPDATESTATS), definido no produto em `/opt/hwa/TWS/config/Sfinal`. Essas definições **haviam sido removidas do banco na limpeza de objetos de teste (P7b)** — `model/jobstream` count = 0 — então o planner nunca mais criava instâncias de virada e o JnextPlan apenas **estendia** o plano existente (o dia corrente ficava "preso").
- **Fix (official procedure)**:
  1. `composer add Sfinal` (a partir de `/opt/hwa/TWS/config/Sfinal`) → `AWSBIA288I Total objects updated: 2` (FINAL + FINALPOSTREPORTS restaurados). Ref: `awsrgautomateprodplan.html`.
  2. `planman unlock` → `AWSJPL504I The "planner" process unlocked the database` — resolveu o lock que causava `AWSJPL017E The production plan cannot be created because a previous action on the production plan did not complete successfully` (recovery oficial: `ResetPlan -scratch` e/ou `planman unlock`, `awstrjnextplan017.html`).
  3. `JnextPlan` → MakePlan/SwitchPlan/checksync/CreatePostReports/UpdateStats com sucesso; `conman sc` passou a mostrar **MDM RUN 9 DATE 08/19/26 22:00**; `planman showinfo` com Production plan end time **08/20/2026 02:59**; nova instância `MDMXA#FINAL 2359 08/19` HOLD [Carry] no plano — a virada diária automática voltou a funcionar (23:59 gera o plano do dia seguinte).
- **Key facts**:
  - JnextPlan sem argumentos = extensão 24h (default, mesmo efeito de `-for 0000`); para janela explícita use `JnextPlan -for 24:00` / `-days 1` / `-for 48:00`.
  - O FINAL do Sfinal executa MakePlan/SwitchPlan herdando os mesmos argumentos do JnextPlan.
  - Sem o FINAL no banco, NÃO há virada automática — o plano só estende.
  - `planman unlock` é o recovery para AWSJPL017E (lock deixado set após ação anterior incompleta).
- **Evidence**: 0099.

### Quarantine (272→235) and buffer — resolved with validation + redaction (2026-08-19)

- **Sensitive-data redaction**: real company domains/hostnames redacted to placeholders in `corpus.jsonl` and `quarantine.jsonl` — `inbev.com`→`[COMPANY].com`, `orb-data.com`→`[COMPANY].com`, `stlpr160.corp.anheuser-busch.com`/`STLPR160`/`STLPR162_BKM`→`[COMPANY]`/`[HOSTNAME]` (SCRIPT SHELL.pdf + TWS.pdf). Verified 0 remaining hits.
- **Validated via Perplexity + existing `unofficial_validation_results.jsonl`**:
  - `SCRIPT SHELL.pdf` (8 chunks) → **community_practice** (operational monitoring scripts) → promoted with disclaimer.
  - `TWS.pdf` (29 chunks) → **reclassified as community_practice** (local PT operational runbook: restart sequence conman shut/start, twsinst -new -agent fta/both, planman unlock/resync, trace configDropins, datagather). Perplexity validation confirmed the individual commands are official (Troubleshooting Guide 10.2.8, awsrgstartstop, awsrgusingconman, awspiagentparams) but the sequence is team customization → promoted to training with explicit disclaimer.
  - `iws-hwa-10.2-perfreport.pdf` (25) → **verified** official HCL Rome Lab report; stays out of training (`training_eligible: False` — benchmark numbers environment-specific; atomic tuning claims registered separately).
  - `awscertsmst.pdf` (69) → **obsolete** (TWS 8.3–8.6 legacy cert remediation); stays out of training.
  - `awsfab502e` (124) + `tws_ai_knowledge_optimized.md` (17) → **synthetic_unverified**, kept quarantined (AI-generated).
- **Result**: quarantine 272→**235**; 37 community_practice chunks (8 SCRIPT SHELL + 29 TWS.pdf) in train_full with `training_eligible=True`; train representative 15407; pipeline verdict **APROVADO** (0 critical/0 warnings).
- **New claims**: `com-monitoring-scripts-0004` (community), `hwa-lab-10.2.8-corpus-redaction-reclass-0101` (evidence).
- **Buffer 101** = tie-break reservoir (18 community chunks) — intentional, no action.
- **Second pass (2026-08-19) — remaining 235 assessed with Perplexity**: the 94 `internal_operational_unreviewed` are official documents, NOT community practice (`perfreport` = HCL Rome Lab verified report; `awscertsmst` = IBM official cert book, obsolete for 10.2.8) — reclassifying them as "community" would be wrong. The 141 `synthetic_unverified` are AI-generated; the **validated knowledge** they contain was captured as verified claims instead of promoting the raw chunks: `hwa-10.2.8-proc-tree-0001/0002/0003` (netman→mailman→batchman→jobman process tree, batchman autonomous Symphony dependency resolution, FTA autonomy, WebSphere-based processes, port 31111) — verified against awsrgprodproc.html + awsadnetoperations.html + IBM 10.2.2 components. Final state: claims 790 | verified 766 | community_practice 14; train representative 15410; verdict APROVADO. Remaining quarantine (235) stays: synthetic chunks stay quarantined (AI-generated source), official docs stay out of training by design.

### P18 — Destructive cleanup lesson: FINAL jobstreams are system objects (2026-08-19)

- **Critical post-mortem**: the P7b test-object cleanup deleted `MDMXA#FINAL` and `MDMXA#FINALPOSTREPORTS` (the plan-rollover jobstreams from the product's `Sfinal` file) as if they were test orphans (evidence 0083: "3 MDMXA streams (FINAL, FINALPOSTREPORTS, ...) deleted"). This destructive action broke automatic plan rollover (evidence 0099); in production it would stop D+1 plan generation with major impact.
- **Rule**: never `composer delete` system/plan jobstreams (FINAL, FINALPOSTREPORTS, SFINAL, JNEXTPLAN and rollover equivalents) without verifying their role; use an exclusion allowlist and review `composer display` before confirming any delete.
- **Evidence**: 0100 (`hwa-lab-10.2.8-destructive-cleanup-lesson-0100`); 0083 annotated with the warning.

### P19 - Composer SFT batch regenerated with ADU fixes + topic expansion (2026-08-20)

- **ADU review (hwa-dataset-auditor + hwa-sft-builder + Perplexity) of the 68-candidate composer batch (2026-08-19)**: verdict **NEEDS_FIX**. Findings: P1 38/68 prompts embedded the claim verbatim; P2 22/68 answers carried governance metadata (`notes`); P3 6-7 PT mutating/destructive answers without confirmation warning (asymmetric with EN); P4 `recovery-rerun` lab claim attributed to "official documentation" and risk=destructive incorrect; paraphrase family ids colliding; 4 records leaking WSL2 infra in `platform`; missing topics (modify, replace, update, lock, critical, -jwt, display vs list).
- **User decision (2026-08-20)**: regenerate the batch with fixes. Applied:
  - **P1**: scenario prompts per claim (no claim verbatim, no echo).
  - **P2**: answers without notes/governance metadata; only the fact + integrated safety sentence.
  - **P3**: safety warnings symmetric PT/EN on both variants (concept/detail) for mutating/destructive/credential_sensitive.
  - **P4**: honest attribution - `hwa-lab-*` claims say "validado em laboratório HWA 10.2.8 (ambiente de teste)"; others say "documentação oficial". Claim `hwa-lab-10.2.8-recovery-stop-continue-rerun-0038` risk corrected destructive -> mutating (observational lab claim; consistent with `composer-recovery-0001`), atomic write + backup `claims.jsonl.bak-20260820-185152`.
  - **P5**: `claim_family_id = claim-{sha256(claim_id)[:16]}`, `paraphrase_family_id = {fam}-{variant}` (per claim, no collisions), hash-based `record_id`.
  - **P6**: platform normalized (first segment, no WSL2/x86_64/Ubuntu).
  - **P7**: +21 topics (modify, replace, update, lock/unlock, critical x2, -jwt, invocation, display vs list, runcyclegroup naming/AWSBCZ021E, presentation order, vartable, govern write path, official create/validate/lock, version matrix 9.5->10.2, cliauth) - 40 verified claims total, PT nativo for EN-native claims and vice-versa.
- **Result**: `data/sft/candidates/sft-candidates-composer-2026-08-20.jsonl` = **160 candidates (80 PT / 80 EN, 40 claims)**. Old batch archived at `data/sft/candidates/archive/sft-candidates-composer-2026-08-19.NEEDS_FIX.jsonl`.
- **Validations**: `check_composer_fix.py` (P1-P7) PASS; `validate_sft.py` PASS (risks: read_only 92, mutating 52, credential_sensitive 12, destructive 4); `audit_sft_metadata.py` PASS.
- **Pre-existing stale claim fixed**: `hwa-10.2.8-globalopts-0001` -> `hwa-10.2.8-globalopts-enlistsecchk-0001` (same enListSecChk content; claim was consolidated/renamed). Applied to 4 candidates (`candidates.jsonl`, backup `candidates.jsonl.bak-stale-20260820-185617`) and 14 approved records (`approved.jsonl`, backup `approved.jsonl.bak-stale-20260820-185654`). This unblocked `promote_sft.py` (it validates the whole `candidates.jsonl`).
- **Promotion (1st attempt, then rolled back)**: manifest `data/sft/review_manifest_1028_composer_2026_08_20.json` (accepted=160) -> `promote_sft.py` -> approved.jsonl=10383 (sha256 63351820...) -> splits train=7506/val=1980/test=897. **Rolled back** (approved 10383->10223, candidates->2143, splits 7382/1956/885) because the independent audit ran AFTER ingestion and flagged the process gate as bypassed (12 records in test set).
- **Audit #1 (independent, hwa-dataset-auditor + Perplexity + webfetch)**: verdict **REPROVADO** (process: gate bypassed; ALTA P2: 6 PT answers of `hwa-official-*` embedded `Context:` + raw EN quotes from claim text; MÉDIA P6: 16 version-matrix answers cited "10.2.8" for 9.5/9.5FP2/10.2.x claims; MÉDIA: extract `;lock` asymmetric PT/EN; BAIXA P1: 2 composer-add prompts with partial echo).
- **Fixes applied after audit #1**: (a) pt_fact overrides for `hwa-official-composer-10.2.8-0001/0002/0003` (removed `Context:` + EN quotes); (b) `attribution()` now uses the claim's real version ("HCL Workload Automation 9.5:", "9.5 Fix Pack 2:", "10.2.x:", "9.5-10.2.8:"); (c) extract PT fact now includes `;lock ... (mutativo)` (symmetric); (d) composer-add scenarios rewritten (no echo); (e) composer-commands PT fact includes "Composer opera nas definições do banco; conman opera no plano" (PT/EN symmetric); (f) PT accent normalization map (word-boundary) applied to PT facts derived from claims.
- **Audit #2 (re-audit, independent)**: verdict **APROVADO COM RESSALVAS** - 5/5 fix items confirmed resolved; schema/claims/entailment/security/leakage/translation/balance all PASS; leakage vs approved/splits = 0. Residuals: manifest stale (28 regenerated ids) - regenerated; 3 claims confidence=medium; 4 lab records behavioral (labeled); PT orthography fixed.
- **Final promotion (audit-gated)**: batch re-merged to candidates.jsonl (2303) with current ids; manifest regenerated (accepted=160, matches batch 160/160); `promote_sft.py` -> **approved.jsonl = 10383** (sha256 9c196657...) -> `split_sft.py` -> **train=7506 | validation=1980 | test=897** (batch: 124 train, 24 validation, 12 test; 0 missing). validate_sft (approved) PASS; audit_sft_metadata PASS.

### P20 - EDWA REST action/run + rule_builder resolved; Sfinal/startOfDay evidence (2026-08-21)

- **rule_builder start/stop — RESOLVED (was Next Step)**: decompiled `EventRuleDeploymentResource.class` (TWSdRESTWeb-10.2.8.00-SNAPSHOT.war, exploded at `apps/TWSEngineModel.ear/`) → `startRuleBuilder`/`stopRuleBuilder` are annotated **`jakarta.ws.rs.PUT`** on `/rule_builder/start` and `/rule_builder/stop` (the P15 "405, POST expected" was a verb mistake — it's PUT, no request body). Live test: `PUT .../rule_builder/start` → **HTTP 204**; `PUT .../rule_builder/stop` → **HTTP 204**; `PUT .../rule_builder/start` (restore) → 204 and triggered `AWSJCO125I The event rule "UPDATEFAILURE"/"UPDATESTATUS"/"UPDATESUCCESS" has been successfully built. The rule status is set to ACTIVE.` + `OK`. Verified rules remain ACTIVE via `composer list EVENTRULE` (3 rules, active, no draft). State restored after the test.
- **action/run — RESOLVED AS DEFECT (was Next Step)**: decompiled `ActionRunEventRuleResource` + `ActionRunEventRuleResourceServiceImpl.runActions` → `POST /eventrule/engine/action_run/action/run` takes `List<ActionRun>` and calls `EventRuleEngine.runActions` → `ActionPlugInManager.getPlugIn(pluginName)` → `securityOK(actionRun,user,groups)` → `ActionHelper.executeAction(actionRun)` (re-executes the real action: MSGLOG re-logs, TWSAction sbs re-submits job stream, MailSender re-emails). **BUT live POST with a valid MSGLOG ActionRun JSON (record 000905) returns HTTP 400** — `messages.log`: `java.lang.NoSuchMethodException: com.ibm.tws.objects.log.ActionRun.fromJsonList(java.lang.String)` at `ActionRunJsonListProvider.readFrom(ActionRunJsonListProvider.java:71)` (RESTEasy MessageBodyReader invokes a static `fromJsonList(String)` that exists on `ActionRunHeader` but NOT on `ActionRun`; only `fromJson`/`toJacksonBean` exist). Same exception was already present on 2026-08-19. **Conclusion: programmatic EDWA action execution via this REST endpoint is NOT usable in 10.2.8.00 (product defect); no action was re-executed (400 before deserialization completes).** Research (Perplexity, 2026-08-21) confirmed this endpoint is **NOT in the official REST API documentation / Swagger** (official API = `WA_API3_v2.json` model/plan/security + `sendevent`/`evtdef` CLI + composer/DWC) and no HCL fix list/APAR references it — it is an undocumented internal API. **Do not try to fix it via payload** (the provider's `readFrom` reflectively calls `Class.getMethod("fromJsonList")` — no JSON body can avoid it); patching the jar is not supported. **Use the supported path instead: `sendevent` + active rule → action (validated end-to-end in P21).**
- **Working read paths**: `POST /action_run/header/query` (needs `Content-Type: application/json` + `How-Many` header → 200 with ActionRun list e.g. MSGLOG 000917/000905, TWSAction sbs 000868); `GET /action_run/{id}` (200, full ActionRun incl. header/ruleId/ruleInstanceId/parameterMap); `GET /action_plugin_configuration` (200 XML); `GET /event_plugin_configuration` (200 XML); `GET /active_rules` (200).
- **Sfinal confrontation (evidence `lab-validation-2026-08-21-sfinal-confrontation.jsonl`)**: `/opt/hwa/TWS/Sfinal` == `/opt/hwa/TWS/config/Sfinal` (diff: none); `Sfinal2` differs in FINAL dependency (FOLLOWS MDMXA#FINAL.SWITCHPLAN PREVIOUS vs Sfinal2's dependency on FINALPOSTREPORTS.UPDATESTATS); DB objects FINAL/FINALPOSTREPORTS match Sfinal variant; last FINAL run (logs O596375.2359/O596516.2359, 2026.08.20) completed STARTAPPSERVER/MAKEPLAN/SWITCHPLAN/CHECKSYNC/CREATEPOSTREPORTS/UPDATESTATS exit 0 (planman ext + AWSJCL062I + AWSJCL065I run number updated). 2 lab claims + 2 verified official claims + 1 verified change-management claim added.
- **startOfDay (evidence `lab-validation-2026-08-21-startofday-0005.jsonl`)**: `optman chg sd=0005` → AWSJCL050I; `optman ls` confirms startOfDay/sd = 0005; note: takes effect after JnextPlan, no plan regeneration performed (1 lab claim added).
- **Claims**: claims.jsonl 914 → **916** (2 new lab claims: `hwa-lab-10.2.8-edwa-rule-builder-put-0101`, `hwa-lab-10.2.8-edwa-action-run-defect-0102`); evidence `lab-validation-2026-08-21-edwa-rest-action-run.jsonl`; backup `claims.jsonl.bak-20260821-234538`. Atomic write (read full + backup + temp + os.replace).

### P21 - EDWA sendevent -> rule -> sbs end-to-end validated; SSH access established (2026-08-22)

- **SSH access to lab**: sshd runs inside WSL; root generated an ed25519 keypair for `wauser` (`~/.ssh/id_ed25519`, authorized_keys) — `ssh wauser@127.0.0.1` works (key auth, no password). **This avoids the broken `HOME=C:UsersUser` / catopen issues of running TWS commands via bare `wsl -e bash -lc` as root.** Helper pattern: `sudo -u wauser bash -lc "export HOME=/home/wauser; ssh -o BatchMode=yes wauser@127.0.0.1 '<cmd>'"` (or copy a script to `/home/wauser/` and run it via SSH — avoids PowerShell quoting mangling). Always `source /opt/hwa/TWS/tws_env.sh` + `export UNISONWORK=/opt/hwa/TWSDATA` on the remote side.
- **Composer syntax format (deduced by iteration, evidence `hwa-lab-10.2.8-composer-syntax-format-0104`)**: job definitions use `$JOBS` header + `MDMDA#EVTJOB1 / DOCOMMAND "..." / STREAMLOGON / DESCRIPTION / TASKTYPE / RECOVERY`; job streams use `SCHEDULE workstation#name / DESCRIPTION / ON RUNCYCLE RC1 "FREQ=DAILY;" / : / workstation#jobname / END` (jobs must exist as definitions first); event-rule XML must use `<?xml version="1.0"?>` **without encoding attribute** and the `http://www.ibm.com/xmlns/prod/tws/1.0/event-management/rules` namespace (`eventCondition` with `eventProvider`/`eventType` attrs, `scope` as child element, `attributeFilter name/operator/value` predicates, `action actionProvider/actionType/responseType`). Encoding-declared XML → `AWSBIA358E The encoding used is not that of the locale`.
- **End-to-end validation (evidence `lab-validation-2026-08-22-edwa-sendevent-e2e.jsonl`, claim `hwa-lab-10.2.8-edwa-sendevent-e2e-0103`)**:
  1. Created rule `LAB_SENDEVT` (filter, isDraft=no, GenericEventPlugIn Event1, Param1=LAB_TRIGGER + Workstation=MDMDA, action TWSAction sbs MDMDA#EVTJS_TEST) via composer validate/add (`AWSJCL003I`), status `activation pending`.
  2. `PUT /twsd/eventrule/deployment/rule_builder/start` → HTTP 204 → `AWSJCO125I ... LAB_SENDEVT ... ACTIVE` (immediate activation instead of 5-min deploymentFrequency).
  3. First send attempt `sendevent LAB_TRIGGER GenericEventPlugIn Param1=LAB_TRIGGER Workstation=MDMDA` → `AWSGTW113I` but **no match** (`AWSEVP001I ... event type = "LAB_TRIGGER" ... AWSEVP008I did not match any existing event condition`) because the eventType must be the **event name defined in the plugin** (`Event1`), not an arbitrary name.
  4. Correct send: `sendevent Event1 GenericEventPlugIn Param1=LAB_TRIGGER Workstation=MDMDA` → `AWSEVP001I event type = "EVENT1"; scope = "LAB_TRIGGER on MDMDA"` → `AWSEVP007I matched` → `AWSAHL004I instance LAB_SENDEVT triggered` → `AWSAHL002I action sbs started` → `AWSTAP101I The job stream "EVTJS_TEST" has been successfully submitted` → `AWSAHL003I/005I completed` → new ActionRun `id ...1219` (sbs, SUCCESSFUL, `MDMDA#EVTJS_TEST[(0010 22/08/2026),(0AAAAAAAAAAAAAPH)]`) → new plan instance `MDMDA #EVTJS_TEST 0010 08/22 EXEC` (EVTJOB1 WAIT).
  - **This is the supported programmatic path to execute EDWA actions** (vs. the broken internal `action/run` REST endpoint). If actions must fire without waiting, either use `PUT rule_builder/start` to force deployment or set `deploymentFrequency=0` + `planman deploy` (Release Notes 10.2.7 IJ50261 fixed `df=0` honoring).
- **Claims**: claims.jsonl 916 → **918** (`hwa-lab-10.2.8-edwa-sendevent-e2e-0103`, `hwa-lab-10.2.8-composer-syntax-format-0104`); evidence `lab-validation-2026-08-22-edwa-sendevent-e2e.jsonl`; backup `claims.jsonl.bak-20260822-001047`.

### P22 - Composer gap-closing lab validation (2026-08-22)

- **rename**: syntax is `composer rename <type>=<old> <new_without_type> [;preview]` — type prefix only on OLD id; `;preview` on NEW (or separate `PREVIEW` keyword) = dry-run (`AWSJCL558I ... will be renamed`, 0 updated); real rename persists (`AWSJCL003I`, 1 updated) and old object disappears; rename-back restores (rollback OK). Invalid keyword between args (e.g. `to`) → `AWSBIA349E`. Evidence claim `hwa-lab-10.2.8-composer-rename-new-print-0105`.
- **new**: interactive template command — `composer new <type>` opens a template (in install `templates/` subfolder); passing a name arg fails with `AWSBIA003E` (identifier supplied where not required). Supports calendar/domain/eventrule/folder/job/jobstream/parameter/prompt/resource/runcyclegroup/vartable/user/wat/ws/wsclass.
- **print**: `composer print <object>` sends formatted output to the default printer (`lp`); lab without lp fails with `sh: 1: lp: not found`; a fake `lp` in PATH captures the formatted report (banner `HCL Workload Automation(UNIX)/COMPOSER ... Page 1`, table Workstation/Job Stream Name/Valid From/Updated On/Locked By, plus full `SCHEDULE ... END` definition).
- **VARTABLE + caret E2E (key finding)**: vartable syntax `VARTABLE <name> / DESCRIPTION / MEMBERS / var "value" / END`; the job stream MUST declare `VARTABLE <name>` **before** `ON RUNCYCLE` (after → `AWSJOM915E unexpected token VARTABLE`); variable reference in native job `DOCOMMAND` uses **caret `^var^`** — resolved at run time (`echo ^LAB_MSG^ at ^LAB_WS^` → `HELLO_FROM_VARTABLE at MDMDA` in JobManager zip out.log). **`%var%` does NOT resolve in native FTA jobs** (stays literal) — `%var%` is for dynamic-agent/integration variables; caret is the classic product format (awsrgparmdefn `docommand "ls ^MY_HOME^"`). Evidence claim `hwa-lab-10.2.8-vartable-caret-e2e-0106`.
- **prompt/user**: prompts use `$prompt` marker + `name ":text"` (display, no reply) or `"!text"` (no log); without `$prompt` → `AWSBCZ021E`. Users use `username <name> / password "<pwd>" / end`. `conman audit` does NOT exist — justification/audit trail lives in DB views. Evidence claim `hwa-lab-10.2.8-composer-prompt-user-0107`.
- **JWT / lock**: `composer -jwt <token>` (token from DWC) — invalid token rejected server-side (`AWSITA400E` wrapping `AWSITA238E user not authorized`); real JWT needs DWC (not installed). `composer lock` → `AWSBIA307I`; display shows `Locked By: <user>`; unlock → `AWSBIA308I`; same-user relock/add allowed (effective blocking is cross-user); `extract ... ;lock` requires lock ownership. Evidence claim `hwa-lab-10.2.8-composer-jwt-lock-0108`.
- **Claims**: claims.jsonl 918 → **922** (`-0105` rename/new/print, `-0106` vartable-caret, `-0107` prompt/user, `-0108` jwt/lock); evidence `lab-validation-2026-08-22-composer-gaps.jsonl`; backup `claims.jsonl.bak-20260822-004423`.
- **SFT policy note**: the 4 new lab claims are `observed_in_lab` and therefore NOT eligible for positive SFT (validate_sft.py requires `status=verified`). Lab evidence stays as evidence. **Gap closed 2026-08-22**: verified-official claims were created for composer `rename` (0001-0003), `new` (0001), `list`/`print` (list-print-0001, list-0002), `prompt` (0001), `user` (0001) and `parm-caret` (0001) — all 9 facts confirmed by `hwa-source-verifier` against current official HCL 10.2.8 docs (evidence `official-verification-2026-08-22-composer-verified.jsonl`); claims.jsonl 922 → **931** (backup `claims.jsonl.bak-20260822-012307`). SFT generated: `sft-candidates-composer-verified-2026-08-22.jsonl` (**36 candidates, PT=18/EN=18, 9 claims, validated OK**) + `sft-candidates-composer-vartable-2026-08-22.jsonl` (4 candidates, vartable-0005). Key doc facts validated in lab too (rename preview, caret var, prompt/user formats).
- **Promotion (audit-gated) 2026-08-22**: independent audit of the 40-candidate batch (hwa-dataset-auditor role) → **APROVADO COM RESSALVAS** (6/6 dimensions PASS). Residuals resolved BEFORE promotion: (1) typo `..Essa`/`..This` fixed; (2) isdefault detail added to claim `vartable-0005` + corroborating source; (3) run-on attribution normalized (`10.2.8. o` → `10.2.8: o`, `documentation. the` → `documentation: the`); (4) `rename-0001..0003` + `new-0001` reclassified `read_only`→`mutating`/`guided_action` (they write the DB; claims.jsonl backup `claims.jsonl.bak-20260822-021449`, 20 candidate records refreshed). Merged 40 → `candidates.jsonl` 2305→2345 (backup `candidates.jsonl.bak-20260822-020850`); manifest `review_manifest_1028_composer_verified_2026_08_22.json` (accepted=40); `promote_sft.py` → **approved.jsonl 13067→13107** (sha256 `2e7fcc66...`); `split_sft.py` → **train=9538 | validation=2424 | test=1145** (batch: 32 train / 8 validation / 0 test). validate_sft(approved) PASS; audit_sft_metadata PASS. **Note**: `validate_sft.py` remains valid for the whole approved set; claims count grew 922→931 but 2 were added as `observed_in_lab` earlier and 9 verified now — eval gold should be regenerated (README: run `build_eval_gold.py` + `validate_eval.py` after claim changes).

### P23 - Composer lock contention cross-session reproduced (2026-08-22)

- **Problem**: claim `hwa-lab-10.2.8-composer-jwt-lock-0108` documented same-user lock/unlock but left OPEN: "cross-user lock contention not reproduced (no second login identity)".
- **Key finding — lock identity is (username, session)**: official doc `awsrglocksection` states locks are acquired by `username` + `session` (env `TWS_SESSION`); in batch mode the default session value is the connecting username. Therefore **two shells/sessions of the SAME OS user behave as concurrent identities** — no second login needed. Lab used `TWS_SESSION=ALPHA` vs `TWS_SESSION=BETA`.
- **Cross-session lock rejected**: `TWS_SESSION=BETA composer "lock js=MDMDA#EVTJS_TEST"` while ALPHA holds it → **`AWSJCL006E The object "js=..." cannot be locked because it is already locked by the following user "wauser" in another session.`** (AWSBIA286E Total errors: 1; locked: 0). Display from BETA still shows the object with `Locked By: wauser` (read-only access).
- **Cross-session writes blocked while locked**: replace (`echo y | add <file>`) on a locked object → validation `errors 1`, `AWSBIA288I Total objects updated: 0`; `delete` → `AWSBIA286E`, `deleted: 0`. Definition remained unchanged (DESCRIPTION intact). This matches doc: "any other user has read only access until the object is released or explicitly unlocked".
- **After unlock the same write succeeds**: `TWS_SESSION=ALPHA composer "unlock ..."` → `AWSBIA308I`; then `echo y | TWS_SESSION=BETA composer "add <mod file>"` → **`AWSJCL003I update` completed, 1 updated**, DESCRIPTION persisted as `MODIFIED-BY-BETA` — proving the lock was the blocking factor, not syntax/authorization.
- **Second OS identity not required — but DB user definitions are not composer logins**: `composer -username LABSECOND -password "..."` fails server-side with `AWSBIA389E` wrapping `AWSITA400E`/`AWSITA238E user not authorized` — a DB userdefn is NOT a composer login identity (server rejects it). This confirms the original 0108 note.
- **Evidence**: `lab-validation-2026-08-22-composer-lock-contention.jsonl`; claim `hwa-lab-10.2.8-composer-lock-contention-0109`; claims.jsonl 931 → **932** (backup `claims.jsonl.bak-20260822-025957`). Test objects `MDMDA#EVTLOCKJ`/`MDMDA#EVTJS_LK1` created and cleaned up (DB restored).

### P24 - Conman sj wildcard patterns and start restriction validated; claims + SFT generated (2026-08-22)

- **Corpus gap analysis**: after inserting 3 JOBSELECT/wildcard chunks (1885-1887), a validation run against the live lab confirmed gaps remained in the dataset's teaching examples:
  - `sj @#@.@` (list all jobs across all workstations) — **absent from SFT/corpus teaching examples**
  - `sj workstation#@.@` (filter jobs by specific workstation with wildcards) — **absent from corpus**
  - `@` as wildcard in job selection context — **only present in dependency/security contexts, never in showjobs**
  - `start` command restrictions (agents/pools/brokers don't support `conman start`) — **documented but not taught as restriction**
- **Lab validation (re-executed from conversation transcript, 2026-08-22)**:
  - `sj @#@.@;keys` → listed jobs from MDMDA and MDMXA (STARTAPPSERVER, MAKEPLAN, SWITCHPLAN, EVTJOB*, etc.) — **confirmed working**
  - `sj MDMDA#@.@;keys` → listed only MDMDA jobs (ADHOC_*, CPLX_EVERY, FAIL_*, PRIO_*) — **confirmed workstation filtering works**
  - `conman start MDM` → "MDM already active." on master CPU — **confirmed working**
  - `conman start <agent_ws>` → "the workstation is agent, where the command is not supported" — **confirmed restriction**
- **Official verification (HCL 10.2.8 docs)**:
  - Wildcards page (`awsrgwildcards.html`): `@#@.@ Filters on all jobs in job streams defined in the root (/) folder`; `@` replaces one or more alphanumeric characters, `?` = one char, `%` = one numeric
  - Running commands page (`awsrgcomsyn.html`): `sj sked1(1100 03/05/2023).@+state=hold~priority=0;info;offline` — selects all jobs in a job stream with state/priority filter
  - `start` page (`awsrgstart.html`): "This command is not supported on remote engine workstations"; `start` requires `start` access and must not run during JnextPlan/stageman
- **Claims**: 4 new verified claims added: `hwa-10.2.8-showjobs-wildcard-all-jobs-0110`, `hwa-10.2.8-showjobs-wildcard-ws-filter-0111`, `hwa-10.2.8-showjobs-wildcard-at-0112`, `hwa-10.2.8-conman-start-restriction-0113` — all `status=verified`, `evidence_tier=official_primary/official_corroborated`, with official source quotes + lab validation as corroboration. claims.jsonl 932 → **936** (backup `claims.jsonl.bak-20260822-110216`).
- **Evidence**: `lab-validation-2026-08-22-sj-wildcard-start.jsonl` (6 test records).
- **SFT candidates**: 12 sj-wildcard candidates (3 claims, 2 languages, 2 variants) + initially 4 start-restriction candidates merged under sj-wildcard batch; **later replaced (2026-08-22 P24fix)**: the 4 weak start-restriction records were removed from both candidates and approved, and replaced with 12 stronger scenarios (6 PT/6 EN) teaching the restriction explicitly: agent-type rejection, broker/pool rejection, supported types (MDM/FTA), error message interpretation, contrast with StartUpLwa.sh, FTA startup, and cross-type comparison. Audit-gated promotion: APROVADO (12/12, 0 errors). Final approved: **13.131** (-4 weak +12 strong = net +8). Splits: train=**9.554** | val=2.432 | test=1.145.
- **Corpus chunks**: 3 JOBSELECT/wildcard chunks (1885-1887) already inserted as corpus fix (separate operation, see session record).

### P25 - Job creation vs dataset validation: 10 gaps closed with claims + SFT (2026-08-22)

- **Coverage audit (dataset as manual vs lab)**: attempt to create job defs, complex job streams, ad hoc submission, and validate execution against the live lab revealed 80% coverage plus 10 gaps.
- **Subtle gaps (dataset misleading, lab confirmed)**: composer `new` is interactive (no name arg, AWSBIA003E); EVERY positioning matters (must be inside ON RUNCYCLE parentheses); `at=absolute` required when MDM uses enLegacyStartOfDayEvaluation+enTimeZone (else AWSBHU141E); submit syntax requires `=` (`sbj = job` not `sbj job`).
- **Hard gaps (6) confirmed in lab**: (A) job stream name max 16 bytes (AWSBHW007E); (B) keyword order mandatory - RECOVERY before PRIORITY (AWSJOM915E); (C) VARTABLE must precede ON RUNCYCLE (AWSJOM915E); (D) `into=` requires stream instance IN THE PLAN, not just DB (job disappears otherwise); (E) ad hoc without `into=` goes to default JOBS stream and carries to next day after JnextPlan; (F) TASK JSDL schema validation (AWSJCS029E on invalid JSON).
- **Claims**: 10 new verified claims (0114-0123): js-name-limit, keyword-order, vartable-position, submit-into-plan, submit-adhoc-into-joins, jsdl-validation, every-position, at-absolute, new-interactive, and **conman-start-unified-0123** (merges syntax + type restriction into one claim to fix the "start sem restrições de tipo" gap: works ONLY on MDM/FTA, NOT agents/brokers/pools; use StartUpLwa.sh locally). claims.jsonl 936 → **946** (backup `claims.jsonl.bak-20260822-135806`).
- **Evidence**: `lab-validation-2026-08-22-job-creation-gaps.jsonl` (8 records).
- **SFT**: 26 candidates generated (13 PT / 13 EN, 10 claims), audited APROVADO (0 errors), promoted → **approved.jsonl 13.131 → 13.157** (sha256 `87f6b00a...`); splits train=9.554→**9.576** | val=2.432→2.434 | test=1.145→1.147. validate_sft (approved) PASS. Eval gold regenerated: **3.164** cases (validate_eval PASS).
- **Analysis doc**: `knowledge/analysis/dataset-quality-validation.md` (referenced by user; not present in this workspace path).

### Next Steps

- **[DONE 2026-08-22] Lacuna `into=` multi-instância + API key do ocli validada (P29)**: (1) lacuna `into=JOBS` com múltiplas instâncias resolvida — formas oficiais `into=STREAM(hhmm[date])` (recomendada) e `into=jobstream_id;schedid` (separador `;`); `schedtime=` não é keyword de `sbd`; claim `-0130` + chunks 2376/2377 + 2 SFT records; (2) claims 0131-0134 fechadas (at= nextday, until/deadline, runcycle, follows-hold) com chunks 2378-2383 + 6 SFT records; claims.jsonl 956→957; (3) **API key do ocli gerada e validada de ponta a ponta**: senha `{aes}` decriptada via `DecryptAES.java` + `KeyStringResolver` customizado (chave `1786984332` → `padrao`), `POST /twsd/api/v2/apikey` → JWT, config.yaml `connection.jwt`, contextroot `/,/twsd/cli`, workstation MDM, editor fake → job `OCLI_TESTE_05` criado (AWSMRP001I). Splits: train 9598 / val 2438 / test 1147, eval_independent 3190.
- **[DONE 2026-08-23] Adjudicação PRIORITY em $JOBS + contrato FC contextual (P31)**: (1) **16 pares de contradição adjudicados** (`data/evidence/contradiction_adjudications.jsonl`, 17 registros): 15/16 = `both_scope` (falsos positivos do detector de polaridade/prescrição); par real `0115` vs `0124` → `0124 wins` + `0115 needs_revision`. (2) **Claim 0115 corrigido**: reescrito para não implicar PRIORITY como keyword $JOBS válida (PRIORITY apenas em $SCHEDULES, sbj, chgjob). (3) **4 SFT quarentenados** (`data/sft/quarantine_priority_in_jobs.jsonl`) que ensinavam PRIORITY em $JOBS; `approved.jsonl` 14.892 → 14.888; splits regenerados 10.886/2.658/1.344. (4) **Bug do `contradiction_gate.py` corrigido**: backlog filtra pares adjudicados; `--require-adjudication` PASS com 0 pendentes. (5) **Contrato FC evoluído**: refusal_schema adiciona `origin_not_allowed`, `version_not_supported`, `missing_required_parameter`, `invalid_parameter`; `validate_function_calls.py` aceita recusas contextuais em ações habilitadas; `expand_function_calling.py` → 82 candidatos PT + 82 EN (16 positivos + 66 recusas). Validadores TODOS PASS. Release final: `data/releases/r17-sota-20260823-124416/` (approved 14.888, re-hash PASS).
- **[DONE 2026-08-23] Release SOTA P0-P6 (P30)**: release imutável `data/releases/r17-sota-20260823-114436/` com manifesto SHA-256 (15 artefatos; re-hash PASS) via `release_snapshot.py`; `config.yaml` aponta `sft.approved_file` para o snapshot (treino nunca lê approved mutável); gate de regressão `regression_gate.py` PASS (baseline→final sem queda em idioma/versão/risco/tópico/fonte). P1: blind eval `data/eval/blind_eval_seed.jsonl` (320 casos, 9 famílias, 4 métricas) + runner. P2: contrato RAG evidence-first `docs/RAG_EVIDENCE_CONTRACT.md` + `validate_rag_contract.py` (R1-R5). P3: formato lab `docs/LAB_SESSION_FORMAT.md` + fontes oficiais em `data/incoming/official_sources_*.jsonl` (REST v2, Troubleshooting 10.2.8). P4: `generate_behavioral_scenarios.py` → 904 PT + 904 EN candidatos validados para 181 claims de cobertura baixa; ablação `ablation_report.py` (0 vazamento, 167 claims elevadas a 3+); decisão de promoção PENDENTE (pós-treino). P5: `expand_function_calling.py` → 39 PT + 39 EN candidatos validados. P6: `contradiction_gate.py` → 16 pares pendentes (inclui 0115 vs 0124 PRIORITY em $JOBS); `support_matrix.py` (1152 claims); holdout PT/EN ≈50/50 por fonte. Docs: `docs/PRD_SOTA_RELEASE.md`, `docs/SPEC_SOTA_RELEASE.md`, `docs/PLAN_SOTA_RELEASE.md`, `docs/DECISIONS_SOTA_RELEASE.md`.
- **[DONE 2026-08-22] Ultra-SOTA training/evaluation harness audit (P27)**: `ultra_sota_harness.py all`, `build_eval_gold.py`, `split_sft.py`, `validate_evidence.py`, `validate_sft.py --require-risk-coverage`, `validate_eval.py`, `validate_opencode_assets.py`, `audit_dataset.py`, `simulate_dataset_quality.py`, `test_preflight_parsers.py`, `validate_tokens.py`, `train_lora.py --dry-run` e `train_sft.py --dry-run` executados com sucesso; todos os 86 scripts Python compilam. Corrigidos: suporte explícito a `observed_in_lab`/`lab_observation`, falso positivo de IP em versões 10.2.8.00, arquivos vazios em `validate_tokens.py` e dry-run seguro de `train_lora.py`. Evidência: harness PASS, quality report APROVADO, tokens sem truncamento, 14/14 preflight.
- **[DONE 2026-08-22] Corpus reconciliation + splits + lab_validation (P26)**: (1) chunk 1887/1886 reconciliados com semantica oficial de "root (/) folder" (o padrao `@#@.@` cobre apenas job streams da pasta raiz; para todas as pastas usar `@#/@/@.@`) — antes dizia "broadest possible selection" sem escopo; (2) splits do corpus regenerados via `dedup_and_split.py` (train_full 17.150 / train 14.997 / eval 2.090 / buffer 63; source-holdout 16.526/624) — chunks 1885-1887 agora presentes em train_full/eval/source-train; o chunk 1885 corrompido por artefato de extracao no corpus_full.jsonl foi substituido pela versao limpa; (3) `lab_validation` adicionado as claims 0118/0120/0121 (todas as 10 gap claims 0114-0123 agora tem rastreabilidade lab). Eval gold regenerado: 3.164. validate_sft/validate_eval PASS no WSL.
- **[DONE 2026-08-22] Job creation gaps (P25)**: 10 verified claims (0114-0123) incl. unified start (syntax+restriction), 26 SFT candidates promoted, approved 13.131→13.157, eval gold 3.164. Lacunas A-F + subtis fechadas.
- **[DONE 2026-08-22 fix] conman start restriction reinforced**: 4 weak records substituídos por 12 fortes; depois claim unificada 0123 (sintaxe+restrição em um claim) + 4 SFT records. Lacuna "start sem restrições de tipo" resolvida em definitivo.
- **[DONE 2026-08-22] sj wildcard patterns and start restriction claims + SFT**: 4 verified claims (0110-0113), 12 sj-wildcard SFT candidates, lab evidence logged. See P24.
- **[DONE 2026-08-21] EDWA REST action/run**: `POST /eventrule/engine/action_run/action/run` tested → **HTTP 400 always** (NoSuchMethodException `ActionRun.fromJsonList` — product defect in 10.2.8.00, see P20). No ActionRun was re-executed.
- **[DONE 2026-08-21] rule_builder start/stop**: `PUT /eventrule/deployment/rule_builder/{start,stop}` → HTTP 204 (contract is PUT, not POST; 405 in P15 was verb mistake). `start` triggers build of pending rules (AWSJCO125I). State restored to ACTIVE.
- **[DONE 2026-08-21] Monitor 23:59 FINAL run**: FINAL cycle of 2026.08.20 confirmed executed successfully (logs O596375.2359/O596516.2359: MAKEPLAN/SWITCHPLAN/CHECKSYNC/CREATEPOSTREPORTS/UPDATESTATS exit 0; evidence `sfinal-confrontation-0003`). Plan rollover from 08/20 confirmed in P17/P20 evidence.
- **[DONE 2026-08-22] sendevent -> rule -> action programmatic path validated**: end-to-end proof that EDWA actions run programmatically via `sendevent Event1 GenericEventPlugIn Param1=... Workstation=...` + active rule (sbs submitted EVTJS_TEST; see P21). Alternative to the broken internal `action/run` REST endpoint.
- **[DONE 2026-08-22] SSH access to lab**: key-pair auth as wauser established (avoids WSL-as-root env issues).
- **[DONE 2026-08-22] Composer gap-closing (P22)**: rename/new/print validated; vartable+caret E2E (job var resolution); prompt/user defs; JWT invalid-token rejection; lock/unlock + Locked By. Claims 922.
- **[DONE 2026-08-22] sendevent -> rule -> action programmatic path validated**: end-to-end proof that EDWA actions run programmatically via `sendevent Event1 GenericEventPlugIn Param1=... Workstation=...` + active rule (sbs submitted EVTJS_TEST; see P21). Alternative to the broken internal `action/run` REST endpoint.
- **[DONE 2026-08-22] Composer lock contention cross-session (P23)**: lock identity = (username, TWS_SESSION); cross-session lock → `AWSJCL006E`; cross-session replace/delete blocked while locked, succeed after unlock; DB userdefs are NOT composer login identities (`AWSITA238E`). Claim `-0109`, claims 932.
- **[DONE 2026-08-22] verified claims for composer rename/new/list/print/prompt/user/parm**: 9 claims verified (hwa-source-verifier, official HCL 10.2.8) + SFT 36 candidates + vartable 4 candidates. Claims 931.
- **[DONE 2026-08-22] Audit-gated promotion of 40 composer SFT records**: independent audit PASSED (residuals resolved), approved 13067→13107, splits train=9538/val=2424/test=1145 (0 new in test). Next: regenerate eval gold (`build_eval_gold.py` + `validate_eval.py`).
- **OPEN**: real JWT generation needs DWC (not installed — GUI validation pending); Postgres audit views not queried (no credentials).

### P32 — Rodada 8: ocli kill/release + link/unlink + startmon/stopmon + certman + classificação de práticas comuns não validadas (23/08, madrugada)

- **Objetivo**: atacar o `sensitive_revalidation_backlog` (154 claims sensíveis reprovadas no `--require-corroboration`). Resultado: **103/154 resolvidas** (lab_validation ou corroboração curada) + **51 classificadas como `common_practice_unvalidated`** (política aprovada) → **backlog ativo zerado** (154 → 0 em `sensitive_revalidation_backlog`, movidas para `common_practice_unvalidated` no relatório).
- **Migração em massa**: `scripts/migrate_lab_validation_backlog.py` — 45 claims com evidência lab em arquivos mas campo vazio → `lab_validation` populado (gap de rastreabilidade histórico).
- **Corroboração curada (sem fuzzy!)**: `scripts/apply_curated_corroboration.py` + `apply_curated_corroboration2.py` — mapas manuais claim→claim lab; 35+19+2 aplicadas, 9 tênues revertidas (incidentes de troubleshooting não são cobertos por claims lab de mecanismo).
- **Validações lab novas (evidência `lab-validation-2026-08-23-r8-ocli-conman-ops.jsonl`)**:
  | Comando | Teste | Resultado |
  |---|---|---|
  | `ocli plan kill` | `ocli plan kill MDMDA#JOBS.R8KILL1` (job sleep 300 em EXEC) | Command forwarded → job **ABEND RC 143 (SIGTERM)** — confirma claim ponta a ponta |
  | `ocli plan release job` | sintaxe real **`job=<nome>` com `=`** | `release job=MDMDA#JOBS.R8REL2` → Command forwarded → job SUCC RC 0 (libertou dependência de tempo `at=2359`); sem `=` → AWSMSL018E "dependency does not exist" |
  | `conman link` (lk) | `lk MDMDA;noask` | **AWSBHU158E** — não suportado em agent/pool/broker/remote engine (confirma claim); `lk MDM;noask` → AWSBHU072E |
  | `conman startmon/stopmon` | `startm MDMDA` / `stopm MDMDA` | **AWSBHU470I** "A startmon/stopmon command was issued for MDMDA" (aceito e encaminhado, restart ok) |
  | `certman verify` | `certman verify -inpath /opt/hwa/TWSDATA/ssl/depot -keypasswd dummy` | help confirma sintaxe `-inpath/-keypasswd/-minkeysize/-workdir`; execução validou chain (WACERT021I) e senha errada (WACERT030E) |
  | `certman extract` | `certman extract -help` | sintaxe `-outpath/-storepasswd/-agentscope/-wauser/-wagroup` confirmada; **-wauser/-wagroup requeridos em UNIX** |
- **Descobertas de sintaxe**:
  - `sbd`/`sbj` **não aceitam `hold=`** (AWSBHU039E — keywords aceitas: NEEDS/OPENS/PROMPT/FOLLOWS/AT/UNTIL/EVERY/PRIORITY/CONFIRMED/RECOVERY/STREAMLOGON/INTO/...)
  - `ocli plan kill` aceita formato `MDMDA#JOBS.NOME`; `ocli plan release job` exige `job=NOME`
  - `ocli plan show --job` → AWSMCP025E "not supported" no ocli 2.1.6.0 (só `plan kill/release` funcionam com o formato acima)
- **Validador atualizado** (`validate_evidence.py`): `validation_scope=common_practice_unvalidated` e `lab_validation` satisfazem o gate de corroboração em claims sensíveis; campos `preconditions/impact/reversibility/stop_criterion` adicionados às 5 claims composer CRUD (0135-0139) que os tinham faltando.
- **Relatório**: `ultra_sota_report.json` — `sensitive_revalidation_backlog` 154→**0**; nova seção `common_practice_unvalidated` (51) com rationale por grupo (DWC não instalado, install/upgrade/TLS, security/credenciais, incidents, cross-version).
- **Backups**: `claims.jsonl.bak-20260823-*` (labmig, corroborate, weakfix, corrob2, corrob2b, r8lab, r8certman, scope, secfields) + `ultra_sota_report.json.bak-20260823-005747-scope`.
- **Claims**: 1.006 totais; **92 com lab_validation** (era 39 no início do dia); 51 `common_practice_unvalidated`; validadores todos PASS (default e --require-corroboration).

## References

- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstparams.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiagentparams.html`
- `https://help.hcl-software.com/workloadautomation/v101/distr/src_ref/awsrgautomateprodplan.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgJnextPlan.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgplrstplan.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrglimitcpu.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgfence.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgeverygen.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgvtabledefn.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgjsdefn.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsubmitjob.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgsubmitdocommand.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgresource.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsisnetvbmevents.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsisitmtepevents.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgevntrulemgmntproc.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgfilemonitorevents.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgeruledef.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgtwsaction.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgmessagelogger.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_ref/awsrgstartstop.html`
- `https://help.hcl-software.com/workloadautomation/v101/distr/src_ad/awsadconftwsag.html`
- `https://www.ibm.com/support/pages/node/7248487`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitypicalfullstack.html`
- `https://help.hcl-software.com/workloadautomation/v1028/zos/src_inst/eqqi1dwcprereq.html`
- `https://help.hcl-software.com/workloadautomation/v1027/distr/src_pi/awspidwcinstsyntax.html`
- `https://support.hcl-software.com/csm?id=kb_article&sysparm_article=KB0125168`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_tr/awstrjnextplan017.html`

## P33 — Rodada 9: Runbooks de error codes AWS* + escopo z/OS (2026-08-23)

**Objetivo**: fechar o gap de claims de runbook (formato Sintoma→Causa→Resolução) para códigos de erro AWS* observados no lab, e fixar a política de escopo (z/OS fora do dataset).

**Decisão de escopo (Adriano)**: o dataset cobre **apenas HWA Distributed 10.2.8**. Mensagens EQQ* pertencem ao HWA for Z (z/OS) e **não** devem virar claims (a claim `hwa-10.2.8-eqq199e-distributed-0001` documenta a fronteira). As 3 claims EEL* (agente→z/OS) são mantidas como fronteira. O gap real de error codes é **AWS*** (99 códigos distintos nas claims, 85 observados no lab).

**lab_validation adicionado a 5 incidents existentes** (evidência lab já existia nos arquivos, campo estava vazio):
- `incident-bhu152e-0018` (AWSBHU152E múltiplas instâncias) → into=JOBS vs into=JOBS(0300 08/22)
- `incident-bhu025e-0019` (AWSBHU025E ID com #) → into=JOBS#CF26233... rejeitado
- `incident-jom915e-0020` (AWSJOM915E keywords fora de ordem) → RECOVERY/PRIORITY/VARTABLE
- `incident-jco032e-0021` (workstation inexistente) → TEST_AGENT → AWSJCO032E
- `incident-mrc019e-0022` (contextroot ocli) → /twsd sozinho → AWSMRC019E

**5 claims de runbook NOVAS (0033-0037)** com lab_validation real + chunks sintéticos (2384-2393):
| Claim | Código | Descoberta |
|---|---|---|
| `incident-bhu510e-0033` | AWSBHU510E | sbj duplicado → rerun ou alias (hold= não é keyword de sbj) |
| `incident-msl018e-0034` | AWSMSL018E | ocli release job exige `job=` com '=' (falso "dependency does not exist") |
| `incident-bhu158e-0035` | AWSBHU158E | link/unlink restrito a FTA/master; agents dão AWSBHU158E |
| `incident-bhu470i-0036` | AWSBHU470I | startmon/stopmon: confirmação informativa, não erro |
| `incident-jcl015w-0037` | AWSJCL015W | composer add/replace de objeto existente/locked → 0 updated |

**Propagação**: claims 1011 (102 com lab_validation); chunks +10 em corpus (21.813), corpus_full/train_full/eligible (17.172), train_source_holdout (16.548), eval_buffer (85); approved 13.811, candidates 3.049; SFT splits train 10.071 / val 2.514 / test 1.226; eval_independent regenerado 3.424 (build_eval_gold com anti-leak, +20 casos).

**Validação**: validate_evidence PASS (2 modos, 0 warnings), validate_sft PASS, validate_generic_prompts PASS (0/16.860), validate_eval PASS, audit_dataset PASS, JSON 0 erros.

**Backups**: `claims.jsonl.bak-20260823-r9-pre`, `eval_independent.jsonl.bak-20260823-r9`.

**Lições**: (1) claims `verified` exigem source_url oficial — usar a URL da claim correspondente + lab_validation; (2) claims mutating exigem preconditions/impact/reversibility/stop_criterion no gate --require-corroboration; (3) o gap real de "error codes" é AWS*, não EQQ*/EEL* (z/OS fora).

## P34 — Rodada 10: Performance config-level validada + expansão AWS* (2026-08-23)

**Objetivo**: (1) validar no lab as claims de performance config-level (opções globais testáveis via optman); (2) expandir cobertura de error codes AWS* com apoio de pesquisa Perplexity Direct (MCP).

**Frente 1 — Performance config-level (lab real)**:
- `optman ls` no lab 10.2.8.00 confirmou os defaults de 6 opções globais de performance: `statsHistory/sh=400`, `workstationLimit/wl=100`, `deploymentFrequency/df=5`, `logCleanupFrequency/lc=5`, `logHistory/lh=10`, `enEventDrivenWorkloadAutomation/ed=YES`
- **Controle positivo**: `optman chg sh=401` → `AWSJCL050I Command "chg" completed successfully`; `optman ls` confirmou sh=401; `optman chg sh=400` restaurou (AWSJCL050I de novo)
- Evidência: `lab-validation-2026-08-23-r10-perf-config.jsonl`
- **lab_validation aplicado em 6 claims capacity** (0002, 0003, 0004, 0005, 0007, 0008) — eram 35 claims capacity/perfreport sem nenhuma validação lab

**Frente 2 — Expansão AWS\* (pesquisa Perplexity Direct)**:
- 8 pesquisas perplexity via MCP (script `pplx_query.py` no servidor perplexity-direct): AWSJPL018E, AWSJOM179E, AWSDEQ024E, AWSJCO135W, AWSJSY404E, AWSBIN091E, AWSJDB801E, AWSJPL526W — todas com fontes oficiais HCL/IBM
- **4 claims novas**:
  | Claim | Código | Tipo |
  |---|---|---|
  | `incident-jsy404e-0038` | AWSJSY404E | RUNBOOK Symphony recovery (procedimento oficial: parar agent, deletar Symphony, copiar Sinfonia do master, relink; lock → stageman/planman) — gap real (só aparecia como contexto REST) |
  | `message-jcl050i-0039` | AWSJCL050I | optman chg confirmação (lab) |
  | `message-jdb402e-0040` | AWSJDB402E | cleanup objetos (lab) |
  | `message-bdd003e-0041` | AWSBDD003E | BmEvents config (lab) |
- **3 claims trouble enriquecidas** com notas perplexity (AWSJPL018E, AWSJOM179E, AWSDEQ024E)
- Teste lab de AWSJPL526W (FOLLOWS de stream inexistente) → composer rejeitou com AWSBCZ021E (sintaxe: FOLLOWS precisa de contexto de job; AWSJPL526W é do MakePlan, não do composer) — mantida como verified com doc IBM

**Propagação**: claims 1015 (111 com lab_validation); chunks +8 (2394-2401) em 6 arquivos (corpus 21.821); SFT +8 records (approved 13.819, candidates 3.057); splits train 10.079/val 2.514/test 1.226; eval_independent regenerado 3.440 (+16 casos).

**Validação**: todos PASS (evidence 2 modos 0 warnings, sft, generic 0/16.868, eval 3.440, audit).

**Backups**: `eval_independent.jsonl.bak-20260823-r10`.

**Lições**: (1) corroborating_sources aceita apenas claim_id, não arquivos de evidência — apontar para a claim lab correspondente; (2) claims verified exigem source_url oficial — usar catálogo de mensagens (awsmspar.html) + corroboração lab; (3) AWSJPL526W não é reproduzível via composer (é do MakePlan); (4) a expansão AWS* mostrou que a maioria dos 99 códigos JÁ tem claim (incident/trouble/message) — o valor estava em lab_validation + runbook dos gaps reais (AWSJSY404E Symphony).

## P35 — Rodada 11: localopts de performance + runbooks AWSBCZ021E/AWSJCL521E/AWSBCV012E (2026-08-23)

**Objetivo**: (1) validar no lab as claims de localopts de performance (jm job table size, mm cache size) — os próximos candidatos naturais da Frente performance; (2) criar runbooks para os códigos de erro restantes com apoio Perplexity.

**Frente 1 — localopts de performance (lab real)**:
- Localizado `/opt/hwa/TWSDATA/localopts` (não `/opt/hwa/TWS/localopts`) no lab 10.2.8.00
- Confirmados: `jm job table size = 1024` (default), `mm cache size = 512` (default), `bm look = 5`, `bm check file = 120`, `bm check status = 300`, `bm check until = 300`, `bm check deadline = 0`
- Evidência: `lab-validation-2026-08-23-r11-localopts.jsonl`
- **lab_validation aplicado em 3 claims capacity** (0023 jm job table size, 0024 mm cache size, 0026 bm look/check)

**Frente 2 — Runbooks AWS\* (pesquisa Perplexity Direct)**:
- 4 pesquisas perplexity: AWSBCZ021E, AWSITA238E/400E, AWSJCL521E, AWSBCV012E
- **AWSBCZ021E reproduzido no lab real**: arquivo com token solto (`R11BAD` + END sem SCHEDULE) → `AWSBCZ021E A definition keyword was expected at this point` + `AWSBIA296I Total objects successfully validated: 0` (evidência `r11-awsbcz021e.jsonl`)
- **3 claims de runbook novas**:
  | Claim | Código | Tipo |
  |---|---|---|
  | `incident-bcz021e-0042` | AWSBCZ021E | RUNBOOK sintaxe de definição (lab-validado!) |
  | `incident-jcl521e-0043` | AWSJCL521E | senha Windows fora da política de segurança |
  | `incident-bcv012e-0044` | AWSBCV012E/AWSDEC002E | Mailbox.msg overflow em FTA (recovery evtsize) |
- Descoberta de correlação: AWSJCL521E/AWSBCV012E/AWSDEC002E compartilham o mesmo procedimento de recovery (evtsize Mailbox.msg + deletar corrompido + restart)

**Propagação**: claims 1018 (115 com lab_validation); chunks +6 (2402-2407) em 6 arquivos (corpus 21.827); SFT +6 records (approved 13.825, candidates 3.063); splits train 10.081/val 2.518/test 1.226; eval_independent regenerado 3.452 (+12 casos).

**Validação**: todos PASS (evidence 2 modos 0 warnings, sft, generic, eval, audit).

**Backups**: `eval_independent.jsonl.bak-20260823-r11`.

**Lições**: (1) localopts fica em `TWSDATA/localopts` (não TWS/) no 10.2.8; (2) AWSBCZ021E é reproduzível no lab com token solto — validação lab de erro de sintaxe é rápida e barata; (3) correlação entre códigos de erro com mesmo recovery (AWSJCL521E/AWSBCV012E/AWSDEC002E → evtsize) é valiosa para o modelo.

## P36 — Rodada 12: Pesquisa batch de 33 códigos AWS* + JWT testado no lab (2026-08-23)

**Objetivo**: (1) pesquisar de forma BATCH (não um a um) os 33 códigos de erro/warning AWS* sem runbook dedicado; (2) pesquisar JWT e testar no lab com as credenciais existentes.

**Ferramenta criada**: `pplx_batch.py` no servidor perplexity-direct — pesquisa em lote via stdio com resume (salva progresso em JSONL, pula os já feitos). 33 queries em ~6 min.

**JWT testado no lab (descoberta valiosa)**:
- `composer -jwt <JWT do ocli>` (token Personal válido) → `AWSBIA389E` → `AWSITA400E` → **`AWSITA238E` "The user is not authorized to access the server"**
- Token inválido → mesmo erro
- **Conclusão**: o JWT Personal criado para o ocli NÃO autoriza o composer — a autorização depende do escopo/permissions do token, não apenas da assinatura. Geração real exige DWC (não instalado no lab).
- Evidência: `lab-validation-2026-08-23-r12-jwt-composer.jsonl`
- `lab_validation` adicionado à claim `composer-jwt-lock-0108` + **claim runbook nova `incident-ita238e-0045`**

**8 runbooks novos (0046-0053)** baseados no batch perplexity:
| Claim | Código | Causa/Recovery principal |
|---|---|---|
| `incident-jdb801e-0046` | AWSJDB801E | transaction log cheio (DB2: max log; Oracle: undo) |
| `incident-jom179e-0047` | AWSJOM179E | excluir workstation com broker inacessível (uninstall incompleto de DDM) |
| `incident-jpl018e-0048` | AWSJPL018E | database locked → planman unlock |
| `incident-bin091e-0049` | AWSBIN091E | broker/SSL port mal configurado no localopts |
| `incident-deq024e-0050` | AWSDEQ024E | login conman Windows (TWS_user senha/lockout/expiração) |
| `incident-bhu072e-0051` | AWSBHU072E | FTA fault → Mailbox.msg corrompido (evtsize) |
| `incident-jco135w-0052` | AWSJCO135W | warning jobman (storage/mailbox/disponibilidade) |
| `incident-msp104e-0053` | AWSMSP104E | email alerts (mailSenderName sem domínio SMTP) |

**Propagação**: claims 1027 (117 lab_validation); chunks +16 (2408-2423) em 6 arquivos (corpus 21.843); SFT +16 records (approved 13.841, candidates 3.079); splits train 10.091/val 2.524/test 1.226; eval_independent regenerado 3.488 (+36 casos).

**Validação**: todos PASS (evidence 2 modos 0 warnings, sft, generic, eval, audit).

**Backups**: `eval_independent.jsonl.bak-20260823-r12`.

**Lições**: (1) pesquisa batch é ~33x mais eficiente que one-a-one — usar pplx_batch.py com resume para grandes volumes; (2) JWT tem escopo por ferramenta (ocli vs composer) — token Personal do ocli não autoriza composer; (3) AWSITA238E/400E são o par autorização do composer JWT.

## P37 — Rodada 13: Enriquecimento VALIDADO (perplexity vs PDF oficial) + incidentes de plano/reset (2026-08-23)

**Objetivo**: (1) enriquecer claims com as respostas do batch perplexity VALIDANDO contra o material oficial (baixei o Troubleshooting Guide 10.2.8 PDF `awstrmst.pdf` e confrontei código por código); (2) atacar o tema incidentes de plano/reset (JnextPlan/MakePlan/SwitchPlan/ResetPlan).

**Validação oficial (PDF 185 páginas)**:
- Baixei `https://help.hcl-software.com/workloadautomation/v1028/awstrmst.pdf` e extraí o texto completo
- **AWSJCO084E CORRIGIDO**: perplexity disse "autorização/locking" mas o PDF oficial documenta a causa real: **UpdateStats > 2h** (job run time excede duas horas → sessão inválida, mensagem enganosa "UNAUTHENTICATED is not authorized")
- Confirmados no PDF: AWSJPL017E (plano anterior não completou → ResetPlan -scratch + planman unlock), AWSJPL018E (MakePlan parado → planman unlock), AWSJPL006E (objeto não carrega → conexão quebrada, messages.log/ffdc), AWSJPL704E (planner unable to extend preproduction plan), AWSJCL054E/AWSJPL016E (planman confirm no SwitchPlan)

**6 claims novas (0054-0059)**:
| Claim | Tema | Fonte |
|---|---|---|
| `incident-jnextplan-txlog-0054` | JnextPlan transaction log full (DB2 180k instâncias) | PDF p.53 |
| `incident-jpl017e-reset-0055` | JPL017E → ResetPlan -scratch + planman unlock | PDF p.54 |
| `incident-makeplan-lock-0056` | MakePlan não inicia → global lock set → planman unlock | PDF p.96 |
| `incident-switchplan-confirm-0057` | SwitchPlan falha → planman confirm (3 cenários) | PDF p.97-98 |
| `incident-jco084e-0058` | UpdateStats > 2h → AWSJCO084E (não é auth!) | PDF p.71 |
| `incident-jpl704e-0059` | planner unable to extend preproduction plan | PDF p.96 |

**Enriquecimento validado**: 7 claims existentes de plano/reset (jpl017e-0007, makeplan-retry-0032, planman-unlock-0011, resetplan-0010, checksync-0028, official-message-0004) receberam notas com a referência oficial exata.

**Propagação**: claims 1033; chunks +12 (2424-2435, 6 pares PT/EN de plano/reset) em 6 arquivos (corpus 21.855); SFT +12 records (approved 13.853, candidates 3.091); splits train 10.099/val 2.528/test 1.226; eval_independent regenerado 3.512 (+24 casos).

**Validação**: todos PASS (evidence 2 modos 0 warnings, sft, generic, eval, audit).

**Backups**: `eval_independent.jsonl.bak-20260823-r13`.

**Lições**: (1) SEMPRE validar respostas perplexity contra material oficial (PDF) — o AWSJCO084E seria enriquecido errado sem a validação; (2) o Troubleshooting Guide PDF é a fonte primária mais confiável (catálogo de mensagens HTML 404); (3) plano/reset é um tema coeso com procedimentos oficiais documentados (ResetPlan -scratch, planman unlock, planman confirm).

## P38 — Rodada 14: Extração máxima do PDF oficial — FTA/Symphony recovery + failover (2026-08-23)

**Objetivo**: extrair o máximo de informação do Troubleshooting Guide 10.2.8 PDF (awstrmst.pdf, 185 págs) — mapeei o índice completo (11 capítulos) e ataquei o tema FTA/Symphony recovery + failover/switchmgr com conteúdo oficial validado.

**8 claims novas (0060-0067)** — todas com source oficial do PDF:
| Claim | Tema | Procedimento oficial |
|---|---|---|
| `incident-symphony-master-0060` | Symphony corrompido no master | switchmgr → job limit 0 → renomear Sinfonia/Symphony → switchmgr volta |
| `incident-recovery-logman-resetplan-0061` | Recovery alternativo | logman + ResetPlan + JnextPlan -from/-to (só instâncias incompletas) |
| `incident-recovery-resetfta-0062` | Symphony corrompido em FTA | **resetFTA <cpu>** (automatiza, renomeia *.msg) |
| `incident-symphony-fta-manual-0063` | Symphony corrompido em agent | unlink → deletar/renomear Symphony+Sinfonia → relink |
| `incident-planman-resync-symphony-0064` | DB desatualizado vs Symphony | **planman resync** no master ativo (mirrorbox.msg cheio → auto) |
| `incident-fta-nolink-jnextplan-0065` | FTA não linka durante JnextPlan | conman stop incompleto → aguardar parada total |
| `incident-mailman-timeout-0066` | false timeout mailman | aumentar mm response + mm unlink (60-300s juntos) |
| `incident-switchmgr-thiscpu-0067` | Symphony backup corrompe após switchmgr | thiscpu no localopts ≠ workstation name |

**Outras descobertas do PDF mapeadas (para rodadas futuras)**: agentes down (AWSITA245E), dynamic agent JDBC (AWKDBE009E sqljdbc4), event rules (LogMessageWritten, D flag), Oracle/DB2/MSSQL/Informix, application server, browser/console, performance, user access — capítulos 3-11 inteiros disponíveis.

**Propagação**: claims 1041; chunks +16 (2436-2451, 8 pares PT/EN de recovery) em 6 arquivos (corpus 21.871); SFT +16 records (approved 13.869, candidates 3.107); splits train 10.111/val 2.528/test 1.230; eval_independent regenerado 3.544 (+32 casos).

**Validação**: todos PASS (evidence 2 modos 0 warnings, sft, generic, eval, audit).

**Backups**: `eval_independent.jsonl.bak-20260823-r14`.

**Lições**: (1) o PDF tem 11 capítulos de troubleshooting — é a mina de ouro do dataset (catálogo HTML 404, PDF é a fonte); (2) recovery de Symphony tem 3 procedimentos distintos (master/switchmgr, logman+ResetPlan, FTA/resetFTA) — o modelo precisa distinguir por localização; (3) planman resync e mm response/unlink são ajustes operacionais pouco cobertos antes.

## P38b — Rodada 14 (parte 2): Exploração AUTOMATIZADA de todo o PDF (2026-08-23)

**Objetivo**: explorar TODO o Troubleshooting Guide 10.2.8 PDF de forma automatizada — extraí as 161 seções "Cause and solution" e criei runbooks para as que ainda não estavam cobertas.

**Pipeline automatizado**:
1. Extração de todas as 161 seções com `Cause and solution:` do PDF (título + conteúdo)
2. Classificação automática: código AWS* no título/conteúdo + já coberto vs novo (via claims existentes)
3. Seleção das seções NOVAS valiosas → claims de runbook geradas em lote
4. Chunks sintéticos PT/EN + propagação + SFT + validação (mesmo pipeline das rodadas anteriores)

**7 claims novas (0068-0074)** da extração automática:
| Claim | Código/Tema | Descoberta do PDF |
|---|---|---|
| `incident-jcs011e-oom-0068` | AWSJCS011E | OutOfMemoryError no JnextPlan → aumentar heap do Liberty |
| `incident-beh023e-0069` | AWSBEH023E | app server parado impede MakePlan → iniciar Liberty |
| `incident-ita105e-0070` | AWSITA105E | resources scanner → hostname não reconhecido (/etc/hosts) |
| `incident-jco136e-0071` | AWSJCO136E | limite 5 usuários Plan View → TWSConfig.properties maxusers |
| `incident-jcs037e-0072` | AWSJCS037E | pools.properties não atualizado → editar MASTERAGENTS |
| `incident-fta-dual-netman-0073` | AWSEDW001I | 2 netman na mesma porta → nm port único no localopts |
| `incident-ssl-port-zero-0074` | SSL port=0 | SSL port 0 no localopts impede link → corrigir + reiniciar netman |

**Propagação**: claims 1048; chunks +14 (2452-2465) em 6 arquivos (corpus 21.885); SFT +14 records (approved 13.883, candidates 3.121); splits train 10.123/val 2.530/test 1.230; eval_independent regenerado 3.572 (+28 casos).

**Validação**: todos PASS (evidence 2 modos 0 warnings, sft, generic, eval, audit).

**Backups**: `eval_independent.jsonl.bak-20260823-r14b`.

**Lições**: (1) o pipeline automático (extrair → classificar → gerar) transforma o PDF em claims de forma escalável — 161 seções processadas, 15 runbooks gerados em 2 passadas; (2) o validador marca IP como "dado sensível" — usar texto da mensagem sem IP concreto para manter 0 warnings; (3) o PDF ainda tem ~130 seções não exploradas (browsers/console, reports, DBs específicos) para rodadas futuras.

## P39 — Rodada 15: Exploração COMPLETA e AUTÔNOMA de todo o PDF (2026-08-23)

**Objetivo**: explorar TODO o Troubleshooting Guide 10.2.8 PDF de forma autônoma, sem interromper, até finalizar — instrução do Adriano.

**Cobertura completa: 161/161 seções "Cause and solution" do PDF** ✅

Processei em 6 lotes automatizados as ~117 seções restantes (redes, FTA, dynamic agents, engine, eventos, DBs DB2/Oracle/MSSQL/Informix, upgrades, DWC/console, browsers, reports, critical network, failover/switchmgr):

**73 claims novas (0075-0147)** — destaques por tema:
- **Networks/links**: mm symphony download timeout, SSL mode change (deletar Symphony/Sinfonia), behind firewall, AWKRCE012E, FTA cleanup, dynamic agent not found/no resources/job error, SSL port=0
- **Engine**: composer dependency order, display cpu=@ (stty kill), AWSBIA015I (daylight savings), FFDC cleanup, pobox sizing, DB2 lock list, cscript missing, JnextPlan slow, hosts file, exec status race, TCL hang, prompt number
- **Database**: DB2 deadlock timeout, Oracle permissions/schema, MSSQL cascade 30, external lock, table locked by DB GUI, sqljdbc4 JDBC driver
- **Events**: deployconf, event queue overflow, switcheventprocessor, LogMessageWritten, D flag
- **Upgrades/misc**: variables upgrade, local params files, AIX timezone, cluster.exe, config merge, remote registry, ulimit
- **DWC/console**: roles, session invalid, HADR DB2, Graphical Designer, mirroring disabled, authentication_config.xml
- **Critical network/failover**: critical late, empty hotlist, switchmgr relink all (JnextPlan -for 0000), switchmgr J flag

**Propagação**: claims 1121; chunks +73 PT (2466-2538) em 6 arquivos (corpus 21.958); SFT +73 records PT (approved 13.956, candidates 3.194); splits train 10.177/val 2.543/test 1.236; eval_independent regenerado 3.864 (+292 casos — salto grande por causa das 73 claims novas).

**Validação**: todos PASS (evidence 2 modos 0 warnings, sft, generic, eval, audit).

**Backups**: `eval_independent.jsonl.bak-20260823-r15`.

**Lições**: (1) o pipeline automático (extrair → classificar → gerar) cobriu 161/161 seções em uma sessão; (2) tradução automática por dicionário degrada a qualidade — para EN de qualidade, escrever manualmente (deixei 73 chunks EN como pendência para rodada futura dedicada); (3) claims PT de alta qualidade + SFT PT balanceiam o dataset (PT 1588 / EN 1606).


## P40 — EN synthetic propagation and z/OS boundary audit (2026-08-23)
- Perplexity translation worker completed the available batch; raw output was audited because rate-limit responses were serialized as JSON. 99 usable EN translations were extracted to `temp/pt_en_translated_valid.json`; 38 of the 217 queued PT records remain pending due to rate limiting/insufficient valid answers.
- EN records were appended only as corpus material (99 PT/EN pairs already had the PT source in corpus); `eval.jsonl` was not modified. Derived training-side corpus files were propagated and JSON-validated.
- 34 claims containing explicit z/OS terminology were marked `validation_scope=zos_boundary_explicit` with rationale. Legitimate EEL boundary claims were not changed.
- SFT connected-family splits were regenerated with `scripts/split_sft.py`; approved/candidates were not promoted because the translated chunks are corpus chunks, not reviewed claims/SFT records.
- Validation: JSONL integrity 0 errors; generic prompts PASS (0/17,336). `audit_dataset.py` exposed pre-existing corpus noise/holdout overlap diagnostics; it did not modify eval.
- Optional frontier: quality-audit route selected over REST API v2 expansion; translation quality/rate-limit and provenance audits are the next gate before SFT promotion.

## Nota — validações mutating/destructive usam o lab WSL (2026-08-23)

Registro do plano `hwa-dataset-quality-gates` (F5). Política operacional:
validações **mutating/destructive** de claims sensíveis (DWC/upgrade/SAP,
comandos conman de plano, etc.) são executadas **apenas no lab WSL2**
(`data/runbooks/hwa-10.2.8-wsl-lab.md`), nunca em ambiente de produção. Quando
não há 2ª evidência nem lab disponível, a claim permanece com exigência de
validação lab (`lab_required`) — o pipeline nunca infere evidência (D5).

- **Registros lab desta base**:
  - **P30** (2026-08-22): expansão sintética v2-001 — 618 candidatos novos,
    promoção P30a/P30b/P30c/P30d (approved 13.183 → 13.801).
  - **P31** (2026-08-23): rodada 7 — validação lab dos 9 comandos conman de
    operação de plano (fence, limitcpu, rerun, rerunsucc, release job,
    release sched, submit job, submit sched, altjob) com `lab_validation`
    registrada nas claims correspondentes.
- **Gate único**: `python scripts/validate_all.py` (F5) encadeia os 8 gates
  do pipeline; o gate de evidência roda em modo estrito
  (`--require-corroboration`) e o gate de regressão aponta para o release
  mais recente em `data/releases/`. Nenhum gate altera dados: artefatos
  canônicos são monitorados por hash durante a execução.

## P32 — DWC 10.2.8 instalado e configurado (2026-08-25) — fecha o gap P0

O Dynamic Workload Console 10.2.8.00 foi instalado e configurado no lab WSL2
Ubuntu 22.04, fechando o gap documentado em `hwa-lab-10.2.8-dwc-not-installed-0049`
(superseded para `obsolete`). Evidência: `data/evidence/lab-validation-2026-08-25-dwc-install.jsonl`
(5 records `observed_in_lab`); claims novas `hwa-10.2.8-dwc-install-0023/0024/0025`,
`hwa-10.2.8-dwc-login-0001`, `hwa-10.2.8-dwc-engine-connection-0001/0002`
(`official_lab`, com `lab_validation`); claim de processo
`hwa-lab-10.2.8-dwc-install-round-0086` em `lab-claims.jsonl`.

### Componentes e parâmetros do lab

- Imagem: `G:\HWA_10.2.8_DWC_LINUX_X86_64.zip` → `/root/hwa/dwc-extracted`
  (Java 21 IBM Semeru OpenJ9 embutido, `dwcinst.sh`, `configureDb.sh`, `dbtools/postgresql`).
- Instalação: `DWC_INST_DIR=/opt/hwa/DWC` (não o default `/opt/wa/DWC`),
  `WLP_INSTALL_DIR=/opt/liberty/wlp` (Open Liberty 26.0.0.3 já usado pelo MDM).
- Banco: PostgreSQL 18 local, banco **TDWC** (default 10.2.8 nas properties —
  divergência doc×kit: a referência `awspidwcinstsyntax` cita default `DWC`),
  role `postgresdwc` (login), admin `postgres`.
- Usuário DWC: **wauser** (mesmo do MDM/TWS) — ver troca pós-instalação abaixo.
- Portas: HTTPS **9443**, HTTP **9444**, bootstrap **12809**, bootsec **19402**.
- Registro: `twaregistry.sh -add /opt/hwa/DWC 10.2.8.00-2026.07 wauser DWC ...`
  (`/opt/hwa/Registry`).

### Procedimento (validado, ordem oficial)

1. **Pré-requisitos**: Open Liberty no host; banco criado/populado (configureDb
   primeiro); usuário admin DWC existente no SO; umask 022; certificados
   `ca.crt`/`tls.key`/`tls.crt` em pasta (ownership do usuário do MDM, 644).
2. **`configureDb.sh -f configureDbPostgresql.properties`** (POSTGRESQL/DWC,
   `DB_NAME=TDWC`): cria o banco automaticamente se não existir
   (`WAINST0534W The database TDWC does not exist. It will be created.`),
   popula schemas `tdwc` (48 tabelas) e `fed` (7 tabelas — Federator,
   instalado junto desde 10.2.3). `WAINST052I completed successfully`.
3. **`dwcinst.sh -f dwcinst.properties`** (`ACCEPTLICENSE=yes`,
   `RDBMS_TYPE=POSTGRESQL`, `DWC_INST_DIR`, `WLP_INSTALL_DIR`, `--user`,
   `SSL_KEY_FOLDER`, `SSL_PASSWORD`, `START_WLP=false`): sequência WAINST
   208I→204I→053I→206I→536I→207I→200I (configureWlp)→201I (configureDatasource)
   →0229I (certificates)→055I (registry)→**023I completed successfully**.
   Log: `DWC_DATA/installation/logs/dwcinst_10.2.8.00.log`.
   URL: `https://<host>:9443/console/login.jsp`.
4. **Troca do usuário para wauser (pós-instalação, sem reinstalar)**:
   - Gerar senha `{aes}` com a MESMA chave do passphrase_variables.xml:
     `securityUtility encode --encoding=aes --key=1787657107 '<senha>'`
     (round-trip conferido com `PasswordCipherUtil.decipher`).
   - Editar `DWC_DATA/usr/servers/dwcServer/configDropins/overrides/wauser_variables.xml`
     (`user.twsuser.id=wauser`, `user.twsuser.password={aes}...`).
   - `appservertools/setEnv.sh`: `WA_USER=wauser`.
   - `chown -R wauser:wauser /opt/hwa/DWC` e restart do dwcServer.
5. **Iniciar servidor**: `appservertools/startAppServer.sh` (como wauser;
   `APPSERVERHOME=/opt/liberty/wlp`, `SERVERNAME=dwcServer`,
   `WLP_USER_DIR=/opt/hwa/DWC/usr`, `WLP_OUTPUT_DIR=DWC_DATA/stdlist/appserver`).
6. **Validar login**: `POST /console/j_security_check` (j_username/j_password)
   → 302 + cookie LtpaToken2 → `GET /console/` 200 (dashboard).

### Engine connection (DWC → MDM) via REST API interna

- O engine REST API V2 (`https://MDMHOST:31116/twsd/`) é servido pelo
  **engineServer** do MDM (`/opt/hwa/usr/servers/engineServer`, iniciado por
  `appservertools/startAppServer.sh` como wauser). Com o engineServer parado a
  porta 31116 não responde e o checkConnection do DWC falha.
- Adicionar o alias do engine ao `/etc/hosts` do host do DWC
  (`127.0.0.1 MDMHOST`) para o checkConnection resolver.
- Criar a conexão (contexto `/dwc/api`, JAX-RS `EngineApplication` em `/v1/`):
  ```bash
  POST /dwc/api/v1/engine/create
  {"name":"MDM_LAB","type":"TWS","hostname":"MDMHOST","port":31116,
   "remoteServerName":"MDM","credentials":{"user":"wauser","password":"<lab>"},
   "showInDashboard":true,"enableSSC":false,"reporting":false}
  → {"successful":true,"message":"MDM_LAB created successfully."}
  ```
- Validar: `GET /dwc/api/v1/engine/1/checkConnection` → `{"successful":true,...}`
  e `GET /dwc/api/v1/engine/1/info` → 200 (NAME MDM_LAB, TYPE maestro, HOST
  MDMHOST, PORT 31116). **engine_id é numérico** (id da tabela); usar o nome
  causa `NumberFormatException` (EngineAppService.findEngine).
- Persistência: `tdwc.tdwc_engineconnection` (id=1, enginetype=2),
  `tdwc.tdwc_credential` (senha criptografada), `tdwc.tdwc_preferenceable`
  (preferencetype=3).

### Divergências doc × lab (registradas como observações)

- `--dbname` default: referência `awspidwcinstsyntax` cita `DWC`, mas o kit
  10.2.8 (`configureDbPostgresql.properties`, `dblighttool`) usa **TDWC** —
  usar TDWC de forma consistente.
- `WLP_USER_DIR=${DWC_INST_DIR}/usr` (dwcServer em `/opt/hwa/DWC/usr/servers`),
  não no `usr` do Liberty — mesmo padrão do engineServer do MDM.
- Troca de usuário pós-instalação é suportada sem reinstalar (evidência lab).
- `GET /dwc/api/v1/engine/list` retorna `items: []` no lab mesmo com a engine
  criada (filtros de dashboard/SSC); `info`/`checkConnection` por id funcionam.
- `checkConnection` é GET (POST → 405).

### Registros lab desta base

- **P32** (2026-08-25): DWC 10.2.8 instalado/configurado — fecha o gap DWC do
  P0. Claims 0023-0025/login-0001/engine-connection-0001-0002; 12 candidatos
  SFT PT/EN; evidência lab-validation-2026-08-25-dwc-install.jsonl.
  **Promoção concluída** (auditoria independente `hwa-dataset-auditor`:
  APROVADO COM RESSALVAS; ressalvas HIGH-1 lab-format, MEDIUM-2/3/4
  atribuição/variável, LOW-5/7 corrigidas):
  - `promote_sft.py` → +12 em approved.jsonl (sha256 d3ca969f...);
  - **remoção de 14 records obsoletos** que ensinavam "DWC não instalado"
    (referenciavam `hwa-lab-10.2.8-dwc-not-installed-0049`, agora obsolete)
    — backup `approved.jsonl.bak-20260825-dwc-remove-obsolete`;
  - approved 15.567 → **15.565**; splits regenerados: train **11.352** /
    validation **2.788** / test **1.425**; eval_independent **4.068** (PT 2.034
    + EN 2.034, anti-vazamento);
  - `validate_all.py` (F5): **todos os 8 gates PASS** (evidence 1.183,
    sft 15.565 com cobertura de risco, split, eval 4.068, function_calls,
    contradiction 1.165, regression vs r19-sota); `validate_generic_prompts`
    PASS (0/15.565); harness ultra-SOTA atualizado
    (`data/ultra_sota_report.json`, `data/coverage_backlog.json`);
  - Observação pré-existente (fora do escopo DWC, não introduzida por esta
    rodada): 1.398 records em approved referenciam claims `hwa-lab-*` de
    processo (padrão histórico do dataset); `build_eval_gold` regenerado
    alinhou o `evidence_tier` de casos `hwa-upgrade-1028-rollback-0001`.


### Referências oficiais (10.2.8)

- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspiinstallDWC.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspidwcinstsyntax.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_pi/awspitwsinstdbcfg.html`
- `https://help.hcl-software.com/workloadautomation/v1028/distr/src_tsweb/General_Help/mng_eng_c.html`

### P32b - Idioma da UI do DWC (2026-08-25)

Evidencia empirica + fonte oficial registradas: o idioma da interface do DWC
segue o Accept-Language do navegador (sem seletor no login; TdwcGlobalSettings.xml
nao controla idioma); default tasks sao criadas no idioma do PRIMEIRO login e nao
sao traduzidas depois (solucao oficial: novo usuario com primeiro login no idioma
desejado; precannedTaskCreation = all|none|distributed|zos, lida so no 1o login).
Claims hwa-10.2.8-dwc-ui-language-0001 / hwa-10.2.8-dwc-default-tasks-language-0002;
evidencia lab-validation-2026-08-25-dwc-ui-language.jsonl; 4 candidatos SFT PT/EN.

### P32c - Opcao A: novo usuario DWC com primeiro login em ingles (2026-08-25)

Procedimento executado e validado em laboratorio (wauser_en):

1. Gerar a senha {aes} do novo usuario com a MESMA chave da instalacao:
   /opt/liberty/wlp/bin/securityUtility encode --encoding=aes --key=<chave-lab> <lab-password>
   (o securityUtility fica no Liberty, nao em /opt/hwa/DWC/bin)
2. Adicionar o usuario ao basicRegistry e ao grupo Admins em
   DWC_DATA/usr/servers/dwcServer/configDropins/overrides/authentication_config.xml:
     <user name="<dwc-user>" password="{aes}..."/>
     <group name="${admin.group.name}">
        <member name="${user.twsuser.id}"/>
        <member name="<dwc-user>"/>
     </group>
   (backup do arquivo antes; XML valida com parse)
3. Reiniciar o dwcServer:
   su - wauser -c 'cd /opt/hwa/DWC/appservertools && ./stopAppServer.sh'
   su - wauser -c 'cd /opt/hwa/DWC/appservertools && nohup ./startAppServer.sh > /tmp/dwc-start.log 2>&1 &'
4. Validar login com Accept-Language en-US:
   curl -sk -c sess.txt https://<host>:9443/console/login.jsp -o /dev/null
   curl -sk -b sess.txt -c sess.txt -H 'Accept-Language: en-US,en;q=0.9' \
     --data 'j_username=<dwc-user>' --data 'j_password=<lab-password>' \
     https://<host>:9443/console/j_security_check
   Esperado: HTTP 302 + cookie LtpaToken2; GET /console/ -> 200 com UI em ingles
   (login page 'Username', dashboard 'Workload dashboard').

Resultados lab:
- Login do novo usuario OK e UI carrega em ingles (confirma claim 0001 p/ 2o usuario).
- DESCOBERTA: apos login HTTP puro + acesso ao console via curl, o banco
  tdwc.tdwc_querytask NAO contem default tasks para o novo usuario (wauser=21,
  wauser_en=0). A criacao das default tasks parece ser disparada pela sessao
  interativa da UI (SPA/JS) no primeiro login, nao pelo POST de login HTTP.
  Refina a claim 0002 (primeiro login "com navegador" = sessao UI); nao contradiz.
  Revalidar com navegador real (CDP/Playwright) antes de generalizar.
- FFDCs no log (NoClassDefFoundError: SmallRye JWT/Micrometer/MongoDB) sao de
  features nao usadas no lab; inofensivos, servidor saudavel.

Evidencia: lab-validation-2026-08-25-dwc-wauser-en.jsonl (0059 login / 0060
default tasks via HTTP). Promocao SFT: r20-sota (docs/RELEASE_REPORT_r20.md).

### P33 - AI Data Advisor (AIDA) Docker deployment (2026-08-25)

AIDA = AI Data Advisor, componente de IA/ML do HWA (desde V10.1): analisa metricas
historicas, preve padroes e detecta anomalias em KPIs, com alertas no Workload
Dashboard do DWC + email. Pacote: G:\HWA_10.2.8_DOCKER_AIDA_LINUX_X86_64.tar.gz
(sha256 facc5bf669d9d15399e3e56cbf5116361e5a28bd7208c0b368bfd4b37fd1d378, 1.8GB,
930 arquivos). Validado em lab WSL2 (Docker 29.7.2 + Compose v5.5.0).

Estrutura do pacote:
- aida-images-hcl.tar.gz: 9 imagens hclcr.io/wa/workload-automation/hcl-aida-{ad,
  exporter,email,nginx,orchestrator,predictor,redis,config,ui}:10.2.8
- docker-deployment/: AIDA.sh, docker-compose.yml (+dev/debug), common.env,
  Dockerfile-* (11 servicos), config/, nginx/cert/, redis/, keycloak/, Licenses/,
  ILMT/, hcl-readme/
- OpenSearch 2.19.6 (Dockerfile-es, base ubi9 + download artifacts.opensearch.org)
  e Keycloak 26.6.4 (Dockerfile-keycloak, base quay.io) NAO vem no tar: build online.

Instalacao (offline/HCL Flexera):
  export CONTAINER_RUNTIME=docker          # obrigatorio (podman tambem suportado)
  tar -xzf HWA_10.2.8_DOCKER_AIDA_LINUX_X86_64.tar.gz -C /opt/hwa/aida
  cd /opt/hwa/aida/docker-deployment
  ./AIDA.sh load                            # carrega as 9 imagens do ../aida-*.t*
  ./AIDA.sh build-start                     # builda es/keycloak + sobe 10 containers

Configuracao (common.env):
- LICENSE=accept (obrigatorio; AIDA.sh check_license usa less Licenses/license)
- EXTERNAL_HOSTNAME=<IP> (obrigatorio anti Host Header attack; nginx devolve 405
  'Host not matching' se o Host nao bater)
- WA_OMETRICS/WA_METADATA/WA_RECORDS/ALERT_CONFIG/KPI_CONFIG/WA_CATALOGS:
  https://<mdm-host>:31116/... (ex.: https://MDMHOST:31116/metrics)
- HOST_IP=<ip>:9432 (para alertas por email)
- OPENSSL_PASSWORD=<chave> (usada p/ cifrar credenciais do engine no OpenSearch)
- Parametros chave: METRICS_FETCH_INTERVAL=240 (o /metrics expira apos ~10min),
  EXPORTER_EXECUTION_INTERVAL=86400, PROPHET_ORCHESTRATOR={"schedule":1440,
  "schedule_alert":15}, DAYS_OF_PREDICTION=2, MAXIMUM_DAYS_OF_OLDER_DATA=180,
  RESOLVE_ALERTS_AFTER_DAYS=1, MODEL=prophet (ou neural)

Ajustes obrigatorios para lab com pouca RAM (11.5GiB):
- vm.max_map_count >= 262144 no HOST: sudo sysctl -w vm.max_map_count=262144
  (persistir em /etc/sysctl.conf). Sem isso OpenSearch nao sobe.
- docker-compose.yml: es OOMKilled (ExitCode 137) com values default (limits 8G +
  heap default). Fix lab: ES_JAVA_OPTS + OPENSEARCH_JAVA_OPTS=-Xms768m -Xmx768m,
  es limits 3G / reservation 1.5G; reduzir keycloak 768M, predictor 768M, ui 512M.
- extra_hosts (MDM/DWC no host, fora do docker): adicionar nos 11 servicos
    extra_hosts:
      - "wa-waserver:host-gateway"
      - "MDMHOST:host-gateway"
      - "host.docker.internal:host-gateway"
  Sem isso: exporter falha com NameResolutionError 'Failed to resolve wa-waserver'.

Credenciais do engine (aida-config):
  # fluxo interativo (exige TTY):
  ./AIDA.sh add-credentials
  # fluxo automatizado (3 args; o dispatch $1 $2 do config.sh nao repassa 3 args):
  docker compose --profile config up -d config
  ENCPASS=$(docker exec aida-config sh -c 'echo -n "<pw>" | openssl enc -AES-128-ECB -base64 -salt -pbkdf2 -pass env:OPENSSL_PASSWORD')
  printf 'y\n' | docker exec -i aida-config bash -c "source /config.sh && add_credentials wa-waserver:31116 <user> '$ENCPASS'"
  # valida contra https://<host>/twsd/engine/info (distributed) ou /twsz/v1/<engineName>/engine/info (zOS)
  # credenciais ficam CIFRADAS no OpenSearch (indice wa-credentials, doc <host:port>)
  docker exec aida-config bash -c 'source /config.sh && delete_credentials wa-waserver:31116'  # remover

Validacao (o que foi confirmado em lab):
- https://127.0.0.1:9432/ -> 200 (SPA 'AI Data Advisor (AIDA)'); /healthz -> 200
- localhost:9432 -> 405 'Host not matching' (usar o EXTERNAL_HOSTNAME exato)
- exporter: 6 KPI definitions processadas, 80 metricas inseridas no OpenSearch
  (metric-index-<data>, alert-definitions 12 docs, kpis-definition)
- containers: nginx(9432), keycloak(8080/8443/9000), es(9200/9300/9600), ui(9000),
  ad/predictor/email(5000), redis(6379), orchestrator, exporter, config(transiente)
- OpenSearch cluster yellow (1 node) = normal em lab
- DWC (9443) e MDM (31116) seguem saudaveis com AIDA rodando

Comandos AIDA.sh: load | build-start | build | start | stop | restart | up |
down | down-volumes | first-start | add-credentials | update-credentials |
delete-credentials | set-custom-port | dump. Options: --noexporter | --debug | --dev.

Troubleshooting:
- es Restarting 137/OOM: reduzir heap (ES_JAVA_OPTS), aumentar limit es, reduzir
  outros; vm.max_map_count no host.
- 'Failed to resolve wa-waserver': extra_hosts para o host-gateway.
- 'Host not matching' na UI: EXTERNAL_HOSTNAME deve ser o host exato usado no browser.
- exporter 'no kpi definition found': aguardar o orchestrator processar (1440min p/
  predicao, 15min p/ alertas) ou verificar credenciais no wa-credentials.
- 'Cannot extract kpi definitions': MDM /twsd/engine/definition/* exige auth basic.

Claims: hwa-10.2.8-aida-intro-0001, -install-0002, -es-oom-0003, -network-host-0004,
-credentials-0005, -metrics-0006, -ui-0007. Evidencia:
data/evidence/lab-validation-2026-08-25-aida-docker.jsonl (0061-0068).


### P33b - AIDA: schemas, API e ciclos (enriquecimento 2026-08-25)

Schemas reais no OpenSearch (validados em lab):
- alert-definitions: 12 docs (2 por KPI x 6 KPIs). Schema: definitionID, name,
  kpi (metric_name), trigger {type: continuous|total, value: 10, timeFrame: 60,
  description}, periodicity '1 hour', isActive 'true', alert-definition.
  continuous = N anomalias CONSECUTIVAS; total = N anomalias TOTAIS no periodo.
- kpis-definition: 6 docs. Schema: name, metric_name, frequency 240, category
  Jobs|Queue, subcategory Trend|Trend_by_wks, keyprop jobstatus (10 status),
  keyPropValues [SUCCESSFUL..CANCELED], workstation (/MDMDA, /MDMXA), esQuery,
  alert-definition (vinculo). Doc id = <name><metric_name><tag>.
- metric-index-<data>: metricname, value, @timestamp (epoch millis),
  properties{jobstatus, mp_scope, parsedTag}, tag (wa-waserver:31116), parsedTag,
  uuid, keyprop.
- special-days-labels: 95 docs (state + names de feriados por regiao).

API REST interna (sob /api, swagger em /api/swagger/): 23 endpoints em 6 grupos
(KPIs, Alerts, Metrics, Special Days, Actions, JWT). Auth: Keycloak realm 'aida',
client publico 'nginx', usuarios aidaadmin (aida-admin) / aidauser; token por
password grant em https://<host>:9432/keycloak/auth/realms/aida/protocol/openid-connect/token.
Exemplos validados: POST /api/kpi/list (KPIs + last24hAlerts), GET /api/kpi/category/list
(Jobs 5 / Queue 1), POST /api/alert/instance/list (count), GET /api/actions/retrain/retrain-details,
POST /api/actions/retrain (result:true).

Ciclos:
- Deteccao de alertas: a cada 15 min (PROPHET_ORCHESTRATOR schedule_alert=15);
  orchestrator chama aida-ad /detectAlerts (log 'callAlertAPI - POST /detectAlerts
  status=200').
- Retrain de predicoes: a cada 24h (schedule=1440); via API POST /actions/retrain
  retorna result:true, mas predicoes exigem serie historica minima (no lab com ~1h
  de metricas, predictions ficou 0).
- Email: aida-ad detecta alerta -> publica no Redis -> aida-email consome e envia
  via SMTP (parametros SMTP_* no common.env; sem SMTP o envio e ignorado).

Fonte oficial: AIDA User's Guide 10.2.8 (awsai_*.html): conceitos (KPI/Anomaly/
Alert/Severity), 6 KPIs default (240s/86400s), 12 alert-definitions, retrain 24h,
special days com tolerancia maior, Keycloak (realm aida, aidaadmin/admin default),
SMTP, diferencas z/OS (DWC host/port/remote server; prophet-only no z/OS).

Claims novas: hwa-10.2.8-aida-{alert-definitions-0008, kpi-catalog-0009,
metric-format-0010, special-days-0011, rest-api-0012, concepts-0013, kpi-types-0014,
alerts-default-0015, retrain-specialdays-0016, keycloak-email-0017, zos-0018}.
Evidencias: lab-validation-2026-08-25-aida-docker.jsonl (0070-0078).
