# R06 researcher3: independent check of Q* (R05-researcher1) -- own code, no reuse.
import itertools, networkx as nx

def qstar():
    Q = nx.Graph()
    M = ['m1','m2','m3']
    Q.add_edges_from([('m1','m2'),('m2','m3'),('m1','m3')])
    for i in (1,2,3):
        for j in (1,2,3):
            if j != i:
                Q.add_edge(f'a{i}', f'm{j}'); Q.add_edge(f'b{i}', f'm{j}')
    Q.add_edges_from([('a1','b2'),('a2','b3'),('a3','b1')])
    return Q

def add_leaf(G, T, tag):
    x, y = tag+'x', tag+'y'
    G.add_edge(x, y)
    for t in T:
        G.add_edge(x, t); G.add_edge(y, t)

def colorable(G, k):
    """plain backtracking, DSATUR-ish order; returns a coloring or None"""
    nodes = sorted(G, key=lambda v: -G.degree(v))
    col = {}
    def bt(i):
        if i == len(nodes): return True
        v = nodes[i]
        used = {col[u] for u in G[v] if u in col}
        for c in range(k):
            if c not in used:
                col[v] = c
                if bt(i+1): return True
                del col[v]
        return False
    return dict(col) if bt(0) else None

def all_colorings(Q, k):
    nodes = list(Q)
    idx = {v:i for i,v in enumerate(nodes)}
    out = []
    for cs in itertools.product(range(k), repeat=len(nodes)):
        if all(cs[idx[u]] != cs[idx[v]] for u,v in Q.edges()):
            out.append(dict(zip(nodes, cs)))
    return out

def rainbow(c, T): return len({c[t] for t in T}) == 3

if __name__ == '__main__':
    Q = qstar()
    T1, T2 = ['a1','a2','a3'], ['b1','b2','b3']
    print('Q*: |V|,|E| =', Q.number_of_nodes(), Q.number_of_edges())
    print('T1,T2 independent:', all(not Q.has_edge(u,v) for T in (T1,T2) for u,v in itertools.combinations(T,2)))
    print('Q* planar:', nx.check_planarity(Q)[0], ' chi(Q*)<=3:', colorable(Q,3) is not None, ' 2-col:', colorable(Q,2) is not None)
    # exhaustive over 4^9 assignments (a finite fact, not statistics)
    C4 = all_colorings(Q, 4)
    bad = [c for c in C4 if not rainbow(c,T1) and not rainbow(c,T2)]
    print('4-colorings of Q*:', len(C4), ' both-nonrainbow:', len(bad))
    G = Q.copy(); add_leaf(G, T1, 'L1'); add_leaf(G, T2, 'L2')
    print('G: |V|,|E| =', G.number_of_nodes(), G.number_of_edges())
    print('G 4-colorable (backtracking):', colorable(G,4) is not None)
    c5 = colorable(G,5); print('G 5-colorable:', c5 is not None)
    # networkx independent check: greedy strategies give an upper bound; check validity
    best = min(max(nx.greedy_color(G, s).values())+1 for s in
               ['largest_first','smallest_last','DSATUR','independent_set','connected_sequential_bfs'])
    print('networkx greedy upper bound:', best)
    # networkx-based 4-colorability check by a different method: H-homomorphism to K4 via
    # exhaustive over colorings of Q* then leaf extension test (leaf K2+T needs T nonrainbow).
    # (already = 'bad' count above.)  Also check leaves are planar and pieces chi:
    L = nx.Graph(); add_leaf(L, T1, 'L'); print('leaf K113 planar:', nx.check_planarity(L)[0], 'chi(leaf)=3')
    # edge-minimality and edge-deletion planarity
    for e in list(Q.edges()):
        Qe = Q.copy(); Qe.remove_edge(*e)
        C = all_colorings(Qe, 4)
        nb = sum(1 for c in C if not rainbow(c,T1) and not rainbow(c,T2))
        print('  delete', e, ': planar', nx.check_planarity(Qe)[0], ' both-nonrainbow colorings', nb)
