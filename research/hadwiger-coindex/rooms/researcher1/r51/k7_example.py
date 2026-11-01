"""K_7 의 곧은 선 (2,2) 겹침과 K_6 의 (1,1) 겹침: 정수 좌표로 구성하고 독립적으로 재검사."""
import itertools, random
import networkx as nx
from line_search import crossing_graph, pareto, orient
def find(n, target, seed=1, trials=50000):
    rnd=random.Random(seed); E=list(itertools.combinations(range(n),2))
    for t in range(trials):
        pts=[(rnd.randrange(0,40),rnd.randrange(0,40)) for _ in range(n)]
        if any(orient(*[pts[i] for i in tr])==0 for tr in itertools.combinations(range(n),3)): continue
        X=crossing_graph(pts,E); P=pareto(X)
        if P and any(p[0]<=target[0] and p[1]<=target[1] for p in P): return pts,E,X
for n,target in [(6,(1,1)),(7,(2,2))]:
    pts,E,X=find(n,target)
    # 층 배정: 각 성분에서 c1 쪽이 target[0] 이하가 되도록
    L={}
    for comp in nx.connected_components(X):
        H=X.subgraph(comp)
        if len(comp)==1: L[next(iter(comp))]=1; continue
        A,B=nx.bipartite.sets(H)
        da=max(H.degree(v) for v in A); db=max(H.degree(v) for v in B)
        if not (da<=target[0] and db<=target[1]): A,B=B,A
        for v in A: L[v]=1
        for v in B: L[v]=2
    print("n",n,"pts",pts)
    for l in (1,2):
        print(" L%d"%l,[E[i] for i in sorted(L) if L[i]==l])
    print(" crossings",[(E[i],E[j]) for i,j in X.edges()])
    for l in (1,2):
        print(" max crossings per L%d edge"%l, max([X.degree(i) for i in L if L[i]==l]+[0]))
    # 층 내부 교차 없음 재확인
    for i,j in X.edges(): assert L[i]!=L[j]
