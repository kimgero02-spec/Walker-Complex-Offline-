# R12 researcher1: search for G realizable with two different N (decisive counterexample hunt, not evidence)
import random, itertools, sys, networkx as nx
sys.path.insert(0, '.')
from r11_inverse import build_manual, try_W

def all_W(G, mode):
    D = dict(nx.all_pairs_shortest_path_length(G))
    cand = [v for v in G if G.degree(v) >= 2]
    # whites pairwise: (circ) dist exactly 3 ; (full) dist in {1,3}? keep <=3 and !=2
    def ok(a, b):
        d = D[a].get(b, 99)
        return d == 3 if mode == 'circ' else d in (1, 3)
    C = nx.Graph(); C.add_nodes_from(cand)
    C.add_edges_from((a, b) for a, b in itertools.combinations(cand, 2) if ok(a, b))
    res = []
    for W in [()] + [tuple(c) for c in nx.enumerate_all_cliques(C)]:
        P = try_W(G, W, mode)
        if P is not None:
            res.append((W, len({f for Vk, Ek in P for f in Vk})))
    return res

def rand_decomp(N, rng):
    V = list(range(N)); E = list(itertools.combinations(V, 2))
    pieces = []
    k = rng.randint(1, 4)
    for _ in range(k):
        Vk = [v for v in V if rng.random() < 0.6]
        pieces.append((Vk, []))
    for e in E:
        # put e in random pieces (at least one); add vertices if needed
        ks = [i for i in range(k) if rng.random() < 0.35] or [rng.randrange(k)]
        for i in ks:
            for v in e:
                if v not in pieces[i][0]: pieces[i][0].append(v)
            pieces[i][1].append(e)
    for Vk, Ek in pieces:
        P = nx.Graph(); P.add_nodes_from(Vk); P.add_edges_from(Ek)
        if not nx.check_planarity(P)[0]: return None
    return pieces

rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
seen = 0
for it in range(4000):
    N = rng.randint(1, 6)
    P = rand_decomp(N, rng)
    if P is None: continue
    M, Mc, A = build_manual(P)
    for mode, G in (('circ', Mc), ('full', M)):
        if G.number_of_nodes() > 22: continue
        Ns = {n for W, n in all_W(G, mode)}
        seen += 1
        if len(Ns) > 1:
            print('MULTI', mode, N, Ns, G.number_of_nodes(), sorted(G.edges()))
            sys.exit()
print('checked', seen, 'no multi-N found')
