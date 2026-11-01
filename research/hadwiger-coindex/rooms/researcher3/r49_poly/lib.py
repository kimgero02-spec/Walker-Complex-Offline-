"""R49 다항식: 경계 색칠다항식 벡터와 결합 행렬 M_H (정수 x 에서 평가)."""
import itertools, networkx as nx

def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i+1:]
        yield [[first]] + p

def ff(x, k):
    r = 1
    for i in range(k): r *= (x - i)
    return r

def count_colorings(G, x, fixed=None):
    """G 의 올바른 x-색칠 수 (fixed: 정점->색 고정)."""
    fixed = fixed or {}
    for u, v in G.edges():
        if u in fixed and v in fixed and fixed[u] == fixed[v]:
            return 0
    free = [v for v in G if v not in fixed]
    free.sort(key=lambda v: -G.degree(v))
    c = dict(fixed)
    def rec(i):
        if i == len(free): return 1
        v = free[i]; s = 0
        for a in range(x):
            if all(c.get(w) != a for w in G[v]):
                c[v] = a; s += rec(i + 1); del c[v]
        return s
    return rec(0)

def atilde(B, W, pi, x):
    """블록 i 에 색 i 를 고정했을 때의 색칠 수 (x>=|pi| 일 때). x<|pi| 이면 0."""
    if x < len(pi): return 0
    fixed = {}
    for i, blk in enumerate(pi):
        for v in blk: fixed[v] = i
    return count_colorings(B, x, fixed)

def M_entry(pi, rho, H, x):
    """sum over 부분 매칭 sigma (pi-블록 i, rho-블록 j 짝, 사이에 H 간선 없음) of ff(x,|pi|+|rho|-|sigma|)."""
    bp = {v: i for i, b in enumerate(pi) for v in b}
    br = {v: j for j, b in enumerate(rho) for v in b}
    bad = set()
    for u, v in H:
        if u in bp and v in br: bad.add((bp[u], br[v]))
        elif v in bp and u in br: bad.add((bp[v], br[u]))
    p, r = len(pi), len(rho)
    # m[k] = 크기 k 매칭 수, DP over pi-블록 with bitmask of rho-블록
    from collections import defaultdict
    dp = {0: [1]}
    for i in range(p):
        nd = defaultdict(lambda: None)
        new = {}
        for mask, vec in dp.items():
            # i 를 짝짓지 않음
            new.setdefault(mask, [0]*(p+1))
            for k, c in enumerate(vec): new[mask][k] += c
            for j in range(r):
                if not (mask >> j) & 1 and (i, j) not in bad:
                    m2 = mask | (1 << j)
                    new.setdefault(m2, [0]*(p+1))
                    for k, c in enumerate(vec):
                        if c: new[m2][k+1] += c
        dp = new
    tot = 0
    for mask, vec in dp.items():
        for k, c in enumerate(vec):
            if c: tot += c * ff(x, p + r - k)
    return tot

def rank_mod(rows, p=2**61-1):
    A = [[v % p for v in row] for row in rows]
    rank = 0; ncol = len(A[0]) if A else 0
    for col in range(ncol):
        piv = None
        for i in range(rank, len(A)):
            if A[i][col]: piv = i; break
        if piv is None: continue
        A[rank], A[piv] = A[piv], A[rank]
        inv = pow(A[rank][col], p-2, p)
        A[rank] = [v*inv % p for v in A[rank]]
        for i in range(len(A)):
            if i != rank and A[i][col]:
                f = A[i][col]
                A[i] = [(a - f*b) % p for a, b in zip(A[i], A[rank])]
        rank += 1
    return rank

def bilinear(B1, W1, B2, W2, H, x, P1=None, P2=None):
    P1 = P1 or list(set_partitions(W1)); P2 = P2 or list(set_partitions(W2))
    a1 = [atilde(B1, W1, pi, x) for pi in P1]
    a2 = [atilde(B2, W2, rho, x) for rho in P2]
    s = 0
    for i, pi in enumerate(P1):
        if not a1[i]: continue
        for j, rho in enumerate(P2):
            if a2[j]: s += a1[i] * M_entry(pi, rho, H, x) * a2[j]
    return s
