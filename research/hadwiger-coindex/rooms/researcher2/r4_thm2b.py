import random, networkx as nx, itertools
from r4_thm2 import *
random.seed(7)
seen=set()
for trial in range(60):
    n=random.choice([9,10,11]); G=nx.gnp_random_graph(n,0.75,seed=trial)
    order=list(G.nodes()); random.shuffle(order)
    parts=lemma5(G,order); eta=check_lemma5(G,parts)
    c={}
    for i,(X,sd) in enumerate(parts):
        for v in X: c[v]=2*(i+1)-1+sd[v]
    Z=best_zigzag(G,c)
    if len(Z)<4: continue
    k,m,t=construct(G,parts,eta,c,Z)
    key=(t,m)
    if key not in seen:
        seen.add(key); print("n",n,"zigzag",len(Z),"t",t,"|M|",m,"k",k,"ok")
