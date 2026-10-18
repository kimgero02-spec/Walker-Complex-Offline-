# R11: two-piece decompositions K7 = P1 + H (P1 maximal planar, H = complement); r = |V(H)|-c(H) (nontrivial comps)
import networkx as nx, itertools
K=nx.complete_graph(7); best={}
E=list(K.edges())
for H_edges in itertools.combinations(E,6):
    P=K.copy(); P.remove_edges_from(H_edges)
    if not nx.check_planarity(P)[0]: continue
    H=nx.Graph(list(H_edges)); r=H.number_of_nodes()-nx.number_connected_components(H)
    key=r
    if key not in best: best[key]=sorted(H.degree()) 
print('achievable r for two-piece (P1 maximal planar spanning, P2 = complement):',sorted(best))
for r in sorted(best): print(r,best[r])
