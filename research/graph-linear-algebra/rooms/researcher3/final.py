import sys, numpy as np
from collections import defaultdict
from lib import *
from descent import *
import gsel
from scan import points
def enum(f,B):
    a1,a2,a3=f; r=np.arange(-B,B+1,dtype=np.int64); out=[]
    m12,m13,m22,m23,m33=np.meshgrid(r,r,r,r,r,indexing='ij')
    for m11 in range(-B,B+1):
        g2=m11-2*m12-2*m13+m22-2*m23+m33
        mask=(g2==2*a1)
        g1=-2*m11*m23+2*m12*m13+2*m12*m23-2*m12*m33-2*m13*m22+2*m13*m23
        mask&=(g1==2*a2)
        g0=-m11*m22*m33+m11*m23**2+m12**2*m33-2*m12*m13*m23+m13**2*m22
        mask&=(g0==2*a3)
        for k in range(int(mask.sum())):
            out.append((m11,)+tuple(int(a[mask][k]) for a in (m12,m13,m22,m23,m33)))
    return out
th=tuple(int(x) for x in sys.argv[1:4]); B=int(sys.argv[4]); NP=int(sys.argv[5]) if len(sys.argv)>5 else 0
f=(-sum(th), th[0]*th[1]+th[0]*th[2]+th[1]*th[2], -th[0]*th[1]*th[2])
S,sel,ker=gsel.selmer(th); places=[0]+S
print("theta",th,"f=t^3+%dt^2+%dt+%d"%f,"S",S,"|Sel2|",len(sel),"dim",len(sel).bit_length()-1)
# points -> classes
cls=set()
def dvec(d): return tuple(sqf_frac(x) for x in d)
for i in range(3):
    d=[None]*3
    for j in range(3):
        if j!=i: d[j]=2*(th[i]-th[j])
    d[i]=Fraction(fp(th,i)); cls.add(dvec(d))
cls.add((1,1,1))
# E: y^2=X(X-2m)(X-2n) with X=2t  : points from points(m,n)
m,n=th[1],th[2]
P=points(m,n,400,8)
for X,y in P:
    t=X/2; cls.add(dvec([2*(t-th[i]) for i in range(3)]))
# group generated
def mul(d,e): return tuple(squarefree(a*b) for a,b in zip(d,e))
grp=set(cls); ch=True
while ch:
    ch=False
    for a in list(grp):
        for b in list(grp):
            c=mul(a,b)
            if c not in grp: grp.add(c); ch=True
print("subgroup gen by torsion + found points: size",len(grp),"equals Sel2:",grp==set(sel))
Ms=enum(f,B)
byd=defaultdict(list)
for mm in Ms:
    Mm=[[mm[0],mm[1],mm[2]],[mm[1],mm[3],mm[4]],[mm[2],mm[4],mm[5]]]
    byd[gsel.delta_of_M(th,sp.Matrix(Mm))].append(mm)
print("B",B,"#M",len(Ms),"#Q-orbits met",len(byd),"(all in global ker:",all(d in ker for d in byd),")")
good=set()
for d,l in sorted(byd.items()):
    mm=l[0]; c=quartic([[mm[0],mm[1],mm[2]],[mm[1],mm[3],mm[4]],[mm[2],mm[4],mm[5]]])
    sol=[solv_quartic(c,v) for v in places]
    ok=all(sol)
    if ok: good.add(d)
    print(d,"#M",len(l),"in Sel2:",d in sel,"loc.solv",dict(zip(places,sol)))
print("locally soluble orbits",len(good),"subset of Sel2:",good<=set(sel),"missed Sel2:",sorted(set(sel)-good))
