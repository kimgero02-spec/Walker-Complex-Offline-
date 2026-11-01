from sdim import *
import itertools
# characteristic dependence
for hn,AH,gn,AG in [('K3',comp(3),'K3',comp(3)),('C5',cyc(5),'C5',cyc(5)),('K2',comp(2),'C4',cyc(4)),('K3',comp(3),'K4',comp(4)),('C5','','','')]:
    if hn=='C5' and gn=='': continue
    print(hn,gn,[dimS(AH,AG,p)[1] for p in (2,3,5,7,1000003)])
print('K4->K4',[dimS(comp(4),comp(4),p)[1] for p in (2,3,5,1000003)],'K5->K5',[dimS(comp(5),comp(5),p)[1] for p in (2,3,5,1000003)])
print('C4->C4',[dimS(cyc(4),cyc(4),p)[1] for p in (2,3,1000003)])
# covering / local injective intertwiner check: enumerate all maps f:H->G (all set maps), test A_H P = P A_G etc
def P(f,n): return [[1 if f[h]==g else 0 for g in range(n)] for h in range(len(f))]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tolist(f): return f
def test(AH,AG):
    m=len(AH);n=len(AG); eq=[];le=[]
    for f in itertools.product(range(n),repeat=m):
        Pf=P(f,n); L=mm(AH,Pf); R=mm(Pf,AG)
        if L==R: eq.append(f)
        if all(L[i][j]<=R[i][j] for i in range(m) for j in range(n)): le.append(f)
    return eq,le
for hn,AH,gn,AG in [('C6',cyc(6),'C3',cyc(3)),('C6',cyc(6),'C6',cyc(6)),('C4',cyc(4),'C4',cyc(4)),('C5',cyc(5),'C5',cyc(5)),('K33',kmn(3,3),'K3',comp(3)), ('C6',cyc(6),'C4',cyc(4))]:
    eq,le=test(AH,AG); h=homs(AH,AG)
    print(hn,gn,'|Hom|',len(h),'covers(A_H P=P A_G)',len(eq),'loc.inj(A_H P<=P A_G)',len(le))
