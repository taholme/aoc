from math import prod
from networkx import Graph, minimum_edge_cut, connected_components

g = Graph()

for line in open(0):
    l, r = line.strip().split(":")
    for n in r.split():
        g.add_edge(l, n)
        g.add_edge(n, l)

g.remove_edges_from(minimum_edge_cut(g))
print(prod(len(x) for x in connected_components(g)))
