# R22: one-vertex extensions of complement(C7); keep omega<=3, zig<=3 (exact via interleaved K22), 2-sheet planar test.
import itertools, networkx as nx, sys
def base():
    G=nx.Graph(); G.add_nodes_from(range(7))
    for i in range(7):
        for j in range(i+1,7):
            if (j-i)%7 not in (1,6): G.add_edge(i,j)
    return G
def k22s(G):
    V=list(G.nodes()); res=[]
    for p,q in itertools.combinations(V,2):
        common=sorted(set(G[p])&set(G[q]))
        for a,b in itertools.combinations(common,2):
            # P={p,q}, Q={a,b}; need a,b adjacent to both p,q (true). Avoid duplicates by sorting
            P=frozenset([p,q]); Q=frozenset([a,b])
            if P&Q: continue
            res.append((P,Q))
    return list({(P,Q) if sorted(P)<sorted(Q) else (Q,P) for P,Q in res})
def has_interleave(order,P,Q):
    pos={v:i for i,v in enumerate(order)}
    seq=sorted([(pos[v],'P') for v in P]+[(pos[v],'Q') for v in Q])
    labs=[l for _,l in seq]
    runs=1+sum(1 for i in range(1,4) if labs[i]!=labs[i-1])
    return runs>=4
def zig_le3(G):
    V=list(G.nodes()); K=k22s(G)
    if not K: return True, None
    for perm in itertools.permutations(V):
        ok=True
        for P,Q in K:
            if has_interleave(perm,P,Q): ok=False; break
        if ok: return True, perm
    return False, None
def omega(G):
    return max(len(c) for c in nx.find_cliques(G))
if __name__=="__main__":
    G7=base()
    print("omega(G7)=",omega(G7))
    survivors=[]
    for r in range(0,8):
        for N in itertools.combinations(range(7),r):
            H=G7.copy(); H.add_node(7)
            for v in N: H.add_edge(7,v)
            if omega(H)>3: continue
            ok,perm=zig_le3(H)
            if ok: survivors.append((N,perm))
    print("omega<=3 and zig<=3 extensions:",len(survivors))
    for N,perm in survivors: print("N=",N,"order=",perm)
