# F-R5: V8 이 평면 조각의 <=3 클릭 합의 부분그래프가 아님을 위한 결정적 확인
# (분리집합 S, |S|<=3 마다 각 쪽 + S 위 클릭 이 평면인지 본다)
import networkx as nx, itertools
V8 = nx.circulant_graph(8, [1, 4])
print("V8 3-연결:", nx.node_connectivity(V8) == 3, "평면:", nx.check_planarity(V8)[0])
bad = []
for r in (1, 2, 3):
    for S in itertools.combinations(V8, r):
        R = V8.copy(); R.remove_nodes_from(S)
        comps = list(nx.connected_components(R))
        if len(comps) < 2: continue
        for c in comps:
            side = V8.subgraph(set(c) | set(S)).copy()
            side.add_edges_from(itertools.combinations(S, 2))
            others = set(V8) - set(c) - set(S)
            other = V8.subgraph(others | set(S)).copy(); other.add_edges_from(itertools.combinations(S, 2))
            bad.append((S, len(c), nx.check_planarity(side)[0], len(others), nx.check_planarity(other)[0]))
for b in bad: print("S=", b[0], "|한쪽|=", b[1], "평면", b[2], "| 다른쪽|=", b[3], "평면", b[4])

# 재귀 판정: X 가 "평면 그래프들의 <=3 클릭 합의 부분그래프" 인가
from functools import lru_cache
def key(X): return nx.weisfeiler_lehman_graph_hash(X) + str(sorted(d for _, d in X.degree()))
memo = {}
def in_class(X):
    k = (key(X), X.number_of_nodes(), X.number_of_edges())
    if k in memo: return memo[k]
    if nx.check_planarity(X)[0]: memo[k] = True; return True
    res = False
    for r in (0, 1, 2, 3):
        for S in itertools.combinations(X, r):
            R = X.copy(); R.remove_nodes_from(S)
            comps = [set(c) for c in nx.connected_components(R)]
            if len(comps) < 2: continue
            for mask in range(1, 2 ** (len(comps) - 1)):
                A = set().union(*[c for i, c in enumerate(comps) if mask >> i & 1])
                B = set(R) - A
                XA = X.subgraph(A | set(S)).copy(); XA.add_edges_from(itertools.combinations(S, 2))
                XB = X.subgraph(B | set(S)).copy(); XB.add_edges_from(itertools.combinations(S, 2))
                if in_class(XA) and in_class(XB): res = True; break
            if res: break
        if res: break
    memo[k] = res; return res
print("V8 in class:", in_class(V8))
print("K5 in class:", in_class(nx.complete_graph(5)), "K33 in class:", in_class(nx.complete_bipartite_graph(3, 3)))
