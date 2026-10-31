"""R51-r1: 곧은 선 셀로판 겹침의 결정적 예 찾기 (구성용 탐색, 근거 아님).
K_n 의 점 배치에서 교차 그래프 (간선=정점, 교차=인접) 를 만들고
이분 그래프이면 층 배정 (성분별 두 방향) 중 교차 차수 (c1,c2) 의 파레토 최소를 구한다.
찾은 배치는 좌표·층·교차를 출력해 손으로 재확인할 수 있게 한다."""
import itertools, random, sys
import networkx as nx

def orient(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def cross(p, q, r, s):
    # 끝점을 공유하지 않는 두 선분의 고유 교차 (일반 위치 가정)
    o1, o2 = orient(p, q, r), orient(p, q, s)
    o3, o4 = orient(r, s, p), orient(r, s, q)
    return o1*o2 < 0 and o3*o4 < 0

def crossing_graph(pts, edges):
    X = nx.Graph(); X.add_nodes_from(range(len(edges)))
    for i, j in itertools.combinations(range(len(edges)), 2):
        (a, b), (c, d) = edges[i], edges[j]
        if len({a, b, c, d}) < 4: continue
        if cross(pts[a], pts[b], pts[c], pts[d]): X.add_edge(i, j)
    return X

def pareto(X):
    """이분이면 가능한 (c1,c2) 파레토 집합 (c1<=c2 로 정규화 안 함)."""
    if not nx.is_bipartite(X): return None
    comps = [c for c in nx.connected_components(X) if len(c) > 1]
    opts = []
    for c in comps:
        H = X.subgraph(c); A, B = nx.bipartite.sets(H)
        da = max(H.degree(v) for v in A); db = max(H.degree(v) for v in B)
        opts.append(((da, db), (db, da)))
    best = set()
    for choice in itertools.product(*opts) if len(opts) <= 14 else []:
        c1 = max([x[0] for x in choice], default=0); c2 = max([x[1] for x in choice], default=0)
        best.add((c1, c2))
    if len(opts) > 14:  # 탐욕 근사
        best.add((max(max(o[0]) for o in opts), max(max(o[0]) for o in opts)))
    if not opts: best.add((0, 0))
    return {p for p in best if not any(q != p and q[0] <= p[0] and q[1] <= p[1] for q in best)}

def search(n, trials, seed, target=None):
    rnd = random.Random(seed)
    edges = list(itertools.combinations(range(n), 2))
    found = {}
    for t in range(trials):
        pts = [(rnd.random(), rnd.random()) for _ in range(n)]
        X = crossing_graph(pts, edges)
        P = pareto(X)
        if P is None: continue
        for p in P:
            key = tuple(sorted(p))
            if key not in found or X.number_of_edges() < found[key][0]:
                found[key] = (X.number_of_edges(), pts)
    return found

if __name__ == "__main__":
    n = int(sys.argv[1]); trials = int(sys.argv[2])
    f = search(n, trials, 1)
    for k in sorted(f): print(n, k, "crossings", f[k][0])
