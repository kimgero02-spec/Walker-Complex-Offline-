import sys, time
sys.path.insert(0, '.')
from graphs import *
from planar_cert import search
n, adj = mycielski(5, cycle(5)[1])
print('pairs', len(maximal_pairs(n, adj)))
for seed in (11, 12):
    t = time.time()
    y, info = search(n, adj, R=6, iters=12000, restarts=8, seed=seed)
    print('seed', seed, 'feasible' if y else 'not found', (y if y else info), 'time %.1f' % (time.time()-t), flush=True)
    if y: break
