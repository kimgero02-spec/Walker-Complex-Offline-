import itertools, networkx as nx
def has_odd_Kt(G,t):
    nodes=list(G.nodes()); n=len(nodes)
    for col in itertools.product((0,1),repeat=n):
        if col[0]==1: continue
        c=dict(zip(nodes,col))
        Hc=nx.Graph(); Hc.add_nodes_from(nodes)
        Hc.add_edges_from((u,v) for u,v in G.edges() if c[u]!=c[v])
        # 분할: 라벨 배정
        for lab in itertools.product(range(-1,t),repeat=n):
            used=sorted(set(lab)-{-1})
            if used!=list(range(t)): continue
            # 대칭 제거: 라벨 첫 등장 순서
            first=[]; ok=True
            for l in lab:
                if l>=0 and l not in first:
                    if l!=len(first): ok=False;break
                    first.append(l)
            if not ok: continue
            sets=[[v for v,l in zip(nodes,lab) if l==i] for i in range(t)]
            if not all(nx.is_connected(Hc.subgraph(s)) for s in sets): continue
            lm=dict(zip(nodes,lab)); pairs=set()
            for u,v in G.edges():
                if lm[u]>=0 and lm[v]>=0 and lm[u]!=lm[v] and c[u]==c[v]:
                    pairs.add(frozenset((lm[u],lm[v])))
            if len(pairs)==t*(t-1)//2: return True
    return False
if __name__=='__main__':
    from networkx.generators.atlas import graph_atlas_g
    G=graph_atlas_g()[1227]; print(sorted(G.edges()), has_odd_Kt(G,5))
