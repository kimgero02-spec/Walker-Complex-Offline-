import sympy as sp, itertools, numpy as np
t=sp.symbols('t')
def charcoef(A):
    # Faddeev-LeVerrier exact integer
    n=len(A); A=sp.Matrix(A)
    return A.charpoly(sp.symbols('x')).all_coeffs()  # c_0..c_n
def PG(A):
    n=len(A); c=charcoef(A)
    return sp.Poly(sum(c[k]*t**k for k in range(n+1))*(-1)**n, t)
def decomp(P):
    """P=c*S0*Q^2, S0 squarefree monic-ish, Q poly. returns (c,S0,Q)"""
    c,fl=sp.sqf_list(P.as_expr(),t)
    S0=sp.Integer(1);Q=sp.Integer(1)
    for f,m in fl:
        if m%2: S0*=f
        Q*=f**(m//2)
    return c,sp.Poly(S0,t),sp.Poly(Q,t)
def gab(P):
    c,S0,Q=decomp(P); d=S0.degree()
    return (d-1)//2 if d>=1 else 0
def signed_cover(A,sig):
    """A symmetric 0/1, sig dict edge->±1 ; return adjacency of double cover and signed adjacency"""
    n=len(A); S=sp.zeros(n,n)
    for i in range(n):
        for j in range(n):
            if A[i][j]: S[i,j]=sig[(min(i,j),max(i,j))]
    H=sp.zeros(2*n,2*n)
    for i in range(n):
        for j in range(n):
            if A[i][j]:
                if S[i,j]==1:
                    H[i,j]=1;H[n+i,n+j]=1
                else:
                    H[i,n+j]=1;H[n+i,j]=1
    return H,S
