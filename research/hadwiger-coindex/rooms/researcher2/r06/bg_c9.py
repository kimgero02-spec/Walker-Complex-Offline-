import sys, time
sys.path.insert(0,'.')
from graphs import *
from exactsep import *
n, adj = circulant(9,[1,2,3])
pairs = maximal_pairs(n, adj)
t = time.time()
for seed in range(100, 106):
    b = anneal_d(n, adj, 3, 5, 25000, seed, T0=0.8, pairs=pairs)
    print('seed', seed, 'best', b[0], 'time %.0f' % (time.time()-t), flush=True)
    if b[0] == 0:
        print('FOUND', b[1], flush=True); break
print('done', flush=True)
