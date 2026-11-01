"""R05 (researcher3): c=3 case of Sigma* (=>).
Exact criterion E (proved in report):  ind Hom(K2,G) <= 1  <=>  exists a : oriented edges -> odd integers,
antisymmetric, with sum of a around every 4-cycle (K_{2,2}) equal to 0.
Tools: e_crit(G), tri_orient(G) (orientation making every triangle a directed 3-cycle; exists iff no odd K3-chain),
obstruction o on 4-cycles for a = t."""
import itertools, sys, networkx as nx
from zlift import int_kernel, in_span_f2, ind_le_1
from oddchain import odd_chain

def four_cycles(G):
    """each 4-cycle once, as tuple (u,v,u2,v2) meaning u-v-u2-v2-u"""
    out = set()
    for u, u2 in itertools.combinations(G.nodes(), 2):
        cn = sorted(set(G[u]) & set(G[u2]))
        for v, v2 in itertools.combinations(cn, 2):
            cyc = (u, v, u2, v2)
            # canonical: rotations/reflections
            rots = [cyc[i:] + cyc[:i] for i in range(4)]
            rots += [tuple(reversed(r)) for r in rots]
            out.add(min(rots))
    return sorted(out)

def e_crit(G):
    G = nx.convert_node_labels_to_integers(G)
    E = sorted(tuple(sorted(e)) for e in G.edges()); ei = {e: i for i, e in enumerate(E)}
    rows = []
    for q in four_cycles(G):
        r = [0] * len(E)
        for i in range(4):
            x, y = q[i], q[(i + 1) % 4]
            r[ei[tuple(sorted((x, y)))]] += 1 if x < y else -1
        rows.append(r)
    if not rows: return True
    K = int_kernel(rows, len(E))
    return in_span_f2(K, (1 << len(E)) - 1)

def triangles(G):
    return [tuple(sorted(q)) for q in nx.enumerate_all_cliques(G) if len(q) == 3]

def tri_orient(G):
    """2-SAT-free version: unknown x_e in Z2 (1 = edge oriented small->large), triangle (a<b<c) cyclic iff
    orientation a->b->c->a  (x_ab=1,x_bc=1,x_ca: c->a means x_ac=0)  or reverse. Encode s_Q in Z2:
    x_ab = s, x_bc = s, x_ac = 1+s.  Solve by BFS on the bipartite incidence graph. Returns dict or None."""
    val = {}; T = triangles(G)
    inc = {}
    for Q in T:
        a, b, c = Q
        for e, off in (((a, b), 0), ((b, c), 0), ((a, c), 1)):
            inc.setdefault(e, []).append((Q, off))
    sQ = {}
    for Q0 in T:
        if Q0 in sQ: continue
        sQ[Q0] = 0; st = [Q0]
        while st:
            Q = st.pop(); a, b, c = Q
            for e, off in (((a, b), 0), ((b, c), 0), ((a, c), 1)):
                xe = sQ[Q] ^ off
                if e in val and val[e] != xe: return None
                val[e] = xe
                for R, off2 in inc[e]:
                    need = xe ^ off2
                    if R in sQ:
                        if sQ[R] != need: return None
                    else:
                        sQ[R] = need; st.append(R)
    return val

def obstruction(G, t):
    """o(Q) = (sum of +-1 of a=t around Q)/2 for 4-cycles whose edges are all oriented by t"""
    res = []
    for q in four_cycles(G):
        s = 0; ok = True
        for i in range(4):
            x, y = q[i], q[(i + 1) % 4]; e = tuple(sorted((x, y)))
            if e not in t: ok = False; break
            fwd = (t[e] == 1) == (x < y)
            s += 1 if fwd else -1
        chord = G.has_edge(q[0], q[2]) or G.has_edge(q[1], q[3])
        res.append((q, s // 2 if ok else None, chord))
    return res

if __name__ == "__main__":
    from r04 import chain
    tests = [("K3", nx.complete_graph(3)), ("K4", nx.complete_graph(4)), ("C5", nx.cycle_graph(5)),
             ("W4", nx.wheel_graph(5)), ("W5", nx.wheel_graph(6)), ("Grotzsch", nx.mycielski_graph(4)),
             ("C5(M)", nx.mycielski_graph(3))]
    for m in range(6, 13):
        tests.append((f"C_{m}^2", chain(m, [3] * m)[0]))
    for name, G in tests:
        G = nx.convert_node_labels_to_integers(G)
        t = tri_orient(G)
        oc = odd_chain(G, 3)
        print(name, "E:", e_crit(G), "zlift:", ind_le_1(G), "oddchain:", oc, "t exists:", t is not None)
        assert (t is None) == oc
        if t is not None:
            bad = [(q, o, ch) for q, o, ch in obstruction(G, t) if o not in (0, None)]
            print("   nonzero o under t:", bad[:6], "any chordal:", any(ch for _, _, ch in bad))
        sys.stdout.flush()
