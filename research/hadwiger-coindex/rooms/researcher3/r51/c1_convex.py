# C1: convex K_n into ceil(n/2) non-crossing layers; interlayer crossing matrix
import itertools, sys
from pysat.solvers import Glucose4
def cross(e,f):
    a,b=sorted(e); c,d=sorted(f)
    if len({a,b,c,d})<4: return False
    return (a<c<b) != (a<d<b)
def zigzag(n):
    p=n//2; layers=[]
    for i in range(p):
        # zigzag path starting at i: i, i+1, i-1, i+2, i-2,...
        seq=[i]; l=i; r=i
        while len(seq)<n:
            r=(r+1)%n; seq.append(r)
            if len(seq)<n: l=(l-1)%n; seq.append(l)
        layers.append({tuple(sorted(e)) for e in zip(seq,seq[1:])})
    return layers
for n in [6,8,10]:
    L=zigzag(n)
    allE={tuple(sorted(e)) for e in itertools.combinations(range(n),2)}
    assert set().union(*L)==allE and sum(map(len,L))==len(allE)
    for l in L: assert not any(cross(e,f) for e,f in itertools.combinations(l,2))
    M=[[sum(cross(e,f) for e in L[i] for f in L[j]) for j in range(len(L))] for i in range(len(L))]
    print("n",n,"zigzag interlayer crossing matrix",M,"total",sum(M[i][j] for i in range(len(L)) for j in range(i+1,len(L))),"C(n,4)=",len(list(itertools.combinations(range(n),4))))
# count all 3-layer partitions of convex K6 chords (diagonals only; hull edges free) up to layer permutation
for n in [6]:
    D=[e for e in itertools.combinations(range(n),2) if (e[1]-e[0])%n not in (1,n-1)]
    k=(n+1)//2
    cnt=0; mats=set()
    for col in itertools.product(range(k),repeat=len(D)):
        if col[0]!=0: continue
        ok=all(col[i]!=col[j] for i,j in itertools.combinations(range(len(D)),2) if cross(D[i],D[j]))
        if ok:
            cnt+=1
            sizes=tuple(sorted(col.count(c) for c in range(k)))
            mats.add(sizes)
    print("n",n,"proper",k,"-colorings of circle graph (first chord fixed color 0):",cnt,"layer size patterns",mats)
