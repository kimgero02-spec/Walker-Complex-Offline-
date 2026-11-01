from lib import *
from collections import Counter
def summary(name,B,W):
    print("==",name,"n",B.number_of_nodes(),"planar",nx.check_planarity(B)[0],"|W|",len(W),"chi(B[W])",
          min(k for k in range(1,7) if colorable(B.subgraph(W),k) is not None))
    for q in (4,5,6):
        S,I=realized(B,W,q)
        cS=Counter(len(p) for p in S); cI=Counter(len(p) for p in I)
        print(f" q={q}: |I|={len(I)} |S|={len(S)}  by blocks S:{dict(sorted(cS.items()))} I:{dict(sorted(cI.items()))}")
        if q==6:
            miss=[p for p in I if p not in S]
            print("  missing at q=6 (first 5):",miss[:5])
# Apollonian A
A=nx.Graph(); A.add_edges_from(itertools.combinations('pqrs',2))
for new,face in (("P","qrs"),("Q","prs"),("R","pqs")): A.add_edges_from((new,f) for f in face)
summary("Apollonian A, W={p,q,r,p',q',r'}",A,list("pqrPQR"))
# icosahedron, W = link of vertex 0
I=nx.icosahedral_graph(); W=list(I[0])
summary("icosahedron, W=link C5",I,W)
W2=W+[ [v for v in I if v!=0 and v not in I[0] and not any(u in I[0] for u in I[v])][0] ]
summary("icosahedron, W=link+antipode",I,W2)
# Tutte fragment (R49-r2 W)
Wadj={'x':'y z p q1 q2 q3','y':'x z p q4 q5','z':'x y q1 q5','p':'x y q3 q4','c':'q1 q2 q3 q4 q5'}
T=nx.Graph()
for u,vs in Wadj.items():
    for v in vs.split(): T.add_edge(u,v)
for i in range(1,6): T.add_edge(f'q{i}',f'q{i%5+1}')
summary("Tutte fragment, W={x,y,z,p}",T,['x','y','z','p'])
summary("Tutte fragment, W={x,y,z,c}",T,['x','y','z','c'])
summary("Tutte fragment, W=q1..q5",T,[f'q{i}' for i in range(1,6)])
