# R17 researcher3: F_2 homology of the free quotient X/Z2 via orbit chains (free cellular action, swap i<->i+n).
import sys, io, contextlib
sys.path.insert(0, ".")
from r06_lib import make, B0_empty
with contextlib.redirect_stdout(io.StringIO()):
    from r08_checks import graph

def rank2(rows):
    piv = {}
    r = 0
    for row in rows:
        v = set(row)
        while v:
            c = max(v)
            if c in piv:
                v ^= piv[c]
            else:
                piv[c] = v; r += 1; break
    return r

def quotient_betti(n, E):
    F = B0_empty(make(n, E), n)
    faces = [f for k in F for f in F[k] if f]
    def orb(f):
        g = tuple(sorted((x + n) % (2*n) for x in f))
        return min(f, g)
    orbits = {}
    for f in faces:
        orbits.setdefault(len(f)-1, set()).add(orb(f))
    dims = sorted(orbits)
    idx = {d: {o: i for i, o in enumerate(sorted(orbits[d]))} for d in dims}
    ranks = {}
    for d in dims:
        if d-1 not in idx:
            ranks[d] = 0; continue
        rows = []
        for o in sorted(orbits[d]):
            row = []
            for j in range(len(o)):
                g = o[:j] + o[j+1:]
                if not g: continue  # augmentation ignored (reduced homology)
                row.append(idx[d-1][orb(g)])
            # mod 2 cancel duplicates
            cnt = {}
            for c in row: cnt[c] = cnt.get(c, 0) ^ 1
            rows.append([c for c, v in cnt.items() if v])
        ranks[d] = rank2(rows)
    betti = {}
    for d in dims:
        betti[d] = len(idx[d]) - ranks[d] - ranks.get(d+1, 0)
    return {d: b for d, b in betti.items() if b}

if __name__ == "__main__":
    for name in ["K5", "K6", "C5K2"]:
        n, E = graph(name)
        print(name, "H_*(X/Z2;F2) reduced:", quotient_betti(n, E))
