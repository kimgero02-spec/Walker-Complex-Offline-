import sys
from r3_exp2 import *
cases = eval(sys.argv[1])
for (f,p,R,nS,nT) in cases:
    print("f",f,"p",p,"(#classes, ker, inconsistent, nonbilinear, nonalt)=",run(f,p,R=R,nS=nS,nT=nT,ntri=150),flush=True)
