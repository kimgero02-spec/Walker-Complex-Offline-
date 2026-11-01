import sympy as sp, itertools
t=sp.symbols('t')
def Mx(edges,n):
    A=sp.zeros(n,n)
    for u,v in edges: A[u,v]=A[v,u]=1
    return A
def K(n): return Mx([(i,j) for i in range(n) for j in range(i+1,n)],n)
def C(n): return Mx([(i,(i+1)%n) for i in range(n)],n)
def P(n): return Mx([(i,i+1) for i in range(n-1)],n)
def star(m): return Mx([(0,i) for i in range(1,m+1)],m+1)
def kron_sum(A,B): return sp.kronecker_product(A,sp.eye(B.shape[0]))+sp.kronecker_product(sp.eye(A.shape[0]),B)
def cart(A,B): return kron_sum(A,B)
def tens(A,B): return sp.kronecker_product(A,B)
def dsum(A,B): return sp.diag(A,B)
def comp(A): n=A.shape[0]; return sp.ones(n,n)-sp.eye(n)-A
def join(A,B):
    n,m=A.shape[0],B.shape[0]
    M=sp.zeros(n+m,n+m); M[:n,:n]=A; M[n:,n:]=B; M[:n,n:]=sp.ones(n,m); M[n:,:n]=sp.ones(m,n); return M
def Pg(A):
    n=A.shape[0]; return sp.factor((t*A-sp.eye(n)).det(method='berkowitz'))
