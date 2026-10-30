import networkx as nx, time
from r03_conv import Qd_search
from r03_tsum import gadget
t=time.time(); G=gadget(2,2,2,2); print("T+2 per pair+2 triple n=",G.number_of_nodes(),"planar",nx.check_planarity(G)[0],"Q3",Qd_search(G,3,120),round(time.time()-t,1),flush=True)
V8=nx.circulant_graph(8,[1,4]); print("V8 Q3",Qd_search(V8,3,60),"Q2",Qd_search(V8,2,60),flush=True)
