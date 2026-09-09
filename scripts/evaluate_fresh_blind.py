#!/usr/bin/env python3
"""Avaliação Cega com Holdout Novo de 40 Perguntas Inéditas.
Testa o pipeline em CPU Pura sem nenhuma modificação de código ou ajuste fino.
"""
import sys, os
sys.path.insert(0, "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval")

import evaluate_rag_benchmark as engine

TEST_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval/fresh_blind_test_40.jsonl"

def main():
    print("==================================================")
    print("  AVALIAÇÃO CEGA FRESH (HOLDOUT PURO - 40 Qs)     ")
    print("==================================================")
    engine.BENCHMARK_FILE = TEST_FILE
    engine.run_evaluation()

if __name__ == "__main__":
    main()
