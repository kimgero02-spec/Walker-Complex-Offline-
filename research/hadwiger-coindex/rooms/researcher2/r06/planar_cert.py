# R06 반례꾼: R^2 배치 y: V -> Z^2 가 모든 극대 완전이분쌍 (X,Y) 에 대해 conv y(X) ∩ conv y(Y) = ∅ 인지 정확 판정.
# 정확 판정: 분리 축 정리(SAT). 후보 축 = {perp(p-q): p,q in X∪Y} ∪ {p-q : p in X, q in Y} (정수 좌표, 정확 비교).
import random, sys
from graphs import maximal_pairs

def sep_ok(P, Q):
    """정수 점 집합 P, Q (튜플 리스트). conv P ∩ conv Q = ∅ 이면 True (정확)."""
    S = list(set(P) | set(Q))
    cands = []
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            dx, dy = S[j][0]-S[i][0], S[j][1]-S[i][1]
            if dx or dy:
                cands.append((-dy, dx)); cands.append((dy, -dx))
    for p in P:
        for q in Q:
            cands.append((p[0]-q[0], p[1]-q[1]))
    for (nx_, ny_) in cands:
        if nx_ == 0 and ny_ == 0: continue
        pv = [nx_*x + ny_*y for (x, y) in P]
        qv = [nx_*x + ny_*y for (x, y) in Q]
        if max(pv) < min(qv) or max(qv) < min(pv): return True
    return False

def bad_pairs(n, adj, y, pairs):
    bad = []
    for k, (X, Y) in enumerate(pairs):
        Xs = [y[v] for v in range(n) if X >> v & 1]
        Ys = [y[v] for v in range(n) if Y >> v & 1]
        if not sep_ok(Xs, Ys): bad.append(k)
    return bad

def search(n, adj, R=3, iters=4000, restarts=20, seed=1, verbose=False):
    """y: V -> [-R,R]^2 ∩ Z^2 hill-climb: 위반 쌍 수 최소화. 성공 시 y 반환."""
    pairs = maximal_pairs(n, adj)
    rnd = random.Random(seed)
    grid = [(a, b) for a in range(-R, R+1) for b in range(-R, R+1)]
    best_overall = None
    for r in range(restarts):
        y = [rnd.choice(grid) for _ in range(n)]
        cur = len(bad_pairs(n, adj, y, pairs))
        for it in range(iters):
            if cur == 0: return y, pairs
            v = rnd.randrange(n)
            old = y[v]
            y[v] = rnd.choice(grid)
            c = len(bad_pairs(n, adj, y, pairs))
            if c <= cur or rnd.random() < 0.02:
                cur = c
            else:
                y[v] = old
        if best_overall is None or cur < best_overall[0]:
            best_overall = (cur, list(y))
        if verbose: print('restart', r, 'remaining bad', cur, flush=True)
    return None, best_overall
