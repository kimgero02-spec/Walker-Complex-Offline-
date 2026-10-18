# R15: check r=2 closed forms and flow expansion of kappa
import networkx as nx, itertools
from fractions import Fraction as Fr
def colorings(H,q,fixed):
    nodes=[x for x in H if x not in fixed]; tot=0
    for c in itertools.product(range(q),repeat=len(nodes)):
        d=dict(zip(nodes,c)); d.update(fixed)
        if all(d[a]!=d[b] for a,b in H.edges()): tot+=1
    return tot
P=lambda H,q: colorings(H,q,{})
def kappa(pieces,q):
    G=nx.Graph(); V0=0; prod=1
    for p in pieces:
        G.add_nodes_from(p); G.add_edges_from(p.edges())
        for C in nx.connected_components(p):
            B=p.subgraph(C); V0+=B.number_of_nodes(); prod*=P(B,q)
    return Fr(q**(V0-G.number_of_nodes())*P(G,q),prod)
def tau(B,hubs,q):  # normalized tensor
    Pb=P(B,q); k=len(hubs)
    return {c:Fr(q**k*colorings(B,q,dict(zip(hubs,c))),Pb) for c in itertools.product(range(q),repeat=k)}
def E(f,q,k): return sum(f.values(),Fr(0))/q**k
psi=lambda a,b,q: q*(a==b)-1
Xi=lambda a,b,c,q: q*q*(a==b==c)-q*((a==b)+(b==c)+(a==c))+2
def coef3(B,h,q):
    t=tau(B,h,q)
    s={(i,j):E({c:v*psi(c[i],c[j],q) for c,v in t.items()},q,3)/(q-1) for i,j in [(0,1),(0,2),(1,2)]}
    u=E({c:v*Xi(*c,q) for c,v in t.items()},q,3)/((q-1)*(q-2))
    return s,u
def t2(B,h,q):
    t=tau(B,h,q); return E({c:v*psi(c[0],c[1],q) for c,v in t.items()},q,2)/(q-1)
Eg=lambda *es: nx.Graph(list(es))
def Kn(vs): return nx.complete_graph(vs)
for q in (3,4,5):
    # (a) theta, hubs u=0,v=1: (K4-uv, K2, K2)
    K4m=Kn(4); K4m.remove_edge(0,1)
    T=[t2(K4m,(0,1),q),t2(Eg((0,1)),(0,1),q),t2(Eg((0,1)),(0,1),q)]
    f=1+(q-1)*(T[0]*T[1]+T[0]*T[2]+T[1]*T[2])+(q-1)*(q-2)*T[0]*T[1]*T[2]
    print('a',q,kappa([K4m,Eg((0,1)),Eg((0,1))],q),f)
    # (b) theta, two 3-hub blocks sharing hubs 1,2,3 directly: K4{0123}, K4{1234}
    if q>=4:
     A=Kn([0,1,2,3]); B=Kn([1,2,3,4])
     sA,uA=coef3(A,(1,2,3),q); sB,uB=coef3(B,(1,2,3),q)
     f=1+(q-1)*sum(sA[k]*sB[k] for k in sA)+(q-1)*(q-2)*uA*uB
     print('b',q,kappa([A,B],q),f)
    # (c) block K3{1,2,3} + K2 to hub 0 from each: K4
    A=Kn([1,2,3]); sA,uA=coef3(A,(1,2,3),q); T=t2(Eg((0,1)),(0,1),q)
    f=1+(q-1)*sum(sA[k]*T*T for k in sA)+(q-1)*(q-2)*uA*T**3
    print('c',q,kappa([A,Eg((0,1)),Eg((0,2)),Eg((0,3))],q),f)
# flow expansion for 2-terminal decompositions: K4 into 6 edges, K_{2,3} into 3 paths
def flowpoly(edges,nodes,q):
    cnt=0
    for ks in itertools.product(range(1,q),repeat=len(edges)):
        net={v:0 for v in nodes}
        for (a,b),k in zip(edges,ks): net[a]+=k; net[b]-=k
        if all(x%q==0 for x in net.values()): cnt+=1
    return cnt
def flowexp(chains,nodes,q):  # chains: list of (a,b,T)
    tot=Fr(0)
    for r in range(len(chains)+1):
        for F in itertools.combinations(chains,r):
            w=Fr(1)
            for a,b,T in F: w*=T
            tot+=w*flowpoly([(a,b) for a,b,_ in F],nodes,q)
    return tot
for q in (3,4,5):
    K4=Kn(4); T=Fr(-1,q-1)
    print('flow K4 edges',q,kappa([Eg(e) for e in K4.edges()],q),flowexp([(a,b,T) for a,b in K4.edges()],range(4),q))
    paths=[Eg((0,'x%d'%i),('x%d'%i,1)) for i in range(3)]
    print('flow K23 paths',q,kappa(paths,q),flowexp([(0,1,T*T)]*3,[0,1],q))
