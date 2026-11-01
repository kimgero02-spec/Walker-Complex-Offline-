# 가젯의 한 결합 성분 H_a: A={p,q,r,p',q',r'} (V1) <-> Q2 (K4, V2)
from lib import *
import networkx as nx
A=['p','q','r','P','Q','R']; Q=['v1','v2','v3','v4']
H=[(a,v) for v in ('v1','v2','v3') for a in ('p','q','r')]+[(a,'v4') for a in ('P','Q','R')]
BA=nx.Graph([('p','q'),('p','r'),('q','r'),('P','q'),('P','r'),('Q','p'),('Q','r'),('R','p'),('R','q')])
BQ=nx.complete_graph(Q)
P1=list(set_partitions(A)); P2=list(set_partitions(Q))
for x in (6,10**6+3):
    M=[[M_entry(pi,rho,H,x) for rho in P2] for pi in P1]
    print('x',x,'full M rank',rank_mod(M),'of',len(P1),'x',len(P2))
def indep(B,p): return all(not B.has_edge(u,v) for b in p for u in b for v in b if u!=v)
S1=[p for p in P1 if indep(BA,p)]; S2=[p for p in P2 if indep(BQ,p)]
for x in (6,10**6+3):
    M=[[M_entry(pi,rho,H,x) for rho in S2] for pi in S1]
    print('x',x,'effective (indep) rank',rank_mod(M),'support sizes',len(S1),len(S2))
