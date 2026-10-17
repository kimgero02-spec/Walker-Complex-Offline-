# R06 반례꾼: 단순 연결성 점검. 2-골격의 기본군 presentation (스패닝트리, 삼각형 관계) 을 Tietze 소거로 줄인다.
# 결과 'trivial' 이면 π1=1 이 증명됨 (소거 전부 성공). 'stuck' 이면 판정 불가 (미결).
from itertools import combinations
from collections import deque

def free_reduce(w):
    out = []
    for x in w:
        if out and out[-1] == -x: out.pop()
        else: out.append(x)
    return out

def inv(w): return [-x for x in reversed(w)]

def pi1_presentation(vertices, edges, triangles):
    adj = {v: [] for v in vertices}
    for (a, b) in edges: adj[a].append(b); adj[b].append(a)
    root = vertices[0]; par = {root: None}; dq = deque([root]); tree = set()
    while dq:
        u = dq.popleft()
        for w in adj[u]:
            if w not in par:
                par[w] = u; dq.append(w); tree.add(frozenset((u, w)))
    gens = {}
    for (a, b) in edges:
        if frozenset((a, b)) not in tree:
            gens[(a, b)] = len(gens)+1
    def e(i, j):  # word for oriented edge i->j
        if frozenset((i, j)) in tree: return []
        if i < j: return [gens[(i, j)]]
        return [-gens[(j, i)]]
    rels = []
    for (i, j, k) in triangles:
        w = free_reduce(e(i, j) + e(j, k) + inv(e(i, k)))
        if w: rels.append(w)
    return len(gens), rels

def tietze(ngens, rels):
    rels = [r for r in rels if r]
    alive = set(range(1, ngens+1))
    changed = True
    while changed and rels:
        changed = False
        for ri, r in enumerate(rels):
            cnt = {}
            for x in r: cnt[abs(x)] = cnt.get(abs(x), 0) + 1
            cand = [g for g, c in cnt.items() if c == 1]
            if not cand: continue
            g = cand[0]
            p = [i for i, x in enumerate(r) if abs(x) == g][0]
            u, v = r[:p], r[p+1:]
            e = 1 if r[p] == g else -1
            # g^e = u^{-1} v^{-1}   (from u g^e v = 1)
            Wg = free_reduce(inv(u) + inv(v))  # this equals g^e
            W = Wg if e == 1 else inv(Wg)       # g = W
            new = []
            for j, s in enumerate(rels):
                if j == ri: continue
                out = []
                for x in s:
                    if abs(x) == g: out.extend(W if x == g else inv(W))
                    else: out.append(x)
                out = free_reduce(out)
                if out: new.append(out)
            rels = new; alive.discard(g); changed = True
            break
    return alive, rels
