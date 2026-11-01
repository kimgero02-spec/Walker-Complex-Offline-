# C4: (i) k convex triangulation layers: crossing graph components <-> regions cut by chords common to ALL layers
#     (ii) two triangulations of a general point set: #components of Cr(non-common edges) vs #bounded faces of common graph H minus common empty triangles
import random, itertools, networkx as nx
random.seed(7)
def orient(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
def segx(P,e,f):
    a,b=e;c,d=f
    if len({a,b,c,d})<4: return False
    return orient(P[a],P[b],P[c])*orient(P[a],P[b],P[d])<0 and orient(P[c],P[d],P[a])*orient(P[c],P[d],P[b])<0
def randtri_pts(P):
    E=list(itertools.combinations(range(len(P)),2)); random.shuffle(E); T=[]
    for e in E:
        if not any(segx(P,e,f) for f in T): T.append(e)
    return set(T)
def comps(P,edges):
    C=nx.Graph(); C.add_nodes_from(edges)
    C.add_edges_from((e,f) for e,f in itertools.combinations(edges,2) if segx(P,e,f))
    return nx.number_connected_components(C), C
# (i) convex, k=3
import math
for n,k in [(7,3),(9,3),(10,4)]:
    P=[(math.cos(2*math.pi*i/n),math.sin(2*math.pi*i/n)) for i in range(n)]
    for trial in range(3):
        Ts=[randtri_pts(P) for _ in range(k)]
        hull={tuple(sorted((i,(i+1)%n))) for i in range(n)}
        common=set.intersection(*Ts)-hull
        D=set.union(*Ts)-hull-common
        nc,C=comps(P,list(D))
        # regions with >=4 vertices cut by common chords: count = (#common chords+1) - #triangular regions
        # count regions by splitting polygon
        regions=[list(range(n))]
        for (a,b) in common:
            new=[]
            for R in regions:
                if a in R and b in R:
                    i,j=R.index(a),R.index(b); i,j=min(i,j),max(i,j)
                    new+= [R[i:j+1], R[j:]+R[:i+1]]
                else: new.append(R)
            regions=new
        big=sum(1 for R in regions if len(R)>=4)
        assert all(any(segx(P,d,f) for f in D) for d in D)
        print(f"convex n={n} k={k}: components={nc}, regions(>=4)={big}, X={C.number_edges() if hasattr(C,'number_edges') else C.number_of_edges()}, |D|-1={len(D)-1}")
# (ii) general position, 2 layers
for n in [7,8,9]:
    for trial in range(4):
        P=[(random.random(),random.random()) for _ in range(n)]
        T1=randtri_pts(P); T2=randtri_pts(P)
        common=T1&T2; D=list((T1|T2)-common)
        nc,C=comps(P,D)
        H=nx.Graph(); H.add_nodes_from(range(n)); H.add_edges_from(common)
        Fb=H.number_of_edges()-n+nx.number_connected_components(H)
        def faces_tri(T):
            S=set()
            for a,b,c in itertools.combinations(range(n),3):
                if {(a,b),(a,c),(b,c)}<=T and not any(orient(P[a],P[b],P[x])*orient(P[a],P[b],P[c])>0 and orient(P[b],P[c],P[x])*orient(P[b],P[c],P[a])>0 and orient(P[a],P[c],P[x])*orient(P[a],P[c],P[b])>0 for x in range(n) if x not in (a,b,c)):
                    S.add((a,b,c))
            return S
        ct=len(faces_tri(T1)&faces_tri(T2))
        print(f"general n={n}: components={nc}, predicted (bounded faces of H - common triangles)={Fb-ct}")
