"""Holonomy-sign conjecture: necklace of uniquely c-colourable cliques K_c on c consecutive vertices
of a cyclic sequence (G = C_m^{c-1}), H = C_m, interfaces = (c-1)-cliques.
holonomy = cyclic shift by m mod c of the c colours; sign = (-1)^{(c-1)*(m mod c)}."""
import sys, networkx as nx
from topo import h_index, simplices_B, chi

def L(G, dmax=5):
    G = nx.convert_node_labels_to_integers(G)
    return h_index(simplices_B(G, dmax), dmax) + 2

def power_cycle(m, r):
    G = nx.Graph()
    for i in range(m):
        for d in range(1, r + 1): G.add_edge(i, (i + d) % m)
    return G

if __name__ == "__main__":
    for c, ms in ((3, [7, 8, 9, 10, 11]), (4, [12, 13, 14])):
        for m in ms:
          s = m % c
          sign = (-1) ** ((c - 1) * s)   # a c-cycle has sign (-1)^(c-1); shift^s
          G = power_cycle(m, c - 1)
          print(f"c={c} C_{m}^{c-1}: shift={s} sign={'+' if sign > 0 else '-'} chi={chi(G)} L={L(G)} predicted L={c if sign > 0 else c + 1}")
          sys.stdout.flush()
