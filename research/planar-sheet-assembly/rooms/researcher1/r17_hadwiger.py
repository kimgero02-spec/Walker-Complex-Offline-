# R17: 예 확인용 (근거 아님). 교재 정의대로 M, M° 를 짓고, 작은 그래프의 h 를 수축 탐색으로 계산.
import itertools, networkx as nx, sys
def manual(pieces):
    # pieces: list of (Vset, Elist) ; returns (Mcirc, M, N, mu)
    V=set().union(*[set(p[0]) for p in pieces])
    F={v:[(v,k) for k,p in enumerate(pieces) if v in p[0]] for v in V}
    Mc=nx.Graph(); Mc.add_nodes_from(x for v in V for x in F[v])
    mu={}
    for k,(Vs,Es) in enumerate(pieces):
        for u,v in Es:
            Mc.add_edge((u,k),(v,k)); e=frozenset((u,v)); mu[e]=mu.get(e,0)+1
    W=[v for v in V if len(F[v])>=2]
    for v in W:
        for x in F[v]: Mc.add_edge(x,(v,'*'))
    M=Mc.copy()
    for a,b in itertools.combinations(W,2):
        if mu.get(frozenset((a,b)),0)>=2: M.add_edge((a,'*'),(b,'*'))
    return Mc,M,mu
def beta1(G): return G.number_of_edges()-G.number_of_nodes()+nx.number_connected_components(G)
def has_Kt_minor(G,t):
    G=nx.convert_node_labels_to_integers(G)
    seen=set()
    def key(H): return nx.weisfeiler_lehman_graph_hash(H,iterations=4)
    stack=[G]
    while stack:
        H=stack.pop()
        if H.number_of_nodes()<t or H.number_of_edges()<t*(t-1)//2: continue
        if beta1(H)<(t-1)*(t-2)//2: continue
        # delete vertices of degree < t-1 (they can be removed: a K_t model never needs... ) -> 안전하지 않으므로 하지 않음
        if any(len(c)>=t for c in nx.find_cliques(H)): return True
        k=key(H)
        if k in seen: continue   # 해시 충돌 가능: 예 확인용일 뿐
        seen.add(k)
        for a,b in H.edges():
            stack.append(nx.relabel_nodes(nx.contracted_nodes(H,a,b,self_loops=False),lambda x:x))
    return False
def h(G):
    t=1
    while has_Kt_minor(G,t+1): t+=1
    return t
if __name__=='__main__':
    V4=[0,1,2,3]
    ex13=[(V4,[(0,1),(1,3),(3,2),(2,0)]),(V4,[(0,3),(3,1),(1,2),(2,0)])]
    Mc,M,mu=manual(ex13)
    print('ex1.3 Mc',Mc.number_of_nodes(),Mc.number_of_edges(),'b1',beta1(Mc),'h',h(Mc),'| M b1',beta1(M),'h',h(M))
    V5=list(range(5))
    ex15=[(V5,[(0,1),(1,2),(2,3),(3,4),(0,4)]),(V5,[(0,2),(2,4),(4,1),(1,3),(0,3)])]
    Mc,M,mu=manual(ex15); print('ex1.5 Mc',Mc.number_of_nodes(),'b1',beta1(Mc),'h',h(Mc))
    P=nx.petersen_graph(); print('Petersen b1',beta1(P),'h',h(P))
    print('K33 h',h(nx.complete_bipartite_graph(3,3)),'C5 h',h(nx.cycle_graph(5)),'C6 h',h(nx.cycle_graph(6)))
    # nu(6): K6 - P4 planar?
    K6=nx.complete_graph(6); Q=K6.copy(); Q.remove_edges_from([(0,1),(1,2),(2,3)])
    print('K6-P4 planar',nx.check_planarity(Q)[0])
    pieces=[(list(range(6)),list(Q.edges())),([0,1,2,3],[(0,1),(1,2),(2,3)])]
    Mc,M,mu=manual(pieces); print('K6 via (K6-P4,P4): |V(Mc)|',Mc.number_of_nodes(),'b1',beta1(Mc))
    K5=nx.complete_graph(5); Q5=K5.copy(); Q5.remove_edge(0,1)
    Mc,M,mu=manual([(list(range(5)),list(Q5.edges())),([0,1],[(0,1)])]); print('K5 via (K5-e,K2): |V(Mc)|',Mc.number_of_nodes(),'h',h(Mc))
