# R21 과제 2: 세 점 확장 조작 T 의 검산.
# 정리 2.3 의 증명을 그대로 코드로 옮긴 것이다. 계산은 증명의 근거가 아니라 오타 검산용이다.
# 기반: N=7 (R19 쌍뿔 예), N=8 (R19 보충 예), N=9 (R20 순환 예) 에 표시 쌍을 붙인다.
import itertools, ast, networkx as nx, sys
sys.path.insert(0, '.')
from r19_lib import chi, omega

def sharp_ok(P, pairs, need_nonadj):
    """P# = P + 각 표시 쌍마다 차수 2 새 점. 평면이고, (3,2) 장이면 쌍이 비인접."""
    H = P.copy()
    for t, (a, b) in enumerate(pairs):
        w = ('w', t)
        H.add_edge(w, a); H.add_edge(w, b)
        if need_nonadj and P.has_edge(a, b):
            return False
    return nx.check_planarity(H)[0]

def check(N, sheets, pairs):
    """sheets: 그래프 목록, pairs: 장마다 표시 쌍 목록 (chi=3 이면 1개, chi=4 이면 2개, chi=2 이면 0개)."""
    V = list(range(N)) if all(isinstance(v, int) for P in sheets for v in P) else None
    cnt = {}
    for P in sheets:
        for e in P.edges():
            cnt[frozenset(e)] = cnt.get(frozenset(e), 0) + 1
    allv = set().union(*[set(P.nodes()) for P in sheets])
    exact = len(allv) == N and set(cnt) == set(frozenset(e) for e in itertools.combinations(allv, 2)) and all(c == 1 for c in cnt.values())
    chis = [chi(P) for P in sheets]; oms = [omega(P) for P in sheets]
    planar = all(nx.check_planarity(P)[0] for P in sheets)
    used = [v for ps in pairs for p in ps for v in p]
    disjoint = len(used) == len(set(used))
    npairs_ok = all(len(ps) == {2: 0, 3: 1, 4: 2}[c] for ps, c in zip(pairs, chis))
    sharp = all(sharp_ok(P, ps, (c, o) == (3, 2)) for P, ps, c, o in zip(sheets, pairs, chis, oms))
    sigma = sum(chis); Delta = sum(1 for c, o in zip(chis, oms) if c > o)
    return dict(N=N, exact=exact, planar=planar, sigma=sigma, Delta=Delta, floorN3=N // 3,
                disjoint=disjoint, npairs_ok=npairs_ok, sharp=sharp, chis=chis, omegas=oms)

def step(N, sheets, pairs):
    """조작 T: 새 점 x,y,z 를 더한다 (정리 2.3 의 증명)."""
    x, y, z = N, N + 1, N + 2
    V = list(range(N))
    chis = [chi(P) for P in sheets]
    used = [v for ps in pairs for p in ps for v in p]
    free = [v for v in V if v not in used]          # 펜던트 칸에 줄 점들
    new = [P.copy() for P in sheets]
    A, B = [], []                                    # A: 옛 장에서 z 의 이웃, B: 옛 장에서 x 의 이웃
    fi = 0
    for j, (P, ps, c) in enumerate(zip(new, pairs, chis)):
        if c == 3:   # z 가 쌍 위 차수 2, x 는 펜던트 (j 가 홀수면 역할을 바꿔 A,B 를 둘 다 비지 않게)
            hi, lo = (z, x) if j % 2 == 0 else (x, z)
            a, b = ps[0]; P.add_edge(hi, a); P.add_edge(hi, b)
            l = free[fi]; fi += 1; P.add_edge(lo, l)
            (A if hi == z else B).extend([a, b]); (A if lo == z else B).append(l)
        elif c == 4:
            (a, b), (a2, b2) = ps
            P.add_edge(z, a); P.add_edge(z, b); P.add_edge(x, a2); P.add_edge(x, b2)
            A.extend([a, b]); B.extend([a2, b2])
        elif c == 2:
            l1 = free[fi]; l2 = free[fi + 1]; fi += 2
            P.add_edge(z, l1); P.add_edge(x, l2); A.append(l1); B.append(l2)
    assert fi == len(free), (fi, len(free))
    assert sorted(A + B) == V and A and B
    new[0].add_edge(x, y)            # y 는 펜던트
    new[1].add_edge(y, z)
    S = nx.Graph()
    for a in A: S.add_edge(x, a); S.add_edge(y, a)
    for b in B: S.add_edge(y, b); S.add_edge(z, b)
    S.add_edge(x, z)
    return N + 3, new + [S], pairs + [[(x, y)]]

def base7():
    P1 = nx.Graph([(i, (i + 1) % 5) for i in range(5)] + [(5, 6)])                     # C5 ⊔ K2
    P2 = nx.Graph([(i, (i + 2) % 5) for i in range(5)] + [(h, i) for h in (5, 6) for i in range(5)])  # 오각별 ∨ 2점
    return 7, [P1, P2], [[(2, 4)], [(5, 0), (6, 1)]]

def base8():
    P = nx.Graph([(7, i) for i in range(5)] + [(i, (i + 1) % 5) for i in range(5)] + [(7, 5), (5, 6)])
    Pc = nx.complement(P)
    return 8, [P, Pc], [[(1, 2), (3, 4)], [(6, 7), (5, 0)]]

def base9():
    L = open('r20_cyc3_out.txt').read().splitlines(); E = ast.literal_eval(L[1]); n = 3
    lab = {(i, r): 3 * i + r for i in range(n) for r in range(3)}
    sheets = [nx.Graph([(lab[((a + k) % n, r)], lab[((b + k) % n, s)]) for (a, r), (b, s) in E]) for k in range(n)]
    # 표시 쌍: 장 0 의 (0,1) 을 회전한 (3k,3k+1). 0 과 1 은 차수 2 점 2 의 두 이웃이라 같은 면 위에 있다.
    return 9, sheets, [[(3 * k, 3 * k + 1)] for k in range(n)]

if __name__ == '__main__':
    for base in (base7, base8, base9):
        N, sh, pr = base()
        print('base', check(N, sh, pr), pr)
        for _ in range(int(sys.argv[1]) if len(sys.argv) > 1 else 3):
            N, sh, pr = step(N, sh, pr)
            r = check(N, sh, pr)
            print('  step', {k: r[k] for k in ('N', 'exact', 'planar', 'sigma', 'Delta', 'floorN3', 'disjoint', 'npairs_ok', 'sharp')})
