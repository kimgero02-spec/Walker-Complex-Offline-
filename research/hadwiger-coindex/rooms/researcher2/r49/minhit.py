# For base triangulation G0: min number k of W-gadgets glued directly into faces (one per face, forbidding one edge of that face)
# killing every FB of G0.  n(G) = n0 + 7k.  (search tool for smaller counterexamples to K)
import networkx as nx, itertools
from pysat.solvers import Cadical153
from pysat.card import CardEnc
from tri import faces_of
from gstar import W
def all_fb(G):
    V=list(G); out=[]
    for bits in itertools.product([0,1],repeat=len(V)):
        F=[v for v,b in zip(V,bits) if b]; B=[v for v,b in zip(V,bits) if not b]
        H=G.subgraph(F)
        if F and H.number_of_edges()!=len(F)-nx.number_connected_components(H): continue
        if nx.is_bipartite(G.subgraph(B)): out.append(set(F))
    return out
def minhit(G0,kmax=8):
    fbs=all_fb(G0); faces=faces_of(G0)
    pairs=[(fi,frozenset(e)) for fi,f in enumerate(faces) for e in itertools.combinations(f,2)]
    var={p:i+1 for i,p in enumerate(pairs)}
    for k in range(1,kmax+1):
        s=Cadical153(); top=len(pairs)
        for fi in range(len(faces)):
            ps=[var[p] for p in pairs if p[0]==fi]
            for a,b in itertools.combinations(ps,2): s.add_clause([-a,-b])
        for F in fbs:
            s.add_clause([var[p] for p in pairs if p[1]<=F])
        enc=CardEnc.atmost(lits=list(var.values()),bound=k,top_id=top)
        for c in enc.clauses: s.add_clause(c)
        if s.solve():
            m=set(x for x in s.get_model() if x>0)
            return k,len(fbs),[(faces[p[0]],tuple(p[1])) for p in pairs if var[p] in m]
    return None,len(fbs),None
if __name__=="__main__":
    for name,G0 in [('K4',nx.complete_graph(4)),('bipyr',nx.Graph([(0,1),(1,2),(2,0)]+[(x,y) for x in 'NS' for y in range(3)])),
                    ('W',W()),('ico',nx.icosahedral_graph())]:
        k,nf,sol=minhit(G0); print(name,'n0',G0.number_of_nodes(),'#FB',nf,'min k',k,'-> n',(G0.number_of_nodes()+7*k) if k else None,sol)
