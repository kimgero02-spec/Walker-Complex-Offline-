import itertools, sys
sys.path.insert(0, '.')
from r6_zig_sp import bicliques, zig_value
def graph(n, E):
    adj={i:set() for i in range(n)}
    for a,b in E: adj[a].add(b); adj[b].add(a)
    return adj
def cyc(n): return [(i,(i+1)%n) for i in range(n)]
def blowup(adj, n, m):
    # G[K_m]: vertices (v,s) index v*m+s
    E=set()
    N=n*m
    for v in range(n):
        for s in range(m):
            for t in range(m):
                if s<t: E.add((v*m+s, v*m+t))
    for u in range(n):
        for v in adj[u]:
            if u<v:
                for s in range(m):
                    for t in range(m): E.add((u*m+s, v*m+t))
    return N, graph(N, E)
tests = {}
tests['K4'] = (4, graph(4, list(itertools.combinations(range(4),2))))
tests['K5'] = (5, graph(5, list(itertools.combinations(range(5),2))))
tests['C5'] = (5, graph(5, cyc(5)))
c7b = [(i,j) for i,j in itertools.combinations(range(7),2) if min((j-i)%7,(i-j)%7) in (2,3)]
tests['C7bar'] = (7, graph(7, c7b))
tests['W5'] = (6, graph(6, cyc(5)+[(5,i) for i in range(5)]))
n,a = graph(5, cyc(5)) and (5, graph(5, cyc(5)))
N,b = blowup(graph(5, cyc(5)), 5, 2)
tests['C5[K2]'] = (N, b)
for k,(n,adj) in tests.items():
    E=[(i,j) for i in adj for j in adj[i] if i<j]
    print(k, 'zig =', zig_value(n, bicliques(n, adj)))
