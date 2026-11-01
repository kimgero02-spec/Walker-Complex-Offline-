"""R48 망상꾼: Alon-Tarsi 계수 계산 (정량적 CN 공식), 소수 정선된 예만."""
from fractions import Fraction
import itertools, sys
import networkx as nx

def coef(n, edges, t):
    """[x^t] prod_{(u,v) in edges, u<v} (x_u - x_v),  sum t = |E| 필요.
    공식: sum_{c in prod A_v, c proper} P(c)/prod phi_v'(c_v), A_v={0..t_v}."""
    E = [(min(u, v), max(u, v)) for u, v in edges]
    assert sum(t) == len(E)
    adj = [[] for _ in range(n)]
    for u, v in E:
        adj[u].append(v); adj[v].append(u)
    from math import factorial
    def dphi(v, a):
        return factorial(a) * factorial(t[v] - a) * (-1) ** (t[v] - a)
    order = sorted(range(n), key=lambda v: -len(adj[v]))
    pos = {v: i for i, v in enumerate(order)}
    c = [None] * n
    total = Fraction(0)
    def rec(i):
        nonlocal total
        if i == n:
            p = 1
            for u, v in E:
                p *= (c[u] - c[v])
            d = 1
            for v in range(n):
                d *= dphi(v, c[v])
            total += Fraction(p, d)
            return
        v = order[i]
        for a in range(t[v] + 1):
            if all(c[w] != a for w in adj[v] if pos[w] < i):
                c[v] = a
                rec(i + 1)
        c[v] = None
    rec(0)
    assert total.denominator == 1
    return int(total)

def coef_brute(n, edges, t):
    """직접 전개 (상한 t 로 가지치기)."""
    poly = {tuple([0]*n): 1}
    for u, v in edges:
        u, v = min(u, v), max(u, v)
        nxt = {}
        for m, c in poly.items():
            for w, s in ((u, 1), (v, -1)):
                if m[w] + 1 <= t[w]:
                    mm = list(m); mm[w] += 1; mm = tuple(mm)
                    nxt[mm] = nxt.get(mm, 0) + s * c
        poly = {m: c for m, c in nxt.items() if c}
    return poly.get(tuple(t), 0)

def proper_coloring(n, edges, lists):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    order = sorted(range(n), key=lambda v: (len(lists[v]), -len(adj[v])))
    c = {}
    def rec(i):
        if i == n:
            return True
        v = order[i]
        for a in lists[v]:
            if all(c.get(w) != a for w in adj[v]):
                c[v] = a
                if rec(i + 1):
                    return True
                del c[v]
        return False
    return dict(c) if rec(0) else None

def all_colorings(n, edges, k):
    """모든 k-색칠 (작은 그래프 전용)."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    c = [None] * n
    out = []
    def rec(i):
        if i == n:
            out.append(tuple(c)); return
        for a in range(k):
            if all(c[w] != a for w in adj[i] if w < i):
                c[i] = a; rec(i + 1)
        c[i] = None
    rec(0)
    return out
