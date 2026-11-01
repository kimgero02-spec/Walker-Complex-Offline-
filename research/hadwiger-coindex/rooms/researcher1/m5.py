import networkx as nx
from boxlib import *
from table import myc
G=myc(5); print(G.number_of_nodes(),G.number_of_edges(),clique_number(G))
_,S=B_simplices(G); print(len(S))
k,hk,sc,allb=certified_conn(S); print('B cert conn',k,hk,sc,{d:b for d,b in allb[2].items() if b})
