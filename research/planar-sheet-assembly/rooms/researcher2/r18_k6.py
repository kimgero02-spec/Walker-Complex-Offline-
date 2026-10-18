import networkx as nx
from r18_sum import chi, omega, report
K6=nx.complete_graph(6)
T=nx.cycle_graph(5); T.add_edges_from([(5,0),(5,2)])
Tb=nx.complement(T)
print("T triangle-free:", omega(T)==2, "Tb edges",sorted(Tb.edges()))
report("K6=T+Tbar",K6,[T,Tb])
# K4=C4uC4 manual graph M°: copies (v,k), white w_v
C1=[("00","01"),("01","11"),("11","10"),("10","00")]
C2=[("00","11"),("11","01"),("01","10"),("10","00")]
M=nx.Graph()
for k,C in ((1,C1),(2,C2)):
    M.add_edges_from([((u,k),(v,k)) for u,v in C])
for v in ["00","01","10","11"]:
    M.add_edges_from([(("w",v),(v,1)),(("w",v),(v,2))])
# suppress degree-2 white points -> cubic multigraph on 8 vertices
H=nx.Graph([e for e in M.edges() if e[0][0]!="w" and e[1][0]!="w"])
H.add_edges_from([((v,1),(v,2)) for v in ["00","01","10","11"]])
print("smoothed M°: cube?",nx.is_isomorphic(H,nx.hypercube_graph(3)),"Mobius-Wagner?",nx.is_isomorphic(H,nx.circulant_graph(8,[1,4])),"bipartite",nx.is_bipartite(H))
