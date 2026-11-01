# R05 researcher1: 두 잎 판 검사 도구
import itertools, networkx as nx

def colorings(Q, k):
    """Q 의 적정 k-색칠 전부 (색 이름 대칭 제거: 첫 등장 순서 정규화)."""
    nodes = sorted(Q.nodes(), key=lambda v: -Q.degree(v))
    # BFS-ish order for pruning
    order=[]; seen=set()
    for s in nodes:
        if s in seen: continue
        for v in nx.bfs_tree(Q, s):
            if v not in seen: seen.add(v); order.append(v)
    out=[]; col={}
    def bt(i, mx):
        if i==len(order): out.append(dict(col)); return
        v=order[i]; used={col[u] for u in Q[v] if u in col}
        for c in range(min(k, mx+2)):
            if c not in used:
                col[v]=c; bt(i+1, max(mx,c)); del col[v]
    bt(0,-1); return out

def chi(Q):
    for k in range(1, Q.number_of_nodes()+1):
        if has_col(Q,k): return k

def has_col(Q,k):
    order=list(nx.dfs_preorder_nodes(Q)) if nx.is_connected(Q) else list(Q.nodes())
    col={}
    def bt(i,mx):
        if i==len(order): return True
        v=order[i]; used={col[u] for u in Q[v] if u in col}
        for c in range(min(k,mx+2)):
            if c not in used:
                col[v]=c
                if bt(i+1,max(mx,c)): return True
                del col[v]
        return False
    return bt(0,-1)

def indep_triples(Q):
    return [t for t in itertools.combinations(sorted(Q.nodes(),key=str),3)
            if not any(Q.has_edge(a,b) for a,b in itertools.combinations(t,2))]

def masks(Q, cols, triples):
    M={}
    for t in triples:
        m=0
        for i,c in enumerate(cols):
            if len({c[v] for v in t})<3: m|=1<<i
        M[t]=m
    return M

def two_leaf_pairs(Q, disjoint_only=False, k=4):
    """4-색칠마다 T1 또는 T2 가 무지개인 (T1,T2) 쌍 목록."""
    cols=colorings(Q,k); T=indep_triples(Q); M=masks(Q,cols,T)
    res=[]
    for t1,t2 in itertools.combinations(T,2):
        if disjoint_only and set(t1)&set(t2): continue
        if M[t1]&M[t2]==0: res.append((t1,t2))
    return res, len(cols)

def assemble(Q, Ts):
    G=nx.Graph(Q)
    for i,t in enumerate(Ts):
        h1,h2=('h',i,1),('h',i,2)
        G.add_edge(h1,h2)
        for v in t: G.add_edge(h1,v); G.add_edge(h2,v)
    return G
