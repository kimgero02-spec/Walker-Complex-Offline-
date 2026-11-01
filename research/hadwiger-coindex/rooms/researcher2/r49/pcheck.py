import sys, networkx as nx
sys.path.insert(0,'../r48')
from cegar import cegar
G=nx.read_edgelist(sys.argv[1],nodetype=int)
M,it=cegar(G,fix={0:(1,2)},verbose=True)
print('RESULT',M,it)
