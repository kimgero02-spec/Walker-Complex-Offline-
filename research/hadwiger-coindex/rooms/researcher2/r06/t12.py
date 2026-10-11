import sys
sys.path.insert(0,'.')
from graphs import *
from homol import neighborhood_complex
from pi1 import pi1_presentation, tietze
from t10 import complex_parts
from itertools import combinations

def rank_modp(rows, p):
    # rows: list of dict col->val
    piv = {}
    r = 0
    for row in rows:
        row = {k: v % p for k, v in row.items() if v % p}
        while row:
            c = max(row)
            if c in piv:
                prow = piv[c]; f = row[c] * pow(prow[c], -1, p) % p
                for k, v in prow.items():
                    nv = (row.get(k, 0) - f*v) % p
                    if nv: row[k] = nv
                    else: row.pop(k, None)
            else:
                piv[c] = row; r += 1; break
    return r

def betti_modp(faces, p):
    by = {}
    for f in faces: by.setdefault(len(f)-1, []).append(tuple(sorted(f)))
    idx = {d: {f: i for i, f in enumerate(sorted(by[d]))} for d in by}
    maxd = max(by)
    rk = {0: 1 if by.get(0) else 0}  # augmentation rank (reduced): rank of d=0 boundary to empty = 1
    rk = {}
    rk[0] = 1
    for d in range(1, maxd+1):
        rows = []
        for f in by.get(d, []):
            row = {}
            for i in range(len(f)):
                g = f[:i]+f[i+1:]
                row[idx[d-1][g]] = (-1)**i
            rows.append(row)
        rk[d] = rank_modp(rows, p)
    out = {}
    for d in range(-1, maxd+1):
        nd = len(by[d]) if d >= 0 else 1
        b = nd - (rk.get(d, 0) if d >= 0 else 0) - rk.get(d+1, 0)
        if b: out[d] = b
    return out

n, adj = circulant(9, [1,2,3])
F = neighborhood_complex(n, adj)
for p in (2, 3, 5, 7):
    print('p=%d H~(N(C9^3);F_p)' % p, betti_modp(F, p), flush=True)
V, E, T = complex_parts(n, adj)
ng, rels = pi1_presentation(V, E, T)
alive, left = tietze(ng, rels)
print('pi1(N(C9^3)) Tietze: gens', ng, 'alive', len(alive), 'rels left', len(left), flush=True)
