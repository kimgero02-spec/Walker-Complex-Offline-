# Q 의 평면판 찾기 (구성 탐색: p,q,r 가 보는 귀 쌍 27가지)
import itertools, networkx as nx
from r03_chi import chi, g, union, K113, colorings
base=[('a','b'),('b','c'),('c','a'),('x','b'),('x','c'),('y','a'),('y','c'),('z','a'),('z','b')]
pairs=list(itertools.combinations('xyz',2))
for P1,P2,P3 in itertools.product(pairs,repeat=3):
    E=base+[('p','a'),('p','b')]+[('p',t) for t in P1]+[('q','a'),('q','c')]+[('q',t) for t in P2]+[('r','b'),('r','c')]+[('r',t) for t in P3]
    Q=g(E)
    if not nx.check_planarity(Q)[0]: continue
    if chi(Q)>3: continue
    bad=sum(1 for c in colorings(Q,4) if len({c['x'],c['y'],c['z']})<3 and len({c['p'],c['q'],c['r']})<3)
    G=union(Q,K113(('x','y','z'),'h'),K113(('p','q','r'),'k'))
    print(P1,P2,P3,"평면 chi(Q)=",chi(Q),"반례쌍",bad,"chi(G)=",chi(G))
