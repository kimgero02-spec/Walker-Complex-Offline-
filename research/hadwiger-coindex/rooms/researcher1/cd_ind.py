# 표준 Kneser 표현: ground = 극대 독립집합, e_x = {I : x ∈ I}. KG(H) = G 임이 자명 (xy 가 간선 ⇔ 둘을 모두 포함하는 독립집합 없음).
import itertools, sys
from cd_check import cd_of, cycle, complement, lexicographic

def max_indep(n, adj):
    res = []
    def rec(i, cur, forb):
        # 간단한 Bron–Kerbosch 형태 대신 전수 부분집합 (n<=10)
        pass
    subs = []
    for mask in range(1, 1 << n):
        S = [v for v in range(n) if mask >> v & 1]
        if any(b in adj[a] for a, b in itertools.combinations(S, 2)):
            continue
        subs.append(frozenset(S))
    for S in subs:
        if not any(S < T for T in subs):
            res.append(S)
    return res

def rep_ind(n, adj):
    I = max_indep(n, adj)
    ground = list(range(len(I)))
    hedges = {x: frozenset(i for i, S in enumerate(I) if x in S) for x in range(n)}
    return ground, hedges

def check(n, adj, hedges):
    for x in range(n):
        for y in range(x + 1, n):
            assert (not (hedges[x] & hedges[y])) == (y in adj[x])
    return True

if __name__ == '__main__':
    tests = [
        ('K3', [set(range(3)) - {v} for v in range(3)], 3, 3),
        ('C5', cycle(5), 3, 3),
        ('C7', cycle(7), 3, 4),
        ('comp(C7)', complement(cycle(7)), 3, 4),
        ('C5[K2]', lexicographic(cycle(5), 2), 4, 5),
    ]
    for name, adj, tau, chi in tests:
        n = len(adj)
        ground, H = rep_ind(n, adj)
        check(n, adj, H)
        res = cd_of(ground, H)
        print(name, 'n=', n, '#maxindep=', len(ground), 'cd(H_ind)=', res[0], '| tau(R01)=', tau, 'chi=', chi, flush=True)
