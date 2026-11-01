"""F-R2: (1) 포트 쪼개기 비용 kappa, (2) s* 와 t* = chi - s* 확인. 결정적 예 E1-E6."""
import itertools, networkx as nx
src = open('fr1_junction.py').read().split("K4m = ")[0]
exec(src)

def set_partitions(lst):
    if not lst: yield []; return
    f, rest = lst[0], lst[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[f] + p[i]] + p[i+1:]
        yield [[f]] + p

def split_graph(A, sigma):
    """sigma: port -> list of blocks (각 블록은 이웃 검정 점들의 리스트)."""
    sub = {}
    for x, blocks in sigma.items():
        for i, bl in enumerate(blocks):
            for y in bl: sub[(x, y)] = (x, i)
    S = nx.Graph()
    def name(x, y): return sub.get((x, y), x)
    for v in A:
        if A.nodes[v]['c'] == 'B' and v not in sigma: S.add_node(v)
    for x, blocks in sigma.items():
        for i in range(len(blocks)): S.add_node((x, i))
    for a, b in A.subgraph(black(A)).edges:
        S.add_edge(name(a, b), name(b, a))
    for w in whites(A):
        for p in A[w]:
            if p in sigma:
                for i in range(len(sigma[p])): S.add_edge(w, (p, i))
            else: S.add_edge(w, p)
    return S

def kappa(A, cap=6):
    ports = [p for w in whites(A) for p in A[w]]
    opts = {}
    for p in ports:
        nb = [y for y in A[p] if A.nodes[y]['c'] == 'B']
        opts[p] = sorted(([len(P) - 1, P] for P in set_partitions(nb)), key=lambda z: z[0]) if nb else [[0, [[]]]]
    best = None
    for combo in itertools.product(*[opts[p] for p in ports]):
        cost = sum(c for c, _ in combo)
        if best is not None and cost >= best: continue
        sigma = {p: P for p, (c, P) in zip(ports, combo) if c > 0}
        if nx.check_planarity(split_graph(A, sigma))[0]: best = cost
    return best if best is not None else float('inf')

def colorings(g, q):
    nodes = list(g.nodes); out = []
    def bt(i, col):
        if i == len(nodes): out.append(dict(col)); return
        v = nodes[i]; used = {col[u] for u in g[v] if u in col}
        for c in range(q):
            if c not in used: col[v] = c; bt(i+1, col); del col[v]
    bt(0, {}); return out

def s_star(A, q):
    comps = [A.subgraph(c).copy() for c in nx.connected_components(A.subgraph(black(A)))]
    cols = [colorings(c, q) for c in comps]
    if any(not c for c in cols): return float('inf')
    best = float('inf')
    for combo in itertools.product(*cols):
        c = {}; [c.update(d) for d in combo]
        s = max(len({c[p] for p in A[w]}) for w in whites(A))
        best = min(best, s)
        if best == 2: break
    return best

def info(name, A, T):
    G = nx.Graph(recover(A)[0]); chi = chrom(G)
    seq = [chrom(subst(A, t)) for t in range(T + 1)]
    m = seq[0]; tstar = next(t for t in range(T + 1) if seq[t] == chi)
    ss = s_star(A, chi - 1) if chi > m else None
    print('== %s: chi=%d m=%d seq=%s t*=%d g=%d s*=%s  chi-s*=%s  kappa=%s  Gplanar=%s' % (
        name, chi, m, seq, tstar, chi - m, ss, (chi - ss) if ss else '-', kappa(A), nx.check_planarity(G)[0]), flush=True)

def sq(c): return [(c[i], c[(i + 1) % len(c)]) for i in range(len(c))]
def band(k, twist):
    P, cl = {}, []
    for i in range(k): P[i] = sq([('t',i),('t',i+1),('s',i+1),('s',i)])
    for i in range(1, k): cl += [[(i-1,('t',i)),(i,('t',i))], [(i-1,('s',i)),(i,('s',i))]]
    if twist: cl += [[(k-1,('t',k)),(0,('s',0))], [(k-1,('s',k)),(0,('t',0))]]
    else:     cl += [[(k-1,('t',k)),(0,('t',0))], [(k-1,('s',k)),(0,('s',0))]]
    return build(P, cl)
K4m = [('u','a'),('u','b'),('v','a'),('v','b'),('a','b')]
W4 = [('a','b'),('b','d'),('d','c'),('c','a'),('e','a'),('e','b'),('e','c'),('e','d')]
info('E1', build({1: K4m, 2: [('u','v')]}, [[(1,'u'),(2,'u')],[(1,'v'),(2,'v')]]), 5)
info('E2', build({1: sq([0,1,3,2]), 2: sq([0,3,1,2])}, [[(1,v),(2,v)] for v in range(4)]), 5)
info('E3', build({1: sq([1,2,3,4]) + [('h',1),('h',3)], 2: [('h',2),('h',4)]},
     [[(1,'h'),(2,'h')],[(1,2),(2,2)],[(1,4),(2,4)]]), 4)
info('E4', build({1: W4, 2: sq(['a','b','c','d'])}, [[(1,v),(2,v)] for v in 'abcd']), 5)
info('E5a', band(3, 0), 4); info('E5b', band(3, 1), 4); info('E6', band(4, 1), 4)
# K_n from K_2 pieces (m=2): 예상 t* = g
for n in (4, 5):
    Kn = nx.complete_graph(n); P = {i: [e] for i, e in enumerate(Kn.edges)}
    cl = [[(i, v) for i, e in enumerate(Kn.edges) if v in e] for v in Kn]
    info('K%d from K2' % n, build(P, cl), n)
# K5 from K4 + K2 (m=4,g=1): 엄격 여부
K4e = list(nx.complete_graph(4).edges)
info('K5=K4(0123)+K2-star?', build({1: K4e, 2: [(0,4)], 3: [(1,4)], 4: [(2,4)], 5: [(3,4)]},
     [[(1,0),(2,0)],[(1,1),(3,1)],[(1,2),(4,2)],[(1,3),(5,3)],[(2,4),(3,4),(4,4),(5,4)]]), 5)
