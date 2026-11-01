import random, itertools, numpy as np, networkx as nx
from r03_conv import runs, Qd_search
from radon import max_pairs
from r04_lib import *
# (a) offsets K1,K2,K3 via the Q_d solver
for n in (2,3,4):
    G=nx.complete_graph(n); print("K%d"%n,[(d,bool(Qd_search(G,d))) for d in range(1,n)])
# (b) reduction check: pair condition <=> all bicliques <=4 runs, on planar triangulations, random orders
random.seed(7); agree=dis=0
for trial in range(120):
    G=nx.convert_node_labels_to_integers(stacked(trial,9) if trial%2 else hubflips(stacked(trial,9),200,trial))
    o=list(G.nodes()); random.shuffle(o)
    # try to make orders near-valid half the time: take SAT order and perturb
    if trial%3==0:
        so,_=solve(G); o=list(so); i,j=random.sample(range(len(o)),2); o[i],o[j]=o[j],o[i]
    pos={v:i for i,v in enumerate(o)}
    full=all(runs(pos,A,B)<=4 for A,B in max_pairs(G) if A and B)
    pr=(nviol(G,o)==0)
    agree+=(full==pr); dis+=(full!=pr)
print("reduction agree",agree,"disagree",dis)
# (c) W5 angular lemma: (2)&(3) at i  =>  c_i not angularly between c_{i-1},c_{i+1} seen from h
def seg_inter(p,q,r,s):
    def o(a,b,c): return np.sign((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))
    return o(p,q,r)!=o(p,q,s) and o(r,s,p)!=o(r,s,q)
def in_tri(x,a,b,c):
    def o(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
    s=[o(a,b,x),o(b,c,x),o(c,a,x)]; return all(t>0 for t in s) or all(t<0 for t in s)
rng=np.random.default_rng(0); cnt=0; viol=0
for _ in range(100000):
    h,a,m,b=rng.standard_normal((4,2))   # h, c_{i-1}, c_i, c_{i+1}
    ang=lambda p:np.arctan2(p[1]-h[1],p[0]-h[0])
    # between (angularly, within <pi): m's direction inside the cone of a,b
    cr=lambda u,v:u[0]*v[1]-u[1]*v[0]
    A,M,B=a-h,m-h,b-h
    between = cr(A,M)*cr(A,B)>0 and cr(M,B)*cr(A,B)>0
    ok2=not seg_inter(h,m,a,b); ok3=not in_tri(m,h,a,b)
    if ok2 and ok3:
        cnt+=1
        if between: viol+=1
print("W5 lemma: samples with (2)&(3):",cnt,"of which angularly between:",viol)
