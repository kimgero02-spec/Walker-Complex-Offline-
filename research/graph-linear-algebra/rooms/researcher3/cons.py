import sys
from box import *
from descent import kummer_image, clsvec
ths=[(0,2,-2),(0,1,3),(0,-1,4),(1,2,-3),(0,3,-5),(0,1,-1)]
B=int(sys.argv[1]) if len(sys.argv)>1 else 4
tot=0;bad=0
for th in ths:
    f=(-sum(th), th[0]*th[1]+th[0]*th[2]+th[1]*th[2], -th[0]*th[1]*th[2])
    Ms=enum(f,B)
    S=primes_S(th); places=sorted(set([0,2,3,5]+S))
    imgs={v:kummer_image(th,v,40)[0] for v in places}
    seen=set(); n=0; nb=0
    for m in Ms:
        Mm=[[m[0],m[1],m[2]],[m[1],m[3],m[4]],[m[2],m[4],m[5]]]
        d=gsel.delta_of_M(th,sp.Matrix(Mm))
        c=quartic(Mm)
        for v in places:
            s=solv_quartic(c,v)
            pred=clsvec(d,v) in imgs[v]
            tot+=1;n+=1
            if s is None or s!=pred: bad+=1;nb+=1;print("MISMATCH",th,m,v,s,pred)
    print(th,"S",S,"#M",len(Ms),"#orbits",len({gsel.delta_of_M(th,sp.Matrix([[m[0],m[1],m[2]],[m[1],m[3],m[4]],[m[2],m[4],m[5]]])) for m in Ms}),"pairs",n,"bad",nb,flush=True)
print("total",tot,"bad",bad)
