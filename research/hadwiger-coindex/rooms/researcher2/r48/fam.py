import networkx as nx, sys
from gadget import gadget
from cegar import cegar
def stack_all(G):
    ok,emb=nx.check_planarity(G); assert ok
    faces=set()
    for u,v in emb.edges():
        f=emb.traverse_face(u,v)
        faces.add(tuple(sorted(f)))
    H=G.copy(); n=max(G)+1
    for f in faces:
        assert len(f)==3
        for u in f: H.add_edge(n,u)
        n+=1
    return H
def k2p(k):
    G=nx.Graph(); G.add_edge(0,1)
    for i in range(k):
        G.add_edge(0,2+i); G.add_edge(1,2+i)
        if i: G.add_edge(1+i,2+i)
    return G
if __name__=="__main__":
    k=int(sys.argv[1])
    G=stack_all(k2p(k)); print(G.number_of_nodes(),nx.check_planarity(G)[0])
    for pre in [(5,6),(5,1),(1,2)]:
        print(pre, gadget(G,{0:pre[0],1:pre[1]}),flush=True)
