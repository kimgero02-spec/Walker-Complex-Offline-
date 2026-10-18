import random, itertools, math, networkx as nx
random.seed(5)
def orient(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
def segx(P,e,f):
    a,b=e;c,d=f
    if len({a,b,c,d})<4: return False
    return orient(P[a],P[b],P[c])*orient(P[a],P[b],P[d])<0 and orient(P[c],P[d],P[a])*orient(P[c],P[d],P[b])<0
# K6 1-planar straight: outer triangle + small inner triangle rotated
P=[(0,0),(12,0),(6,10),(6,2.5),(7.3,4.8),(4.7,4.8)]
E=list(itertools.combinations(range(6),2))
C=[(e,f) for e,f in itertools.combinations(E,2) if segx(P,e,f)]
print("K6 crossings:",C, "max crossings per edge:",max(sum(1 for c in C if e in c) for e in E))
# convex k=3 layers forced to share chord (0,n/2): components vs regions
n=10; P=[(math.cos(2*math.pi*i/n),math.sin(2*math.pi*i/n)) for i in range(n)]
def randtri_pts(P,forced):
    E=list(itertools.combinations(range(len(P)),2)); random.shuffle(E); T=list(forced)
    for e in E:
        if e not in T and not any(segx(P,e,f) for f in T): T.append(e)
    return set(T)
for trial in range(3):
    Ts=[randtri_pts(P,[(0,5),(2,5)]) for _ in range(3)]
    hull={tuple(sorted((i,(i+1)%n))) for i in range(n)}
    common=set.intersection(*Ts)-hull; D=list(set.union(*Ts)-hull-common)
    G=nx.Graph(); G.add_nodes_from(D); G.add_edges_from((e,f) for e,f in itertools.combinations(D,2) if segx(P,e,f))
    print("convex n=10 k=3 common chords",sorted(common),"components",nx.number_connected_components(G))
