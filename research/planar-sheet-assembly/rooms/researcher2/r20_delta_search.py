# R20 과제1: Delta = floor(N/3) 를 이루는 예 하나 찾기 (근거 아님, 예 구성용).
# 장 종류: 't' = 삼각형 없음 (목표 (3,2)), 'k' = K4 없음 + chi=4 목표 ((4,3)), 'b' = 이분.
import networkx as nx, itertools, random, sys
from r19_lib import chi, omega
def npl(G):
    H=nx.Graph(); bad=0
    for e in G.edges():
        H.add_edge(*e)
        if not nx.check_planarity(H)[0]: H.remove_edge(*e); bad+=1
    return bad
def cost(cls,types,N):
    c=0
    for E,t in zip(cls,types):
        G=nx.Graph(E); c+=npl(G)
        if t=='t': c+=sum(nx.triangles(G).values())//3
        elif t=='k': c+=sum(1 for q in nx.enumerate_all_cliques(G) if len(q)==4)
        elif t=='b':
            if not nx.is_bipartite(G): c+=1
    return c
def search(N,types,seed,iters):
    random.seed(seed); E=list(itertools.combinations(range(N),2)); n=len(types)
    a={e:random.randrange(n) for e in E}
    def cl(): return [[e for e in E if a[e]==k] for k in range(n)]
    c=cost(cl(),types,N); T=1.0
    for it in range(iters):
        e=random.choice(E); old=a[e]; a[e]=random.choice([k for k in range(n) if k!=old])
        c2=cost(cl(),types,N)
        if c2<=c or random.random()<2.718**((c-c2)/T): c=c2
        else: a[e]=old
        T=max(0.05,T*0.9995)
        if c==0:
            P=[nx.Graph(x) for x in cl()]
            for G in P: G.add_nodes_from(range(N))
            ch=[chi(G) for G in P]; om=[omega(G) for G in P]
            want=[3 if t=='t' else 4 if t=='k' else 2 for t in types]
            if ch==want and sum(ch)==N: return P,ch,om
            # chi 가 모자라면 계속 탐색: 비용 1 로 취급
            c=1
    return None
if __name__=="__main__":
    N=int(sys.argv[1]); types=sys.argv[2]; ns=int(sys.argv[3]); it=int(sys.argv[4])
    for s in range(ns):
        r=search(N,types,s,it)
        if r:
            P,ch,om=r; print("N",N,"types",types,"seed",s,"chi",ch,"omega",om,"Delta",sum(c>w for c,w in zip(ch,om)))
            print([sorted(G.edges()) for G in P]); break
        print("seed",s,"fail",flush=True)
