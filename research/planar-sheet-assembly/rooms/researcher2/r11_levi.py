# R11 망상꾼: 매뉴얼 그래프 M, 압축 M° 의 구성과 인식 (작은 예 확인용)
import itertools, networkx as nx

def manual(pieces):
    """pieces: list of (Vk, Ek). returns (Mo, M, N-graph)"""
    F = {}
    for k,(Vk,Ek) in enumerate(pieces):
        for v in Vk: F.setdefault(v,[]).append((v,k))
    Mo = nx.Graph()
    for v,fs in F.items(): Mo.add_nodes_from(fs)
    mu = {}
    for k,(Vk,Ek) in enumerate(pieces):
        for (u,v) in Ek:
            Mo.add_edge((u,k),(v,k)); e=frozenset((u,v)); mu[e]=mu.get(e,0)+1
    for v,fs in F.items():
        if len(fs)>=2:
            for x in fs: Mo.add_edge(x,(v,'*'))
    M = Mo.copy()
    for e,m in mu.items():
        u,v = tuple(e)
        if m>=2: M.add_edge((u,'*'),(v,'*'))
    G = nx.Graph(); G.add_nodes_from(F)
    G.add_edges_from(tuple(e) for e in mu)
    return Mo, M, G, mu

def is_complete(G):
    n=G.number_of_nodes(); return G.number_of_edges()==n*(n-1)//2

def recognize(X, mode):
    """mode 'Mo' or 'M'. brute force over white sets W. returns list of (W,N)"""
    sols=[]
    V=list(X.nodes())
    for r in range(0,len(V)+1):
        for W in itertools.combinations(V,r):
            Ws=set(W); B=[x for x in V if x not in Ws]
            if mode=='Mo' and any(X.has_edge(a,b) for a,b in itertools.combinations(W,2)): continue
            ok=True
            for w in W:
                nb=[x for x in X[w] if x not in Ws]
                if len(nb)<2: ok=False;break
            if not ok: continue
            if any(sum(1 for y in X[b] if y in Ws)>1 for b in B): continue
            XB=X.subgraph(B); comp={}
            for i,c in enumerate(nx.connected_components(XB)):
                for x in c: comp[x]=i
            if any(len({comp[x] for x in X[w] if x not in Ws})<len([x for x in X[w] if x not in Ws]) for w in W): continue
            if any(not nx.check_planarity(XB.subgraph(c))[0] for c in nx.connected_components(XB)): continue
            cls={}
            for w in W:
                cls[w]=w
                for x in X[w]:
                    if x not in Ws: cls[x]=w
            for b in B: cls.setdefault(b,b)
            Q=nx.Graph(); Q.add_nodes_from(set(cls.values())); cnt={}
            for a,b in XB.edges():
                e=frozenset((cls[a],cls[b])); cnt[e]=cnt.get(e,0)+1; Q.add_edge(cls[a],cls[b])
            if not is_complete(Q): continue
            if mode=='M':
                want={frozenset(e) for e,c in cnt.items() if c>=2 and all(z in Ws for z in e)}
                have={frozenset(e) for e in itertools.combinations(W,2) if X.has_edge(*e)}
                if want!=have: continue
            sols.append((W,Q.number_of_nodes()))
    return sols

if __name__=='__main__':
    # 작은 예
    for n in range(2,7):
        X=nx.complete_graph(n); print('K',n,'Mo',[s[1] for s in recognize(X,'Mo')],'M',[s[1] for s in recognize(X,'M')])
    for m in range(3,13):
        X=nx.cycle_graph(m); print('C',m,'Mo',sorted({s[1] for s in recognize(X,'Mo')}),'M',sorted({s[1] for s in recognize(X,'M')}))
    X=nx.complete_bipartite_graph(3,3); print('K33',recognize(X,'Mo'),recognize(X,'M'))
    X=nx.petersen_graph(); print('Petersen',recognize(X,'Mo'),recognize(X,'M'))
    # 예 8.4 의 M (K_2 두 장)
    Mo,M,G,mu=manual([(['u','v'],[('u','v')]),(['u','v'],[('u','v')])])
    print('Ex8.4: M as X: Mo-recog',recognize(nx.convert_node_labels_to_integers(M),'Mo'),'M-recog',[s[1] for s in recognize(nx.convert_node_labels_to_integers(M),'M')])
    # 파노 삼각형
    fano=[(0,1,3),(1,2,4),(2,3,5),(3,4,6),(4,5,0),(5,6,1),(6,0,2)]
    Mo,M,G,mu=manual([(list(b),list(itertools.combinations(b,2))) for b in fano])
    print('Fano: |V|',Mo.number_of_nodes(),'deg',set(dict(Mo.degree()).values()),'A=K7',is_complete(G) and G.number_of_nodes()==7,'M==Mo',nx.utils.graphs_equal(M,Mo),
          'conn',nx.node_connectivity(Mo),'planar',nx.check_planarity(Mo)[0],'girth',min(len(c) for c in nx.minimum_cycle_basis(Mo)),'beta1',Mo.number_of_edges()-Mo.number_of_nodes()+1)
    # K7 = C7(1)+C7(2)+C7(3)
    hc=[(list(range(7)),[(i,(i+s)%7) for i in range(7)]) for s in (1,2,3)]
    Mo2,M2,G2,_=manual(hc)
    print('3 Ham cycles: |V|',Mo2.number_of_nodes(),'deg',set(dict(Mo2.degree()).values()),'conn',nx.node_connectivity(Mo2),'iso to Fano Mo',nx.is_isomorphic(Mo,Mo2),'girth',min(len(c) for c in nx.minimum_cycle_basis(Mo2)))
    # PG(2,3) K4 pieces: difference set {0,1,3,9} mod 13
    pg=[tuple(sorted(((x+i)%13) for x in (0,1,3,9))) for i in range(13)]
    Mo3,M3,G3,mu3=manual([(list(b),list(itertools.combinations(b,2))) for b in pg])
    print('PG(2,3): |V|',Mo3.number_of_nodes(),'deg',set(dict(Mo3.degree()).values()),'A=K13',is_complete(G3),'mu',set(mu3.values()),'conn',nx.node_connectivity(Mo3))
    # near-pencils N=3,4,5
    for N in (3,4,5):
        big=list(range(N-1)); ps=[(big,list(itertools.combinations(big,2)))]+[([N-1,i],[(N-1,i)]) for i in big]
        Mo4,M4,G4,mu4=manual(ps); print('near-pencil N',N,'pieces',len(ps),'A complete',is_complete(G4),'mu',set(mu4.values()),'|V(Mo)|',Mo4.number_of_nodes())
    # 전압 그래프: Z7 lift of K4 (apex w + triangle x0,x1,x3), spoke voltages
    L=nx.Graph()
    for g in range(7):
        for a,b in [(0,1),(1,3),(0,3)]: L.add_edge(('x',a,g),('x',b,g))
        for a in (0,1,3): L.add_edge(('w',(a+g)%7),('x',a,g))
    print('Z7-lift of K4 iso Fano Mo:',nx.is_isomorphic(L,Mo))
