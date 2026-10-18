# R17: 뫼비우스 사다리 M12 의 h (예 확인용) 와 K5 모형
import networkx as nx
from r17_model import search
G=nx.cycle_graph(12); G.add_edges_from((i,i+6) for i in range(6))
r=search(G,5); print('K5 model in M12:', [sorted(b) for b in r] if r else None)
