# R21-researcher3: GENERATOR ONLY. Look for G = A u B (A,B planar => theta<=2) with a locked 3-partition.
import random, sys, networkx as nx
def planar(E):
    H=nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]
def rand_tri(N, rng, flips=200):
    G=nx.Graph(); G.add_edges_from([(0,1),(1,2),(0,2)]); faces=[(0,1,2),(0,2,1)]
    for v in range(3,N):
        a,b,c=faces.pop(rng.randrange(len(faces))); G.add_edges_from([(v,a),(v,b),(v,c)]); faces+=[(a,b,v),(b,c,v),(c,a,v)]
    for _ in range(flips):
        u,v=rng.choice(list(G.edges())); cn=list(nx.common_neighbors(G,u,v))
        if len(cn)!=2: continue
        x,y=cn
        if G.has_edge(x,y) or G.degree(u)<=3 or G.degree(v)<=3: continue
        G.remove_edge(u,v); G.add_edge(x,y)
        if not nx.check_planarity(G)[0]: G.remove_edge(x,y); G.add_edge(u,v)
    return G
def greedy(pool, base, rng):
    S=list(base); order=pool[:]; rng.shuffle(order)
    for e in order:
        if planar(S+[e]): S.append(e)
    return S
def locked(Q, E):
    for q in Q:
        if not planar(q): return False
        s=set(q)
        for e in E:
            if e not in s and planar(q+[e]): return False
    return True
if __name__=="__main__":
    N=int(sys.argv[1]); rng=random.Random(int(sys.argv[2])); T=int(sys.argv[3]); dens=float(sys.argv[4])
    for t in range(T):
        A=rand_tri(N,rng); B=rand_tri(N,rng); p=list(range(N)); rng.shuffle(p)
        E=set(tuple(sorted(e)) for e in A.edges())
        Bk=[tuple(sorted((p[u],p[v]))) for u,v in B.edges() if rng.random()<dens]
        E|=set(Bk); E=sorted(E)
        if planar(E): continue
        for s in range(30):
            Q1=greedy(E,[],rng); R=[e for e in E if e not in set(Q1)]
            Q2=greedy(R,[],rng); Q3=[e for e in R if e not in set(Q2)]
            if not Q3: continue
            if locked([Q1,Q2,Q3],E):
                print("FOUND",N,len(E),[len(Q1),len(Q2),len(Q3)])
                print("E=",E); print("Q=",[Q1,Q2,Q3]); sys.exit()
    print("none")
