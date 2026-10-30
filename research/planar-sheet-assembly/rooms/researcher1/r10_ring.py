# R10 researcher1: symbolic s=2 channel matrices; D_pi table; prism / Mobius ladder closed forms.
import sympy as sp
import itertools
from r10_channels import ALL, rho, P, piece_n, brute_P, dims

q = sp.symbols('q')

def coarser(s, p):   # s >= p : every block of p inside a block of s
    return all((p[i] == p[j]) <= (s[i] == s[j]) for i in range(4) for j in range(4))

def name(p):
    blocks = {}
    for i, b in enumerate(p): blocks.setdefault(b, []).append("x1 x2 y1 y2".split()[i])
    return '|'.join(''.join(b) for b in blocks.values())

def table():
    print('pi | tr triv | tr std | (q-2,2) | (q-2,1,1)')
    for p in ALL:
        n = {s: (1 if coarser(s, p) else 0) for s in ALL}
        t, s, pe, de = rho(q, n)
        print(name(p), '|', sp.factor(sp.Matrix(t).trace()), '|', sp.factor(sp.Matrix(s).trace()), '|', pe, '|', de)

def square_piece(twist):
    # junction x=(u0,v0), y=(u1,v1); rung u0v0 belongs to this piece; sides u0u1, v0v1 (or crossed)
    E = [('u0', 'v0'), ('u0', 'u1'), ('v0', 'v1')] if not twist else [('u0', 'v0'), ('u0', 'v1'), ('v0', 'u1')]
    return E

def sym_rho(E, priv, jx, jy, qs=range(4, 12)):
    # n_pi are polynomials in q (here constants, junction-only); evaluate rho symbolically via interpolation
    vals = {}
    for qq in qs:
        vals[qq] = piece_n(qq, E, priv, jx, jy)
    # junction-only => n_pi independent of q (0/1)
    n = vals[qs[0]]
    return rho(q, n)

if __name__ == '__main__':
    table()
    for tw in (False, True):
        t, s, pe, de = sym_rho(square_piece(tw), [], ('u0', 'v0'), ('u1', 'v1'))
        T = sp.Matrix(t); S = sp.Matrix(s)
        print('twist', tw, 'triv', T, 'eig', {sp.factor(k): v for k, v in T.eigenvals().items()})
        print('   std', S, 'eig', {sp.factor(k): v for k, v in S.eigenvals().items()}, 'per', pe, 'det', de)
    # closed forms for k squares (prism: all straight; Mobius: one twisted)
    tS, sS, pS, dS = [sp.Matrix(a) if i < 2 else a for i, a in enumerate(sym_rho(square_piece(False), [], ('u0', 'v0'), ('u1', 'v1')))]
    tM, sM, pM, dM = [sp.Matrix(a) if i < 2 else a for i, a in enumerate(sym_rho(square_piece(True), [], ('u0', 'v0'), ('u1', 'v1')))]
    for k in (2, 3, 4, 5):
        for tw in (False, True):
            T = tS**(k-1) * (tM if tw else tS); S = sS**(k-1) * (sM if tw else sS)
            pp = pS**(k-1) * (pM if tw else pS); dd = dS**(k-1) * (dM if tw else dS)
            dt, ds, dp, dq = 1, q-1, q*(q-3)/2, (q-1)*(q-2)/2
            Pq = sp.expand(T.trace() + ds*S.trace() + dp*pp + dq*dd)
            # brute check at q=3,4
            V = [f'u{i}' for i in range(k)] + [f'v{i}' for i in range(k)]
            E = []
            for i in range(k):
                j = (i+1) % k
                E.append((f'u{i}', f'v{i}'))
                if tw and i == k-1:
                    E += [(f'u{i}', f'v{j}'), (f'v{i}', f'u{j}')]
                else:
                    E += [(f'u{i}', f'u{j}'), (f'v{i}', f'v{j}')]
            chk = [(qq, Pq.subs(q, qq), brute_P(qq, V, E)) for qq in (2, 3, 4)]
            print('k=%d %s: P = %s ; channels: triv=%s std=(q-1)*(%s) 22=%s 211=%s ; check %s' % (
                k, 'Mobius' if tw else 'prism', sp.factor(Pq), sp.factor(T.trace()), sp.factor(S.trace()),
                sp.factor(dp*pp), sp.factor(dq*dd), chk))
