# R06 researcher3: run the proof of Theorem 2L constructively (own implementation) on
# hand-built planar candidates; report the step that produces the witness.
import itertools, networkx as nx
from r06_qstar import qstar, colorable, all_colorings, rainbow

def proper(G, c): return all(c[u] != c[v] for u, v in G.edges())

def witness_2L(Q, T1, T2, phi):
    """phi: proper 3-coloring with colors 1,2,3. Returns (step, 4-coloring) or (None,None)."""
    T1, T2 = list(T1), list(T2)
    I = set(T1) & set(T2)
    def setto4(Z):
        c = dict(phi)
        for z in Z: c[z] = 4
        return c
    if len(I) == 2: return 'A', setto4(I)
    if len(I) == 1:
        x = I.pop(); u = [v for v in T1 if v != x]; w = [v for v in T2 if v != x]
        for ui in u:
            for wj in w:
                if not Q.has_edge(ui, wj): return 'B1', setto4([x, ui, wj])
        if phi[u[0]] == phi[u[1]]: return 'B2', setto4(w)
        return 'B3', setto4(u)
    # case C
    if not rainbow(phi, T1): return 'N1', setto4(T2[:2])
    if not rainbow(phi, T2): return 'N1', setto4(T1[:2])
    a = {phi[v]: v for v in T1}; b = {phi[v]: v for v in T2}
    for s, t in itertools.combinations([1, 2, 3], 2):
        for p in itertools.combinations([1, 2, 3], 2):
            for q in itertools.combinations([1, 2, 3], 2):
                P = [a[i] for i in p]; R = [b[i] for i in q]
                if not any(Q.has_edge(x, y) for x in P for y in R):
                    return f'N2 p={p} q={q}', setto4(P + R)
        break
    for cc in (1, 2, 3):
        rest = [i for i in (1, 2, 3) if i != cc]
        for s in rest:
            for t in rest:
                Cc = {v for v in Q if phi[v] == cc}
                common = set(Q[a[s]]) & set(Q[b[t]]) & Cc
                if not common:
                    psi = dict(phi); psi[a[s]] = 4; psi[a[cc]] = 4; psi[b[t]] = cc
                    for z in set(Q[b[t]]) & Cc: psi[z] = 4
                    return f'N3 c={cc} s={s} t={t}', psi
    return None, None

def three_coloring(Q):
    c = colorable(Q, 3)
    return {v: k + 1 for v, k in c.items()} if c else None

def report(name, Q, T1, T2, phi=None):
    phi = phi or three_coloring(Q)
    pl = nx.check_planarity(Q)[0]
    step, psi = witness_2L(Q, T1, T2, phi)
    ok = psi is not None and proper(Q, psi) and not rainbow(psi, T1) and not rainbow(psi, T2)
    print(f'{name}: |V|={Q.number_of_nodes()} |E|={Q.number_of_edges()} planar={pl} step={step} witness_ok={ok}')
    if psi: print('    psi =', {k: psi[k] for k in sorted(psi)})
    return step

def H0():
    Q = nx.Graph()
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            if j != i: Q.add_edge(f'a{i}', f'm{j}'); Q.add_edge(f'b{i}', f'm{j}')
    return Q

if __name__ == '__main__':
    T1, T2 = ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3']
    phi = {f'{x}{i}': i for x in 'amb' for i in (1, 2, 3)}
    Qs = qstar()
    report("Q* (control, nonplanar)", Qs, T1, T2, phi)
    for e in [('a1', 'b2'), ('a1', 'm2'), ('m1', 'm2'), ('a1', 'm3')]:
        Q = Qs.copy(); Q.remove_edge(*e); report(f'Q* - {e}', Q, T1, T2, phi)
    Hm = H0(); Hm.add_edges_from([('a1', 'b2'), ('a2', 'b3'), ('a3', 'b1')])
    report('H0 + cyclic matching (no triangle)', Hm, T1, T2, phi)
    H2 = Hm.copy(); H2.remove_edge('a3', 'b1'); H2.add_edges_from([('m1','m2'),('m2','m3'),('m1','m3')])
    report('H0 + triangle + 2 matching edges', H2, T1, T2, phi)
    # planar crossing-number-1 test for Q*: replace a pair of disjoint edges by a crossing vertex
    cr1 = []
    for e, f in itertools.combinations(Qs.edges(), 2):
        if set(e) & set(f): continue
        G = Qs.copy(); G.remove_edge(*e); G.remove_edge(*f)
        for v in e + f: G.add_edge('X', v)
        if nx.check_planarity(G)[0]: cr1.append((e, f))
    print('Q* crossing number 1 drawings (pairs e,f):', len(cr1), cr1[:3])
