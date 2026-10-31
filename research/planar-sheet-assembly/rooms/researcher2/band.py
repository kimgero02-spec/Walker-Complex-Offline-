# 다각형 조각 띠(H=C_k). 조각 i: 경계 = 가로대 r_i, 윗호(길이 t_i), 가로대 r_{i+1}, 아랫호(길이 s_i).
# t_i=0 이면 윗쪽 핀치(두 가로대가 윗 끝점 공유). 마지막 조각이 r_k -> r_0 로 닫힘(twist 면 위/아래 교차).
import itertools as it
import networkx as nx

def band(ts, ss, twist):
    k = len(ts)
    G = nx.MultiGraph()
    cnt = [0]
    def new():
        cnt[0] += 1; return cnt[0]
    top0, bot0 = new(), new()
    top, bot = top0, bot0
    rungs = [(top0, bot0)]
    G.add_edge(top0, bot0)
    for i in range(k):
        last = (i == k - 1)
        # 윗호
        endT = (bot0 if twist else top0) if last else None
        endB = (top0 if twist else bot0) if last else None
        def arc(start, L, end):
            cur = start
            if L == 0:
                return cur if end is None else ('MERGE', cur, end)
            for j in range(L):
                nxt = end if (end is not None and j == L - 1) else new()
                G.add_edge(cur, nxt); cur = nxt
            return cur
        nt = arc(top, ts[i], endT); nb = arc(bot, ss[i], endB)
        if last:
            merges = [x for x in (nt, nb) if isinstance(x, tuple)]
            for _, a, b in merges:
                G = nx.contracted_nodes(G, b, a, self_loops=True)
            break
        top, bot = nt, nb
        if not (isinstance(top, tuple) or isinstance(bot, tuple)):
            G.add_edge(top, bot); rungs.append((top, bot))
    return G

def simple(G):
    return nx.number_of_selfloops(G) == 0 and all(G.number_of_edges(u, v) == 1 for u, v in set(map(lambda e: tuple(sorted(e)), G.edges())))

def planar(G):
    return nx.check_planarity(nx.Graph(G))[0]

if __name__ == "__main__":
    # 검증: 핀치 없는 사각형 띠 = 프리즘/뫼비우스
    for k in (3, 4):
        print("sq", k, planar(band([1]*k, [1]*k, False)), planar(band([1]*k, [1]*k, True)),
              nx.is_isomorphic(nx.Graph(band([1]*k, [1]*k, True)), nx.circulant_graph(2*k, [1, k])))
    # 두 부채: 위 핀치 m개, 아래 핀치 m개, 닫는 조각은 큰 다각형
    for m in (2, 3, 5):
        ts = [0]*m + [1]*m + [2]; ss = [1]*m + [0]*m + [2]
        Gt = band(ts, ss, True); Gs = band(ts, ss, False)
        print("2fan m=", m, "k=", len(ts), "twist simple", simple(Gt), "planar", planar(Gt), "| straight planar", planar(Gs))
    # 4개 조각: 삼각형-사각형-삼각형-사각형 (핀치 짝 2개, 서로 다른 변)
    for ts, ss in [([0,1,0,1],[1,1,1,1]), ([0,1,1,1],[1,1,0,1]), ([0,0,1,1],[1,1,1,1])]:
        G = band(ts, ss, True); print("k4", ts, ss, "simple", simple(G), "planar", planar(G))
