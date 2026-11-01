"""F-R1 (재배정): 접합 그래프 A 의 결정적 예. 복원 G, 정리 A 수열, A 의 평면성, 포트 연속 조건."""
import itertools, sys, networkx as nx

def colorable(g, q):
    nodes = sorted(g.nodes, key=lambda v: -g.degree(v)); col = {}
    adj = {v: set(g[v]) for v in g}
    def bt():
        un = [v for v in nodes if v not in col]
        if not un: return True
        v = max(un, key=lambda u: (len({col[x] for x in adj[u] if x in col}), len(adj[u])))
        used = {col[x] for x in adj[v] if x in col}
        mx = max(col.values(), default=-1)
        for c in range(min(q, mx + 2)):
            if c not in used:
                col[v] = c
                if bt(): return True
                del col[v]
        return False
    return bt()

def chrom(g):
    if g.number_of_nodes() == 0: return 0
    q = 1
    while not colorable(g, q): q += 1
    return q

def build(pieces, classes):
    A = nx.Graph()
    for k, E in pieces.items():
        for a, b in E: A.add_edge((k, a), (k, b))
    for v in A: A.nodes[v]['c'] = 'B'
    for j, cl in enumerate(classes):
        w = ('w', j); A.add_node(w, c='W')
        for p in cl: A.add_edge(w, p)
    return A

def black(A): return [v for v in A if A.nodes[v]['c'] == 'B']
def whites(A): return [v for v in A if A.nodes[v]['c'] == 'W']

def recover(A):
    rep = {v: v for v in black(A)}
    for w in whites(A):
        r = min(A[w])
        for p in A[w]: rep[p] = r
    G = nx.MultiGraph(); G.add_nodes_from(set(rep.values()))
    for a, b in A.subgraph(black(A)).edges: G.add_edge(rep[a], rep[b], src=(a, b))
    return G, rep

def subst(A, t):
    S = A.subgraph(black(A)).copy()
    for w in whites(A):
        cl = [(w, i) for i in range(t)]
        S.add_nodes_from(cl); S.add_edges_from(itertools.combinations(cl, 2))
        for c in cl:
            for p in A[w]: S.add_edge(c, p)
    return S

def piece_level_H(A):
    """조각 수준 그래프: 점 = 검정 성분, 흰 점마다 그 포트들의 조각을 잇는 하이퍼변 (다중집합)."""
    comp = {}
    for i, c in enumerate(nx.connected_components(A.subgraph(black(A)))):
        for v in c: comp[v] = i
    return sorted(tuple(sorted(comp[p] for p in A[w])) for w in whites(A))

def rep_(name, A, T, target=None):
    MG, _ = recover(A); G = nx.Graph(MG)
    chi = chrom(G); seq = [chrom(subst(A, t)) for t in range(T + 1)]
    print('==', name)
    print('  G: n=%d m=%d (multi m=%d) chi=%d planar=%s' % (G.number_of_nodes(), G.number_of_edges(),
          MG.number_of_edges(), chi, nx.check_planarity(G)[0]))
    if target is not None: print('  G iso target:', nx.is_isomorphic(G, target))
    print('  chi(A^(t)) t=0..%d:' % T, seq, ' A planar:', nx.check_planarity(A)[0])
    print('  plateau check  t+2<=val<=chi for t<=chi-2:',
          all(t + 2 <= seq[t] <= chi for t in range(min(chi - 1, T + 1))),
          '; val=t+1 for t>=chi-1:', all(seq[t] == t + 1 for t in range(chi - 1, T + 1)))
    print('  piece-level H:', piece_level_H(A)); sys.stdout.flush()
    return G

def sq(c): return [(c[i], c[(i + 1) % len(c)]) for i in range(len(c))]

K4m = [('u','a'),('u','b'),('v','a'),('v','b'),('a','b')]
# E1: K4 = (K4-uv) U K2, 포트 u,v
rep_('E1 K4=(K4-uv)+K2', build({1: K4m, 2: [('u','v')]}, [[(1,'u'),(2,'u')],[(1,'v'),(2,'v')]]), 5, nx.complete_graph(4))
# E1': 같은 조각, 같은 조각수준 H, 포트만 a,b
rep_("E1' ports a,b", build({1: K4m, 2: [('u','v')]}, [[(1,'a'),(2,'u')],[(1,'b'),(2,'v')]]), 4)
# E2: K4 = 정사각형 둘 (뫼비우스)
rep_('E2 K4=two squares', build({1: sq([0,1,3,2]), 2: sq([0,3,1,2])}, [[(1,v),(2,v)] for v in range(4)]), 5, nx.complete_graph(4))
# E3: W4 의 중심을 쪼갬: P1 = 테 1234 + h1,h3 ; P2 = 경로 2-h-4
rep_('E3 W4 split hub', build({1: sq([1,2,3,4]) + [('h',1),('h',3)], 2: [('h',2),('h',4)]},
     [[(1,'h'),(2,'h')],[(1,2),(2,2)],[(1,4),(2,4)]]), 4, nx.wheel_graph(5))
# E4: K5 = W4 U C4
W4 = [('a','b'),('b','d'),('d','c'),('c','a'),('e','a'),('e','b'),('e','c'),('e','d')]
rep_('E4 K5=W4+C4', build({1: W4, 2: sq(['a','b','c','d'])}, [[(1,v),(2,v)] for v in 'abcd']), 5, nx.complete_graph(5))
# E5: 정사각형 3장 띠, 곧게 / 꼬아
def band(k, twist):
    P, cl = {}, []
    for i in range(k):
        P[i] = sq([('t',i),('t',i+1),('s',i+1),('s',i)])
    for i in range(1, k): cl += [[(i-1,('t',i)),(i,('t',i))], [(i-1,('s',i)),(i,('s',i))]]
    if twist: cl += [[(k-1,('t',k)),(0,('s',0))], [(k-1,('s',k)),(0,('t',0))]]
    else:     cl += [[(k-1,('t',k)),(0,('t',0))], [(k-1,('s',k)),(0,('s',0))]]
    return build(P, cl)
rep_('E5a prism k=3', band(3, 0), 4, nx.circular_ladder_graph(3))
rep_('E5b Moebius k=3', band(3, 1), 4, nx.complete_bipartite_graph(3, 3))
