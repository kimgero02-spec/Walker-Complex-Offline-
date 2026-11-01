# 구성 후보: 삼각형 abc + 귀 6개 (T1=x,y,z / T2=u,v,w 를 변 ab,bc,ca 에) + T1-T2 사이 변 B.
# 충분조건: 모든 p⊂T1, q⊂T2 (쌍) 에 대해 Q/p/q ⊇ K5 (= w1,w2,a,b,c) 이면 두 잎 판이 성립.
import itertools, networkx as nx
from r05_lib import *
base=[('a','b'),('b','c'),('c','a')]
T1=('x','y','z'); T2=('u','v','w')
side={'x':'ab','y':'bc','z':'ca','u':'ab','v':'bc','w':'ca'}
for t,s in side.items(): base+= [(t,s[0]),(t,s[1])]
cand=[(p,q) for p in T1 for q in T2 if side[p]!=side[q]]
def N2(B):
    for P in itertools.combinations(T1,2):
        for R in itertools.combinations(T2,2):
            if not any((p,q) in B for p in P for q in R): return False
    return True
cnt=0; planar=[]
for r in range(1,len(cand)+1):
    for B in itertools.combinations(cand,r):
        B=set(B)
        if not N2(B): continue
        cnt+=1
        Q=nx.Graph(base+list(B))
        if nx.check_planarity(Q)[0]: planar.append(B)
print('N2 B 수',cnt,'평면',len(planar))
