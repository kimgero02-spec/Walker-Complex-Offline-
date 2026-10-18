# R06: 잎 셋 평면판 예의 직접 확인 (Q 평면, chi(Q)=3, 삼중쌍 독립, G=Q+잎3 의 chi=5)
import itertools, networkx as nx
from r05_lib import has_col, colorings
def build(ears, E):
    Q=nx.Graph(); M=['m0','m1','m2']; Q.add_edges_from([('m0','m1'),('m1','m2'),('m0','m2')])
    for v,c in ears.items():
        for j in range(3):
            if j!=c: Q.add_edge(v,M[j])
    Q.add_edges_from(E); return Q
def check(name, ears, E, Ts):
    Q=build(ears,E)
    pl,emb=nx.check_planarity(Q)
    G=Q.copy()
    for i,T in enumerate(Ts):
        assert not any(Q.has_edge(x,y) for x,y in itertools.combinations(T,2))
        G.add_edge(('p',i),('q',i))
        for t in T: G.add_edge(('p',i),t); G.add_edge(('q',i),t)
    cols=colorings(Q,4)
    bad=[c for c in cols if all(len({c[t] for t in T})<3 for T in Ts)]
    print(name,'|V(Q)|=',Q.number_of_nodes(),'|E(Q)|=',Q.number_of_edges(),'planar',pl,
          'chi(Q)<=3',has_col(Q,3),'not2',not has_col(Q,2),
          '#4col(Q,정규화)',len(cols),'#all-nonrainbow',len(bad),
          'G 4col?',has_col(G,4),'G 5col?',has_col(G,5))
    # 잎 둘만으로는 부족함(정리 2L 일관성 점검)
    for S in itertools.combinations(Ts,2):
        print('   pair',S,'all-nonrainbow 4-col exist:',any(all(len({c[t] for t in T})<3 for T in S) for c in cols))
    if pl:
        print('   faces:'); seen=set()
        for u,v in emb.edges():
            if (u,v) in seen: continue
            f=emb.traverse_face(u,v,mark_half_edges=seen); print('    ',f)
# 예 A (12점, 삼중쌍 서로소)
ears={'a0':0,'a1':1,'a2':2,'b0':0,'b1':1,'b2':2,'c0':0,'c1':1,'c2':2}
E=[('a0','b1'),('a0','b2'),('a1','c0'),('a1','c2')]
check('A',ears,E,[('a0','a1','a2'),('b0','b1','b2'),('c0','c1','c2')])
# 예 B (10점, T1,T2 가 두 점 공유)
ears={'a0':0,'a1':1,'a2':2,'b1':1,'b2':2,'c0':0,'c2':2}
check('B',ears,E,[('a0','a1','a2'),('b1','b2','c0'),('c0','c2','b1')])
