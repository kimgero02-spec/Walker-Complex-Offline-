from r48_at import *
import networkx as nx, time, sys
exec(open('r48_t5.py').read().split("def one_sided")[0])
print('gadget G: degeneracy',max(nx.core_number(G).values()),'|E|',G.number_of_edges())
# 두 정팔면체 + 3-정칙 교차 (원순열 연결 i -> i, i+1, i+3 mod 6 류)
O=nx.octahedral_graph()
G2=nx.Graph()
G2.add_edges_from(O.edges()); G2.add_edges_from((u+6,v+6) for u,v in O.edges())
for i in range(6):
    for s in (0,1,3): G2.add_edge(i,6+(i+s)%6)
print('G2 degrees',set(dict(G2.degree()).values()),'|E|',G2.number_of_edges(),'degeneracy',max(nx.core_number(G2).values()))
E2=list(G2.edges())
for k in (4,5): print('G2 chi<=%d'%k, proper_coloring(12,E2,[list(range(k))]*12) is not None)
# AT<=5 시험: t<=4, sum 42 -> 여섯 개 3, 여섯 개 4 ; 시트별 한 패턴씩 몇 개
import itertools
t0=time.time(); found=None; tried=0
for T in [(0,1,2,6,7,8),(0,1,2,9,10,11),(0,2,4,7,9,11),(0,1,6,7,2,8)]:
    t=[3 if v in T else 4 for v in range(12)]
    c=coef(12,E2,t); tried+=1
    print('t=3 on',T,'coef',c, round(time.time()-t0,1)); 
    if c: found=T; break
