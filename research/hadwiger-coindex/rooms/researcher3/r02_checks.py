# R02 researcher3 checks: (1) reduced homology of B_0(K_n) under problem.md convention
# (faces A^1 u B^2, A,B disjoint, A or B may be empty), GF(2) ranks; (2) d_R placements.
import itertools, sys
import numpy as np

def faces_B0_complete(n):
    V = range(n)
    faces = []
    for lab in itertools.product((0, 1, 2), repeat=n):  # 0: neither, 1: copy1, 2: copy2
        A = tuple(v for v in V if lab[v] == 1)
        B = tuple(v for v in V if lab[v] == 2)
        faces.append(tuple([(a, 1) for a in A] + [(b, 2) for b in B]))
    return faces  # includes empty face (dim -1)

def gf2_rank(M):
    M = M.copy() % 2
    r = 0
    rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]:
                piv = i; break
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        for i in range(rows):
            if i != r and M[i, c]:
                M[i] ^= M[r]
        r += 1
        if r == rows: break
    return r

def reduced_betti_gf2(faces):
    by_dim = {}
    for f in faces:
        by_dim.setdefault(len(f) - 1, []).append(tuple(sorted(f)))
    maxd = max(by_dim)
    idx = {d: {f: i for i, f in enumerate(sorted(by_dim[d]))} for d in by_dim}
    ranks = {}
    for d in range(0, maxd + 1):  # boundary d -> d-1 (reduced: include dim -1)
        if d not in by_dim or (d - 1) not in by_dim: ranks[d] = 0; continue
        M = np.zeros((len(idx[d - 1]), len(idx[d])), dtype=np.uint8)
        for f, j in idx[d].items():
            for k in range(len(f)):
                g = f[:k] + f[k + 1:]
                M[idx[d - 1][g], j] = 1
        ranks[d] = gf2_rank(M)
    betti = {}
    for d in range(-1, maxd + 1):
        nd = len(idx.get(d, {}))
        rk_out = ranks.get(d, 0) if d >= 0 else 0
        rk_in = ranks.get(d + 1, 0)
        betti[d] = nd - rk_out - rk_in
    return {d: b for d, b in betti.items() if b}

for n in range(1, 5):
    print("K_%d : reduced GF(2) Betti (dim: rank) =" % n, reduced_betti_gf2(faces_B0_complete(n)))
