from g import *
def cmulti(parts):
    n=sum(parts); A=sp.ones(n,n); i=0
    for p in parts:
        for a in range(i,i+p):
            for b in range(i,i+p): A[a,b]=0
        i+=p
    return A
for parts in [(1,1,2),(1,2,2),(1,1,3),(1,2,3),(2,2,2),(1,1,1,2)]:
    A=cmulti(parts); print(parts, Pg(A), sp.factor(A.charpoly().as_expr()))
