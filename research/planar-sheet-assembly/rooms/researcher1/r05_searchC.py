# 후보 C: 3-분할 고정, T1=(0,1,2), T2=(3,4,5) 를 각 분할에서 하나씩 (N1 의 3-색칠 무지개 조건을 그 분할에서 만족),
# T 안의 변은 금지하고 분할을 건너는 변을 평면성이 허락하는 한 모두 추가 (변-극대) -> 그 (T1,T2) 만 검사.
import random, sys, itertools, networkx as nx
from r05_lib import *
seed=int(sys.argv[1]); random.seed(seed)
nmin,nmax,iters=int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
T1=(0,1,2); T2=(3,4,5)
best=None
for it in range(iters):
    n=random.randint(nmin,nmax)
    part=[0,1,2,0,1,2]+[random.randrange(3) for _ in range(n-6)]
    if random.random()<0.5:  # T2 의 순서를 섞는다 (T1 과 다른 대응)
        part[3],part[4],part[5]=random.sample([0,1,2],3)
    Q=nx.empty_graph(n)
    E=[(u,v) for u,v in itertools.combinations(range(n),2) if part[u]!=part[v]
       and not ({u,v}<=set(T1) or {u,v}<=set(T2))]
    random.shuffle(E)
    for u,v in E:
        Q.add_edge(u,v)
        if not nx.check_planarity(Q)[0]: Q.remove_edge(u,v)
    cols=colorings(Q,4); M=masks(Q,cols,[T1,T2])
    bad=bin(M[T1]&M[T2]).count('1')
    if best is None or bad<best[0]: best=(bad,n,len(cols)); print('best',best,sorted(Q.edges())); sys.stdout.flush()
    if bad==0: print('FOUND'); break
