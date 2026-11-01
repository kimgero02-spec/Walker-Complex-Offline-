"""(a) witness odd triangle chain in the K4-free counterexample to R03 conj. 5.3;
   (b) wheel family table (pieces uniquely c-colourable cliques around a hub)."""
import itertools, sys, networkx as nx
from r04 import chain, holonomy, sign, L_h
from oddchain import perm_sign
from zlift import ind_le_1
from topo import chi

def odd_witness(G, c):
    cl = [tuple(sorted(q)) for q in nx.enumerate_all_cliques(G) if len(q) == c]
    by_face = {}
    for q in cl:
        for f in itertools.combinations(q, c - 1): by_face.setdefault(f, []).append(q)
    adj = {q: [] for q in cl}
    for f, qs in by_face.items():
        for q1, q2 in itertools.combinations(qs, 2):
            col = {v: i for i, v in enumerate(q1)}
            new2 = [v for v in q2 if v not in f][0]; old1 = [v for v in q1 if v not in f][0]
            col2 = {v: col[v] for v in f}; col2[new2] = col[old1]
            s = perm_sign([col2[v] for v in q2]); adj[q1].append((q2, s)); adj[q2].append((q1, s))
    lab = {}; par = {}
    for q0 in cl:
        if q0 in lab: continue
        lab[q0] = 1; par[q0] = None; queue = [q0]
        for q in queue:
            for r, s in adj[q]:
                if r not in lab: lab[r] = lab[q] * s; par[r] = q; queue.append(r)
                elif lab[r] != lab[q] * s:
                    def path(x):
                        p = []
                        while x is not None: p.append(x); x = par[x]
                        return p
                    a, b = path(q), path(r)
                    sa = set(a); lca = next(x for x in b if x in sa)
                    return a[:a.index(lca) + 1][::-1][::-1] , b[:b.index(lca)]
    return None

ell = [2, 2, 3, 5, 2, 2, 3, 5]; m = 8
G, T, c = chain(m, ell); g = holonomy(m, ell, T, c)
print("pieces T_i:", [sorted(t) for t in T])
print("edges:", sorted(G.edges()))
print("H-cycle holonomy", g, "sign", sign(g), "chi", chi(G), "omega", max(len(q) for q in nx.find_cliques(G)), "L_h", L_h(G, 4), "ind<=1", ind_le_1(G))
w = odd_witness(G, 3)
a, b = w
cyc = a[::-1] + b[::-1]
print("odd closed triangle chain:", [list(x) for x in (a + b[::-1])])
# wheel-type family
def join(G1, G2):
    H = nx.disjoint_union(G1, G2); n1 = G1.number_of_nodes()
    H.add_edges_from((x, n1 + y) for x in range(n1) for y in range(G2.number_of_nodes())); return H
from r03f import power_cycle
fam = []
for k in range(4, 10): fam.append((f"W_{k} = K1+C_{k}", join(nx.complete_graph(1), nx.cycle_graph(k)), 3))
for k in (4, 5, 6, 7): fam.append((f"K2+C_{k}", join(nx.complete_graph(2), nx.cycle_graph(k)), 4))
for k in (7, 8, 9, 10): fam.append((f"K1+C_{k}^2", join(nx.complete_graph(1), power_cycle(k, 2)), 4))
from oddchain import odd_chain
for name, H, cc in fam:
    print(f"{name:16s} c={cc} chi={chi(H)} oddchain={odd_chain(H, cc)} L_h={L_h(H, cc+1)}"); sys.stdout.flush()
