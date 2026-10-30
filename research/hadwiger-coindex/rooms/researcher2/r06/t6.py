import sys, time
sys.path.insert(0,'.')
from graphs import *
from exactsep import *
targets = {
 'C5[K2] R3': (lex_blowup(5, cycle(5)[1], 2), 3),
 'C9^3 R3': (circulant(9,[1,2,3]), 3),
}
for name, ((n, adj), d) in targets.items():
    pairs = maximal_pairs(n, adj)
    t = time.time()
    res = []
    for seed in range(int(sys.argv[1]), int(sys.argv[2])):
        b = anneal_d(n, adj, d, 4, int(sys.argv[3]), seed, pairs=pairs)
        res.append(b[0])
        if b[0] == 0:
            print(name, 'FOUND seed', seed, b[1], flush=True); break
    print(name, 'pairs', len(pairs), 'best bad per seed', res, 'time %.0f' % (time.time()-t), flush=True)
