# R04 researcher3: SAT for the planar pair condition (no common-neighbour set of a pair meets all three zones)
import itertools, time, numpy as np, networkx as nx
from pysat.solvers import Cadical153
from scipy.spatial import Delaunay
def pairs_of(G):
    out=[]
    for a,b in itertools.combinations(G.nodes(),2):
        C=sorted(set(G[a])&set(G[b]))
        if len(C)>=3: out.append((a,b,C))
    return out
def solve(G, extra=None, tl=None):
    nodes=list(G.nodes()); idx={v:i for i,v in enumerate(nodes)}; n=len(nodes)
    var={}
    def X(i,j):
        if i<j: return var.setdefault((i,j),len(var)+1)
        return -var.setdefault((j,i),len(var)+1)
    S=Cadical153()
    for i,j,k in itertools.permutations(range(n),3):
        S.add_clause([-X(i,j),-X(j,k),X(i,k)])
    npair=0
    for a,b,C in pairs_of(G):
        npair+=1
        a,b=idx[a],idx[b]; Ci=[idx[c] for c in C]
        for (p,q) in ((a,b),(b,a)):
            for c1,c2,c3 in itertools.permutations(Ci,3):
                S.add_clause([-X(c1,p),-X(p,c2),-X(c2,q),-X(q,c3)])
    if extra: extra(S,X,idx)
    r=S.solve()
    if not r: return False,npair
    m=S.get_model(); ms=set(l for l in m if l>0)
    pos=[sum(1 for j in range(n) if j!=i and (X(j,i)>0 and X(j,i) in ms or X(j,i)<0 and -X(j,i) not in ms)) for i in range(n)]
    order=sorted(nodes,key=lambda v:pos[idx[v]])
    return order,npair
def check(G,order):
    pos={v:i for i,v in enumerate(order)}
    for a,b,C in pairs_of(G):
        lo,hi=sorted((pos[a],pos[b]))
        z=set(0 if pos[c]<lo else (1 if pos[c]<hi else 2) for c in C)
        if len(z)==3: return False
    return True
def tri_graph(seed,n):
    rng=np.random.default_rng(seed); P=rng.random((n,2)); T=Delaunay(P)
    G=nx.Graph()
    for s in T.simplices: G.add_edges_from([(int(s[0]),int(s[1])),(int(s[1]),int(s[2])),(int(s[0]),int(s[2]))])
    return G
def stacked(seed,n):
    rng=np.random.default_rng(seed); G=nx.complete_graph(3); faces=[(0,1,2),(0,1,2)]
    for v in range(3,n):
        f=faces.pop(rng.integers(len(faces))); a,b,c=f
        G.add_edges_from([(v,a),(v,b),(v,c)]); faces+= [(a,b,v),(b,c,v),(a,c,v)]
    return G
if __name__=="__main__":
    import sys
    for n in (14,20,30,40,60,80):
        for seed in range(3):
            G=tri_graph(seed,n); t=time.time(); o,npair=solve(G)
            print("delaunay",n,seed,"pairs>=3:",npair, "SAT" if o else "UNSAT", (check(G,o) if o else None), round(time.time()-t,1),flush=True)
