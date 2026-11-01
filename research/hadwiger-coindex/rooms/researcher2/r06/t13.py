import sys, time
sys.path.insert(0,'.')
from graphs import *
from homol import betti_gf2, neighborhood_complex
from pi1 import pi1_presentation, tietze
from t10 import complex_parts
from t12 import betti_modp
def clebsch():
    S = [1,2,4,8,15]
    E = set()
    for x in range(16):
        for s in S:
            y = x ^ s
            E.add(tuple(sorted((x,y))))
    return from_edges(16, list(E))
def mycielski_c7():
    return mycielski(7, cycle(7)[1])
which = sys.argv[1]
n, adj = {'clebsch': clebsch, 'mc7': mycielski_c7}[which]()
t = time.time()
F = neighborhood_complex(n, adj)
print(which, 'n', n, 'edges', sum(bin(a).count('1') for a in adj)//2, 'omega', clique_number(n, adj), 'H~(N;F2)', betti_gf2(F), 'H~(N;F3)', betti_modp(F,3), flush=True)
V, E, T = complex_parts(n, adj)
ng, rels = pi1_presentation(V, E, T)
alive, left = tietze(ng, rels)
print('  pi1 Tietze: gens', ng, 'alive', len(alive), 'rels left', len(left), 'time %.1f' % (time.time()-t), flush=True)
t = time.time()
z, o = zig(n, adj)
print('  zig', z, 'time %.1f' % (time.time()-t), flush=True)
