"""C 의 3-연결 가정이 필요한지 시험: 2-연결(3-연결 아님) 평면 그래프에서
주변 사이클 조각 몇 개(각 변 ≤2)가 비자명 홀로노미를 갖는 예 하나를 찾는다(찾으면 멈춤)."""
import itertools, networkx as nx
from networkx.generators.atlas import graph_atlas_g
from holo import *
def cycles(G):
    out={};
    for c in nx.simple_cycles(G.to_directed()):
        if len(c)>=3: out.setdefault(frozenset(c) if len(c)>3 or True else None, c)
    # 같은 정점집합 다른 사이클 구분: 변집합으로
    res={}
    for c in nx.simple_cycles(G.to_directed()):
        if len(c)>=3: res.setdefault(frozenset(frozenset(e) for e in cyc_edges(c)), c)
    return list(res.values())
for G in graph_atlas_g():
    if G.number_of_nodes()<4 or not nx.is_connected(G): continue
    if not nx.is_biconnected(G) or nx.node_connectivity(G)>=3 or not nx.check_planarity(G)[0]: continue
    per=[c for c in cycles(G) if is_peripheral(G,c)]
    hit=None
    for r in (2,3):
        for S in itertools.combinations(per,r):
            H,m=overlap_graph(list(S))
            if max(m.values())<=2 and nx.is_connected(nx.Graph(H)) and not holonomy_trivial(H):
                hit=S;break
        if hit: break
    if hit:
        print("발견:", sorted(G.edges()), "조각:", hit); break
else: print("7점 이하에서 없음")
