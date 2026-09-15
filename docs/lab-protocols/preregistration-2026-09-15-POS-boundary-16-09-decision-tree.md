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
