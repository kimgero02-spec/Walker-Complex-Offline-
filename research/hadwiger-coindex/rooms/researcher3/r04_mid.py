# K3-sum forcing test: for triangle T in a planar triangulation, which "middle element" of T is realisable by a pair-valid order?
from r04_lib import *
def mids(G,T):
    out=[]
    for mid in range(3):
        a,b,c=[T[(mid+1)%3],T[mid],T[(mid+2)%3]]   # b in the middle of a,c
        def extra(S,X,idx):
            # a<b<c (reflection handled by symmetry: reversal of an order keeps validity)
            S.add_clause([X(idx[a],idx[b])]); S.add_clause([X(idx[b],idx[c])])
        o,_=solve(G,extra); out.append(bool(o))
    return out
def allt(G):
    return [t for t in itertools.combinations(G.nodes(),3) if G.has_edge(t[0],t[1]) and G.has_edge(t[1],t[2]) and G.has_edge(t[0],t[2])]
if __name__=="__main__":
    bad=0; tot=0
    for name,G in tests():
        ts=allt(G); rng=np.random.default_rng(0)
        sel=[ts[i] for i in rng.choice(len(ts),size=min(25,len(ts)),replace=False)]
        # also triangles with biggest degree sum (hub triangles)
        sel+=sorted(ts,key=lambda t:-sum(G.degree(x) for x in t))[:10]
        res=[mids(G,t) for t in sel]
        forced=[(t,r) for t,r in zip(sel,res) if sum(r)<3]
        print(name,"triangles tested",len(sel),"with a non-realisable middle:",len(forced),flush=True)
        for t,r in forced[:3]: print("   ",t,r,[G.degree(x) for x in t])
