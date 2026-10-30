# R08 researcher3: check the refinement criterion for E11 transport on small examples.
# Planarity is not used (the criterion is purely combinatorial); pieces are arbitrary subgraphs.
import itertools, random
from collections import defaultdict

def manual(pieces, V, E):
    # pieces: list of (Vset, Eset). returns (copies, whites, adj) where adj is set of frozenset pairs
    F = {v: [k for k,(Vk,Ek) in enumerate(pieces) if v in Vk] for v in V}
    mu = {e: sum(1 for (Vk,Ek) in pieces if e in Ek) for e in E}
    copies = [(v,k) for v in V for k in F[v]]
    whites = [('w',v) for v in V if len(F[v]) >= 2]
    adj = set()
    for k,(Vk,Ek) in enumerate(pieces):
        for e in Ek:
            u,v = tuple(e)
            adj.add(frozenset({(u,k),(v,k)}))
    for v in V:
        if len(F[v]) >= 2:
            for k in F[v]:
                adj.add(frozenset({(v,k),('w',v)}))
    for e in E:
        u,v = tuple(e)
        if mu[e] >= 2:
            adj.add(frozenset({('w',u),('w',v)}))
    return F, mu, copies, whites, adj

def is_rg(fmap, src_edges, adj):
    for e in src_edges:
        x,y = tuple(e)
        fx,fy = fmap[x], fmap[y]
        if fx != fy and frozenset({fx,fy}) not in adj:
            return False
    return True

def brute_exists(Dp, sigma, D, V, E):
    Fp, mup, copies_p, whites_p, adj_p = manual(Dp, V, E)
    F, mu, copies, whites, adj = manual(D, V, E)
    src_edges = adj_p
    # canonical copy map
    base = {(v,j): (v,sigma[j]) for (v,j) in copies_p}
    # white options: any target over v in M(D)
    wvars = [('w',v) for v in V if len(Fp[v]) >= 2]
    opts = []
    for wv in wvars:
        v = wv[1]
        cand = [(v,k) for k in F[v]] + ([('w',v)] if len(F[v]) >= 2 else [])
        opts.append(cand)
    for choice in itertools.product(*opts):
        fmap = dict(base)
        for wv,c in zip(wvars,choice):
            fmap[wv] = c
        ok = True
        for e in adj_p:
            x,y = tuple(e)
            fx,fy = fmap[x], fmap[y]
            if fx != fy and frozenset({fx,fy}) not in adj:
                ok = False; break
        if ok:
            return True
    return False

def criterion(Dp, sigma, D, V, E):
    Fp, mup, _, _, _ = manual(Dp, V, E)
    F, mu, _, _, _ = manual(D, V, E)
    W = [v for v in V if len(Fp[v]) >= 2]
    pure = {v: len({sigma[j] for j in Fp[v]}) == 1 for v in W}
    Gam = {v: set() for v in W}
    gedges = []
    for e in E:
        if mup[e] >= 2:
            u,v = tuple(e)
            Gam[u].add(v); Gam[v].add(u); gedges.append(e)
    seen = set()
    for s in W:
        if s in seen: continue
        comp, st = set(), [s]
        while st:
            x = st.pop()
            if x in comp: continue
            comp.add(x); st.extend(Gam[x])
        seen |= comp
        allpure = all(pure[v] for v in comp)
        whiteok = all(len(F[v]) >= 2 for v in comp) and all(mu[e] >= 2 for e in gedges if set(tuple(e)) <= comp)
        if not (allpure or whiteok):
            return False
    return True

def rand_case(rng):
    nv = rng.randint(3,5)
    V = list(range(nv))
    allE = [frozenset(p) for p in itertools.combinations(V,2)]
    E = set(e for e in allE if rng.random() < 0.7)
    if not E: return None
    # D: random pieces covering V and E
    while True:
        m = rng.randint(1,3)
        D = []
        for _ in range(m):
            Ek = set(e for e in E if rng.random() < 0.6)
            Vk = set(v for e in Ek for v in e) | set(v for v in V if rng.random() < 0.3)
            D.append((Vk, Ek))
        if set().union(*[Ek for _,Ek in D]) == E and set().union(*[Vk for Vk,_ in D]) == set(V):
            break
    # D': random sub-pieces, each inside some D piece, covering
    while True:
        mp = rng.randint(1,4)
        Dp, sigma = [], []
        for _ in range(mp):
            k = rng.randrange(len(D))
            Vk, Ek = D[k]
            Ej = set(e for e in Ek if rng.random() < 0.7)
            Vj = set(v for e in Ej for v in e) | set(v for v in Vk if rng.random() < 0.3)
            Dp.append((Vj, Ej)); sigma.append(k)
        if set().union(*[Ej for _,Ej in Dp]) == E and set().union(*[Vj for Vj,_ in Dp]) == set(V):
            break
    return V, E, D, Dp, sigma

if __name__ == "__main__":
    # Triangle example: D = three pieces each one edge; D' = each edge twice
    V = ['a','b','c']
    e = lambda x,y: frozenset({x,y})
    E = {e('a','b'), e('b','c'), e('a','c')}
    D = [({'a','b'}, {e('a','b')}), ({'b','c'}, {e('b','c')}), ({'a','c'}, {e('a','c')})]
    Dp = [(set(Vk), set(Ek)) for (Vk,Ek) in D for _ in range(2)]
    sigma = [0,0,1,1,2,2]
    print("triangle: brute", brute_exists(Dp, sigma, D, V, E), "criterion", criterion(Dp, sigma, D, V, E))
    # K2 example (R07 g): D'=(K2,K2) -> D=(K2)
    V2 = ['u','v']; E2 = {e('u','v')}
    D2 = [({'u','v'}, set(E2))]; Dp2 = [({'u','v'}, set(E2)), ({'u','v'}, set(E2))]
    print("K2 merge: brute", brute_exists(Dp2, [0,0], D2, V2, E2), "criterion", criterion(Dp2, [0,0], D2, V2, E2))
    rng = random.Random(8)
    agree = dis = 0; ex_fail = ex_ok = 0
    for _ in range(300):
        c = rand_case(rng)
        if c is None: continue
        V_, E_, D_, Dp_, s_ = c
        b = brute_exists(Dp_, s_, D_, V_, E_)
        cr = criterion(Dp_, s_, D_, V_, E_)
        if b == cr: agree += 1
        else: dis += 1; print("MISMATCH", D_, Dp_, s_, b, cr)
        ex_ok += b; ex_fail += (not b)
    print("random small cases: agree", agree, "disagree", dis, "exists", ex_ok, "not exists", ex_fail)
