import networkx as nx

with open("input.txt", "r") as file:
    conns = nx.Graph()
    for x, y in [line.strip().split("-") for line in file]:
        conns.add_edge(x, y)
        conns.add_edge(y, x)

print(*sorted(max(nx.find_cliques(nx.Graph(conns)), key=len)), sep=",")
