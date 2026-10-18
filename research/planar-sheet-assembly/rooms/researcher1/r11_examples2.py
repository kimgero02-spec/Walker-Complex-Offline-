import networkx as nx, itertools
from r11_inverse import build_manual, realize
def show(name, pieces):
    M, Mc, A = build_manual(pieces)
    N=A.number_of_nodes()
    print(name, 'N=',N,'A complete:',A.number_of_edges()==N*(N-1)//2,
          '|V(M)|=',M.number_of_nodes(),'M==Mc:',M.number_of_edges()==Mc.number_of_edges(),
          'Mc planar:',nx.check_planarity(Mc)[0])
    for mode,G in (('circ',Mc),('full',M)):
        r=realize(G,mode,maxW=4)
        print('   re-recognize',mode,sorted({(x[1],x[2]) for x in r}), all(x[3] and x[4] for x in r))
V=range(4)
show('Ex1.3 K4', [(list(V),[(0,1),(1,3),(3,2),(2,0)]),(list(V),[(0,3),(3,1),(1,2),(2,0)])])
K5me=[e for e in itertools.combinations(range(5),2) if e!=(3,4)]
show('K5 = (K5-e)+K2 (s=3)', [(list(range(5)),K5me),([3,4],[(3,4)])])
show('K4 + pendant star', [(list(range(4)),list(itertools.combinations(range(4),2))),([0],[]),([0],[])])
