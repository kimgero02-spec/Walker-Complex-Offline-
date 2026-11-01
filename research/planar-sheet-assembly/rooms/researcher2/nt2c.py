# 추측 Q5 반례 찾기: 평면 P, q=5 에서 Pi_5(P,J) 가 'P[J] 에서 블록이 독립인 모든 분할' 보다 작은 J 가 있는가
import networkx as nx, itertools, sys, io
_o = sys.stdout; sys.stdout = io.StringIO()
from nt2 import profile, partitions, colorable
sys.stdout = _o
G = nx.icosahedral_graph()
hit = None
for s in (3, 4):
    for J in itertools.combinations(G.nodes(), s):
        allowed = {frozenset(frozenset(b) for b in p) for p in partitions(J)
                   if len(p) <= 5 and all(not G.has_edge(x, y) for b in p for x, y in itertools.combinations(b, 2))}
        pr = profile(G, list(J), 5)
        if pr != allowed:
            hit = (J, allowed - pr); break
    if hit: break
print("icosahedron, q=5:", "반례" if hit else "반례 없음 (|J|<=4)", hit if hit else "")
