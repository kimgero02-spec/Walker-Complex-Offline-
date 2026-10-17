import sys, time
sys.path.insert(0,'.')
from graphs import *
n, adj = lex_blowup(5, cycle(5)[1], 3)
pairs = maximal_pairs(n, adj)
print('n',n,'pairs',len(pairs),'omega',clique_number(n,adj), flush=True)
t=time.time()
o = zig_at_most(n, adj, 6, pairs)
print('zig<=6 order:', o, 'time %.1f'%(time.time()-t), flush=True)
if o: print('check runs of order', runs_of_order(n, adj, o), flush=True)
