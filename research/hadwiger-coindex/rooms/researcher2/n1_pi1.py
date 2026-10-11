import sys, itertools, networkx as nx
from b0 import simplices
from n1_homZ import circ
def simply_connected(G):
    S,n=simplices(G)
    def verts(A,B): return tuple([i for i in range(n) if A>>i&1]+[n+i for i in range(n) if B>>i&1])
    F=[verts(A,B) for A,B in S]
    edges=set();tris=set()
    for f in F:
        if len(f)>=2:
            for e in itertools.combinations(f,2): edges.add(e)
        if len(f)>=3:
            for t in itertools.combinations(f,3): tris.add(t)
    H=nx.Graph(); H.add_edges_from(edges)
    if not nx.is_connected(H): return False,'disconnected'
    T=nx.minimum_spanning_tree(H)
    triv=set(tuple(sorted(e)) for e in T.edges())
    tl=list(tris)
    ch=True
    while ch:
        ch=False
        for (a,b,c) in tl:
            es=[(a,b),(a,c),(b,c)]
            k=[e in triv for e in es]
            if sum(k)==2:
                for e,kk in zip(es,k):
                    if not kk: triv.add(e)
                ch=True
    return len(triv)==len(edges),(len(triv),len(edges))
if __name__=="__main__":
    n=int(sys.argv[1]); ks=tuple(int(x) for x in sys.argv[2].split(','))
    print(n,ks,simply_connected(circ(n,ks)))
