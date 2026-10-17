# R10: Groetzsch vertex split with overlapping neighbourhoods, aiming kappa_H(u,v)>=3
import itertools, networkx as nx
from r10_grotzsch import M, split, info
for w in (10,0):
    N=sorted(M[w]); out=0
    for Su in itertools.chain.from_iterable(itertools.combinations(N,r) for r in range(3,len(N)+1)):
        for Sv in itertools.chain.from_iterable(itertools.combinations(N,r) for r in range(3,len(N)+1)):
            if set(Su)|set(Sv)!=set(N) or Su>Sv: continue
            G=split(M,w,Su,Sv); H=G.copy(); H.remove_edge('u','v')
            if nx.node_connectivity(H,'u','v')<3: continue
            a=info(G)
            if a: print(w,Su,Sv,a); out+=1
            if out>=4: break
        if out>=4: break
