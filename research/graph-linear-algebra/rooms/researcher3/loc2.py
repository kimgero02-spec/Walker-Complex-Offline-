import sys, numpy as np
from lib import *
from descent import *
import gsel
sys.argv=['x']+sys.argv[1:]
exec(open('final.py').read().split("th=tuple")[0])   # reuse enum
def run(th,B):
    f=(-sum(th), th[0]*th[1]+th[0]*th[2]+th[1]*th[2], -th[0]*th[1]*th[2])
    Ms=enum(f,B)
    cl=set()
    for m in Ms:
        d=gsel.delta_of_M(th,sp.Matrix([[m[0],m[1],m[2]],[m[1],m[3],m[4]],[m[2],m[4],m[5]]]))
        cl.add(clsvec(d,2))
    im,_=kummer_image(th,2)
    cands=local_candidates(th,2)
    ker={clsvec(d,2) for d in cands if isotropic_class(th,d,2)}
    print(th,"#M",len(Ms),"2-adic classes hit by integral M:",len(cl),"; Kummer image at 2:",len(im),"; hit∩image",len(cl&im),"; kernel at 2:",len(ker),"hit⊂ker",cl<=ker)
    return cl,im,ker
for th in [(0,1,-2),(0,2,-2),(0,1,3),(0,-1,4)]:
    run(th,8)
