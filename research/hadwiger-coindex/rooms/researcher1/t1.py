import networkx as nx
from boxlib import *
for name,G in [('K2',nx.complete_graph(2)),('K3',nx.complete_graph(3)),('K4',nx.complete_graph(4)),('K5',nx.complete_graph(5)),('C5',nx.cycle_graph(5)),('C7',nx.cycle_graph(7)),('P3',nx.path_graph(3))]:
    n,S=B0_simplices(G)
    k,hk,sc,allb=certified_conn(S)
    print(name,'B0 #simp',len(S),'cert conn',k,'hconn',hk,'sc',sc,{p:{d:b for d,b in allb[p].items() if b} for p in allb})
    n,S=B_simplices(G)
    k,hk,sc,allb=certified_conn(S)
    print('   B  #simp',len(S),'cert conn',k,'hconn',hk,'sc',sc,{d:b for d,b in allb[2].items() if b})
