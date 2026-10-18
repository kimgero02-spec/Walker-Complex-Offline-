"""Torus manuals (bare / outerplanar chords / 3-connected wheels) and n=2 Moebius manuals."""
from surf import *
import itertools

def torus(variant):
    oc = list(range(8))
    P = {'P0': oc}
    inner = {}
    if variant == 'chords':
        inner['P0'] = [(0, 2), (2, 4), (0, 5)]
    if variant == 'wheel':
        inner['P0'] = [('c', v) for v in oc]
    best = None
    for s1, s2 in itertools.product([0, 1], repeat=2):
        P = {'P0': oc,
             'Q1': [1, 0, 'x0', 'x1'], 'Q2': (['x0', 'x1', 4, 5] if s1 else ['x0', 'x1', 5, 4]),
             'R1': [3, 2, 'y0', 'y1'], 'R2': (['y0', 'y1', 6, 7] if s2 else ['y0', 'y1', 7, 6])}
        arcs = [('P0', 'Q1', [0, 1]), ('Q1', 'Q2', ['x0', 'x1']), ('Q2', 'P0', [4, 5]),
                ('P0', 'R1', [2, 3]), ('R1', 'R2', ['y0', 'y1']), ('R2', 'P0', [6, 7])]
        inn = dict(inner)
        if variant == 'wheel':
            for k in ('Q1', 'Q2', 'R1', 'R2'):
                inn[k] = [('h' + k, v) for v in P[k]]
        Mn = Manual(P, arcs, inn)
        if Mn.orientable():
            return Mn
    raise RuntimeError

for var in ('bare', 'chords', 'wheel'):
    r = report("torus-" + var, torus(var))
    print("   types (columns of N):", [tuple(c) for c in r['_N'].T])

# n=2 Moebius: P1 rim a b d c, P2 rim a b c d, arcs ab, cd
def n2(hub1, hub2):
    P = {1: ['a', 'b', 'd', 'c'], 2: ['a', 'b', 'c', 'd']}
    inner = {}
    if hub1: inner[1] = [('e', v) for v in P[1]]
    if hub2: inner[2] = [('f', v) for v in P[2]]
    return Manual(P, [(1, 2, ['a', 'b']), (1, 2, ['c', 'd'])], inner)

for h1, h2 in ((0, 0), (1, 0), (1, 1)):
    Mn = n2(h1, h2)
    r = report("n2 hubs=%d%d" % (h1, h2), Mn)
    Bs, O, bip, each = tutte_report(Mn.G, r['_W'])
    print("   W =", r['_W'], " bridges:", [sorted(map(str, a)) for a, _ in Bs], " overlap edges:", list(O.edges()))
