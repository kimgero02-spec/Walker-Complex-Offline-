"""Rebuild researcher2's Y1 from the interim text (own code) and test my P9 (W-path classes)."""
from surf import *
C0 = ['u1','m1','w1','g1','s1','n1','t1','g2','u2','m2','w2','g3','s2','n2','t2','g4']
CQ = ['u1','m1','w1','p','u2','m2','w2','q']
CR = ['s1','n1','t1','r1','s2','n2','t2','r2']
P = {'P0': C0, 'Q': CQ, 'R': CR}
inner = {'P0': [('z', v) for v in ('u1','w1','u2','w2')],
         'Q': [('y', 'u1'), ('y', 'w1')], 'R': [('yR', 's1'), ('yR', 't1')]}
arcs = [('P0','Q',['u1','m1','w1']), ('P0','Q',['u2','m2','w2']),
        ('P0','R',['s1','n1','t1']), ('P0','R',['s2','n2','t2'])]
Mn = Manual(P, arcs, inner)
r = report("Y1", Mn)
types, N, loops, Q = wpath_types(Mn, maxlen=10)
print("arc types", [tuple(int(x) for x in c) for c in N.T])
for ty, p in sorted(types.items()):
    print("  W-path type", ty, p)
Bs, O, bip, each = tutte_report(Mn.G, r['_W'])
print("bridges", [sorted(a) for a, _ in Bs]); print("overlap", list(O.edges()))
