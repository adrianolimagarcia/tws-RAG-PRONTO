#!/usr/bin/env python3
"""build_honest_splits.py — splits TREINO/TESTE disjuntos por EVIDENCIA, nao por pergunta.

POR QUE ISTO EXISTE
-------------------
O `decontaminated-manifest.json` admite explicitamente o que NAO foi corrigido:
    "escopo_nao_corrigido": ["7-split (309 FAIL)", "8-duplicata (446 FAIL)"]
E mesmo os checks 7 e 8 do `audit_eval_leakage.py` sao apenas "pergunta em dois arquivos"
e "pergunta quase-duplicada entre arquivos". Nenhum dos dois pega o vazamento mais grave:

    a mesma EVIDENCIA (claim/runbook) aparecendo no TREINO e no TESTE.

Se a mesma claim fundamenta uma pergunta de treino e uma de teste, um modelo que decora a
claim acerta o teste - e a metrica de teste para de medir generalizacao. Este script ataca
exatamente isso.

COMO
----
1. Deduplica perguntas por TEXTO NORMALIZADO (o `7-split` sozinho ja' acusava 309).
2. Agrupa perguntas em CLUSTERS DE EVIDENCIA por uniao-find: duas perguntas entram no mesmo
   cluster se compartilham QUALQUER claim relevante (e, opcionalmente, qualquer runbook).
   Um cluster e' indivisivel - ou vai inteiro para treino, ou inteiro para teste.
3. Distribui clusters inteiros entre treino/teste de forma DETERMINISTICA e balanceada
   (maiores primeiro, para o lado mais distante do alvo). Sem RNG: reproduzivel por construcao.
4. Emite manifesto + FALHA se qualquer invariante de disjuncao for violada.

O QUE ELE **NAO** FAZ (e por que)
---------------------------------
* Nao gera perguntas novas. O benchmark V4 (sealed holdout) exige perguntas que nao possam
  ser derivadas do corpus - e este repo ja' provou por medicao que gerar do corpus produz
  perguntas tautologicas. Isso continua BLOQUEADO por entrada humana.
* Nao torna o benchmark "justo" com o mundo. Ele torna o par treino/teste NAO-VAZADO entre
  si, que e' o requisito minimo para qualquer numero de "generalizacao" significar algo.

USO
---
  python3 scripts/build_honest_splits.py                 # constroi e valida
  python3 scripts/build_honest_splits.py --test-pct 33   # fracao alvo do teste
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import re

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

IN_DIR = REPO / "data" / "eval" / "decontaminated"
OUT_DIR = REPO / "data" / "eval" / "splits" / "honest_v1"

# Ordem de prioridade na deduplicacao: do mais curado para o mais derivado. A copia de
# menor prioridade e' descartada, para que um arquivo sintetico nao substitua o original.
PRIORITY = [
    "golden_qa_benchmark.jsonl",
    "golden_qa_messages_benchmark.jsonl",
    "golden_qa_virgin_benchmark.jsonl",
    "holdout_100_unseen.jsonl",
    "holdout_40_test.jsonl",
    "blind_v3_slices.jsonl",
    "blind_holdout_50_vault.jsonl",
    "fresh_blind_test_40.jsonl",
    "realistic_blind_holdout_30.jsonl",
    "blind_holdout_qa_30.jsonl",
    "pure_virgin_test_40.jsonl",
    "rest_api_benchmark_40.jsonl",
    "rest_api_benchmark_ops_40.jsonl",
    "rest_api_zeroshot_variantA.jsonl",
    "rest_api_zeroshot_variantB.jsonl",
    "golden_qa_virgin_en_benchmark.jsonl",
    "golden_qa_virgin_expanded.jsonl",
    "blind_v3_slice_d_manual.jsonl",
]


def norm(text: str) -> str:
    """Normalizacao para comparar perguntas. Igual em espirito ao `norm` do
    audit_eval_leakage.py: minusculas, sem acento, sem pontuacao, espaco colapsado."""
    import unicodedata
    t = unicodedata.normalize("NFKD", text or "")
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower()
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def load_rows():
    """Le os benchmarks decontaminados. Retorna lista de (arquivo, indice, linha)."""
    rows = []
    for name in sorted(os.listdir(IN_DIR)):
        if not name.endswith(".jsonl"):
            continue
        if "negatives" in name:
            continue
        for i, line in enumerate((IN_DIR / name).read_text(encoding="utf-8").splitlines()):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            rows.append((name, i, obj))
    return rows


def corpus_claim_ids():
    """Ids do corpus CARREGADO, pelo loader REAL do repo - nao por uma reimplementacao.
    Reusar o loader evita a classe de erro que ja' invalidou medicoes neste projeto:
    medir um corpus que o repo nao executa."""
    from rag_core.corpus import load_documents
    return {d["id"] for d in load_documents()}


class DSU:
    def __init__(self):
        self.pai = {}

    def find(self, x):
        self.pai.setdefault(x, x)
        while self.pai[x] != x:
            self.pai[x] = self.pai[self.pai[x]]
            x = self.pai[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.pai[rb] = ra


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--test-pct", type=float, default=33.0,
                    help="fracao alvo de CLUSTERS no teste (default 33)")
    ap.add_argument("--sem-runbook", action="store_true",
                    help="NAO liga perguntas que compartilham runbook_ref. Default e' ligar "
                         "(mais estrito): so' ha' ~13 runbooks no total, entao o custo de "
                         "acoplar por runbook e' baixo e a disjuncao e' mais forte.")
    ap.add_argument("--ambos", action="store_true",
                    help="emite as DUAS variantes (estrita e so'-claim) e compara o "
                         "compromisso entre disjuncao e representatividade")
    ap.add_argument("--out", default="honest_v1", help="subdiretorio de data/eval/splits/")
    args = ap.parse_args()

    if args.ambos:
        return ambos(args)

    return constroi(args, args.sem_runbook, OUT_DIR.parent / args.out)


def ambos(args):
    """Emite as duas variantes e imprime o COMPROMISSO medido.

    Estrita  = cluster por claim E runbook. Disjuncao total, mas um runbook "cola" dezenas
               de perguntas de topicos diferentes -> cluster gigante -> o teste pode ficar
               concentrado em poucos runbooks.
    So'-claim = cluster apenas por claim. Representatividade melhor, mas perguntas de treino
               e teste podem citar o MESMO runbook (o teste ainda e' claim-disjunto, que e'
               a evidencia que de fato fundamenta a resposta).

    Nenhuma das duas e' "a certa": o script mostra o numero das duas.
    """
    import io
    import contextlib
    res = {}
    for sem_rb, nome in ((False, "honest_v1"), (True, "honest_v1_claim")):
        buf = io.StringIO()
        a = argparse.Namespace(**vars(args))
        a.sem_runbook = sem_rb
        with contextlib.redirect_stdout(buf):
            rc = constroi(a, sem_rb, OUT_DIR.parent / nome)
        res[nome] = {"rc": rc, "log": buf.getvalue()}
        print("=" * 78)
        print("VARIANTE: %s   (runbook %s)" % (nome, "ACOPLADO" if not sem_rb else "livre"))
        print("=" * 78)
        print(buf.getvalue().rstrip())
    return 0 if all(v["rc"] == 0 for v in res.values()) else 1


def constroi(args, sem_runbook, out_dir):
    rows = load_rows()
    print(f"linhas lidas dos benchmarks decontaminados: {len(rows)}")

    # --- 1. dedup por texto normalizado ------------------------------------
    visto: dict[str, tuple[str, int, dict]] = {}
    descartadas_dup = collections.Counter()
    for name, i, obj in rows:
        q = norm(obj.get("question", ""))
        if not q:
            continue
        prio = PRIORITY.index(name) if name in PRIORITY else len(PRIORITY)
        if q in visto:
            old_prio = PRIORITY.index(visto[q][0]) if visto[q][0] in PRIORITY else len(PRIORITY)
            descartadas_dup[name] += 1
            if prio < old_prio:
                visto[q] = (name, i, obj)
            continue
        visto[q] = (name, i, obj)
    unicas = list(visto.values())
    print(f"perguntas DISTINTAS apos dedup por texto: {len(unicas)}")

    # --- 2. clusters de evidencia ------------------------------------------
    corpus = corpus_claim_ids()
    dsu = DSU()
    for idx, (name, i, obj) in enumerate(unicas):
        node = ("q", idx)
        dsu.find(node)
        for cid in obj.get("relevant_claim_ids", []) or []:
            if cid:  # liga pela claim, exista ela no corpus ou nao
                dsu.union(node, ("c", cid))
        if not sem_runbook and obj.get("runbook_ref"):
            dsu.union(node, ("r", obj["runbook_ref"]))

    clusters: dict[str, list[int]] = collections.defaultdict(list)
    for idx in range(len(unicas)):
        clusters[dsu.find(("q", idx))].append(idx)
    print(f"clusters de evidencia: {len(clusters)}")

    # --- 3. distribuicao deterministica ------------------------------------
    # Ordena por tamanho desc e desempata por chave estavel derivada do CONTEUDO do cluster:
    # nada depende de ordem de arquivo, de hash de processo ou de RNG.
    def chave_cluster(ids):
        h = hashlib.sha256()
        for j in sorted(norm(unicas[j][2].get("question", "")) for j in ids):
            h.update(j.encode())
        return h.hexdigest()

    ordenados = sorted(clusters.values(), key=lambda ids: (-len(ids), chave_cluster(ids)))
    # Alvo do teste em numero de PERGUNTAS (nao de clusters, para o teste nao encolher).
    alvo_teste = args.test_pct / 100.0 * len(unicas)
    treino, teste = [], []
    for ids in ordenados:
        # Cada cluster vai inteiro para o lado que esta' mais atras do seu alvo, medido em
        # fracao do proprio alvo. Deterministico: sem RNG, e a ordem de `ordenados` e'
        # estavel por construcao (tamanho, depois hash do conteudo).
        falta_treino = (len(unicas) - alvo_teste - len(treino)) / max(1.0, len(unicas) - alvo_teste)
        falta_teste = (alvo_teste - len(teste)) / max(1.0, alvo_teste)
        if falta_treino >= falta_teste:
            treino.extend(ids)
        else:
            teste.extend(ids)
    n_treino = len(treino)
    n_teste = len(teste)

    def claims_de(ids):
        s = set()
        for j in ids:
            s |= set(unicas[j][2].get("relevant_claim_ids", []) or [])
        return s

    def runbooks_de(ids):
        return {unicas[j][2].get("runbook_ref") for j in ids
                if unicas[j][2].get("runbook_ref")}

    c_tr, c_te = claims_de(treino), claims_de(teste)
    r_tr, r_te = runbooks_de(treino), runbooks_de(teste)

    # --- 4. invariantes (fail-closed) --------------------------------------
    viol = []
    nao_garantido = []
    q_tr = {norm(unicas[j][2]["question"]) for j in treino}
    q_te = {norm(unicas[j][2]["question"]) for j in teste}
    if q_tr & q_te:
        viol.append("pergunta identica em treino E teste: %d" % len(q_tr & q_te))
    if c_tr & c_te:
        viol.append("CLAIM em treino E teste: %d" % len(c_tr & c_te))
    if r_tr & r_te:
        # Na variante so'-claim isto e' o compromisso ACEITO, e nao uma falha: a evidencia
        # que fundamenta a resposta e' a claim, e ela esta' disjunta. Registrar como
        # "nao garantido" mantem o manifesto honesto sem reprovar a variante.
        alvo = viol if not sem_runbook else nao_garantido
        alvo.append("runbook em treino E teste: %d" % len(r_tr & r_te))

    print()
    print("=== INVARIANTES DE DISJUNCAO ===")
    print("  perguntas: treino %d | teste %d" % (len(treino), len(teste)))
    print("  claims:    treino %d | teste %d | INTERSECCAO %d"
          % (len(c_tr), len(c_te), len(c_tr & c_te)))
    print("  runbooks:  treino %d | teste %d | INTERSECCAO %d"
          % (len(r_tr), len(r_te), len(r_tr & r_te)))
    for v in viol:
        print("  [FAIL] " + v)
    for v in nao_garantido:
        print("  [WARN] nao garantido nesta variante - " + v)
    if not viol:
        print("  [PASS] disjuncao de PERGUNTA e CLAIM garantida"
              + (" e de runbook" if not sem_runbook else ""))

    # distribuicao de tamanhos de cluster - se houver um componente gigante, o split e'
    # estruturalmente limitado e isso precisa aparecer, nao ser escondido no numero final.
    tam = sorted((len(v) for v in clusters.values()), reverse=True)
    print()
    print("=== TAMANHO DOS CLUSTERS DE EVIDENCIA (top 10) ===")
    print("  " + ", ".join(str(x) for x in tam[:10]))
    print("  cluster unico de 1 pergunta: %d de %d" % (tam.count(1), len(tam)))

    # --- 5. grava ----------------------------------------------------------
    out_dir.mkdir(parents=True, exist_ok=True)
    for nome, ids in (("train", treino), ("test", teste)):
        with open(out_dir / f"{nome}.jsonl", "w", encoding="utf-8") as f:
            for j in sorted(ids):
                obj = dict(unicas[j][2])
                obj["_split_source"] = unicas[j][0]
                f.write(json.dumps(obj, ensure_ascii=False) + "\n")

    sem_resposta_te = sum(1 for j in teste
                          if not (set(unicas[j][2].get("relevant_claim_ids", []) or []) & corpus))
    manifest = {
        "gerado_por": "scripts/build_honest_splits.py",
        "entrada": "data/eval/decontaminated/*.jsonl",
        "regra": "clusters de evidencia (uniao por claim compartilhada); cluster e indivisivel",
        "agrupar_por_runbook": not args.sem_runbook,
        "test_pct_alvo": args.test_pct,
        "linhas_lidas": len(rows),
        "perguntas_distintas": len(unicas),
        "duplicatas_por_texto_removidas": dict(descartadas_dup),
        "clusters": len(clusters),
        "cluster_maior": tam[0] if tam else 0,
        "clusters_de_1_pergunta": tam.count(1),
        "treino": {"perguntas": len(treino), "claims": len(c_tr), "runbooks": len(r_tr)},
        "teste": {"perguntas": len(teste), "claims": len(c_te), "runbooks": len(r_te),
                  "sem_resposta_no_corpus": sem_resposta_te},
        "violacoes": viol,
        "nao_garantido": nao_garantido,
        "veredito": "PASS" if not viol else "FAIL",
    }
    with open(out_dir / "split-manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print()
    print(f"gravado em {out_dir.relative_to(REPO)}: train.jsonl, test.jsonl, split-manifest.json")
    print(f"veredito: {manifest['veredito']}")
    return 0 if not viol else 1


if __name__ == "__main__":
    sys.exit(main())
