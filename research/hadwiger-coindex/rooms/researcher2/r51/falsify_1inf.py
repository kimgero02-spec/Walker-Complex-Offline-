# 4n-8 정리 반증 시도: 고정 점 배치에서 (1,∞) 2층 곧은 선 그림의 최대 간선 수 (MaxSAT, 정확)
import itertools, random, sys
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF
from pysat.card import CardEnc, EncType
from twolayer import cross
def maxedges(P):
    n=len(P); E=list(itertools.combinations(range(n),2)); w=WCNF(); top=[0]
    def nv(): top[0]+=1; return top[0]
    a={e:nv() for e in E}; b={e:nv() for e in E}   # a: 층1, b: 층2 (둘 다 가능 = 공유)
    C={e:[f for f in E if len({*e,*f})==4 and cross(P[e[0]],P[e[1]],P[f[0]],P[f[1]])] for e in E}
    cl=[]
    for e in E:
        for f in C[e]:
            if e<f: cl+= [[-a[e],-a[f]],[-b[e],-b[f]]]
        # 층1 간선 e 는 층2 간선과 최대 1번 교차
        if len(C[e])>=2:
            lits=[b[f] for f in C[e]]
            enc=CardEnc.atmost(lits,bound=1,top_id=top[0],encoding=EncType.seqcounter); top[0]=max(top[0],enc.nv)
            for c in enc.clauses: cl.append([-a[e]]+c)
    for c in cl: w.append(c)
    for e in E:
        x=nv(); w.append([-x,a[e],b[e]]); w.append([x],weight=1)
    r=RC2(w); r.compute(); return len(E)-r.cost
random.seed(int(sys.argv[2])); n=int(sys.argv[1]); best=0
for t in range(int(sys.argv[3])):
    P=[(random.random(),random.random()) for _ in range(n)]; best=max(best,maxedges(P))
print('n',n,'max edges found',best,'4n-8 =',4*n-8)
