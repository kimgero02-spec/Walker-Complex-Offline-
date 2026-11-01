"""Petersen n=2 Moebius manual from the hemi-dodecahedron; essential-bridge count (P7)."""
from surf import *
import itertools
from collections import Counter

Pg = nx.petersen_graph()
cyc5 = set()
for c in nx.simple_cycles(Pg.to_directed()):
    if len(c) == 5:
        cyc5.add(frozenset(frozenset((c[t], c[(t + 1) % 5])) for t in range(5)))
cyc5 = list(cyc5)
print("5-cycles:", len(cyc5))
faces = None
for S in itertools.combinations(range(len(cyc5)), 6):
    cnt = Counter(e for s in S for e in cyc5[s])
    if len(cnt) == 15 and all(v == 2 for v in cnt.values()):
        faces = [cyc5[s] for s in S]; break
print("hemi-dodecahedron found:", faces is not None)

def rim_of(group):
    cnt = Counter(e for f in group for e in f)
    bd = [tuple(e) for e, v in cnt.items() if v == 1]
    inn = [tuple(e) for e, v in cnt.items() if v == 2]
    g = nx.Graph(bd)
    if not (nx.is_connected(g) and all(d == 2 for _, d in g.degree())):
        return None
    cyc = [x for x, _ in nx.find_cycle(g)]
    return cyc, inn

def paths_of(edges):
    g = nx.Graph(edges)
    out = []
    for comp in nx.connected_components(g):
        sg = g.subgraph(comp)
        if not nx.is_tree(sg) or max(d for _, d in sg.degree()) > 2:
            return None
        ends = [x for x, d in sg.degree() if d == 1]
        out.append(nx.shortest_path(sg, ends[0], ends[1]))
    return out

found = 0
for drop in range(1):  # by symmetry one dropped face
    rest = [f for t, f in enumerate(faces) if t != drop]
    for k in (1, 2):
        for g1 in itertools.combinations(range(5), k):
            A = [rest[t] for t in g1]; B = [rest[t] for t in range(5) if t not in g1]
            ra, rb = rim_of(A), rim_of(B)
            if ra is None or rb is None:
                continue
            shared = set(frozenset(e) for e in nx.Graph(list(zip(ra[0], ra[0][1:] + ra[0][:1]))).edges()) & \
                     set(frozenset(e) for e in nx.Graph(list(zip(rb[0], rb[0][1:] + rb[0][:1]))).edges())
            ps = paths_of([tuple(e) for e in shared])
            if ps is None or len(ps) != 2 or set(ps[0]) & set(ps[1]):
                continue
            Mn = Manual({1: ra[0], 2: rb[0]}, [(1, 2, ps[0]), (1, 2, ps[1])], {1: ra[1], 2: rb[1]})
            r = report("petersen n=2 group=%s" % (g1,), Mn)
            Bs, O, bip, each = tutte_report(Mn.G, r['_W'])
            arcs_set = [set(p) for p in ps]
            print("   iso Petersen:", nx.is_isomorphic(Mn.G, Pg), " W len", len(r['_W']),
                  " bridges(att):", [sorted(a) for a, _ in Bs])
            print("   overlap edges:", list(O.edges()), " bipartite:", bip)
            found += 1
print("manuals:", found)
