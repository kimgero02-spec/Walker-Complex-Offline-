from surf import Manual
import networkx as nx
def info(name,Mn):
    print("%-30s V=%d E=%d b=%d chi=%d orient=%s planarG=%s H-simple=%s"%(name,Mn.G.number_of_nodes(),Mn.G.number_of_edges(),
        Mn.b,Mn.chi,Mn.orientable(),nx.check_planarity(Mn.G)[0], nx.Graph(Mn.H).number_of_edges()==Mn.H.number_of_edges()))
P0=['u1','m1','w1','g1','u2','m2','w2','g2']
Y2=Manual({0:P0,1:['u1','m1','w1','p','w2','m2','u2','q']},
          [(0,1,['u1','m1','w1']),(0,1,['u2','m2','w2'])],
          {0:[('u1','z'),('z','u2')],1:[('u1','y'),('y','w1')]})
info("Y2 (r2)",Y2)
# H-simple variant: split Q along arc c = p c1 q
for q2int,lab in [([('w2','x'),('x','u2')],"Q2 inner x~w2,u2"),([('p','x'),('x','u2')],"Q2 inner x~p,u2"),([('w2','x'),('x','q')],"Q2 inner x~w2,q")]:
    V=Manual({0:P0,1:['u1','m1','w1','p','c1','q'],2:['p','w2','m2','u2','q','c1']},
         [(0,1,['u1','m1','w1']),(0,2,['u2','m2','w2']),(1,2,['p','c1','q'])],
         {0:[('u1','z'),('z','u2')],1:[('u1','y'),('y','w1')],2:q2int})
    info("Y2 split, "+lab,V)
import itertools
def seppairs(G):
    out=[]
    for x,y in itertools.combinations(G.nodes(),2):
        H=G.copy(); H.remove_nodes_from([x,y])
        comps=[c for c in nx.connected_components(H)]
        if len(comps)>1 and all(len(c)>1 or True for c in comps):
            # ignore trivial: a single degree-2 vertex between x,y on a path
            big=[c for c in comps if not (len(c)==1 and G.degree(next(iter(c)))==2)]
            if len(big)>=2 or (len(comps)>=3): out.append(((x,y),[sorted(c) for c in comps]))
    return out
for (p,c) in seppairs(Y2.G): print(p,c)
