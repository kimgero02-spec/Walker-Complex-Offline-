from lib import *
import networkx as nx
def glue(B1,B2,H):
    G=nx.Graph(); G.add_nodes_from(B1); G.add_nodes_from(B2)
    G.add_edges_from(B1.edges()); G.add_edges_from(B2.edges()); G.add_edges_from(H); return G
# (A) 일반 공식 확인: 작은 예들, x=0..7
tests=[]
B1=nx.relabel_nodes(nx.wheel_graph(6),lambda v:'a%d'%v); B2=nx.relabel_nodes(nx.complete_graph(4),lambda v:'b%d'%v)
H=[('a1','b0'),('a2','b0'),('a2','b1'),('a3','b2'),('a0','b3'),('a4','b1')]
tests.append(('W5|K4',B1,['a0','a1','a2','a3','a4'],B2,['b0','b1','b2','b3'],H))
P4=nx.relabel_nodes(nx.path_graph(4),lambda v:'a%d'%v); E=nx.Graph([('b0','b1')])
tests.append(('P4|K2',P4,['a0','a3'],E,['b0','b1'],[('a0','b0'),('a3','b1')]))
for name,B1,W1,B2,W2,H in tests:
    G=glue(B1,B2,H)
    ok=all(count_colorings(G,x)==bilinear(B1,W1,B2,W2,H,x) for x in range(0,8))
    print(name,'formula P_G = a1^T M a2 at x=0..7:',ok)
# (B) 결정적 반례: P4 (끝점 경계) vs K_{1,3} (두 잎 경계), 같은 H = 2-매칭, B2=K2
S=nx.Graph([('o','l1'),('o','l2'),('o','l3')])
G1=glue(P4,E,[('a0','b0'),('a3','b1')]); G2=glue(S,E,[('l1','b0'),('l2','b1')])
for x in range(2,6):
    print('x',x,'P_B1',count_colorings(P4,x),count_colorings(S,x),'P_G',count_colorings(G1,x),count_colorings(G2,x))
