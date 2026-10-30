# R09 researcher3: minimum number of induced planar vertex blocks m_pl(G); bound tau <= 4*m_pl (P1 + 4CT).
import itertools, networkx as nx
def graph(name):
    G = nx.Graph()
    if name=="K5": G.add_edges_from(itertools.combinations(range(5),2))
    if name=="K6": G.add_edges_from(itertools.combinations(range(6),2))
    if name=="K33": G.add_edges_from((a,b) for a in range(3) for b in range(3,6))
    if name=="C5K2":
        for i in range(5):
            G.add_edge(2*i,2*i+1)
            j=(i+1)%5
            for a in (2*i,2*i+1):
                for b in (2*j,2*j+1): G.add_edge(a,b)
    return G
def m_pl(G):
    V=list(G.nodes()); best=None; bp=None
    for m in range(1,len(V)+1):
        for lab in itertools.product(range(m), repeat=len(V)):
            if len(set(lab))<m: continue  # use exactly m parts (nonempty)
            ok=True
            for c in range(m):
                S=[v for v,l in zip(V,lab) if l==c]
                if not nx.check_planarity(G.subgraph(S))[0]: ok=False; break
            if ok: return m, dict(zip(V,lab))
    return None
for name in ["K5","K6","K33","C5K2"]:
    G=graph(name)
    if len(G)>8:
        # restrict search to m<=3 for speed
        found=None
        for m in (2,3):
            for lab in itertools.product(range(m), repeat=len(G)):
                if len(set(lab))<m: continue
                V=list(G.nodes())
                if all(nx.check_planarity(G.subgraph([v for v,l in zip(V,lab) if l==c]))[0] for c in range(m)):
                    found=(m,lab); break
            if found: break
        print(name, "m_pl (searched m<=3):", found[0], "bound tau <=", 4*found[0])
    else:
        r=m_pl(G); print(name, "m_pl:", r[0], "bound tau <=", 4*r[0])
