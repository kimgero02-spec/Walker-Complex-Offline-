# 3-페이지 책: 볼록 n-각형의 삼각분할 세 장의 합집합이 6-색칠 불가능한 예를 찾는 구성 탐색 (예 하나용)
import random, itertools, sys
from pysat.solvers import Glucose4
def rand_tri(n,rng):
    # 무작위 삼각분할: 귀 자르기
    poly=list(range(n)); E=set()
    while len(poly)>3:
        i=rng.randrange(len(poly)); a,b,c=poly[i-1],poly[i],poly[(i+1)%len(poly)]
        E.add(tuple(sorted((a,c)))); poly.pop(i)
    return E
def colorable(n,E,k):
    s=Glucose4(); v=lambda x,c: x*k+c+1
    for x in range(n): s.add_clause([v(x,c) for c in range(k)])
    for a,b in E:
        for c in range(k): s.add_clause([-v(a,c),-v(b,c)])
    s.add_clause([v(0,0)]); r=s.solve(); s.delete(); return r
def greedy3(n,rng,tries=30):
    # 각 페이지를 독립 무작위 삼각분할로
    hull={tuple(sorted((i,(i+1)%n))) for i in range(n)}
    pages=[rand_tri(n,rng) for _ in range(3)]
    return hull|pages[0]|pages[1]|pages[2], pages
rng=random.Random(int(sys.argv[2])); n=int(sys.argv[1]); cnt=0
for t in range(int(sys.argv[3])):
    E,pages=greedy3(n,rng)
    if not colorable(n,E,6):
        print('chi>=7 found',n,sorted(E)); break
    if not colorable(n,E,5): cnt+=1
print('n',n,'non-5-colorable count',cnt)
