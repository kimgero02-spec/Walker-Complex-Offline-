# R24-researcher3: candidate search for a triangular-locked 4-partition of G80 (tau(G80) >= 4 ?).
# Greedy peeling: P1 maximal planar in G, P2 maximal planar in G-P1, P3 maximal planar in G-P1-P2.
# If G-P1-P2-P3 is nonempty, continue peeling -> triangular-locked partition with >= 4 sheets.
# This is ONLY a search; any hit is saved and re-verified independently by r24_check.py.
# usage: python3 r24_peel.py [trials] [seed] [mode]
#   mode "rand": random edge order;  mode "mix": order interleaving the three Q-classes (try to cut Q evenly)
import sys, json, random, networkx as nx
def planar_add(H, e):
    H.add_edge(*e)
    if nx.check_planarity(H)[0]: return True
    H.remove_edge(*e); return False
def maximal_planar(edges, order):
    H = nx.Graph()
    for e in order:
        planar_add(H, e)
    return sorted(tuple(sorted(e)) for e in H.edges())
def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    mode = sys.argv[3] if len(sys.argv) > 3 else "rand"
    rng = random.Random(seed)
    Q = [[tuple(sorted(e)) for e in q] for q in json.load(open("r20_locked_only_N80_n3.json"))["Q"]]
    E = sorted(e for q in Q for e in q)
    cls = {e: k for k, q in enumerate(Q) for e in q}
    best = None
    for t in range(trials):
        rest = set(E); sheets = []
        while rest:
            order = list(rest); rng.shuffle(order)
            if mode == "mix" and not sheets:
                # first sheet: take edges round-robin from the three Q classes
                byc = [[e for e in order if cls[e] == k] for k in range(3)]
                order = [x for tup in zip(*byc) for x in tup]
            P = maximal_planar(rest, order)
            sheets.append(P); rest -= set(P)
        sz = [len(p) for p in sheets]
        print(t, len(sheets), sz, flush=True)
        if best is None or len(sheets) > len(best):
            best = sheets
        if len(sheets) >= 4:
            json.dump({"Q": [[list(e) for e in p] for p in sheets]}, open(f"r24_tl{len(sheets)}_seed{seed}_{mode}_{t}.json", "w"))
            print("FOUND", len(sheets), sz); break
main()
