# R08 researcher3: thickness family check (formula [기억-미검증]: theta(K_n)=floor((n+7)/6), n!=9,10; theta(K_9)=theta(K_10)=3)
import math
def theta_formula(n):
    if n in (9, 10): return 3
    return (n+7)//6
rows=[]
for n in range(4, 41):
    th = theta_formula(n)
    edge_lb = math.ceil(math.comb(n,2)/(3*n-6)) if n>=3 else 1
    ok = th >= edge_lb            # necessary: |E| <= theta*(3n-6)
    rows.append((n, th, edge_lb, ok, 6*th-2, n, n<=6*th-2))
bad = [r for r in rows if not r[3]]
print("edge-count consistency failures:", bad)
print("n, theta, edge-LB, 6theta-2, tau=n, tight?")
for r in rows:
    if r[0] in (4,5,6,8,9,10,11,16,17,22,23,28,34):
        print(r[0], r[1], r[2], r[4], r[5], "TIGHT" if r[5]==r[4] else "", "" if r[5]<=r[4] else "VIOLATES 6k-2")
# edge-sum law test: sheets planar (tau<=4) -> sum + (k-1) bound
for k in range(2,8):
    n = 6*k-2
    th = theta_formula(n)
    print("k",k,"K_%d theta=%d tau=%d  planar-sheet bound sum+(k-1)=%d  refuted=%s" % (n, th, n, 4*th+th-1, n > 4*th+th-1))
