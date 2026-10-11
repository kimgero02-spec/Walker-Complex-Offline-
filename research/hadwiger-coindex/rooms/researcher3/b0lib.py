import itertools, networkx as nx
def b0_simplices(G, remove=None):
    """simplices of B_0(G) as bitmasks over 2n vertices (copy1: i, copy2: n+i). nodes relabeled 0..n-1.
    remove: optional list of vertex-pairs (u,v): drop simplices containing u^1 and v^2 (X_e subcomplex)."""
    n=G.number_of_nodes(); nodes=list(G.nodes()); idx={v:i for i,v in enumerate(nodes)}
    nb=[0]*n
    for u,v in G.edges():
        nb[idx[u]]|=1<<idx[v]; nb[idx[v]]|=1<<idx[u]
    full=(1<<n)-1
    S=[]
    for A in range(1<<n):
        common=full
        a=A
        while a:
            low=a&-a; i=low.bit_length()-1; common&=nb[i]; a^=low
        if A==0: common=full
        # B any nonempty-or-empty subset of common (B disjoint auto)
        B=common
        while True:
            if A or B:
                ok=True
                if remove:
                    for (u,v) in remove:
                        iu,iv=idx[u],idx[v]
                        if (A>>iu&1 and B>>iv&1) or (A>>iv&1 and B>>iu&1): ok=False;break
                if ok: S.append(A|(B<<n))
            if B==0: break
            B=(B-1)&common
    return S,n
def rank_gf2(rows):
    piv={}
    r=0
    for x in rows:
        while x:
            h=x.bit_length()-1
            if h in piv: x^=piv[h]
            else: piv[h]=x; r+=1; break
    return r
def reduced_betti(S):
    bydim={}
    for s in S: bydim.setdefault(bin(s).count('1')-1,[]).append(s)
    maxd=max(bydim)
    index={d:{s:i for i,s in enumerate(bydim[d])} for d in bydim}
    ranks={}
    for d in range(1,maxd+1):
        rows=[]
        for s in bydim.get(d,[]):
            x=0;t=s
            while t:
                low=t&-t; x|=1<<index[d-1][s^low]; t^=low
            rows.append(x)
        ranks[d]=rank_gf2(rows)
    # augmented: d=0 boundary to empty simplex rank 1 (if any vertices)
    ranks[0]=1; ranks[maxd+1]=0
    betti={}
    for d in range(0,maxd+1):
        betti[d]=len(bydim.get(d,[]))-ranks[d]-ranks[d+1]
    return betti
def tau_h(G, remove=None):
    """homological lower bound: tau_h = (min k with reduced H_k(B0;Z2)!=0) + 1  (= homological conn + 2)."""
    S,n=b0_simplices(G,remove)
    if not S: return 0
    b=reduced_betti(S)
    for k in sorted(b):
        if b[k]>0: return k+1
    return 99  # acyclic
if __name__=="__main__":
    for name,G in [("K2",nx.complete_graph(2)),("K3",nx.complete_graph(3)),("K4",nx.complete_graph(4)),("K5",nx.complete_graph(5)),
                   ("C5",nx.cycle_graph(5)),("C7",nx.cycle_graph(7)),("C4",nx.cycle_graph(4)),("P3",nx.path_graph(3)),("E3",nx.empty_graph(3)),("Petersen",nx.petersen_graph())]:
        S,n=b0_simplices(G); print(name,len(S),reduced_betti(S),"tau_h=",tau_h(G))
