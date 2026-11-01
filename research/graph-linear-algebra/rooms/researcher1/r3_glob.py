import sys
from r3_sel import *
ex = {
 'a': dict(f=[0,0,-2], S=[2,3], gens=[[-1,0,0],[0,1,0],[-1,1,0],[1,1,0]], name="t^3-2 (Y^2=X^3-16)"),
 'b': dict(f=[1,-2,-1], S=[2,7], gens=[[-1,0,0],[0,1,0],[1,1,0],[2,0,0],[-2,1,0]], name="t^3+t^2-2t-1 (cyclic 7)"),
 'c': dict(f=[0,-1,-1], S=[2,23], gens=[[-1,0,0],[0,1,0],[2,0,0],[-6,6,-1],[-4,-5,-3]], name="t^3-t-1 (disc -23)"),
}
if __name__ == "__main__":
    key = sys.argv[1]
    E = ex[key]
    print(E['name'])
    Kmap = {2: 8, 3: 3, 7: 2, 23: 2}
    alg, Hs, rows, info = selmer(E['f'], E['gens'], E['S'], K=None)
    for bits, d, row in rows:
        print(bits, {v: (('eps0' if row[v][0] == 1 else 'eps1'), ('inW' if row[v][1] else 'notW')) for v in row})
    sel = [bits for bits, d, row in rows if all(row[v][1] for v in row)]
    ker = [bits for bits, d, row in rows if all(row[v][0] == 1 for v in row)]
    print("|H(S)| =", len(rows), " #in all ker eps_v =", len(ker), " |Sel2| =", len(sel))
    for v in info: print(" |W_%s| found" % v, len(info[v][1]))
