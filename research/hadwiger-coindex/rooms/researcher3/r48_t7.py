from r48_at import *
import networkx as nx, time
I=nx.icosahedral_graph()
G=nx.Graph(); G.add_edges_from(I.edges()); G.add_edges_from((u+12,v+12) for u,v in I.edges())
# 교차: 정점 i (V1) -> 12+i, 12+anti?  간단히 i -> 12+((i+s)%12), s in 0,1,5 (3-정칙 이분)
for i in range(12):
    for s in (0,1,5): G.add_edge(i,12+(i+s)%12)
E=list(G.edges()); print('deg',set(dict(G.degree()).values()),'|E|',len(E),'degen',max(nx.core_number(G).values()))
for k in (5,6): print('chi<=%d'%k, proper_coloring(24,E,[list(range(k))]*24) is not None)
t0=time.time()
c=coef(24,E,[4]*24); print('coef x^(4^24)=',c,round(time.time()-t0,1))
