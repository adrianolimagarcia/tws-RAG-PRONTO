# Roadmap de Qualidade do Dataset HWA 10.2.8

> Gerado: 2026-08-23 | Estado base: claims 1.152 | corpus 17.625 | approved 14.892 | eval_independent 3.864

## 1. Diagnóstico atual (pontos fracos identificados)

| # | Fraqueza | Evidência |
|---|---|---|
| F1 | **Corpus 92% EN** — RAG desbalanceado | corpus: en 16.323 / pt 999 / mixed 303 |
| F2 | **Function calling subdesenvolvido** — só 49 records p/ 39 actions | approved: 49 de 14.892 (0,3%) |
| F3 | **79 claims sem cobertura SFT** | 39 version_dependent + 14 verified + 14 community + 9 observed + 2 contradicted + 1 insuficiente |
| F4 | **Citações raras** — só 14% das respostas citam fonte | 2.078 de 14.892 |
| F5 | **Cenários sintéticos finos** — média ~1,4 cenários/claim | 14.892 records / 1.073 claims |
| F6 | **Sem eval adversarial** — nada testa recusa/alucinação | eval_independent só cobre claims |
| F7 | **Contradições entre chunks não auditadas** | entailment_audit v7 ruidoso, nunca aplicado no approved |
| F8 | **Versões antigas no corpus** (9.5, 9.4, 8.5.1.1, 8.3.0) sem marcação forte | corpus: 9.5=921, 9.4=883, 8.5.1.1=314, 8.3.0=76 |
| F9 | **Sem exemplos reais de sessão CLI** no SFT | tudo é sintético/natural, nada capturado do lab |
| F10 | **REST API v2 sub-representada** no SFT | 304 chunks wa-api3-v2-rest no corpus, mas poucos claims SFT dedicados |

## 2. Eixos de melhoria — opções detalhadas

### EIXO A — MAIS CONTEÚDO (fonte oficial/primária)

| Opção | Descrição | Impacto anti-alucinação | Esforço |
|---|---|---|---|
| **A1. Manuais 10.2.8 faltantes** | Processar PDFs ainda não chunked: `awsdwc*` (DWC), `awsusr*` (User's Guide), `awsocl*` (OCLI), `awsdb2/oracle/mssql*` (DB), `awsbestpract*` (best practices — já existe no MANUAIS mas sem chunks?) | 🔥 Alto — fecha lacunas de tópicos | Médio |
| **A2. Sessões reais do lab** | Capturar execuções reais de ocli/conman/composer no lab (com saídas reais) → pares (comando, saída real) como exemplos SFT | 🔥🔥 Muito alto — exemplos autênticos, zero alucinação | Baixo (lab já disponível) |
| **A3. REST API v2 com payloads reais** | Gerar exemplos curl + payloads + respostas reais da REST API v2 (spec já extraída) | 🔥 Alto | Baixo |
| **A4. Runbooks de recovery expandidos** | Symphony/FTA/plan recovery em mais variações (master, FTA, agent, eventos) | 🔥 Alto — incidents são o maior risco de alucinação | Médio |
| **A5. Exemplos negativos oficiais** | Extrair do Troubleshooting Guide os casos "sintoma→causa→resolução" como triplos estruturados | 🔥 Alto | Médio |

### EIXO B — TREINAMENTO SINTÉTICO (mais rico)

| Opção | Descrição | Impacto | Esforço |
|---|---|---|---|
| **B1. Expandir cenários por claim** | Gerar 3-5 cenários por claim (hoje ~1,4): technical, beginner, cli_operation, troubleshooting, comparison, edge_case, version_platform, risk_confirmation | 🔥 Alto — mais variação = menos overfitting, mais robustez | Baixo (pipeline existe) |
| **B2. Hard negatives reais** | false_premise com negações de versão/plataforma: "no z/OS posso usar X?" (deve recusar/corrigir), "no 9.5 tem Y?" (deve diferenciar versão) | 🔥🔥 Muito alto — treina recusa de info errada | Médio |
| **B3. Multi-turn troubleshooting** | Conversas em cadeia (2-3 turnos) de diagnóstico: sintoma → investigação → resolução. Requer ajustar ROLES do validador | 🔥 Alto — cenário real de uso | Médio |
| **B4. Function calling massivo** | Gerar 20-50 exemplos por action do registry (39 actions × PT/EN × variações) com payloads corretos + recusas para ações não autorizadas | 🔥🔥 Muito alto — habilidade prática | Médio |
| **B5. RAG-grounded synth** | Gerar Q&A estritamente ancorado em chunks (pergunta só sobre o chunk, resposta só do chunk) → base para RAG eval e fine-tune de retrieval | 🔥 Alto — grounding forte | Médio |
| **B6. Paraphrase adversarial** | Reformular perguntas com vocabulário coloquial/errado ("como faço pra rodar o job?") para robustez | Médio | Baixo |

### EIXO C — ANTI-ALUCINAÇÃO ESTRUTURAL

| Opção | Descrição | Impacto | Esforço |
|---|---|---|---|
| **C1. Refusal/out-of-scope training** | Pares: pergunta fora de escopo (produto diferente, versão não suportada, plataforma errada) → resposta de recusa calibrada ("não suportado no escopo/versão") | 🔥🔥🔥 Crítico — ataca alucinação na raiz | Médio |
| **C2. Version awareness reforçada** | Cada resposta deve ancorar a versão (10.2.8); treinar recusa quando a versão da pergunta é ambígua ou divergente | 🔥🔥 Muito alto | Médio |
| **C3. Citações nas respostas** | Aumentar de 14% para ~40%+ das respostas com referência (source_url/supporting_quote do claim) | 🔥🔥 Muito alto — permite verificação | Baixo (metadados existem) |
| **C4. Auditoria de contradições no approved** | Rodar pairwise/entailment entre respostas do mesmo claim (paráfrases) e entre claims vizinhos → eliminar respostas conflitantes | 🔥🔥 Muito alto — remove info contraditória | Médio |
| **C5. Hedging/confidence** | Para version_dependent/community: treinar expressões de incerteza ("depende da versão", "prática comum, verifique") | 🔥 Alto | Baixo |
| **C6. Validador de termos frios no approved** | Garantir que toda resposta contém o código/comando do claim (sem inventar AWS* inexistentes) | 🔥🔥 Muito alto — zero código inventado | Baixo |
| **C7. Version pinning no corpus** | Completar metadados de versão nos chunks antigos (9.5/9.4/8.5.1.1) para RAG não misturar | 🔥 Alto | Baixo |

### EIXO D — AVALIAÇÃO (medir = melhorar)

| Opção | Descrição | Impacto | Esforço |
|---|---|---|---|
| **D1. eval_adversarial** | Novo eval com perguntas out-of-scope, versões erradas, entidades falsas → deve recusar (mede alucinação diretamente) | 🔥🔥🔥 Crítico | Médio |
| **D2. eval_factual_consistency** | LLM-as-judge: resposta vs claim/source (entailment) em amostra grande | 🔥🔥 Alto | Médio |
| **D3. eval_function_calling** | Payloads corretos/incorretos para as 39 actions | 🔥 Alto | Baixo |
| **D4. eval_RAG** | Recuperação: pergunta → chunk certo retornado (recall@k) | 🔥 Alto | Médio |
| **D5. eval_cross_version** | Pergunta sobre 9.5 → resposta não deve conter info de 10.2.8 (e vice-versa) | 🔥🔥 Alto | Baixo |

### EIXO E — PROCESSO/VERIFICAÇÃO

| Opção | Descrição | Impacto | Esforço |
|---|---|---|---|
| **E1. Fechar 79 claims sem cobertura** | version_dependent (39) com cenário version_platform; community (14) com disclaimer; observed (9) com lab; verified (14) restantes | 🔥 Alto — completude | Baixo |
| **E2. Proveniência claim↔chunk** | Vincular chunks do corpus aos claims (hoje corpus não referencia claims) → rastreabilidade total | Médio | Médio |
| **E3. Curadoria community** | Padronizar disclaimer nos 14 claims community_practice | Médio | Baixo |
| **E4. Calibrar entailment_audit** | Corrigir os falsos positivos (regex IP, versão) e aplicar no approved como gate | 🔥 Alto | Médio |
| **E5. Consistência EN/PT** | Os 999 chunks PT vs EN: garantir que traduções são fiéis (auditoria já feita nos 86, estender) | Médio | Médio |

## 3. Priorização recomendada (impacto × esforço)

### 🚀 Fase 1 — "Núcleo anti-alucinação" (alto impacto, baixo-médio esforço)
1. **C1 + D1** — Refusal/out-of-scope training + eval adversarial (par — treinar e medir)
2. **C6** — Validador de termos frios no approved (zero código inventado)
3. **C4** — Auditoria de contradições no approved
4. **A2** — Sessões reais do lab (exemplos autênticos)

### 🔥 Fase 2 — "Riqueza sintética" (médio esforço)
5. **B4** — Function calling massivo (39 actions × variações)
6. **B1** — Expandir cenários para 3-5 por claim
7. **B2** — Hard negatives de versão/plataforma
8. **C3** — Citações em ~40% das respostas

### 📚 Fase 3 — "Conteúdo e avaliação" (médio-alto esforço)
9. **A1** — Manuais 10.2.8 faltantes (DWC, OCLI, DBs, best practices)
10. **D2/D3/D4/D5** — Suíte de evals especializados
11. **B5** — RAG-grounded synth
12. **E1** — Fechar os 79 claims restantes

### 🧹 Fase 4 — "Higiene e rastreabilidade"
13. **C7** — Version pinning no corpus
14. **E2/E4/E5** — Proveniência, entailment calibrado, consistência PT/EN

## 4. Métricas de sucesso (definir antes de começar)

| Métrica | Hoje | Meta |
|---|---|---|
| Cobertura de claims no SFT | 1.073/1.152 (93%) | 1.130+ (98%) |
| Records com citação | 14% | 40%+ |
| Function calling records | 49 | 1.000+ |
| Cenários por claim | ~1,4 | 3+ |
| eval_adversarial (recusa correta) | — | 95%+ |
| Códigos AWS* inventados no approved | — | 0 |
| Contradições entre respostas do mesmo claim | — | 0 |
