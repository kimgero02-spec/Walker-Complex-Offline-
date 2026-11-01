import sys
sys.path.insert(0,'.')
from r4_blowup import *
for name,G in [("Petersen",nx.petersen_graph()),("W5",nx.wheel_graph(6)),("Cbar7",nx.complement(nx.cycle_graph(7))),("C5",nx.cycle_graph(5)),("K4",nx.complete_graph(4)),("C6",nx.cycle_graph(6))]:
    G=nx.convert_node_labels_to_integers(G)
    a=types(G)[3]; b=types2(G)[3]
    print(name,len(a),len(b),a==b)
