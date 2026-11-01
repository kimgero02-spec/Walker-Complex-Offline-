import sys, time
sys.path.insert(0,'.')
from graphs import *
rows = []
cases = []
for n in range(7, 13):
    for k in (2, 3):
        if 2*k+1 < n: cases.append((f'C{n}^{k}', circulant(n, list(range(1, k+1)))))
cases.append(('C11(1,2,4)?', circulant(11,[1,2,4])))  # 참고용 (거리 집합 1,2,4)
for name, (n, adj) in cases:
    t = time.time()
    z, o = zig(n, adj)
    w = clique_number(n, adj)
    print(name, 'omega', w, 'zig', z, 'time %.1f' % (time.time()-t), flush=True)
