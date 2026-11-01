import numpy as np, sys, random, itertools
from collections import defaultdict
from oagrp import OA
from burn import rank_mod
def key(P): return tuple(int(x) for x in P.flatten())
def classes(G,p):
    keys={key(P):i for i,P in enumerate(G)}
    n=len(G)
    # generators: random until generate
    random.seed(1)
    while True:
        gens=random.sample(range(n),2)
        S={key(np.eye(3,dtype=np.int64))}; frontier=[np.eye(3,dtype=np.int64)]
        while frontier:
            nf=[]
            for X in frontier:
                for gi in gens:
                    Y=(X@G[gi])%p
                    k=key(Y)
                    if k not in S: S.add(k); nf.append(Y)
            frontier=nf
        if len(S)==n: break
    def inv(P):
        # inverse in group: P^{-1} = A P^T A^{-1} ... compute via adjugate mod p
        import sympy
        return np.array(sympy.Matrix(P.tolist()).inv_mod(p)).astype(np.int64)
    gi=[(G[g],inv(G[g])) for g in gens]
    par=list(range(n))
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for i,P in enumerate(G):
        for g,gv in gi:
            j=keys[key((g@P@gv)%p)]
            a,b=find(i),find(j)
            if a!=b: par[a]=b
    cl=defaultdict(list)
    for i in range(n): cl[find(i)].append(i)
    return [(G[v[0]],len(v)) for v in cl.values()]
def run(p):
    G=OA(p); cls=classes(G,p)
    tot=0
    for P,a in cls:
        for Q,b in cls:
            K=np.kron(P,Q)%p
            d=9-rank_mod((K-np.eye(9,dtype=np.int64))%p,p)
            tot+=a*b*p**d
    from fractions import Fraction
    return Fraction(tot,len(G)**2),len(cls)
if __name__=="__main__":
    for p in map(int,sys.argv[1:]):
        print(p,run(p),flush=True)
