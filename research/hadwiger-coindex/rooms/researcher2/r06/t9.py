import sys, time
sys.path.insert(0,'.')
from graphs import *
from homol import *
cases = [('C5', cycle(5)), ('C6', cycle(6)), ('C5[K2]', lex_blowup(5, cycle(5)[1], 2)), ('Grotzsch', mycielski(5, cycle(5)[1]))]
for name, (n, adj) in cases:
    t = time.time()
    N = betti_gf2(neighborhood_complex(n, adj))
    print(name, 'H~(N(G);F2)', N, 'time %.1f' % (time.time()-t), flush=True)
    t = time.time()
    X = betti_gf2(box_complex_empty(n, adj))
    print(name, 'H~(X(G);F2)', X, 'time %.1f' % (time.time()-t), flush=True)
