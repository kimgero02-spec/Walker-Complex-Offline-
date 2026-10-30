# R18: 조각 색칠수 합 = chi(G) 예 확인 + C-weak (정렬된 최적 색칠) 반례 찾기
import itertools, networkx as nx, random
def colorings(n, edges, q):
    # all proper q-colorings of vertices 0..n-1 (backtracking)
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v); adj[v].add(u)
    c=[-1]*n; out=[]
    def bt(i):
        if i==n: out.append(tuple(c)); return
        for x in range(q):
            if all(c[j]!=x for j in adj[i] if j<i):
                c[i]=x; bt(i+1)
        c[i]=-1
    bt(0); return out
def chi(n, edges):
    q=1
    while not colorings_exist(n,edges,q): q+=1
    return q
def colorings_exist(n,edges,q):
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v); adj[v].add(u)
    c=[-1]*n
    def bt(i):
        if i==n: return True
        for x in range(q):
            if all(c[j]!=x for j in adj[i] if j<i):
                c[i]=x
                if bt(i+1): return True
        c[i]=-1; return False
    return bt(0)
def planar(n,edges):
    g=nx.Graph(); g.add_nodes_from(range(n)); g.add_edges_from(edges); return nx.check_planarity(g)[0]
def min_tuples(n, pieces):
    # min over optimal colorings c_k of pieces (spanning V) of #distinct tuples
    cols=[]
    for E in pieces:
        a=chi(n,E); cols.append(colorings(n,E,a))
    best=10**9
    for combo in itertools.product(*cols):
        t=len(set(zip(*combo))); best=min(best,t)
    return best
if __name__=="__main__":
    # K8 = hexagonal bipyramid U (prism + pole edge)
    eq=list(range(6)); N,S=6,7
    P1=[(i,(i+1)%6) for i in eq]+[(i,N) for i in eq]+[(i,S) for i in eq]
    K8=set(itertools.combinations(range(8),2))
    P2=sorted(K8-set(tuple(sorted(e)) for e in P1))
    print("K8: planar",planar(8,P1),planar(8,P2),"chi",chi(8,P1),chi(8,P2),"chiG",chi(8,list(K8)))
    # W5 hub 0, rim 1..5 ; colors 0:00,1:01,2:10,3:01,4:10,5:11
    col={0:(0,0),1:(0,1),2:(1,0),3:(0,1),4:(1,0),5:(1,1)}
    W5=[(0,i) for i in range(1,6)]+[(i,i%5+1) for i in range(1,6)]
    A=[e for e in W5 if col[e[0]][0]!=col[e[1]][0]]; B=[e for e in W5 if col[e[0]][1]!=col[e[1]][1]]
    print("W5:",sorted(set(A)|set(B))==sorted(W5),chi(6,A),chi(6,B),chi(6,W5),A,B)
