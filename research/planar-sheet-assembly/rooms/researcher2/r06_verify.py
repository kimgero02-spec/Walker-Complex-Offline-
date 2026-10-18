# R06: 추측 R5 독립 재검증. (a) E-현->S 가지가 강제되는 n=7 삼각분할 G7 을 손으로 구성,
# (b) R05 solve 를 그 위에서 실행해 흐름 기록, (c) 독립 정확 판정기(L+T삼각형의 5-색칠)로 구조적 후보 점검.
import itertools, sys
import networkx as nx
sys.path.insert(0, '.')
import r05_r5 as R

def exact5(L, T):
    """독립 판정: L + {xy,yz,zx} 의 5-색칠 (단순 백트래킹, R05 코드와 별개)."""
    G = nx.Graph(L); G.add_edges_from(itertools.combinations(T, 2))
    nodes = sorted(G, key=lambda u: -G.degree(u)); c = {}
    def rec(i):
        if i == len(nodes): return True
        u = nodes[i]; used = {c[w] for w in G[u] if w in c}
        for k in range(5):
            if k not in used:
                c[u] = k
                if rec(i + 1): return True
                del c[u]
        return False
    return dict(c) if rec(0) else None

def four_col_T_mono_forced(L, T):
    """모든 4-색칠에서 T 가 단색인가 (= T 의 두 점 x,y 에 대해 c(x)!=c(y) 인 4-색칠이 없음)."""
    for x, y in itertools.combinations(T, 2):
        if R.color(L, 4, neq=[(x, y)]) is not None: return False
    return True

def stack(G, face, name):
    G.add_node(name); G.add_edges_from((name, f) for f in face)

# (a) G7: K4 = {w0,p,q,r}, w0 를 품는 세 면에 x,y,z 를 쌓음 (면 pqr 은 비움)
G7 = nx.complete_graph(['w0', 'p', 'q', 'r'])
stack(G7, ('w0', 'p', 'q'), 'x'); stack(G7, ('w0', 'q', 'r'), 'y'); stack(G7, ('w0', 'r', 'p'), 'z')
T7 = ('x', 'y', 'z')

def report(name, L, T):
    assert nx.check_planarity(L)[0]
    assert all(not L.has_edge(a, b) for a, b in itertools.combinations(T, 2))
    tri = L.number_of_edges() == 3 * L.number_of_nodes() - 6
    nonT = {v: L.degree(v) for v in L if v not in T}
    R.LOG.clear(); c = R.solve(L, T)
    ok = R.proper(L, c) and R.rainbow(c, T) and max(c.values()) <= 4
    ex = exact5(L, T)
    mono = four_col_T_mono_forced(L, T)
    print(f'{name}: n={L.number_of_nodes()} 삼각분할={tri} T밖 최소차수={min(nonT.values())} '
          f'모든4색에서T단색={mono} | solve 흐름={R.LOG} 출력적정무지개={ok} | 독립판정 5색무지개={ex is not None}')
    return c

print('== (a)(b) G7 ==  (주의: LOG 는 후위순서 — 가장 깊은 재귀가 먼저 기록됨)')
print('차수:', dict(G7.degree()))
_, emb = nx.check_planarity(G7)
for v in ('p', 'q', 'r'):
    print(v, '회전:', list(emb.neighbors_cw_order(v)))
c = report('G7', G7, T7); print('solve 색칠:', c)

# G7 변형: 면 pqr 에 정점 s 를 쌓음 -> p,q,r 차수 6, s 차수 3 (T 밖) -> D 가 먼저
G7s = nx.Graph(G7); stack(G7s, ('p', 'q', 'r'), 's'); report('G7+s', G7s, T7)

print('== (c) 구조적 후보 ==')
# 정이십면체: 모든 독립 삼중쌍 (자기동형 궤도 대표만)
I = nx.icosahedral_graph()
GM = nx.algorithms.isomorphism.GraphMatcher(I, I)
autos = list(GM.isomorphisms_iter())
seen = set(); reps = []
for t in itertools.combinations(I, 3):
    if any(I.has_edge(a, b) for a, b in itertools.combinations(t, 2)): continue
    key = min(tuple(sorted(m[u] for u in t)) for m in autos)
    if key not in seen: seen.add(key); reps.append(t)
for t in reps: report(f'정이십면체 T={t}', I, t)

# 유일 4-색칠 적층 삼각분할 (n=12): K4 에서 시작해 면마다 쌓기, T 는 한 색 클래스에서 면을 공유하지 않는 세 점
def stacked(depth_faces):
    G = nx.complete_graph(4); faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]; nxt = 4
    for idx in depth_faces:
        f = faces.pop(idx); stack(G, f, nxt)
        faces += [(f[0], f[1], nxt), (f[0], f[2], nxt), (f[1], f[2], nxt)]; nxt += 1
    return G
for seq in ([0, 3, 6, 9, 2, 5, 8, 11], [3, 3, 3, 3, 3, 3, 3, 3], [0, 0, 0, 0, 0, 0, 0, 0], [1, 4, 2, 7, 5, 10, 3, 12]):
    S = stacked(seq); c4 = R.color(S, 4)
    cls = [v for v in S if c4[v] == c4[0]]
    done = 0
    for t in itertools.combinations(cls, 3):
        if all(not S.has_edge(a, b) for a, b in itertools.combinations(t, 2)):
            report(f'적층 seq={seq} T={t}', S, t); done += 1
            if done >= 2: break

# 4-연결: C_5 이중바퀴(=n7), 팔면체 기반 (n=6, 독립 3점 없음 확인), C_8 반프리즘+두 극 n=18 은 범위 밖 -> C_5 반프리즘+두 극 n=12
def antiprism_poles(k):
    G = nx.Graph()
    for i in range(k):
        G.add_edges_from([(('a', i), ('a', (i + 1) % k)), (('b', i), ('b', (i + 1) % k)),
                          (('a', i), ('b', i)), (('a', i), ('b', (i + 1) % k))])
        G.add_edge('N', ('a', i)); G.add_edge('S', ('b', i))
    return G
A5 = antiprism_poles(5)
report('C5 반프리즘+극, T={N,a0,..}', A5, ('N', ('b', 0), ('b', 2)))
report('C5 반프리즘+극, T=(a0,a2,b4)', A5, (('a', 0), ('a', 2), ('b', 4)))
