# Release Report — r24-sota (2026-08-25)

**Snapshot:** `data/releases/r24-sota-20260825-161729/`
**Release anterior:** `r23-sota-20260825-150804` (baseline de regressão)
**Manifesto:** `snapshot_manifest.json` (15 artefatos, SHA-256 por arquivo)

---

## 1. Escopo da rodada

Rodada **hwa-conman-ocli-2026-08-25**: geração de SFT candidates a partir de
56 claims Conman + OCLI já verificadas no dataset ("gap preenchido": estas
claims existiam mas não tinham SFT).

- **112 SFT promovidos** (56 PT / 56 EN), 56 claims (31 conman + 25 ocli)
- Comandos conman: altjob, at absolute, fence, limitcpu, link/unlink, listsucc,
  release sched, reply, rerun, rerunsucc, return codes, running/batch, security
  file, showdomain, showresources, start/stop, status, submit (várias variantes),
  switcheventprocessor, tellop
- Comandos ocli: context (list/new/remove/set/switch), model (add/delete/extract/
  list/lock/mkfolder/modify/replace/rmfolder/catalog), plan (kill/reply/rerun/
  showjobs/submit docommand/job/sched), release job, syntax, version
- Auditoria independente: APROVADO COM RESSALVAS na 1ª rodada (7.2: 3 records p/
  ocli-plan-kill) → corrigido → **FINAL: APROVADO**

## 2. Métricas

### SFT (approved.jsonl)
| Métrica | r23 | r24 | Δ |
|---|---|---|---|
| aprovados | 15629 | 15729 | +100 líquido* |

\* 112 promovidos − 12 removidos (11 respostas duplicadas + 1 prompt normalizado
duplicado de records pré-existentes) = +100 líquido.

- Idiomas: pt=7716 / en=8013
- topic cli_planning: 4713 → **4825** (+112)

### Splits: train=11469 / validation=2818 / test=1443
### Eval: 4200 casos (2100 PT / 2100 EN) — inalterado (sem claims novas)

### Gates: 8/8 PASS (RAG SKIP opcional) · Regression r23→r24: PASS

## 3. Notas técnicas

- Duplicatas detectadas pelo validate_sft (hash normalizado de prompt/resposta)
  com records de rodadas anteriores (ex.: conman-return-codes já tinha SFT com
  "Conman" vs novo "conman") — removidos os novos.
- Laço de correção: promote → validate_all FAIL → remoção de duplicatas →
  validate_all PASS → snapshot r24.