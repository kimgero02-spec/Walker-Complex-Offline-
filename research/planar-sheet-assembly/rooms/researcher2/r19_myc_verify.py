import networkx as nx, ast
from r19_lib import chi, omega, planar
G=nx.mycielski_graph(5)
L=open('r19_myc_out.txt').read().splitlines()
B=nx.Graph(ast.literal_eval(L[-2].split('B edges ')[1])); T=nx.Graph(ast.literal_eval(L[-1].split('T edges ')[1]))
U=set(map(frozenset,B.edges()))|set(map(frozenset,T.edges()))
print("union==E(M5):",U==set(map(frozenset,G.edges())), "overlap:",len(set(map(frozenset,B.edges()))&set(map(frozenset,T.edges()))))
print("planar B,T:",planar(B),planar(T),"chi B,T:",chi(B),chi(T),"omega(M5):",omega(G))
print("chi(M5):",chi(G))
