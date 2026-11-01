from surf import *
from ex2 import torus
Mn = torus('chords')
loops, Q, N, T = Mn.bouquet()
W, M = Mn.dual_M(); L = len(W); pos = {v: t for t, v in enumerate(W)}
epm = edge_piece_map(Mn)
arcT = {tuple(Mn.arcs[e][2]): tuple(int(x) for x in N[:, e]) for e in range(len(Mn.arcs))}
print("arc types", arcT)
for (u, v) in [(0, 2), (2, 4), (0, 5)]:
    a, b = sorted((u, v), key=lambda x: pos[x])
    t = pos[b]; back = []
    while W[t] != a:
        t = (t + 1) % L; back.append(W[t])
    cyc = [a, b] + back[:-1]
    print("chord", (u, v), "type", class_type(Mn, cyc, loops, Q, epm))
