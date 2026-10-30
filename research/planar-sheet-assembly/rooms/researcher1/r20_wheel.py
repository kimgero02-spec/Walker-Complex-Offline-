# R20: check (support only) the general M(W_n) decomposition: x=v1,y=v2,Y={v0,v2}
import networkx as nx, itertools, sys
def colorable(G,k):
    nodes=sorted(G.nodes(),key=lambda v:-G.degree(v)); col={}
    def bt(i):
        if i==len(nodes): return True
        v=nodes[i]; used={col[w] for w in G[v] if w in col}
        for c in range(k):
            if c not in used:
                col[v]=c
                if bt(i+1): return True
                del col[v]
        return False
    return bt(0)
def chi(G):
    k=1
    while not colorable(G,k): k+=1
    return k
def build(n):
    H=nx.Graph(); rim=[f'v{i}' for i in range(1,n+1)]
    for i in range(1,n+1):
        H.add_edge('v0',f'v{i}'); H.add_edge(f'v{i}',f'v{i%n+1}')
    G=H.copy(); S=[]
    for a,b in H.edges():
        S.append(('u'+a[1:],b)); S.append(('u'+b[1:],a))
    G.add_edges_from(S); A=[('z','u'+v[1:]) for v in H.nodes()]; G.add_edges_from(A)
    Y={'v0','v2'}
    P1=nx.Graph(); P1.add_edges_from(A); P1.add_edge('v1','v2'); P1.add_edges_from([e for e in S if e[1] not in Y])
    P2=nx.Graph(); P2.add_edges_from([e for e in H.edges() if set(e)!={'v1','v2'}]); P2.add_edges_from([e for e in S if e[1] in Y])
    return H,G,P1,P2
for n in [5,7,9,11]:
    H,G,P1,P2=build(n)
    assert set(map(frozenset,G.edges()))==set(map(frozenset,P1.edges()))|set(map(frozenset,P2.edges()))
    V1={'z','v1'}|{f'u{i}' for i in range(n+1)}; V2=set(G)-V1
    own=all(P1.has_edge(*e) for e in G.subgraph(V1).edges()) and all(P2.has_edge(*e) for e in G.subgraph(V2).edges())
    print(n,'E',G.number_of_edges(),P1.number_of_edges(),P2.number_of_edges(),'P1 bip',nx.is_bipartite(P1),'pl',nx.check_planarity(P1)[0],
          'P2 chi',chi(P2),'pl',nx.check_planarity(P2)[0],'own',own,'chiG',chi(G) if n<=9 else '-','omega',max(map(len,nx.find_cliques(G))))
    if n==7:
        print(' G-v3 4-col', colorable(G.subgraph(set(G)-{'v3'}),4))
