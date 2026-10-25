# R21 과제 1 시험 사례: K_8 = P ∪ B1 ∪ B2, P 는 (3,2) 평면, B1,B2 는 평면 이분 (sigma=7, 꽉 찬 체 8=2*2*2).
# 올은 크기 2 (P 의 변) 이고 좌표 (a,b) in Z_2^2 로 붙는다. 예 하나를 찾거나 없음을 보이는 탐색.
# 결과는 정리 3.3 의 손 증명과 대조하는 용도이다.
import itertools, networkx as nx, sys
fib = [(a, b) for a in (0, 1) for b in (0, 1)]
V = [(f, s) for f in fib for s in (0, 1)]
rungs = [((f, 0), (f, 1)) for f in fib]
pairs = list(itertools.combinations(fib, 2))
def cross(f, g): return [((f, s), (g, t)) for s in (0, 1) for t in (0, 1)]
opts = []  # 올 쌍마다 P 의 교차 변 선택: 짝 (matching) 만 가능 (삼각형 없음)
for f, g in pairs:
    E = cross(f, g)
    o = [()] + [(e,) for e in E] + [(((f, 0), (g, 0)), ((f, 1), (g, 1))), (((f, 0), (g, 1)), ((f, 1), (g, 0)))]
    opts.append(o)
def tri_free(G): return all(not (set(G[u]) & set(G[v])) for u, v in G.edges())
found = 0
for choice in itertools.product(*opts):
    P = nx.Graph(rungs + [e for c in choice for e in c])
    if not tri_free(P) or nx.is_bipartite(P) or not nx.check_planarity(P)[0]:
        continue
    Pset = set(frozenset(e) for e in P.edges())
    b1, b2, free = [], [], []
    for f, g in pairs:
        for e in cross(f, g):
            if frozenset(e) in Pset: continue
            d1, d2 = f[0] != g[0], f[1] != g[1]
            if d1 and d2: free.append(e)
            elif d1: b1.append(e)
            else: b2.append(e)
    G1, G2 = nx.Graph(b1), nx.Graph(b2)
    if not (nx.check_planarity(G1)[0] and nx.check_planarity(G2)[0]): continue
    for mask in range(1 << len(free)):
        H1 = G1.copy(); H2 = G2.copy()
        for i, e in enumerate(free):
            (H1 if mask >> i & 1 else H2).add_edge(*e)
        if nx.check_planarity(H1)[0] and nx.check_planarity(H2)[0]:
            found += 1
            if found <= 3:
                print('예:', sorted(P.edges()), '\nB1:', sorted(H1.edges()), '\nB2:', sorted(H2.edges()))
            break
print('찾은 P 선택 수:', found)
