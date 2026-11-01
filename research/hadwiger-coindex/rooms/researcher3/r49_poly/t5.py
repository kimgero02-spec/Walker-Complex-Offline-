# 조인 (움브랄 곱) 과 클리크 합 공식 확인
from lib import *
import networkx as nx
def indep_part_counts(B):
    V=list(B); cnt={}
    def rec(i,blocks):
        if i==len(V): cnt[len(blocks)]=cnt.get(len(blocks),0)+1; return
        v=V[i]
        for b in blocks:
            if all(not B.has_edge(v,w) for w in b): b.append(v); rec(i+1,blocks); b.pop()
        blocks.append([v]); rec(i+1,blocks); blocks.pop()
    rec(0,[]); return cnt
G1=nx.relabel_nodes(nx.cycle_graph(5),lambda v:'a%d'%v); G2=nx.relabel_nodes(nx.wheel_graph(5),lambda v:'b%d'%v)
J=nx.compose(G1,G2); J.add_edges_from((u,v) for u in G1 for v in G2)
a=indep_part_counts(G1); b=indep_part_counts(G2)
print('join C5+W4 umbral:',all(count_colorings(J,x)==sum(a[i]*b[j]*ff(x,i+j) for i in a for j in b) for x in range(0,10)))
print('K6=K3+K3 check:', [count_colorings(nx.complete_graph(6),x) for x in (5,6)], 'umbral K_{n}: a=b={3:1} ->', [ff(x,6) for x in (5,6)])
# 클리크 합: 정팔면체 와 W5 를 삼각형 따라 붙임
O=nx.octahedral_graph(); W=nx.relabel_nodes(nx.wheel_graph(6),lambda v:v+100)
tri_O=[0,1,2]; assert all(O.has_edge(u,v) for u in tri_O for v in tri_O if u<v)
tri_W=[100,101,102]
S=nx.relabel_nodes(W,{100:0,101:1,102:2}); C=nx.compose(O,S)
print('clique sum oct ⊕_K3 W5:',all(count_colorings(C,x)*ff(x,3)==count_colorings(O,x)*count_colorings(W,x) for x in range(0,9)))
