# 보조정리 후보 L': "G 에 K4 마이너가 있고 모든 K4 모형이 u,v 를 가르면 G/{u=v} 에 K4 마이너가 없다" 의 반례 탐색 (그래프 아틀라스 <=7 점)
import networkx as nx, itertools
from r25_hard import k4free, chi, hard, ident
res=[]
for G in nx.graph_atlas_g():
    if G.number_of_nodes()<5 or k4free(G): continue
    for u,v in itertools.combinations(G.nodes(),2):
        if G.has_edge(u,v): continue
        if hard(G,u,v):
            H=ident(G,u,v)
            res.append((not k4free(H), G.number_of_nodes(),G.number_of_edges(),sorted(G.edges()),u,v,chi(G)))
res.sort(key=lambda r:(not r[0],r[1],r[2]))
print("hard cases:",len(res),"of which H has K4:",sum(r[0] for r in res))
for r in res[:8]: print(r)
