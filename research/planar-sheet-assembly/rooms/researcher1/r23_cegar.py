# R23: (2,3) 소유 분해 탐색기 (CEGAR: SAT + 쿠라토프스키 절단). 후보 탐색 전용, 근거 아님.
# 변수: x_e (e in P1), s_v (v in V1), b_v (P1 이분 쪽), c_{v,i} (P2 3-색칠)
import networkx as nx, itertools, sys, json
from pysat.solvers import Cadical153
def mycielski(H):
    G=nx.Graph(); n=list(H.nodes())
    for v in n: G.add_node(('v',v)); G.add_node(('u',v))
    G.add_node('z')
    for a,b in H.edges():
        G.add_edge(('v',a),('v',b)); G.add_edge(('u',a),('v',b)); G.add_edge(('v',a),('u',b))
    for v in n: G.add_edge('z',('u',v))
    return G
def grotzsch():
    return nx.convert_node_labels_to_integers(mycielski(nx.cycle_graph(5)))
def search(G, maxit=20000, extra=None, verbose=True):
    V=list(G.nodes()); E=[tuple(e) for e in G.edges()]
    cnt=[0]
    def nv(): cnt[0]+=1; return cnt[0]
    x={e:nv() for e in E}; s={v:nv() for v in V}; b={v:nv() for v in V}
    c={(v,i):nv() for v in V for i in range(3)}
    S=Cadical153()
    for (u,v) in E:
        e=(u,v)
        # e in P1 -> b_u != b_v
        S.add_clause([-x[e],b[u],b[v]]); S.add_clause([-x[e],-b[u],-b[v]])
        # e in P2 -> colors differ
        for i in range(3): S.add_clause([x[e],-c[(u,i)],-c[(v,i)]])
        # ownership: both in V1 -> P1 ; both in V2 -> P2
        S.add_clause([-s[u],-s[v],x[e]]); S.add_clause([s[u],s[v],-x[e]])
    for v in V: S.add_clause([c[(v,i)] for i in range(3)])
    if extra: extra(S,x,s,b,c)
    for it in range(maxit):
        if not S.solve(): return None,it
        m=set(l for l in S.get_model() if l>0)
        P1=[e for e in E if x[e] in m]; P2=[e for e in E if x[e] not in m]
        ok=True
        for P,sign in ((P1,-1),(P2,1)):
            H=nx.Graph(P)
            pl,cert=nx.check_planarity(H,counterexample=True)
            if not pl:
                ok=False
                K=[tuple(e) for e in cert.edges()]
                cl=[]
                for e in K:
                    ee=e if e in x else (e[1],e[0])
                    cl.append(sign*x[ee])
                S.add_clause(cl)
        if ok:
            V1=[v for v in V if s[v] in m]
            return dict(P1=P1,P2=P2,V1=V1),it
        if verbose and it%200==0: print('it',it,flush=True)
    return 'timeout',maxit
def verify(G,sol):
    P1=nx.Graph(sol['P1']); P2=nx.Graph(sol['P2'])
    V1=set(sol['V1']); V2=set(G)-V1
    assert set(map(frozenset,G.edges()))==set(map(frozenset,sol['P1']))|set(map(frozenset,sol['P2']))
    out=dict(P1planar=nx.check_planarity(P1)[0],P2planar=nx.check_planarity(P2)[0],P1bip=nx.is_bipartite(P1))
    e1=set(map(frozenset,sol['P1'])); e2=set(map(frozenset,sol['P2']))
    out['own']=all(frozenset(e) in e1 for e in G.subgraph(V1).edges()) and all(frozenset(e) in e2 for e in G.subgraph(V2).edges())
    from r23_circ import colorable
    out['P2_3col']=colorable(P2,3); out['G_4col']=colorable(G,4); out['girth']=nx.girth(G)
    return out
if __name__=="__main__":
    G=nx.convert_node_labels_to_integers(mycielski(grotzsch()))
    print(G.number_of_nodes(),G.number_of_edges(),nx.girth(G))
    sol,it=search(G)
    print('iters',it)
    if isinstance(sol,dict):
        print(verify(G,sol)); json.dump({k:[list(e) if isinstance(e,tuple) else e for e in v] for k,v in sol.items()},open('r23_myc_grotzsch.json','w'))
    else: print(sol)
