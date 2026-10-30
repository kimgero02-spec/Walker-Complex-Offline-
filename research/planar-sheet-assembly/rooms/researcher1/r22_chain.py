from r22_star import *
import networkx as nx, sys
def gamma(m):
    x=lambda i,j:'x%d_%d'%(i,j)
    E=[]
    for i in range(1,m+1):
        Q=['w']+[x(i,j) for j in range(1,5)]
        miss=set()
        if i>1: miss.add(frozenset(('w',x(i,1))))
        if i<m: miss.add(frozenset(('w',x(i,2))))
        E+=[e for e in itertools.combinations(Q,2) if frozenset(e) not in miss]
    E+=[(x(i,2),x(i+1,1)) for i in range(1,m)]
    P1=[];P2=[]
    for i in range(1,m+1):
        if i==1 or i==m:
            t= 2 if i==1 else 1   # end vertex
            o=[j for j in range(1,5) if j!=t]
            P1+=[('w',x(i,j)) for j in o]+[(x(i,t),x(i,j)) for j in o]
            P2+=list(itertools.combinations([x(i,j) for j in o],2))
        else:
            P1+=[(x(i,1),x(i,2)),('w',x(i,3)),('w',x(i,4))]
            P2+=[e for e in itertools.combinations([x(i,j) for j in range(1,5)],2) if set(e)!={x(i,1),x(i,2)}]
    for i in range(1,m):
        (P2 if i==m-1 and m>2 else P1).append((x(i,2),x(i+1,1)))
    if m==2: pass
    V1={'w',x(1,2),x(m,1)}|{x(i,1) for i in range(2,m)}
    return E,P1,P2,V1
for m in range(2,int(sys.argv[1])+1):
    E,P1,P2,V1=gamma(m)
    fs=lambda L:{frozenset(e) for e in L}
    assert fs(E)==fs(P1)|fs(P2) and not (fs(P1)&fs(P2))
    g1=nx.Graph(P1); g2=nx.Graph(P2); G=nx.Graph(E)
    adj=edges_to_adj(E)
    V2=set(G)-V1
    own=all((e<=V1 and e in fs(P1)) or (e<=V2 and e in fs(P2)) or (not e<=V1 and not e<=V2) for e in fs(E))
    print(m,len(G),len(E),'P1 bip',nx.is_bipartite(g1),'P1 pl',nx.check_planarity(g1)[0],'P2 pl',nx.check_planarity(g2)[0],
          'chiP2',chi(edges_to_adj(P2)),'own',own,'chiG',chi(adj), 'viol', star_violation(adj) if m<=int(sys.argv[2]) else '-')
