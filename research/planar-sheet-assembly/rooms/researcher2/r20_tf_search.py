# R20: 예 하나 찾기 — K_N 을 n 장의 삼각형 없는 평면 그래프로 분해 (각 장 chi=3 이면 sigma=3n).
import networkx as nx, itertools, random, sys
from r19_lib import chi, omega, planar
def nonplanar_pen(edges, N):
    G=nx.Graph(); G.add_nodes_from(range(N)); bad=0
    for e in edges:
        G.add_edge(*e)
        if not nx.check_planarity(G)[0]:
            G.remove_edge(*e); bad+=1
    return bad
def cost(assign, N, n):
    cls=[[e for e in assign if assign[e]==k] for k in range(n)]
    tri=0
    for a,b,c in itertools.combinations(range(N),3):
        x=assign[(a,b)];
        if assign[(a,c)]==x and assign[(b,c)]==x: tri+=1
    return tri+sum(nonplanar_pen(c,N) for c in cls)
def search(N,n,seed,iters=20000):
    random.seed(seed)
    E=list(itertools.combinations(range(N),2))
    assign={e:random.randrange(n) for e in E}
    c=cost(assign,N,n); T=1.0
    for it in range(iters):
        e=random.choice(E); old=assign[e]; assign[e]=random.choice([k for k in range(n) if k!=old])
        c2=cost(assign,N,n)
        if c2<=c or random.random()<2.718**((c-c2)/T): c=c2
        else: assign[e]=old
        T=max(0.05,T*0.9995)
        if c==0: return assign
    return None
if __name__=="__main__":
    N=int(sys.argv[1]); n=int(sys.argv[2])
    for s in range(int(sys.argv[3]) if len(sys.argv)>3 else 5):
        a=search(N,n,s)
        if a:
            P=[nx.Graph([e for e in a if a[e]==k]) for k in range(n)]
            for G in P: G.add_nodes_from(range(N))
            print("seed",s,"chis",[chi(G) for G in P],"omegas",[omega(G) for G in P],"planar",[planar(G) for G in P])
            print([sorted(G.edges()) for G in P]); break
        else: print("seed",s,"fail")
