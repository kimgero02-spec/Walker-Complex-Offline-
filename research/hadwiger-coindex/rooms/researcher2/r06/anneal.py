# R06 반례꾼: 담금질 탐색으로 R^2 배치 (모든 극대 완전이분쌍 엄격 분리) 를 찾는다. 찾으면 정수 좌표로 정확 검사.
import random, math, sys, time
from graphs import maximal_pairs
from planar_cert import bad_pairs

def anneal(n, adj, R, steps, seed, T0=0.6):
    pairs = maximal_pairs(n, adj)
    rnd = random.Random(seed)
    grid = [(a, b) for a in range(-R, R+1) for b in range(-R, R+1)]
    y = [rnd.choice(grid) for _ in range(n)]
    cur = len(bad_pairs(n, adj, y, pairs)); best = (cur, list(y))
    for s in range(steps):
        T = T0 * (1 - s/steps) + 1e-3
        v = rnd.randrange(n); old = y[v]
        y[v] = rnd.choice(grid)
        c = len(bad_pairs(n, adj, y, pairs))
        if c <= cur or rnd.random() < math.exp(-(c-cur)/T):
            cur = c
            if c < best[0]: best = (c, list(y))
            if c == 0: return 0, list(y)
        else:
            y[v] = old
    return best

if __name__ == '__main__':
    from graphs import mycielski, cycle
    n, adj = mycielski(5, cycle(5)[1])
    t = time.time()
    for seed in range(int(sys.argv[1]), int(sys.argv[2])):
        b = anneal(n, adj, R=int(sys.argv[3]), steps=int(sys.argv[4]), seed=seed)
        print('seed', seed, 'best bad', b[0], b[1] if b[0]==0 else '', 'time %.0f' % (time.time()-t), flush=True)
        if b[0] == 0:
            print('FOUND', b[1]); break
