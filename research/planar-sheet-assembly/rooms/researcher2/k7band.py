# 예측 9 공격: 사다리(프리즘/뫼비우스, 가로대 7) -> K7 로 가는 변-전단사 사상, 각 사각형 단사.
# 그러면 K7 은 '조각=G 의 4-사이클, H=C_7(공유 변 기준)' 띠형 설명서를 가진다.
import sys, networkx as nx, itertools as it
sys.setrecursionlimit(10000)
def ladder(k, twist):
    G = nx.Graph()
    for i in range(k): G.add_edge(('a',i),('b',i))
    for i in range(k-1): G.add_edge(('a',i),('a',i+1)); G.add_edge(('b',i),('b',i+1))
    if twist: G.add_edge(('a',k-1),('b',0)); G.add_edge(('b',k-1),('a',0))
    else: G.add_edge(('a',k-1),('a',0)); G.add_edge(('b',k-1),('b',0))
    sq = []
    for i in range(k):
        j = i+1
        if j < k: sq.append([('a',i),('a',j),('b',j),('b',i)])
        else: sq.append([('a',i),('b',0),('a',0),('b',i)] if twist else [('a',i),('a',0),('b',0),('b',i)])
    return G, sq
def search(twist, N=7):
    L, sq = ladder(7, twist)
    order = [('a',i) for i in range(7)] + [('b',i) for i in range(7)]
    # BFS 순서로 재배열
    order = list(nx.bfs_tree(L, ('a',0)).nodes())
    f = {}; used = set()
    def ok_sq():
        for s in sq:
            img = [f[v] for v in s if v in f]
            if len(img) != len(set(img)): return False
        return True
    def rec(t):
        if t == len(order): return True
        v = order[t]
        for x in range(N):
            if t == 0 and x != 0: continue
            new = []
            good = True
            for u in L[v]:
                if u in f:
                    e = frozenset((x, f[u]))
                    if len(e) < 2 or e in used or e in new: good = False; break
                    new.append(e)
            if not good: continue
            f[v] = x
            if ok_sq():
                used.update(new)
                if rec(t+1): return True
                used.difference_update(new)
            del f[v]
        return False
    return (f, sq, L) if rec(0) else None
for tw in (False, True):
    r = search(tw)
    if r is None: print("twist", tw, "없음"); continue
    f, sq, L = r
    G = nx.Graph([(f[u], f[v]) for u, v in L.edges()])
    pieces = [[f[v] for v in s] for s in sq]
    # 공유 변 그래프
    def E(p): return {frozenset((p[i], p[(i+1)%4])) for i in range(4)}
    Hedges = [(i, j) for i in range(7) for j in range(i+1, 7) if E(pieces[i]) & E(pieces[j])]
    print("twist", tw, "G≅K7", nx.is_isomorphic(G, nx.complete_graph(7)), "조각", pieces)
    print("  공유변 H 변", Hedges, "H≅C7", nx.is_isomorphic(nx.Graph(Hedges), nx.cycle_graph(7)),
          "각 쌍 공유변 수", [len(E(pieces[i]) & E(pieces[j])) for i, j in Hedges])
