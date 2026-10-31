# 정리 2L 의 증명을 그대로 따라가는 구성 알고리즘. 평면 Q 에서 실패하면 증명에 구멍이 있다는 뜻 (증명의 점검용, 근거 아님).
import random, sys, itertools, networkx as nx
from r05_lib import *
def three_col(Q):
    c=colorings(Q,3); return c[0] if c else None
def proper(Q,c): return all(c[u]!=c[v] for u,v in Q.edges())
def nonrb(c,T): return len({c[v] for v in T})<3
def construct(Q,T1,T2,phi):
    I=set(T1)&set(T2)
    if len(I)==2:
        x,y=sorted(I,key=str); psi={v:phi[v] for v in Q}; 
        # 단계 0: 공유 두 점을 한 색으로 -> phi 에서 x 의 색을 y 에... 일반 구성: x,y 를 4 로
        psi[x]=psi[y]=3; return psi,'overlap2'
    if len(I)==1:
        x=next(iter(I)); U=[v for v in T1 if v!=x]; W=[v for v in T2 if v!=x]
        for u in U:
            for w in W:
                if not Q.has_edge(u,w):
                    psi=dict(phi); 
                    for v in (x,u,w): psi[v]=3
                    return psi,'overlap1-triple'
        # 모든 u~w: phi 에서 T2 단색 -> U 둘을 4 로
        psi=dict(phi)
        if phi[U[0]]==phi[U[1]]: psi[W[0]]=psi[W[1]]=3
        else: psi[U[0]]=psi[U[1]]=3
        return psi,'overlap1-mono'
    # 서로소
    for A,Bt in ((T1,T2),(T2,T1)):
        if nonrb(phi,A):
            psi=dict(phi); psi[Bt[0]]=psi[Bt[1]]=3; return psi,'N1'
    for p in itertools.combinations(T1,2):
        for q in itertools.combinations(T2,2):
            if not any(Q.has_edge(x,y) for x in p for y in q):
                psi=dict(phi)
                for v in p+q: psi[v]=3
                return psi,'N2'
    a={phi[v]:v for v in T1}; b={phi[v]:v for v in T2}
    for c in range(3):
        for s in range(3):
            for t in range(3):
                if c in (s,t): continue
                common=[m for m in Q[a[s]] if Q.has_edge(m,b[t]) and phi[m]==c]
                if not common:
                    psi=dict(phi)
                    for z in Q[b[t]]:
                        if phi[z]==c: psi[z]=3
                    psi[a[s]]=psi[a[c]]=3; psi[b[t]]=c
                    return psi,'N3'
    return None,'skeleton'
random.seed(int(sys.argv[1])); stats={}
for it in range(int(sys.argv[2])):
    n=random.randint(7,14)
    part=[random.randrange(3) for _ in range(n)]
    Q=nx.empty_graph(n); E=[(u,v) for u,v in itertools.combinations(range(n),2) if part[u]!=part[v]]; random.shuffle(E)
    for u,v in E[:random.randint(min(n,len(E)),len(E))]:
        Q.add_edge(u,v)
        if not nx.check_planarity(Q)[0]: Q.remove_edge(u,v)
    phi={v:part[v] for v in Q}
    T=indep_triples(Q)
    for _ in range(30):
        if len(T)<2: break
        T1,T2=random.sample(T,2)
        psi,how=construct(Q,T1,T2,phi)
        if psi is None or not proper(Q,psi) or not (nonrb(psi,T1) and nonrb(psi,T2)):
            print('FAIL',how,T1,T2,sorted(Q.edges())); sys.exit()
        stats[how]=stats.get(how,0)+1
print(stats)
