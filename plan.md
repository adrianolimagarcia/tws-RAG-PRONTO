# PLANO DE EXECUÇÃO: ENRIQUECIMENTO OFFLINE DO DATASET (DOC2QUERY & METADADOS)

## Objetivo
Elevar a performance do 1º estágio (BM25 e denso leve) offline para eliminar a necessidade de re-ranker neural pesado online (reduzindo latência de 1.700ms para <50ms e consumo de GPU a zero), preservando a conformidade estrita contra vazamento (`audit_eval_leakage.py`).

## Fases
- [x] Fase 0: Validação de Re-ranker (Large deu +20 pp no holdout e +29 acertos no pool 423, confirmando teto de ordenação)
- [x] Fase 1: Piloto do Enriquecedor Offline via `gemini-3.8-flash-medium` testado com sucesso
- [x] Fase 2: Enriquecer em lote (concorrência) os claims prioritários e claims sem `synthetic_questions`
- [x] Fase 3: Integrar o corpus enriquecido de forma aditiva e validar com o auditor anti-leakage (`audit_eval_leakage.py`)
- [x] Fase 4: Avaliar impacto no benchmark de nível-resposta com `measure_resposta.py` e registrar evidência formal


