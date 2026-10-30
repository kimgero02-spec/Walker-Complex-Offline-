import networkx as nx, itertools
def k4free(G):
    G=nx.Graph(G); G.remove_edges_from(nx.selfloop_edges(G))
    ch=True
    while ch:
        ch=False
        for v in list(G):
            d=G.degree(v)
            if d<=1: G.remove_node(v); ch=True; break
            if d==2:
                a,b=list(G[v]); G.remove_node(v); G.add_edge(a,b); ch=True; break
    return G.number_of_nodes()==0
def ident(G,u,v):
    H=nx.contracted_nodes(G,u,v,self_loops=False); return nx.Graph(H)
found=0
for n in range(5,8):
  for G in nx.graph_atlas_g():
    if G.number_of_nodes()!=n or not nx.is_connected(G): continue
    if k4free(G): continue
    for u,v in itertools.combinations(G,2):
        if G.has_edge(u,v): continue
        if k4free(ident(G,u,v)):
            print(n,sorted(G.edges()),u,v); found+=1; break
    if found>3: break
  if found>3: break
print('found',found)
