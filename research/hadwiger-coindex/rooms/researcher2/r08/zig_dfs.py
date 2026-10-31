# Feasibility of zig(G) <= r by DFS over prefixes.
# Runs of restriction to a prefix never exceed runs of the full restriction (prefix monotonicity),
# so prune as soon as some biclique exceeds r runs.
import sys, itertools

def bicliques(n, adj):
    bics = []
    for la in range(1, 1 << n):
        A = [i for i in range(n) if la >> i & 1]
        common = [j for j in range(n) if not (la >> j & 1) and all(adj[a][j] for a in A)]
        for lb in range(1, 1 << len(common)):
            B = [common[k] for k in range(len(common)) if lb >> k & 1]
            # keep only maximal bicliques (runs is monotone under insertion, so this suffices)
            bics.append((frozenset(A), frozenset(B)))
    # maximality filter
    keep = []
    sets = [(A, B) for A, B in bics]
    for A, B in sets:
        maximal = True
        for A2, B2 in sets:
            if (A2, B2) != (A, B) and A <= A2 and B <= B2:
                maximal = False; break
        if maximal:
            keep.append((A, B))
    return keep

def feasible(n, adj, r):
    bics = bicliques(n, adj)
    # Only maximal bicliques are needed: runs under insertion is non-decreasing.
    order = []
    used = [False]*n
    def runs_ok():
        pos = {v: i for i, v in enumerate(order)}
        for A, B in bics:
            seq = sorted([(pos[v], 0) for v in A if v in pos] + [(pos[v], 1) for v in B if v in pos])
            cnt = 0; prev = None
            for _, c in seq:
                if c != prev:
                    cnt += 1; prev = c
            if cnt > r:
                return False
        return True
    def dfs():
        if len(order) == n:
            return True
        for v in range(n):
            if not used[v]:
                used[v] = True; order.append(v)
                if runs_ok() and dfs():
                    return True
                order.pop(); used[v] = False
        return False
    ok = dfs()
    return ok, list(order) if ok else None

def zig_value(n, edges, lo=1):
    adj = [[False]*n for _ in range(n)]
    for i, j in edges:
        adj[i][j] = adj[j][i] = True
    r = lo
    while True:
        ok, order = feasible(n, adj, r)
        if ok:
            return r, order
        r += 1

if __name__ == "__main__":
    # C_5[K_2]: vertices (i, s), i in Z_5, s in {0,1}; index 2*i+s
    n = 10
    E = []
    for i in range(5):
        for j in range(5):
            if (j - i) % 5 in (1, 4):
                for s in range(2):
                    for t in range(2):
                        E.append((2*i+s, 2*j+t))
    E = [(min(a,b), max(a,b)) for a, b in E]
    E = sorted(set(E))
    print("edges:", len(E))
    print("zig(C5[K2]) <= 4 ?", feasible(n, [[ (min(i,j),max(i,j)) in set(E) and i!=j for j in range(n)] for i in range(n)], 4))
    print("zig(C5[K2]) <= 5 ?", feasible(n, [[ (min(i,j),max(i,j)) in set(E) and i!=j for j in range(n)] for i in range(n)], 5)[0])
    print("zig(C5) =", zig_value(5, [(i,(i+1)%5) for i in range(5)]))
    print("zig(K5)=", zig_value(5, [(i,j) for i in range(5) for j in range(i+1,5)]))
    print("zig(K6)=", zig_value(6, [(i,j) for i in range(6) for j in range(i+1,6)]))
