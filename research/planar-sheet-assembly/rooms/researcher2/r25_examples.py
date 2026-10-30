# R25 연구원2: 본문 예의 손 계산 대조용 (근거 아님)
import networkx as nx, itertools
from r25_hard import k4free, chi, hard, ident
def rep(name,G,u,v):
    H=ident(G,u,v)
    print(name,"chi=",chi(G),"K4(G)=",not k4free(G),"hard=",hard(G,u,v),"K4(G/uv)=",not k4free(H),"chi(G/uv)=",chi(H))
K33=nx.complete_bipartite_graph(3,3)  # 0,1,2 | 3,4,5
rep("K33 u,v same side",K33,0,1)
K33e=K33.copy(); K33e.add_edge(1,2)
rep("K33+vw",K33e,0,1)
Oct=nx.octahedral_graph(); 
anti=[(a,b) for a,b in itertools.combinations(Oct,2) if not Oct.has_edge(a,b)][0]
rep("octahedron antipodal",Oct,*anti)
S=nx.Graph([(0,1),(0,5),(1,2),(1,4),(2,3),(2,5),(3,4),(4,5)])
rep("K4 two opposite edges subdivided",S,0,3)
# K4 hajos K4: K4 on x,a1,b1,y1 and x,a2,b2,y2
HH=nx.Graph()
for Q in (["x","a1","b1","y1"],["x","a2","b2","y2"]):
    HH.add_edges_from(itertools.combinations(Q,2))
HH.remove_edge("x","y1"); HH.remove_edge("x","y2"); HH.add_edge("y1","y2")
for u,v in itertools.combinations(HH,2):
    if not HH.has_edge(u,v): rep(f"K4^K4 ({u},{v})",HH,u,v)
W=nx.wheel_graph(6) # hub 0, rim 1..5
rep("W5 rim (1,3)",W,1,3)
# 3-connected 4-critical graphs on <=7 vertices with nonadjacent pair, G-u and G-v K4-free
def critical(G,k=4):
    if chi(G)<k: return False
    return all(chi(nx.restricted_view(G,[],[e]))<k for e in G.edges())
for G in nx.graph_atlas_g():
    if G.number_of_nodes()<5 or not nx.is_connected(G): continue
    if nx.node_connectivity(G)<3: continue
    if not critical(G): continue
    for u,v in itertools.combinations(G,2):
        if G.has_edge(u,v): continue
        if k4free(G.subgraph([x for x in G if x!=u])) and k4free(G.subgraph([x for x in G if x!=v])):
            print("3conn crit, both deletions K4-free:",G.number_of_nodes(),sorted(G.edges()),u,v)
