import numpy as np, sys, random, itertools
from collections import defaultdict, Counter
from oagrp import OA
from ns import key
def run(p):
    G=OA(p); random.seed(3)
    
    def closure(gs):
        I=np.eye(3,dtype=np.int64); S={key(I)}; fr=[I]
        while fr:
            nf=[]
            for X in fr:
                for g in gs:
                    Y=(X@g)%p; k=key(Y)
                    if k not in S: S.add(k); nf.append(Y)
            fr=nf
        return len(S)
    while True:
        gens=random.sample(G,4)
        if closure(gens)==len(G): break
    n=p**9
    idx=np.arange(n)
    digs=[(idx//p**(8-k))%p for k in range(9)]
    M=np.stack(digs,1).reshape(n,3,3).astype(np.int64)
    w=p**np.arange(8,-1,-1)
    def index(F): return F.reshape(n,9)@w
    perms=[]
    for g in gens:
        perms.append(index((g@M)%p))           # left
        perms.append(index((M@g.T)%p))         # right
    lab=idx.copy()
    for it in range(400):
        new=lab.copy()
        for pm in perms:
            new=np.minimum(new,lab[pm]); 
        # also inverse direction through scatter
        for pm in perms:
            np.minimum.at(new,pm,lab)
        if (new==lab).all(): break
        lab=new
    print("iterations",it)
    return M,lab
def invariants(M,p):
    Ainv=np.array([[(-1)%p,(pow(2,-1,p))%p,(pow(2,-1,p))%p],[pow(2,-1,p),(-1)%p,pow(2,-1,p)],[pow(2,-1,p),pow(2,-1,p),(-1)%p]])
    # A^{-1}=J/2 - I
    S=(M@Ainv@M.transpose(0,2,1))%p
    return S
def rank_arr(M,p):
    return np.array([rank3(m,p) for m in M[:0]])
if __name__=="__main__":
    p=int(sys.argv[1])
    M,lab=run(p)
    print("orbits",len(np.unique(lab)))
    np.save(f"lab{p}.npy",lab)
