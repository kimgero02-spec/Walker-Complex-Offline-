import itertools, random, sys
from twolayer import analyze
n=int(sys.argv[1]); E=list(itertools.combinations(range(n),2))
P=eval(sys.argv[2]); r=analyze(P,E); best=r[0]; random.seed(int(sys.argv[3]))
for step in range(int(sys.argv[4])):
    Q=list(P); k=random.randrange(n); s=random.choice([0.1,0.02,0.005])
    Q[k]=(Q[k][0]+random.gauss(0,s),Q[k][1]+random.gauss(0,s))
    r=analyze(Q,E)
    if r and (r[0][1],r[0][0],r[2])<=(best[1],best[0],99) : P,best=Q,r[0]
print(best, analyze(P,E)[2]); print([(round(x,4),round(y,4)) for x,y in P])
