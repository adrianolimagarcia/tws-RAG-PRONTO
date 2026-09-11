#!/usr/bin/env python3
"""P1 — Extrai o catalogo de mensagens HWA das paginas oficiais de message help (v95).

Para cada familia AWSxxx, baixa https://help.hcl-software.com/workloadautomation/v95/common/src_ms/awsmsaws<fam>.html
e parseia os <article id="AWSxxxNNNY"> extraindo: codigo, texto (msgText), explicacao (msgExplanation),
resposta ao usuario (msgResponse). Salva JSONL incremental no workspace.
"""
import re, json, os, sys, time, urllib.request

BASE = "/run/media/adriano/e681b5ac-a4fb-44d4-aebf-9d6584065787/projetos/tws-RAG-PRONTO"
OUT = f"{BASE}/data/export/tws_messages_catalog_v95.jsonl"
FAM_FILE = "/tmp/real_codes.txt"
UA = {"User-Agent": "Mozilla/5.0"}


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def clean(s):
    s = re.sub(r"<var[^>]*>(.*?)</var>", r"\1", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&quot;", '"').replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&#39;", "'")
    return re.sub(r"\s+", " ", s).strip()


def parse(html):
    """Extrai cada mensagem como um bloco <article id="CODIGO">."""
    out = []
    for m in re.finditer(r'<article[^>]*id="(AWS[A-Z]{3}[0-9]{3}[IWE])"[^>]*>(.*?)</article>', html, re.S):
        code, body = m.group(1), m.group(2)
        def sect(cls):
            mm = re.search(r'<[^>]*class="[^"]*' + cls + r'[^"]*"[^>]*>(.*?)</(?:p|section|div)>', body, re.S)
            return clean(mm.group(1)) if mm else ""
        rec = {
            "code": code,
            "text": sect("msgText"),
            "explanation": sect("msgExplanation"),
            "response": sect("msgResponse"),
        }
        if rec["text"]:
            out.append(rec)
    return out


def main():
    fams = sorted({l.strip()[3:6] for l in open(FAM_FILE) if l.strip().startswith("AWS")})
    print(f"familias a processar: {len(fams)}", flush=True)
    seen, n_ok, n_fail = set(), 0, 0
    with open(OUT, "w", encoding="utf-8") as fo:
        for i, fam in enumerate(fams, 1):
            url = f"https://help.hcl-software.com/workloadautomation/v95/common/src_ms/awsmsaws{fam.lower()}.html"
            try:
                msgs = parse(fetch(url))
            except Exception as e:
                msgs = []
                print(f"  [{i}/{len(fams)}] {fam}: ERRO {e}", flush=True)
            if msgs:
                n_ok += 1
            else:
                n_fail += 1
            for r in msgs:
                if r["code"] in seen:
                    continue
                seen.add(r["code"])
                r["source_url"] = url
                r["source_version"] = "9.5"
                fo.write(json.dumps(r, ensure_ascii=False) + "\n")
            if i % 15 == 0:
                print(f"  [{i}/{len(fams)}] familias | {len(seen)} mensagens acumuladas", flush=True)
            time.sleep(0.4)
    print(f"FIM: familias OK={n_ok} vazias={n_fail} | mensagens unicas={len(seen)} -> {OUT}", flush=True)


if __name__ == "__main__":
    main()
