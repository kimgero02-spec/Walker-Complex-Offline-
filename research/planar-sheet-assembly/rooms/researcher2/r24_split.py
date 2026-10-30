# R24 researcher2: 두 조각 소유 분할의 가법성 후보 (S1: 단일 공유 부류 증인) 반례 탐색용.
# 근거가 아니라 반례 찾기 도구이다.
import itertools, random, sys
import networkx as nx

def chi(G, nodes=None, cap=12):
    H = G if nodes is None else G.subgraph(nodes)
    V = list(H.nodes())
    if not V: return 0
    if H.number_of_edges() == 0: return 1
    adj = {v: set(H[v]) for v in V}
    V.sort(key=lambda v: -len(adj[v]))
    for k in range(1, cap+1):
        col = {}
        def bt(i):
            if i == len(V): return True
            v = V[i]; used = {col[u] for u in adj[v] if u in col}
            mx = max(col.values(), default=-1)
            for c in range(min(k, mx+2)):
                if c not in used:
                    col[v] = c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return k
    return None

def indep_sets(G, nodes):
    nodes = list(nodes)
    out = []
    for r in range(1, len(nodes)+1):
        for S in itertools.combinations(nodes, r):
            if all(not G.has_edge(a, b) for a, b in itertools.combinations(S, 2)):
                out.append(frozenset(S))
    return out

def removable(G, Vk, ak):
    """독립집합 I ⊆ Vk 로 chi(G[Vk]-I) = ak-1 인 것 (극대인 것만 충분: 상위집합도 됨)."""
    res = []
    for I in indep_sets(G, Vk):
        if chi(G, set(Vk) - I) <= ak - 1:
            res.append(I)
    return res

def single_witness(G, V1, V2):
    a1, a2 = chi(G, V1), chi(G, V2)
    R1, R2 = removable(G, V1, a1), removable(G, V2, a2)
    for I1 in R1:
        for I2 in R2:
            if all(not G.has_edge(x, y) for x in I1 for y in I2):
                return (I1, I2)
    return None

def check(G, V1, V2):
    a1, a2 = chi(G, V1), chi(G, V2)
    q = chi(G)
    w = single_witness(G, V1, V2)
    return a1, a2, q, w

if __name__ == '__main__':
    random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
    found = 0
    for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 3000):
        n = random.randint(5, 9)
        p = random.uniform(0.3, 0.8)
        G = nx.gnp_random_graph(n, p, seed=random.randrange(10**9))
        V = list(G.nodes()); random.shuffle(V)
        k = random.randint(2, n-2)
        V1, V2 = set(V[:k]), set(V[k:])
        a1, a2, q, w = check(G, V1, V2)
        if q < a1 + a2 and w is None:
            print('COUNTEREX', n, sorted(G.edges()), sorted(V1), sorted(V2), a1, a2, q)
            found += 1
            if found > 5: break
    print('done', found)
