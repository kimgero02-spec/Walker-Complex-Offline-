"""Does G contain a closed K_c-chain (c-cliques glued along (c-1)-cliques) with odd colour holonomy?
Z2-cocycle on the 'c-clique graph'; odd chain exists iff the cocycle is not a coboundary on some component."""
import itertools, networkx as nx

def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s

def odd_chain(G, c, witness=False):
    cl = [tuple(sorted(q)) for q in nx.enumerate_all_cliques(G) if len(q) == c]
    by_face = {}
    for q in cl:
        for f in itertools.combinations(q, c - 1):
            by_face.setdefault(f, []).append(q)
    adj = {q: [] for q in cl}
    for f, qs in by_face.items():
        for q1, q2 in itertools.combinations(qs, 2):
            # bijection: q1 sorted -> colours 0..c-1 ; transport to q2
            col = {v: i for i, v in enumerate(q1)}
            new2 = [v for v in q2 if v not in f][0]; old1 = [v for v in q1 if v not in f][0]
            col2 = {v: col[v] for v in f}; col2[new2] = col[old1]
            s = perm_sign([col2[v] for v in q2])     # relative to q2's sorted reference
            adj[q1].append((q2, s)); adj[q2].append((q1, s))
    lab = {}
    for q0 in cl:
        if q0 in lab: continue
        lab[q0] = 1; stack = [q0]
        while stack:
            q = stack.pop()
            for r, s in adj[q]:
                if r not in lab: lab[r] = lab[q] * s; stack.append(r)
                elif lab[r] != lab[q] * s: return True
    return False
