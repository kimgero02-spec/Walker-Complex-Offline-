# Strengthening K_all: "every 4-coloring has a connected Kempe pair". Look for one 4-coloring with all 6 pairs disconnected.
import networkx as nx, itertools
from tri import dual
def colorings(G):
    V=sorted(G, key=lambda v:-G.degree(v)); c={}
    def rec(i):
        if i==len(V): yield dict(c); return
        v=V[i]
        for k in range(4):
            if all(c.get(u)!=k for u in G[v]):
                c[v]=k; yield from rec(i+1); del c[v]
    yield from rec(0)
def allbad(G,c):
    return all(not nx.is_connected(G.subgraph([v for v in G if c[v] in p])) for p in itertools.combinations(range(4),2))
if __name__=="__main__":
   for name,G in [('ico',nx.icosahedral_graph()),('tutte*',dual(nx.tutte_graph()))]:
      n=0; found=None
      for c in colorings(G):
          n+=1
          if allbad(G,c): found=c; break
      print(name,'colorings scanned',n,'all-pairs-disconnected coloring:',found)
