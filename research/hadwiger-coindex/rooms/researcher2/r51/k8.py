import itertools, random, networkx as nx
from twolayer import cross, analyze
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF
n=8; E=list(itertools.combinations(range(n),2))
def frust(P):
    # 교차 그래프를 이분으로 만들려면 지워야 할 최소 교차 수 (MaxSAT)
    w=WCNF(); idx={e:i+1 for i,e in enumerate(range(len(E)))}
    cnt=0
    for i,j in itertools.combinations(range(len(E)),2):
        a,b=E[i];c,d=E[j]
        if len({a,b,c,d})==4 and cross(P[a],P[b],P[c],P[d]):
            w.append([i+1,j+1],weight=1); w.append([-(i+1),-(j+1)],weight=1); cnt+=1
    if cnt==0: return 0
    r=RC2(w); r.compute(); return r.cost
random.seed(7)
for restart in range(40):
    P=[(random.random(),random.random()) for _ in range(n)]; f=frust(P)
    for step in range(400):
        Q=list(P); k=random.randrange(n); s=random.choice([0.2,0.05,0.01])
        Q[k]=(Q[k][0]+random.gauss(0,s),Q[k][1]+random.gauss(0,s))
        g=frust(Q)
        if g<=f: P,f=Q,g
        if f==0: break
    if f==0:
        r=analyze(P,E); print('found',r[0],'crossings',r[2]); print([(round(x,4),round(y,4)) for x,y in P]); break
    print('restart',restart,'best frust',f)
