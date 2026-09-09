#!/usr/bin/env python3
"""Avaliação Cega com o Cofre Fechado de 50 Perguntas Inéditas.
Executa estritamente em CPU pura sem GPU e sem qualquer intervenção posterior.
"""
import sys, os
sys.path.insert(0, "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval")

import evaluate_rag_benchmark as engine

VAULT_FILE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO/data/eval/blind_holdout_50_vault.jsonl"

def main():
    print("==================================================")
    print("  AVALIAÇÃO DO COFRE FECHADO (50 PERGUNTAS CEGAS) ")
    print("==================================================")
    engine.BENCHMARK_FILE = VAULT_FILE
    engine.run_evaluation()

if __name__ == "__main__":
    main()
