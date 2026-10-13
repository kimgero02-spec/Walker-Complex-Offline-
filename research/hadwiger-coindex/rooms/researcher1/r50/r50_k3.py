# k=3 시트 경계 색수 정리의 극값 예 두 개 확인
import itertools, networkx as nx
import importlib.util,sys
spec=importlib.util.spec_from_file_location("t","/home/user/Walker-Complex-Offline-/research/hadwiger-coindex/rooms/researcher1/r50/r50_tight.py")
import io,contextlib
with contextlib.redirect_stdout(io.StringIO()):
    t=importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
def multi(parts):
    G=nx.Graph()
    for B,W in parts: G=nx.union(G,B)
    for (B,W),(B2,W2) in itertools.combinations(parts,2):
        G.add_edges_from((u,v) for u in W for v in W2)
    return G
print("(1,1,1) 3xGamma1:", t.chi(multi([t.gamma1("A"),t.gamma1("B"),t.gamma1("C")])), "bound 5")
print("(2,2,1) Gamma2,Gamma2,Gamma1:", t.chi(multi([t.gamma(2,"A"),t.gamma(2,"B"),t.gamma1("C")])), "bound 6")
