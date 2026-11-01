# 구성 탐색(지정 설계 + 무작위 변 추가): 평면 Q, T1={x,y,z}, T2={p,q,r}, 4-색칠에서 둘 다 비무지개 불가?
import random, sys
from r04_lib import *
random.seed(int(sys.argv[1]))
T1=('x','y','z'); T2=('p','q','r')
base=[('a','b'),('b','c'),('a','c'),('x','b'),('x','c'),('y','a'),('y','c'),('z','a'),('z','b'),
      ('p','x'),('p','b'),('q','y'),('q','c'),('r','z'),('r','a')]
def ok(Q):
    return col_ok(Q,[T1,T2]) is None
extra=['e1','e2','e3']
best=0
for it in range(int(sys.argv[2])):
    Q=nx.Graph(base)
    V=list(Q.nodes())+extra[:random.randint(0,3)]
    E=[e for e in itertools.combinations(V,2) if not (set(e)<=set(T1) or set(e)<=set(T2))]
    random.shuffle(E)
    for u,v in E:
        if Q.has_edge(u,v) or random.random()<0.3: continue
        Q.add_edge(u,v)
        if not nx.check_planarity(Q)[0] or chi(Q)>3: Q.remove_edge(u,v)
    if chi(Q)==3 and ok(Q):
        print('FOUND', sorted(Q.edges())); break
print('it', it)
