# R06: 삼각형 + 귀 9개 (삼중쌍 셋, 각 삼중쌍에 종류 1,2,3 귀 하나씩) + 귀 사이 변 E.
# 조건: 모든 쌍 선택 p_i⊂T_i 에 대해 p1∪p2∪p3 가 E 의 변을 품음  <=>  잎 셋으로 chi=5.
import itertools, networkx as nx, sys
ears=[(i,c) for i in range(3) for c in range(3)]   # (삼중쌍 i, 종류 c)
cand=[(u,v) for u,v in itertools.combinations(ears,2) if u[0]!=v[0] and u[1]!=v[1]]
pairs=[list(itertools.combinations([(i,c) for c in range(3)],2)) for i in range(3)]
choices=[set(p0+p1+p2) for p0 in pairs[0] for p1 in pairs[1] for p2 in pairs[2]]
cov={e:sum(1<<k for k,S in enumerate(choices) if e[0] in S and e[1] in S) for e in cand}
FULL=(1<<len(choices))-1
def Q_of(E):
    Q=nx.Graph(); M=['m0','m1','m2']; Q.add_edges_from([('m0','m1'),('m1','m2'),('m0','m2')])
    for (i,c) in ears:
        for j in range(3):
            if j!=c: Q.add_edge((i,c),M[j])
    Q.add_edges_from(E); return Q
found=0
for k in range(3,int(sys.argv[1])+1):
    for E in itertools.combinations(cand,k):
        m=0
        for e in E: m|=cov[e]
        if m!=FULL: continue
        Q=Q_of(E)
        pl,_=nx.check_planarity(Q)
        if pl:
            found+=1; print('PLANAR',k,E); 
            if found>5: sys.exit()
    print('size',k,'done, planar found',found)
