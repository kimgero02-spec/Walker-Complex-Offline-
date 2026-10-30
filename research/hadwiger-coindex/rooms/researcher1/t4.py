import networkx as nx
from boxlib import *
from table import lex
G=lex(nx.cycle_graph(5),nx.complete_graph(2))
n,S=B0_simplices(G); print(len(S))
k,hk,sc,allb=certified_conn(S); print(k,hk,sc,{p:{d:b for d,b in allb[p].items() if b} for p in allb})
_,S=B_simplices(G); k,hk,sc,allb=certified_conn(S); print('B',len(S),k,hk,sc,{p:{d:b for d,b in allb[p].items() if b} for p in allb})
n,el=poset_Hom(G); print('poset elems',len(el))
