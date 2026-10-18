# reduce X for K_8 two straight layers (keep crossing graph bipartite)
import random, itertools, networkx as nx, sys
sys.path.insert(0,'/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3/r51')
random.seed(3)
def orient(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
def segx(P,e,f):
    a,b=e;c,d=f
    if len({a,b,c,d})<4: return False
    return orient(P[a],P[b],P[c])*orient(P[a],P[b],P[d])<0 and orient(P[c],P[d],P[a])*orient(P[c],P[d],P[b])<0
def crossg(P,n):
    E=list(itertools.combinations(range(n),2)); C=nx.Graph(); C.add_nodes_from(E)
    C.add_edges_from((e,f) for e,f in itertools.combinations(E,2) if segx(P,e,f)); return C
n=8
P=[(0.0552, 0.656), (0.5108, 0.5699), (0.4131, 0.7531), (0.7979, 0.8352), (-0.0287, 0.6686), (1.1874, 0.9514), (0.9025, -0.2772), (0.4105, 0.6883)]
C=crossg(P,n); X=C.number_of_edges()
for it in range(20000):
    i=random.randrange(n); old=P[i]; s=random.choice([0.2,0.05,0.01])
    P[i]=(old[0]+random.gauss(0,s),old[1]+random.gauss(0,s))
    C2=crossg(P,n)
    if nx.is_bipartite(C2) and C2.number_of_edges()<=X: C=C2; X=C2.number_of_edges()
    else: P[i]=old
print("min X found with 2 layers:",X,"points",[(round(a,4),round(b,4)) for a,b in P])
