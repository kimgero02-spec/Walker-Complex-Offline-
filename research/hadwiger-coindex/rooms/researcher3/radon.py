import numpy as np, networkx as nx, itertools, random
from scipy.optimize import linprog
def max_pairs(G):
    nodes=list(G.nodes()); n=len(nodes); N={v:set(G[v]) for v in nodes}
    seen=set(); out=[]
    for r in range(1,n+1):
        for A in itertools.combinations(nodes,r):
            B=set(nodes)
            for a in A: B&=N[a]
            if not B: continue
            # close A
            A2=set(nodes)
            for b in B: A2&=N[b]
            key=(frozenset(A2),frozenset(B))
            if key in seen: continue
            seen.add(key); out.append((sorted(A2),sorted(B)))
    return out
def margin(Y,A,B):
    # max t s.t. w.(a - b)... affine separation: w.y_a >= c+t, w.y_b <= c-t, |w|_inf<=1. vars w(d),c,t
    d=Y.shape[1]
    c=np.zeros(d+2);c[-1]=-1
    Aub=[];bub=[]
    for a in A: Aub.append(list(-Y[a])+[1,1]);bub.append(0)
    for b in B: Aub.append(list(Y[b])+[-1,1]);bub.append(0)
    r=linprog(c,A_ub=Aub,b_ub=bub,bounds=[(-1,1)]*d+[(None,None),(None,1)],method='highs')
    return -r.fun
def score(Y,pairs):
    return min(margin(Y,A,B) for A,B in pairs)
def search(G,d,iters=300,seed=0):
    G=nx.convert_node_labels_to_integers(G)
    pairs=max_pairs(G); n=G.number_of_nodes()
    rng=np.random.default_rng(seed)
    best=None
    for rs in range(5):
        Y=rng.normal(size=(n,d)); s=score(Y,pairs)
        step=0.5
        for it in range(iters):
            Z=Y+rng.normal(size=Y.shape)*step*(rng.random(size=(n,1))<0.4)
            sz=score(Z,pairs)
            if sz>=s: Y,s=Z,sz
            if s>1e-6: return Y,s,len(pairs)
            if it%100==99: step*=0.6
        best=max(best,(s,rs)) if best else (s,rs)
    return None,best,len(pairs)
if __name__=="__main__":
    import sys
    tests=[("K4",nx.complete_graph(4)),("C5",nx.cycle_graph(5)),("Petersen",nx.petersen_graph()),("W5",nx.wheel_graph(6))]
    for nm,G in tests:
        for d in range(1,6):
            Y,s,np_=search(G,d,iters=150)
            print(nm,"d=",d,"found" if Y is not None else "none",s if Y is None else round(s,4),np_,flush=True)
            if Y is not None: break
