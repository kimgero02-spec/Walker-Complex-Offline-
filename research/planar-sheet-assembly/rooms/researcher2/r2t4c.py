# R2-T4 P5 alone (t=0..3 suffices: for t>=chi(G)-1=4, chi(A^(t))=t+1 by Thm A)
import networkx as nx, time
from r2t4 import build, glue, chi
C5=nx.cycle_graph(5); C5s=nx.Graph([(i,(i+2)%5) for i in range(5)])
W4=nx.wheel_graph(5)
m_w=([W4,nx.Graph([(0,1)]),nx.Graph([(0,1)])],[[(0,1),(1,0)],[(0,3),(1,1)],[(0,2),(2,0)],[(0,4),(2,1)]])
m_c=([C5,C5s],[[(0,i),(1,i)] for i in range(5)])
cls=[[(0,i)] for i in range(5)]
for j in range(5):
    a,b=j,(j+2)%5; cls[a].append((1+j,0)); cls[b].append((1+j,1))
m_k=([C5]+[nx.Graph([(0,1)]) for _ in range(5)],cls)
for name,m in (('C5+C5*',m_c),('W4+2K2',m_w),('C5+5K2',m_k)):
    G=glue(*m); print(name,'G~K5',nx.is_isomorphic(G,nx.complete_graph(5)),'max chi(P)',max(chi(P) for P in m[0]),flush=True)
    for t in range(4):
        t0=time.time(); c=chi(build(*m,t)); print(f'   t={t}: chi(A^(t))={c}, d={c-t-1} ({time.time()-t0:.1f}s)',flush=True)
