"""R03 (colouring): cohomological Z2-index h of box complexes B_0(G), B(G).
h(X) = max n with w1^n != 0 in H^n(X/Z2;F2); computed by iterating the Smith/Gysin
connecting map  d = delta_X(lift(c))  on invariant cochains.
Bounds: chi >= h(B0)+1 , chi >= h(B)+2 (since ind >= h)."""
import itertools, networkx as nx

def simplices_B0(G, dmax):
    V = sorted(G.nodes()); idx = {v: i for i, v in enumerate(V)}
    adj = {v: set(G[v]) for v in V}
    out = []  # (frozenset A, frozenset B)
    for ka in range(0, dmax + 2):
        for A in itertools.combinations(V, ka):
            cn = set(V) - set(A) if not A else set.intersection(*[adj[a] for a in A])
            cn = sorted(cn)
            for kb in range(0, dmax + 2 - ka):
                if ka + kb == 0: continue
                for B in itertools.combinations(cn, kb):
                    out.append((frozenset(A), frozenset(B)))
    return out

def simplices_B(G, dmax):
    V = set(G.nodes()); adj = {v: set(G[v]) for v in V}
    def CN(S):
        return set(V) if not S else set.intersection(*[adj[a] for a in S])
    res = []
    for A, B in simplices_B0(G, dmax):
        if CN(A) and CN(B):
            res.append((A, B))
    return res

def h_index(simps, dmax):
    S = set(simps)
    bydim = {}
    for s in S:
        bydim.setdefault(len(s[0]) + len(s[1]) - 1, []).append(s)
    # orbit reps: choose canonical rep = min of (s, swap(s)) by a key
    def key(s): return (sorted(s[0]), sorted(s[1]))
    def rep(s):
        t = (s[1], s[0]); return s if key(s) <= key(t) else t
    orbits = {d: sorted({rep(s) for s in L}, key=key) for d, L in bydim.items()}
    oidx = {d: {o: i for i, o in enumerate(orbits[d])} for d in orbits}
    def faces(s):
        A, B = s
        for a in A:
            f = (A - {a}, B)
            if f[0] or f[1]: yield f
        for b in B:
            f = (A, B - {b})
            if f[0] or f[1]: yield f
    # c: set of orbit reps (support) in dim n
    c = set(orbits[0])  # constant 1
    n = 0
    while True:
        if n + 1 not in orbits: return n
        # d(sigma) for sigma in reps of dim n+1 : sum over faces f of lift(c)(f); lift = c on reps
        d = set()
        for s in orbits[n + 1]:
            v = 0
            for f in faces(s):
                if f in c: v ^= 1   # f must itself be a rep and in support
            if v: d.add(s)
        # coboundary test: d in image of delta_q (invariant cochains of dim n)
        # delta_q(e)(sigma) = sum_{faces f} e([f])
        rows = oidx[n + 1]
        cols = []
        for o in orbits[n]:
            cols.append(0)
        colmask = [0] * len(orbits[n])
        for s in orbits[n + 1]:
            r = rows[s]
            for f in faces(s):
                colmask[oidx[n][rep(f)]] ^= (1 << r)
        target = 0
        for s in d: target |= 1 << rows[s]
        if in_span(colmask, target):
            return n
        c = d; n += 1
        if n >= dmax: return n  # capped

def in_span(vecs, t):
    basis = {}  # pivot -> vec
    for v in vecs:
        while v:
            p = v.bit_length() - 1
            if p in basis: v ^= basis[p]
            else: basis[p] = v; break
    while t:
        p = t.bit_length() - 1
        if p in basis: t ^= basis[p]
        else: return False
    return True

def bounds(G, dmax=None):
    if dmax is None:
        dmax = nx.graph_clique_number(G) + 2 if hasattr(nx, 'graph_clique_number') else 6
    b0 = h_index(simplices_B0(G, dmax), dmax) + 1
    b = h_index(simplices_B(G, dmax), dmax) + 2
    return b0, b

def chi(G):
    n = G.number_of_nodes()
    for k in range(1, n + 1):
        if colorable(G, k): return k
def colorable(G, k):
    V = sorted(G.nodes(), key=lambda v: -G.degree(v)); col = {}
    def bt(i):
        if i == len(V): return True
        v = V[i]; used = {col[u] for u in G[v] if u in col}
        for c in range(k):
            if c not in used:
                col[v] = c
                if bt(i + 1): return True
                del col[v]
        return False
    return bt(0)

def report(name, G, dmax=5):
    b0 = h_index(simplices_B0(G, dmax), dmax) + 1
    b = h_index(simplices_B(G, dmax), dmax) + 2
    print(f"{name:40s} n={G.number_of_nodes():2d} chi={chi(G)} L0=h(B0)+1={b0} L=h(B)+2={b}")
    return chi(G), b0, b

if __name__ == '__main__':
    for n in range(2, 6): report(f"K{n}", nx.complete_graph(n))
    for n in range(4, 8): report(f"C{n}", nx.cycle_graph(n))
    report("Petersen", nx.petersen_graph())
