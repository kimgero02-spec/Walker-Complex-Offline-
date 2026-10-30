# 구성 탐색: 평면 3-색 중심 P 에 잎 K_{1,1,3} 을 몇 개 붙여 chi=5. 잎 수 최소화, 서로소 판 기록
import random, sys
from r04_lib import *
random.seed(int(sys.argv[1]))
def all4(P):
    nodes = sorted(P.nodes(), key=lambda v: -P.degree(v)); out=[]; col={}
    def bt(i):
        if len(out)>20000: return
        if i==len(nodes): out.append(dict(col)); return
        v=nodes[i]; used={col[u] for u in P[v] if u in col}; mx=max(col.values(),default=-1)
        for c in range(min(4,mx+2)):
            if c not in used: col[v]=c; bt(i+1); del col[v]
    bt(0); return out
def rand_planar(n, dens):
    P = nx.empty_graph(n); E = list(itertools.combinations(range(n),2)); random.shuffle(E)
    for u,v in E:
        if random.random() > dens: continue
        P.add_edge(u,v)
        if not nx.check_planarity(P)[0]: P.remove_edge(u,v)
    return P
K = int(sys.argv[3])  # 잎 수 상한
for it in range(int(sys.argv[4])):
    n = random.randint(7,int(sys.argv[2]))
    P = rand_planar(n, random.uniform(0.4,1.0))
    if not nx.is_connected(P) or chi(P)!=3: continue
    cols = all4(P)
    if len(cols)>20000: continue
    T = [t for t in itertools.combinations(P.nodes(),3) if indep(P,t)]
    full=(1<<len(cols))-1
    mask={t:sum(1<<i for i,c in enumerate(cols) if len({c[v] for v in t})<3) for t in T}
    T=[t for t in T if mask[t]!=full]
    for k in range(2,K+1):
        hit=None
        for F in itertools.combinations(T,k):
            m=full
            for t in F: m&=mask[t]
            if m==0: hit=F; break
        if hit:
            disj = len(set().union(*hit))==3*k
            print('FOUND n=%d e=%d k=%d disjoint=%s'%(n,P.number_of_edges(),k,disj), hit, sorted(P.edges()), flush=True)
            break
