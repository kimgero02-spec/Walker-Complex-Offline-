# 홀수 판: 기반 K_{4k} 에 점 inf 와 별 장 K_{1,4k} 를 더한 뒤 같은 허브 단계.
import networkx as nx, itertools, r20_hub2 as H
from r20_hub import three_col
def build_odd(k):
    Z,base=H.base_up(k); Z=Z+['inf']; base.append(nx.Graph([('inf',v) for v in Z[:-1]]))
    t=len(Z); chi=lambda G: 2 if nx.is_bipartite(G) else three_col(G)
    m=t+1-sum(chi(G) for G in base)
    X=[('x',i) for i in range(1,m+1)]; Y=[('y',i) for i in range(1,m+1)]; Q=[]; prev=list(Z)
    for i in range(1,m+1):
        x,y=X[i-1],Y[i-1]; G=nx.Graph()
        for v in prev: G.add_edge(x,v); G.add_edge(y,v)
        if i>=2:
            a,b=X[i-2],Y[i-2]; G.remove_edge(x,b); G.remove_edge(y,a); G.add_edge(a,b)
        Q.append(G); prev=prev+[x,y]
    if m>=1:
        L=nx.Graph([(X[i-1],Y[i-2]) for i in range(2,m+1)]+[(Y[i-1],X[i-2]) for i in range(2,m+1)]+[(X[m-1],Y[m-1])])
        base[0]=nx.compose(base[0],L)
    return prev,base+Q,m
for k in [5,6,7]:
    V,sh,m=build_odd(k); N=len(V); cnt={}
    for S in sh:
        for e in S.edges(): cnt[frozenset(e)]=cnt.get(frozenset(e),0)+1
    exact=set(cnt)==set(frozenset(e) for e in itertools.combinations(V,2)) and all(c==1 for c in cnt.values())
    chis=[2 if nx.is_bipartite(S) else three_col(S) for S in sh]; oms=[max(len(c) for c in nx.find_cliques(S)) for S in sh]
    print(f"k={k} m={m} N={N} 정확={exact} 평면={all(nx.check_planarity(S)[0] for S in sh)} sigma={sum(chis)} Delta={sum(c>w for c,w in zip(chis,oms))} (N-8)/3={(N-8)/3:.2f}")
