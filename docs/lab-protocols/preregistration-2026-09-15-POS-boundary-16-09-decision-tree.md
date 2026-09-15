# Pré-registro — FASE PÓS-BOUNDARY (após a leitura do boundary de 16.09 00:00Z)

> **NÃO EXECUTAR NADA DESTE ARQUIVO ENQUANTO O FREEZE ESTIVER VIGENTE.**
> Arquivo deliberadamente em `docs/lab-protocols/` porque este diretório **NÃO** entra no corpus do RAG
> (verificado no código: os globs indexados são `data/evidence/lab-validation-*.jsonl` e
> `data/runbooks/*.md` — `docs/` não está entre eles).
> Autorização vigente: `[VIGIA-ARQUITETO]` — congelamento de mutação até a leitura do boundary de 16.09.

## Por que o boundary de 16.09 é o evento DISCRIMINANTE

O lab tem duas anomalias medidas que **podem ou não** ter a mesma causa:

1. **Divergência modelo×runtime no domain manager** — corrigida pela M1 (15.09 13:05Z). Antes dela,
   qualquer operação de plano a partir do MDM morria em `AWSJPL004E`.
2. **Boundary de produção anômalo** desde 13.09 20:58Z (0 READY / 0 `dR` / sem esteira noturna).

Se o boundary de 16.09 **normalizar**, a divergência era o bloqueio (causa única). Se **permanecer
anômalo**, a M1 removeu um bloqueio real mas **não** era a causa do boundary — e a anomalia tem outra
origem.

## Estado medido ANTES da leitura (pré-condições da decisão)

- **Plano ativo (run 69) com horizonte COMPLETO**: `sj @#@.@` mostra **78 instâncias em 09/16** e cobertura
  contínua **até 09/25** (09/16–09/18 e 09/21–09/25 com 78/dia; 09/19 57; 09/20 69). Inclui
  `LABPOOL#POOL_STREAM 0005 09/16` e `POOL_JOB` — as instâncias que o boundary deve readiar.
- **`Symnew` pendente com extensão de 0 dias** (`showinfo`: *"Production plan end time: (same as the start
  time of the last extension)"*; `Run 72` / `Confirm 69`). O arquivo tem 23.392 B — **tamanho normal** de
  delta de extensão (precedente no próprio lab: `Symnew.bak` = 19.584 B). **Não é um plano degenerado**:
  o horizonte zero é da *extensão pendente*, não do plano ativo.
- `Batchman LIVES`; `MDM ... *UNIX MASTER`; modelo `*MANAGER MDM`.

## PRIMEIRO DISCRIMINADOR DA JANELA (correção de medição do vigia, 15.09 19:50Z)

**Leia o `dR` ANTES de qualquer conclusão.** Assinatura medida nos 4 arquivos, janela
`^(20:5[89]|21:0[0-2]):` do merge do MDM:

| grupo | linhas | BATCHMAN | `Received dR ... from cpu MDM_BK` | READY | MAILMAN |
|---|---|---|---|---|---|
| **NORMAL** (dias-alvo 11.09 e 12.09) | 77 / 79 | 100% | **13** | 13 | **0** |
| **ANÔMALO** (13.09 e 14.09) | 22 | — | **0** | 0 | **20** (com `AWSBCV035W Mailman was unable to link to workstation: AGT1` + `AWSBCV082I ... (errno=111)`) |

- **Discriminador:** **`dR > 0` E ausência do burst MAILMAN**. A contagem de READY só confirma depois.
- **Correlação medida, causa NÃO estabelecida:** o `MY:UNLINK AGT1` aparece **também** na janela normal de
  12.09 — o UNLINK sozinho **não** discrimina. E o link do AGT1 já falhava em 13.09, **antes** da M-C de hoje.

## Enumeração do conjunto (correção: NÃO usar contagem crua de linhas do `sj`)

Contagem crua de linhas que contêm `09/16` **não** é número de instâncias (inclui linhas de JOB filho e
brancos). Enumerado por **instância de job stream**, o dia de plano 09/16 tem **26 instâncias, TODAS em HOLD**:

- **20** do cohort de produção `2105 09/16` — **conjunto IDÊNTICO, nome a nome, ao `2105 09/15`**
  (verificado por igualdade de conjuntos) → o boundary 16→17 tem conjunto de **20 ÍNTEGRO**, e é a
  **leitura não contaminada** (a de hoje está contaminada pelo consumo das acelerações);
- **4** repovoadas via `sbs` em `0005 09/16`;
- **2** (`MDMXA#FINAL`, `#FINALPOSTREPORTS`) em `2359 09/16`.

O BMDM enumera os mesmos 26 (a diferença de render é o par AGT1).

## ÁRVORE DE DECISÃO (a executar somente após a leitura)

### Ramo A — boundary de 16.09 NORMALIZOU (READY/`dR`/launch como em 09/11–09/12)

1. Registrar evidência: contagem de READY, `dR`, `AWSBHT036I`, assinatura BATCHMAN vs MAILMAN na janela
   20:5x/21:0x BR do merge do MDM **e** a contraparte UTC no BMDM.
2. Conclusão permitida: **a divergência de domain manager era o bloqueio** (a M1 a removeu).
3. Higiene do plano (cada passo com pré-estado + validação):
   a. Confirmar que a extensão pendente é íntegra **antes** de qualquer `SwitchPlan`.
   b. `SwitchPlan` **somente** com `Symphony` copiado antes e `stop_criterion` armado.
   c. Limpar do plano os registros órfãos do `AGT1` (a workstation já saiu do modelo na M-C) — o plano
      ainda tem `AGT1#CROSS_STREAM 0005 09/16 HOLD` e `AGT1 35 UNIX FTA`.

### Ramo B — boundary de 16.09 PERMANECEU ANÔMALO

1. Registrar a evidência com a **mesma** assinatura da série (22 linhas, só o ciclo do AGT1).
2. Conclusão permitida: a M1 removeu um bloqueio real, **mas não era a causa** do boundary.
3. Próximas hipóteses, em ordem de custo (todas read-only primeiro):
   a. **Esteira/`Sfinal`** — a cadeia `FINAL`→`FINALPOSTREPORTS`→`CHECKSYNC`→`MAKEPLAN` não roda nas noites
      de 09/13 e 09/14; existe um fix documentado no próprio lab (claim `...-plan-rollover-fix-0099`).
      Protocolo do dono: **nunca** rodar `MakePlan` na mão; primeiro `optman ls` + `joblog`; `conman start;mgr`
      para o batchman down; confirmar SUCC em residual.
   b. **Transição run 68→69** (09/12 23:59) e a troca da origem do `UNLINK` do AGT1 (`MDM_BK`→`MDM`).
   c. **Registro órfão do `AGT1` no plano** (run 35 vs 69 do domínio).

## STOP CRITERION (para qualquer ramo)

- **P1** — qualquer mutação fora do lab, ou que toque o PostgreSQL compartilhado, ou que destrua `Sfinal`
  → **parar e escalar**.
- **P2** — `SwitchPlan`/`planman reset`/`crt` sem pré-estado capturado e sem `Symphony` copiado → **não executar**.
- **P3** — o plano ativo perder cobertura de dias futuros após uma operação → **parar imediatamente** e
  restaurar (mapa de reversão abaixo).
- **P4** — recusa do produto não prevista (mensagem nova) → **parar e registrar o limite**, sem tentar
  variantes destrutivas.

## MAPA DE REVERSÃO

| nível | artefato | como restaurar |
|---|---|---|
| 1 | `ws_mdm.def.PRE-M1` / `ws_mdmbk.def.PRE-M1` | `add <arquivo>` + `y` (mesmo mecanismo do composer) — reverte a M1 |
| 2 | `Symphony.pre-extensao` / `planbox.msg.pre-extensao` (em `/tmp/ha_fm/fase2/`, dentro do container) | parar o batchman e repor os arquivos |
| 3 | snapshot `ha_snap_20260914-0035` (tws-hwa 9,28 GB · tws-bmdm 7,27 GB · tws-agent 4,34 GB) | restauração total do lab |
| 4 | definições dos objetos AGT1 removidos na M-C | `/tmp/ha_fm/fase2/pre_*.txt` |

## Fora de escopo até autorização explícita

`planman reset` · `planman crt` · `SwitchPlan` · `JnextPlan` · `conman submit|release|sbs|cs|altjob|switchmgr` ·
`composer add|update`. A recuperação pesada do runbook (`planman reset` + `crt -days 3` + `SwitchPlan` +
`ext`) **não** está autorizada e, pela medição acima, **não é necessária**: o plano ativo tem horizonte
completo até 09/25.
