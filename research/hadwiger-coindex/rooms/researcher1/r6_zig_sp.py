# R06 researcher1: zig(G) <= 3 ? for 2-trees (maximal K4-minor-free / series-parallel).
# zig(G) = min over linear orders of max run number over complete bipartite (A,B) (R04 명제 O).
# Counterexample test: a K4-minor-free G with zig >= 4 gives tau <= d_R+1 <= 3 < 4 <= zig (since d_R<=2 for K4-minor-free [R04-r2]).
# Stdlib only. Usage: python3 -I r6_zig_sp.py exhaustive n | random n count seed
import sys, random, itertools

def two_tree(n, choices):
    edges = {(0,1)}; adj = {i:set() for i in range(n)}
    adj[0].add(1); adj[1].add(0)
    elist = [(0,1)]
    for k in range(2, n):
        u, w = elist[choices[k-2] % len(elist)]
        for x in (u, w):
            adj[k].add(x); adj[x].add(k)
        elist.append((min(u,k), max(u,k))); elist.append((min(w,k), max(w,k)))
    return adj

def bicliques(n, adj):
    nb = [sum(1<<x for x in adj[i]) for i in range(n)]
    out = set()
    for A in range(1, 1<<n):
        B = (1<<n)-1
        for i in range(n):
            if A>>i & 1: B &= nb[i]
        if B == 0: continue
        out.add((A, B))
    return list(out)

def zig_le(n, bcs, limit):
    """Is there an order with all biclique run numbers <= limit ? returns order or None."""
    # bicliques by vertex-set mask
    full = [(A|B, A, B) for (A,B) in bcs]
    byv = [[] for _ in range(n)]
    for S,A,B in full:
        for v in range(n):
            if S>>v & 1: byv[v].append((S,A,B))
    order = []
    def runs_ok(placed, S, A, B):
        seq = [1 if (A>>v&1) else 2 for v in order if S>>v & 1]
        r = 1 + sum(1 for i in range(len(seq)-1) if seq[i]!=seq[i+1])
        return r <= limit
    def dfs(placed):
        if len(order) == n: return True
        for v in range(n):
            if placed>>v & 1: continue
            order.append(v)
            ok = True
            np_ = placed | (1<<v)
            for S,A,B in byv[v]:
                if S & ~np_: continue
                if not runs_ok(np_, S, A, B): ok = False; break
            if ok and dfs(np_): return True
            order.pop()
        return False
    return list(order) if dfs(0) else None

def zig_value(n, bcs):
    for L in range(1, n+1):
        if zig_le(n, bcs, L) is not None: return L

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "exhaustive":
        n = int(sys.argv[2]); cnt = 0; bad = []
        for ch in itertools.product(*[range(2*k-1) for k in range(2, n)]):
            adj = two_tree(n, list(ch))
            bcs = bicliques(n, adj)
            cnt += 1
            if zig_le(n, bcs, 3) is None: bad.append(ch)
        print(f"n={n} 2-trees (choice sequences) {cnt}: zig>=4 count {len(bad)}; first {bad[:3]}")
    else:
        n = int(sys.argv[2]); N = int(sys.argv[3]); seed = int(sys.argv[4]); random.seed(seed)
        bad = 0
        for t in range(N):
            ch = [random.randrange(10**6) for _ in range(n)]
            adj = two_tree(n, ch); bcs = bicliques(n, adj)
            if zig_le(n, bcs, 3) is None:
                bad += 1
                if bad <= 3: print("zig>=4 example", sorted((i,j) for i in adj for j in adj[i] if i<j))
        print(f"random n={n} trials {N}: zig>=4 count {bad}")
