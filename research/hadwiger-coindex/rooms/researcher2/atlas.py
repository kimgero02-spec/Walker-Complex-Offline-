import networkx as nx, itertools, sys
from networkx.generators.atlas import graph_atlas_g
from b0 import tau_h
def chrom(G):
    V=list(G.nodes())
    for k in range(1,len(V)+1):
        col={}
        def rec(i):
            if i==len(V): return True
            for c in range(k):
                if all(col.get(u)!=c for u in G[V[i]]):
                    col[V[i]]=c
                    if rec(i+1): return True
                    del col[V[i]]
            return False
        if rec(0): return k
    return 0
def had(G):
    best=0; seen=set()
    def key(H): return nx.weisfeiler_lehman_graph_hash(H)+str(H.number_of_edges())
    stack=[nx.convert_node_labels_to_integers(G)]
    # exact: use frozenset-edge canonical via sorted edges on relabel (no iso reduction) w/ cap
    seen=set()
    while stack:
        H=stack.pop()
        k=max((len(c) for c in nx.find_cliques(H)),default=0)
        best=max(best,k)
        for u,v in list(H.edges()):
            M=nx.contracted_nodes(H,u,v,self_loops=False)
            M=nx.convert_node_labels_to_integers(M)
            kk=(M.number_of_nodes(),frozenset(map(frozenset,M.edges())))
            if kk in seen: continue
            seen.add(kk); stack.append(M)
    return best
if __name__!="__main__": raise SystemExit
bad=[]; n=0; tight=0
for G in graph_atlas_g():
    if G.number_of_nodes()==0: continue
    t,_=tau_h(G)
    c=chrom(G); n+=1
    if t is None: print("contractible?",G.edges()); continue
    if t>c: print("TAU>CHI",list(G.edges()),t,c); bad.append(G)
    if t==c: tight+=1
    # hadwiger check only on components
    h=max(had(G.subgraph(cc).copy()) for cc in nx.connected_components(G))
    if t>h: print("TAU>HAD",list(G.edges()),t,h); bad.append(G)
print("graphs",n,"tight(tau=chi)",tight,"violations",len(bad))
