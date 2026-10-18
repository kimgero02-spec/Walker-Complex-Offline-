# 순환 예 검산: 기본 장 P 와 그 회전 P_k (k in Z_n) 가 K_{3n} 의 정확한 분해이고 각 장이 (3,2) 인지.
import ast, itertools, networkx as nx, sys
from r19_lib import chi, omega
for fn in sys.argv[1:]:
    L=open(fn).read().splitlines(); n=int(L[0].split()[1]); E=ast.literal_eval(L[1])
    sh=[nx.Graph([(((a+k)%n,r),((b+k)%n,s)) for (a,r),(b,s) in E]) for k in range(n)]
    cnt={}
    for G in sh:
        for e in G.edges(): cnt[frozenset(e)]=cnt.get(frozenset(e),0)+1
    V=[(i,r) for i in range(n) for r in range(3)]
    ex=set(cnt)==set(frozenset(e) for e in itertools.combinations(V,2)) and all(c==1 for c in cnt.values())
    print(fn,"N=",3*n,"정확=",ex,"평면=",nx.check_planarity(sh[0])[0],"chi=",chi(sh[0]),"omega=",omega(sh[0]),
          "sigma=",n*chi(sh[0]),"Delta=",n if chi(sh[0])>omega(sh[0]) else 0)
