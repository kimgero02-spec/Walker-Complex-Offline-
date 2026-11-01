import itertools, networkx as nx
from r22_ext import base, zig_le3, omega
def colourable(G,k):
    V=sorted(G.nodes(), key=lambda v:-G.degree(v)); col={}
    def bt(i):
        if i==len(V): return True
        v=V[i]; used={col[u] for u in G[v] if u in col}
        for c in range(k):
            if c not in used:
                col[v]=c
                if bt(i+1): return True
                del col[v]
        return False
    return bt(0)
def two_sheet_planar(G):
    V=list(G.nodes()); n=len(V)
    for mask in range(2**(n-1)):
        A=[V[i] for i in range(n) if (mask>>i)&1]
        B=[v for v in V if v not in A]
        if nx.check_planarity(G.subgraph(A))[0] and nx.check_planarity(G.subgraph(B))[0]:
            return (A,B)
    return None
G7=base()
reps=[]
cands=[]
for r in range(0,8):
    for N in itertools.combinations(range(7),r):
        H=G7.copy(); H.add_node(7)
        for v in N: H.add_edge(7,v)
        if omega(H)>3: continue
        ok,_=zig_le3(H)
        if ok: cands.append((N,H))
print("candidates",len(cands))
for N,H in cands:
    if any(nx.is_isomorphic(H,R) for _,R in reps): continue
    reps.append((N,H))
print("isomorphism classes:",len(reps))
for N,H in reps:
    c4=colourable(H,4)
    part=two_sheet_planar(H) if c4 else None
    print("N=",N,"deg",H.degree(7),"edges",H.number_of_edges(),"4-col",c4,"2-sheet planar partition:",part is not None, part)
