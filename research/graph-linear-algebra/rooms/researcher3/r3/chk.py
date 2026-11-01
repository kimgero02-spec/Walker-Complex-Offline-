import numpy as np, sympy as sp, random
p=5
A=sp.Matrix([[0,1,1],[1,0,1],[1,1,0]]); Ainv=A.inv()
t=sp.symbols('t')
random.seed(2)
for _ in range(3):
    M=sp.Matrix(3,3,[random.randrange(p) for _ in range(9)])
    phi=Ainv*M; ps=Ainv*phi.T*A; H=ps*phi
    cp=sp.Poly((t*sp.eye(3)-H).det(),t).all_coeffs()
    print(M.tolist(), [ (sp.Rational(c).p*pow(sp.Rational(c).q,-1,p))%p for c in cp])
    # numpy
    inv2=3
    Ai=(inv2*np.ones((3,3),dtype=np.int64)-np.eye(3,dtype=np.int64))%p
    Mn=np.array(M.tolist(),dtype=np.int64)
    ph=(Ai@Mn)%p; pst=(Ai@ph.T@np.array(A.tolist()))%p; Hn=(pst@ph)%p
    tr=np.trace(Hn)%p; tr2=np.trace(Hn@Hn)%p
    print(tr,((tr*tr-tr2)*inv2)%p, round(np.linalg.det(Hn.astype(float)))%p)
