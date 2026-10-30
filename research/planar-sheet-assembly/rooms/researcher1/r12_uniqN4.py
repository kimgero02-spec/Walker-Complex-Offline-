# R12 r1 (resumed 2): decisive counterexample hunt for "N determined by G", both modes,
# N<=6, pieces = random planar subgraphs (incl. K1 pieces). Not evidence; only a found MULTI matters.
import random, itertools, sys, networkx as nx
from r11_inverse import build_manual, try_W
def Ws(G, mode):
    D = dict(nx.all_pairs_shortest_path_length(G))
    cand = [v for v in G if G.degree(v) >= 2]
    if mode == 'circ':
        cand = [v for v in cand if not any(G.has_edge(a,b) for a,b in itertools.combinations(G[v],2))]
        ok = lambda a,b: D[a].get(b)==3
    else:
        ok = lambda a,b: D[a].get(b,99)<=3
    C = nx.Graph(); C.add_nodes_from(cand)
    C.add_edges_from((a,b) for a,b in itertools.combinations(cand,2) if ok(a,b))
    out=set()
    for W in [()]+[tuple(c) for c in nx.enumerate_all_cliques(C)]:
        P = try_W(G,W,mode)
        if P is not None: out.add((len(W), len({f for Vk,Ek in P for f in Vk})))
    return out
rng = random.Random(int(sys.argv[1])); cnt=0; maxV=int(sys.argv[3])
for it in range(int(sys.argv[2])):
    N = rng.randint(2,6); E = list(itertools.combinations(range(N),2))
    k = rng.randint(1,5); pieces=[[set(),set()] for _ in range(k)]
    for e in E:
        for i in rng.sample(range(k), min(k, rng.choice([1,1,1,2,2,3]))):
            pieces[i][1].add(e); pieces[i][0].update(e)
    for _ in range(rng.choice([0,0,1,2])): pieces.append([{rng.randrange(N)},set()])
    pieces=[(sorted(a),sorted(b)) for a,b in pieces if a]
    if any(not nx.check_planarity(nx.Graph(b))[0] for a,b in pieces): continue
    M,Mc,A = build_manual(pieces)
    for mode,G in (('circ',Mc),('full',M)):
        if G.number_of_nodes()>maxV: continue
        cnt+=1
        S = Ws(G,mode); Ns={n for w,n in S}
        if N not in Ns: print('BUG', mode, pieces)
        if len(Ns)>1: print('MULTI', mode, S, pieces); sys.stdout.flush()
print('done', cnt)
