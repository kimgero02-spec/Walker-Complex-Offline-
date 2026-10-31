# (3,2)-defective colourings (each class induces max degree <=2), class-monotone orders: does a pair-valid order exist inside the classes?
from r04_lib import *
from pysat.solvers import Cadical153
import random
def defcol(G,k,dmax,seed):
    nodes=list(G.nodes()); cnt=[0]
    def new(): cnt[0]+=1; return cnt[0]
    col={(v,i):new() for v in nodes for i in range(k)}
    S=Cadical153()
    for v in nodes:
        S.add_clause([col[v,i] for i in range(k)])
        for i in range(k):
            for j in range(i+1,k): S.add_clause([-col[v,i],-col[v,j]])
    # defect: any dmax+1 neighbours of v in same class with v is forbidden
    for v in nodes:
        for T in itertools.combinations(list(G[v]),dmax+1):
            for i in range(k): S.add_clause([-col[v,i]]+[-col[u,i] for u in T])
    rng=random.Random(seed)
    S.set_phases([rng.choice((1,-1))*col[v,i] for v in nodes for i in range(k)])
    if not S.solve(): return None
    m=set(l for l in S.get_model() if l>0)
    return {v:[i for i in range(k) if col[v,i] in m][0] for v in nodes}
def solve_classes(G,c,perm):
    rank={cl:i for i,cl in enumerate(perm)}
    def extra(S,X,idx):
        for u in G:
            for v in G:
                if rank[c[u]]<rank[c[v]]: S.add_clause([X(idx[u],idx[v])])
    return solve(G,extra)
if __name__=="__main__":
    for name,G in tests():
        res=[]
        for seed in range(4):
            c=defcol(G,3,2,seed)
            if c is None: res.append("nocol"); continue
            best=any(solve_classes(G,c,p)[0] for p in itertools.permutations(range(3)))
            res.append(best)
        print(name,"(3,2)-defective colouring + class-monotone pair-valid order exists:",res,flush=True)
