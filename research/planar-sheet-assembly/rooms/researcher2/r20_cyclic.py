# R20: Z_n 순환 대칭 예 찾기. 점 (i,r), i in Z_n (n 홀수), r in {0,1,2}. N=3n.
# 기본 장 P 가 변 궤도마다 대표 하나를 가지면 P_k = rho^k(P) (k in Z_n) 가 K_N 의 분해.
import networkx as nx, random, sys, itertools
def orbits(n):
    O=[]
    for r in range(3):
        for rp in range(r+1,3):
            for d in range(n): O.append(((0,r),(d,rp)))
        for d in range(1,(n-1)//2+1): O.append(((0,r),(d,r)))
    return O
def edge(o,i,n):
    (a,r),(b,rp)=o; return ((a+i)%n,r),((b+i)%n,rp)
def build(O,choice,n):
    G=nx.Graph(); G.add_nodes_from((i,r) for i in range(n) for r in range(3))
    for o,c in zip(O,choice): G.add_edge(*edge(o,c,n))
    return G
def pen(G):
    tri=sum(nx.triangles(G).values())//3
    H=nx.Graph(); H.add_nodes_from(G); bad=0
    for e in G.edges():
        H.add_edge(*e)
        if not nx.check_planarity(H)[0]: H.remove_edge(*e); bad+=1
    return tri+bad
def search(n,seed,iters=200000):
    random.seed(seed); O=orbits(n); ch=[random.randrange(n) for _ in O]
    c=pen(build(O,ch,n)); T=1.0
    for it in range(iters):
        j=random.randrange(len(O)); old=ch[j]; ch[j]=random.randrange(n)
        c2=pen(build(O,ch,n))
        if c2<=c or random.random()<2.718**((c-c2)/T): c=c2
        else: ch[j]=old
        T=max(0.03,T*0.9997)
        if c==0:
            G=build(O,ch,n)
            if not nx.is_bipartite(G): return O,ch,G
    return None
if __name__=="__main__":
    n=int(sys.argv[1])
    for s in range(int(sys.argv[2])):
        r=search(n,s)
        if r:
            O,ch,G=r; print("n",n,"seed",s,"edges",G.number_of_edges()); print(sorted(G.edges())); break
        print("seed",s,"fail")
