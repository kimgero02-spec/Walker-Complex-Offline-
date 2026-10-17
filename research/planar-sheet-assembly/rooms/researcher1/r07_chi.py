# R07 researcher1: checks for the chromatic reformulation (labelled piece profiles).
import itertools, networkx as nx

def colorings(P, q, fixed=None):
    """all proper colorings of P with colors 0..q-1 (dict node->color), optionally restricted by fixed."""
    nodes = sorted(P.nodes(), key=lambda v: -P.degree(v))
    out = []
    col = {}
    def bt(i):
        if i == len(nodes):
            out.append(dict(col)); return
        v = nodes[i]
        used = {col[w] for w in P[v] if w in col}
        for c in range(q):
            if c not in used:
                col[v] = c; bt(i+1); del col[v]
    bt(0)
    return out

def chi(G):
    # simple backtracking minimal q
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    for q in range(1, len(nodes)+1):
        col = {}
        def bt(i):
            if i == len(nodes): return True
            v = nodes[i]
            used = {col[w] for w in G[v] if w in col}
            for c in range(q):
                if c not in used:
                    col[v] = c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return q
    return 0

def gluing_sat(G_nodes, pieces, q):
    """Theorem 1 check: exists f: V(G)->[q] with f|V(P_k) proper for each piece."""
    V = list(G_nodes)
    for f_vals in itertools.product(range(q), repeat=len(V)):
        f = dict(zip(V, f_vals))
        ok = True
        for P in pieces:
            for u, v in P.edges():
                if f[u] == f[v]:
                    ok = False; break
            if not ok: break
        if ok: return True
    return False

def profile_sat(S, pieces, q):
    """Theorem 2 check (single interface S): exists g:S->[q] with g in Phi_k(q) for all k,
    Phi_k(q) = {c|S : c proper q-coloring of P_k}."""
    S = list(S)
    Phis = []
    for P in pieces:
        Phi = set()
        for c in colorings(P, q):
            Phi.add(tuple(c[s] for s in S if s in c))
        Phis.append(Phi)
    # every S-vertex lies in every piece? if not, treat missing as free: here we require S subset of each piece
    inter = set(itertools.product(range(q), repeat=len(S)))
    for Phi in Phis:
        inter &= Phi
    return len(inter) > 0

def min_q(check, qmax):
    for q in range(1, qmax+1):
        if check(q): return q
    return None
