from sdim import *
K4m=graph(4,[(0,1),(1,2),(2,3),(0,2),(0,3)])  # K4 minus edge 13
bowtie=graph(5,[(0,1),(1,2),(0,2),(2,3),(3,4),(2,4)])
Gs={'K3':comp(3),'K4':comp(4),'K4-e':K4m,'K5':comp(5),'C5':cyc(5),'bowtie':bowtie,'C7':cyc(7),
 'K3+pend':graph(4,[(0,1),(1,2),(0,2),(2,3)]),'K3+pend2':graph(5,[(0,1),(1,2),(0,2),(2,3),(3,4)]),'C5+chord':graph(5,[(i,(i+1)%5) for i in range(5)]+[(0,2)]),
 'K4+pend':graph(5,[(i,j) for i in range(4) for j in range(i+1,4)]+[(3,4)]),'Wheel5':graph(6,[(i,(i+1)%5) for i in range(5)]+[(i,5) for i in range(5)])}
for hn,AH in [('K3',comp(3)),('C5',cyc(5)),('C3+pend',graph(4,[(0,1),(1,2),(0,2),(2,3)])),('K4',comp(4))]:
    print('H=',hn)
    for gn,AG in Gs.items():
        h,d=dimS(AH,AG); n1,c1,b1=stats(AG)
        print('  ->',gn,'n',len(AG),'c',c1,'b',b1,'E',sum(map(sum,AG))//2,'|Hom|',h,'dim',d,'naive bound',bound(len(AH),AG))
