# N-T1: manual Gamma=(disjoint pieces, E_J) -> G = Gamma/E_J ; chi via profiles
import itertools, networkx as nx

def assemble(pieces, EJ):
    """pieces: list of nx.Graph with vertices (k, name). EJ: list of pairs. returns G or raises."""
    Gam = nx.Graph()
    for P in pieces: Gam.add_edges_from(P.edges(), t='P'); Gam.add_nodes_from(P.nodes())
    J = nx.Graph(); J.add_nodes_from(Gam.nodes()); J.add_edges_from(EJ)
    cls = {}
    for i, C in enumerate(nx.connected_components(J)):
        ks = [v[0] for v in C]
        assert len(ks) == len(set(ks)), "W2 violated: class meets a piece twice"
        for v in C: cls[v] = i
    G = nx.Graph(); G.add_nodes_from(set(cls.values()))
    for P in pieces:
        for a, b in P.edges():
            assert cls[a] != cls[b], "W1 violated: loop"
            G.add_edge(cls[a], cls[b])
    return Gam, G, cls

def colorings(P, q):
    nodes = list(P.nodes()); 
    # simple backtracking
    order = list(nx.dfs_preorder_nodes(P)) if P.number_of_nodes() else []
    order += [v for v in nodes if v not in order]
    col = {}
    def bt(i):
        if i == len(order): yield dict(col); return
        v = order[i]
        for c in range(q):
            if all(col.get(w) != c for w in P[v]):
                col[v] = c; yield from bt(i+1); del col[v]
    yield from bt(0)

def kernel(c, Jk):
    # partition of Jk induced by coloring c (canonical)
    blocks = {}
    for x in Jk: blocks.setdefault(c[x], []).append(x)
    return frozenset(frozenset(b) for b in blocks.values())

def profile(P, Jk, q):
    return {kernel(c, Jk) for c in colorings(P, q)}

def chi(G):
    q = 1
    while True:
        if next(colorings(G, q), None) is not None: return q
        q += 1

def chi_from_profiles(pieces, EJ, qmax=8):
    """decide q-colorability using ONLY profiles + class map (no G)."""
    _, _, cls = assemble(pieces, EJ)
    Jv = {v for e in EJ for v in e}
    Jk = [[v for v in P.nodes() if v in Jv] for P in pieces]
    classes = sorted({cls[v] for v in Jv})
    for q in range(1, qmax+1):
        prof = [profile(P, Jk[k], q) for k, P in enumerate(pieces)]
        for f in itertools.product(range(q), repeat=len(classes)):
            fd = dict(zip(classes, f))
            if all(kernel({x: fd[cls[x]] for x in Jk[k]}, Jk[k]) in prof[k] for k in range(len(pieces))):
                return q
    return None

def mixed_chi(Gam, EJ):
    # min q with coloring of Gamma: != on piece edges, == on EJ edges
    q = 1
    while True:
        H = Gam.copy()
        for q_try in [q]:
            pass
        # brute via assembling: equivalent; compute directly by backtracking on Gamma
        nodes = list(Gam.nodes()); col = {}
        Jg = nx.Graph(); Jg.add_edges_from(EJ)
        def ok(v, c):
            if any(col.get(w) == c for w in Gam[v] if Gam[v][w].get('t') == 'P'): return False
            if v in Jg and any(w in col and col[w] != c for w in Jg[v]): return False
            return True
        def bt(i):
            if i == len(nodes): return True
            v = nodes[i]
            for c in range(q):
                if ok(v, c):
                    col[v] = c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return q
        q += 1

def piece(k, edges):
    P = nx.Graph(); P.add_edges_from(((k, a), (k, b)) for a, b in edges); return P

diamond = [('u','a'),('u','b'),('a','b'),('a','v'),('b','v')]   # K4 - uv
print("=== Example 1: K4 = (K4-uv) u K2 ===")
P1 = piece(1, diamond); P2 = piece(2, [('u','v')])
EJ = [((1,'u'),(2,'u')), ((1,'v'),(2,'v'))]
Gam, G, _ = assemble([P1, P2], EJ)
print("G iso K4:", nx.is_isomorphic(G, nx.complete_graph(4)), " chi(P)=", chi(P1), chi(P2), " chi(G)=", chi(G))
for q in (3, 4):
    print(" q=%d profile P1:" % q, [sorted(map(sorted, p)) for p in profile(P1, [(1,'u'),(1,'v')], q)],
          " P2:", [sorted(map(sorted, p)) for p in profile(P2, [(2,'u'),(2,'v')], q)])
print(" chi from profiles only:", chi_from_profiles([P1, P2], EJ), " mixed chi(Gamma):", mixed_chi(Gam, EJ),
      " plain chi(Gamma):", chi(Gam), " Gamma planar:", nx.check_planarity(Gam)[0], " G planar:", nx.check_planarity(G)[0])

print("=== Example 2: same coarse data, different chi ===")
# A: P2 = diamond(u,a,b,w) + wv  -> forces c(u) != c(v)
A2 = piece(2, [('u','a'),('u','b'),('a','b'),('a','w'),('b','w'),('w','v')])
# B: P2' = diamond(u,a,b,v) + pendant z on a -> forces c(u) == c(v)
B2 = piece(2, diamond + [('a','z')])
for name, Q in (("A", A2), ("B", B2)):
    Gam, G, _ = assemble([P1, Q], EJ)
    print(name, "|V|,|E| of P2:", Q.number_of_nodes(), Q.number_of_edges(), " planar pieces:",
          nx.check_planarity(P1)[0], nx.check_planarity(Q)[0], " chi(P1),chi(P2):", chi(P1), chi(Q),
          " uv edge in P1/P2:", P1.has_edge((1,'u'),(1,'v')), Q.has_edge((2,'u'),(2,'v')),
          " chi(G)=", chi(G), " from profiles:", chi_from_profiles([P1, Q], EJ),
          " Pi_3(P2):", [sorted(map(sorted, p)) for p in profile(Q, [(2,'u'),(2,'v')], 3)],
          " chi(Gamma)=", chi(Gam), " G planar:", nx.check_planarity(G)[0])
    print("   deg seq P2:", sorted(d for _, d in Q.degree()))

print("=== Example 3: gadget Q_pi (separation of profiles), q=3, J={u,v} ===")
def gadget(k, blocks, q):
    E = [(('z',i),('z',j)) for i in range(q) for j in range(i+1, q)]
    for i, B in enumerate(blocks):
        for x in B:
            E += [(x, ('z', j)) for j in range(q) if j != i]
    return piece(k, E)
for blocks in ([['u','v']], [['u'],['v']]):
    Q = gadget(2, blocks, 3)
    print(" gadget blocks", blocks, "Pi_3:", [sorted(map(sorted, p)) for p in profile(Q, [(2,'u'),(2,'v')], 3)])
    for name, Q1 in (("diamond", P1), ("A2-as-piece1", piece(1, [('u','a'),('u','b'),('a','b'),('a','w'),('b','w'),('w','v')]))):
        Gam, G, _ = assemble([Q1, Q], EJ)
        print("   glued with", name, "-> 3-colorable:", chi(G) <= 3)

print("=== Example 4: planarity, same coarse data ===")
K33me = piece(1, [(a, b) for a in ('x','a2','a3') for b in ('y','b2','b3') if (a, b) != ('x','y')])
prism = nx.circular_ladder_graph(3)  # 0-1-2 ring, 3-4-5 ring, rungs i-(i+3)
pr = piece(1, [e for e in prism.edges() if set(e) != {0, 3}])
pr = nx.relabel_nodes(pr, {(1, 0): (1, 'x'), (1, 3): (1, 'y')})
K2 = piece(2, [('x','y')]); EJ2 = [((1,'x'),(2,'x')), ((1,'y'),(2,'y'))]
for name, P in (("K33-e", K33me), ("prism-rung", pr)):
    Gam, G, _ = assemble([P, K2], EJ2)
    print(name, "n,m:", P.number_of_nodes(), P.number_of_edges(), "degs:", sorted(d for _, d in P.degree()),
          "piece planar:", nx.check_planarity(P)[0], "xy edge:", P.has_edge((1,'x'),(1,'y')), "-> G planar:", nx.check_planarity(G)[0])
