# R17 — Plano de próximos passos (pós-r16 FINAL)

> Base: estado canônico `data/final_snapshot_20260823-051710/` + `data/reconciliation_r16_final2.json`
> claims 1.146 | corpus 17.593 | approved 14.049 | candidates 1 | splits 10.243/2.560/1.246 | eval 2.090 intacto | eval_independent 3.864 | quarantine 4.729
> Status validadores: TODOS PASS (evidence 2 modos, generic 0/14.050, tokens, sft, eval, harness, final_audit Intacto SIM, quality APROVADO COM RESSALVAS)

---

## Fase A — Pendências imediatas do r16 (curto prazo, autônomo)

### A1. Fechar as 38 traduções EN pendentes (rate-limited no P40)
- **O quê**: a fila de tradução PT→EN ficou com 38 itens rate-limited (respostas JSON inválidas do Perplexity).
- **Como**: re-rodar a fila com `pplx_batch.py` (resume) / nova leva; extrair EN válidos; aplicar o mesmo pipeline r16 (limpeza → classificação → integração → dedup → splits → validadores).
- **Critério de saída**: 0 itens pendentes; validadores PASS; manifesto reconciliado (r17).

### A2. Auditoria de qualidade de tradução/proveniência (a "next frontier" anotada)
- **O quê**: auditar os 86 EN integrados vs os PT originais (1:1).
- **Checklist**:
  - Fidelidade: comandos, códigos de erro, paths e nomes preservados (nada de paráfrase que mude semântica).
  - Rejeitar qualquer texto MCP bruto residual (garbage JSON, "Source:", artifacts).
  - Proveniência: os 54 synthetic_factual realmente derivam de fonte oficial (não é community practice disfarçada).
  - Terminologia EN consistente (job stream, workstation, plan, broker, etc.).
- **Entregável**: `docs/r17-en-audit.md` com amostra auditada (n ≥ 20) + veredito por item.

### A3. Ressalvas do final_audit (16.9% não-entailed / 15.5% contradições)
- **O quê**: separar ruído do entailment_audit experimental de problemas reais.
- **Como**: amostrar os pares flagged; se ruído → calibrar/desativar o entailment_audit no gate; se real → corrigir claims/chunks e revalidar.
- **Critério de saída**: final_audit sem ressalvas ou com ressalva documentada e justificada.

---

## Fase B — Decisões de escopo (recomendação + registro)

### B1. Destino da quarentena z/OS (4.729 chunks)
- **Recomendação**: manter quarentenado (escopo DISTRIBUTED decidido) + adicionar `README.md` em `data/quarantine/` com justificativa e procedência (manuais eqq*.pdf).
- **Alternativa**: dataset z/OS separado (EQQ*) para treino futuro específico — só se Adriano quiser expandir escopo.

### B2. 106 pares de alta contenção (10.2 vs 10.2.8)
- **Recomendação**: manter (variações de versão do mesmo manual oficial, esperado em corpus bilíngue) + documentar no quality_report como "conhecido e aceito".
- **Alternativa**: canonicalização de versão (dedup 10.2 em favor de 10.2.8) — não recomendado agora (perde cobertura).

---

## Fase C — Expansão (médio prazo)

### C1. REST API v2 no lab (próximo fronte de lab)
- Claims restv2-* já existem (jwt-cli, payload, model-query, oql). Validar endpoints REST v2 no lab com ocli/composer (ex.: `/twsd/api/v2/`), adicionar runbooks + lab_validation.
- **Gate**: auditoria A2 concluída antes (decisão registrada na memória: "quality audit before REST API v2").

### C2. Synthetic teacher v7 (expansão sintética pós-r15)
- A expansão v6 (8.355 sintéticos) cobre claims até ~r12. Claims novos 0075-0147 (rodadas 13-15) e os 1.146 atuais precisam de cobertura sintética.
- Atualizar `docs/PROGRESS.md` (stale desde 2026-08-21).

### C3. Revalidar cobertura claims ↔ corpus
- coverage_backlog: 9/9 tópicos, 0 missing — revalidar com claims 1.146 pós-r16 (novos claims podem ter criado lacunas de chunk).

---

## Fase D — Entrega final (longo prazo)

### D1. Export + fine-tune
- Dataset pronto (snapshot canônico). Exportar shard de treino (`extract_tune_shard.py`), rodar fine-tune, avaliar com `eval_independent` (3.864).
- Documentar hyperparâmetros e resultado (loss, métricas) em `docs/`.

### D2. Release/versão
- Changelog r16→r17, tag de versão do dataset, integração com CowAgent (RAG) e documentação de consumo.

---

## Ordem de execução sugerida (autônoma)

```
A1 → A2 → A3 → (gate: auditoria ok) → B1+B2 (registro) → C1 → C2 → C3 → D1 → D2
```

- A1–A3: 1–2 sessões, 100% autônomo.
- B1–B2: decisões documentadas (recomendações acima), sem bloqueio.
- C1: depende de lab disponível (WSL2 wauser).
- D1: depende de ambiente de treino (GPU).

## Riscos
- 38 traduções podem re-introduzir texto MCP bruto → pipeline r16 de limpeza obrigatório.
- entailment_audit pode estar gerando falsos positivos → calibrar antes de confiar.
- REST API v2 pode exigir credenciais/escopos novos no lab (lição r12: JWT é por ferramenta).
