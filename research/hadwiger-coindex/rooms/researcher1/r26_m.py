# R26: minimal number of cross edges giving K7 minor for (W5, K3); and chi=7 threshold. Guessing aid.
import itertools, networkx as nx
from r22_check import colourable
def W5():
    G=nx.Graph()
    for i in range(5): G.add_edge(i,(i+1)%5); G.add_edge(i,5)
    return G  # vertices 0..4 rim, 5 hub
def has_K7_minor(G):
    V=list(G.nodes()); n=len(V)
    adj={v:set(G[v]) for v in V}
    # models: delete set D (|D|<=n-7), partition rest into 7 connected blocks
    def connected(S):
        S=set(S)
        if not S: return False
        st=[next(iter(S))]; seen={st[0]}
        while st:
            u=st.pop()
            for w in adj[u]:
                if w in S and w not in seen: seen.add(w); st.append(w)
        return seen==S
    def adjb(A,B): return any(b in adj[a] for a in A for b in B)
    for d in range(0,n-6):
        for D in itertools.combinations(V,d):
            R=[v for v in V if v not in D]
            # set partitions of R into exactly 7 blocks
            def parts(lst,k):
                if not lst:
                    if k==0: yield []
                    return
                if k==0: return
                first=lst[0]; rest=lst[1:]
                for p in parts(rest,k-1): yield [[first]]+p
                for p in parts(rest,k):
                    for i in range(len(p)):
                        yield p[:i]+[[first]+p[i]]+p[i+1:]
            for P in parts(R,7):
                if not all(connected(b) for b in P): continue
                if all(adjb(P[i],P[j]) for i in range(7) for j in range(i+1,7)):
                    return True,(D,P)
    return False,None
if __name__=="__main__":
    B1=W5(); B2=nx.complete_graph(3)
    # relabel K3 to 6,7,8
    B2=nx.relabel_nodes(B2,{0:6,1:7,2:8})
    cross=[(a,b) for a in range(6) for b in (6,7,8)]
    base=nx.union(B1,B2)
    best=None
    for m in range(8,19):
        found=None
        for S in itertools.combinations(cross,m):
            G=base.copy(); G.add_edges_from(S)
            ok,w=has_K7_minor(G)
            if ok: found=(S,w); break
        print("m=",m,"K7 minor found:", found is not None, found[0] if found else "")
        if found: best=m; break
    print("m* (W5,K3) =",best)
    # chi threshold
    for m in range(0,19):
        f=None
        for S in itertools.combinations(cross,m):
            G=base.copy(); G.add_edges_from(S)
            if not colourable(G,6): f=S; break
        if f is not None:
            print("min m with chi>=7:", m, f); break
