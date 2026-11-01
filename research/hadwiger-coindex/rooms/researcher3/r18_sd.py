# R18 researcher3: barycentric subdivision of B0(G) (free Z2), orbit cochains, cup product mod 2, test x^3 coboundary.
import sys, io, contextlib, itertools
sys.path.insert(0, ".")
from r06_lib import make, B0_empty
with contextlib.redirect_stdout(io.StringIO()):
    from r08_checks import graph

def setup(n, E):
    F = B0_empty(make(n, E), n)
    faces = sorted([f for k in F for f in F[k] if f], key=lambda f: (len(f), f))
    fid = {f: i for i, f in enumerate(faces)}
    sw = lambda f: tuple(sorted((x + n) % (2*n) for x in f))
    swap = [fid[sw(f)] for f in faces]
    subs = [[fid[s] for s in (faces[i][:j]+faces[i][j+1:] for j in range(len(faces[i]))) if s and s in fid] for i in range(len(faces))]
    # cover: all faces contained in face i (proper), for chains
    up = {}
    for i, f in enumerate(faces):
        up[i] = [j for j, g in enumerate(faces) if len(g) > len(f) and set(f) <= set(g)]
    return faces, swap, subs, up

def chains(n, E, maxlen):
    faces, swap, subs, up = setup(n, E)
    # chains as tuples of face ids, strictly increasing inclusion
    out = {1: [(i,) for i in range(len(faces))]}
    for L in range(2, maxlen+1):
        out[L] = [c + (j,) for c in out[L-1] for j in up[c[-1]]]
    return faces, swap, out

if __name__ == "__main__":
    for name in ["K3", "K4", "C5K2"]:
        if name == "K3":
            n, E = 3, [(0,1),(1,2),(0,2)]
        elif name == "K4":
            n, E = 4, [(a,b) for a in range(4) for b in range(a+1,4)]
        else:
            n, E = graph(name)
        faces, swap, out = chains(n, E, 4)
        print(name, {L: len(out[L]) for L in out})
