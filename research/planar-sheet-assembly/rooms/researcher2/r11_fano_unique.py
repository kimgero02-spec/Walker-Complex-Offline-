import itertools, networkx as nx
from r11_levi import manual, recognize
fano=[(0,1,3),(1,2,4),(2,3,5),(3,4,6),(4,5,0),(5,6,1),(6,0,2)]
Mo,M,G,mu=manual([(list(b),list(itertools.combinations(b,2))) for b in fano])
tri=set()
for c in nx.enumerate_all_cliques(Mo):
    if len(c)==3: tri|=set(c)
cand=[x for x in Mo if x not in tri]
print('non-triangle vertices',len(cand))
# W 는 삼각형 점을 가질 수 없다 (흰 점 이웃 비인접). 따라서 W ⊆ cand 만 보면 충분
sols=[]
import r11_levi
for r in range(len(cand)+1):
    for W in itertools.combinations(cand,r):
        H=Mo.copy()
        # recognize 를 W 고정으로 돌리기 위해 내부 논리 재사용: 부분 그래프 대신 직접 검사
        Ws=set(W);B=[x for x in Mo if x not in Ws]
        if any(len([y for y in Mo[w]])<2 for w in W): continue
        if any(sum(1 for y in Mo[b] if y in Ws)>1 for b in B): continue
        XB=Mo.subgraph(B); cid={x:i for i,c in enumerate(nx.connected_components(XB)) for x in c}
        if any(len({cid[y] for y in Mo[w]})<3 for w in W): continue
        if not all(nx.check_planarity(XB.subgraph(c))[0] for c in nx.connected_components(XB)): continue
        cls={b:b for b in B}
        for w in W:
            for y in Mo[w]: cls[y]=w
        Q=nx.Graph(); Q.add_nodes_from(set(cls.values())); Q.add_edges_from((cls[a],cls[b]) for a,b in XB.edges())
        n=Q.number_of_nodes()
        if Q.number_of_edges()==n*(n-1)//2: sols.append(len(W))
print('valid W sizes',sols)
