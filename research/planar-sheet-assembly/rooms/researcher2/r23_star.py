"""(★) checker, written independently for R23-2.
(★) fails iff exists z, H subset G-z with chi(H)>=4, s:V(H)->N(z) with N_H(v) subset N(s(v)) (s(v)=v allowed when v in N(z)).
Returns a witness (z, H edges, s) or None."""
import itertools, sys

def adj_from_edges(edges):
    A = {}
    for u, v in edges:
        A.setdefault(u, set()).add(v); A.setdefault(v, set()).add(u)
    return A

def colorable(A, verts, k):
    verts = sorted(verts, key=lambda v: -len(A[v] & verts))
    col = {}
    def bt(i):
        if i == len(verts): return True
        v = verts[i]
        used = {col[u] for u in A[v] if u in col}
        for c in range(k):
            if c not in used:
                col[v] = c
                if bt(i + 1): return True
                del col[v]
        return False
    return bt(0)

def core(adj, k):
    adj = {v: set(n) for v, n in adj.items()}
    ch = True
    while ch:
        ch = False
        for v in list(adj):
            if len(adj[v]) < k:
                for u in adj[v]: adj[u].discard(v)
                del adj[v]; ch = True
    return adj

def star_witness(A, kk=4):
    V = list(A)
    for z in V:
        Nz = A[z]
        opts = {}
        for v in V:
            if v == z: continue
            cand = []
            if v in Nz:
                cand.append((frozenset(A[v] - {z}), v))
            for t in Nz:
                if t == v: continue
                cand.append((frozenset((A[v] & A[t]) - {z}), t))
            # keep maximal, size >= kk-1
            cand = [c for c in cand if len(c[0]) >= kk - 1]
            mx = []
            for c in cand:
                if not any(c[0] < d[0] for d in cand) and all(c[0] != d[0] for d in mx):
                    mx.append(c)
            if mx: opts[v] = mx
        # iterative pruning with union bound
        alive = set(opts)
        while True:
            ub = {v: set().union(*[o[0] for o in opts[v]]) & alive for v in alive}
            ub2 = {v: {u for u in ub[v] if v in ub.get(u, set())} for v in alive}
            dead = {v for v in alive if len(ub2[v]) < kk - 1}
            if not dead: break
            alive -= dead
        if len(alive) < kk: continue
        al = sorted(alive)
        choices = [[o for o in opts[v] if len(o[0] & alive) >= kk - 1] for v in al]
        if any(not c for c in choices): pass
        n = 1
        for c in choices: n *= max(1, len(c))
        if n > 2_000_000:
            print('too many combos', z, n, file=sys.stderr); continue
        for combo in itertools.product(*choices):
            S = {v: combo[i][0] for i, v in enumerate(al)}
            adj = {v: {u for u in S[v] if u in S and v in S[u]} for v in al}
            adj = core(adj, kk - 1)
            if len(adj) < kk: continue
            verts = set(adj)
            if not colorable(adj, verts, kk - 1):
                s = {v: combo[al.index(v)][1] for v in verts}
                return z, sorted({tuple(sorted((u, w))) for u in adj for w in adj[u]}), s
    return None

def chi(A, maxk=7):
    vs = set(A)
    for k in range(1, maxk):
        if colorable(A, vs, k): return k
    return None

def hajos(E1, x1, y1, E2, x2, y2, tag=('a', 'b')):
    """E1 with edge x1y1, E2 with edge x2y2. identify x1=x2, delete both edges, add y1y2."""
    def ren(v, t, x):
        return 'x' if v == x else f'{t}{v}'
    E = set()
    for (u, v) in E1:
        if {u, v} == {x1, y1}: continue
        E.add(tuple(sorted((ren(u, tag[0], x1), ren(v, tag[0], x1)))))
    for (u, v) in E2:
        if {u, v} == {x2, y2}: continue
        E.add(tuple(sorted((ren(u, tag[1], x2), ren(v, tag[1], x2)))))
    E.add(tuple(sorted((ren(y1, tag[0], x1), ren(y2, tag[1], x2)))))
    return sorted(E)

def K(n, labels=None):
    labels = labels or list(range(n))
    return [(labels[i], labels[j]) for i in range(n) for j in range(i + 1, n)]
