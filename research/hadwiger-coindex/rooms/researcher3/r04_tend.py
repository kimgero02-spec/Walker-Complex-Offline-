# C2: triangulation G, triangle T (face or separating): valid order with T = last three positions ?
from r04_lib import *
from r04_mid import allt
def tend(G,T):
    def extra(S,X,idx):
        for u in G:
            if u in T: continue
            for t in T: S.add_clause([X(idx[u],idx[t])])
    o,_=solve(G,extra); return bool(o)
def tend_fixed(G,T,perm):
    def extra(S,X,idx):
        for u in G:
            if u in T: continue
            for t in T: S.add_clause([X(idx[u],idx[t])])
        S.add_clause([X(idx[perm[0]],idx[perm[1]])]); S.add_clause([X(idx[perm[1]],idx[perm[2]])])
    o,_=solve(G,extra); return bool(o)
if __name__=="__main__":
    for name,G in tests():
        ts=allt(G); rng=np.random.default_rng(1)
        sel=[ts[i] for i in rng.choice(len(ts),size=min(30,len(ts)),replace=False)]+sorted(ts,key=lambda t:-sum(G.degree(x) for x in t))[:10]
        r=[tend(G,t) for t in sel]
        print(name,"T-last feasible:",sum(r),"/",len(r),flush=True)
        for t,x in zip(sel,r):
            if not x:
                # is it a face?
                nb=len(set(G[t[0]])&set(G[t[1]])&set(G[t[2]]))
                print("   FAIL",t,"degrees",[G.degree(v) for v in t],"common nbrs of T (interior/exterior sides)",nb); break
