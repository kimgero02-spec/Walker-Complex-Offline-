# R04 researcher2: 평면 E6 시도용 도구
import itertools, networkx as nx

def col_ok(P, triples, k=4, order=None):
    """P 의 k-색칠 중 모든 triple 이 2색 이하인 것이 있으면 하나 반환, 없으면 None."""
    nodes = order if order else sorted(P.nodes(), key=lambda v: -P.degree(v))
    tri_of = {v: [] for v in nodes}
    for t in triples:
        for v in t: tri_of[v].append(t)
    col = {}
    def bad(v):
        for t in tri_of[v]:
            if all(u in col for u in t) and len({col[u] for u in t}) == 3:
                return True
        return False
    def bt(i):
        if i == len(nodes): return True
        v = nodes[i]
        used = {col[u] for u in P[v] if u in col}
        mx = max(col.values(), default=-1)
        for c in range(min(k, mx + 2)):
            if c in used: continue
            col[v] = c
            if not bad(v) and bt(i + 1): return True
            del col[v]
        return False
    return dict(col) if bt(0) else None

def chi(G):
    for k in range(1, G.number_of_nodes() + 1):
        if col_ok(G, [], k) is not None: return k

def assemble(P, triples):
    G = P.copy()
    for i, t in enumerate(triples):
        h1, h2 = ('h', i, 1), ('h', i, 2)
        G.add_edge(h1, h2)
        for v in t: G.add_edge(h1, v); G.add_edge(h2, v)
    return G

def indep(P, t):
    return all(not P.has_edge(u, v) for u, v in itertools.combinations(t, 2))
