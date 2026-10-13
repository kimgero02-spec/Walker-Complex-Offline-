# R50 common: W gadget, G*, 2-choosability (Erdos-Rubin-Taylor core test), unicyclic-even test
import sys, itertools, networkx as nx
sys.path.insert(0,'/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r49')
from gstar import W, WE, glue
def gstar():
    G=nx.complete_graph('abcd')
    glue(G,('a','b','c'),1); glue(G,('b','d','a'),2); glue(G,('c','d','a'),3); glue(G,('b','c','d'),4)
    glue(G,('a','c',(1,'q1')),5); glue(G,('d','a',(3,'q5')),6)
    return G
def core(H):
    H=H.copy()
    while True:
        r=[v for v in H if H.degree(v)<=1]
        if not r: return H
        H.remove_nodes_from(r)
def comp_ok(C, mode):
    """C: connected core component (min deg>=2) or single vertex. mode 'uni': even cycle only; 'ert': even cycle or theta_{2,2,2m}"""
    n=C.number_of_nodes(); e=C.number_of_edges()
    if n==1: return True
    if e==n: return n%2==0           # cycle
    if mode=='uni': return False
    if e==n+1:
        d3=[v for v in C if C.degree(v)==3]
        if len(d3)!=2 or any(C.degree(v) not in (2,3) for v in C): return False
        u,w=d3; H=C.copy()
        # path lengths between u and w
        lens=[]
        for s in C[u]:
            L=1; prev=u; cur=s
            while cur!=w:
                nxt=[t for t in C[cur] if t!=prev][0]; prev,cur=cur,nxt; L+=1
            lens.append(L)
        lens.sort(); return lens[0]==2 and lens[1]==2 and lens[2]%2==0
    return False
def bad_cores(G,S,mode):
    """return list of vertex sets of bad core components of G[S] (empty iff G[S] 2-choosable in mode)"""
    K=core(G.subgraph(S))
    out=[]
    for cc in nx.connected_components(K):
        if not comp_ok(K.subgraph(cc),mode): out.append(set(cc))
    return out
