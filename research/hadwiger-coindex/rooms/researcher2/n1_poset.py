# Z2-poset map from face poset of B_0(G) to Q_k (nonzero signed vectors in {+,-,0}^k, inclusion order). SAT (pysat).
import itertools, networkx as nx, sys, time
from pysat.solvers import Cadical153
def faces(G):
    V=list(G.nodes()); n=len(V); idx={v:i for i,v in enumerate(V)}
    adj=[0]*n
    for u,v in G.edges(): adj[idx[u]]|=1<<idx[v]; adj[idx[v]]|=1<<idx[u]
    out=[]
    for B in range(1<<n):
        cn=(1<<n)-1
        for i in range(n):
            if B>>i&1: cn&=adj[i]
        A=cn
        while True:
            if A or B: out.append((A,B))
            if A==0: break
            A=(A-1)&cn
    return out,n
def Q(k):
    return [q for q in itertools.product((0,1,-1),repeat=k) if any(q)]
def leq(p,q): return all(a==0 or a==b for a,b in zip(p,q))
def poset_map(G,k,timeout=None):
    F,n=faces(G); Fi={f:i for i,f in enumerate(F)}
    Qs=Q(k); qi={q:j for j,q in enumerate(Qs)}; nq=len(Qs)
    var=lambda i,j:i*nq+j+1
    s=Cadical153()
    for i in range(len(F)):
        s.add_clause([var(i,j) for j in range(nq)])
        for j1 in range(nq):
            for j2 in range(j1+1,nq): s.add_clause([-var(i,j1),-var(i,j2)])
    neg=lambda q:tuple(-a for a in q)
    # equivariance: f(B,A) = -f(A,B)
    for (A,B),i in Fi.items():
        i2=Fi[(B,A)]
        if i2<i: continue
        for j,q in enumerate(Qs):
            s.add_clause([-var(i,j),var(i2,qi[neg(q)])])
            s.add_clause([-var(i2,j),var(i,qi[neg(q)])])
    # covering relations: remove one vertex
    for (A,B),i in Fi.items():
        subs=[]
        for t in range(n):
            if A>>t&1 and (A^(1<<t) or B): subs.append((A^(1<<t),B))
            if B>>t&1 and (A or B^(1<<t)): subs.append((A,B^(1<<t)))
        for sf in subs:
            i0=Fi[sf]
            for j0,q0 in enumerate(Qs):
                ok=[var(i,j) for j,q in enumerate(Qs) if leq(q0,q)]
                s.add_clause([-var(i0,j0)]+ok)
    # symmetry breaking: none
    r=s.solve()
    return r,len(F)
if __name__=="__main__":
    pass
