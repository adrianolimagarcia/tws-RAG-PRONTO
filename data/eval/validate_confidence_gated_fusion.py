"""VALIDACAO FINAL da politica deployavel.

Do grid: o que importa e' UM parametro - o peso do denso na faixa mais fraca. w_media
quase nao move o resultado. Entao a politica minima e':
    se margem_norm < T:  funde(lexical, denso, w_denso=1.8)
    senao:               lexical puro
Testa T e w honestamente (A/B), e reporta a politica escolhida com intervalo.
"""
import json
import hashlib
import math

R = json.load(open("/tmp/ragexp/fusao_resultado.json"))
dados = R["dados"]
n = len(dados)


def rank(seq, exp):
    for i, did in enumerate(seq, 1):
        if did in exp:
            return i
    return None


def funde(lex, dense, w, top=15):
    rrf = {}
    for r, did in enumerate(dense, 1):
        rrf[did] = rrf.get(did, 0.0) + w / (60.0 + r)
    for r, did in enumerate(lex, 1):
        rrf[did] = rrf.get(did, 0.0) + (2.0 - w) / (60.0 + r)
    return sorted(rrf, key=lambda x: (-rrf[x], str(x)))[:top]


def pol(dds, T, w):
    h1 = 0
    rr = []
    for dd in dds:
        seq = funde(dd["lex"], dd["dense"], w) if dd["margem"] < T else dd["lex"][:15]
        r = rank(seq, set(dd["exp"]))
        if r == 1:
            h1 += 1
        rr.append(1.0 / r if r else 0.0)
    return h1, sum(rr) / len(rr)


def metade(q):
    return int(hashlib.md5(q.encode()).hexdigest(), 16) % 2


A = [d for d in dados if metade(d["q"]) == 0]
B = [d for d in dados if metade(d["q"]) == 1]
hA0 = pol(A, 0, 0)
hB0 = pol(B, 0, 0)
print("baseline lexical: global %d/%d | A %d/%d | B %d/%d"
      % (pol(dados, 0, 0)[0], n, hA0[0], len(A), hB0[0], len(B)))
print()
print("=" * 84)
print("%-18s %14s %14s %14s" % ("(T, w_denso)", "A hit@1", "B hit@1", "todos"))
print("=" * 84)
cands = []
for T in (0.02, 0.05, 0.08, 0.12, 0.177, 0.25):
    for w in (1.2, 1.5, 1.8, 2.0):
        a = pol(A, T, w)
        b = pol(B, T, w)
        t = pol(dados, T, w)
        da = a[0] - hA0[0]
        db = b[0] - hB0[0]
        flag = "  OK" if da > 0 and db > 0 else ("" if da >= 0 and db >= 0 else "  PIORA")
        print("%-18s %4d/%d (%+3d) %4d/%d (%+3d) %4d/%d (%.1f%%)%s"
              % ("T=%.3f w=%.1f" % (T, w), a[0], len(A), da, b[0], len(B), db,
                 t[0], n, 100 * t[0] / n, flag))
        cands.append((T, w, da, db, t[0]))

print()
# escolha: o maior ganho MINIMO entre as duas metades (robusto, nao o maior total)
melhor = max(cands, key=lambda c: (min(c[2], c[3]), c[4]))
print("ESCOLHA ROBUSTA (maximiza o PIOR ganho entre A e B): T=%.3f, w_denso=%.1f" % (melhor[0], melhor[1]))
print("  A %+d | B %+d | total %d/%d (+%d, %+.1f pp)"
      % (melhor[2], melhor[3], melhor[4], n, melhor[4] - pol(dados, 0, 0)[0],
         100 * (melhor[4] - pol(dados, 0, 0)[0]) / n))

# intervalo de confianca do ganho (bootstrap sobre perguntas)
import random
random.seed(1234)
T, w = melhor[0], melhor[1]
ganhos = []
for _ in range(2000):
    amostra = [random.choice(dados) for _ in range(n)]
    g = pol(amostra, T, w)[0] - pol(amostra, 0, 0)[0]
    ganhos.append(g)
ganhos.sort()
print("  bootstrap 2000x do ganho: mediana %+d | IC95%% [%+d, %+d]"
      % (ganhos[1000], ganhos[50], ganhos[1950]))
print("  -> %s" % ("IC inteiramente POSITIVO: ganho nao e' ruido"
                    if ganhos[50] > 0 else "IC toca o zero: ganho NAO concluinte"))
