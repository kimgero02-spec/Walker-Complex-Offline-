# 별 둘 (색 2,3 은 별 중심 m2,m3, 색 1 은 별 아님 -> 축약하면 {a2,a3}x{b2,b3} 완전) + 극소 B 각각의 쿠라토프스키 증인
import networkx as nx, itertools
exec(open('r05_skeleton.py').read().split("C={c:minimal_covers")[0].replace("print('극소 B:',Bmin)",""))
base=[('m2','a1'),('m2','a3'),('m2','b1'),('m2','b3'),('m3','a1'),('m3','a2'),('m3','b1'),('m3','b2')]
base+=[('a%d'%i,'b%d'%j) for i in (2,3) for j in (2,3)]
for B in Bmin:
    G=nx.Graph(base+list(B)); ok,K=nx.check_planarity(G,counterexample=True)
    d=[v for v in K if K.degree(v)>=3]
    print(B,'planar' if ok else ('K5' if len(d)==5 else 'K33'), sorted(K.edges()))
