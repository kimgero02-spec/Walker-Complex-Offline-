import networkx as nx, itertools, numpy as np, time
from networkx.generators.atlas import graph_atlas_g
from n1_lib2 import *
def poset(pairs):
    P=set()
    for a,b in pairs: P.add((a,b)); P.add((b,a))
    return sorted(P)
def chains(P):
    lt={p:[q for q in P if q[0]!=p[0] and q[0]&p[0]==p[0]] for p in P}  # q>p
    ch=[[ (p,) for p in P ]]
    while True:
        nxt=[c+(q,) for c in ch[-1] for q in lt[c[-1]]]
        if not nxt: break
        ch.append(nxt)
    return ch
def rank2(M):
    M=M.copy()%2; r=0; rows,cols=M.shape
    for c in range(cols):
        piv=None
        for i in range(r,rows):
            if M[i,c]: piv=i;break
        if piv is None: continue
        M[[r,piv]]=M[[piv,r]]
        for i in range(rows):
            if i!=r and M[i,c]: M[i]^=M[r]
        r+=1
        if r==rows: break
    return r
def betti(ch):
    idx=[{c:i for i,c in enumerate(L)} for L in ch]
    ranks=[0]
    for k in range(1,len(ch)):
        M=np.zeros((len(ch[k-1]),len(ch[k])),dtype=np.uint8)
        for j,c in enumerate(ch[k]):
            for t in range(len(c)):
                f=c[:t]+c[t+1:]
                M[idx[k-1][f],j]^=1
        ranks.append(rank2(M))
    ranks.append(0)
    return [len(ch[k])-ranks[k]-ranks[k+1] for k in range(len(ch))]
if __name__=="__main__":
  for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<5 or n>7 or G.number_of_edges()==0: continue
    pairs=maxbic(G)
    z=zig(n,pairs)
    if z<4: continue
    P=poset(pairs); ch=chains(P)
    print(n,G.number_of_edges(),"zig",z,"ell",len(ch),"betti2",betti(ch),flush=True)
