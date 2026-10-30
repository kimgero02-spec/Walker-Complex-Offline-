# R11 researcher1: inverse problem  G == M  or  G == M°  with A(M) = K_N
# (1) build_manual: textbook Def 2.1/2.3/3.1 literally, from a decomposition
# (2) realize: cluster theorem (Thm C) -> decomposition from (G, W); then verify with (1)
import itertools, networkx as nx

def build_manual(pieces):
    """pieces: list of (Vk, Ek) ; returns (M, Mcirc, A) as nx graphs"""
    V0 = [(v, k) for k, (Vk, Ek) in enumerate(pieces) for v in Vk]
    E00 = [((u, k), (v, k)) for k, (Vk, Ek) in enumerate(pieces) for (u, v) in Ek]
    F = {}
    for (v, k) in V0: F.setdefault(v, []).append((v, k))
    V1 = [('w', v) for v in F if len(F[v]) >= 2]
    E01 = [(x, ('w', v)) for v in F if len(F[v]) >= 2 for x in F[v]]
    mu = {}
    for k, (Vk, Ek) in enumerate(pieces):
        for (u, v) in Ek: mu[frozenset((u, v))] = mu.get(frozenset((u, v)), 0) + 1
    E11 = [(('w', u), ('w', v)) for e, m in mu.items() if m >= 2
           for (u, v) in [tuple(e)] if len(F[u]) >= 2 and len(F[v]) >= 2]
    Mc = nx.Graph(); Mc.add_nodes_from(V0 + V1); Mc.add_edges_from(E00 + E01)
    M = Mc.copy(); M.add_edges_from(E11)
    rho = lambda a: a[1] if a[0] == 'w' else a[0]
    A = nx.Graph(); A.add_nodes_from(F)
    A.add_edges_from((rho(a), rho(b)) for a, b in M.edges() if rho(a) != rho(b))
    return M, Mc, A

def try_W(G, W, mode):
    """mode 'circ' (G = M°) or 'full' (G = M). returns pieces or None (Thm C conditions)."""
    W = set(W); B = [x for x in G if x not in W]
    if mode == 'circ' and any(G.has_edge(a, b) for a, b in itertools.combinations(W, 2)):
        return None
    NB = {w: [x for x in G[w] if x not in W] for w in W}
    if any(len(NB[w]) < 2 for w in W): return None            # (C1)
    owner = {}
    for w in W:
        for x in NB[w]:
            if x in owner: return None                         # (C2) <=1 white nbr
            owner[x] = w
    H = G.subgraph(B)
    comp = {}
    for i, C in enumerate(nx.connected_components(H)):
        for x in C: comp[x] = i
    for w in W:
        if len({comp[x] for x in NB[w]}) < len(NB[w]): return None   # (C3)
    for C in nx.connected_components(H):
        if not nx.check_planarity(H.subgraph(C))[0]: return None     # (C4)
    fib = {x: ('f', owner[x]) if x in owner else ('s', x) for x in B}
    fibers = set(fib.values())
    adj = {frozenset((fib[a], fib[b])) for a, b in H.edges()}
    if any(frozenset(p) not in adj for p in itertools.combinations(fibers, 2)):
        return None                                            # (C5) quotient complete
    if mode == 'full':                                         # (C6) E11 rule
        for w, w2 in itertools.combinations(W, 2):
            cnt = sum(1 for a, b in H.edges() if {fib[a], fib[b]} == {('f', w), ('f', w2)})
            if G.has_edge(w, w2) != (cnt >= 2): return None
    # decomposition: vertex set of K_N = fibers, one piece per component
    pieces = []
    for C in nx.connected_components(H):
        pieces.append(([fib[x] for x in C], [(fib[a], fib[b]) for a, b in H.subgraph(C).edges()]))
    return pieces

def realize(G, mode, maxW=None):
    out = []
    nodes = list(G)
    for r in range(0, (maxW or len(nodes)) + 1):
        for W in itertools.combinations(nodes, r):
            P = try_W(G, W, mode)
            if P is not None:
                M, Mc, A = build_manual(P)
                N = A.number_of_nodes()
                ok_A = A.number_of_edges() == N * (N - 1) // 2
                ok_G = nx.is_isomorphic(Mc if mode == 'circ' else M, G)
                out.append((W, N, len(P), ok_A, ok_G))
    return out

def subdiv3(N):
    G = nx.Graph()
    for u, v in itertools.combinations(range(N), 2):
        nx.add_path(G, [('h', u), (u, v, 'a'), (u, v, 'b'), ('h', v)])
    return G

if __name__ == '__main__':
    tests = {f'K{m}': nx.complete_graph(m) for m in range(1, 7)}
    tests.update({f'C{m}': nx.cycle_graph(m) for m in range(3, 12)})
    tests['K33'] = nx.complete_bipartite_graph(3, 3)
    tests['Petersen'] = nx.petersen_graph()
    tests['3-subdiv K5'] = subdiv3(5)
    # theta = M of textbook Ex 8.4 (M_b)
    T = nx.Graph([('a1','b1'),('a2','b2'),('wu','a1'),('wu','a2'),('wv','b1'),('wv','b2'),('wu','wv')])
    tests['theta(Ex8.4 M_b)'] = T
    # Petersen with spokes subdivided = M of Ex 1.5
    P = nx.Graph();
    for i in range(5):
        P.add_edge(('o', i), ('o', (i+1) % 5)); P.add_edge(('i', i), ('i', (i+2) % 5))
        P.add_edge(('o', i), ('s', i)); P.add_edge(('s', i), ('i', i))
    tests['Petersen spoke-subdiv'] = P
    for name, G in tests.items():
        for mode in ('circ', 'full'):
            mw = None if G.number_of_nodes() <= 12 else 5
            res = realize(G, mode, mw)
            Ns = sorted({(N, n) for (W, N, n, a, g) in res})
            bad = [r for r in res if not (r[3] and r[4])]
            print(f'{name:22s} {mode:4s} #W={len(res):3d} (N,n)={Ns} verify_fail={len(bad)}')
