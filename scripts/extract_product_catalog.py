#!/usr/bin/env python3
"""P1b — Extrai mensagens do catalogo COMPILADO do proprio produto (fonte autoritativa 10.2.8).

Os arquivos /opt/hwa/TWS/catalog/C/*.cat contem os pares "<CODIGO> <texto>" separados por \x00.
Isso da a fonte definitiva: o texto exato da versao instalada, sem ressalva de versao.
Saida: data/export/tws_messages_catalog_product.jsonl
"""
import json, re, os, sys

CAT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/opt/hwa/TWS/catalog/C"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/tws_messages_catalog_product.jsonl"

# CODIGO + espaco + texto (ate o proximo \x00)
MSG_RE = re.compile(rb"(AWS[A-Z0-9]{3}[0-9]{3}[IWE])\s+([^\x00]{1,2000})")


def main():
    msgs = {}
    per_file = {}
    for fn in sorted(os.listdir(CAT_DIR)):
        if not fn.endswith(".cat"):
            continue
        raw = open(os.path.join(CAT_DIR, fn), "rb").read()
        found = 0
        for m in MSG_RE.finditer(raw):
            code = m.group(1).decode("ascii", "replace")
            text = m.group(2).decode("utf-8", "replace").strip()
            text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
            text = re.sub(r"\s+", " ", text).strip()
            if not text or len(text) < 4:
                continue
            # manter a ocorrencia com texto mais longo (mais informativa)
            if code not in msgs or len(text) > len(msgs[code]["text"]):
                msgs[code] = {"code": code, "text": text, "catalog_file": fn,
                              "source_url": "produto instalado: /opt/hwa/TWS/catalog/C/" + fn}
            found += 1
        per_file[fn] = found

    with open(OUT, "w", encoding="utf-8") as f:
        for code in sorted(msgs):
            f.write(json.dumps(msgs[code], ensure_ascii=False) + "\n")

    print("por arquivo:", json.dumps(per_file, indent=0).replace("\n", " "))
    print(f"TOTAL de codigos unicos com texto: {len(msgs)}")
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
