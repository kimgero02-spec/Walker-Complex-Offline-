# T-block profiles: T consecutive with middle m, a<m<b; side of C(a,b)\{m}: before a / after b
from r04_lib import *
from r04_mid import allt
def profiles(G,T):
    out={}
    for m in T:
        a,b=sorted(x for x in T if x!=m)
        Cab=[c for c in set(G[a])&set(G[b]) if c!=m]
        for side in ("before","after"):
            def extra(S,X,idx):
                S.add_clause([X(idx[a],idx[m])]); S.add_clause([X(idx[m],idx[b])])
                for u in G:
                    if u not in T: S.add_clause([X(idx[u],idx[a]),X(idx[b],idx[u])])
                for c in Cab:
                    if side=="before": S.add_clause([X(idx[c],idx[a])])
                    else: S.add_clause([X(idx[b],idx[c])])
            o,_=solve(G,extra); out[(m,side)]=bool(o)
    return out
if __name__=="__main__":
    for name,G in tests():
        ts=allt(G); rng=np.random.default_rng(2)
        sel=[ts[i] for i in rng.choice(len(ts),size=min(25,len(ts)),replace=False)]+sorted(ts,key=lambda t:-sum(G.degree(x) for x in t))[:8]
        nonone=0; forced=0; none=0
        for T in sel:
            P=profiles(G,T)
            for m in T:
                s=(P[m,"before"],P[m,"after"])
                if s==(False,False): none+=1
                elif s!=(True,True):
                    forced+=1
        print(name,"triangles",len(sel),"(T,m) with no T-block order:",none,"(T,m) forcing a single side:",forced,flush=True)
