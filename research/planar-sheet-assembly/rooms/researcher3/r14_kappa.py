# R14: chromatic gluing factor kappa_D(q)=q^{|V0|-|V|} P_G(q)/prod_beta P_beta(q); check r=1 transfer formula
import networkx as nx, itertools
from fractions import Fraction as Fr
def P(H,q):
    nodes=list(H); n=len(nodes); cnt=0
    for c in itertools.product(range(q),repeat=n):
        d=dict(zip(nodes,c))
        if all(d[a]!=d[b] for a,b in H.edges()): cnt+=1
    return cnt
def cnt2(H,h1,h2,q,same):
    nodes=[x for x in H if x not in (h1,h2)]; tot=0
    for c in itertools.product(range(q),repeat=len(nodes)):
        d=dict(zip(nodes,c)); d[h1]=0; d[h2]=0 if same else 1
        if all(d[a]!=d[b] for a,b in H.edges()): tot+=1
    return tot
def kappa(pieces,q):
    G=nx.Graph(); V0=0; prod=1
    for p in pieces:
        G.add_nodes_from(p); G.add_edges_from(p.edges())
        for C in nx.connected_components(p):
            B=p.subgraph(C); V0+=B.number_of_nodes(); prod*=P(B,q)
    return Fr(q**(V0-G.number_of_nodes())*P(G,q),prod) if prod else None
E=lambda *es: nx.Graph(list(es))
def Kme(N): K=nx.complete_graph(N); K.remove_edge(0,1); return K
cyc={ 'K2=(K2,K2)':[(E((0,1)),0,1),(E((0,1)),0,1)],
      'K4=(K4-uv,K2)':[(Kme(4),0,1),(E((0,1)),0,1)],
      'K5=(K5-uv,K2)':[(Kme(5),0,1),(E((0,1)),0,1)],
      'K3=(P3,K2) [C7]':[(E((0,2),(2,1)),0,1),(E((0,1)),0,1)],
      'K3=three K2 [C9]':[(E((0,1)),0,1),(E((1,2)),1,2),(E((2,0)),2,0)],
      'C6=(P4,P4) two paths':[(E((0,1),(1,2),(2,3)),0,3),(E((3,4),(4,5),(5,0)),3,0)],
      'C5=(P3,P4)':[(E((0,1),(1,2)),0,2),(E((2,3),(3,4),(4,0)),2,0)]}
for name,bl in cyc.items():
    for q in (2,3,4,5):
        k=kappa([b for b,_,_ in bl],q)
        prodt=Fr(1)
        for B,h1,h2 in bl:
            x,y=cnt2(B,h1,h2,q,True),cnt2(B,h1,h2,q,False)
            prodt*=Fr(x-y,x+(q-1)*y) if x+(q-1)*y else 0
        pred=1+(q-1)*prodt
        print(f'{name:22s} q={q} kappa={k} formula={pred} match={k==pred}')
