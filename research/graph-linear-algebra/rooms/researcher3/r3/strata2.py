import numpy as np, sys
from collections import Counter, defaultdict
p=int(sys.argv[1]); lab=np.load(f"lab{p}.npy")
n=p**9
idx=np.arange(n)
M=np.stack([(idx//p**(8-k))%p for k in range(9)],1).reshape(n,3,3).astype(np.int64)
inv2=pow(2,-1,p)
Ainv=(inv2*np.ones((3,3),dtype=np.int64)-np.eye(3,dtype=np.int64))%p
A=np.array([[0,1,1],[1,0,1],[1,1,0]])
assert ((A@Ainv)%p==np.eye(3)).all()
phi=(Ainv@M)%p
ps=(Ainv@phi.transpose(0,2,1)@A)%p
H=(ps@phi)%p
tr=(H[:,0,0]+H[:,1,1]+H[:,2,2])%p
H2=(H@H)%p
tr2=(H2[:,0,0]+H2[:,1,1]+H2[:,2,2])%p
det=(np.round(np.linalg.det(H.astype(float))).astype(np.int64))%p
# charpoly t^3 - e1 t^2 + e2 t - e3
e1=tr; e2=((tr*tr-tr2)*inv2)%p; e3=det
key=(e1*p+e2)*p+e3
orb=defaultdict(set)
for k,l in zip(key,lab): orb[int(k)].add(int(l))
res=Counter()
for k,v in orb.items():
    res[len(v)]+=1
print(sorted(res.items()))
# detail for split squarefree h with nonzero e3
def roots(e1,e2,e3):
    return [x for x in range(p) if (x**3-e1*x*x+e2*x-e3)%p==0]
for k,v in sorted(orb.items()):
    e3_=k%p; e2_=(k//p)%p; e1_=k//p//p
    r=roots(e1_,e2_,e3_)
    if len(r)==3 and len(set(r))==3: print("split",r,len(v),"e3",e3_); 
print("----")
# rank of M
def rank3(m):
    from burn import rank_mod
    return rank_mod(m.tolist(),p)
u,first=np.unique(lab,return_index=True)
cnt=Counter()
def mults(e1,e2,e3):
    r=roots(e1,e2,e3)
    if not r: return ()
    c=[1,(-e1)%p,e2,(-e3)%p]; m={}
    for x in r:
        k=0; cur=c[:]
        while len(cur)>1:
            q=[cur[0]]
            for z in cur[1:-1]: q.append((z+q[-1]*x)%p)
            if (cur[-1]+q[-1]*x)%p==0: k+=1;cur=q
            else: break
        m[x]=k
    return tuple(sorted(m.values(),reverse=True))
for i in first:
    kk=int(key[i]); e3_=kk%p; e2_=(kk//p)%p; e1_=kk//p//p
    rk=rank3(M[i])
    dd=int(np.round(np.linalg.det(M[i].astype(float))))%p
    dc=0 if dd==0 else (1 if pow(dd,(p-1)//2,p)==1 else -1)
    e3c=0 if e3_==0 else (1 if pow(e3_,(p-1)//2,p)==1 else -1)
    cnt[(rk,mults(e1_,e2_,e3_),e3c)]+=1
for k,v in sorted(cnt.items()): print(k,v)
