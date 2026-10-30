# 추측 10 공격 2: P0 = 팔각형 + 비교차 현 집합(외평면, 강체 조건 만족), 두 띠 가향 부착. G 평면인 강체 P0 가 있나?
import itertools as it, networkx as nx
from band2 import check
n = 8
chords = [(i, j) for i in range(n) for j in range(i + 2, n) if not (i == 0 and j == n - 1)]
def cross(c, d):
    (a, b), (x, y) = c, d
    if len({a, b, x, y}) < 4: return False
    return (a < x < b) != (a < y < b)
arcs = [(0, 1), (2, 3), (4, 5), (6, 7)]
def faces_of(S):
    # 외평면 매장의 내부면: 재귀 분할
    polys = [list(range(n))]
    for (a, b) in sorted(S, key=lambda c: c[1] - c[0]):
        pass
    G = nx.Graph([(i, (i + 1) % n) for i in range(n)] + list(S))
    # 각 현으로 다각형을 자름
    polys = [list(range(n))]
    for (a, b) in S:
        new = []
        for p in polys:
            if a in p and b in p:
                ia, ib = p.index(a), p.index(b)
                i, j = min(ia, ib), max(ia, ib)
                if j - i >= 2 and not (i == 0 and j == len(p) - 1):
                    new += [p[i:j + 1], p[j:] + p[:i + 1]]; continue
            new.append(p)
        polys = new
    return polys
def rigid(polys):
    for p in polys:
        L = len(p); E = {frozenset((p[t], p[(t + 1) % L])) for t in range(L)}
        if sum(frozenset(a) in E for a in arcs) > 1: return False
    return True
def bandf(name, e_start, e_end):
    (a0, b0) = e_start; (b4, a4) = e_end  # 가향 연결(앞 계산에서 cross=True)
    A = [a0] + [f'{name}a{j}' for j in range(1, 4)] + [a4]
    B = [b0] + [f'{name}b{j}' for j in range(1, 4)] + [b4]
    return [(A[j], A[j + 1], B[j + 1], B[j]) for j in range(4)]
found = 0; tried = 0
for r in range(1, 6):
    for S in it.combinations(chords, r):
        if any(cross(c, d) for c, d in it.combinations(S, 2)): continue
        polys = faces_of(S)
        if not rigid(polys): continue
        tried += 1
        faces = [tuple(f'v{x}' for x in p) for p in polys] + bandf('p', ('v0', 'v1'), ('v4', 'v5')) + bandf('q', ('v2', 'v3'), ('v6', 'v7'))
        ok, G, cyc = check(faces)
        if ok and nx.check_planarity(G)[0]:
            found += 1
            if found <= 3: print("평면 강체 예:", S, "가향", ok)
print("강체 P0 수", tried, "평면 G 수", found)
