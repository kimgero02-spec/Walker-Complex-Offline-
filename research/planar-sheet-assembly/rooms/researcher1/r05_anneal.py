# 근접 실패 예에서 출발해 점 추가/변 교체로 "둘 다 비무지개" 패턴 수를 줄이는 국소 탐색 (구성 후보 생성용, 근거 아님)
import random, sys, itertools, networkx as nx
from r05_lib import *
random.seed(int(sys.argv[1])); NMAX=int(sys.argv[2]); ITERS=int(sys.argv[3])
T1=(0,1,2); T2=(3,4,5); S=T1+T2

def set_partitions(lst):
    if not lst: yield []; return
    f=lst[0]
    for p in set_partitions(lst[1:]):
        for i in range(len(p)): yield p[:i]+[[f]+p[i]]+p[i+1:]
        yield [[f]]+p
PATS=[]
for p in set_partitions(list(S)):
    if len(p)>4: continue
    lab={v:i for i,b in enumerate(p) for v in b}
    if len({lab[v] for v in T1})<3 and len({lab[v] for v in T2})<3: PATS.append(lab)

def extends(Q,pre,k=4):
    order=[v for v in nx.dfs_preorder_nodes(Q) if v not in pre] if nx.is_connected(Q) else [v for v in Q if v not in pre]
    col=dict(pre)
    for v in pre:
        for u in Q[v]:
            if u in pre and pre[u]==pre[v]: return False
    def bt(i):
        if i==len(order): return True
        v=order[i]; used={col[u] for u in Q[v] if u in col}
        for c in range(k):
            if c not in used:
                col[v]=c
                if bt(i+1): return True
                del col[v]
        return False
    return bt(0)
def score(Q): return sum(extends(Q,p) for p in PATS)

def saturate(Q,part,prob=1.0):
    n=Q.number_of_nodes()
    E=[(u,v) for u,v in itertools.combinations(range(n),2) if part[u]!=part[v] and not Q.has_edge(u,v)
       and not ({u,v}<=set(T1) or {u,v}<=set(T2))]
    random.shuffle(E)
    for u,v in E:
        if random.random()>prob: continue
        Q.add_edge(u,v)
        if not nx.check_planarity(Q)[0]: Q.remove_edge(u,v)
    return Q

def start():
    n=random.randint(8,10)
    part=[0,1,2]+random.sample([0,1,2],3)+[random.randrange(3) for _ in range(n-6)]
    Q=nx.empty_graph(n); return saturate(Q,part),part

Q,part=start(); sc=score(Q); best=sc
for it in range(ITERS):
    Q2=nx.Graph(Q); p2=list(part); n=Q2.number_of_nodes()
    r=random.random()
    if r<0.3 and n<NMAX:
        p2.append(random.randrange(3)); Q2.add_node(n)
    else:
        es=[e for e in Q2.edges()]
        for e in random.sample(es, min(len(es),random.randint(1,3))): Q2.remove_edge(*e)
    if r>0.9: # 분할 한 점 바꾸기 (T 밖)
        v=random.randrange(6,len(p2)) if len(p2)>6 else None
        if v is not None:
            p2[v]=random.randrange(3); Q2.remove_edges_from([e for e in list(Q2.edges(v)) if p2[e[0]]==p2[e[1]]])
    saturate(Q2,p2)
    if not nx.is_connected(Q2): continue
    s2=score(Q2)
    if s2<=sc or random.random()<0.05:
        Q,part,sc=Q2,p2,s2
        if sc<best:
            best=sc; print(it,'score',sc,'n',Q.number_of_nodes(),sorted(Q.edges())); sys.stdout.flush()
    if sc==0:
        print('FOUND chi',chi(Q),'planar',nx.check_planarity(Q)[0]); break
    if it%200==199 and sc>best+3: Q,part=start(); sc=score(Q)
