# m=4 판 시도: 평면 4-색 잎 L 과 독립 삼중쌍 T 로 "5-색칠에서 T 무지개 불가" 인 것 (적층 삼각분할에서 구성 탐색)
import random, sys
from r04_lib import *
if __name__=='__main__': random.seed(int(sys.argv[1]))
def rainbow_possible(L, t, k=5):
    nodes = list(t) + [v for v in sorted(L.nodes(), key=lambda v:-L.degree(v)) if v not in t]
    col={}
    def bt(i):
        if i==len(nodes): return True
        v=nodes[i]; used={col[u] for u in L[v] if u in col}
        if i<3: cand=[i]          # T 를 0,1,2 로 고정 (무지개)
        else: cand=range(k)
        for c in cand:
            if c not in used:
                col[v]=c
                if bt(i+1): return True
                del col[v]
        return False
    return bt(0)
def stacked(n):
    L=nx.complete_graph(4); faces=[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
    for v in range(4,n):
        f=faces.pop(random.randrange(len(faces)))
        for u in f: L.add_edge(u,v)
        a,b,c=f; faces += [(a,b,v),(a,c,v),(b,c,v)]
    return L
if __name__=='__main__':
  for it in range(int(sys.argv[2])):
    L=stacked(random.randint(6,int(sys.argv[3])))
    T=[t for t in itertools.combinations(L.nodes(),3) if indep(L,t)]
    for t in T:
        if not rainbow_possible(L,t):
            print('FOUND leaf', L.number_of_nodes(), t, sorted(L.edges())); sys.exit()
  print('none')
