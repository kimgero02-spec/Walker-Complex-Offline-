"""F-R5: 흰-흰 간선이 A 의 평면성 층을 바꾸는가. B = A + (M3 허용 흰-흰 간선 전부)."""
import itertools, networkx as nx
exec(open('fr2.py').read().split("def sq(c)")[0])
def sq(c): return [(c[i], c[(i + 1) % len(c)]) for i in range(len(c))]

def add_ww(A):
    B = A.copy()
    W = whites(A)
    for w, x in itertools.combinations(W, 2):
        cnt = 0
        for p in A[w]:
            for q in A[x]:
                if p[0] == q[0] and A.has_edge(p, q): cnt += 1
        if cnt >= 2: B.add_edge(w, x)
    return B

def glue_arc(cl, Pi, e_i, Pj, e_j):
    """호(변 하나): P_i 의 테 변 (u,v) [테 방향], P_j 의 (u',v') -> 반대 방향 식별 (eps=+1)."""
    (u, v), (u2, v2) = e_i, e_j
    cl += [[(Pi, u), (Pj, v2)], [(Pi, v), (Pj, u2)]]

def report(name, A):
    B = add_ww(A); G = nx.Graph(recover(A)[0])
    print('%-34s G planar=%s  A planar=%s  B planar=%s  #ww=%d' % (name, nx.check_planarity(G)[0],
          nx.check_planarity(A)[0], nx.check_planarity(B)[0], B.number_of_edges() - A.number_of_edges()), flush=True)

# 엇갈림 토러스 (R01 §5): 팔각형 P0, 호 a=(0,1), b=(2,3), a'=(4,5), b'=(6,7). 사각형 Q1,Q2,R1,R2.
def torus(wheel=False):
    P = {'P0': sq(list(range(8))) + ([('c', i) for i in range(8)] if wheel else [])}
    for s in ['Q1', 'Q2', 'R1', 'R2']: P[s] = sq([0, 1, 2, 3])
    cl = []
    glue_arc(cl, 'P0', (0, 1), 'Q1', (0, 1)); glue_arc(cl, 'Q1', (2, 3), 'Q2', (0, 1)); glue_arc(cl, 'Q2', (2, 3), 'P0', (4, 5))
    glue_arc(cl, 'P0', (2, 3), 'R1', (0, 1)); glue_arc(cl, 'R1', (2, 3), 'R2', (0, 1)); glue_arc(cl, 'R2', (2, 3), 'P0', (6, 7))
    return build(P, cl)
report('crossed torus, bare octagon', torus(False))
report('crossed torus, W8', torus(True))
# 프리즘 띠 / 뫼비우스 띠 / 두 삼각형 / K4 두 사각형
def band(k, twist):
    P, cl = {}, []
    for i in range(k): P[i] = sq([('t',i),('t',i+1),('s',i+1),('s',i)])
    for i in range(1, k): cl += [[(i-1,('t',i)),(i,('t',i))], [(i-1,('s',i)),(i,('s',i))]]
    if twist: cl += [[(k-1,('t',k)),(0,('s',0))], [(k-1,('s',k)),(0,('t',0))]]
    else:     cl += [[(k-1,('t',k)),(0,('t',0))], [(k-1,('s',k)),(0,('s',0))]]
    return build(P, cl)
report('prism band k=3', band(3, 0)); report('prism band k=4', band(4, 0))
report('two triangles all 3 pts', build({1: sq([0,1,2]), 2: sq([0,1,2])}, [[(1,v),(2,v)] for v in range(3)]))
report('W6 u W6 straight arc', build({1: sq(list(range(6))) + [('c',i) for i in range(6)], 2: sq(list(range(6))) + [('c',i) for i in range(6)]},
       [[(1,0),(2,1)],[(1,1),(2,0)]]))
