# R20 과제2: 체가 꽉 찬 (4,3) 장, N=12, 다른 장 chi {2,2}. 올 F_t (t in {0,1}^2) 은 P 의 삼각형.
# 예 하나를 찾는 탐색 (근거 아님). want4=1 이면 chi(P)=4 를 요구.
import networkx as nx, itertools, random, sys
from r19_lib import chi
F={t:[(t,s) for s in range(3)] for t in itertools.product((0,1),repeat=2)}
V=[v for t in F for v in F[t]]
cross=[(u,v) for u,v in itertools.combinations(V,2) if u[0]!=v[0]]
allowed={e:['P']+[j for j in (0,1) if e[0][0][j]!=e[1][0][j]] for e in cross}
def graphs(a):
    P=nx.Graph(); P.add_nodes_from(V); B=[nx.Graph(),nx.Graph()]
    for t in F: P.add_edges_from(itertools.combinations(F[t],2))
    for e,s in a.items():
        (P if s=='P' else B[s]).add_edge(*e)
    return P,B
def npl(G):
    H=nx.Graph(); bad=0
    for e in G.edges():
        H.add_edge(*e)
        if not nx.check_planarity(H)[0]: H.remove_edge(*e); bad+=1
    return bad
def k4(P): return sum(1 for c in nx.enumerate_all_cliques(P) if len(c)==4)
def cost(a,want4):
    P,B=graphs(a); c=npl(P)+npl(B[0])+npl(B[1])+k4(P)
    if want4 and c==0 and chi(P)<4: c=1
    return c
def run(seed,want4,iters=60000):
    random.seed(seed); a={e:random.choice(allowed[e]) for e in cross}; c=cost(a,want4); T=1.0
    for it in range(iters):
        e=random.choice(cross); old=a[e]; opts=[s for s in allowed[e] if s!=old]
        a[e]=random.choice(opts); c2=cost(a,want4)
        if c2<=c or random.random()<2.718**((c-c2)/T): c=c2
        else: a[e]=old
        T=max(0.03,T*0.9995)
        if c==0: return a
    return None
if __name__=="__main__":
    want4=int(sys.argv[1]); ns=int(sys.argv[2])
    for s in range(ns):
        a=run(s,want4)
        if a:
            P,B=graphs(a); print("seed",s,"chi(P)",chi(P),"|P|",P.number_of_edges(),"|B|",[b.number_of_edges() for b in B])
            if want4: print(sorted(P.edges())); print([sorted(b.edges()) for b in B]); break
        else: print("seed",s,"fail")
