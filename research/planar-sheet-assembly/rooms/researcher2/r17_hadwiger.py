# R17 망상꾼: 역조립 해드위거 수 h_M 의 정선한 예 확인 (근거 아님, 구성 확인용)
import networkx as nx, itertools as it
def Mcirc(N, pieces):
    X=nx.Graph(); F={v:[] for v in range(N)}
    for k,P in enumerate(pieces):
        for v in P.nodes(): F[v].append(k); X.add_node(('c',v,k))
        for u,v in P.edges(): X.add_edge(('c',u,k),('c',v,k))
    for v in range(N):
        if len(F[v])>=2:
            for k in F[v]: X.add_edge(('w',v),('c',v,k))
    return X
def contract_check(X,N):
    # 흰 별 수축 -> K_N 확인
    Y=nx.Graph(); 
    for a,b in X.edges(): 
        if a[1]!=b[1]: Y.add_edge(a[1],b[1])
    return nx.is_isomorphic(Y,nx.complete_graph(N))
pl=lambda G: nx.check_planarity(G)[0]
# nu(5): K5-e + K2
K5e=nx.complete_graph(5); K5e.remove_edge(3,4); e=nx.Graph([(3,4)])
X9=Mcirc(5,[K5e,e]); print('X9',X9.number_of_nodes(),X9.number_of_edges(),sorted(d for _,d in X9.degree()),contract_check(X9,5))
P=nx.petersen_graph(); u,v=list(P.edges())[0]
Pc=nx.contracted_nodes(P,u,v,self_loops=False); print('P/e',Pc.number_of_nodes(),Pc.number_of_edges(),sorted(d for _,d in Pc.degree()))
# nu(6): K_{1,1,4} on all + K4 on 2..5
P1=nx.complete_graph(6); P1.remove_edges_from(it.combinations(range(2,6),2)); P2=nx.complete_graph(range(2,6))
X=Mcirc(6,[P1,P2]); print('nu6',X.number_of_nodes(),pl(P1),pl(P2),contract_check(X,6))
# nu(7): K2 v (5 isolated + edge 23) ; K5 - 23 on 2..6
P1=nx.complete_graph(7); P1.remove_edges_from([e for e in it.combinations(range(2,7),2) if e!=(2,3)])
P2=nx.complete_graph(range(2,7)); P2.remove_edge(2,3)
X=Mcirc(7,[P1,P2]); print('nu7',X.number_of_nodes(),pl(P1),pl(P2),contract_check(X,7))
# nu(8): K2 v (perfect matching on 2..7) ; octahedron
L=[(2,3),(4,5),(6,7)]
P1=nx.complete_graph(8); P1.remove_edges_from([e for e in it.combinations(range(2,8),2) if e not in L])
P2=nx.complete_graph(range(2,8)); P2.remove_edges_from(L)
X=Mcirc(8,[P1,P2]); print('nu8',X.number_of_nodes(),pl(P1),pl(P2),contract_check(X,8))
# K7 minus Hamilton path planar?  (thickness(K9)=3 이면 비평면이어야)
Q=nx.complete_graph(7); Q.remove_edges_from([(i,i+1) for i in range(6)]); print('K7-P7 planar',pl(Q))
K2P7=nx.complete_graph(9); K2P7.remove_edges_from([e for e in it.combinations(range(2,9),2) if e[1]-e[0]!=1]); print('K2vP7 planar',pl(K2P7))
# Petersen: M°(C5, pentagram) == Petersen with spokes subdivided
C1=nx.cycle_graph(5); C2=nx.Graph([(i,(i+2)%5) for i in range(5)])
Y=Mcirc(5,[C1,C2]); S=nx.Graph(P)
for i in range(5): S.remove_edge(i,i+5); S.add_edge(i,('s',i)); S.add_edge(('s',i),i+5)
print('M°(C5,C5*) ~ spoke-subdivided Petersen', nx.is_isomorphic(Y,S), contract_check(Y,5))
