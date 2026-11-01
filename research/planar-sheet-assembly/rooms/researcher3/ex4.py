from surf import *
from ex2 import torus
import ex1  # noqa (prints)
for var in ('bare', 'chords', 'wheel'):
    Mn = torus(var)
    types, N, loops, Q = wpath_types(Mn)
    arc_types = set(tuple(int(x) for x in c) for c in N.T)
    print(var, "arc types", sorted(arc_types), " W-path types", sorted(types), " planar", planar(Mn.G))
    for ty, p in sorted(types.items()):
        print("    ", ty, p)
