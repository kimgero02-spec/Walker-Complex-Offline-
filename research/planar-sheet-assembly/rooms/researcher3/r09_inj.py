import sys; sys.path.insert(0,__import__('os').path.dirname(__file__))
from r09_check import *
K2=({'u','v'},{('u','v')})
for name,(Dp,D,sig) in {'id':([K2,K2],[K2,K2],(0,1)),'inj(0,2)':([K2,K2],[K2,K2,K2],(0,2)),'nonInj(0,0)':([K2,K2],[K2,K2],(0,0))}.items():
    _,_,Ls=L(Dp,D,sig)
    print(name,'|L|=',len(Ls),[ {str(k):str(v) for k,v in f.items() if k[0]=='w'} for f in Ls])
