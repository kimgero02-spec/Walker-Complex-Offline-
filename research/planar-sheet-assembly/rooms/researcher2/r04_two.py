# 구성 탐색: 평면 3-색 Q 와 독립 삼중쌍 T1,T2 로 "4-색칠에서 둘 다 비무지개 불가" 인 것
import random, sys
from r04_lib import *
random.seed(int(sys.argv[1]))
def all4(P):
    nodes = sorted(P.nodes(), key=lambda v: -P.degree(v)); out=[]; col={}
    def bt(i):
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
best=None
for it in range(3000):
    n = random.randint(7,int(sys.argv[2]))
    P = rand_planar(n, random.uniform(0.5,1.0))
    if not nx.is_connected(P) or chi(P)!=3: continue
    cols = all4(P)
    T = [t for t in itertools.combinations(P.nodes(),3) if indep(P,t)]
    mask = {}
    for t in T:
        m=0
        for i,c in enumerate(cols):
            if len({c[v] for v in t})<3: m|=1<<i
        mask[t]=m
    for t1,t2 in itertools.combinations(T,2):
        if mask[t1]&mask[t2]==0 and mask[t1] and mask[t2]:
            print('FOUND n=%d e=%d'%(n,P.number_of_edges()), t1, t2, sorted(P.edges())); best=1; break
    if best: break
print('it',it)
