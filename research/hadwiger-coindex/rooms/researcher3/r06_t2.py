# Test 2: zig under removal of a dominated vertex a (N(a) ⊊ N(c) for some c != a)
import sys; sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3')
from r06_lib import *
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
def delete(n, E, a):
    m = {v:(v if v<a else v-1) for v in range(n) if v!=a}
    return n-1, [(m[u],m[v]) for u,v in E if a not in (u,v)]
def dominated(n, E):
    adj = make(n,E); out=[]
    for a in range(n):
        for c in range(n):
            if c!=a and adj[a] and (adj[a] & ~adj[c]) == 0:
                out.append((a,c)); break
    return out
G = {
 "K4":(4, list(itertools.combinations(range(4),2))),
 "C5+pendant":(6, cyc(5)+[(0,5)]),
 "P4":(4,[(0,1),(1,2),(2,3)]),
 "C5+twin(false)":(6, cyc(5)+[(5,1),(5,4)]),
 "C5+pend-on-1-and-2?":(6, cyc(5)+[(0,5),(1,5)]),
 "C7+pendant":(8, cyc(7)+[(0,7)]),
 "K_{1,3}+edge":(5, [(0,1),(0,2),(0,3),(1,4)]),
 "Petersen-minus-v (dominated?)":None,
}
for name,val in G.items():
    if val is None: continue
    n,E = val
    adj = make(n,E)
    z = zig(adj,n)
    dom = dominated(n,E)
    line = f"{name}: n={n} zig={z} dominated pairs (a,c)={dom}"
    for a,c in dom[:3]:
        n2,E2 = delete(n,E,a)
        z2 = zig(make(n2,E2),n2)
        line += f" | zig(G-{a})={z2}"
    print(line, flush=True)
