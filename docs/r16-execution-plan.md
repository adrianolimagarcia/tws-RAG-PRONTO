# Plano R16-FINAL — Fechamento do lote de tradução EN (86 chunks)

Estado: 2026-08-23 · Atitude: harness / ultra-sota / autônomo
Autor: Cowbot (execução autônoma sob instrução de Adriano)

## Contexto

Lote r16 = 86 chunks PT traduzidos para EN via Perplexity (`temp/r16_en_clean.jsonl`).
O run anterior (`temp/reconcile_r16.py`) integrou só 42/86 EN no corpus e marcou 43 como
"rejected" por critério excessivamente agressivo (sufixo `Source:` vazio e substring MCP/Perplexity).
Relatórios (`quality_report.json`, `ultra_sota_report.json`) estão stale e não representam o estado final.
`validate_tokens.py` nunca rodou (falta `transformers`).

## Fases

0. Congelar e contar (FEITA — ver números abaixo)
1. Higienizar `temp/r16_en_clean.jsonl` (86): limpar sufixos vazios, preservar citações reais, rejeitar só MCP bruto
2. Mapear 1:1 PT↔EN (chunk 2634-2719 + `translated_from`)
3. Classificar os 86: oficial / synthetic factual / community practice / boundary-EEL
4. Auditar EQQ/z/OS/EEL em claims + corpus + approved → quarentena do que viola escopo
5. Integrar seletivamente os EN aprovados (factual) no corpus; community → RAG-only; nunca eval
6. Dedup real (medir impacto antes; aplicar só o comprovado)
7. Regenerar corpus e splits com scripts canônicos
8. Validadores: evidence (+strict), generic, tokens (instalar transformers), ultra_sota, final_audit, validate_sft, validate_eval
9. Reconciliação de manifestos (zero divergência, zero vazamento holdout↔treino)
10. Snapshot final + atualizar knowledge base

## Estado congelado (Fase 0)

claims 1.146 | corpus 22.280 | corpus_full/train_full/eligible_full 17.723 |
train_source_holdout 17.116 | eval_buffer 20.839 | eval 2.090 | train 15.003 |
approved 14.049 (pt 6.974/en 7.075) | candidates 3.287 | splits 10.243/2.560/1.246 |
eval_independent 3.864 | en_clean 86 (42 EN já no corpus) | quarantine 0

## Riscos / notas
- validate_tokens exige transformers (pip install).
- Família eqqr1mst (~1.368 em train) é z/OS → candidata a quarentena por política de escopo.
- Dedup full pode reduzir approved — medir antes; se agressivo demais, só dedup exato/near-dup comprovado.
