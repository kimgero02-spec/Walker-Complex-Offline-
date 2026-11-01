import sys, time
sys.path.insert(0, '.')
from graphs import *
from planar_cert import search, bad_pairs
# 정합성 점검: K3 는 R^2 에서 가능 (d_R=2), K4 는 불가능 (d_R=3)
for name, (n, adj) in [('K3', from_edges(3, [(0,1),(1,2),(0,2)])), ('K4', from_edges(4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])),
                       ('C5', cycle(5)), ('C5[K2]', lex_blowup(5, cycle(5)[1], 2)), ('compC7', complement(*cycle(7))),
                       ('Petersen', kneser(5,2)), ('C7^2', circulant(7,[1,2])), ('Grotzsch', mycielski(5, cycle(5)[1]))]:
    t = time.time()
    y, info = search(n, adj, R=3, iters=1500, restarts=6, seed=7)
    if y is not None:
        print(name, 'R^2 feasible', y, 'time %.1f' % (time.time()-t), flush=True)
    else:
        print(name, 'not found; best remaining bad pairs =', info[0], 'time %.1f' % (time.time()-t), flush=True)
