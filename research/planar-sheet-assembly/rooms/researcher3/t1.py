from r03 import *
def prism(k, twist=False):
    P={}; arcs=[]
    for i in range(k):
        j=(i+1)%k
        P[i]=['t%d'%i,'t%d'%j,'b%d'%j,'b%d'%i]
    for i in range(k):
        j=(i+1)%k
        arcs.append((i,j,['t%d'%j,'b%d'%j]))
    if twist:  # mobius: last square crosses
        P[k-1]=['t%d'%(k-1),'b0','t0','b%d'%(k-1)]
        arcs[-1]=(k-1,0,['t0','b0'])
    return Manual(P,arcs)
for k in (3,4): criterion(prism(k),"prism k=%d"%k)
def handles(Q,R,order='cross'):
    P={0:list(range(8)),1:Q,2:R}
    if order=='cross': arcs=[(0,1,[0,1]),(0,1,[4,5]),(0,2,[2,3]),(0,2,[6,7])]
    else: arcs=[(0,1,[0,1]),(0,1,[2,3]),(0,2,[4,5]),(0,2,[6,7])]
    return Manual(P,arcs)
criterion(handles([0,1,5,4],[2,3,7,6]),"Z2 twisted x twisted cross")
criterion(handles([0,1,5,4],[2,3,6,7]),"twisted x straight cross")
criterion(handles([0,1,3,2],[4,5,7,6],'nc'),"twisted,twisted noncross")
criterion(handles([0,1,2,3],[4,5,6,7],'nc'),"straight noncross b=3")
criterion(handles([0,1,2,3],[4,5,7,6],'nc'),"straight+twisted noncross")
