# R19: Mycielskian of W5 -> split into planar bipartite P1 + planar 3-chromatic P2 with owned partition
import networkx as nx, itertools, random
def W5():
    H=nx.Graph(); H.add_edges_from([(0,i) for i in range(1,6)]+[(i,i%5+1) for i in range(1,6)]); return H
def myc(H):
    G=nx.Graph(); n=len(H)
    for a,b in H.edges(): G.add_edge('v%d'%a,'v%d'%b); G.add_edge('u%d'%a,'v%d'%b); G.add_edge('v%d'%a,'u%d'%b)
    for a in H: G.add_edge('z','u%d'%a)
    return G
def chi_le(G,k):
    nodes=sorted(G,key=lambda x:-G.degree(x)); col={}
    def bt(i):
        if i==len(nodes): return True
        v=nodes[i]; used={col[w] for w in G[v] if w in col}
        for c in range(k):
            if c not in used:
                col[v]=c
                if bt(i+1): return True
                del col[v]
        return False
    return bt(0)
def chi(G):
    k=1
    while not chi_le(G,k): k+=1
    return k
G=myc(W5()); print(len(G),G.number_of_edges(),'chi',chi(G),'omega',max(len(c) for c in nx.find_cliques(G)))
# 5-colouring: H colours c, u copies same, z gets 4
c={0:0,1:1,2:2,3:1,4:2,5:3}
f={'v%d'%a:c[a] for a in c}; f.update({'u%d'%a:c[a] for a in c}); f['z']=4
random.seed(1)
best=None
for trial in range(4000):
    perm=random.sample(range(5),5)  # which colours -> V1 (first two)
    tup={}
    V1c=perm[:2]; V2c=perm[2:]
    # V1 colours distinct alpha, V2 colours distinct beta, all tuples distinct
    opts=[t for t in itertools.product(range(2),range(3))]
    random.shuffle(opts)
    for combo in itertools.permutations(opts,5):
        T=dict(zip(perm,combo))
        if T[V1c[0]][0]!=T[V1c[1]][0] and len({T[x][1] for x in V2c})==3: break
    g={v:T[f[v]] for v in G}
    forced1=[];forced2=[];free=[]
    for a,b in G.edges():
        if g[a][0]==g[b][0]: forced2.append((a,b))
        elif g[a][1]==g[b][1]: forced1.append((a,b))
        else:
            inV1=f[a] in V1c and f[b] in V1c; inV2=f[a] in V2c and f[b] in V2c
            if inV1: forced1.append((a,b))
            elif inV2: forced2.append((a,b))
            else: free.append((a,b))
    P1=nx.Graph(forced1); P2=nx.Graph(forced2)
    if not nx.check_planarity(P1)[0] or not nx.check_planarity(P2)[0]: continue
    ok=True
    random.shuffle(free)
    for e in free:
        P1.add_edge(*e)
        if nx.check_planarity(P1)[0]: continue
        P1.remove_edge(*e); P2.add_edge(*e)
        if nx.check_planarity(P2)[0]: continue
        ok=False;break
    if ok:
        print('found trial',trial,'perm',perm,'T',T)
        print('P1',sorted(P1.edges()),P1.number_of_edges(),'bip',nx.is_bipartite(P1))
        print('P2',sorted(P2.edges()),P2.number_of_edges(),'chi',chi(P2))
        V1=[v for v in G if f[v] in V1c]; V2=[v for v in G if f[v] in V2c]
        print('V1',V1);print('V2',V2)
        print('owned', all(P1.has_edge(a,b) for a,b in G.subgraph(V1).edges()), all(P2.has_edge(a,b) for a,b in G.subgraph(V2).edges()))
        break
