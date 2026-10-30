# R25 researcher3: find smallest G (chi=k) with nonadjacent u,v such that some Kempe class of
# optimal k-colorings forces u,v different but u,v are NOT forced different overall.
# (decisive example: "Kempe-local forcing" != "forced difference")
import itertools, networkx as nx
from networkx.generators.atlas import graph_atlas_g

def colorings(G,k):
    nodes=list(G); out=[]
    def bt(i,col):
        if i==len(nodes): out.append(tuple(col[v] for v in nodes)); return
        v=nodes[i]
        for c in range(k):
            if all(col.get(x)!=c for x in G[v]):
                col[v]=c; bt(i+1,col); del col[v]
    bt(0,{}); return nodes,out

def canon(c):  # partition into colour classes (mod S_k)
    m={};r=[]
    for x in c:
        if x not in m: m[x]=len(m)
        r.append(m[x])
    return tuple(r)

def kempe_nbrs(G,nodes,c,k):
    idx={v:i for i,v in enumerate(nodes)}
    for a,b in itertools.combinations(range(k),2):
        S=[v for v in nodes if c[idx[v]] in (a,b)]
        for comp in nx.connected_components(G.subgraph(S)):
            d=list(c)
            for v in comp: d[idx[v]]= b if c[idx[v]]==a else a
            yield canon(d)

for G in graph_atlas_g():
    if G.number_of_nodes()<4 or not nx.is_connected(G): continue
    for k in range(2,5):
        nodes,cols=colorings(G,k)
        if cols: break
    P=set(canon(c) for c in cols)
    # Kempe classes
    adj={p:set(kempe_nbrs(G,nodes,p,k)) for p in P}
    seen=set();classes=[]
    for p in P:
        if p in seen: continue
        st=[p];cl={p};seen.add(p)
        while st:
            x=st.pop()
            for y in adj[x]:
                if y not in seen: seen.add(y);cl.add(y);st.append(y)
        classes.append(cl)
    if len(classes)<2: continue
    idx={v:i for i,v in enumerate(nodes)}
    for u,v in itertools.combinations(nodes,2):
        if G.has_edge(u,v): continue
        diff=[all(p[idx[u]]!=p[idx[v]] for p in cl) for cl in classes]
        if any(diff) and not all(diff):
            print("n",G.number_of_nodes(),"k",k,"edges",sorted(G.edges()),"u,v",u,v,
                  "#classes",len(classes),"forcing pattern",diff)
            raise SystemExit
print("none")
