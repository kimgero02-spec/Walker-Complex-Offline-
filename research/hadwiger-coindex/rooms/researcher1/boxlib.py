"""researcher1: 박스 복합체 B_0(G), B(G), 호몰로지, pi1(Tietze), SW 높이, Hadwiger 수."""
import itertools, networkx as nx

# ---------- 박스 복합체 ----------
def adjmasks(G):
    nodes = sorted(G.nodes()); idx = {v:i for i,v in enumerate(nodes)}
    n = len(nodes); adj=[0]*n
    for u,v in G.edges():
        adj[idx[u]] |= 1<<idx[v]; adj[idx[v]] |= 1<<idx[u]
    return n, adj

def CN(adj, n, A):
    r = (1<<n)-1
    i=0
    while A:
        if A&1: r &= adj[i]
        A >>= 1; i+=1
    return r

def submasks(m):
    s=m
    while True:
        yield s
        if s==0: break
        s=(s-1)&m

def B0_simplices(G):
    """B_0: (A,B), A x B subset E. 반환: 정점이 비트 (A | B<<n) 인 마스크들(공집합 제외)."""
    n, adj = adjmasks(G)
    out=[]
    for A in range(1<<n):
        for B in submasks(CN(adj,n,A)):
            if A|B: out.append(A | (B<<n))
    return n, out

def B_simplices(G):
    """B(G): CN(A)!=empty, CN(B)!=empty (공집합의 CN = V)."""
    n, adj = adjmasks(G)
    out=[]
    for A in range(1<<n):
        cA = CN(adj,n,A)
        if cA==0: continue
        for B in submasks(cA):
            if A|B and CN(adj,n,B)!=0: out.append(A|(B<<n))
    return n, out

def bits(m):
    i=0
    while m:
        if m&1: yield i
        m>>=1; i+=1

# ---------- 호몰로지 (mod p) ----------
def rank_modp(rows, p):
    """rows: list of dict col->val. 희소 가우스 소거."""
    piv={}
    r=0
    for row in rows:
        row=dict(row)
        while row:
            c=min(row)
            if c in piv:
                pr=piv[c]; f=row[c]*pow(pr[c],-1,p)%p
                for k,v in pr.items():
                    nv=(row.get(k,0)-f*v)%p
                    if nv: row[k]=nv
                    else: row.pop(k,None)
            else:
                piv[c]=row; r+=1; break
    return r

def reduced_betti(simps, p):
    """simps: 정점 비트마스크 리스트(공집합 제외, 폐포 닫힘 가정). 환원 호몰로지 Betti 수 (p 체), 차원 -1..dim"""
    by={}
    for m in simps:
        by.setdefault(bin(m).count('1')-1,[]).append(m)
    by[-1]=[0]
    maxd=max(by)
    index={d:{m:i for i,m in enumerate(sorted(by[d]))} for d in by}
    ranks={}
    for d in range(0,maxd+1):
        rows=[]
        for m in by[d]:
            vs=list(bits(m)); row={}
            for j,v in enumerate(vs):
                f=m & ~(1<<v)
                row[index[d-1][f]] = (1 if j%2==0 else p-1)%p
            rows.append(row)
        ranks[d]=rank_modp(rows,p)
    ranks[maxd+1]=0; ranks[-1]=0
    return {d: len(by[d])-ranks[d]-ranks[d+1] for d in range(-1,maxd+1)}, maxd

def hconn(simps, ps=(2,3,32003)):
    """호몰로지 연결도: 최대 k (환원 호몰로지 H_i=0, i<=k). 반환 (k, dim)."""
    best=None
    allb={}
    for p in ps:
        b,maxd=reduced_betti(simps,p); allb[p]=b
    k=-2
    for d in range(-1,maxd+1):
        if all(allb[p][d]==0 for p in ps): k=d
        else: break
    else:
        k=maxd  # 전부 0 -> contractible-ish
    return k, maxd, allb

# ---------- pi1 (Tietze 단순화) ----------
def simply_connected(simps, cap=400):
    """True=증명됨(트리 + Tietze), False=연결 안 됨, None=판정 불가."""
    verts=sorted({v for m in simps for v in bits(m)})
    edges=[tuple(bits(m)) for m in simps if bin(m).count('1')==2]
    tris=[tuple(bits(m)) for m in simps if bin(m).count('1')==3]
    if not verts: return False
    G=nx.Graph(); G.add_nodes_from(verts); G.add_edges_from(edges)
    if not nx.is_connected(G): return False
    T=nx.minimum_spanning_tree(G)
    tree={frozenset(e) for e in T.edges()}
    gen={}
    for e in edges:
        if frozenset(e) not in tree: gen[e]=len(gen)+1
    def w(a,b):
        if a<b:
            return [gen[(a,b)]] if (a,b) in gen else []
        return [-gen[(b,a)]] if (b,a) in gen else []
    def inv(x): return [-g for g in reversed(x)]
    rels=set()
    def norm(r):
        st=[]
        for g in r:
            if st and st[-1]==-g: st.pop()
            else: st.append(g)
        while len(st)>=2 and st[0]==-st[-1]: st=st[1:-1]
        return st
    for a,b,c in tris:
        r=norm(w(a,b)+w(b,c)+inv(w(a,c)))
        if r: rels.add(tuple(r))
    rels=[list(r) for r in rels]
    gens=set(gen.values())
    changed=True
    while changed and gens:
        changed=False
        rels=[r for r in rels if r]
        # 길이1
        rels.sort(key=len)
        for r in rels:
            if not r: continue
            # 한 번만 나타나는 생성원 찾기
            cnt={}
            for g in r: cnt[abs(g)]=cnt.get(abs(g),0)+1
            sing=[g for g,c in cnt.items() if c==1]
            if not sing: continue
            g=sing[0]
            i=[abs(x) for x in r].index(g)
            # r = X g^s Y  => g^s = X^-1 Y^-1 ... 순환: g^s = (Y X)^-1
            s=1 if r[i]>0 else -1
            Y_X=r[i+1:]+r[:i]
            rep=inv(Y_X)  # g^s = rep
            val = rep if s==1 else inv(rep)  # g = val
            newrels=[]
            for q in rels:
                if q is r: continue
                nq=[]
                for x in q:
                    if abs(x)==g: nq += (val if x>0 else inv(val))
                    else: nq.append(x)
                nq=norm(nq)
                if len(nq)>cap: return None
                if nq: newrels.append(nq)
            rels=newrels; gens.discard(g); changed=True
            break
    return len(gens)==0

def certified_conn(simps):
    """보증된 연결도 하한 k: (k-connected). 반환 (k, hk, sc) ; k=-1 이면 비어있지 않음만."""
    hk, maxd, allb = hconn(simps)
    if hk>=maxd: return maxd, hk, True, allb   # 호몰로지 자명 -> (아래 주석 참고)
    sc = simply_connected(simps) if hk>=1 else None
    if hk<=0: return hk, hk, sc, allb
    if sc: return hk, hk, sc, allb
    return 0, hk, sc, allb   # pi1 미확인 -> 0-연결(연결)만 보증

# ---------- 최대 완전 마이너 ----------
def clique_number(G):
    return max((len(c) for c in nx.find_cliques(G)), default=0)

def hadwiger_number(G, target=None, maxnodes=40000):
    """수축 탐색으로 h(G). 반환 (h, exact). 반복 수축 + 동형 중복 제거."""
    G=nx.convert_node_labels_to_integers(nx.Graph(G))
    best=clique_number(G)
    if target and best>=target: return best, True
    level=[G]
    seen=0
    while level:
        buckets={}
        nxt=[]
        for H in level:
            for u,v in list(H.edges()):
                K=nx.contracted_nodes(H,u,v,self_loops=False)
                K=nx.Graph(K)
                K=nx.convert_node_labels_to_integers(K)
                m=K.number_of_nodes()
                if m<=best: continue
                key=(m,K.number_of_edges(),tuple(sorted(d for _,d in K.degree())))
                lst=buckets.setdefault(key,[])
                if any(nx.faster_could_be_isomorphic(K,L) and nx.is_isomorphic(K,L) for L in lst): continue
                lst.append(K); nxt.append(K)
                c=clique_number(K)
                if c>best:
                    best=c
                    if target and best>=target: return best, True
                seen+=1
                if seen>maxnodes: return best, False
        level=[K for K in nxt if K.number_of_nodes()>best]
    return best, True

# ---------- 포셋 모델 + SW 높이 ----------
def poset_Hom(G):
    """P(G) = {(A,B): A,B 비공집합, A x B subset E} 포함순."""
    n, adj = adjmasks(G)
    el=[]
    for A in range(1,1<<n):
        for B in submasks(CN(adj,n,A)):
            if B: el.append((A,B))
    return n, el

def sw_height(G, join=True, maxchains=400000, verbose=False):
    """포셋 모델의 (선택적으로 S^0과 join한) 자유 Z2 공간의 Stiefel-Whitney 높이 h = max k : w1^k != 0.
    join=True: B_0(G) ~ B(G)*S^0 (Csorba, [기억-미검증]) 모델. coind <= h <= ind."""
    n, el = poset_Hom(G)
    # 원소: ('p',0),('p',1) 극 + (A,B)
    elems=[('e',a,b) for a,b in el]
    if join: elems=[('p',0,0),('p',1,0)]+elems
    ids={e:i for i,e in enumerate(elems)}
    def g(e):
        if e[0]=='p': return ('p',1-e[1],0)
        return ('e',e[2],e[1])
    gi=[ids[g(e)] for e in elems]
    N=len(elems)
    less=[[] for _ in range(N)]  # less[i] = j with elems[j] > elems[i]
    for i,e in enumerate(elems):
        for j,f in enumerate(elems):
            if i==j: continue
            if e[0]=='p':
                if f[0]=='e': less[i].append(j)
            elif f[0]=='e':
                if e[1]&f[1]==e[1] and e[2]&f[2]==e[2]: less[i].append(j)
    # 정점 궤도 대표
    rep=[min(i,gi[i]) for i in range(N)]
    eps=[0 if rep[i]==i else 1 for i in range(N)]
    # 사슬 열거 (궤도 대표 사슬 = min(chain, g chain) 사전식)
    chains={0:set()}
    cur=[(i,) for i in range(N)]
    allc={0:cur}
    d=0
    total=len(cur)
    while cur:
        nxt=[]
        for c in cur:
            for j in less[c[-1]]:
                nxt.append(c+(j,))
        total+=len(nxt)
        if total>maxchains: return None
        if nxt: d+=1; allc[d]=nxt
        cur=nxt
    dim=d
    def canon(c):
        gc=tuple(gi[x] for x in c)
        return min(c,gc)
    orb={}
    for dd,L in allc.items():
        orb[dd]=sorted({canon(c) for c in L})
    oidx={dd:{c:i for i,c in enumerate(L)} for dd,L in orb.items()}
    def wedge(a,b): return (eps[a]+eps[b])%2
    h=0
    for k in range(1,dim+1):
        # w^k 코체인
        wk=0
        vec=set()
        for i,c in enumerate(orb[k]):
            ok=all(wedge(c[t],c[t+1]) for t in range(k))
            if ok: vec.add(i)
        # 코경계: 각 (k-1)-궤도 단체 tau 에 대해 delta(e_tau) = sum of k-simplices having tau as face
        rows={}
        for i,c in enumerate(orb[k]):
            for t in range(k+1):
                f=c[:t]+c[t+1:]
                fc=oidx[k-1][canon(f)]
                rows.setdefault(fc,set()).symmetric_difference_update({i})
        # GF(2) 소거: 정수 비트셋
        def toint(s):
            x=0
            for i in s: x|=1<<i
            return x
        piv={}
        for r in rows.values():
            x=toint(r)
            while x:
                hb=x.bit_length()-1
                if hb in piv: x^=piv[hb]
                else: piv[hb]=x; break
        x=toint(vec)
        while x:
            hb=x.bit_length()-1
            if hb in piv: x^=piv[hb]
            else: break
        if x==0: break   # w^k 는 코바운더리 -> 0 류
        h=k
    return h, dim, len(orb[0]), sum(len(v) for v in orb.values())
