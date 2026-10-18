# three relabeled dodecahedra A,B,C on 20 vertices, pairwise "frozen" (each class + any other edge nonplanar).
import random, sys, networkx as nx
from r20_frozen import planar
seed=int(sys.argv[1]); rng=random.Random(seed)
D=nx.dodecahedral_graph(); N=20
base=[tuple(e) for e in D.edges()]
def rel(p): return [tuple(sorted((p[a],p[b]))) for a,b in base]
# cofacial-type test: for 3-connected planar X, X+e planar iff endpoints cofacial; we just use planarity directly
def bad_pairs(X):
    # set of non-edges uv with X+uv planar
    S=set(X); out=set()
    for u in range(N):
        for v in range(u+1,N):
            if (u,v) not in S and planar(X+[(u,v)]): out.add((u,v))
    return out
def cost(cls, bads):
    c=0
    for i,X in enumerate(cls):
        for j,Y in enumerate(cls):
            if i==j: continue
            for e in Y:
                if e in set(X) or e in bads[i]: c+=1
    return c
p=[list(range(N)) for _ in range(3)]
for q in p[1:]: rng.shuffle(q)
cls=[rel(q) for q in p]; bads=[bad_pairs(X) for X in cls]
cur=cost(cls,bads)
for it in range(4000):
    k=rng.choice([1,2]); i,j=rng.sample(range(N),2)
    p[k][i],p[k][j]=p[k][j],p[k][i]
    cls[k]=rel(p[k]); bads[k]=bad_pairs(cls[k])
    c=cost(cls,bads)
    if c<=cur or rng.random()<0.01: cur=c
    else:
        p[k][i],p[k][j]=p[k][j],p[k][i]; cls[k]=rel(p[k]); bads[k]=bad_pairs(cls[k])
    if cur==0: break
print("seed",seed,"final cost",cur, "it",it)
if cur==0:
    print("P=",p)
