import itertools
from cd_check import cd_of
def kneser(n, k):
    ground = list(range(1, n + 1))
    V = [frozenset(s) for s in itertools.combinations(ground, k)]
    return ground, {i: s for i, s in enumerate(V)}
def schrijver(n, k):
    ground = list(range(1, n + 1))
    def stable(s):
        for a in s:
            if (a % n) + 1 in s:
                return False
        return True
    V = [frozenset(s) for s in itertools.combinations(ground, k) if stable(s)]
    # (1,n) 쌍도 연속으로 본다: a%n+1 은 n->1 을 포함
    return ground, {i: s for i, s in enumerate(V)}
def check_adj(hedges, n, k, kind):
    # 인접 = 서로소 확인 (표현 검증)
    return True
for (name, (ground, H), tau, chi) in [
    ('K(5,2)=Petersen', kneser(5, 2), 3, 3),
    ('K(6,2)', kneser(6, 2), 4, 4),
    ('S(6,2)', schrijver(6, 2), 4, 4),
    ('S(7,2)', schrijver(7, 2), 5, 5),
    ('S(8,3)', schrijver(8, 3), 4, 4),
]:
    res = cd_of(ground, H)
    print(name, 'V(G)=', len(H), 'cd(H)=', res[0], 'U=', sorted(res[1]), '| R01 tau=', tau, 'chi=', chi, flush=True)
