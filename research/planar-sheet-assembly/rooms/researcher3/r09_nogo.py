import sys; sys.path.insert(0,__import__('os').path.dirname(__file__))
from r09_check import *
K2=({'u','v'},{('u','v')})
Dpp=[K2,K2]            # D''  (R1,R2)
Dp =[K2,K2,K2]         # D'   (Q1,Q2,Q3)
D  =[K2,K2]            # D    (P1,P2)
Dq =[K2]               # D''' (S1)
tau,sig = (0,1),(0,0,1)     # tau: D''->D', sigma: D'->D
tau2,sig2=(0,0),(0,)        # tau2: D''->D''', sig2: D'''->D
def comp(f,g): return {x: f[g[x]] for x in g}  # not used
Mpp,M,Ltau=L(Dpp,Dp,tau)
_,_,Lsig=L(Dp,D,sig)
_,_,Ltau2=L(Dpp,Dq,tau2)
_,_,Lsig2=L(Dq,D,sig2)
print('nodes D2 :',Mpp['nodes'])
print('|L(tau)|',len(Ltau),'|L(sigma)|',len(Lsig),'|L(tau2)|',len(Ltau2),'|L(sig2)|',len(Lsig2))
u1=('w','u')
print('tau image of white u (D2->D\'):', sorted({str(f[('w','u')]) for f in Ltau}))
print('sigma image of white u (D\'->D):', sorted({str(f[('w','u')]) for f in Lsig}))
print('tau2 image of white u (D2->D\'\'\'):', sorted({str(f[('w','u')]) for f in Ltau2}))
print('sig2 image of copy (u,0) (D\'\'\'->D):', sorted({str(f[('c','u',0)]) for f in Lsig2}))
# composites from factorization A and B at the white point of D'' over u
A={ str(s[tu][('w','u')]) for t in Ltau for s in Lsig for tu in [None] } if False else None
compA=set(); 
for t in Ltau:
    for s in Lsig:
        compA.add(str(s[t[('w','u')]]))
compB=set()
for t in Ltau2:
    for s in Lsig2:
        compB.add(str(s[t[('w','u')]]))
print('composites over factorization A (D\'\'->D\'->D) at white u:',compA)
print('composites over factorization B (D\'\'->D\'\'\'->D) at white u:',compB)
# all lifts of the refinement sigma∘tau (both as sets of Psi-morphisms over the same D''->D)
Mpp2,M2,Lst=L(Dpp,D,(0,0))
print('|L(sigma∘tau)|',len(Lst),' images of white u:',sorted({str(f[('w','u')]) for f in Lst}))
