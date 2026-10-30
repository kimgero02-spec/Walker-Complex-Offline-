import itertools, numpy as np
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy import ZZ
def circle(m):
    # m vertices, m edges; d(e_i)=v_{i+1}-v_i
    d1=np.zeros((m,m),dtype=int)
    for i in range(m): d1[(i+1)%m,i]+=1; d1[i,i]-=1
    return {0:m,1:m},{1:d1}
def tensor(A,B):
    (ra,da),(rb,db)=A,B
    ranks={}; basis={}
    for p in ra:
        for q in rb:
            basis.setdefault(p+q,[]).append((p,q))
    off={}
    for k,blocks in basis.items():
        o=0; off[k]={}
        for (p,q) in blocks: off[k][(p,q)]=o; o+=ra[p]*rb[q]
        ranks[k]=o
    D={}
    for k in ranks:
        if k-1 not in ranks: continue
        M=np.zeros((ranks[k-1],ranks[k]),dtype=int)
        for (p,q),o in off[k].items():
            if p in da and (p-1,q) in off[k-1]:
                blk=np.kron(da[p],np.eye(rb[q],dtype=int)); o2=off[k-1][(p-1,q)]
                M[o2:o2+blk.shape[0],o:o+blk.shape[1]]+=blk
            if q in db and (p,q-1) in off[k-1]:
                blk=((-1)**p)*np.kron(np.eye(ra[p],dtype=int),db[q]); o2=off[k-1][(p,q-1)]
                M[o2:o2+blk.shape[0],o:o+blk.shape[1]]+=blk
        D[k]=M
    return ranks,D
def homology(ranks,D):
    out={}
    def snf(M):
        if M.size==0: return []
        S=smith_normal_form(Matrix(M.tolist()),domain=ZZ)
        return [abs(S[i,i]) for i in range(min(S.shape)) if S[i,i]!=0]
    inv={k:snf(D[k]) if k in D else [] for k in ranks}
    for k in sorted(ranks):
        rk_dk=len(inv[k]); img=inv.get(k+1,[])
        free=ranks[k]-rk_dk-len(img)
        tors=[d for d in img if d>1]
        out[k]=(free,tors)
    return out
for n in range(1,5):
    C=circle(2 if n<4 else 2)
    X=C
    for _ in range(n-1): X=tensor(X,C)
    r,D=X
    for k in D: 
        if k-1 in D: assert not (D[k-1]@D[k]).any()
    print(n,"cells",r,homology(r,D))
# lens L(p,1): Z<-0-Z<-p-Z<-0-Z
for p in [2,3,5]:
    r={0:1,1:1,2:1,3:1}; D={1:np.array([[0]]),2:np.array([[p]]),3:np.array([[0]])}
    print("L",p,homology(r,D))
# Sigma_g
for g in [1,2,3]:
    r={0:1,1:2*g,2:1}; D={1:np.zeros((1,2*g),int),2:np.zeros((2*g,1),int)}
    print("Sigma",g,homology(r,D))
