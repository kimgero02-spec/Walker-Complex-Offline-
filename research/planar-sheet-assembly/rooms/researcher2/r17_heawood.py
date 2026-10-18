# 결정적 시험: 헤우드 그래프에 K5 마이너가 있는가 (모형 하나를 찾으면 끝)
import networkx as nx, itertools as it
G=nx.heawood_graph()
def connsets(G,maxs):
    seen=set(); out=[]
    for v in G:
        stack=[frozenset([v])]
        while stack:
            S=stack.pop()
            if S in seen: continue
            seen.add(S); out.append(S)
            if len(S)<maxs:
                for x in S:
                    for y in G[x]:
                        if y not in S: stack.append(S|{y})
    return out
CS=[S for S in connsets(G,6) if len(S)>=2]
nb={S:set().union(*[set(G[x]) for x in S])-S for S in CS}
def search(N):
    CSs=sorted(CS,key=len)
    def rec(chosen,used,start):
        if len(chosen)==N: return chosen
        for i in range(start,len(CSs)):
            S=CSs[i]
            if S&used: continue
            if all(nb[S]&T for T in chosen):
                r=rec(chosen+[S],used|S,i+1)
                if r: return r
        return None
    return rec([],frozenset(),0)
m=search(5); print('K5 model in Heawood:',[sorted(S) for S in m] if m else None)
