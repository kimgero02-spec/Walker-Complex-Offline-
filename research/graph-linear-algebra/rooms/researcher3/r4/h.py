from g import *
# join formula
def chk_join(A,B,k1,k2):
    n1,n2=A.shape[0],B.shape[0]
    PJ=sp.expand((t*join(A,B)-sp.eye(n1+n2)).det(method='berkowitz'))
    PA=Pg(A);PB=Pg(B)
    q=(k1*k2-n1*n2)*t**2-(k1+k2)*t+1
    rhs=PA*PB*q/((k1*t-1)*(k2*t-1))
    return sp.factor(PJ), sp.simplify(PJ-rhs)==0, sp.simplify(PJ+rhs)==0
print(chk_join(C(5),K(2),2,1))
print(chk_join(K(3),K(3),2,2))
print(chk_join(C(4),C(5),2,2))
# non-regular complements
G1=star(4); G2=dsum(C(4),K(1))
print('K14',Pg(G1),'| C4+K1',Pg(G2))
print('compl K14',Pg(comp(G1)),'| compl C4+K1',Pg(comp(G2)))
print('spec', G1.charpoly().as_expr().factor(), G2.charpoly().as_expr().factor())
# P3 box K2 
f=Pg(cart(P(3),K(2))); print('P3boxK2',f)
tt=sp.symbols('tau')
w1=sp.factor(-(tt-1)*(tt**2-6*tt+1)); w2=sp.factor(-tt*(tt-1)*(tt**2-6*tt+1))
print(w1,w2)
# K2 box G formula: P_{G box K2}=P_G^{(1)} P_G^{(-1)}
def shift(A,c): n=A.shape[0]; return sp.expand((t*(A+c*sp.eye(n))-sp.eye(n)).det(method='berkowitz'))
A=K(3); print(sp.simplify(shift(A,1)*shift(A,-1)-sp.expand((t*cart(A,K(2))-sp.eye(6)).det())))
