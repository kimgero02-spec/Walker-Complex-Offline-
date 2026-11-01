# R06 researcher3 (discrete Hodge lens). Pure python + numpy.
import itertools, numpy as np

def make(n, edges):
    adj = [0]*n
    for u, v in edges:
        adj[u] |= 1 << v; adj[v] |= 1 << u
    return adj

def popc(x): return bin(x).count("1")

def common_nb(adj, n, S):
    full = (1 << n) - 1
    c = full
    s = S
    while s:
        low = s & -s; i = low.bit_length()-1; c &= adj[i]; s ^= low
    return c if S else full

def max_bicliques(adj, n):
    """maximal pairs (X,Y), X,Y nonempty, X = CN(Y), Y = CN(X)."""
    res = set()
    for X in range(1, 1 << n):
        Y = common_nb(adj, n, X)
        if Y == 0: continue
        X2 = common_nb(adj, n, Y)
        res.add((X2, Y))
    return sorted(res)

def runs(order, X, Y):
    """number of runs of the label word on X∪Y read in the order (order = list of vertices)."""
    labs = []
    for v in order:
        if X >> v & 1: labs.append(0)
        elif Y >> v & 1: labs.append(1)
    if not labs: return 0
    return 1 + sum(1 for i in range(1, len(labs)) if labs[i] != labs[i-1])

def zig(adj, n, return_order=False):
    MB = max_bicliques(adj, n)
    best = None; bo = None
    for p in itertools.permutations(range(n)):
        m = 0
        for X, Y in MB:
            r = runs(p, X, Y)
            if r > m:
                m = r
                if best is not None and m >= best: break
        if best is None or m < best:
            best = m; bo = p
    return (best, bo) if return_order else best

def rank_mod_p(rows, ncols, p):
    """rows: list of dict col->val. gaussian elimination mod p."""
    piv = {}
    r = 0
    for row in rows:
        row = {c: v % p for c, v in row.items() if v % p}
        while row:
            c = min(row)
            if c in piv:
                prow = piv[c]
                f = row[c]
                for cc, vv in prow.items():
                    nv = (row.get(cc, 0) - f*vv) % p
                    if nv: row[cc] = nv
                    else: row.pop(cc, None)
            else:
                inv = pow(row[c], p-2, p)
                row = {cc: (vv*inv) % p for cc, vv in row.items()}
                piv[c] = row; r += 1
                break
    return r

def reduced_betti(faces_by_dim, p=10007):
    """faces_by_dim: dict k -> sorted list of simplices (tuples of sorted vertex ids), k = dim.
    includes the empty simplex as dim -1 if desired (tuple ())."""
    dims = sorted(faces_by_dim)
    idx = {k: {f: i for i, f in enumerate(faces_by_dim[k])} for k in dims}
    ranks = {}
    for k in dims:
        if k-1 not in idx:
            ranks[k] = 1 if (k == 0 and faces_by_dim[k]) else 0  # augmentation: reduced homology
            continue
        rows = []
        for f in faces_by_dim[k]:
            row = {}
            for j in range(len(f)):
                g = f[:j]+f[j+1:]
                row[idx[k-1][g]] = (-1)**j
            rows.append(row)
        ranks[k] = rank_mod_p(rows, len(faces_by_dim[k-1]) if k-1 in idx else 0, p)
    out = {}
    for k in dims:
        nk = len(faces_by_dim[k])
        out[k] = nk - ranks[k] - ranks.get(k+1, 0)
    return out

def B0_empty(adj, n):
    """faces of box complex with empties allowed: simplex = sorted tuple of ids, copy1 i -> i, copy2 i -> n+i.
    face (A,B): A x B subset E. Returns faces_by_dim with dim=|face|-1 (incl. empty tuple at -1)."""
    F = {}
    for A in range(1 << n):
        CN = common_nb(adj, n, A) if A else (1 << n) - 1
        B = CN
        while True:
            # enumerate subsets B of CN
            if (A or B):
                ids = [i for i in range(n) if A >> i & 1] + [n+i for i in range(n) if B >> i & 1]
                F.setdefault(len(ids)-1, []).append(tuple(ids))
            if B == 0: break
            B = (B-1) & CN
    for k in F: F[k].sort()
    return F

def Nfaces(adj, n):
    """neighborhood complex: sigma (possibly empty) with a common neighbor."""
    F = {}
    seen = set()
    for v in range(n):
        Nv = adj[v]
        verts = [i for i in range(n) if Nv >> i & 1]
        for k in range(len(verts)+1):
            for s in itertools.combinations(verts, k):
                seen.add(s)
    for s in seen:
        F.setdefault(len(s)-1, []).append(s)
    for k in F: F[k].sort()
    return F
