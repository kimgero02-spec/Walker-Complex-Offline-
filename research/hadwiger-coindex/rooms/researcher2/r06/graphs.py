# R06 반례꾼 공용: 그래프 생성 (순수 파이썬), 극대 완전이분쌍, zig 정확 계산(순서 DFS + 가지치기)
import itertools, sys

def from_edges(n, edges):
    adj = [0]*n
    for a, b in edges:
        adj[a] |= 1 << b; adj[b] |= 1 << a
    return n, adj

def circulant(n, S):
    E = set()
    for i in range(n):
        for s in S:
            j = (i+s) % n
            if i != j: E.add(tuple(sorted((i, j))))
    return from_edges(n, list(E))

def complement(n, adj):
    full = (1<<n)-1
    return n, [((full & ~adj[i]) & ~(1<<i)) for i in range(n)]

def cycle(n): return circulant(n, [1])

def lex_blowup(n, adj, m):
    # G[K_m]: 블롭 K_m, 블롭 사이는 G 의 간선 전부
    N = n*m
    E = []
    for i in range(n):
        for s in range(m):
            for t in range(s+1, m): E.append((i*m+s, i*m+t))
            for j in range(i+1, n):
                if adj[i] >> j & 1:
                    for t in range(m): E.append((i*m+s, j*m+t))
    return from_edges(N, E)

def kneser(n, k):
    V = [frozenset(c) for c in itertools.combinations(range(n), k)]
    E = [(i, j) for i in range(len(V)) for j in range(i+1, len(V)) if not (V[i] & V[j])]
    return from_edges(len(V), E)

def mycielski(n, adj):
    # M(G): V = V ∪ V' ∪ {w}; v' ~ N(v); w ~ all v'
    E = []
    for i in range(n):
        for j in range(i+1, n):
            if adj[i] >> j & 1:
                E.append((i, j)); E.append((i, n+j)); E.append((j, n+i))
    for i in range(n): E.append((n+i, 2*n))
    return from_edges(2*n+1, E)

def maximal_pairs(n, adj):
    """극대 완전이분쌍 (A,B), A,B 비어있지 않음. A = N(B), B = N(A)."""
    full = (1<<n)-1
    def common(mask):
        r = full; k = 0
        while mask:
            if mask & 1: r &= adj[k]
            mask >>= 1; k += 1
        return r
    pairs = set()
    for A in range(1, 1<<n):
        B = common(A)
        if B == 0: continue
        A2 = common(B)
        if A2 == 0: continue
        key = (min(A2, B), max(A2, B))
        pairs.add(key)
    return sorted(pairs)

def zig_at_most(n, adj, T, pairs=None):
    """min over orders of max runs <= T ? returns an order or None (DFS with memo on states)."""
    if pairs is None: pairs = maximal_pairs(n, adj)
    P = len(pairs)
    # per vertex: list of (pair index, side) with side 0 for first set, 1 for second
    inv = [[] for _ in range(n)]
    for pi, (X, Y) in enumerate(pairs):
        for v in range(n):
            if X >> v & 1: inv[v].append((pi, 0))
            elif Y >> v & 1: inv[v].append((pi, 1))
    failed = set()
    order = []
    def dfs(placed, state):
        if placed == (1<<n)-1: return True
        key = (placed, state)
        if key in failed: return False
        for v in range(n):
            if placed >> v & 1: continue
            ok = True
            st = list(state)
            for (pi, side) in inv[v]:
                last, runs = st[pi]
                if last == -1: nl, nr = side, 1
                elif last == side: nl, nr = side, runs
                else: nl, nr = side, runs+1
                if nr > T: ok = False; break
                st[pi] = (nl, nr)
            if not ok: continue
            order.append(v)
            if dfs(placed | (1<<v), tuple(st)): return True
            order.pop()
        failed.add(key)
        return False
    init = tuple((-1, 0) for _ in range(P))
    if dfs(0, init): return list(order)
    return None

def zig(n, adj, maxT=None):
    pairs = maximal_pairs(n, adj)
    if not pairs: return 1, []
    T = 1
    while True:
        o = zig_at_most(n, adj, T, pairs)
        if o is not None: return T, o
        T += 1

def runs_of_order(n, adj, order):
    pairs = maximal_pairs(n, adj)
    pos = {v: i for i, v in enumerate(order)}
    best = 0
    for X, Y in pairs:
        seq = sorted([(pos[v], 0) for v in range(n) if X >> v & 1] + [(pos[v], 1) for v in range(n) if Y >> v & 1])
        r = 0; last = None
        for _, s in seq:
            if s != last: r += 1; last = s
        best = max(best, r)
    return best

def clique_number(n, adj):
    best = 0
    def expand(R, P):
        nonlocal best
        if P == 0:
            best = max(best, bin(R).count('1')); return
        if bin(R).count('1') + bin(P).count('1') <= best: return
        while P:
            v = (P & -P).bit_length()-1
            expand(R | (1<<v), P & adj[v])
            P &= ~(1<<v)
    expand(0, (1<<n)-1)
    return best
