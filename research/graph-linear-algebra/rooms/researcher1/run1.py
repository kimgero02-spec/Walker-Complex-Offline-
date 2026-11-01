from sdim import *
K2=comp(2)
tests={'K3':comp(3),'C4':cyc(4),'P4':path(4),'K4':comp(4),'C5':cyc(5),'P3':path(3),'K33':kmn(3,3),'C6':cyc(6),
 'C4+iso':graph(5,[(0,1),(1,2),(2,3),(3,0)]),'K3+K2':graph(5,[(0,1),(1,2),(0,2),(3,4)]),'K3loop':graph(3,[(0,1),(1,2)],loops=[0]),
 'Petersen':graph(10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)])}
print("K2 formula 2n'-k vs data")
for k,A in tests.items():
    h,d=dimS(K2,A); print(k,h,d,bound(2,A))
print("trees/bipartite H")
for hn,AH in [('P3',path(3)),('P4',path(4)),('K13',kmn(1,3)),('C4',cyc(4)),('C6',cyc(6)),('K23',kmn(2,3))]:
    for gn,AG in tests.items():
        if len(AG)>6 and hn in('C6','K23'): continue
        h,d=dimS(AH,AG); print(hn,'->',gn,'|Hom|',h,'dim',d,'bound',bound(len(AH),AG), 'OK' if d==bound(len(AH),AG) else 'NE')
