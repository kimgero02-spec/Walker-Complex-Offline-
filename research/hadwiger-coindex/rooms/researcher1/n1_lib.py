import itertools, random, numpy as np, networkx as nx
def maxbic(G):
    n=G.number_of_nodes(); V=list(range(n))
    nb=[0]*n
    for u,v in G.edges(): nb[u]|=1<<v; nb[v]|=1<<u
    full=(1<<n)-1
    com=[full]*(1<<n)
    for m in range(1,1<<n):
        low=m&-m; com[m]=com[m^low]&nb[low.bit_length()-1]
    S=set()
    for m in range(1,1<<n):
        B=com[m]
        if not B: continue
        A=com[B]; B2=com[A]
        S.add(frozenset([A,B2]))
    return [tuple(sorted(p)) if len(p)==2 else (list(p)[0],list(p)[0]) for p in S]
def bl(m): return [i for i in range(m.bit_length()) if m>>i&1]
def rho(G, pairs, cap=None):
    n=G.number_of_nodes()
    P=[(bl(a),bl(b)) for a,b in pairs]
    best=99; bo=None
    for perm in itertools.permutations(range(n)):
        pos=[0]*n
        for i,v in enumerate(perm): pos[v]=i
        mx=0
        for A,B in P:
            seq=sorted([(pos[a],0) for a in A]+[(pos[b],1) for b in B])
            r=1+sum(1 for i in range(len(seq)-1) if seq[i][1]!=seq[i+1][1])
            if r>mx:
                mx=r
                if mx>=best: break
        if mx<best: best=mx; bo=perm
    return best,bo
def orient(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
def segcross(a,b,c,d):
    return orient(a,b,c)*orient(a,b,d)<0 and orient(c,d,a)*orient(c,d,b)<0
def inhull(p,pts):
    if len(pts)==1: return False
    if len(pts)==2: return False
    for i in range(len(pts)):
        for j in range(i+1,len(pts)):
            for k in range(j+1,len(pts)):
                o=[orient(pts[i],pts[j],p),orient(pts[j],pts[k],p),orient(pts[k],pts[i],p)]
                if all(x>0 for x in o) or all(x<0 for x in o): return True
    return False
def meet(PA,PB):
    for a,b in itertools.product(PA,PB):
        pass
    for i in range(len(PA)):
        for j in range(i+1,len(PA)):
            for k in range(len(PB)):
                for l in range(k+1,len(PB)):
                    if segcross(PA[i],PA[j],PB[k],PB[l]): return True
    for p in PA:
        if inhull(p,PB): return True
    for p in PB:
        if inhull(p,PA): return True
    return False
def viol(Y,P):
    c=0
    for A,B in P:
        if meet([Y[a] for a in A],[Y[b] for b in B]): c+=1
    return c
def search(n,P,iters=3000,restarts=30,seed=0):
    rng=random.Random(seed)
    for r in range(restarts):
        Y=[(rng.random(),rng.random()) for _ in range(n)]
        v=viol(Y,P)
        for it in range(iters):
            if v==0: return Y
            i=rng.randrange(n); old=Y[i]
            s=rng.choice([1,.3,.05])
            Y[i]=(old[0]+rng.gauss(0,s),old[1]+rng.gauss(0,s))
            v2=viol(Y,P)
            if v2<=v: v=v2
            else: Y[i]=old
        if v==0: return Y
    return None
