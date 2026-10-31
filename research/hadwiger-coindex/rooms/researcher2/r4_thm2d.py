import random, networkx as nx
from r4_thm2 import *
random.seed(5)
G=nx.complete_graph(12)
for trial in range(5):
    order=list(G.nodes()); random.shuffle(order)
    parts=lemma5(G,order); eta=check_lemma5(G,parts)
    c={}
    for i,(X,sd) in enumerate(parts):
        for v in X: c[v]=2*(i+1)-1+sd[v]
    # zigzag: 한 부분에서 하나씩 6개, 또는 일부만 쌍으로
    reps=[sorted(X,key=lambda v:c[v]) for X,_ in parts]
    for choice in ([0,1,2,3,4,5],[0,1,2,3],[0,1,2,3,4]):
        Z=[]
        for p in choice:
            Z.append(reps[p][random.randrange(len(reps[p]))])
        Z.sort(key=lambda v:c[v])
        if len(Z)%2: Z=Z[:-1]
        if len(Z)<4: continue
        print(len(parts),"parts; Z len",len(Z), construct(G,parts,eta,c,Z))
