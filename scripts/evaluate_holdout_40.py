#!/usr/bin/env python3
"""Avaliação do Benchmark Holdout de 40 Perguntas Inéditas em CPU Pura."""
import sys, os
sys.path.insert(0, "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval")
import evaluate_rag_benchmark as engine

BENCHMARK_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval/holdout_40_test.jsonl"

def main():
    print("==================================================")
    print("    AVALIAÇÃO DO BENCHMARK DE 40 PERGUNTAS       ")
    print("==================================================")
    engine.BENCHMARK_FILE = BENCHMARK_FILE
    engine.run_evaluation()

if __name__ == "__main__":
    main()
