"""TUNING + VALIDACAO HONESTA da fusao assimetrica.

Achado: denso destroi a faixa alta (81%->44%) e dobra a baixa (16%->32%). Fundir so'
onde o lexical e' cego da +21 Hit@1. Mas o peso foi escolhido NESTES 423 - in-sample.
Aqui:
  1. varredura fina do peso (e pesos por faixa);
  2. SELECAO numa metade (A) e MEDICAO na outra (B) - numero honesto;
  3. curva A x B: se o otimo de A tambem e' bom em B, a politica generaliza; se nao,
     o peso e' ruido do conjunto e nao vale publicar.
"""
import json
import hashlib
import statistics

R = json.load(open("/tmp/ragexp/fusao_resultado.json"))
dados = R["dados"]
n = len(dados)
print("perguntas: %d" % n)


def acha_rank(seq_ids, exp_set):
    for i, did in enumerate(seq_ids, 1):
        if did in exp_set:
            return i
    return None


def funde(lex, dense, w, top=15):
    rrf = {}
    for r, did in enumerate(dense, 1):
        rrf[did] = rrf.get(did, 0.0) + w / (60.0 + r)
    for r, did in enumerate(lex, 1):
        rrf[did] = rrf.get(did, 0.0) + (2.0 - w) / (60.0 + r)
    return sorted(rrf, key=lambda x: (-rrf[x], str(x)))[:top]


def metrica(dds, wa, wm, wb, lim_alta=0.177, lim_media=0.05):
    """wa/wm/wb = peso do DENSO em cada faixa. wa=0 -> lexical puro."""
    h1 = 0
    rr = []
    for dd in dds:
        m = dd["margem"]
        w = wa if m >= lim_alta else (wm if m >= lim_media else wb)
        seq = dd["lex"][:15] if w <= 0 else funde(dd["lex"], dd["dense"], w)
        r = acha_rank(seq, set(dd["exp"]))
        if r == 1:
            h1 += 1
        rr.append(1.0 / r if r else 0.0)
    return h1, sum(rr) / len(rr)


# --- metade por hash da pergunta (reparticao fixa e independente do resultado) ---
def metade(q):
    return int(hashlib.md5(q.encode()).hexdigest(), 16) % 2


A = [d for d in dados if metade(d["q"]) == 0]
B = [d for d in dados if metade(d["q"]) == 1]
print("metade A: %d | metade B: %d" % (len(A), len(B)))
hA = metrica(A, 0, 0, 0)
hB = metrica(B, 0, 0, 0)
print("  lexical puro: A %d/%d (%.1f%%) MRR %.4f | B %d/%d (%.1f%%) MRR %.4f"
      % (hA[0], len(A), 100 * hA[0] / len(A), hA[1],
         hB[0], len(B), 100 * hB[0] / len(B), hB[1]))

print()
print("=" * 88)
print("VARREDURA — peso do denso em media/baixa (alta fica SEMPRE lexical puro)")
print("=" * 88)
print("  %-16s %14s %14s %14s" % ("(w_media,w_baixa)", "A hit@1", "B hit@1", "todos hit@1"))
melhor_A = None
for wm in (0.0, 0.5, 0.8, 1.0, 1.4, 1.8):
    for wb in (0.0, 0.5, 0.8, 1.0, 1.4, 1.8, 2.0):
        a = metrica(A, 0.0, wm, wb)
        b = metrica(B, 0.0, wm, wb)
        t = metrica(dados, 0.0, wm, wb)
        print("  %-16s %5d/%d (%3.0f%%) %5d/%d (%3.0f%%) %5d/%d (%3.0f%%)"
              % ("%.1f,%.1f" % (wm, wb), a[0], len(A), 100 * a[0] / len(A),
                 b[0], len(B), 100 * b[0] / len(B), t[0], n, 100 * t[0] / n))
        if melhor_A is None or a[0] > melhor_A[0]:
            melhor_A = (a[0], wm, wb)

print()
print("SELECAO HONESTA: o melhor (w_media,w_baixa) em A = (%.1f,%.1f) com %d/%d"
      % (melhor_A[1], melhor_A[2], melhor_A[0], len(A)))
b_honesto = metrica(B, 0.0, melhor_A[1], melhor_A[2])
print("  -> medido em B (NUNCA visto na selecao): %d/%d (%.1f%%) MRR %.4f"
      % (b_honesto[0], len(B), 100 * b_honesto[0] / len(B), b_honesto[1]))
print("  -> baseline lexical em B: %d/%d (%.1f%%) MRR %.4f"
      % (hB[0], len(B), 100 * hB[0] / len(B), hB[1]))
print("  -> GANHO HONESTO em B: %+d hit@1 (%+.1f pp), MRR %+.4f"
      % (b_honesto[0] - hB[0], 100 * (b_honesto[0] - hB[0]) / len(B), b_honesto[1] - hB[1]))
print()
print("CONTROLE CRUZADO (selecao em B, medicao em A) — o ganho e' simetrico?")
melhor_B = None
for wm in (0.0, 0.5, 0.8, 1.0, 1.4, 1.8):
    for wb in (0.0, 0.5, 0.8, 1.0, 1.4, 1.8, 2.0):
        b = metrica(B, 0.0, wm, wb)
        if melhor_B is None or b[0] > melhor_B[0]:
            melhor_B = (b[0], wm, wb)
a_honesto = metrica(A, 0.0, melhor_B[1], melhor_B[2])
print("  melhor em B = (%.1f,%.1f); medido em A: %d/%d (%.1f%%) vs lexical %d/%d (%.1f%%) -> %+d"
      % (melhor_B[1], melhor_B[2], a_honesto[0], len(A), 100 * a_honesto[0] / len(A),
         hA[0], len(A), 100 * hA[0] / len(A), a_honesto[0] - hA[0]))

# estabilidade: o ganho aparece nas DUAS metades com um peso fixo e unico?
print()
print("ESTABILIDADE COM PESO FIXO (2.0, 1.4) — sem escolher nada:")
for wm, wb in ((1.4, 1.8), (1.4, 2.0), (1.0, 1.4)):
    a = metrica(A, 0.0, wm, wb)
    b = metrica(B, 0.0, wm, wb)
    print("  (%.1f,%.1f): A %+d (%+.1f pp) | B %+d (%+.1f pp)"
          % (wm, wb, a[0] - hA[0], 100 * (a[0] - hA[0]) / len(A),
             b[0] - hB[0], 100 * (b[0] - hB[0]) / len(B)))
