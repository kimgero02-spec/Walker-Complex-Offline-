import sys, itertools, time
sys.path.insert(0, '/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher2/r19')
from k4k4 import cross, chi
t = time.time()
for size in range(8, 17):
    cnt = 0; ex = None
    for F in itertools.combinations(cross, size):
        if chi(F) >= 7:
            cnt += 1
            if ex is None: ex = F
    print("size", size, "chi>=7 count", cnt, "time", round(time.time()-t,1), flush=True)
    if cnt:
        print("example", sorted(ex), flush=True)
        break
