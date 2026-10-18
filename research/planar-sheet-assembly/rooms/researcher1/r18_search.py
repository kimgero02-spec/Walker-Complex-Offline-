# 목적: "합=chi 이지만 어떤 최적 조각 색칠의 곱도 chi 개 튜플로 접히지 않는" 결정적 반례 하나 찾기 (근거 아님, 반례 탐색)
import random, itertools, networkx as nx
from r18_sum import chi, planar, min_tuples
random.seed(1)
found=0
for trial in range(20000):
    n=random.choice([6,7])
    allE=list(itertools.combinations(range(n),2))
    E=[e for e in allE if random.random()<0.75]
    q=chi(n,E)
    if q<4: continue
    # random 2-cover with planar pieces
    A=[];B=[]
    for e in E:
        r=random.random()
        if r<0.45: A.append(e)
        elif r<0.9: B.append(e)
        else: A.append(e);B.append(e)
    if not(planar(n,A) and planar(n,B)): continue
    a,b=chi(n,A),chi(n,B)
    if a+b!=q: continue
    m=min_tuples(n,[A,B])
    if m>q:
        print("COUNTER n",n,"q",q,"a,b",a,b,"min tuples",m); print("A",A); print("B",B); found+=1
        if found>=2: break
print("done")
