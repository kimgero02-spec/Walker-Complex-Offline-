import sys
from math import gcd
src=open('snf.py').read().split("def cyc")[0]
exec(src)
def inc(E,n,a,b): return B(E,n,a,b)
def mul(M):
    BT=[[M.a[i][j] for i in range(M.rows)] for j in range(M.cols)]
    n=M.cols
    return Matrix([[sum(BT[i][k]*M.a[k][j] for k in range(M.rows)) for j in range(n)] for i in range(n)])
def struct(M):
    d=SNFdiag(M.a); r=M.cols-len(d); t=[x for x in d if x!=1]
    return r,t
P5=[(i,i+1) for i in range(4)]
C6=[(i,(i+1)%6) for i in range(6)]
C5=[(i,(i+1)%5) for i in range(5)]
Q3=[(u,u^(1<<k)) for u in range(8) for k in range(3) if u<u^(1<<k)]
K33=[(i,3+j) for i in range(3) for j in range(3)]
K4=[(i,j) for i in range(4) for j in range(i+1,4)]
G={'P5':(P5,5),'C6':(C6,6),'Q3':(Q3,8),'K33':(K33,6),'C5':(C5,5),'K4':(K4,4)}
def hom(r,t,n):
    # Hom(Z^r + sum Z/d, Z/n) as string
    parts=[]
    if r: parts.append(f"(Z/{n})^{r}" if r>1 else f"Z/{n}")
    for d in t:
        g=gcd(d,n)
        if g>1: parts.append(f"Z/{g}")
    return "+".join(parts) if parts else "0"
for name,(E,n) in G.items():
    print("==",name)
    for lab,(a,b) in {'x=y (1,-1)':(1,-1),'x+y=0 (1,1)':(1,1)}.items():
        M=inc(E,n,a,b); r,t=struct(M); 
        L=mul(M); rl,tl=struct(L)
        print(lab,"A_G = Z^%d +"%r,t," | coker B^TB = Z^%d +"%rl,tl)
        print("   R^G:",{N:hom(r,t,N) for N in (2,3,4,6)})
        print("   harmonic Hom(coker B^TB,R):",{N:hom(rl,tl,N) for N in (2,3,4,6,9)})
