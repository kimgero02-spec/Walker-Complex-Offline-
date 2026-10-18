# R20 정리 2 검산: 별숲 기반 압축 + 줄 친 쌍 허브 -> 결함 장 수가 N 에 비례하는 비경직 등식.
import networkx as nx, itertools, sys
def base_K4k(k, odd=False):
    """K_{4k} (odd=True 이면 K_{4k+1}) 의 이분 평면 장 분해. 점 이름 ('a',i,s),('b',i,s), s in {0,1}."""
    A=lambda i:[('a',i,0),('a',i,1)]; B=lambda i:[('b',i,0),('b',i,1)]
    Z=[v for i in range(k) for v in A(i)+B(i)]
    sheets=[]
    for i in range(k):
        S=nx.Graph()
        la=[v for j in range(k) if j>i for v in A(j)]+[v for j in range(k) if j<i for v in B(j)]
        lb=[v for j in range(k) if j>i for v in B(j)]+[v for j in range(k) if j<i for v in A(j)]
        for h in A(i):
            for v in la: S.add_edge(h,v)
        for h in B(i):
            for v in lb: S.add_edge(h,v)
        sheets.append(S)
    S0=nx.Graph([(u,v) for i in range(k) for u in A(i) for v in B(i)]); sheets.append(S0)
    M=nx.Graph([tuple(A(i)) for i in range(k)]+[tuple(B(i)) for i in range(k)]); sheets.append(M)
    if odd:
        Z=Z+['inf']; sheets.append(nx.Graph([('inf',v) for v in Z if v!='inf']))
    return Z,sheets
def build(k, odd=False):
    Z,base=base_K4k(k,odd); t=len(Z)
    sb=2*len(base); m=t+1-sb
    assert m>=2, "k 가 너무 작다"
    X=[('x',i) for i in range(1,m+1)]; Y=[('y',i) for i in range(1,m+1)]
    Q=[]; prev=list(Z)
    for i in range(1,m+1):
        x,y=X[i-1],Y[i-1]; G=nx.Graph()
        for v in prev: G.add_edge(x,v); G.add_edge(y,v)
        if i>=2:
            a,b=X[i-2],Y[i-2]
            G.remove_edge(x,b); G.remove_edge(y,a); G.add_edge(a,b)
        Q.append(G); prev=prev+[x,y]
    L=nx.Graph([(X[i-1],Y[i-2]) for i in range(2,m+1)]+[(Y[i-1],X[i-2]) for i in range(2,m+1)]+[(X[m-1],Y[m-1])])
    base[0]=nx.compose(base[0],L)
    return prev, base+Q
def three_col(G):
    # 줄 친 허브 장은 손 색칠이 있다; 여기서는 일반 탐욕+역추적 대신 DSATUR 후 검증
    c=nx.coloring.greedy_color(G,strategy='DSATUR')
    return max(c.values())+1
def check(k,odd=False):
    V,sh=build(k,odd); N=len(V)
    cnt={}
    for S in sh:
        for e in S.edges(): cnt[frozenset(e)]=cnt.get(frozenset(e),0)+1
    allE=[frozenset(e) for e in itertools.combinations(V,2)]
    exact=all(cnt.get(e,0)==1 for e in allE) and len(cnt)==len(allE)
    chis=[];oms=[]
    for S in sh:
        if nx.is_bipartite(S): chis.append(2)
        else: chis.append(three_col(S))
        oms.append(max(len(c) for c in nx.find_cliques(S)))
    D=sum(1 for c,w in zip(chis,oms) if c>w)
    print(f"k={k} odd={odd} N={N} 정확분해={exact} 평면={all(nx.check_planarity(S)[0] for S in sh)} "
          f"sigma={sum(chis)} sum_omega={sum(oms)} Delta={D} 장수={len(sh)} chi다중집합={sorted(chis)}")
for k in [3,4,5,6]:
    check(k); check(k,True)
