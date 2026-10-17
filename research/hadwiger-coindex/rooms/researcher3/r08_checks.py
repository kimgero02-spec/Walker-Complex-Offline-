# R08 researcher3 (algebraic topology lens). Uses r06_lib (own room). Pure python.
import sys, itertools
sys.path.insert(0, "/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher3")
from r06_lib import make, B0_empty, reduced_betti, popc

def graph(name):
    if name == "C5":  n=5; E=[(i,(i+1)%5) for i in range(5)]
    elif name == "K5": n=5; E=list(itertools.combinations(range(5),2))
    elif name == "K6": n=6; E=list(itertools.combinations(range(6),2))
    elif name == "K33": n=6; E=[(a,b) for a in range(3) for b in range(3,6)]
    elif name == "C5K2":  # C5[K2]: blow up each vertex into K2 (no loops), adjacent blobs fully joined
        n=10; E=[]
        for i in range(5):
            E.append((2*i,2*i+1))
            for j in [(i+1)%5]:
                for a in (2*i,2*i+1):
                    for b in (2*j,2*j+1): E.append((min(a,b),max(a,b)))
    return n, E

def B0_info(n, E):
    adj = make(n, E)
    F = B0_empty(adj, n)
    # Euler char of reduced complex: sum (-1)^k n_k over k>=-1 incl empty face
    chi_red = sum(((-1)**k)*len(F[k]) for k in F)  # F includes dim -1? we skip empty tuple below
    # reduced Euler char = sum_{k>=-1} (-1)^k f_k ; B0_empty excludes empty tuple? check
    betti = reduced_betti(F)
    # free check: swap i <-> n+i must fix no nonempty face
    fixed = 0
    for k in F:
        for f in F[k]:
            if not f: continue
            sw = tuple(sorted((x+n) % (2*n) for x in f))
            if sw == f: fixed += 1
    return F, betti, fixed

if __name__ == "__main__":
    for name in ["C5","K5","K6","K33","C5K2"]:
        n,E = graph(name)
        F, betti, fixed = B0_info(n,E)
        nf = {k: len(F[k]) for k in sorted(F)}
        chi = sum(((-1)**k)*v for k,v in nf.items())  # unreduced chi = sum_{k>=0}(-1)^k f_k
        print(name, "edges", len(E), "faces by dim", nf, "chi", chi, "chi even", chi%2==0,
              "fixed nonempty faces", fixed, "reduced betti", {k:v for k,v in betti.items() if v})
