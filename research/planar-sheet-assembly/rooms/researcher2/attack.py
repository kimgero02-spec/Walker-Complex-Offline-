# R01 반례꾼 계산: 각 블록은 특정 반례/검증 하나에 대응한다 (대량 점검 아님).
import itertools as it
import networkx as nx
from networkx.algorithms import isomorphism as iso

def planar(G):
    return nx.check_planarity(G)[0]

def say(tag, *a):
    print(f"[{tag}]", *a)

# ---------- (3) 표 검증 ----------
# 3a. 두 5-사이클 상대위치: D5 \ S5 / D5
n = 5
C = [(i, (i + 1) % n) for i in range(n)]
def cyc_edges(perm):  # perm: 위치 i -> 정점 perm[i] 인 5-사이클의 변 집합
    return frozenset(frozenset((perm[i], perm[(i + 1) % n])) for i in range(n))
# 5-사이클 (라벨된) 집합 = S5 / D5 ; 고정 C0 에 대한 상대위치 = D5 궤도
C0 = cyc_edges(tuple(range(n)))
cycles = {cyc_edges(p) for p in it.permutations(range(n))}
say("3a", "라벨된 5-사이클 수", len(cycles))
# D5 = Aut(C0) 작용
D5 = [p for p in it.permutations(range(n)) if frozenset(frozenset((p[a], p[b])) for a, b in [tuple(e) for e in C0]) == C0]
def act(p, cyc):
    return frozenset(frozenset(p[v] for v in e) for e in cyc)
orbits = []
seen = set()
for c in cycles:
    if c in seen: continue
    orb = {act(p, c) for p in D5}
    seen |= orb
    orbits.append(orb)
say("3a", "|D5|", len(D5), "이중잉여류 수", len(orbits),
    "공유변 수", sorted(len(next(iter(o)) & C0) for o in orbits))
for o in orbits:
    c = next(iter(o))
    if len(c & C0) == 0:
        G = nx.Graph(); G.add_edges_from(tuple(e) for e in c | C0)
        say("3a", "공유0 궤도 크기", len(o), "합집합 ≅K5", nx.is_isomorphic(G, nx.complete_graph(5)))

# 3b. H* 피터슨
Hs = nx.Graph()
for i in range(5):
    Hs.add_edge(('o', i), ('o', (i + 1) % 5))
    Hs.add_edge(('i', i), ('i', (i + 2) % 5))
    Hs.add_edge(('o', i), ('i', i))
say("3b", "H* ≅ Petersen", nx.is_isomorphic(Hs, nx.petersen_graph()))

# 3c. 프리즘 / 뫼비우스
def ladder(k, twist, pinch=False):
    G = nx.Graph()
    for i in range(k):
        G.add_edge(('a', i), ('b', i))
    for i in range(k - 1):
        G.add_edge(('a', i), ('a', i + 1)); G.add_edge(('b', i), ('b', i + 1))
    L = k - 1
    if not pinch:
        if twist: G.add_edge(('a', L), ('b', 0)); G.add_edge(('b', L), ('a', 0))
        else:     G.add_edge(('a', L), ('a', 0)); G.add_edge(('b', L), ('b', 0))
    else:  # 닫는 조각이 삼각형 x->y->z, 공유변 xy(=e_L), yz(=e_0)
        if twist:  # y = a_L = b_0 , 새 변 z x = a_0 b_L
            G = nx.contracted_nodes(G, ('b', 0), ('a', L), self_loops=False)
            G.add_edge(('a', 0), ('b', L))
        else:      # y = a_L = a_0 , 새 변 b_0 b_L
            G = nx.contracted_nodes(G, ('a', 0), ('a', L), self_loops=False)
            G.add_edge(('b', 0), ('b', L))
        G = nx.Graph(G)
    return G
for k in range(2, 8):
    P = ladder(k, False); M = ladder(k, True)
    say("3c", f"k={k} prism planar={planar(P)} mobius planar={planar(M)}",
        "M≅K4" if k == 2 and nx.is_isomorphic(M, nx.complete_graph(4)) else "",
        "M≅circ(2k,[1,k])", nx.is_isomorphic(M, nx.circulant_graph(2 * k, [1, k])))
say("3c", "M6≅K33", nx.is_isomorphic(ladder(3, True), nx.complete_bipartite_graph(3, 3)))
say("3c", "prism k=2 (단순그래프화) =", sorted(d for _, d in ladder(2, False).degree()), "→ C4 (다중변 소실)")
# K7 = C7(1,2,3) 레이블: 걸음1->걸음s 사이클 정점대응은 x->s x
for s, t in [(1, 2), (1, 3), (2, 3)]:
    say("3d", f"걸음{s}->걸음{t} 인자", (t * pow(s, -1, 7)) % 7)
say("3d", "홀로노미 2*5*3^-1 mod 7 =", (2 * 5 * pow(3, -1, 7)) % 7)

# ---------- (2)(i) H 트리, 조각 평면, G 비평면 ----------
K = nx.Graph()
for c in (4, 5, 6):
    for x, y in it.combinations([1, 2, 3, c], 2): K.add_edge(x, y)
say("2i-A", "3개 K4 (삼각형 123 공유, H=별 K_{1,2}) G 평면?", planar(K),
    "K33 ⊂ G?", any(True for _ in [0]) and nx.is_isomorphic(nx.Graph([(a, b) for a in (1, 2, 3) for b in (4, 5, 6)]), nx.complete_bipartite_graph(3, 3)))
P2 = nx.complete_graph([1, 2, 3, 5, 6]); P2.remove_edge(5, 6)
P1 = nx.complete_graph([1, 2, 3, 4])
G = nx.compose(P1, P2)
say("2i-B", "K4 ∪_{123} (K5-56): P1,P2 평면", planar(P1), planar(P2), "G 평면", planar(G))
# 삼각형 123 이 K5-56 에서 면인가: 제거하면 5,6 분리 → 분리 삼각형
Q = P2.copy(); Q.remove_nodes_from([1, 2, 3])
say("2i-B", "K5-56 에서 {1,2,3} 제거 후 연결?", nx.is_connected(Q), "(비연결 → 분리 삼각형, 면 아님)")
A = nx.complete_bipartite_graph(2, 3)  # 0,1 | 2,3,4
B = nx.Graph([(5, 2), (5, 3), (5, 4)])
say("2i-C", "K23 ∪_{3 independent} K13 ≅ K33", nx.is_isomorphic(nx.compose(A, B), nx.complete_bipartite_graph(3, 3)))
P1 = nx.complete_graph(5); P1.remove_edge(0, 1)
P2 = nx.Graph([(0, 'w'), ('w', 1)])
G = nx.compose(P1, P2)
say("2i-D", "2점 공유(변 없음): K5-uv 평면", planar(P1), "G=K5-uv+u-w-v 평면", planar(G))

# ---------- (2)(ii)/(iii) 꼬인 핀치 띠 ----------
for k in range(3, 8):
    T = ladder(k, True, pinch=True); S = ladder(k, False, pinch=True)
    say("2ii", f"k={k} (조각 k개: 사각형 k-1 + 삼각형 1) twisted planar={planar(T)} straight planar={planar(S)} 동형={nx.is_isomorphic(T, S)}")

# ---------- 숨은 공유: 프리즘에서 비이웃 조각이 정점 공유 ----------
for k, j in [(6, 3), (4, 2)]:
    P = ladder(k, False)
    Pm = nx.Graph(nx.contracted_nodes(P, ('a', 0), ('b', j), self_loops=False))
    say("hid", f"prism k={k}, a0~b{j}: planar={planar(Pm)}")

# ---------- 원기둥 조각(프리즘)을 사이클로 공유, H=C_n, 레이블 항등 ----------
for m, nn in [(3, 3), (4, 3), (3, 5)]:
    T = nx.cartesian_product(nx.cycle_graph(m), nx.cycle_graph(nn))
    piece = nx.cartesian_product(nx.cycle_graph(m), nx.path_graph(2))
    say("cyl", f"C{m}xC{nn}: 조각 C{m}xK2 평면={planar(piece)}, G 평면={planar(T)}")

# ---------- 면 조각 모델: K7 토러스 ----------
def faces_surface(faces):
    # 각 변이 정확히 2개 면에, 일관된 방향 존재(가향) 검사, 정점 링크 단일 사이클 검사
    from collections import defaultdict
    occ = defaultdict(list)
    for fi, f in enumerate(faces):
        L = len(f)
        for t in range(L):
            occ[frozenset((f[t], f[(t + 1) % L]))].append(fi)
    two = all(len(v) == 2 for v in occ.values())
    # 방향 BFS
    sign = {0: 1}
    def dirs(f, s):
        L = len(f)
        return {(f[t], f[(t + 1) % L]) if s == 1 else (f[(t + 1) % L], f[t]) for t in range(L)}
    ok = True
    stack = [0]
    while stack:
        fi = stack.pop()
        D = dirs(faces[fi], sign[fi])
        for (u, v) in D:
            for fj in occ[frozenset((u, v))]:
                if fj == fi: continue
                s = 1 if (v, u) in dirs(faces[fj], 1) else -1
                if fj in sign:
                    if sign[fj] != s: ok = False
                else:
                    sign[fj] = s; stack.append(fj)
    dual = nx.MultiGraph()
    dual.add_nodes_from(range(len(faces)))
    for e, fs in occ.items():
        if len(fs) == 2: dual.add_edge(*fs)
    Vs = {v for f in faces for v in f}
    chi = len(Vs) - len(occ) + len(faces)
    return two, ok, chi, dual
f7 = [(i, (i + 1) % 7, (i + 3) % 7) for i in range(7)] + [(i, (i + 3) % 7, (i + 2) % 7) for i in range(7)]
two, ok, chi, dual = faces_surface(f7)
say("K7", "변 2회", two, "가향(홀로노미 자명)", ok, "χ", chi, "쌍대≅Heawood", nx.is_isomorphic(nx.Graph(dual), nx.heawood_graph()))
G = nx.Graph(); [G.add_edges_from([(f[0], f[1]), (f[1], f[2]), (f[2], f[0])]) for f in f7]
say("K7", "합집합≅K7", nx.is_isomorphic(G, nx.complete_graph(7)))

# 사영평면 K6: 10 삼각형 (반구 정이십면체 몫) → 홀로노미 비자명 예 비교
# 정이십면체 대척 몫
I = nx.icosahedral_graph()
pos = None

# 토러스 K33: 회전계로 면 추적
def trace(rot):
    # rot[v] = 이웃의 순환 순서. 면: (u,v) 다음 변 (v, rot[v] 에서 u 의 다음)
    darts = {(u, v) for u in rot for v in rot[u]}
    faces = []
    while darts:
        d = darts.pop(); f = [d[0]]
        u, v = d
        while True:
            r = rot[v]; w = r[(r.index(u) + 1) % len(r)]
            if (v, w) == d: break
            darts.discard((v, w)); f.append(v); u, v = v, w
        faces.append(tuple(f))
    return faces
# K33: a0,a1,a2 / b0,b1,b2 ; 회전 몇 개를 고정 시도 (소수 정선: 순환 대칭 회전계)
best = None
for ra in it.permutations([1, 2]):
    for rb in it.permutations([1, 2]):
        rot = {}
        for i in range(3):
            rot[('a', i)] = [('b', (i + 0) % 3)] + [('b', (i + x) % 3) for x in ra]
            rot[('b', i)] = [('a', (i + 0) % 3)] + [('a', (i - x) % 3) for x in rb]
        F = trace(rot)
        if len(F) == 3 and all(len(set(f)) == len(f) for f in F):
            best = F
say("K33", "토러스 회전계: 면", best)
if best:
    two, ok, chi, dual = faces_surface(best)
    say("K33", "변2회", two, "가향", ok, "χ", chi, "쌍대 변수", dual.number_of_edges(), "각 면 사이클 길이", [len(f) for f in best])

# ---------- 정의 공격: 같은 (조각, 'H 레이블 형식') 다른 G ----------
paw = nx.Graph([(0, 1), (1, 2), (2, 0), (2, 3)])
def glue(P, Q, e, f, flip=False):
    G = nx.disjoint_union(P, Q)
    m = P.number_of_nodes()
    u, v = e; x, y = f
    if flip: x, y = y, x
    G = nx.contracted_nodes(G, u, m + x, self_loops=False)
    G = nx.contracted_nodes(G, v, m + y, self_loops=False)
    return nx.Graph(G)
G1 = glue(paw, paw, (0, 1), (0, 1))
G2 = glue(paw, paw, (2, 3), (2, 3))
G3 = glue(paw, paw, (0, 1), (2, 3))
say("R1", "paw+paw 변 공유 '+' : 세 선택 쌍별 동형?", nx.is_isomorphic(G1, G2), nx.is_isomorphic(G1, G3), nx.is_isomorphic(G2, G3))
# 같은 변 (1,2) 에 + / - : paw 의 (2,3) 에 대해 ± 가 다르면?
Ga = glue(paw, paw, (2, 3), (2, 3), flip=False); Gb = glue(paw, paw, (2, 3), (2, 3), flip=True)
say("R1", "pendant 변 (2,3) 을 + 와 - 로: 동형?", nx.is_isomorphic(Ga, Gb), "단순성", Gb.number_of_edges())
# 일관성 실패: 세 삼각형, x1~y1, y1~z1, x1~z2 → z1~z2 (P3 의 변이 고리로)
M = nx.MultiGraph()
for p in 'xyz': M.add_edges_from([(p + '1', p + '2'), (p + '2', p + '3'), (p + '3', p + '1')])
uf = {v: v for v in M}
def find(v):
    while uf[v] != v: v = uf[v]
    return v
for a, b in [('x1', 'y1'), ('y1', 'z1'), ('x1', 'z2')]: uf[find(a)] = find(b)
Q = nx.MultiGraph(); Q.add_edges_from((find(u), find(v)) for u, v in M.edges())
say("R1", "세 삼각형 순환 접착: 고리 수", nx.number_of_selfloops(Q), "→ P3 가 G 에 단사로 안 들어감")
