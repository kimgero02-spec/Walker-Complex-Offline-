import itertools, networkx as nx, json
def simple_paths(G,a,b,maxlen=8):
    return nx.all_simple_paths(G,a,b,cutoff=maxlen)
def has_top_K(G,t):
    nodes=list(G.nodes())
    for S in itertools.combinations(nodes,t):
        if any(G.degree(v)<t-1 for v in S): continue
        pairs=list(itertools.combinations(S,2))
        Sset=set(S)
        def rec(i,used):
            if i==len(pairs): return True
            a,b=pairs[i]
            for p in nx.all_simple_paths(G,a,b):
                inner=set(p[1:-1])
                if inner&Sset or inner&used: continue
                if rec(i+1,used|inner): return True
            return False
        if rec(0,set()): return True
    return False
def has_imm_K(G,t):
    """약한 이머전: t 개 정점, 쌍마다 간선-서로소 경로 (경로는 다른 정점 통과 가능, 선택 정점도 통과 가능)."""
    nodes=list(G.nodes())
    for S in itertools.combinations(nodes,t):
        if any(G.degree(v)<t-1 for v in S): continue
        pairs=list(itertools.combinations(S,2))
        def rec(i,used):
            if i==len(pairs): return True
            a,b=pairs[i]
            for p in nx.all_simple_paths(G,a,b):
                es={frozenset(e) for e in zip(p,p[1:])}
                if es&used: continue
                if rec(i+1,used|es): return True
            return False
        if rec(0,frozenset()): return True
    return False
if __name__=='__main__':
    from networkx.generators.atlas import graph_atlas_g
    A=graph_atlas_g(); r=json.load(open('atlas2.json'))
    from boxlib import clique_number
    bad=[x for x in r if x['L']>clique_number(A[x['i']]) and x['L']>=4]
    res=[]
    for x in bad:
        G=A[x['i']]; t=x['L']
        res.append((x['i'],t,has_top_K(G,t),has_imm_K(G,t)))
    print(res)
    print('failures',[y for y in res if not (y[2] and y[3])])
