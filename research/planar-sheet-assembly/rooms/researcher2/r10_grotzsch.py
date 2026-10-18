# R10: split a vertex w of the Groetzsch graph (4-critical, triangle-free) into edge uv.
# Targets the strengthened candidate T4 v T6 v sep(|T|<=2); T6 = link of w non-bipartite (impossible: triangle-free).
import itertools, networkx as nx
from r10_wheel import cols
M=nx.convert_node_labels_to_integers(nx.mycielski_graph(4))
print('n',M.number_of_nodes(),'deg',dict(M.degree()), 'tri',sum(nx.triangles(M).values()))
def split(M,w,Su,Sv):
    G=M.copy(); G.remove_node(w)
    G.add_edge('u','v')
    for i in Su: G.add_edge('u',i)
    for i in Sv: G.add_edge('v',i)
    return G
def info(G):
    H=G.copy(); H.remove_edge('u','v')
    CG=cols(G)
    if not CG: return None
    CH=cols(H)
    danger=all(c['u']!=c['v'] for c in CH)
    eq={x:[p for p in H if p!=x and all(c[p]==c[x] for c in CH)] for x in ('u','v')}
    t4=any(H.has_edge(p,r) for p in eq['u']+['u'] for r in eq['v']+['v'])
    return dict(danger=danger,eq=eq,t4=t4,kG=nx.node_connectivity(G),luv=nx.node_connectivity(H,'u','v'),nCH=len(CH))
if __name__!="__main__":
    pass
seen=set() if __name__=="__main__" else {3,4,5}
for w in M:
    d=M.degree(w)
    if d in seen: continue
    seen.add(d)
    N=sorted(M[w])
    for r in range(1,len(N)):
        for Su in itertools.combinations(N,r):
            Sv=tuple(x for x in N if x not in Su)
            if Su>Sv: continue
            G=split(M,w,Su,Sv); a=info(G)
            print(w,d,Su,Sv,a)
