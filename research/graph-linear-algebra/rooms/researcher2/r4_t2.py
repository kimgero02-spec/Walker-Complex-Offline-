import warnings;warnings.filterwarnings('ignore')
from r4_gam import *
from r4_ce import PGp,PHp
P4=PG([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]])
P2P4=Poly(P4.as_expr()**2,t)
print('P4',sp.factor(P4.as_expr()))
for p in [5,7,11,13,17,19]:
    gG=gam_order(PGp,p); gH=gam_order(PHp,p)
    print('p',p,'G(6v):',gG,'H:',gH, 'divides?', gH[2]%gG[2]==0)
# 2P4: reducible curve w^2=S^2, S=P4 ; Gamma = (K^*/F_p^*) with K=F_p[t]/S
for p in [5,7,11,13,19,29]:
    c,fl=sp.factor_list(P4.as_expr(),t,modulus=p)
    EP=None
    # E: y^2=P4 genus 1
    n1=0
    f=Poly(P4.as_expr(),t,modulus=p)
    for x in range(p):
        v=int(f.eval(x))%p
        n1+=1 if v==0 else (2 if pow(v,(p-1)//2,p)==1 else 0)
    n1+= 2 if pow(1,(p-1)//2,p)==1 else 0
    Kstar=1
    for g,m in fl:
        d=Poly(g,t,modulus=p).degree(); Kstar*=p**d-1
    print('p',p,'|Gamma_P4|=#E=',n1,' |Gamma_2P4|=|K*|/(p-1)=',Kstar//(p-1),' divisible?',(Kstar//(p-1))%n1==0)
