# R18 확인용 (근거 아님): 소수 예의 chi 계산, sigma_n 문턱, C5*C5 의 chi
import itertools, networkx as nx
from functools import reduce
def chi(G):
    n=G.number_of_nodes()
    if n==0: return 0
    nodes=list(G.nodes()); idx={v:i for i,v in enumerate(nodes)}
    adj=[[idx[u] for u in G[v]] for v in nodes]
    order=sorted(range(n),key=lambda i:-len(adj[i]))
    for q in range(1,n+1):
        col=[-1]*n
        def bt(t,used):
            if t==n: return True
            i=order[t]
            for c in range(min(q,used+1)):
                if all(col[j]!=c for j in adj[i]):
                    col[i]=c
                    if bt(t+1,max(used,c+1)): return True
                    col[i]=-1
            return False
        if bt(0,0): return q
def g(edges,V=None):
    G=nx.Graph(); 
    if V: G.add_nodes_from(V)
    G.add_edges_from(edges); return G
# K4 = C4a u C4b
a=[(1,2),(2,3),(3,4),(4,1)]; b=[(1,3),(3,2),(2,4),(4,1)]
print("K4=C4uC4", chi(g(a)),chi(g(b)),chi(g(a+b)))
# K5 = P1 u P2 (join mechanism, product not tight)
P1=[(1,2),(1,3),(2,4)]; P2=[(3,4),(3,5),(4,5),(1,4),(1,5),(2,3),(2,5)]
G=g(P1+P2); print("K5 example", chi(g(P1)),chi(g(P2)),chi(G),G.number_of_edges())
# K4 = C4 u 2K2
print("K4=C4u2K2", chi(g(a)), chi(g([(1,3),(2,4)])), chi(g(a+[(1,3),(2,4)])))
# Groetzsch bit decomposition
Gr=nx.mycielski_graph(4); c=nx.coloring.greedy_color(Gr)
# exact 4-coloring via search
import itertools
nodes=list(Gr.nodes())
def find4():
    col={}
    def bt(i):
        if i==len(nodes): return True
        v=nodes[i]
        for k in range(4):
            if all(col.get(u)!=k for u in Gr[v]):
                col[v]=k
                if bt(i+1): return True
                del col[v]
        return False
    bt(0); return col
col=find4()
E1=[(u,v) for u,v in Gr.edges() if (col[u]>>1)!=(col[v]>>1)]
E2=[(u,v) for u,v in Gr.edges() if (col[u]&1)!=(col[v]&1)]
print("Groetzsch", chi(Gr), chi(g(E1)), chi(g(E2)), nx.is_connected(nx.complement(Gr)))
# sigma_n thresholds
def sigma(n,x):
    best=None
    for m in itertools.product(range(1,x+1),repeat=n):
        if reduce(lambda p,q:p*q,m)>=x:
            s=sum(m); best=s if best is None or s<best else best
    return best
for n in [2,3,4]:
    print("n",n,[ (x,sigma(n,x)) for x in range(1,13)])
# C5 * C5 (disjunctive product)
C5=nx.cycle_graph(5); H=nx.Graph()
V=[(i,j) for i in range(5) for j in range(5)]; H.add_nodes_from(V)
for (i,j),(k,l) in itertools.combinations(V,2):
    if C5.has_edge(i,k) or C5.has_edge(j,l): H.add_edge((i,j),(k,l))
print("chi(C5*C5)",chi(H))
