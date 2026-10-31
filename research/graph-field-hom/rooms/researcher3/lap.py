import itertools
exec(open('snf.py').read().split("def cyc")[0])
def graphs():
    P5=[(i,i+1) for i in range(4)]
    C6=[(i,(i+1)%6) for i in range(6)]
    Q3=[(u,u^(1<<k)) for u in range(8) for k in range(3) if u<u^(1<<k)]
    K33=[(i,3+j) for i in range(3) for j in range(3)]
    return {'P5':(P5,5),'C6':(C6,6),'Q3':(Q3,8),'K33':(K33,6)}
for name,(E,n) in graphs().items():
    for lab,(a,b) in {'L (x=y)':(1,-1),'Q signless (x+y=0)':(1,1)}.items():
        M=B(E,n,a,b)
        # B^T B
        BT=[[M.a[i][j] for i in range(M.rows)] for j in range(n)]
        G=Matrix([[sum(BT[i][k]*M.a[k][j] for k in range(M.rows)) for j in range(n)] for i in range(n)])
        print(name,lab,"ker B over p=2,3,5:",[nullity(M,p) for p in (2,3,5)],"ker B^TB:",[nullity(G,p) for p in (2,3,5)],"SNF(BtB)",SNFdiag(G.a))
