"""R03 colouring experiments: deterministic examples for predictions (not bulk statistics)."""
import itertools, networkx as nx
from topo import report

def kneser(n, k):
    S = [frozenset(c) for c in itertools.combinations(range(n), k)]
    G = nx.Graph(); G.add_nodes_from(S)
    for a, b in itertools.combinations(S, 2):
        if not (a & b): G.add_edge(a, b)
    return G

def glue(G1, G2, pairs, keep_edges=True):
    """disjoint union with G2 vertex y identified to G1 vertex x for (x,y) in pairs."""
    m = {y: x for x, y in pairs}
    G = nx.Graph(); G.add_edges_from(G1.edges()); G.add_nodes_from(G1.nodes())
    for a, b in G2.edges():
        G.add_edge(m.get(a, ('2', a)), m.get(b, ('2', b)))
    return G

def mycielski(G):
    return nx.mycielskian(G)

def wheel(m):  # hub 'h' + rim C_m
    G = nx.cycle_graph(m); G.add_edges_from(('h', i) for i in range(m)); return G

def hajos(G1, x1, y1, G2, x2, y2):
    A = G1.copy(); A.remove_edge(x1, y1)
    B = G2.copy(); B.remove_edge(x2, y2)
    G = glue(A, B, [(x1, x2)])
    G.add_edge(y1, ('2', y2)); return G

if __name__ == '__main__':
    print("== sanity ==")
    report("KG(6,2)", kneser(6, 2), 5)
    report("Grotzsch=M(C5)", mycielski(nx.cycle_graph(5)), 5)
    report("M(K2)=C5", mycielski(nx.complete_graph(2)), 5)
    K4 = nx.complete_graph(4)
    K4e = K4.copy(); K4e.remove_edge(0, 1)          # u=0,v=1
    K2 = nx.Graph([(0, 1)])
    print("== (b) K4 = (K4-uv) U uv ==")
    report("K4-uv", K4e); report("K2", K2)
    report("glue(K4-uv, K2) at u,v", glue(K4e, K2, [(0, 0), (1, 1)]))
    print("== (a) edge 2-sums ==")
    K4b = K4.copy()
    report("K4 +_edge K4 (=K6-...)", glue(K4, K4, [(0, 0), (1, 1)]))
    C5 = nx.cycle_graph(5)
    report("C5 +_edge C5", glue(C5, C5, [(0, 0), (1, 1)]))
    report("C5 +_edge K4", glue(C5, K4, [(0, 0), (1, 1)]))
    report("Petersen +_edge K3", glue(nx.petersen_graph(), nx.complete_graph(3), [(0, 0), (1, 1)]))
    print("== pure non-edge 2-sum ==")
    P3 = nx.path_graph(3); P4 = nx.path_graph(4)
    report("P3 U P4 at ends (=C5)", glue(P3, P4, [(0, 0), (2, 3)]))
    # Moser: G1=K4-uv (u=0,v=1); G2 = (K4-uw)+wv with u=0,w=1, v new 'v'
    G2 = K4e.copy(); G2.add_edge(1, 'v')
    report("G2=(K4-uw)+wv", G2)
    M = glue(K4e, G2, [(0, 0), (1, 'v')])
    report("Moser spindle (non-edge 2-sum)", M)
    report("Hajos(K4,K4)", hajos(K4, 0, 1, K4, 0, 1))
    report("Hajos(K5,K5)", hajos(nx.complete_graph(5), 0, 1, nx.complete_graph(5), 0, 1), 6)
    print("== (c) wheels: triangles with H=C_m ==")
    for m in range(3, 9): report(f"W_{m} (hub+C{m})", wheel(m))
