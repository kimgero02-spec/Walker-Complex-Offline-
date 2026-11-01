"""Check: cubic Hamiltonian G with Ham. cycle W: g(G) = (1/2) min_sigma rank_Z2 A'_sigma
(A' = interlace matrix of bouquet: annulus N(W) as disk+band e0, chord feet on L/R sides).
Independent check: brute-force face tracing over all 2^V rotation systems."""
import networkx as nx, itertools, numpy as np
from surf import rank2

def ham_cycle(G):
    n = G.number_of_nodes(); nodes = list(G)
    def dfs(path, seen):
        if len(path) == n:
            return path if G.has_edge(path[-1], path[0]) else None
        for y in G[path[-1]]:
            if y not in seen:
                r = dfs(path + [y], seen | {y})
                if r: return r
        return None
    return dfs([nodes[0]], {nodes[0]})

def genus_rank(G, W):
    L = len(W); pos = {v: t for t, v in enumerate(W)}
    Wed = {frozenset((W[t], W[(t+1) % L])) for t in range(L)}
    chords = [tuple(e) for e in G.edges() if frozenset(e) not in Wed]
    best = None
    for sig in itertools.product([0, 1], repeat=L):  # side of the chord-foot at each W vertex
        # circular sequence: e0, L feet 0..L-1, e0, R feet L-1..0
        seq = [('e0',)]
        seq += [('c', v) for v in W if sig[pos[v]] == 0]
        seq += [('e0',)]
        seq += [('c', v) for v in reversed(W) if sig[pos[v]] == 1]
        idx = {}
        for t, s in enumerate(seq):
            key = 'e0' if s[0] == 'e0' else next(i for i, c in enumerate(chords) if s[1] in c)
            idx.setdefault(key, []).append(t)
        keys = list(idx)
        m = len(keys); A = np.zeros((m, m), dtype=np.uint8)
        for i, j in itertools.combinations(range(m), 2):
            a, b = idx[keys[i]]; c, d = idx[keys[j]]
            if (a < c < b) != (a < d < b):
                A[i, j] = A[j, i] = 1
        rk = rank2(A)
        best = rk if best is None else min(best, rk)
    return best / 2

def genus_brute(G):
    nodes = list(G); nbrs = {v: list(G[v]) for v in nodes}
    V, E = G.number_of_nodes(), G.number_of_edges()
    best = None
    for choice in itertools.product([0, 1], repeat=V):
        rot = {}
        for v, c in zip(nodes, choice):
            nb = nbrs[v]; order = nb if c == 0 else [nb[0], nb[2], nb[1]]
            rot[v] = {order[i]: order[(i+1) % 3] for i in range(3)}
        seen = set(); F = 0
        for u in nodes:
            for w in nbrs[u]:
                if (u, w) in seen: continue
                F += 1; a, b = u, w
                while (a, b) not in seen:
                    seen.add((a, b)); a, b = b, rot[b][a]
        g = (2 - V + E - F) // 2
        best = g if best is None else min(best, g)
    return best

tests = {"K4": nx.complete_graph(4), "K33": nx.complete_bipartite_graph(3, 3),
         "cube": nx.hypercube_graph(3), "Heawood": nx.heawood_graph(),
         "MobiusKantor": nx.LCF_graph(16, [5, -5], 8)}
for name, G in tests.items():
    G = nx.convert_node_labels_to_integers(G)
    W = ham_cycle(G)
    print(name, "rank-formula genus", genus_rank(G, W), " brute genus", genus_brute(G))
