# R25 연구원2: (**)_4 의 "어려운 경우" 최소 예 찾기 (반례/예 탐색용, 근거 아님)
import networkx as nx, itertools
from networkx.algorithms.simple_paths import all_simple_paths

def k4free(G):
    H = nx.MultiGraph(G)
    changed=True
    while changed:
        changed=False
        # merge parallel edges
        for a,b in list(H.edges()):
            if H.number_of_edges(a,b)>1:
                while H.number_of_edges(a,b)>1: H.remove_edge(a,b)
                changed=True
        for x in list(H.nodes()):
            d=H.degree(x)
            if d<=1:
                H.remove_node(x); changed=True; break
            if d==2:
                nb=[w for _,w in H.edges(x)]
                if nb[0]!=nb[1] or True:
                    H.remove_node(x)
                    if nb[0]!=nb[1]: H.add_edge(nb[0],nb[1])
                    changed=True; break
        # remove self loops
        H.remove_edges_from([e for e in nx.selfloop_edges(H)])
    return H.number_of_nodes()==0

def chi(G):
    n=G.number_of_nodes(); nodes=list(G.nodes())
    for k in range(1,n+1):
        col={}
        def bt(i):
            if i==n: return True
            x=nodes[i]
            for c in range(k):
                if all(col.get(y)!=c for y in G[x]):
                    col[x]=c
                    if bt(i+1): return True
                    del col[x]
            return False
        if bt(0): return k
def ident(G,u,v):
    return nx.contracted_nodes(G,u,v,self_loops=False)
def hard(G,u,v):
    if not k4free(G.subgraph([x for x in G if x!=u])): return False
    if not k4free(G.subgraph([x for x in G if x!=v])): return False
    for P in all_simple_paths(G,u,v):
        H=G.copy()
        for w in P[1:]:
            H=nx.contracted_nodes(H,P[0],w,self_loops=False)
        if not k4free(H): return False
    return True
if __name__=="__main__":
    found=[]
    for G in nx.graph_atlas_g():
        if G.number_of_nodes()<4 or not nx.is_connected(G): continue
        if k4free(G): continue
        if chi(G)<4: continue
        for u,v in itertools.combinations(G.nodes(),2):
            if G.has_edge(u,v): continue
            if hard(G,u,v):
                found.append((G.number_of_nodes(),G.number_of_edges(),sorted(G.edges()),u,v))
    found.sort()
    print(len(found))
    for f in found[:10]: print(f)
