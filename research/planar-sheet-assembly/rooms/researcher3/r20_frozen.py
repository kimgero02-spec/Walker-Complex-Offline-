# R20-researcher3: search for a FROZEN planar 3-assignment of a thickness-2 graph.
# frozen: every class planar, nonempty, and for every edge e in class i and j!=i, class_j + e is nonplanar.
# Used only to FIND a candidate; the candidate is then certified by direct checks (verify()).
import random, sys, itertools
import networkx as nx

def planar(edges):
    H = nx.Graph(); H.add_edges_from(edges)
    return nx.check_planarity(H)[0]

def random_triangulation(N, rng, flips=200):
    G = nx.Graph(); G.add_edges_from([(0,1),(1,2),(0,2)])
    faces = [(0,1,2),(0,2,1)]
    for v in range(3, N):
        f = faces.pop(rng.randrange(len(faces)))
        a,b,c = f
        G.add_edges_from([(v,a),(v,b),(v,c)])
        faces += [(a,b,v),(b,c,v),(c,a,v)]
    # random flips via planarity-preserving swaps: remove edge, add other diagonal if planar & simple
    E = list(G.edges())
    for _ in range(flips):
        u,v = rng.choice(list(G.edges()))
        cn = list(nx.common_neighbors(G,u,v))
        if len(cn) < 2: continue
        x,y = rng.sample(cn,2)
        if G.has_edge(x,y): continue
        G.remove_edge(u,v); G.add_edge(x,y)
        if not nx.check_planarity(G)[0] or G.number_of_edges()!=3*N-6:
            G.remove_edge(x,y); G.add_edge(u,v)
    return G

def movable(E, col, k=3):
    cls = [[e for e in E if col[e]==j] for j in range(k)]
    cnt = 0
    for e in E:
        for j in range(k):
            if j!=col[e] and planar(cls[j]+[e]): cnt += 1
    return cnt

def verify(E, col, T1, T2, k=3):
    cls = [[e for e in E if col[e]==j] for j in range(k)]
    assert all(len(c)>0 for c in cls)
    assert all(planar(c) for c in cls)
    for e in E:
        for j in range(k):
            if j!=col[e]: assert not planar(cls[j]+[e]), (e,j)
    assert planar(T1) and planar(T2)
    assert set(map(frozenset,T1))|set(map(frozenset,T2)) == set(map(frozenset,E))
    assert not planar(E)
    return True

def search(N, seed, iters=4000):
    rng = random.Random(seed)
    T1 = random_triangulation(N, rng); T2 = random_triangulation(N, rng)
    perm = list(range(N)); rng.shuffle(perm)
    T2 = nx.relabel_nodes(T2, dict(enumerate(perm)))
    G = nx.Graph(); G.add_edges_from(T1.edges()); G.add_edges_from(T2.edges())
    E = [tuple(sorted(e)) for e in G.edges()]
    t1 = [tuple(sorted(e)) for e in T1.edges()]
    t2 = [e for e in E if e not in set(t1)]
    # initial planar 3-coloring: random greedy
    col = {}
    order = E[:]; rng.shuffle(order)
    cls = [[],[],[]]
    for e in order:
        js = [0,1,2]; rng.shuffle(js)
        for j in js:
            if planar(cls[j]+[e]): cls[j].append(e); col[e]=j; break
        else:
            return None
    best = movable(E,col)
    for it in range(iters):
        e = rng.choice(E); j = rng.choice([x for x in range(3) if x!=col[e]])
        cj = [x for x in E if col[x]==j]
        if not planar(cj+[e]): continue
        old = col[e]; col[e]=j
        if sum(1 for x in E if col[x]==old)==0: col[e]=old; continue
        m = movable(E,col)
        if m <= best or rng.random()<0.02:
            best = m
            if m==0:
                return E,col,t1,t2
        else:
            col[e]=old
    return None

if __name__=="__main__":
    N = int(sys.argv[1]); s0=int(sys.argv[2]); s1=int(sys.argv[3])
    for s in range(s0,s1):
        r = search(N,s)
        if r:
            E,col,t1,t2 = r
            print("FOUND seed",s, verify(E,col,t1,t2))
            print("E=",E); print("col=",[col[e] for e in E]); print("T1=",t1)
            break
        else:
            print("seed",s,"no")
