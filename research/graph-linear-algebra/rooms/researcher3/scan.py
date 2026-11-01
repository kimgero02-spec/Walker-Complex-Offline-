import gsel
from descent import *
from math import isqrt
def points(m,n,Ub=3000,Vb=12):
    pts=[]
    for v in range(1,Vb):
        for u in range(-Ub,Ub*3):
            if gcd(u,v)!=1: continue
            # X=u/v^2 ; y^2 = u(u-2m v^2)(u-2n v^2)/v^6
            P=u*(u-2*m*v*v)*(u-2*n*v*v)
            if P<0: continue
            r=isqrt(P)
            if r*r==P and v>1 and P!=0: pts.append((Fraction(u,v*v),Fraction(r,v**3)))
    return pts
if __name__=="__main__":
  for m in range(1,9):
      for n in range(-9,0):
          th=(0,m,n)
          S,sel,ker=gsel.selmer(th)
          pts=points(m,n,400,8) 
          print(th,"|S|",len(S),"dim Sel2",len(sel).bit_length()-1,"nonintegral-X pts found:",len(pts), pts[:1],flush=True)
