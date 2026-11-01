# Q* = 중심 삼각형 m1m2m3 + 귀 a_i,b_i (m_j m_k 위) + 순환 짝맞춤 a1b2,a2b3,a3b1. 두 잎 판의 가장 작은 예 후보.
from r05_lib import *
E=[('m1','m2'),('m2','m3'),('m1','m3')]
for c in (1,2,3):
    for s in (1,2,3):
        if s!=c: E+=[('m%d'%c,'a%d'%s),('m%d'%c,'b%d'%s)]
E+=[('a1','b2'),('a2','b3'),('a3','b1')]
Q=nx.Graph(E); T1=('a1','a2','a3'); T2=('b1','b2','b3')
G=assemble(Q,[T1,T2])
print('Q 점/변',Q.number_of_nodes(),Q.number_of_edges(),'chi(Q)',chi(Q),'평면?',nx.check_planarity(Q)[0])
print('G 점/변',G.number_of_nodes(),G.number_of_edges(),'chi(G)',chi(G))
print('변 하나 지워 평면이 되는 변:',[e for e in Q.edges() if nx.check_planarity(nx.restricted_view(Q,[],[e]))[0]])
# 변 하나 지운 Q-e 에서 두 잎 성질이 남는가 (극소성)
keep=[]
for e in Q.edges():
    Qe=nx.Graph(Q); Qe.remove_edge(*e)
    cols=colorings(Qe,4); M=masks(Qe,cols,[T1,T2])
    if M[T1]&M[T2]==0: keep.append(e)
print('지워도 두 잎 성질이 남는 변:',keep)
