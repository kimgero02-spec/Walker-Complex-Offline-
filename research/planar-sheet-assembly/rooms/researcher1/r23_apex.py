# R23: 꼭짓점 하나 덧붙인 평면 둘레5 그래프 Q+y 가 4-색 (3-색칠 불가) 이 될 수 있는지 후보 탐색. 근거 아님.
import networkx as nx, random, sys, itertools
import numpy as np
from scipy.spatial import Delaunay
from pysat.solvers import Cadical153
def rand_planar_girth5(n,seed):
    rng=np.random.default_rng(seed); pts=rng.random((n,2))
    tri=Delaunay(pts); E=set()
    for s in tri.simplices:
        for a,b in itertools.combinations(sorted(s),2): E.add((a,b))
    E=list(E); random.Random(seed).shuffle(E)
    G=nx.Graph(); G.add_nodes_from(range(n))
    for a,b in E:
        try: d=nx.shortest_path_length(G,a,b)
        except nx.NetworkXNoPath: d=99
        if d>=4: G.add_edge(a,b)
    return G
def threecol_with(G,S):
    # Q + y(S): 3-coloring of Q with S using <=2 colors
    V=list(G); idx={v:i for i,v in enumerate(V)}; var=lambda v,c: 3*idx[v]+c+1
    s=Cadical153(); Y=3*len(V)+1
    for v in V: s.add_clause([var(v,c) for c in range(3)])
    for u,v in G.edges():
        for c in range(3): s.add_clause([-var(u,c),-var(v,c)])
    # y colour: Y+c
    s.add_clause([Y+c for c in range(3)])
    for v in S:
        for c in range(3): s.add_clause([-var(v,c),-(Y+c)])
    if s.solve():
        m=set(l for l in s.get_model() if l>0)
        col={v:[c for c in range(3) if var(v,c) in m][0] for v in V}
        yc=[c for c in range(3) if Y+c in m][0]
        return col,yc
    return None
def find_S(G,maxit=5000):
    V=list(G); t={v:i+1 for i,v in enumerate(V)}
    s=Cadical153()
    D=dict(nx.all_pairs_shortest_path_length(G,cutoff=2))
    for u,v in itertools.combinations(V,2):
        if v in D[u]: s.add_clause([-t[u],-t[v]])
    for it in range(maxit):
        if not s.solve(): return None,it
        m=set(l for l in s.get_model() if l>0); S=[v for v in V if t[v] in m]
        r=threecol_with(G,S)
        if r is None: return S,it
        col,yc=r
        # 같은 색칠의 세 색 모두에 대해 절 추가 (색 이름 바꿈 대칭)
        for c in range(3):
            s.add_clause([t[v] for v in V if col[v]==c])
    return 'timeout',maxit
if __name__=="__main__":
    n0,n1,seeds=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
    for n in range(n0,n1+1,5):
        for sd in range(seeds):
            G=rand_planar_girth5(n,sd)
            S,it=find_S(G)
            print(n,sd,G.number_of_edges(),'S=',S if S is None or S=='timeout' else len(S),it,flush=True)
            if isinstance(S,list):
                import json; json.dump(dict(E=[list(map(int,e)) for e in G.edges()],S=list(map(int,S))),open(f'r23_apex_{n}_{sd}.json','w'))
