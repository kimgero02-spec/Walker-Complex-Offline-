# R21 researcher1: shadow-family certification test + (2,3) owned planar decomposition search.
# Reference/exploration only; claims in the report are proved by hand.
import itertools, sys
import networkx as nx

def chrom_le(G, k):
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
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
    return bt(0)

def chi(G):
    k = 0
    while not chrom_le(G, k): k += 1
    return k

def odd_cycles(G):
    # simple cycles as vertex lists (undirected), odd length
    D = G.to_directed()
    seen = set()
    for cyc in nx.simple_cycles(D):
        if len(cyc) >= 3 and len(cyc) % 2 == 1:
            key = frozenset(zip(cyc, cyc[1:] + cyc[:1]))
            key = frozenset(frozenset(e) for e in key)
            if key in seen: continue
            seen.add(key)
            yield cyc

def certified5(G, verbose=False):
    N = {v: set(G[v]) for v in G}
    cycles = list(odd_cycles(G))
    for z2 in G:
        for C in cycles:
            if z2 in C: continue
            Cn = {v: set() for v in C}
            m = len(C)
            for i in range(m):
                a, b = C[i], C[(i+1) % m]
                Cn[a].add(b); Cn[b].add(a)
            for z1 in G:
                if z1 == z2 or z1 in C: continue
                opts = []
                for v in C:
                    o = [s for s in N[z1] if s != z2 and Cn[v] <= N[s]]
                    if not o: break
                    opts.append(o)
                else:
                    for choice in itertools.product(*opts):
                        H = {v: set(Cn[v]) for v in C}
                        H.setdefault(z1, set())
                        for v, s in zip(C, choice):
                            H.setdefault(s, set())
                            H[z1].add(s); H[s].add(z1)
                            for w in Cn[v]:
                                H[s].add(w); H[w].add(s)
                        ok = True
                        for v in H:
                            if not any(H[v] <= N[t] for t in N[z2] if True):
                                ok = False; break
                        if ok:
                            if verbose: print('cert', z2, C, z1, choice)
                            return True
    return False

def hajos(G1, x1, y1, G2, x2, y2):
    G = nx.Graph()
    G.add_edges_from((('A', u), ('A', v)) for u, v in G1.edges())
    G.add_edges_from((('B', u), ('B', v)) for u, v in G2.edges())
    G.remove_edge(('A', x1), ('A', y1)); G.remove_edge(('B', x2), ('B', y2))
    G = nx.contracted_nodes(G, ('A', x1), ('B', x2), self_loops=False)
    G.add_edge(('A', y1), ('B', y2))
    return nx.convert_node_labels_to_integers(G, label_attribute='old')

def owned_decomps(G, limit=1):
    V = list(G.nodes()); E = [tuple(e) for e in G.edges()]
    found = []
    for r in range(2, len(V)-2):
        for V1 in itertools.combinations(V, r):
            V1 = set(V1); V2 = set(V) - V1
            G1 = G.subgraph(V1); G2 = G.subgraph(V2)
            if not nx.is_bipartite(G1) or G1.number_of_edges() == 0: continue
            if not chrom_le(G2, 3): continue
            if chrom_le(G2, 2): continue
            cross = [e for e in E if (e[0] in V1) != (e[1] in V1)]
            for mask in range(1 << len(cross)):
                P1 = nx.Graph(); P1.add_edges_from(G1.edges())
                P2 = nx.Graph(); P2.add_edges_from(G2.edges())
                for i, e in enumerate(cross):
                    (P1 if mask >> i & 1 else P2).add_edge(*e)
                if not nx.is_bipartite(P1): continue
                if not nx.check_planarity(P1)[0]: continue
                if not nx.check_planarity(P2)[0]: continue
                if not chrom_le(P2, 3): continue
                found.append((V1, list(P1.edges()), list(P2.edges())))
                if len(found) >= limit: return found
    return found

if __name__ == '__main__':
    K5 = nx.complete_graph(5)
    H = hajos(K5, 0, 1, K5, 0, 1)
    print('Hajos n,m', H.number_of_nodes(), H.number_of_edges(), 'chi', chi(H))
    print('K5 certified', certified5(K5))
    print('Hajos certified', certified5(H, True))
    d = owned_decomps(H)
    print('decomp', d)
