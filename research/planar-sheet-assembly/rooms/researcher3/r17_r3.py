# R17: r=3 examples (types c, d) and sanity checks. Used only to find examples, not as evidence.
import itertools, networkx as nx

def colorable(G, q, pre=None):
    nodes = sorted(G.nodes(), key=lambda v: -G.degree(v))
    col = dict(pre or {})
    order = [v for v in nodes if v not in col]
    def bt(i):
        if i == len(order): return True
        v = order[i]
        used = {col[u] for u in G[v] if u in col}
        for c in range(q):
            if c not in used:
                col[v] = c
                if bt(i+1): return True
                del col[v]
        return False
    return bt(0)

def chi(G):
    q = 1
    while not colorable(G, q): q += 1
    return q

def join(A, B):
    G = nx.disjoint_union(A, B)
    for a in range(len(A)):
        for b in range(len(A), len(A)+len(B)):
            G.add_edge(a, b)
    return G

# type (d): K6 = octahedron + perfect matching
octa = nx.complete_multipartite_graph(2, 2, 2)
K6 = octa.copy(); K6.add_edges_from([(0,1),(2,3),(4,5)])
print("(d) octahedron planar", nx.check_planarity(octa)[0], "chi(x)=", chi(octa), "chi(G)=", chi(K6))

# type (c) search: G 6-chromatic; pick 5 hubs forming K5: triangle T=(h1,h2,h3), edge e=(a1,a2);
# x = G - T - e must be planar with chi(x)=3.
cands = {
  "K2vW5": join(nx.complete_graph(2), nx.wheel_graph(6)),
  "K3vC5": join(nx.complete_graph(3), nx.cycle_graph(5)),
  "K1vK1vW5'": join(nx.complete_graph(1), join(nx.complete_graph(1), nx.wheel_graph(6))),
  "C5vC5": join(nx.cycle_graph(5), nx.cycle_graph(5)),
  "K2vC5vK1": join(join(nx.complete_graph(2), nx.cycle_graph(5)), nx.complete_graph(1)),
  "K1vK1vK1vC7": join(nx.complete_graph(3), nx.cycle_graph(7)),
}
for name, G in cands.items():
    found = None
    for H in itertools.combinations(G.nodes(), 5):
        if not all(G.has_edge(u, v) for u, v in itertools.combinations(H, 2)): continue
        for T in itertools.combinations(H, 3):
            a = [v for v in H if v not in T]
            x = G.copy()
            x.remove_edges_from(list(itertools.combinations(T, 2)) + [tuple(a)])
            if nx.check_planarity(x)[0] and chi(x) <= 3:
                found = (T, a); break
        if found: break
    print(name, "chi(G)=", chi(G), "type(c) planar split:", found)

# abstract (non-planar-block) sanity examples for the r=3 theorem
# (c): K6 = K_{1,2,3} + triangle + edge ; (a): K7 = K_{1,1,1,4} + K4
x = nx.complete_multipartite_graph(1, 2, 3)
print("(c) abstract: x=K123 planar?", nx.check_planarity(x)[0], "chi(x)=", chi(x))
y = nx.complete_multipartite_graph(1, 1, 1, 4)
print("(a) abstract: y=K1114 planar?", nx.check_planarity(y)[0], "chi(y)=", chi(y), "chi(K7)=", chi(nx.complete_graph(7)))
