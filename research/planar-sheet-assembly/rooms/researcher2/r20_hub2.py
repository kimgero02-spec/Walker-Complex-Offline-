# R20 정리 2' 검산: 기반 별숲 장 S_i 에도 줄(chord)을 쳐서 (3,2) 로 올린 판. Delta = (N-12)/3 목표.
import networkx as nx, itertools
from r20_hub import three_col
def base_up(k, up_last=True):
    A=lambda i:[('a',i,0),('a',i,1)]; B=lambda i:[('b',i,0),('b',i,1)]
    Z=[v for i in range(k) for v in A(i)+B(i)]
    S=[]
    for i in range(k):
        G=nx.Graph()
        la=[v for j in range(k) if j>i for v in A(j)]+[v for j in range(k) if j<i for v in B(j)]
        lb=[v for j in range(k) if j>i for v in B(j)]+[v for j in range(k) if j<i for v in A(j)]
        for h in A(i):
            for v in la: G.add_edge(h,v)
        for h in B(i):
            for v in lb: G.add_edge(h,v)
        S.append(G)
    S0=nx.Graph([(u,v) for i in range(k) for u in A(i) for v in B(i)])
    M=nx.Graph([tuple(A(i)) for i in range(k)]+[tuple(B(i)) for i in range(k)])
    # 줄 계획: i (0-기준) 짝수 -> a-블록, 잎 쌍 a_{i+1}; i 홀수 -> b-블록, 잎 쌍 b_{i+1}; 마지막 S_{k-1} 은 a-블록, 잎 쌍 b_0
    plan=[]
    for i in range(k-1):
        plan.append((i, A(i), A(i+1)) if i%2==0 else (i, B(i), B(i+1)))
    if up_last: plan.append((k-1, A(k-1), B(0)))
    for i,(h1,h2),(u,w) in plan:
        G=S[i]; G.remove_edge(h2,u); G.remove_edge(h1,w); G.add_edge(u,w)
        M.remove_edge(u,w); M.add_edge(h2,u); M.add_edge(h1,w)
    return Z, S+[S0,M]
def build2(k, up_last=True):
    Z,base=base_up(k,up_last); t=len(Z)
    def chi(G): return 2 if nx.is_bipartite(G) else three_col(G)
    sb=sum(chi(G) for G in base); m=t+1-sb
    X=[('x',i) for i in range(1,m+1)]; Y=[('y',i) for i in range(1,m+1)]
    Q=[]; prev=list(Z)
    for i in range(1,m+1):
        x,y=X[i-1],Y[i-1]; G=nx.Graph()
        for v in prev: G.add_edge(x,v); G.add_edge(y,v)
        if i>=2:
            a,b=X[i-2],Y[i-2]; G.remove_edge(x,b); G.remove_edge(y,a); G.add_edge(a,b)
        Q.append(G); prev=prev+[x,y]
    if m>=1:
        L=nx.Graph([(X[i-1],Y[i-2]) for i in range(2,m+1)]+[(Y[i-1],X[i-2]) for i in range(2,m+1)]+[(X[m-1],Y[m-1])])
        base[0]=nx.compose(base[0],L)
    return prev, base+Q, m
for k in [4,5,6,7,8]:
    V,sh,m=build2(k); N=len(V)
    cnt={}
    for S in sh:
        for e in S.edges(): cnt[frozenset(e)]=cnt.get(frozenset(e),0)+1
    allE=set(frozenset(e) for e in itertools.combinations(V,2))
    exact=set(cnt)==allE and all(c==1 for c in cnt.values())
    chis=[2 if nx.is_bipartite(S) else three_col(S) for S in sh]
    oms=[max(len(c) for c in nx.find_cliques(S)) for S in sh]
    D=sum(c>w for c,w in zip(chis,oms))
    print(f"k={k} m={m} N={N} 정확={exact} 평면={all(nx.check_planarity(S)[0] for S in sh)} sigma={sum(chis)} "
          f"sum_omega={sum(oms)} Delta={D} (N-12)/3={(N-12)/3:.2f} N/3={N/3:.2f} M장 이분={nx.is_bipartite(sh[k+1])}")
