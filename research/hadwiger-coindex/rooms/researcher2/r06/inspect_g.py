import sys
sys.path.insert(0,'.')
from graphs import *
from planar_cert import bad_pairs
from anneal import anneal
n, adj = mycielski(5, cycle(5)[1])
def mem(m): return [v for v in range(n) if m>>v&1]
pairs = maximal_pairs(n, adj)
for X,Y in pairs: print('X=',mem(X),'Y=',mem(Y))
b = anneal(n, adj, R=3, steps=60000, seed=0)
print('best', b)
for k in bad_pairs(n, adj, b[1], pairs):
    X,Y = pairs[k]; print('BAD X=',mem(X),'Y=',mem(Y))
