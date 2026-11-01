# R2-T4 addendum: single numbers chi(A), chi(H), chi(P_k), chi(P_k\J_k) equal on opponent's (b-2) pair, chi(G) differs
import networkx as nx
from r2t4 import build, glue, H_of, chi, chiG, T11
for ports2,lab in (((4,5,6,7),'rainbow'),((4,8,9,10),'color-0')):
    cls=[[(0,a),(1,b)] for a,b in zip((4,8,9,10),ports2)]
    pcs=[T11(),T11()]
    A=build(pcs,cls,1); H=H_of(pcs,cls)
    inner=[chi(P.subgraph([v for v in P if v not in (p if k==0 else ports2)])) for k,(P,p) in enumerate(zip(pcs,[(4,8,9,10),ports2]))]
    print(f'{lab}: chi(A)={chi(A)}, chi(H)={chi(H)}, chi(P)={[chi(P) for P in pcs]}, chi(P\\J)={inner}, chi(G)={chiG(glue(pcs,cls))}')
