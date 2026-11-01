import networkx as nx, time, random
from n1_lib2 import *
from n1_run4 import poset, chains
from n1_bock import *
random.seed(11); t=time.time(); cnt=0; z4=0; hits=0
from collections import Counter
C=Counter()
while time.time()-t<240:
    n=random.choice([8,9,10]); p=random.choice([.25,.3,.4,.5,.6])
    G=nx.gnp_random_graph(n,p,seed=random.randrange(10**9))
    if not nx.is_connected(G): continue
    pairs=maxbic(G)
    if not zigle(n,pairs,3):   # zig>=4
        P=poset(pairs); ch=chains(P)
        b=bockstein_zero(P,ch)
        C[b]+=1
        if b: hits+=1; print("HIT",n,sorted(G.edges()),flush=True)
    cnt+=1
print(cnt,C)
