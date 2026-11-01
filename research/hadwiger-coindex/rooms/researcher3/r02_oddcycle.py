# [계산 확인] d_R <= 1 (R^1 placement) for cycles: 1-D disjointness depends only on the order of values.
import itertools, sys
sys.path.insert(0, ".")
from r02_dR import radon_free
for m in (3, 4, 5, 6):
    E = [(i, (i + 1) % m) for i in range(m)]
    ok = [p for p in itertools.permutations(range(m)) if radon_free(m, E, list(p))[0]]
    print("C%d: orders giving R^1 radon-free placement:" % m, len(ok), "of", len(list(itertools.permutations(range(m)))))
