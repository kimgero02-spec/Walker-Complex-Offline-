import random, networkx as nx, time
from r4_thm2 import *
random.seed(11); t0=time.time(); found=0
for trial in range(400):
    if time.time()-t0>200: break
    n=random.choice([12,14]); G=nx.gnp_random_graph(n,random.choice([0.85,0.9]),seed=1000+trial)
    order=list(G.nodes()); random.shuffle(order)
    parts=lemma5(G,order); eta=check_lemma5(G,parts)
    c={}
    for i,(X,sd) in enumerate(parts):
        for v in X: c[v]=2*(i+1)-1+sd[v]
    Z=best_zigzag(G,c)
    if len(Z)<6: continue
    k,m,t=construct(G,parts,eta,c,Z)
    if m<=k-3:
        found+=1; print("merged-tree case: n",n,"t",t,"|M|",m,"k",k,"ok")
        if found>=2: break
print("done",time.time()-t0)
