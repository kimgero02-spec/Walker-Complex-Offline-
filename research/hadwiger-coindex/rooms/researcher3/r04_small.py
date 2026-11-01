from r04_lib import *
from r04_mid import allt
from r04_tend import tend
import random
found={}
random.seed(3)
for n in range(5,13):
    hit=None
    for trial in range(300):
        G=stacked(random.randrange(10**6),n) if trial%2==0 else hubflips(stacked(random.randrange(10**6),n),40*n,trial)
        for T in allt(G):
            if not tend(G,T): hit=(G,T); break
        if hit: break
    print(n,"T-last failure found" if hit else "none in 300 trials",flush=True)
    if hit:
        G,T=hit; found[n]=hit
        ok,emb=nx.check_planarity(G)
        isface=any(set(emb.traverse_face(u,v))==set(T) for u,v in emb.edges())
        print("   T",T,"is face:",isface,"edges",sorted(G.edges()),"degs",dict(G.degree()))
        break
