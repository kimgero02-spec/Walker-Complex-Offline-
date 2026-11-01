# 곧은 선 2층 그림 탐색: 점 배치 P 에서 K_n 의 교차 그래프가 이분이면 층 배정 (성분별 뒤집기) 중
# 교차 차수 (c1,c2) 를 사전식 최소화. 결정적 예(구성) 하나를 찾는 용도.
import itertools, random, sys
import networkx as nx
def cross(p,q,r,s):
    def o(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    return o(p,q,r)*o(p,q,s)<0 and o(r,s,p)*o(r,s,q)<0
def analyze(P,edges):
    X=nx.Graph(); X.add_nodes_from(range(len(edges)))
    for i,j in itertools.combinations(range(len(edges)),2):
        a,b=edges[i]; c,d=edges[j]
        if len({a,b,c,d})==4 and cross(P[a],P[b],P[c],P[d]): X.add_edge(i,j)
    if not nx.is_bipartite(X): return None
    comps=[c for c in nx.connected_components(X) if len(c)>1]
    cols=[nx.bipartite.color(X.subgraph(c)) for c in comps]
    best=None
    for flips in itertools.product([0,1],repeat=len(comps)):
        lay={}
        for f,col in zip(flips,cols):
            for v,c in col.items(): lay[v]=c^f
        c1=max([X.degree(v) for v in lay if lay[v]==0]+[0]); c2=max([X.degree(v) for v in lay if lay[v]==1]+[0])
        key=(min(c1,c2),max(c1,c2))
        if best is None or key<best[0]: best=(key,dict(lay))
    return best[0],best[1],X.number_of_edges()
def search(n,iters,seed=1):
    random.seed(seed); edges=list(itertools.combinations(range(n),2)); best=None
    for it in range(iters):
        P=[(random.random(),random.random()) for _ in range(n)]
        r=analyze(P,edges)
        if r and (best is None or r[0]<best[0]): best=(r[0],P,r[1],r[2])
    return best
if __name__=="__main__":
    n=int(sys.argv[1]); it=int(sys.argv[2])
    b=search(n,it)
    print(n, b[0] if b else None, 'crossings',b[3] if b else None)
    if b: print([ (round(x,3),round(y,3)) for x,y in b[1]])
