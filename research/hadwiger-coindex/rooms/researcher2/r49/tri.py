# triangulation utilities + FB SAT (CEGAR on F-cycles), optional face pattern
import networkx as nx
from pysat.solvers import Cadical153
def faces_of(G):
    ok,emb=nx.check_planarity(G); assert ok
    seen=set(); F=[]
    for u,v in emb.edges():
        if (u,v) in seen: continue
        f=emb.traverse_face(u,v,mark_half_edges=seen); F.append(tuple(f))
    return F
def dual(G):
    F=faces_of(G); D=nx.Graph(); e2f={}
    for i,f in enumerate(F):
        for j in range(len(f)):
            e=frozenset((f[j],f[(j+1)%len(f)])); e2f.setdefault(e,[]).append(i)
    for e,l in e2f.items(): D.add_edge(*l)
    return D
def fb(G,pattern=None,extra=None):
    """pattern: dict v->'F'/'B'. returns (S=F-set) or None"""
    idx={v:i for i,v in enumerate(G)}; n=len(idx)
    t=lambda v: idx[v]+1; b=lambda v: n+idx[v]+1
    s=Cadical153()
    for u,v in G.edges():
        s.add_clause([-t(u),-t(v),b(u),b(v)]); s.add_clause([-t(u),-t(v),-b(u),-b(v)])
    for tri in [c for c in nx.enumerate_all_cliques(G) if len(c)==3]:
        s.add_clause([t(v) for v in tri])
    if pattern:
        for v,p in pattern.items(): s.add_clause([t(v)] if p=='B' else [-t(v)])
    for cl in (extra or []): s.add_clause([ (t(v) if sg else -t(v)) for v,sg in cl])
    while s.solve():
        m=set(x for x in s.get_model() if x>0)
        S=[v for v in G if t(v) not in m]
        try: cyc=nx.find_cycle(G.subgraph(S))
        except nx.NetworkXNoCycle: return S
        s.add_clause([t(u) for u,_ in cyc])
    return None
def is_fb(G,S):
    T=[v for v in G if v not in S]
    return nx.is_forest(G.subgraph(S)) and nx.is_bipartite(G.subgraph(T))
