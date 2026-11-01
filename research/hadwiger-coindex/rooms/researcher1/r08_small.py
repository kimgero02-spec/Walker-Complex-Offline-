# R08 researcher1: small-example checks (guessing aid only)
import itertools, random, sys
import networkx as nx

def K(n):
    G = nx.complete_graph(n); return G
def K33():
    return nx.complete_bipartite_graph(3,3)
def C5K2():
    G = nx.Graph()
    for i in range(5):
        for s in (0,1):
            G.add_node((i,s))
    for i in range(5):
        for s in (0,1):
            for t in (0,1):
                if s!=t: G.add_edge((i,s),(i,t))
            for t in (0,1):
                j=(i+1)%5
                G.add_edge((i,s),(j,t))
    return G

def maximal_bicliques(G):
    V = list(G.nodes()); idx = {v:i for i,v in enumerate(V)}
    res = []
    for r in range(1, len(V)+1):
        for A in itertools.combinations(V, r):
            common = set(V)
            for a in A: common &= set(G[a])
            common -= set(A)
            if common:
                res.append((set(A), common))
    return V, res

def runs_max(order, bics):
    m = 0
    for A,B in bics:
        seq = [1 if v in A else 2 for v in order if (v in A or v in B)]
        r = 1 + sum(1 for i in range(1,len(seq)) if seq[i]!=seq[i-1])
        m = max(m, r)
    return m

def zig_upper(G, iters=20000, seed=1):
    V, bics = maximal_bicliques(G)
    rnd = random.Random(seed)
    order = V[:]; rnd.shuffle(order)
    best = runs_max(order, bics); bo = order[:]
    cur = best
    for it in range(iters):
        i,j = rnd.sample(range(len(order)),2)
        new = order[:]; new[i],new[j] = new[j],new[i]
        val = runs_max(new, bics)
        if val <= cur or rnd.random() < 0.02:
            order, cur = new, val
            if val < best: best, bo = val, new[:]
        if best <= 2 and len(V)<=0: break
    return best, bo

def planar_parts(G, k):
    V = list(G.nodes()); n=len(V)
    # k=1,2 brute force (labelled partitions up to symmetry for k=2)
    if k==1:
        return nx.check_planarity(G)[0]
    if k==2:
        for mask in range(2**(n-1)):
            P1 = [V[i] for i in range(n) if (mask>>i)&1 or i==n-1]
            P2 = [v for v in V if v not in P1]
            if nx.check_planarity(G.subgraph(P1))[0] and nx.check_planarity(G.subgraph(P2))[0]:
                return (P1,P2)
        return None
    return None

def planar_number(G):
    if nx.check_planarity(G)[0]: return 1
    if planar_parts(G,2): return 2
    return ">=3"

if __name__ == "__main__":
    tests = {"K5":K(5),"K6":K(6),"K33":K33(),"C5[K2]":C5K2()}
    for name,G in tests.items():
        print(name, "n=",G.number_of_nodes(), "m=",G.number_of_edges(), "planar sheet number p =", planar_number(G))
    # zig sanity and value
    for name,G in tests.items():
        z,_ = zig_upper(G, iters=6000, seed=2)
        print(name, "zig upper certificate (random search) =", z)
