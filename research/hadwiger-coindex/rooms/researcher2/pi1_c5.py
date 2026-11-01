import itertools, networkx as nx
G=nx.cycle_graph(5)
V=[(v,s) for v in range(5) for s in (1,2)]
def isface(S):
    A=[v for v,s in S if s==1]; B=[v for v,s in S if s==2]
    if set(A)&set(B): return False
    return all(G.has_edge(a,b) for a in A for b in B)
faces={k:[S for S in itertools.combinations(V,k) if isface(S)] for k in (1,2,3,4,5)}
print({k:len(v) for k,v in faces.items()})
edges=faces[2]; tris=faces[3]
H=nx.Graph(); H.add_nodes_from(V); H.add_edges_from(edges)
T=nx.minimum_spanning_tree(H); tree={frozenset(e) for e in T.edges()}
gens={frozenset(e) for e in edges}-tree
# 정점 순서에 따른 방향 있는 간선 글자: (u,v) u<v ; 나무 간선=항등
def letter(u,v):
    e=frozenset((u,v))
    return None if e in tree else e
rels=[]
for t in tris:
    a,b,c=t
    ws=[letter(a,b),letter(b,c),letter(a,c)]
    rels.append([w for w in ws if w is not None])
trivial=set(); changed=True
while changed:
    changed=False
    for r in rels:
        rest=[w for w in r if w not in trivial]
        # 관계 g1 g2 g3^-1 = 1 : 하나만 남으면 그 생성원 자명; 같은 생성원이 둘이고 나머지 자명이면 g=g^{±1}.. 보수적으로 처리
        if len(rest)==1 and rest[0] not in trivial:
            trivial.add(rest[0]); changed=True
print("생성원 수",len(gens),"자명으로 소거된 수",len(trivial&gens))
