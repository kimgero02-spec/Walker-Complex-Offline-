import networkx as nx
def K5m_gadget(G, u, v, extras):
    # K5 minus edge uv on {u,v}+extras (u,v nonadjacent); extras form triangle, all joined to u,v
    a,b,c = extras
    for p,q in [(a,b),(b,c),(a,c)]: G.add_edge(p,q)
    for w in (a,b,c):
        G.add_edge(u,w); G.add_edge(v,w)
B1 = nx.Graph()
x = ['x1','x2','x3','x4']
K5m_gadget(B1, x[0], x[1], ['a1','a2','a3'])
K5m_gadget(B1, x[1], x[2], ['b1','b2','b3'])
K5m_gadget(B1, x[2], x[3], ['c1','c2','c3'])
B2 = nx.complete_graph(['y1','y2','y3','y4'])
G = nx.union(B1, B2)
for xi, yi in zip(x, ['y1','y2','y3','y4']): G.add_edge(xi, yi)
print("n", G.number_of_nodes(), "m", G.number_of_edges())
print("B1 planar", nx.check_planarity(B1)[0], "B2 planar", nx.check_planarity(B2)[0])
# matching check
cross=[(u,v) for u,v in G.edges() if (u in B1) != (v in B1)]
print("cross edges", len(cross), "matching", len({u for u,_ in cross}|{v for _,v in cross})==2*len(cross))
def colorable(G,k):
    nodes=sorted(G.nodes(), key=lambda v:-G.degree(v)); idx={v:i for i,v in enumerate(nodes)}
    col={}
    def bt(i):
        if i==len(nodes): return True
        v=nodes[i]
        for c in range(k):
            if all(col.get(u)!=c for u in G[v]):
                col[v]=c
                if bt(i+1): return True
                del col[v]
        return False
    return bt(0)
print("4-colourable:", colorable(G,4), " 5-colourable:", colorable(G,5))
