# R08 researcher3: sigma(x) = -x on Z_n (n odd) acting on B0(K_n) (copy-wise). Fixed set via invariant-face order complex.
import itertools, sys
sys.path.insert(0, ".")
from r08_smith import chains_fixed
from r06_lib import reduced_betti
for n in (3, 5, 7):
    E = list(itertools.combinations(range(n), 2))
    perm = {}
    for x in range(2*n):
        c, v = (0, x) if x < n else (1, x-n)
        perm[x] = ((-v) % n) + c*n
    out, nf = chains_fixed(n, E, perm)
    b = reduced_betti(out)
    print("n", n, "invariant faces", nf, "Fix reduced betti", {k: v for k, v in b.items() if v})
