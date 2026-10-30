# R21-researcher3: VERIFIER. Direct planarity checks (networkx check_planarity) of a claimed locked partition.
# usage: python3 r21_verify.py file.json   (keys: "Q": list of edge lists; optional "E")
# Prints: partition ok, each sheet planar, locked (L1,L2), connectivity of sheets, triangle count t of G,
# and the girth/triangle thickness bound  theta=2 possible only if |E| <= 2(2V-4) + t/2  (R21 Lemma 1).
import sys, json, itertools, networkx as nx
def planar(E):
    H=nx.Graph(); H.add_edges_from(E); return nx.check_planarity(H)[0]
def main(fn):
    d=json.load(open(fn)); Q=[[tuple(sorted(e)) for e in q] for q in d["Q"]]
    E=sorted(set(e for q in Q for e in q)) if "E" not in d else sorted(tuple(sorted(e)) for e in d["E"])
    G=nx.Graph(); G.add_edges_from(E); V=G.number_of_nodes()
    allq=[e for q in Q for e in q]
    print("V",V,"|E|",len(E),"sheets",[len(q) for q in Q])
    print("L1 disjoint & cover:", len(allq)==len(set(allq)) and set(allq)==set(E))
    for k,q in enumerate(Q):
        H=nx.Graph(); H.add_edges_from(q)
        print(f"sheet {k}: planar={planar(q)} nodes={H.number_of_nodes()} connected={nx.is_connected(H)} "
              f"3conn={nx.node_connectivity(H)>=3}")
    tests=0; ok=True
    for k,q in enumerate(Q):
        s=set(q)
        for e in E:
            if e in s: continue
            tests+=1
            if planar(q+[e]): ok=False; print("NOT locked: sheet",k,"+",e)
    print("L2 locked:",ok,"(direct planarity tests:",tests,")")
    t=sum(nx.triangles(G).values())//3
    print("triangles t(G) =",t, "; theta=2 needs |E| <=", 2*(2*V-4)+t/2, "->",
          "theta>=3 PROVED" if len(E)>2*(2*V-4)+t/2 else "bound inconclusive")
    if "A" in d and "B" in d:
        print("A planar",planar([tuple(e) for e in d["A"]]),"B planar",planar([tuple(e) for e in d["B"]]),
              "A u B == E", set(tuple(sorted(e)) for e in d["A"]+d["B"])==set(E))
if __name__=="__main__": main(sys.argv[1])
