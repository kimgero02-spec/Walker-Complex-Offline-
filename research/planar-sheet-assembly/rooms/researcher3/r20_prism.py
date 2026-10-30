# R20-researcher3: structured search for a frozen planar 3-assignment (A,B,C) with theta(G)=2.
# A = prism C_k x K_2 (u_i outer, v_i inner); B, C = pseudo-double-wheel quadrangulations on U|V.
# Search is only a generator; candidate is certified by verify() (direct planarity checks).
import random, sys
import networkx as nx
def planar(E):
    H=nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]
def prism(k):
    E=[]
    for i in range(k):
        E+= [(('u',i),('u',(i+1)%k)), (('v',i),('v',(i+1)%k)), (('u',i),('v',i))]
    return E
def pdw(m):  # pseudo double wheel: cycle c0..c_{2m-1}, hub a~odd, hub b~even
    E=[(('c',i),('c',(i+1)%(2*m))) for i in range(2*m)]
    E+=[('a',('c',i)) for i in range(1,2*m,2)]+[('b',('c',i)) for i in range(0,2*m,2)]
    U=['b']+[('c',i) for i in range(0,2*m,2)]  # side 1
    W=['a']+[('c',i) for i in range(1,2*m,2)]  # side 2
    return E,U,W
def norm(e): return tuple(sorted(e))
def rand_label(k, rng):
    m=k-1; E,U,W=pdw(m)
    pu=list(range(k)); pw=list(range(k)); rng.shuffle(pu); rng.shuffle(pw)
    if rng.random()<0.5: U,W=W,U
    lab={}
    for x,i in zip(U,pu): lab[x]=('u',i)
    for x,i in zip(W,pw): lab[x]=('v',i)
    return [norm((lab[a],lab[b])) for a,b in E]
def frozen(classes):
    allE=[e for c in classes for e in c]
    for j,c in enumerate(classes):
        S=set(c)
        for e in allE:
            if e not in S and planar(c+[e]): return False
    return True
def thick2(E, rng, tries=200):
    # randomized greedy for a planar 2-cover certificate
    for t in range(tries):
        order=E[:]; rng.shuffle(order); P=[[],[]]; ok=True
        for e in order:
            js=[0,1]; rng.shuffle(js)
            for j in js:
                if planar(P[j]+[e]): P[j].append(e); break
            else: ok=False; break
        if ok: return P
    return None
if __name__=="__main__":
    k=int(sys.argv[1]); seeds=int(sys.argv[2]); rng=random.Random(int(sys.argv[3]))
    A=[norm(e) for e in prism(k)]
    for s in range(seeds):
        B=rand_label(k,rng); C=rand_label(k,rng)
        if set(A)&set(B) or set(A)&set(C) or set(B)&set(C): continue
        cl=[A,B,C]
        if not all(planar(c) for c in cl): continue
        if not frozen(cl): continue
        E=A+B+C
        print("frozen candidate found at", s, "|E|=",len(E))
        P=thick2(E,rng,2000)
        if P:
            assert planar(P[0]) and planar(P[1]) and set(P[0])|set(P[1])==set(E) and not planar(E)
            print("THICKNESS-2 CERTIFICATE FOUND"); print("A=",A);print("B=",B);print("C=",C);print("T1=",P[0]);print("T2=",P[1]); break
        else: print(" no thickness-2 cover found by greedy")
