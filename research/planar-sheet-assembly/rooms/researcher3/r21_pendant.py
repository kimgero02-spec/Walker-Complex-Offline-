# R21-researcher3: CONSTRUCTOR for the "core + pendant" locked 3-partition (R21 report, Sec. 3).
# Finds a triangulation T, proper 4-colouring c (colours 0..3) and pairwise non-adjacent hubs H[x] (colour x)
# whose neighbours avoid colour x+2 (mod 4). Then builds G on {0,1,2} x V(T):
#   core_k = copy k of T;  pendant edge of sheet j for w=(k,v), k!=j :  (k,v) -- (j, H[(c(v)+1)%4]).
# Output JSON is to be checked by r21_verify.py (direct planarity tests). Generator only.
import random, sys, json, itertools, networkx as nx
from r21_search import rand_tri
def sphere_tri(N, rng):
    # convex hull of random points on the sphere = a (generic) triangulation of the sphere
    import numpy as np
    from scipy.spatial import ConvexHull
    P=np.array([[rng.gauss(0,1) for _ in range(3)] for _ in range(N)]); P/=np.linalg.norm(P,axis=1)[:,None]
    T=nx.Graph()
    for a,b,c in ConvexHull(P).simplices: T.add_edges_from([(int(a),int(b)),(int(b),int(c)),(int(a),int(c))])
    return T
def find(T, rng, tries=200):
    V=list(T.nodes())
    for _ in range(tries):
        ev=[v for v in V if T.degree(v)%2==0]; rng.shuffle(ev); hubs=[]
        for v in ev:
            if all(not T.has_edge(v,h) for h in hubs): hubs.append(v)
            if len(hubs)==4: break
        if len(hubs)<4: continue
        rng.shuffle(hubs); H={x:hubs[x] for x in range(4)}
        allowed={v:set(range(4)) for v in V}
        for x,h in H.items():
            allowed[h]={x}
        for x,h in H.items():
            for u in T[h]:
                allowed[u]&={(x+1)%4,(x+3)%4}
        if any(not a for a in allowed.values()): continue
        order=sorted(V,key=lambda v:len(allowed[v])); col={}
        def bt(i):
            if i==len(order): return True
            v=order[i]
            for c in sorted(allowed[v],key=lambda _:rng.random()):
                if all(col.get(u)!=c for u in T[v]):
                    col[v]=c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return H,col
    return None
def build(T,H,col,W=0):
    idx={}
    for k in range(3):
        for v in T.nodes(): idx[(k,v)]=len(idx)
    Q=[[] for _ in range(3)]
    for k in range(3):
        for u,v in T.edges(): Q[k].append(tuple(sorted((idx[(k,u)],idx[(k,v)]))))
    for j in range(3):
        for k in range(3):
            if k==j: continue
            for v in T.nodes():
                Q[j].append(tuple(sorted((idx[(k,v)],idx[(j,H[(col[v]+1)%4])]))))
    # extra vertices W: virtual colour i%4, pendant in every sheet j to hub H_j[(i%4+1)%4]
    for i in range(W):
        idx[('w',i)]=len(idx)
        for j in range(3): Q[j].append(tuple(sorted((idx[('w',i)],idx[(j,H[(i%4+1)%4])]))))
    return Q,idx
if __name__=="__main__":
    N=int(sys.argv[1]); seed=int(sys.argv[2]); rng=random.Random(seed); mode=sys.argv[3] if len(sys.argv)>3 else 'sphere'; W=int(sys.argv[4]) if len(sys.argv)>4 else 0
    for t in range(500):
        T=sphere_tri(N-4,rng) if mode=='sphere' else rand_tri(N-4,rng,flips=20*N)
        # insert 4 degree-4 hubs on edges (an edge ac with apexes b,d, bd not an edge): T stays a triangulation
        for i in range(4):
            for _ in range(200):
                a,c=rng.choice(list(T.edges())); cn=list(nx.common_neighbors(T,a,c))
                if len(cn)==2 and not T.has_edge(*cn) and all(T.degree(z)<90 for z in cn):
                    b,d=cn; h=N-4+i; T.remove_edge(a,c); T.add_edges_from([(h,a),(h,b),(h,c),(h,d)])
                    if nx.check_planarity(T)[0] and T.number_of_edges()==3*T.number_of_nodes()-6: break
                    T.remove_node(h); T.add_edge(a,c)
        if T.number_of_nodes()<N: continue
        r=find(T,rng)
        if r:
            H,col=r; Q,idx=build(T,H,col,W)
            fn=f"r21_pendant_N{N}_s{seed}_W{W}.json"
            json.dump({"Q":[[list(e) for e in q] for q in Q],"T":[list(e) for e in T.edges()],"H":H,"col":col},open(fn,"w"))
            print("built",fn,"T has",N,"vertices; hubs",H); break
    else: print("no T found")
