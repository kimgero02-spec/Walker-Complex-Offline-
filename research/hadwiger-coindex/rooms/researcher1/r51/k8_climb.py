"""K_8 곧은 선 2층 배치 (기하 두께 2) 를 언덕 오르기로 구성. 목표: 교차 그래프가 이분.
찾으면 좌표를 정수 격자로 반올림해 다시 검사하고 (c1,c2) 파레토와 함께 출력."""
import itertools, random, sys
import networkx as nx
from line_search import crossing_graph, pareto

def frustration(X, rnd, iters=30):
    # 최대 절단 국소 탐색: 같은 쪽 인접 쌍 수의 최소 근사
    best = None
    nodes = list(X.nodes())
    for _ in range(iters):
        side = {v: rnd.randint(0, 1) for v in nodes}
        improved = True
        while improved:
            improved = False
            for v in nodes:
                same = sum(1 for u in X[v] if side[u] == side[v])
                if same * 2 > X.degree(v):
                    side[v] ^= 1; improved = True
        f = sum(1 for u, v in X.edges() if side[u] == side[v])
        best = f if best is None else min(best, f)
        if best == 0: break
    return best

def climb(n, seed, steps=4000):
    rnd = random.Random(seed)
    edges = list(itertools.combinations(range(n), 2))
    pts = [(rnd.random(), rnd.random()) for _ in range(n)]
    cur = frustration(crossing_graph(pts, edges), rnd)
    for s in range(steps):
        i = rnd.randrange(n); old = pts[i]
        sc = 0.3 if s < steps / 2 else 0.05
        pts[i] = (old[0] + rnd.gauss(0, sc), old[1] + rnd.gauss(0, sc))
        f = frustration(crossing_graph(pts, edges), rnd)
        if f <= cur: cur = f
        else: pts[i] = old
        if cur == 0: return pts
    return None

if __name__ == "__main__":
    n = int(sys.argv[1])
    edges = list(itertools.combinations(range(n), 2))
    for seed in range(int(sys.argv[2])):
        pts = climb(n, seed)
        if pts is None: continue
        ip = [(round(x * 1000), round(y * 1000)) for x, y in pts]
        X = crossing_graph(ip, edges)
        P = pareto(X)
        if P is not None:
            print("seed", seed, "pts", ip, "crossings", X.number_of_edges(), "pareto", sorted(P))
            break
