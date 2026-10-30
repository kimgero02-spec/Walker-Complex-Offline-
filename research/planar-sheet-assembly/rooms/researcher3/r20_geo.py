# geodesic triangulations (icosahedron, frequency 1 or 2) -> dual cubic fullerene-like graphs
import networkx as nx
def faces_of(T):
    ok,emb=nx.check_planarity(T); seen=set(); F=[]
    for u,v in emb.edges():
        if (u,v) in seen: continue
        F.append(tuple(emb.traverse_face(u,v,mark_half_edges=seen)))
    return F
def geodesic2():
    I=nx.icosahedral_graph(); F=faces_of(I); G=nx.Graph(I.edges())
    mid={}
    for u,v in list(I.edges()):
        m=('m',min(u,v),max(u,v)); mid[frozenset((u,v))]=m
        G.remove_edge(u,v); G.add_edge(u,m); G.add_edge(m,v)
    for a,b,c in F:
        x,y,z=mid[frozenset((a,b))],mid[frozenset((b,c))],mid[frozenset((c,a))]
        G.add_edges_from([(x,y),(y,z),(z,x)])
    return nx.convert_node_labels_to_integers(G)
