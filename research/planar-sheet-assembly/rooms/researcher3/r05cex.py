"""R05: counterexample to Sigma* (=>, c=3) inside the 'K3-chain union' family.
Base H = Groetzsch graph (triangle-free, ind Hom(K2,H) >= 2).  For each edge e=uv add apex x_e (triangle T_e).
At each vertex v order the H-edges e_1..e_d at v and join T_{e_i}, T_{e_{i+1}} by a fan of k triangles
v x_{e_i} y_1, v y_1 y_2, ..., v y_{k-1} x_{e_{i+1}} (k=2, or 3 if k=2 would close an odd K3-chain)."""
import itertools, sys, networkx as nx
from oddchain import odd_chain
from r05 import tri_orient, e_crit, triangles

def build(H):
    G = nx.Graph(); G.add_edges_from(H.edges())
    apex = {}
    for e in H.edges():
        e = tuple(sorted(e)); x = ("x", e); apex[e] = x
        G.add_edge(e[0], x); G.add_edge(e[1], x)
    fans = []
    cnt = itertools.count()
    for v in sorted(H.nodes()):
        es = sorted(tuple(sorted(e)) for e in H.edges(v))
        for e, f in zip(es, es[1:]):
            for k in (2, 3):
                ys = [("y", next(cnt)) for _ in range(k - 1)]
                path = [apex[e]] + ys + [apex[f]]
                newE = [(v, y) for y in ys] + list(zip(path, path[1:]))
                G.add_edges_from(newE)
                if not odd_chain(nx.convert_node_labels_to_integers(G, ordering="default"), 3):
                    fans.append((v, e, f, k)); break
                G.remove_edges_from(newE); G.remove_nodes_from(ys)
            else:
                raise RuntimeError("both parities odd")
    return G, fans

if __name__ == "__main__":
    H = nx.mycielski_graph(4)
    G, fans = build(H)
    Gi = nx.convert_node_labels_to_integers(G, ordering="default")
    print("n =", G.number_of_nodes(), "m =", G.number_of_edges(), "fans:", len(fans),
          "k=3 fans:", sum(1 for f in fans if f[3] == 3))
    T = triangles(Gi)
    # every edge in a triangle?
    tri_edges = set()
    for a, b, c in T: tri_edges |= {(a, b), (b, c), (a, c)}
    print("every edge in a triangle:", all(tuple(sorted(e)) in tri_edges for e in Gi.edges()))
    # triangle-adjacency (shared edge) connected?
    A = nx.Graph(); A.add_nodes_from(T)
    by = {}
    for Q in T:
        for e in itertools.combinations(Q, 2): by.setdefault(e, []).append(Q)
    for qs in by.values(): A.add_edges_from(itertools.combinations(qs, 2))
    print("triangles:", len(T), "edge-adjacency connected:", nx.is_connected(A))
    # pointwise connectivity: triangles at each vertex connected through shared edges
    pw = all(nx.is_connected(A.subgraph([Q for Q in T if v in Q])) for v in Gi.nodes())
    print("pointwise connected:", pw)
    print("K4 present:", any(len(q) == 4 for q in nx.enumerate_all_cliques(Gi)))
    print("odd K3-chain:", odd_chain(Gi, 3), " t exists:", tri_orient(Gi) is not None)
    print("contains Groetzsch as subgraph by construction; E(H) =", e_crit(H))
    sys.stdout.flush()
    print("E(G) (ind<=1?) =", e_crit(Gi))
