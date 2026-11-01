import numpy as np, itertools, sys
from lib import *
from descent import fp, primes_S
import gsel
def enum(f,B):
    a1,a2,a3=f
    r=np.arange(-B,B+1,dtype=np.int64)
    m11,m12,m13,m22,m23,m33=np.meshgrid(r,r,r,r,r,r,indexing='ij')
    g2=m11-2*m12-2*m13+m22-2*m23+m33
    mask=(g2==2*a1)
    g1=-2*m11*m23+2*m12*m13+2*m12*m23-2*m12*m33-2*m13*m22+2*m13*m23
    mask&=(g1==2*a2)
    g0=-m11*m22*m33+m11*m23**2+m12**2*m33-2*m12*m13*m23+m13**2*m22
    mask&=(g0==2*a3)
    idx=np.nonzero(mask)
    return [tuple(int(x[i]) for x in (m11,m12,m13,m22,m23,m33)) for i in zip(*[ii for ii in idx])] if False else \
           [tuple(int(a[k]) for a in (m11[mask],m12[mask],m13[mask],m22[mask],m23[mask],m33[mask])) for k in range(mask.sum())]
if __name__=="__main__":
    th=tuple(int(x) for x in sys.argv[1:4]); B=int(sys.argv[4])
    f=(-sum(th), th[0]*th[1]+th[0]*th[2]+th[1]*th[2], -th[0]*th[1]*th[2])
    Ms=enum(f,B)
    print("f coeffs",f,"B",B,"#M",len(Ms))
    S,sel,ker=gsel.selmer(th)
    places=[0]+S
    from collections import defaultdict
    byd=defaultdict(list)
    for m in Ms:
        M=sp.Matrix([[m[0],m[1],m[2]],[m[1],m[3],m[4]],[m[2],m[4],m[5]]])
        d=gsel.delta_of_M(th,M)
        byd[d].append(m)
    print("Sel2",sel)
    for d,l in sorted(byd.items()):
        m=l[0]
        c=quartic([[m[0],m[1],m[2]],[m[1],m[3],m[4]],[m[2],m[4],m[5]]])
        sol=[solv_quartic(c,v) for v in places]
        print(d,"#M",len(l),"in Sel:",d in sel,"in glob ker:",d in ker,"loc.solv",dict(zip(places,sol)),"rep",m)
    print("Sel elements not hit:",[d for d in sel if d not in byd])
