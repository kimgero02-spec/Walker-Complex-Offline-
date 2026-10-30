# 후보 B: 고정 3-분할에 대해 변-극대인 평면 3-부분 그래프 (모든 평면 3-색 그래프는 이런 것의 부분그래프)
import random, sys, itertools, networkx as nx
from r05_lib import *
seed=int(sys.argv[1]); random.seed(seed)
nmin,nmax,iters=int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
for it in range(iters):
    n=random.randint(nmin,nmax)
    part=[random.randrange(3) for _ in range(n)]
    if len(set(part))<3: continue
    Q=nx.empty_graph(n)
    E=[(u,v) for u,v in itertools.combinations(range(n),2) if part[u]!=part[v]]
    random.shuffle(E)
    for u,v in E:
        Q.add_edge(u,v)
        if not nx.check_planarity(Q)[0]: Q.remove_edge(u,v)
    res,nc=two_leaf_pairs(Q)
    if res:
        print('FOUND',n,Q.number_of_edges(),nc,res[:3],sorted(Q.edges())); sys.stdout.flush(); break
    if it%50==0: print('it',it,n,Q.number_of_edges(),nc); sys.stdout.flush()
