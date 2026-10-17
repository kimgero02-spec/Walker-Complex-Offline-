import sys, time
sys.path.insert(0, '.')
from graphs import *
tests = {
 'K3': from_edges(3, [(0,1),(1,2),(0,2)]),
 'C5': cycle(5), 'C7': cycle(7), 'C5[K2]': lex_blowup(5, cycle(5)[1], 2),
 'compC7': complement(*cycle(7)), 'Petersen': kneser(5,2),
 'C7^2': circulant(7,[1,2]), 'C8^2': circulant(8,[1,2]), 'C9^2': circulant(9,[1,2]),
 'Grotzsch': mycielski(5, cycle(5)[1]),
}
for name, (n, adj) in tests.items():
    t = time.time()
    z, o = zig(n, adj)
    print(name, 'n=',n, 'omega=', clique_number(n, adj), 'zig=', z, 'order=', o, 'time=%.1f'%(time.time()-t), flush=True)
