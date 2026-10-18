"""K_8 배치를 이분 교차 그래프 유지하며 교차 차수를 줄이는 언덕 오르기 (구성용)."""
import itertools, random, sys
from line_search import crossing_graph, pareto, orient
from k8_climb import climb
n=8; edges=list(itertools.combinations(range(n),2))
def score(pts):
    P=pareto(crossing_graph(pts,edges))
    if P is None: return None
    return min((min(p),max(p)) for p in P), P
def gp(pts):
    return all(orient(*[pts[i] for i in t])!=0 for t in itertools.combinations(range(n),3))
best_overall=None
for seed in range(int(sys.argv[1])):
    rnd=random.Random(100+seed)
    pts=climb(n,seed)
    if pts is None: continue
    cur=score(pts)
    for s in range(3000):
        i=rnd.randrange(n); old=pts[i]
        pts[i]=(old[0]+rnd.gauss(0,0.05),old[1]+rnd.gauss(0,0.05))
        sc=score(pts)
        if sc is not None and sc[0]<=cur[0]: cur=sc
        else: pts[i]=old
    ip=[(round(x*1000),round(y*1000)) for x,y in pts]
    sc=score(ip)
    if sc and gp(ip):
        print(seed, sc[0], sorted(sc[1]), ip, flush=True)
        if best_overall is None or sc[0]<best_overall[0]: best_overall=(sc[0],ip)
print("best",best_overall)
