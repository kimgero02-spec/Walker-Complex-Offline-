# R25 researcher3: search for a decisive counterexample to the "singleton-w" strengthening S*
# S*: chi(G)=k, u,v nonadjacent, forced different (chi(G/uv)=k+1)  ==>
#     G/uv has a K_{k+1} model whose branch set of the merged vertex w is {w}.
# Computation is used only to find a counterexample, not as evidence.
import itertools, networkx as nx
from networkx.generators.atlas import graph_atlas_g

def chi(G):
    n=G.number_of_nodes(); nodes=list(G)
    for k in range(1,n+1):
        col={}
        def bt(i):
            if i==n: return True
            v=nodes[i]
            for c in range(k):
                if all(col.get(x)!=c for x in G[v]):
                    col[v]=c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return k
    return 0

def identify(G,u,v):
    H=nx.relabel_nodes(G,{v:u}) if False else nx.contracted_nodes(G,u,v,self_loops=False)
    return nx.Graph(H)

def has_model(G,t,root=None):
    """K_t model; if root given, root alone is one branch set."""
    nodes=[x for x in G if x!=root]
    tt=t-1 if root is not None else t
    for assign in itertools.product(range(tt+1),repeat=len(nodes)):  # tt = unused
        B=[[nodes[i] for i in range(len(nodes)) if assign[i]==j] for j in range(tt)]
        if any(len(b)==0 for b in B): continue
        if root is None:
            # symmetry break: skip unless first nonempty ordering
            pass
        if not all(nx.is_connected(G.subgraph(b)) for b in B): continue
        ok=True
        sets=[set(b) for b in B]
        for a,b in itertools.combinations(range(tt),2):
            if not any(y in sets[b] for x in sets[a] for y in G[x]): ok=False;break
        if ok and root is not None:
            ok=all(any(y in sets[a] for y in G[root]) for a in range(tt))
        if ok: return B
    return None

found=0
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<4 or not nx.is_connected(G): continue
    k=chi(G)
    if k<3: continue
    for u,v in itertools.combinations(G,2):
        if G.has_edge(u,v): continue
        H=identify(G,u,v)
        if chi(H)!=k+1: continue
        if has_model(H,k+1,root=u) is None:
            print("COUNTEREXAMPLE S*: n",n,"k",k,"edges",sorted(G.edges()),"u,v",u,v,
                  "full model:",has_model(H,k+1))
            found+=1
            if found>=3: raise SystemExit
print("done, found",found)
