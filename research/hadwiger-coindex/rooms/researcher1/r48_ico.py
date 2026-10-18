# R48: 결정적 예 확인 (정이십면체 쌍 + 3-정규 교차), K_7 분할, K_8-PM
import networkx as nx, itertools
def colorable(G,k):
    nodes=sorted(G, key=lambda v:-G.degree(v)); col={}
    def bt(i):
        if i==len(nodes): return True
        v=nodes[i]; used={col[u] for u in G[v] if u in col}
        for c in range(k):
            if c not in used:
                col[v]=c
                if bt(i+1): return True
                del col[v]
        return False
    return bt(0), dict(col)
def chi(G):
    for k in range(1,9):
        if colorable(G,k)[0]: return k
I=nx.icosahedral_graph()
def pair(shifts):
    G=nx.Graph()
    G.add_edges_from(((1,u),(1,v)) for u,v in I.edges())
    G.add_edges_from(((2,u),(2,v)) for u,v in I.edges())
    for i in range(12):
        for s in shifts: G.add_edge((1,i),(2,(i+s)%12))
    return G
for sh in [(0,1,2),(0,1,5),(0,3,7),(0,4,8)]:
    G=pair(sh)
    h=[sum(1 for u in G[v] if u[0]!=v[0]) for v in G]
    dom=[(u,w) for u,w in itertools.combinations(G,2) if not G.has_edge(u,w) and (set(G[u])<=set(G[w]) or set(G[w])<=set(G[u]))]
    print(sh,'n',G.number_of_nodes(),'m',G.number_of_edges(),'deg',set(dict(G.degree()).values()),'h',set(h),'chi',chi(G),'domination',len(dom))
# 정이십면체 비인접 쌍의 공통 이웃 수
print('ico nonadj CN sizes',{len(set(I[u])&set(I[w])) for u,w in itertools.combinations(I,2) if not I.has_edge(u,w)})
# K_8 - PM = 두 K_4 + 3-정규 교차
G=nx.complete_graph(8); G.remove_edges_from([(i,i+4) for i in range(4)])
print('K8-PM chi',chi(G))
