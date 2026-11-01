"""explicit odd solution a for C_7^2, C_8^2 (E criterion) and list of their 4-cycles"""
import networkx as nx, itertools
from r04 import chain
from r05 import four_cycles
from zlift import int_kernel
for m in (7, 8):
    G = chain(m, [3]*m)[0]
    E = sorted(tuple(sorted(e)) for e in G.edges()); ei = {e:i for i,e in enumerate(E)}
    Q = four_cycles(G); rows = []
    for q in Q:
        r = [0]*len(E)
        for i in range(4):
            x,y = q[i], q[(i+1)%4]; r[ei[tuple(sorted((x,y)))]] += 1 if x<y else -1
        rows.append(r)
    K = int_kernel(rows, len(E))
    # find odd combination: solve over F2 then lift
    import numpy as np
    n=len(E); B=[[v%2 for v in k] for k in K]
    # gaussian elimination to express all-ones
    best=None
    for coeffs in itertools.product((0,1), repeat=len(K)) if len(K)<=16 else []:
        s=[sum(c*k[i] for c,k in zip(coeffs,K)) for i in range(n)]
        if all(x%2 for x in s):
            if best is None or max(map(abs,s))<max(map(abs,best)): best=s
    print(m, "#edges", n, "#4-cycles", len(Q), "kernel rank", len(K))
    print("  a (edge u<v oriented u->v):", {e: best[ei[e]] for e in E})
    nonch=[q for q in Q if not (G.has_edge(q[0],q[2]) or G.has_edge(q[1],q[3]))]
    print("  induced 4-cycles:", nonch)
