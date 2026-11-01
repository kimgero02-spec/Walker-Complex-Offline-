import time, random, networkx as nx
from n1_lib2 import *
random.seed(5)
t=time.time(); stats={}
worst=[]
for it in range(400):
    n=random.choice([8,9]); p=random.choice([.3,.4,.5,.6])
    G=nx.gnp_random_graph(n,p,seed=random.randrange(10**9))
    if G.number_of_edges()==0: continue
    pairs=maxbic(G)
    l=chainlen(pairs)
    z=zig(n,pairs)
    d=l+1-z
    stats[d]=stats.get(d,0)+1
    if d<0: print("BAD",sorted(G.edges()),l,z,flush=True)
    if time.time()-t>200: break
print(stats,it)
