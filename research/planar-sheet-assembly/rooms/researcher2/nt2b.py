# q=5 에서 평면 조각 프로필이 간선 비트(P[J])보다 정말 정밀한가: 쌓은 삼각분할에서 같은 색 3점
import networkx as nx, itertools
from nt2 import profile, show, colorable, chi  # nt2 의 출력도 다시 나온다
E = [('a','b'),('a','c'),('a','d'),('b','c'),('b','d'),('c','d')]
col = {'a':0,'b':1,'c':2,'d':3}; faces = [('a','b','c'),('a','b','d'),('a','c','d'),('b','c','d')]
# 결정적 쌓기: 색 3 (d 의 색) 인 점을 늘린다 -- 색 {0,1,2} 인 면에 새 점
new = 0
for step in range(2):
    f = next(F for F in faces if {col[v] for v in F} == {0,1,2})
    v = 'n%d' % new; new += 1
    E += [(v, w) for w in f]; col[v] = 3
    faces.remove(f); faces += [(v, f[0], f[1]), (v, f[0], f[2]), (v, f[1], f[2])]
    # 다음 단계에서 색 {0,1,2} 면이 필요 -> 색 2 점을 하나 넣어 만든다
    g = next(F for F in faces if {col[x] for x in F} == {0,1,3})
    w = 'm%d' % new; new += 1
    E += [(w, x) for x in g]; col[w] = 2
    faces.remove(g); faces += [(w, g[0], g[1]), (w, g[0], g[2]), (w, g[1], g[2])]
U = nx.Graph(E)
J = [v for v in U if col[v] == 3]
print("planar", nx.check_planarity(U)[0], "n", U.number_of_nodes(), "J(색3)", J, "J 독립", not any(U.has_edge(x,y) for x,y in itertools.combinations(J,2)))
print("Pi4", show(profile(U, J, 4)))
print("Pi5", show(profile(U, J, 5)))
print("Pi6", show(profile(U, J, 6)))
