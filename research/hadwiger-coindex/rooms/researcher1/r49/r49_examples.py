# R49-r1: decisive examples only. (a) 13-vertex (1,1) chi=5; (b) theta of R48 gadget.
import networkx as nx, itertools
from pysat.solvers import Minisat22

def kcol(G,k,lists=None):
    V=list(G); idx={v:i for i,v in enumerate(V)}
    var=lambda v,c: idx[v]*k+c+1
    s=Minisat22()
    for v in V:
        L=range(k) if lists is None else [c for c in lists[v] if c<k]
        s.add_clause([var(v,c) for c in L])
        for c in range(k):
            if lists is not None and c not in L: s.add_clause([-var(v,c)])
    for u,v in G.edges():
        for c in range(k): s.add_clause([-var(u,c),-var(v,c)])
    ok=s.solve(); return ok

# (a) Apollonian B1 with 4 vertices forced to the colour of s
B1=nx.Graph(); a,b,c,s='a','b','c','s'
B1.add_edges_from(itertools.combinations([a,b,c,s],2))
def ins(x,f): B1.add_edges_from((x,t) for t in f)
ins('x1',(a,b,c)); ins('y',(a,b,'x1')); ins('z',(a,b,'y')); ins('w',(a,b,'z')); ins('u',(a,b,'w'))
G=B1.copy(); Y=['Y1','Y2','Y3','Y4']; G.add_edges_from(itertools.combinations(Y,2))
G.add_edges_from(zip(['s','x1','z','u'],Y))
print("(a) n,m",G.number_of_nodes(),G.number_of_edges(),"B1 planar",nx.check_planarity(B1)[0])
hs=[sum(1 for t in G[v] if (t in Y)!=(v in Y)) for v in G]; print(" max h",max(hs))
print(" 4-col",kcol(G,4)," 5-col",kcol(G,5))

# (b) theta for R48 gadget: all 4-colourings of B1 = A ⊔ K4, X_v for v in Q2
def apol(tag):
    p,q,r,s_,P,Q,R=[tag+x for x in ["p","q","r","s","P","Q","R"]]
    E=list(itertools.combinations([p,q,r,s_],2))
    E+=[(P,q),(P,r),(P,s_),(Q,p),(Q,r),(Q,s_),(R,p),(R,q),(R,s_)]
    return E,(p,q,r,P,Q,R)
E1,(p,q,r,P,Q,R)=apol("a"); A=nx.Graph(E1)
X={'v1':(p,q,r),'v2':(p,q,r),'v3':(p,q,r),'v4':(P,Q,R)}
cols=[]
V=list(A)
for col in itertools.product(range(4),repeat=len(V)):
    cc=dict(zip(V,col))
    if all(cc[x]!=cc[y] for x,y in A.edges()): cols.append(cc)
print("(b) #4-colourings of A",len(cols))
print(" set of (|phi(X_v)|) profiles",set(tuple(len({cc[x] for x in X[v]}) for v in X) for cc in cols))
print(" union of residual colours over Q2 per phi",set(len(set(range(4))-set().union(*[{cc[x] for x in X[v]} for v in X])) for cc in cols),
      " | U M_phi(v)| =",set(len(set().union(*[set(range(4))-{cc[x] for x in X[v]} for v in X])) for cc in cols))
