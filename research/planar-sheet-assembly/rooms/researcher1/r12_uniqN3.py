# R12 r1 (resumed): decisive counterexample hunt for "N determined by G" in mode circ (G = M°).
# Generate G from random decompositions of K_N (N<=5) via build_manual, then list all W that are
# cliques of the exact-distance-3 graph (proved necessary: whites pairwise at distance exactly 3).
import random, itertools, sys, networkx as nx
from r11_inverse import build_manual, try_W
def Ws(G):
    D = dict(nx.all_pairs_shortest_path_length(G))
    cand = [v for v in G if G.degree(v) >= 2 and not any(G.has_edge(a,b) for a,b in itertools.combinations(G[v],2))]
    C = nx.Graph(); C.add_nodes_from(cand)
    C.add_edges_from((a,b) for a,b in itertools.combinations(cand,2) if D[a].get(b)==3)
    out=set()
    for W in [()]+[tuple(c) for c in nx.enumerate_all_cliques(C)]:
        if try_W(G,W,'circ') is not None:
            out.add((len(W), G.number_of_nodes()-sum(G.degree(w) for w in W)))
    return out
rng = random.Random(int(sys.argv[1])); cnt=0
for it in range(int(sys.argv[2])):
    N = rng.randint(2,5); E = list(itertools.combinations(range(N),2))
    k = rng.randint(2,4); pieces=[[set(),set()] for _ in range(k)]
    for e in E:
        for i in (rng.sample(range(k), rng.choice([1,1,2]))):
            pieces[i][1].add(e); pieces[i][0].update(e)
    for p in pieces:
        for v in range(N):
            if rng.random()<0.15: p[0].add(v)
    pieces=[(sorted(a),sorted(b)) for a,b in pieces if a]
    if any(not nx.check_planarity(nx.Graph(b))[0] for a,b in pieces): continue
    M,Mc,A = build_manual(pieces)
    if Mc.number_of_nodes()>20: continue
    cnt+=1
    S = Ws(Mc); Ns={n for w,n in S}
    if len(Ns)>1: print('MULTI', S, pieces); sys.stdout.flush()
print('done', cnt)
