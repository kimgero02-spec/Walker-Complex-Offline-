"""정리 A (X(1,inf) => m <= 4n-8) 의 증명 오류를 잡기 위한 소수의 시험 (근거 아님).
곧은 선 점 배치에서 교차 그래프가 별 숲 (= (1,inf) 층 배정 존재) 을 유지하도록 간선을 탐욕적으로 추가."""
import itertools, random
import networkx as nx
from line_search import cross
def star_forest(X):
    for c in nx.connected_components(X):
        H=X.subgraph(c)
        if len(c)<=2: continue
        if not nx.is_tree(H): return False
        if sum(1 for v in H if H.degree(v)>1)>1: return False
    return True
for n in [8,10,12,14]:
    for seed in range(3):
        rnd=random.Random(seed*100+n)
        pts=[(rnd.random(),rnd.random()) for _ in range(n)]
        E=list(itertools.combinations(range(n),2)); rnd.shuffle(E)
        chosen=[]; X=nx.Graph()
        for e in E:
            X.add_node(e)
            for g in chosen:
                if len(set(e)|set(g))==4 and cross(pts[e[0]],pts[e[1]],pts[g[0]],pts[g[1]]): X.add_edge(e,g)
            if star_forest(X): chosen.append(e)
            else: X.remove_node(e)
        print(n, seed, "m", len(chosen), "4n-8", 4*n-8, "OK" if len(chosen)<=4*n-8 else "VIOLATION")
