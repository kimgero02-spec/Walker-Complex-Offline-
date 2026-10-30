import itertools
# manual graph of decomposition: pieces = list of (vertexset, edgeset) ; G implicit
def manual(pieces):
    V=set()
    for Vp,Ep in pieces: V|=set(Vp)
    copies=[('c',v,k) for k,(Vp,Ep) in enumerate(pieces) for v in Vp]
    F={v:[x for x in copies if x[1]==v] for v in V}
    whites=[('w',v) for v in V if len(F[v])>=2]
    E=set()
    for k,(Vp,Ep) in enumerate(pieces):
        for (a,b) in Ep: E.add(frozenset([('c',a,k),('c',b,k)]))
    for w in whites:
        for x in F[w[1]]: E.add(frozenset([x,w]))
    mu=lambda a,b: sum(1 for Vp,Ep in pieces if (a,b) in Ep or (b,a) in Ep)
    for w1,w2 in itertools.combinations(whites,2):
        if mu(w1[1],w2[1])>=2: E.add(frozenset([w1,w2]))
    rho=lambda x: x[1]
    nodes=copies+whites
    return dict(nodes=nodes,E=E,rho=rho,F=F,whites=whites)
def rg_maps_over(Mp,M,sigma_copy):
    # all rho-compatible RG maps Mp->M with copies (v,j)->(v,sigma(j,v)) fixed by sigma_copy; whites free
    fixed={}
    for x in Mp['nodes']:
        if x[0]=='c': fixed[x]=('c',x[1],sigma_copy[(x[1],x[2])]) if sigma_copy[(x[1],x[2])] is not None else None
    free=[w for w in Mp['nodes'] if w[0]=='w']
    cand={w:[y for y in M['nodes'] if M['rho'](y)==w[1]] for w in free}
    res=[]
    for choice in itertools.product(*[cand[w] for w in free]):
        f=dict(fixed); f.update(dict(zip(free,choice)))
        ok=True
        for x in Mp['nodes']:
            if x[0]=='c' and f[x]!=('c',x[1],sigma_copy[(x[1],x[2])]): ok=False;break
        if not ok: continue
        for e in Mp['E']:
            a,b=tuple(e)
            fa,fb=f[a],f[b]
            if fa!=fb and frozenset([fa,fb]) not in M['E']: ok=False;break
        if ok: res.append(f)
    return res
def L(Dp,D,sig):
    Mp=manual(Dp); M=manual(D)
    sc={}
    for j,(Vp,Ep) in enumerate(Dp):
        for v in Vp: sc[(v,j)]=sig[j]
    return Mp,M,rg_maps_over(Mp,M,sc)
