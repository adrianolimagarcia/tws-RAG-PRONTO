# PRÉ-REGISTRO — Leitura do boundary de produção de 16.09 (alvo 2026-09-17 00:00:00Z = 21:00 BR)

> **Status: ARMADO, NÃO LIDO.** Escrito ANTES do evento. Este arquivo vive em `docs/lab-protocols/`,
> **fora do glob indexado** do corpus (`data/evidence/lab-validation-*.jsonl`), de propósito: é protocolo,
> não evidência.
>
> **Frente read-only.** Nenhuma mutação de plano/engine é executada para esta leitura. Congelamento vigente.

## 1. O que este evento discrimina

**Hipótese aberta**: o **MDM não processa o boundary de produção** desde 13.09, enquanto o **BMDM processa**.
A leitura de hoje é o evento que discrimina — e é a primeira janela **sem** o `AGT1` no modelo e **com o lab
recém-reconstruído** (estado pós-M1 preservado pelo snapshot 112).

## 2. Alvo e seletores (exatos)

| item | valor |
|---|---|
| nó | **MDM** (container `tws-hwa`) |
| arquivo | `/opt/hwa/TWSDATA/stdlist/traces/20260916_TWSMERGE.log` |
| janela | `^(20:5[89]\|21:0[0-2]):` (BR) |
| discriminador 1 | `Received dR` (BATCHMAN) |
| discriminador 2 | `status to READY` (BATCHMAN) |
| contraste | `MAILMAN` (ruído; sozinho **não** decide) |

**Atenção de fuso**: o boundary é `00:00:00Z` = `21:00 BR`. A janela do MDM é lida em **BR**; a do BMDM, se
conferida, é lida em **UTC** (`^00:00:0[0-9] `).

## 3. Série de controle (medida no mesmo tick do pré-registro, MDM, mesma janela)

| arquivo | linhas | `dR` | `READY` | `MAILMAN` | leitura |
|---|---|---|---|---|---|
| `20260910` | 481 | 2 | 3 | 101 | ruído alto (pré-AGT1-estável) |
| `20260911` | 77 | **13** | **13** | 0 | **boundary PROCESSADO** |
| `20260912` | 79 | **13** | **13** | 0 | **boundary PROCESSADO** |
| `20260913` | 22 | **0** | **0** | 20 | **NÃO processado** |
| `20260914` | 22 | **0** | **0** | 20 | **NÃO processado** |
| `20260915` | 0 | 0 | 0 | 0 | **host desligado na janela** (medida perdida) |
| `20260916` | 0 | 0 | 0 | 0 | **zero TAUTOLÓGICO** — a janela ainda não chegou |

**Controle positivo obrigatório, executado no mesmo tick**: releitura de `20260912` com o **mesmo seletor** →
**79 linhas / dR=13 / READY=13 / MAILMAN=0** ⇒ **seletor VÁLIDO**. Se este controle tivesse dado 0, o
resultado do dia seria **INCONCLUSIVO** (seletor errado), e não negativo.

**Armadilha registrada**: o arquivo do dia vigente dá 0 na janela **antes** das 21:00. Esse zero é
**tautológico** (a janela não chegou) e **NÃO é evidência** — nunca citá-lo como resultado.

## 4. Tabela de decisão (pré-escrita, aplicada mecanicamente)

| observação na janela | conclusão |
|---|---|
| **`dR` = 0 E `READY` = 0** | boundary **NÃO processado** (mesmo padrão de 13–14.09) |
| **`dR` > 0 E `READY` > 0** | boundary **PROCESSADO** (mesmo padrão de 11–12.09) |
| `dR` > 0 mas `READY` = 0 (ou inverso) | **inconclusivo** — registrar e escalar, **não** forçar num ramo |
| janela com 0 linhas | **leitura cedo/arquivo errado** — reconferir o relógio e re-ler; **não** concluir negativo |
| `MAILMAN` alto **com** `dR`/`READY` > 0 | processou; o ruído é concorrente, não substituto |

**Sem conclusão de causalidade.** A leitura diz se processou ou não; não diz por quê.

## 5. Protocolo de leitura (comandos exatos, read-only)

```bash
W='^(20:5[89]|21:0[0-2]):'
F=/opt/hwa/TWSDATA/stdlist/traces/20260916_TWSMERGE.log

# 0. relógio ANTES (a janela tem de ter passado)
date -u '+%F %T UTC' ; TZ=America/Sao_Paulo date '+%F %T BR'

# 1. linhas na janela
docker exec tws-hwa bash -c "grep -cE '$W' $F"

# 2. discriminadores
docker exec tws-hwa bash -c "grep -E '$W' $F | grep -c 'Received dR'"
docker exec tws-hwa bash -c "grep -E '$W' $F | grep -c 'status to READY'"
docker exec tws-hwa bash -c "grep -E '$W' $F | grep -c MAILMAN"

# 3. CONTROLE POSITIVO no mesmo tick (se der 0, o dia é INCONCLUSIVO)
docker exec tws-hwa bash -c "grep -cE '$W' /opt/hwa/TWSDATA/stdlist/traces/20260912_TWSMERGE.log"

# 4. conteúdo, para leitura humana (conjunto por nome, não contagem isolada)
docker exec tws-hwa bash -c "grep -E '$W' $F | head -40"
```

**Regra de leitura**: se a janela estiver vazia, **reconferir o relógio** e re-ler; só concluir depois de
confirmar que a janela passou **e** que o arquivo do dia é o certo.

## 6. Congelamento de mutação (vigente até a leitura)

**Proibidos**: `conman submit|release|sbs|cs|altjob|switchmgr`, `composer add|update`, `JnextPlan`,
`planman reset|crt`, `SwitchPlan` manual. **Livre**: `sj`, `sc`, `joblog`, stdlist, logs, DWC.
**Motivo**: qualquer mutação na janela apaga o poder discriminante da observação.

## 7. stop_criterion

Se a leitura do boundary **exigir mutação** para ser discriminante → **PARAR e escalar**. Não executar.
Se aparecer `AWSJPL004E` → parar e reportar.

## 8. Reversibilidade

Tudo acima é **read-only**: nenhum comando de plano/engine, nenhum acesso ao PostgreSQL compartilhado,
`Sfinal` intocado. Nada a reverter.

## 9. Onde o resultado será registrado

- Evidência: `data/evidence/lab-validation-2026-09-17-*.jsonl` (gate `validate_lab_session.py`)
- Runbook: seção nova em `data/runbooks/hwa-10.2.8-edwa-eif-jobstatus-msglog-e2e.md`
- **Este arquivo não é alterado depois** — o resultado vai para a evidência, para preservar o pré-registro.
