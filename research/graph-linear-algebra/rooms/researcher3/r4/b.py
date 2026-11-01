from g import *
# Petersen
def petersen():
    e=[]
    for i in range(5): e+= [(i,(i+1)%5),(i,i+5),(5+i,5+(i+2)%5)]
    return Mx(e,10)
def Q3():
    return Mx([(i,i^b) for i in range(8) for b in (1,2,4) if i<i^b],8)
def paley9(): return cart(K(3),K(3))
def K33(): return Mx([(i,3+j) for i in range(3) for j in range(3)],6)
phi=-t/(1+t)
def check(A,k):
    n=A.shape[0]
    PG=sp.expand((t*A-sp.eye(n)).det(method='berkowitz'))
    PB=sp.expand((t*comp(A)-sp.eye(n)).det(method='berkowitz'))
    lhs=sp.simplify(PB.subs(t,phi)*(1+t)**n)
    rhs=sp.simplify(PG*((n-k)*t+1)/(k*t-1))
    return sp.factor(lhs), sp.factor(rhs), sp.simplify(lhs-rhs)==0, sp.simplify(lhs+rhs)==0
for nm,A,k in [('K3',K(3),2),('K4',K(4),3),('C5',C(5),2),('C6',C(6),2),('Petersen',petersen(),3),('Q3',Q3(),3),('Paley9',paley9(),4),('K33',K33(),3)]:
    print(nm, check(A,k)[2:], )
    print('   P_G',Pg(A),'  P_comp',Pg(comp(A)))
