import networkx as nx, time, itertools
from networkx.generators.atlas import graph_atlas_g
from boxlib import *
def order_complex_join(G):
    n,el=poset_Hom(G)
    E=[('p',0),('p',1)]+[('e',a,b) for a,b in el]
    N=len(E)
    def lt(x,y):
        if x[0]=='p': return y[0]=='e'
        if y[0]=='p': return False
        return x!=y and x[1]&y[1]==x[1] and x[2]&y[2]==x[2]
    up=[[j for j in range(N) if j!=i and lt(E[i],E[j])] for i in range(N)]
    S=[]
    def rec(c):
        S.append(sum(1<<x for x in c))
        for j in up[c[-1]]: rec(c+[j])
    for i in range(N): rec([i])
    return S
def info(name,G):
    n,S=B0_simplices(G); k,hk,sc,allb=certified_conn(S)
    b0={d:b for d,b in allb[2].items() if b}
    S2=order_complex_join(G)
    b,_=reduced_betti(S2,2); bj={d:x for d,x in b.items() if x}
    print(name,'B0 betti2',b0,'cert conn',k,'| join model betti2',bj,flush=True)
A=graph_atlas_g()
for i in (878,998,1002,1101,1170): info(i,A[i])
info('K4',nx.complete_graph(4)); info('C5',nx.cycle_graph(5))
