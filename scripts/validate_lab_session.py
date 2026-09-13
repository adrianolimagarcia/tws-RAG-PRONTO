#!/usr/bin/env python3
"""validate_lab_session.py — Validador do LAB_SESSION_FORMAT (docs/LAB_SESSION_FORMAT.md).

Motivo: o workflow de laboratório documentava um validador que NUNCA foi versionado
(`scripts/add_lab_evidence.py` nao existe no repo) e o `ci_dataset_gate.py` validava
apenas a sintaxe JSONL. Resultado: deriva de schema sistemica (registros sem `result`
ou com texto livre fora do enum). Este script impoe o schema por maquina.

Regras:
- Campos obrigatorios do schema.
- `result` DEVE estar no enum: SUCCESS | FAIL | REJECTED | PARTIAL.
- `risk` DEVE estar no enum: read_only | mutating | destructive | credential_sensitive.
- Scan de segredos (mesmos padroes do gate de CI).

Baseline de legados: `data/evidence/lab_session_schema_baseline.json` congela, POR ARQUIVO,
a contagem de violacoes historicas. O validador NAO silencia o legado: ele REPORT A a contagem
e FALHA se um arquivo legado EXCEDER a contagem congelada (isto e, se registros NOVOS
introduzirem novas violacoes). Arquivos fora do baseline sao validados ESTRITAMENTE.

Uso:
  python3 scripts/validate_lab_session.py                 # valida o diretorio (modo CI)
  python3 scripts/validate_lab_session.py --write-baseline # congela o baseline de legados
  python3 scripts/validate_lab_session.py --record f.json  # valida UM registro (teste)
"""
import argparse
import glob
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = REPO / "data" / "evidence"
BASELINE_FILE = EVIDENCE_DIR / "lab_session_schema_baseline.json"
LAB_GLOB = "lab-validation-*.jsonl"

REQUIRED_FIELDS = [
    "claim_id", "command", "preconditions", "sanitized_output", "result",
    "product_version", "platform", "risk", "reversibility", "stop_criterion",
    "evidence_url", "performed_at", "performed_by", "observations",
]
RESULT_ENUM = {"SUCCESS", "FAIL", "REJECTED", "PARTIAL"}
RISK_ENUM = {"read_only", "mutating", "destructive", "credential_sensitive"}

SECRET_PATTERNS = [
    re.compile("ghp" + "_" + "[A-Za-z0-9]{20,}"),
    re.compile(r"BEGIN\s+[A-Z\s]+PRIVATE\s+KEY"),
    re.compile(r'password\s*[:=]\s*["\'](?!\[REDACTED\]|\{aes\}|\(conforme|<placeholder>)[^"\']{6,}["\']', re.I),
    re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"),
]


def validate_record(rec):
    """Retorna a lista de violacoes de UM registro."""
    v = []
    if not isinstance(rec, dict):
        return ["registro nao e um objeto JSON"]
    for f in REQUIRED_FIELDS:
        if f not in rec or rec[f] in (None, "", [], {}):
            v.append(f"campo obrigatorio ausente/vazio: {f}")
    r = rec.get("result")
    if isinstance(r, str) and r not in RESULT_ENUM:
        v.append(f"result fora do enum ({r!r}); esperado SUCCESS|FAIL|REJECTED|PARTIAL")
    rk = rec.get("risk")
    if isinstance(rk, str) and rk not in RISK_ENUM:
        v.append(f"risk fora do enum ({rk!r})")
    blob = json.dumps(rec, ensure_ascii=False)
    for pat in SECRET_PATTERNS:
        if pat.search(blob):
            v.append(f"padrao sensivel detectado: {pat.pattern[:40]}")
    return v


def scan_dir():
    """Retorna {arquivo: n_violacoes} para todos os lab-validation-*.jsonl."""
    out = {}
    for path in sorted(glob.glob(str(EVIDENCE_DIR / LAB_GLOB))):
        n = 0
        for line in open(path, encoding="utf-8", errors="ignore"):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except Exception:
                n += 1
                continue
            n += len(validate_record(rec))
        out[os.path.basename(path)] = n
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-baseline", action="store_true")
    ap.add_argument("--record", help="arquivo JSON com UM registro a validar")
    args = ap.parse_args()

    if args.record:
        rec = json.load(open(args.record, encoding="utf-8"))
        v = validate_record(rec)
        if v:
            print(f"INVALIDO ({len(v)} violacoes):")
            for x in v:
                print("  -", x)
            return 1
        print("VALIDO: registro conforme o LAB_SESSION_FORMAT.")
        return 0

    counts = scan_dir()
    if args.write_baseline:
        with open(BASELINE_FILE, "w", encoding="utf-8") as fh:
            json.dump(counts, fh, ensure_ascii=False, indent=1, sort_keys=True)
        print(f"baseline gravado: {BASELINE_FILE} ({len(counts)} arquivos, "
              f"{sum(counts.values())} violacoes historicas)")
        return 0

    baseline = {}
    if BASELINE_FILE.exists():
        baseline = json.load(open(BASELINE_FILE, encoding="utf-8"))

    print("=== Validador LAB_SESSION_FORMAT ===")
    legacy_files = 0
    legacy_viol = 0
    new_viol = 0
    failures = []
    for fname, n in sorted(counts.items()):
        if fname in baseline:
            legacy_files += 1
            legacy_viol += baseline[fname]
            if n > baseline[fname]:
                failures.append(f"{fname}: {n} violacoes > baseline congelado {baseline[fname]} "
                                f"(registros NOVOS introduziram violacoes)")
        else:
            if n:
                failures.append(f"{fname}: {n} violacoes (arquivo NOVO, sem baseline)")
                new_viol += n
    print(f"legado (allowlist): {legacy_files} arquivos, {legacy_viol} violacoes historicas "
          f"(NAO silenciadas — apenas congeladas)")
    print(f"arquivos novos com violacao: {len([f for f in failures if 'NOVO' in f])}")
    if failures:
        print("FALHAS:")
        for f in failures:
            print("  -", f)
        return 1
    print("OK: nenhum registro novo viola o schema.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
