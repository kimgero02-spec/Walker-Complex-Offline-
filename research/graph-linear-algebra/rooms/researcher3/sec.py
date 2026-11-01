import sympy as sp
t,a1,a2,a3=sp.symbols('t a1 a2 a3')
A=sp.Matrix([[0,1,1],[1,0,1],[1,1,0]])
M0=sp.Matrix([[0,1,0],[1,2*(a1+a2+a3+1),a2+2*a3],[0,a2+2*a3,2*a3]])
print(sp.expand((t*A-M0).det()-2*(t**3+a1*t**2+a2*t+a3)))
