#!/usr/bin/env python3
"""Executa a avaliação cega (blind test) contra o dataset holdout de 30 perguntas inéditas
utilizando exatamente a mesma pipeline de recuperação e re-ranking de produção.
"""
import sys, os
sys.path.insert(0, "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval")

import evaluate_rag_benchmark as engine
import json

BLIND_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval/realistic_blind_holdout_30.jsonl"

def main():
    print("==================================================")
    print("   AVALIAÇÃO CEGA (BLIND HOLDOUT TEST - 30 Qs)    ")
    print("==================================================")
    
    # Redirecionar o arquivo de benchmark para o dataset cego
    engine.BENCHMARK_FILE = BLIND_FILE
    engine.EVAL_SUMMARY_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval/blind_eval_summary.json"
    
    engine.run_evaluation()

if __name__ == "__main__":
    main()
