# C_n (홀수) 별 판의 최소 잎 수: 4-색칠(색 대칭 제거)마다 고른 삼중쌍 중 하나가 무지개 = 집합 덮개. 정확한 최소를 계산.
import itertools, sys, networkx as nx
from r05_lib import *
n=int(sys.argv[1]); Q=nx.cycle_graph(n)
cols=colorings(Q,4); T=indep_triples(Q)
R={t:sum(1<<i for i,c in enumerate(cols) if len({c[v] for v in t})==3) for t in T}
FULL=(1<<len(cols))-1
print('n',n,'색칠',len(cols),'삼중쌍',len(T))
for k in range(1,9):
    found=None
    # 대칭(회전) 으로 첫 삼중쌍에 0 을 포함하도록 고정
    first=[t for t in T if 0 in t]
    for t0 in first:
        rest=[t for t in T if t>t0 or 0 not in t]
        for S in itertools.combinations([t for t in T if t!=t0],k-1):
            m=R[t0]
            for t in S: m|=R[t]
            if m==FULL: found=(t0,)+S; break
        if found: break
    print(k, found); sys.stdout.flush()
    if found: break
