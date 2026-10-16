import networkx as nx, itertools
def chi(G):
    nodes=sorted(G.nodes(),key=lambda v:-G.degree(v))
    for k in range(1,len(nodes)+1):
        col={}
        def bt(i):
            if i==len(nodes): return True
            v=nodes[i]; used={col[w] for w in G[v] if w in col}
            for c in range(min(k,max(col.values(),default=-1)+2)):
                if c not in used:
                    col[v]=c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return k
    return 0
def partitions(S):
    if not S: yield []; return
    f,rest=S[0],S[1:]
    for p in partitions(rest):
        for i in range(len(p)): yield p[:i]+[[f]+p[i]]+p[i+1:]
        yield [[f]]+p
def chi_pi(P,pi):
    # coloring whose restriction to S has exactly partition pi
    for B in pi:
        for a,b in itertools.combinations(B,2):
            if P.has_edge(a,b): return float('inf')
    Q=P.copy(); reps=[]
    for B in pi:
        r=B[0]
        for x in B[1:]: Q=nx.contracted_nodes(Q,r,x,self_loops=False)
        reps.append(r)
    Q=nx.Graph(Q); Q.add_edges_from(itertools.combinations(reps,2))
    return chi(Q)
def report(name,pieces,S):
    G=nx.compose_all(pieces)
    prof={str(pi):[chi_pi(P,pi) for P in pieces] for pi in partitions(list(S))}
    formula=min(max(v) for v in prof.values())
    print(name,'chi(P_k)=',[chi(P) for P in pieces],'planar=',[nx.check_planarity(P)[0] for P in pieces],
          'chi(G)=',chi(G),'formula=',formula,'G planar=',nx.check_planarity(G)[0])
    for k,v in prof.items(): print('   ',k,v)
def diamond(a,b,x,y): # K4 - ab
    return nx.Graph([(a,x),(a,y),(b,x),(b,y),(x,y)])
# E1
report('E1 K4-uv + K2',[diamond('u','v','x','y'),nx.Graph([('u','v')])],['u','v'])
# E2 Hajos-type non-edge
P2=diamond('a','v','p','q'); P2.add_edge('u','a')
report('E2 eq vs neq',[diamond('u','v','x','y'),P2],['u','v'])
# E3 two eq-forcing
report('E3 eq vs eq',[diamond('u','v','x','y'),diamond('u','v','x2','y2')],['u','v'])
# E4 3-sum K_{1,1,3} + K3 = K5
P1=nx.Graph([('d','e')]+[(h,s) for h in 'de' for s in 'abc'])
report('E4 K113+K3',[P1,nx.complete_graph('abc')],['a','b','c'])
# E5 center independent set + K2 pieces -> K5 (not single-pair; just chi)
n=5; C=nx.empty_graph(range(n)); pcs=[C]+[nx.Graph([(i,j)]) for i,j in itertools.combinations(range(n),2)]
G=nx.compose_all(pcs); print('E5 chi pieces max',max(chi(P) for P in pcs),'chi(G)',chi(G))
# E6 path-type S={a,b,c} with b adj a,c in both, ac non-edge
Q1=diamond('a','c','x','y'); Q1.add_edges_from([('b','a'),('b','c')])
Q2=diamond('z','a','p','q'); Q2.add_edges_from([('c','z'),('b','a'),('b','c')])
report('E6 S=path a-b-c',[Q1,Q2],['a','b','c'])
