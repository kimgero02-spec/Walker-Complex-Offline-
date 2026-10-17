# R26 fast: K7 minor test on <=9 vertices via explicit minor models (guessing aid)
import itertools, networkx as nx

def k7_minor(G):
    V = list(G.nodes()); n = len(V)
    if n < 7:
        return False
    adj = {v: set(G[v]) for v in V}
    E = [tuple(e) for e in G.edges()]

    def adjb(A, B):
        return any(b in adj[a] for a in A for b in B)

    def is_k7(blocks):
        return all(adjb(blocks[i], blocks[j]) for i in range(7) for j in range(i + 1, 7))

    # a) delete n-7 vertices, rest singletons
    for D in itertools.combinations(V, n - 7):
        R = [v for v in V if v not in D]
        if is_k7([[v] for v in R]):
            return True
    # b) one pair block (an edge), delete n-8 vertices, rest singletons
    if n >= 8:
        for e in E:
            rest = [v for v in V if v not in e]
            for D in itertools.combinations(rest, n - 8):
                R = [v for v in rest if v not in D]
                if is_k7([list(e)] + [[v] for v in R]):
                    return True
    # c) n == 9: two disjoint pair blocks, or one connected triple, no deletion
    if n == 9:
        for e1, e2 in itertools.combinations(E, 2):
            if set(e1) & set(e2):
                continue
            rest = [v for v in V if v not in e1 and v not in e2]
            if is_k7([list(e1), list(e2)] + [[v] for v in rest]):
                return True
        for T in itertools.combinations(V, 3):
            if not nx.is_connected(G.subgraph(T)):
                continue
            rest = [v for v in V if v not in T]
            if is_k7([list(T)] + [[v] for v in rest]):
                return True
    return False
