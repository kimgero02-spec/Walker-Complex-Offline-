# R12 망상꾼 (재개): 매장 이전 정리 확인 (절단 파노의 토러스 매장) 과 코xeter형 M° 의 종수 상계 탐색
import itertools, random, networkx as nx
from r11_levi import manual
def faces(rot):
    # rot: dict v -> cyclic list of neighbours. face tracing: (u,v) -> (v, succ_v(u))
    darts={(u,v) for u in rot for v in rot[u]}; seen=set(); F=[]
    for d in darts:
        if d in seen: continue
        f=[]; x=d
        while x not in seen:
            seen.add(x); f.append(x); u,v=x; L=rot[v]; x=(v,L[(L.index(u)+1)%len(L)])
        F.append(f)
    return F
def genus(rot):
    V=len(rot); E=sum(len(l) for l in rot.values())//2; F=len(faces(rot)); return (2-V+E-F)//2, F
# 1) K7 토러스 매장 [기억-미검증 회전: 차 1,3,2,6,4,5]
rot={i:[(i+d)%7 for d in (1,3,2,6,4,5)] for i in range(7)}
g,F=genus(rot); FF=faces(rot); print('K7 genus',g,'faces',F,'lengths',sorted(len(f) for f in FF))
# 면 2-색칠: 면 쌍대 그래프의 이분성
fid={}
for i,f in enumerate(FF):
    for d in f: fid[d]=i
Dual=nx.Graph()
for (u,v),i in fid.items(): Dual.add_edge(i,fid[(v,u)])
print('dual bipartite',nx.is_bipartite(Dual))
col=nx.bipartite.color(Dual)
black=[sorted({d[0] for d in FF[i]}) for i in range(len(FF)) if col[i]==0]
print('black triangles',black)
# 2) 절단: 꼭짓점 v 의 원판, 검정 삼각형 T 마다 복사 (v,T). 매장 이전 구성의 회전계
tri={i:FF[i] for i in range(len(FF)) if col[i]==0}
R={}
for v in range(7):
    # v 주위의 면 순서: dart (v,x) 다음 면들. 검정 면이 나오는 순서대로 복사점
    order=[]
    for x in rot[v]:
        i=fid[(v,x)]
        if col[i]==0 and i not in order: order.append(i)
    R[('w',v)]=[(v,i) for i in order]
    for i in order:
        f=tri[i]; k=[d[0] for d in f].index(v); nxt=f[k][1]; prv=f[(k-1)%3][0]
        # 원래 회전에서 v 의 이웃 순서 prv?nxt 를 따름; 흰 점은 두 이웃 사이 (원판 쪽)
        L=rot[v]; a,b=(nxt,prv)
        # 회전에서 a 다음에 b 가 오도록 하고 그 사이 각에 흰 점 (원판 중심 방향은 검정 면의 반대쪽)
        R[(v,i)]=[(a,i),(b,i),('w',v)] if L[(L.index(a)+1)%6]!=b else [(a,i),('w',v),(b,i)]
X=nx.Graph([(u,x) for u in R for x in R[u]])
pieces=[(sorted({d[0] for d in tri[i]}),[(d[0],d[1]) for d in tri[i]]) for i in tri]
Mo,_,_,_=manual(pieces)
print('constructed graph iso truncated Fano-type M°:',nx.is_isomorphic(X,nx.Graph(Mo)),' genus of rotation',genus(R))
# 시험 삼아 뒤집은 선택도
R2={k:(v if k[0]=='w' else [v[0],v[2],v[1]]) for k,v in R.items()}; print('alt rotation genus',genus(R2))
# 3) 코xeter형 M°: 3-정칙이므로 회전 = 꼭짓점마다 2 가지. 면 수 최대화 국소탐색 (상계만 줌)
hc=[(list(range(7)),[(i,(i+s)%7) for i in range(7)]) for s in (1,2,3)]
Mo,_,_,_=manual(hc); Y=nx.convert_node_labels_to_integers(Mo)
rnd=random.Random(5); best=None
for rep in range(30):
    rr={v:list(Y[v]) for v in Y}
    for v in rr: rnd.shuffle(rr[v])
    cur=len(faces(rr)); T=2.0
    for it in range(6000):
        v=rnd.choice(list(rr)); rr[v]=[rr[v][0],rr[v][2],rr[v][1]]; nf=len(faces(rr))
        if nf>=cur or rnd.random()<pow(2.718,(nf-cur)/T): cur=nf
        else: rr[v]=[rr[v][0],rr[v][2],rr[v][1]]
        T=max(0.05,T*0.999)
    g=(2-28+42-cur)//2
    if best is None or g<best: best=g; print('Coxeter-type: faces',cur,'genus <=',g,flush=True)
print('Coxeter-type girth 7 => F<=12 => genus>=2; best upper bound found',best)
