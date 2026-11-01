"""'비분리' 가정의 필요성: 유도되었지만 분리하는 사이클 조각으로 비자명 홀로노미 + 평면 예를 찾는다."""
import itertools, networkx as nx
from holo import *
from need3conn import cycles
for G,name in ((nx.complete_bipartite_graph(2,3),"K23"),(nx.complete_bipartite_graph(2,4),"K24"),(nx.cubical_graph(),"Q3"),(nx.octahedral_graph(),"octa")):
    ind=[c for c in cycles(G) if G.subgraph(c).number_of_edges()==len(c)]
    hit=None
    for r in (2,3,4):
        for S in itertools.combinations(ind,r):
            H,m=overlap_graph(list(S))
            if max(m.values())<=2 and nx.is_connected(nx.Graph(H)) and not holonomy_trivial(H):
                hit=S;break
        if hit:break
    print(name,"평면",nx.check_planarity(G)[0],"유도 사이클 조각으로 비자명 홀로노미:",hit,
          "| 조각 주변?",[is_peripheral(G,c) for c in hit] if hit else "")
