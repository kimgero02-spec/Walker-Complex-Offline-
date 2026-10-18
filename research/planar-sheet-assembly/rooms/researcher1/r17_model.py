# R17: 예 1.3 의 매뉴얼 M 에서 K5 마이너 모형(가지 집합) 찾기. 예 확인용.
import networkx as nx, itertools
from r17_hadwiger import manual
V4=[0,1,2,3]
ex13=[(V4,[(0,1),(1,3),(3,2),(2,0)]),(V4,[(0,3),(3,1),(1,2),(2,0)])]
Mc,M,mu=manual(ex13)
print('E11',[e for e in M.edges() if e not in Mc.edges()])
def search(G,t):
    H=nx.Graph(); H.add_nodes_from(frozenset([v]) for v in G)
    for a,b in G.edges(): H.add_edge(frozenset([a]),frozenset([b]))
    seen=set(); st=[H]
    while st:
        H=st.pop()
        k=frozenset(H.nodes())
        if k in seen or H.number_of_nodes()<t: continue
        seen.add(k)
        for c in nx.find_cliques(H):
            if len(c)>=t: return c[:t]
        for a,b in list(H.edges()):
            H2=nx.contracted_nodes(H,a,b,self_loops=False)
            H2=nx.relabel_nodes(H2,{a:a|b})
            st.append(H2)
for bs in search(M,5): print(sorted(bs,key=str))
