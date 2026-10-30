# R06 researcher1: implementation check of the insertion proof (zig<=3 for 2-trees).
# Build 2-tree by attaching v to edge xy. Place v just before the right endpoint (Z'_xy inside (x,y)) or just after it (outside).
# Check: runs<=3 for every biclique (A,B) of the final graph, under the constructed order (implementation check only).
import random, sys
sys.path.insert(0, "/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher1")
from r6_zig_sp import bicliques
def build(n, rnd):
    adj = {0:{1},1:{0}}; edges=[(0,1)]; parent = {}
    for v in range(2, n):
        x,y = rnd.choice(edges)
        adj[v] = {x,y}; adj[x].add(v); adj[y].add(v)
        edges += [(x,v),(y,v)]; parent[v]=(x,y)
    return adj, parent
def order_insert(n, adj, parent):
    order = [0,1]  # sequence of vertices, insertion below
    def pos(v): return order.index(v)
    for v in range(2,n):
        x,y = parent[v]
        Z = [z for z in adj[x]&adj[y] if z != v and z < v]   # common nbrs of x,y present before v
        if not Z:
            # no constraint: put right after the right endpoint
            i = max(pos(x),pos(y)); order.insert(i+1, v); continue
        px, py = pos(x), pos(y)
        lo, hi = min(px,py), max(px,py)
        inside = all(lo < pos(z) < hi for z in Z)
        assert inside or all(not (lo < pos(z) < hi) for z in Z), "invariant broken"
        if inside:
            order.insert(hi, v)            # just before right endpoint (position hi), strictly inside
        else:
            order.insert(hi+1, v)          # just after right endpoint, outside
    return order
def max_runs(n, adj, order):
    rank = {v:i for i,v in enumerate(order)}
    worst = 0
    for A,B in bicliques(n, adj):
        S = sorted([v for v in range(n) if (A|B)>>v & 1], key=lambda v: rank[v])
        seq = [1 if A>>v&1 else 2 for v in S]
        r = 1 + sum(1 for i in range(len(seq)-1) if seq[i]!=seq[i+1])
        worst = max(worst, r)
    return worst
rnd = random.Random(int(sys.argv[1])); worst_all = 0
for t in range(int(sys.argv[2])):
    n = rnd.randrange(3, 13)
    adj, parent = build(n, rnd)
    order = order_insert(n, adj, parent)
    worst_all = max(worst_all, max_runs(n, adj, order))
print("implementation check: max runs over tested 2-trees =", worst_all)
