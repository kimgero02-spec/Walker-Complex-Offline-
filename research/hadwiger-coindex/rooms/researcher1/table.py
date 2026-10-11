import networkx as nx, itertools, time, sys, json
from boxlib import *
from atlas import chrom

def kneser(n,k):
    V=[frozenset(c) for c in itertools.combinations(range(n),k)]
    G=nx.Graph(); G.add_nodes_from(V)
    for a,b in itertools.combinations(V,2):
        if not (a&b): G.add_edge(a,b)
    return nx.convert_node_labels_to_integers(G)
def schrijver(n,k):
    V=[frozenset(c) for c in itertools.combinations(range(n),k)
       if all(((x+1)%n) not in c for x in c)]
    G=nx.Graph(); G.add_nodes_from(V)
    for a,b in itertools.combinations(V,2):
        if not (a&b): G.add_edge(a,b)
    return nx.convert_node_labels_to_integers(G)
def lex(G,H):
    return nx.convert_node_labels_to_integers(nx.lexicographic_product(G,H))
def myc(k):
    G=nx.complete_graph(2)
    for _ in range(k-2): G=nx.convert_node_labels_to_integers(nx.mycielskian(G))
    return G

def analyze(name,G,chi_known=None,use_B=None,sw=True,hmax=40000,swmax=1500000):
    n=G.number_of_nodes(); t=time.time()
    chi=chi_known if chi_known else chrom(G)
    om=clique_number(G)
    tgt=chi
    h,ex=hadwiger_number(G,maxnodes=hmax) if n<=16 else (None,False)
    if use_B is None: use_B = n>11
    if use_B:
        _,S=B_simplices(G); k,hk,sc,allb=certified_conn(S); L=k+3   # conn(B0)=conn(B)+1 [기억-미검증]
    else:
        _,S=B0_simplices(G); k,hk,sc,allb=certified_conn(S); L=k+2
    L=max(L,2 if G.number_of_edges() else 1)
    if not nx.is_bipartite(G): L=max(L,3)
    U=chi; swr=None
    if sw:
        swr=sw_height(G,join=True,maxchains=swmax)
        if swr: U=min(U,swr[0]+1)
    row=dict(name=name,n=n,m=G.number_of_edges(),chi=chi,omega=om,h=h,h_exact=ex,L=L,U=U,sw=swr,useB=use_B,sc=sc,hk=hk,
             betti2={d:b for d,b in allb[2].items() if b},secs=round(time.time()-t,1))
    print(json.dumps(row,default=str),flush=True)
    return row

if __name__=='__main__':
    which=sys.argv[1]
    cases={
     'K':[(f'K{n}',nx.complete_graph(n),n) for n in range(2,7)],
     'C':[(f'C{n}',nx.cycle_graph(n),3) for n in (5,7,9)],
     'Pet':[('KG(5,2)=Petersen',kneser(5,2),3)],
     'KG62':[('KG(6,2)',kneser(6,2),4)],
     'SG':[('SG(6,2)',schrijver(6,2),4),('SG(7,2)',schrijver(7,2),5),('SG(8,3)',schrijver(8,3),4)],
     'Myc':[('Grotzsch=M4',myc(4),4),('M5',myc(5),5)],
     'Cat':[('C5[K2]',lex(nx.cycle_graph(5),nx.complete_graph(2)),5),('C7[K2]',lex(nx.cycle_graph(7),nx.complete_graph(2)),7)],
     'cC7':[('complement C7',nx.complement(nx.cycle_graph(7)),4)],
    }
    for name,G,chi in cases[which]:
        analyze(name,G,chi_known=chi)
