import sympy
from fractions import Fraction as Fr
from r3lib import *
X = sympy.symbols('X')
def charpoly(alg, y):
    M = alg.mat([Fr(c) for c in y])
    S = sympy.Matrix(3, 3, lambda i, j: sympy.Rational(M[i][j].numerator, M[i][j].denominator))
    return S.charpoly(X).as_expr()
def is_square_L(alg, y):
    R = charpoly(alg, y)
    S = sympy.Poly(R.subs(X, X**2), X)
    fl = sympy.factor_list(S.as_expr())[1]
    return any(sympy.degree(g, X) in (3, 1) and sympy.degree(g, X) == 3 or False for g, e in fl) or any(sympy.degree(g, X) == 1 and False for g, e in fl)
def ratio_square(alg, a, b):
    return is_square_L(alg, alg.mul(a, alg.inv(b)))
if __name__ == "__main__":
    A = Alg([1, -2, -1])
    d = [Fr(-1), Fr(-2), Fr(0)]
    for name, g in [("-(th+1)", [Fr(-1), Fr(-1), Fr(0)]), ("1", [Fr(1), 0, 0])]:
        print(name, ratio_square(A, d, g))
