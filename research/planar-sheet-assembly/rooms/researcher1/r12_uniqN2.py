# R12 r1: generate realizable G directly from (planar H, transversal fiber partition with complete quotient),
# then list ALL data W (no distance pruning for 'full'; exact-3 pruning for 'circ' is a proved necessary cond.)
import random, itertools, sys, networkx as nx
from r11_inverse import try_W
def all_W(G, mode):
    D = dict(nx.all_pairs_shortest_path_length(G))
    cand = [v for v in G if G.degree(v) >= 2]
    ok = (lambda a,b: D[a].get(b,99)==3) if mode=='circ' else (lambda a,b: D[a].get(b,99)<=3)
    C = nx.Graph(); C.add_nodes_from(cand)
    C.add_edges_from((a,b) for a,b in itertools.combinations(cand,2) if ok(a,b))
    out=set()
    for W in [()]+[tuple(c) for c in nx.enumerate_all_cliques(C)]:
        P = try_W(G, W, mode)
        if P is not None: out.add((len(W), len({f for Vk,Ek in P for f in Vk})))
    return out
def gen(rng):
    N = rng.randint(2,5); c = rng.randint(1,5)
    # components: random planar graphs on random sizes; fibers: assign each vertex a label in [N], transversal per comp
    H = nx.Graph(); lab = {}
    for i in range(c):
        size = rng.randint(1, N)
        labs = rng.sample(range(N), size)
        T = nx.random_labeled_tree(size, seed=rng.randrange(10**9)) if size>1 else nx.empty_graph(1)
        for a,b in itertools.combinations(range(size),2):
            if rng.random()<0.3: T.add_edge(a,b)
        if not nx.check_planarity(T)[0]: return None
        for v in T: H.add_node((i,v)); lab[(i,v)] = labs[v]
        H.add_edges_from(((i,a),(i,b)) for a,b in T.edges())
    Q = {frozenset((lab[a],lab[b])) for a,b in H.edges()}
    used = set(lab.values())
    if len(used)<N or any(frozenset(p) not in Q for p in itertools.combinations(range(N),2)): return None
    G = H.copy(); W=[]
    for t in range(N):
        fib=[x for x in H if lab[x]==t]
        if len(fib)>=2:
            G.add_edges_from((('w',t),x) for x in fib); W.append(('w',t))
    G2 = G.copy()
    for t,u in itertools.combinations(range(N),2):
        if ('w',t) in G and ('w',u) in G and sum(1 for a,b in H.edges() if {lab[a],lab[b]}=={t,u})>=2:
            G2.add_edge(('w',t),('w',u))
    return G, G2
rng = random.Random(int(sys.argv[1])); cnt=0; diam=0
for it in range(20000):
    r = gen(rng)
    if r is None: continue
    for mode,G in (('circ',r[0]),('full',r[1])):
        if G.number_of_nodes()>18: continue
        cnt+=1; diam=max(diam, nx.diameter(G))
        S = all_W(G, mode); Ns={n for w,n in S}
        if len(Ns)>1:
            print('MULTI',mode,S,sorted(G.edges())); sys.exit()
print('checked',cnt,'max diam',diam)
