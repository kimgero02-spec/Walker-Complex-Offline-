# R13 researcher1: 2-block splits of test graphs; planarity of blocks; cross-edge axioms; chi bounds. Small, guessing aid.
import itertools, networkx as nx

def C5K2():
    G=nx.Graph()
    for i in range(5):
        G.add_edge(('a',i),('b',i))
        j=(i+1)%5
        for x in 'ab':
            for y in 'ab': G.add_edge((x,i),(y,j))
    return G
def K4box():  # K_4 x K_2 (prism over K_4)
    G=nx.Graph()
    for s in 'AB':
        for i,j in itertools.combinations(range(4),2): G.add_edge((s,i),(s,j))
    for i in range(4): G.add_edge(('A',i),('B',i))
    return G
def chi(G):
    V=list(G.nodes()); idx={v:i for i,v in enumerate(V)}
    for k in range(1,len(V)+1):
        # backtracking
        col={}
        def bt(i):
            if i==len(V): return True
            v=V[i]
            used={col[u] for u in G[v] if u in col}
            for c in range(k):
                if c not in used:
                    col[v]=c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return k
def classify(G,A,B):
    cross=[(u,v) for u,v in G.edges() if (u in A)!=(v in A)]
    if not cross: return 'none',0
    deg={}
    for u,v in cross:
        deg[u]=deg.get(u,0)+1; deg[v]=deg.get(v,0)+1
    matching = max(deg.values())==1
    star = len(set(u for u,v in cross))==1 or len(set(v for u,v in cross))==1 or \
           len({u for u,v in cross})==1 or len({v for u,v in cross})==1
    # star: all edges share a common vertex
    common=set(cross[0])
    for e in cross: common &= set(e)
    star = len(common)>0
    return ('matching' if matching else ('star' if star else 'other')), len(cross)

def run(name,G):
    V=list(G.nodes()); n=len(V)
    print("==",name,"n=",n,"m=",G.number_of_edges(),"chi(G)=",chi(G))
    seen=set()
    for r in range(1,n//2+1):
        for A in itertools.combinations(V,r):
            A=set(A); B=set(V)-A
            key=frozenset([frozenset(A),frozenset(B)])
            if key in seen: continue
            seen.add(key)
            if not nx.check_planarity(G.subgraph(A))[0]: continue
            if not nx.check_planarity(G.subgraph(B))[0]: continue
            kind,cnum=classify(G,A,B)
            cA=chi(G.subgraph(A)); cB=chi(G.subgraph(B))
            print("  split",sorted(map(str,A)),"|",len(B),"| cross kind",kind,"#cross",cnum,"chi-sum",cA+cB)
if __name__=="__main__":
    run("K5",nx.complete_graph(5))
    run("K6",nx.complete_graph(6))
    run("C5[K2]",C5K2())
    run("K4xK2",K4box())
