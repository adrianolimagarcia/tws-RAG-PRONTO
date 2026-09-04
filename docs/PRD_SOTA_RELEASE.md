# PRD — Release SOTA (P0–P6)

Título: Elevar o pipeline HWA/TWS a padrão "ultra-SOTA" — release imutável,
avaliação de alucinação no sistema final, RAG evidence-first, expansão real,
sintético comportamental, function calling e equilíbrio de idioma/contradição.

Status: DRAFT (aguardando aprovação de escopo)
Data: 2026-08-23
Autor: ForgeSDD Agent

## Problema

1. O dataset canônico é mutável: `data/sft/approved.jsonl` e `claims.jsonl`
   mudam a cada rodada, e os relatórios ficam stale (ex.: `ultra_sota_report.json`
   reporta 14.049 approved enquanto `approved.jsonl` tem 14.892). Nenhum treino
   pode ser reprodutível sem um snapshot imutável com manifesto.
2. Não há medição de alucinação no *sistema final* (RAG + modelo), apenas no
   dataset. Falta um blind set separado por fonte e família de prompt com
   métricas independentes (fato, fidelidade, citação, abstention).
3. RAG atual não é "evidence-first": não exige IDs de evidência na resposta,
   não declara insuficiência de suporte, e não sinaliza status da fonte
   (version_dependent / observed_in_lab / community).
4. Há lacunas de conteúdo real de alto valor (incidentes, troubleshooting,
   mutações) e claims sensíveis sem segunda evidência.
5. Contradições entre claims não são auditadas como gate (ex.: `PRIORITY` em
   `$JOBS` — dataset ensina como válido; laboratório 10.2.8 mostra AWSJOM915E).
6. Não há matriz explícita claim × versão × plataforma × status.

## Objetivo

Entregar um release congelado e verificável (P0), um blind eval set de
300–500 casos com 4 métricas (P1), contrato RAG evidence-first (P2),
expansão real priorizada (P3), geração sintética estritamente comportamental
com ablação (P4), function calling coberto conforme o produto (P5) e gate de
contradição + reequilíbrio de idioma (P6).

## Usuários/consumidores

- Modelo fine-tuned (QLoRA) e pipeline RAG consumido pela automação CowAgent.
- Auditores humanos (revisão de claims, blind eval).
- Futuro treino QLoRA (usa somente snapshot imutável).

## Escopo (dentro)

- P0: snapshot imutável + manifesto SHA-256 + gate de regressão por
  idioma/versão/risco/tópico/fonte.
- P1: framework blind eval + seed inicial de casos adversos.
- P2: contrato e validador de respostas evidence-first.
- P3: formato de lab session reproduzível + pesquisa oficial de alta prioridade
  (REST/DWC, incidentes).
- P4: geração sintética comportamental para claims com cobertura baixa +
  pares contrastivos + ablação baseline vs sintético.
- P5: cobertura de function calling conforme o automation-action-registry.
- P6: gate de contradição, matriz de suporte e reequilíbrio do holdout PT/EN.

## Escopo (fora)

- Execução de treino QLoRA real (depende de GPU; apenas dry-runs).
- Validação de laboratório ao vivo (WSL) — depende de disponibilidade do lab;
  o P3 registra formato e backlog.
- Migração de claims históricos sem evidência para "verified" por inferência.

## Requisitos funcionais

- REQ-001: `scripts/release_snapshot.py` gera release imutável com manifesto
  (SHA-256, contagens, gerador, data, fontes, gates).
- REQ-002: `scripts/regression_gate.py` compara releases e falha se qualquer
  dimensão (idioma/versão/risco/tópico/fonte) regredir além de tolerância.
- REQ-003: Config de treino aponta para snapshot imutável, nunca para arquivos
  mutáveis.
- REQ-004: Blind eval set com ≥300 casos, separado por fonte e família de
  prompt, cobrindo 9 famílias adversas; 4 métricas independentes.
- REQ-005: Contrato RAG: resposta factual carrega `evidence_ids`; resposta sem
  suporte suficiente declara insuficiência; sinaliza status da fonte.
- REQ-006: Gate de contradição detecta pares de claims conflitantes
  (mesmo comando/tópico, divergência de escopo/versão) e exige adjudicação.
- REQ-007: Matriz de suporte claim × versão × plataforma × status gerada
  por script a partir de `claims.jsonl`.
- REQ-008: Geração sintética comportamental (3–5 cenários/claim em cobertura
  baixa) com validação estrutural, termos frios, versão, risco e entailment.
- REQ-009: Pares contrastivos (pergunta correta × variação única errada).
- REQ-010: Ablação baseline vs +sintético no holdout cego; promoção apenas se
  melhorar sem piorar falsas recusas.
- REQ-011: Function calling: casos positivos/negativos por ação do registry
  (payload inválido, ação desabilitada, origem inválida, versão incompatível,
  parâmetro ausente, pedido destrutivo).
- REQ-012: Reequilíbrio do holdout por fonte, especialmente PT.

## Requisitos não funcionais

- Reproducibilidade: todo release é imutável e identificado por hash.
- Segurança: nenhum segredo no dataset; validação continua bloqueando
  credenciais/IPs reais (mantendo exceção para versões tipo `10.2.8.00`).
- Escala: scripts processam ~15k SFT / ~1.1k claims em <2 min.
- Auditoria: adjudicações de contradição ficam registradas em arquivo
  versionado.

## Critérios de aceitação

- AC-001: `release_snapshot.py` produz `data/releases/<id>/` com manifesto
  completo e hashes verificáveis (re-hash confere).
- AC-002: `regression_gate.py` passa entre releases compatíveis e falha quando
  uma dimensão regride.
- AC-003: `config.yaml` referencia snapshot imutável (ou documenta o mecanismo).
- AC-004: Blind eval set tem ≥300 casos com as 9 famílias e 4 métricas
  definidas no schema.
- AC-005: Validador RAG rejeita resposta factual sem `evidence_ids` e aprova
  resposta de insuficiência bem formada.
- AC-006: Gate de contradição encontra ≥1 par real (ex.: PRIORITY em $JOBS) e
  produz backlog de adjudicação.
- AC-007: Matriz de suporte gerada com todas as claims.
- AC-008: Candidatos sintéticos passam validação estrutural e entailment;
  ablação reportada.
- AC-009: Candidatos function calling cobrem o registry com negativos.
- AC-010: Holdout PT/EN balanceado por fonte com relatório.

## Métricas de sucesso

- 100% dos validadores verdes no release (evidence, sft, eval, assets, tokens).
- Blind set com ≥300 casos revisados; taxa de aprovação humana documentada.
- Zero resposta factual sem `evidence_ids` no corpus de avaliação.
- Nº de contradições adjudicadas ≥ nº de contradições detectadas (fila zerada
  ou com pendência registrada).
- Cobertura sintética comportamental ≥80% dos claims com cobertura baixa.

## Dependências

- Dados atuais: `claims.jsonl` (1.152), `approved.jsonl` (14.892),
  `eval_independent.jsonl` (3.864), splits (10.890/2.658/1.344).
- Scripts existentes: harness, validadores, splitter, build_eval_gold.
- Lab WSL (para P3/P6 laboratório) e Perplexity (pesquisa oficial).

## Riscos

- Divergência de contagens entre relatórios e arquivos (mitigado por P0).
- Falsos positivos de entailment/contradição (calibrar antes de gate).
- Conteúdo sintético pode inflar sem melhorar holdout (mitigado por ablação).
- Falsas recusas podem aumentar com gates agressivos (métrica separada).

## Perguntas em aberto

- Q1: Deve o snapshot R17 substituir o R16 como baseline? (Recomendação: sim,
  R17 é o estado canônico atual com 1.152 claims.)
- Q2: Tolerância do gate de regressão por dimensão (default: 0% para risco
  destrutivo; 5% para outros)?
- Q3: Function calling é produto final? (Registry existe; resposta: sim para
  automação, cobertura necessária.)
