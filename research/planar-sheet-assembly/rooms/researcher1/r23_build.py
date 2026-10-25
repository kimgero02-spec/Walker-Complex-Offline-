# R23: 둘레5 (2,3) 소유 분해 예 직접 탐색 (이중 CEGAR). 후보 탐색 전용, 근거 아님.
# P2 = 고정된 조밀 평면 둘레5 그래프 Q (V1 은 Q 의 독립집합), P1 = 고를 변 (V1 에 닿는 쌍), 이분·평면·둘레 조건.
# 목표: G=P1∪P2 가 4-색칠 불가.
import networkx as nx, itertools, sys, random, json, time
from pysat.solvers import Cadical153
from r23_penta import dense_planar_girth5
def indep_set(Q,seed):
    rng=random.Random(seed); V=list(Q); rng.shuffle(V); I=set()
    for v in sorted(V,key=lambda v:Q.degree(v)):
        if not any(u in I for u in Q[v]): I.add(v)
    return I
def run(n,seed,V1size=None,maxit=200000,tlimit=1500):
    Q=dense_planar_girth5(n,seed); V=list(Q)
    I=indep_set(Q,seed)
    V1=set(sorted(I)[:V1size]) if V1size else I
    D=dict(nx.all_pairs_shortest_path_length(Q))
    cand=[]
    for u,v in itertools.combinations(V,2):
        if u not in V1 and v not in V1: continue
        if D[u].get(v,99)>=4: cand.append((u,v))
    print('n',Q.number_of_nodes(),'|E(Q)|',Q.number_of_edges(),'|V1|',len(V1),'cand',len(cand),flush=True)
    cnt=[0]
    def nv(): cnt[0]+=1; return cnt[0]
    t={e:nv() for e in cand}; side={v:nv() for v in V}
    S=Cadical153()
    for (u,v) in cand:
        S.add_clause([-t[(u,v)],side[u],side[v]]); S.add_clause([-t[(u,v)],-side[u],-side[v]])
    # 둘레: 짧은 사이클 금지
    U=nx.Graph(); U.add_nodes_from(V); U.add_edges_from(Q.edges()); U.add_edges_from(cand)
    key=lambda a,b: (a,b) if (a,b) in t else ((b,a) if (b,a) in t else None)
    nclause=0
    for a in V:
        for b,c in itertools.combinations(list(U[a]),2):
            # 삼각형 a,b,c
            if U.has_edge(b,c) and a<b and a<c:
                cl=[-t[k] for k in (key(a,b),key(a,c),key(b,c)) if k]
                if cl: S.add_clause(cl); nclause+=1
    for a,c in itertools.combinations(V,2):
        com=[x for x in U[a] if U.has_edge(x,c)]
        for b,d in itertools.combinations(com,2):
            if a<min(b,c,d) and c>... if False else True: pass
            cl=[-t[k] for k in (key(a,b),key(b,c),key(c,d),key(d,a)) if k]
            if cl: S.add_clause(cl); nclause+=1
    print('girth clauses',nclause,flush=True)
    # 처음에 4-색칠 하나로 시작하지 않고 반복
    def four_col(Eset):
        G=nx.Graph(); G.add_nodes_from(V); G.add_edges_from(Eset)
        idx={v:i for i,v in enumerate(V)}; var=lambda v,c:4*idx[v]+c+1
        s=Cadical153()
        for v in V: s.add_clause([var(v,c) for c in range(4)])
        for u,v in G.edges():
            for c in range(4): s.add_clause([-var(u,c),-var(v,c)])
        r=s.solve()
        if not r: return None
        m=set(l for l in s.get_model() if l>0)
        return {v:[c for c in range(4) if var(v,c) in m][0] for v in V}
    t0=time.time()
    for it in range(maxit):
        if time.time()-t0>tlimit: return 'timeout',it
        if not S.solve(): return 'UNSAT',it
        m=set(l for l in S.get_model() if l>0)
        P1=[e for e in cand if t[e] in m]
        H=nx.Graph(P1)
        if H.number_of_edges():
            pl,cert=nx.check_planarity(H,counterexample=True)
            if not pl:
                S.add_clause([-t[key(*e)] for e in cert.edges()]); continue
        col=four_col(list(Q.edges())+P1)
        if col is None:
            G=nx.Graph(list(Q.edges())+P1)
            sol=dict(Q=[list(map(int,e)) for e in Q.edges()],P1=[list(map(int,e)) for e in P1],V1=sorted(map(int,V1)))
            json.dump(sol,open(f'r23_build_{n}_{seed}.json','w'))
            return 'FOUND',it
        mono=[t[e] for e in cand if col[e[0]]==col[e[1]]]
        S.add_clause(mono)
        if it%500==0: print('it',it,len(P1),round(time.time()-t0),flush=True)
    return 'maxit',maxit
if __name__=="__main__":
    n,seed=int(sys.argv[1]),int(sys.argv[2])
    print(run(n,seed,tlimit=float(sys.argv[3]) if len(sys.argv)>3 else 1500))
