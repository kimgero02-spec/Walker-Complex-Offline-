import sys, time
sys.path.insert(0,'.')
from graphs import *
n, adj = circulant(int(sys.argv[1]), [1,2,3])
t = time.time()
pairs = maximal_pairs(n, adj)
print('C%s^3 pairs'%sys.argv[1], len(pairs), flush=True)
for T in range(4, 8):
    o = zig_at_most(n, adj, T, pairs)
    print('T', T, 'feasible' if o else 'infeasible', o, 'time %.1f'%(time.time()-t), flush=True)
    if o: break
