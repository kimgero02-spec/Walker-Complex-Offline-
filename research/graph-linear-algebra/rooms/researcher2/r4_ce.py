from r4lib import *
es=[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 4)]
sig={(0, 1): -1, (0, 2): 1, (0, 3): 1, (0, 4): 1, (0, 5): 1, (1, 2): -1, (1, 3): 1, (1, 4): 1, (1, 5): -1, (2, 5): -1, (3, 4): 1}
n=6
A=[[0]*n for _ in range(n)]
for i,j in es: A[i][j]=A[j][i]=1
H,S=signed_cover(A,sig)
PGp=PG(A);PHp=PG(H.tolist());PS=PG(S.tolist())
print('deg seq',[sum(r) for r in A])
print('P_G',sp.factor(PGp.as_expr()))
print('P_H',sp.factor(PHp.as_expr()))
print('P_sigma',sp.factor(PS.as_expr()))
print('ratio',sp.factor(sp.cancel(PHp.as_expr()/PGp.as_expr())))
print(decomp(PGp)); print(decomp(PHp))
# check cover: local bijection
Hl=H.tolist()
for h in range(2*n):
    nb=[k for k in range(2*n) if Hl[h][k]]
    assert sorted(k%n for k in nb)==sorted(j for j in range(n) if A[h%n][j])
print('cover ok; H edges',int(sum(map(sum,Hl))/2))
