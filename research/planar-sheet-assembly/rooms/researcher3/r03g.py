"""Join additivity spot checks (predicted before running): K2+C5 -> L0=5, K1+C7^2 -> L0=4 (chi=5)."""
import networkx as nx
from topo import report
from r03f import power_cycle
def join(G1, G2):
    G = nx.disjoint_union(G1, G2); n1 = G1.number_of_nodes()
    G.add_edges_from((a, n1 + b) for a in range(n1) for b in range(G2.number_of_nodes())); return G
report("K2 + C5", join(nx.complete_graph(2), nx.cycle_graph(5)), 5)
report("K1 + C7^2", join(nx.complete_graph(1), power_cycle(7, 2)), 5)
