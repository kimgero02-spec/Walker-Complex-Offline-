import sys, itertools
from tors import tors_group, disc3
def npts(a,b,c,p):
    cnt=1
    sq=[0]*p
    for y in range(p): sq[y*y%p]+=1
    for x in range(p): cnt+=sq[(x**3+a*x*x+b*x+c)%p]
    return cnt
def full(nu):
    # roots of Y-cubic: X=2nu_i ; a,b,c from prod (X-2nu)
    e=[2*v for v in nu]
    a=-(e[0]+e[1]+e[2]); b=e[0]*e[1]+e[0]*e[2]+e[1]*e[2]; c=-e[0]*e[1]*e[2]
    return a,b,c
def search(order_req,B):
    out=[]
    for r in range(1,B):
        for s in range(-B,B):
            if s in (0,r): continue
            a,b,c=full((0,r,s))
            D=disc3(a,b,c)
            if D==0: continue
            ok=True; goodp=0
            for p in (5,7,11,13,17,19,23):
                if D%p==0: continue
                goodp+=1
                if npts(a,b,c,p)%order_req: ok=False;break
            if ok and goodp>=4: out.append((r,s))
    return out
for req in (12,16):
    cands=search(req,int(sys.argv[1]))
    print("req",req,len(cands))
    shown=0
    for r,s in cands:
        a,b,c=full((0,r,s))
        size,o2,maxo,orders=tors_group(a,b,c)
        if size%req==0:
            print("nu=(0,%d,%d)"%(r,s),"size",size,"o2",o2,"maxorder",maxo); shown+=1
            if shown>=3: break
