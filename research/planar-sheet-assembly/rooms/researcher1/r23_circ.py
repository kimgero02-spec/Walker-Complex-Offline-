# R23: 후보 탐색 전용 — 둘레>=5, chi=5 인 순환 그래프 C_n(S) 찾기 (근거 아님)
import itertools, networkx as nx, sys
from pysat.solvers import Cadical153
def circ(n,S):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for s in S: G.add_edge(i,(i+s)%n)
    return G
def colorable(G,k):
    idx={v:i for i,v in enumerate(G.nodes())}
    var=lambda v,c: idx[v]*k+c+1
    s=Cadical153()
    for v in G: s.add_clause([var(v,c) for c in range(k)])
    for u,v in G.edges():
        for c in range(k): s.add_clause([-var(u,c),-var(v,c)])
    s.add_clause([var(next(iter(G)),0)])
    r=s.solve(); s.delete(); return r
if __name__=="__main__":
    lo,hi=int(sys.argv[1]),int(sys.argv[2])
    for n in range(lo,hi+1):
        half=[s for s in range(1,(n+1)//2)]
        for r in (2,3):
            for S in itertools.combinations(half,r):
                if S[0]!=1 and n%S[0]!=0: pass
                G=circ(n,S)
                if not nx.is_connected(G): continue
                if nx.girth(G)<5: continue
                if not colorable(G,4):
                    print(n,S,G.number_of_edges(),flush=True)
        if n%2==0:
            for S in itertools.combinations(half,2):
                G=circ(n,S+(n//2,))
                if not nx.is_connected(G) or nx.girth(G)<5: continue
                if not colorable(G,4): print(n,S+(n//2,),G.number_of_edges(),'deg5',flush=True)
