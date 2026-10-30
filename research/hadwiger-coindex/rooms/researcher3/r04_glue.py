# Test the Glue Lemma: two pair-valid T-block orders (same middle m, same side) merge into a pair-valid order of the K3-sum.
from r04_lib import *
from r04_mid import allt
import random
def prof_order(G,T,m,side):
    a,b=sorted(x for x in T if x!=m)
    Cab=[c for c in set(G[a])&set(G[b]) if c!=m]
    def extra(S,X,idx):
        S.add_clause([X(idx[a],idx[m])]); S.add_clause([X(idx[m],idx[b])])
        for u in G:
            if u not in T: S.add_clause([X(idx[u],idx[a]),X(idx[b],idx[u])])
        for c in Cab:
            S.add_clause([X(idx[c],idx[a])] if side=="before" else [X(idx[b],idx[c])])
    o,_=solve(G,extra); return o
def merge(o1,o2,T,m):
    a,b=sorted(x for x in T if x!=m)
    def split(o): i=o.index(a); j=o.index(b); return o[:i],o[j+1:]
    A0,A1=split(o1); B0,B1=split(o2)
    return A0+B0+[a,m,b]+A1+B1
random.seed(5); ok=bad=0
base=tests()
for trial in range(24):
    (n1,G1),(n2,G2)=random.sample(base,2)
    G1=nx.relabel_nodes(G1,{v:("x",v) for v in G1}); G2=nx.relabel_nodes(G2,{v:("y",v) for v in G2})
    T1=random.choice(allt(G1)); T2=random.choice(allt(G2))
    perm=list(T2); random.shuffle(perm)
    mp={perm[i]:T1[i] for i in range(3)}   # identify T2 with T1 under a random bijection
    G2r=nx.relabel_nodes(G2,mp)
    G=nx.compose(G1,G2r)
    m=random.choice(T1); side=random.choice(("before","after"))
    o1=prof_order(G1,T1,m,side); o2=prof_order(G2r,T1,m,side)
    om=merge(o1,o2,T1,m)
    v=nviol(G,om); ok+=(v==0); bad+=(v>0)
    print(trial,n1,n2,"|V|",G.number_of_nodes(),"viol",v,"planar?",nx.check_planarity(G)[0],flush=True)
print("glue ok",ok,"bad",bad)
