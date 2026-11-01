# F-R2 researcher2: b>=2 골격 T = 사이클 b 개 + 완전매칭 의 평면성 Z2 판정 (정리 F2) 확인
import networkx as nx, itertools

def build_T(cycles, chords):
    T=nx.Graph()
    for C in cycles: nx.add_cycle(T,C)
    T.add_edges_from(chords); return T

def setup(cycles, chords):
    cyc_of={v:i for i,C in enumerate(cycles) for v in C}
    partner={}
    for idx,(p,q) in enumerate(chords): partner[p]=(q,idx); partner[q]=(p,idx)
    Q=nx.MultiGraph(); Q.add_nodes_from(range(len(cycles)))
    for idx,(p,q) in enumerate(chords):
        if cyc_of[p]!=cyc_of[q]: Q.add_edge(cyc_of[p],cyc_of[q],idx=idx)
    assert nx.is_connected(Q)
    F=set(); seen={0}; st=[0]
    while st:
        x=st.pop()
        for _,y,d in Q.edges(x,data=True):
            if y not in seen: seen.add(y); F.add(d['idx']); st.append(y)
    return cyc_of,partner,F

def walk(cycles, chords, F, sigma):
    """boundary of disk-band tree; returns cyclic list of chord labels (non-tree chord idx, or ('t',idx))."""
    cyc_of,partner,_=setup(cycles,chords)
    pos={v:(i,k) for i,C in enumerate(cycles) for k,v in enumerate(C)}
    def step(v,d):
        i,k=pos[v]; C=cycles[i]; return C[(k+d)%len(C)]
    seq=[]; start=cycles[0][0]
    # start at a vertex that is not a tree endpoint
    start=next(v for v in cycles[0] if not (v in partner and partner[v][1] in F))
    v,d=start,1; first=True; guard=0
    while True:
        guard+=1; assert guard<10000
        if v==start and not first: break
        first=False
        if v in partner and partner[v][1] in F:
            q,idx=partner[v]; seq.append(('t',idx))
            d = d if sigma.get(idx,0)==0 else -d
            v=step(q,d); continue
        if v in partner: seq.append(partner[v][1])
        v=step(v,d)
    return seq

def overlap(seq):
    posn={}
    for k,x in enumerate(seq): posn.setdefault(x,[]).append(k)
    labs=list(posn); E=set()
    for a,b in itertools.combinations(labs,2):
        a1,a2=posn[a]; b1,b2=posn[b]
        if (a1<b1<a2)!=(a1<b2<a2): E.add(frozenset((a,b)))
    return labs,E

def bip(labs,E):
    G=nx.Graph(); G.add_nodes_from(labs); G.add_edges_from(tuple(e) for e in E); return nx.is_bipartite(G)

def treepath(cycles,chords,F,idx):
    cyc_of,_,_=setup(cycles,chords)
    Tr=nx.Graph(); Tr.add_nodes_from(range(len(cycles)))
    for e in F: p,q=chords[e]; Tr.add_edge(cyc_of[p],cyc_of[q],idx=e)
    p,q=chords[idx]; path=nx.shortest_path(Tr,cyc_of[p],cyc_of[q])
    return {Tr[a][b]['idx'] for a,b in zip(path,path[1:])}

def solve_gf2(rows, nvars):
    """rows: list of (set_of_vars, rhs). returns True if consistent."""
    piv={}
    for S,r in rows:
        v=0
        for x in S: v|=1<<x
        while v:
            h=v.bit_length()-1
            if h in piv: pv,pr=piv[h]; v^=pv; r^=pr
            else: piv[h]=(v,r); break
        if v==0 and r==1: return False
    return True

def theorem_F2(cycles, chords):
    cyc_of,partner,F=setup(cycles,chords)
    Fl=sorted(F); fi={e:i for i,e in enumerate(Fl)}
    seq0=walk(cycles,chords,F,{})
    labs,E0=overlap(seq0)
    nontree=[i for i in range(len(chords)) if i not in F]
    P={f:treepath(cycles,chords,F,f) for f in nontree}
    # I*: vertices = all chords (tree chords as ('t',e)); edges fixed
    Istar=nx.Graph(); Istar.add_nodes_from(labs)
    for f in nontree:
        for e in P[f]: Istar.add_edge(('t',e),f)
    rows=[]
    for f,g in itertools.combinations(nontree,2):
        common=P[f]&P[g]; ov=1 if frozenset((f,g)) in E0 else 0
        if common: rows.append(({fi[e] for e in common},ov))
        elif ov: Istar.add_edge(f,g)
    c1=nx.is_bipartite(Istar); c2=solve_gf2(rows,len(Fl))
    return c1,c2,len(F),len(rows)

def check(name,cycles,chords):
    T=build_T(cycles,chords); assert all(d==3 for _,d in T.degree())
    pl=nx.check_planarity(T)[0]
    c1,c2,nf,nr=theorem_F2(cycles,chords)
    cyc_of,partner,F=setup(cycles,chords)
    Fl=sorted(F)
    exist=any(bip(*overlap(walk(cycles,chords,F,dict(zip(Fl,s))))) for s in itertools.product([0,1],repeat=len(Fl)))
    print(f"{name}: b={len(cycles)} planar={pl} | exists sigma bip(I_sigma)={exist} | F2: I* bip={c1}, sigma-system solvable={c2} (|F|={nf}, rows={nr}) -> {c1 and c2}")

if __name__=="__main__":
    # prism C3xK2: two triangles + matching
    check("prism", [[0,1,2],[3,4,5]], [(0,3),(1,4),(2,5)])
    check("prism twisted order", [[0,1,2],[3,4,5]], [(0,3),(1,5),(2,4)])
    # V8 = Mobius ladder M8 with 2-factor of two 4-cycles
    check("V8", [[0,1,5,4],[2,3,7,6]], [(1,2),(5,6),(3,4),(7,0)])
    # Petersen: outer 0..4, inner 5..9 pentagram, spokes
    check("Petersen", [[0,1,2,3,4],[5,7,9,6,8]], [(i,i+5) for i in range(5)])
    # cube Q3: two squares + matching straight / one with order reversed
    check("cube", [[0,1,2,3],[4,5,6,7]], [(0,4),(1,5),(2,6),(3,7)])
    check("cube reversed", [[0,1,2,3],[4,5,6,7]], [(0,4),(1,7),(2,6),(3,5)])
    check("square-square cross", [[0,1,2,3],[4,5,6,7]], [(0,4),(1,6),(2,5),(3,7)])
    # three cycles: triangle-prism like chain
    check("3 squares chain", [[0,1,2,3],[4,5,6,7],[8,9,10,11]], [(0,4),(1,5),(2,3),(6,8),(7,9),(10,11)])
    check("3 squares chain crossed", [[0,1,2,3],[4,5,6,7],[8,9,10,11]], [(0,4),(2,5),(1,3),(6,8),(7,9),(10,11)])
