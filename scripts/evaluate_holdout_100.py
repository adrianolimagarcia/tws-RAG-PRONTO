#!/usr/bin/env python3
"""Avaliação do Benchmark Holdout Expandido de 100 Perguntas Inéditas.
Executa em CPU Pura com Two-Stage Retrieval para medição de qualidade definitiva.
"""
import sys, os
sys.path.insert(0, "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval")

import evaluate_rag_benchmark as engine

BENCHMARK_100 = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval/holdout_100_unseen.jsonl"

def main():
    print("==================================================")
    print("  AVALIAÇÃO DO HOLDOUT EXPANDIDO (100 PERGUNTAS)  ")
    print("==================================================")
    engine.BENCHMARK_FILE = BENCHMARK_100
    engine.run_evaluation()

if __name__ == "__main__":
    main()
