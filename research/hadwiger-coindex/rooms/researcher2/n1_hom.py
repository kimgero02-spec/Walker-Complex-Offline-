# Z2-poset map from Hom(K2,G) cell poset {(A,B): A,B nonempty, AxB in E} to Q_k.
import itertools, networkx as nx, sys, time
from pysat.solvers import Cadical153
from n1_poset import faces, Q, leq
def hom_map(G,k,assume=None):
    F,n=faces(G); F=[f for f in F if f[0] and f[1]]
    Fi={f:i for i,f in enumerate(F)}
    Qs=Q(k); qi={q:j for j,q in enumerate(Qs)}; nq=len(Qs)
    var=lambda i,j:i*nq+j+1
    s=Cadical153()
    for i in range(len(F)):
        s.add_clause([var(i,j) for j in range(nq)])
        for j1 in range(nq):
            for j2 in range(j1+1,nq): s.add_clause([-var(i,j1),-var(i,j2)])
    neg=lambda q:tuple(-a for a in q)
    for (A,B),i in Fi.items():
        i2=Fi[(B,A)]
        if i2<i: continue
        for j,q in enumerate(Qs):
            s.add_clause([-var(i,j),var(i2,qi[neg(q)])])
            s.add_clause([-var(i2,j),var(i,qi[neg(q)])])
    for (A,B),i in Fi.items():
        subs=[]
        for t in range(n):
            if A>>t&1 and (A^(1<<t)): subs.append((A^(1<<t),B))
            if B>>t&1 and (B^(1<<t)): subs.append((A,B^(1<<t)))
        for sf in subs:
            i0=Fi[sf]
            for j0,q0 in enumerate(Qs):
                ok=[var(i,j) for j,q in enumerate(Qs) if leq(q0,q)]
                s.add_clause([-var(i0,j0)]+ok)
    return s.solve(),len(F)
