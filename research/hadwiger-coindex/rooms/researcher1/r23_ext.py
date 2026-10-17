import itertools, pickle, networkx as nx
from r22_ext import zig_le3, omega
from r22_check import colourable, two_sheet_planar
gaps=pickle.load(open('r23_gaps7.pkl','rb'))
out=[]
for gi,G in enumerate(gaps):
    V=list(G.nodes())
    # planarity of H-v for each v (6-vertex subgraphs)
    pv=[v for v in V if nx.check_planarity(G.subgraph([u for u in V if u!=v]))[0]]
    print("gap",gi,"H-v planar for v in",pv, "H itself planar:", nx.check_planarity(G)[0])
    reps=[]
    for r in range(0,8):
        for N in itertools.combinations(V,r):
            H=G.copy(); H.add_node(7)
            for v in N: H.add_edge(7,v)
            if omega(H)>3: continue
            if not colourable(H,4): continue
            ok,_=zig_le3(H)
            if not ok: continue
            if any(nx.is_isomorphic(H,R) for _,R in reps): continue
            reps.append((N,H))
    print("  8-vertex gap extensions (iso classes):",len(reps))
    for N,H in reps:
        part=two_sheet_planar(H)
        print("   N=",N,"edges",H.number_of_edges(),"2-sheet planar:",part is not None, "| H-x planar for x in", [v for v in H.nodes() if nx.check_planarity(H.subgraph([u for u in H.nodes() if u!=v]))[0]])
        if part is None: out.append((gi,N,H))
print("OBSTRUCTION CANDIDATES:",[(g,N) for g,N,_ in out])
pickle.dump(out,open('r23_obs.pkl','wb'))
