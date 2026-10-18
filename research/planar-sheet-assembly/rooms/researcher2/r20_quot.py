# R20 과제2 정리 H 의 예 검산 (근거 아님): 결함 장 P_k 의 올 몫그래프 Q_k 는 사이클을 가진다.
import ast, itertools, networkx as nx
from networkx.algorithms.coloring import greedy_color
from r19_lib import chi, omega
def opt_col(G):
    k=chi(G); nodes=list(G.nodes())
    for strat in ['DSATUR','largest_first','smallest_last']:
        c=greedy_color(G,strategy=strat)
        if max(c.values())+1==k: return c
    # 역추적
    col={}
    order=sorted(nodes,key=lambda v:-G.degree(v))
    def bt(i):
        if i==len(order): return True
        v=order[i]; used={col[u] for u in G[v] if u in col}
        for c in range(k):
            if c not in used:
                col[v]=c
                if bt(i+1): return True
                del col[v]
        return False
    bt(0); return col
def check(name,P):
    V=set().union(*[set(G.nodes()) for G in P])
    for G in P: G.add_nodes_from(V)
    cols=[opt_col(G) for G in P]
    for k,G in enumerate(P):
        if chi(G)>omega(G):
            fib={v:tuple(cols[j][v] for j in range(len(P)) if j!=k) for v in V}
            Q=nx.Graph(); Q.add_nodes_from(set(fib.values()))
            for u,v in G.edges():
                if fib[u]!=fib[v]: Q.add_edge(fib[u],fib[v])
            print(name,"결함 장",k,"(chi,omega)=",(chi(G),omega(G)),"올 수",Q.number_of_nodes(),"Q 숲?",nx.is_forest(Q))
# K6 = T u T-bar (R19 정리 2.1(1))
T=nx.Graph([(0,1),(1,2),(2,3),(3,4),(4,0),(5,0),(5,2)]); Tb=nx.complement(T)
check("K6",[T,Tb])
# K7 = (C5 + K2) u 쌍뿔
A=nx.Graph([(0,1),(1,2),(2,3),(3,4),(4,0),(5,6)]); check("K7",[A,nx.complement(A)])
# 순환 예
for fn in ['r20_cyc3_out.txt','r20_tf12_out.txt']:
    L=open(fn).read().splitlines(); E=ast.literal_eval(L[1])
    if fn.startswith('r20_cyc'):
        n=int(L[0].split()[1]); P=[nx.Graph([(((a+k)%n,r),((b+k)%n,s)) for (a,r),(b,s) in E]) for k in range(n)]
    else: P=[nx.Graph(x) for x in E]
    check(fn,P)
