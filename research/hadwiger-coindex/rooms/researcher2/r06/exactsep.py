# R06 반례꾼: 임의 차원 정확 판정. conv X ∩ conv Y ≠ ∅ <=> Σλ_x x = Σμ_y y, Σλ=Σμ=1, λ,μ≥0 가 풀림.
# Fraction 단체법 phase-1 (Bland 규칙). 정수 좌표 입력.
from fractions import Fraction as F
import random, math, sys, time
from graphs import maximal_pairs

def feasible_nonneg(A, b):
    """A x = b, x >= 0 가 풀리는가 (정확). A: list of rows (Fraction), b: list."""
    m = len(A); n = len(A[0])
    A = [list(r) for r in A]; b = list(b)
    for i in range(m):
        if b[i] < 0:
            A[i] = [-v for v in A[i]]; b[i] = -b[i]
    # tableau with artificials n..n+m-1
    T = [A[i] + [F(1) if j == i else F(0) for j in range(m)] + [b[i]] for i in range(m)]
    basis = [n+i for i in range(m)]
    N = n + m
    # objective: minimize sum of artificials => reduced costs
    cost = [F(0)]*n + [F(1)]*m
    def reduced():
        r = [F(0)]*(N+1)
        for j in range(N+1):
            s = F(0)
            for i in range(m): s += cost[basis[i]] * T[i][j]
            r[j] = (cost[j] if j < N else F(0)) - s
        return r
    while True:
        r = reduced()
        enter = None
        for j in range(N):
            if r[j] < 0 and j not in basis: enter = j; break
        if enter is None: break
        best = None; leave = None
        for i in range(m):
            if T[i][enter] > 0:
                ratio = T[i][N] / T[i][enter]
                if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                    best = ratio; leave = i
        if leave is None: return True  # 불가능한 경우는 없음(방어적)
        piv = T[leave][enter]
        T[leave] = [v / piv for v in T[leave]]
        for i in range(m):
            if i != leave and T[i][enter] != 0:
                f = T[i][enter]
                T[i] = [T[i][j] - f*T[leave][j] for j in range(N+1)]
        basis[leave] = enter
    obj = sum(T[i][N] for i in range(m) if basis[i] >= n)
    return obj == 0

def disjoint_hulls(X, Y):
    """X, Y: 정수 좌표 점 리스트 (같은 차원). conv X ∩ conv Y = ∅ 이면 True (정확)."""
    d = len(X[0])
    pts = [tuple(F(c) for c in p) for p in X] + [tuple(F(c) for c in p) for p in Y]
    nx, ny = len(X), len(Y)
    # 변수: λ (nx), μ (ny). 행: 각 좌표 Σλx - Σμy = 0 (d개), Σλ = 1, Σμ = 1
    A = []; b = []
    for k in range(d):
        A.append([pts[i][k] for i in range(nx)] + [-pts[nx+j][k] for j in range(ny)]); b.append(F(0))
    A.append([F(1)]*nx + [F(0)]*ny); b.append(F(1))
    A.append([F(0)]*nx + [F(1)]*ny); b.append(F(1))
    return not feasible_nonneg(A, b)

def bad_pairs_d(n, adj, y, pairs):
    bad = []
    for k, (X, Y) in enumerate(pairs):
        Xs = [y[v] for v in range(n) if X >> v & 1]
        Ys = [y[v] for v in range(n) if Y >> v & 1]
        if not disjoint_hulls(Xs, Ys): bad.append(k)
    return bad

def anneal_d(n, adj, dim, R, steps, seed, T0=0.6, pairs=None):
    if pairs is None: pairs = maximal_pairs(n, adj)
    rnd = random.Random(seed)
    def rp(): return tuple(rnd.randint(-R, R) for _ in range(dim))
    y = [rp() for _ in range(n)]
    cur = len(bad_pairs_d(n, adj, y, pairs)); best = (cur, list(y))
    for s in range(steps):
        if cur == 0: break
        T = T0*(1 - s/steps) + 1e-3
        v = rnd.randrange(n); old = y[v]; y[v] = rp()
        c = len(bad_pairs_d(n, adj, y, pairs))
        if c <= cur or rnd.random() < math.exp(-(c-cur)/T):
            cur = c
            if c < best[0]: best = (c, list(y))
        else:
            y[v] = old
    return best
