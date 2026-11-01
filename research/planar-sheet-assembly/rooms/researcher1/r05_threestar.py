# 별 셋 (E6 의 Q 가 바로 이 꼴) + N2 가 강제하는 세 변 (쌍 (12),(13),(23) 에서 하나씩) 8 경우의 K33 증인
import networkx as nx, itertools
H0=[]
for c in (1,2,3):
    for s in (1,2,3):
        if s!=c: H0+= [('m%d'%c,'a%d'%s),('m%d'%c,'b%d'%s)]
def describe(K):
    d=[v for v in K if K.degree(v)==3]
    # 가지점끼리의 경로
    paths=[]
    for u in d:
        for w in K[u]:
            path=[u,w]; prev=u
            while path[-1] not in d:
                nxt=[x for x in K[path[-1]] if x!=prev][0]; prev=path[-1]; path.append(nxt)
            if str(path[0])<str(path[-1]): paths.append('-'.join(path))
    H=nx.Graph([(p.split('-')[0],p.split('-')[-1]) for p in paths])
    X,Y=nx.bipartite.sets(H)
    return sorted(X),sorted(Y),paths

for e12,e13,e23 in itertools.product((('a1','b2'),('a2','b1')),(('a1','b3'),('a3','b1')),(('a2','b3'),('a3','b2'))):
    B=[e12,e13,e23]; G=nx.Graph(H0+B); ok,K=nx.check_planarity(G,counterexample=True)
    X,Y,P=describe(K); print('B=',' '.join(a+b for a,b in B),'| 쪽',X,Y,'| 경로',', '.join(P))
