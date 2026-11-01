import itertools, sys, time
from b0 import simplices
import networkx as nx
def circ(n,ks):
    G=nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for k in ks: G.add_edge(i,(i+k)%n)
    return G
def snf_info(rows, ncols):
    """rows: list of dict col->int. returns (rank, list of elementary divisors >1 after unit-pivot elimination + sympy residual)"""
    rows=[dict(r) for r in rows if r]
    colidx={}
    rank=0
    # unit-pivot elimination
    changed=True
    active=rows
    while True:
        # build column->rows index
        cols={}
        for ri,r in enumerate(active):
            for c in r: cols.setdefault(c,set()).add(ri)
        piv=None
        for ri,r in enumerate(active):
            for c,v in r.items():
                if v in (1,-1): piv=(ri,c,v);break
            if piv: break
        if not piv: break
        ri,c,v=piv
        prow=active[ri]
        for rj in list(cols.get(c,())):
            if rj==ri: continue
            r=active[rj]; f=r[c]*v  # since v=+-1, v^-1=v
            for cc,vv in prow.items():
                nv=r.get(cc,0)-f*vv
                if nv: r[cc]=nv
                else: r.pop(cc,None)
        active[ri]={}   # remove pivot row; column c now only in pivot row -> removed
        # column c eliminated implicitly (only pivot row had it)
        rank+=1
        active=[r for r in active if r]
        if not active: break
    divs=[]
    if active:
        import sympy
        from sympy.matrices.normalforms import smith_normal_form
        cs=sorted({c for r in active for c in r}); ci={c:i for i,c in enumerate(cs)}
        M=sympy.zeros(len(active),len(cs))
        for i,r in enumerate(active):
            for c,v in r.items(): M[i,ci[c]]=v
        D=smith_normal_form(M,domain=sympy.ZZ)
        for i in range(min(D.shape)):
            d=abs(D[i,i])
            if d!=0:
                rank+=1
                if d!=1: divs.append(int(d))
    return rank,divs
def homology(G,maxd):
    S,n=simplices(G)
    def verts(A,B): return [i for i in range(n) if A>>i&1]+[n+i for i in range(n) if B>>i&1]
    bydim={}
    for A,B in S:
        vs=tuple(verts(A,B)); bydim.setdefault(len(vs)-1,[]).append(vs)
    idx={d:{f:i for i,f in enumerate(sorted(L))} for d,L in bydim.items()}
    res={}
    ranks={}
    for d in range(1,maxd+2):
        rows=[]
        for f in idx[d]:
            r={}
            for t in range(len(f)):
                g=f[:t]+f[t+1:]
                r[idx[d-1][g]]=(-1)**t
            rows.append(r)
        t0=time.time()
        ranks[d]=snf_info(rows,len(idx[d-1]))
        print('  boundary',d,'rank',ranks[d][0],'torsion divisors',ranks[d][1],round(time.time()-t0,1),flush=True)
    for d in range(0,maxd+1):
        nd=len(idx[d]); rk_d=ranks[d][0] if d>=1 else 0
        betti=nd-rk_d-ranks[d+1][0]
        if d==0: betti-=1
        tors=ranks[d+1][1]
        res[d]=(betti,tors)
    return res
if __name__=="__main__":
    n=int(sys.argv[1]); ks=tuple(int(x) for x in sys.argv[2].split(',')); maxd=int(sys.argv[3])
    print(n,ks,homology(circ(n,ks),maxd))
