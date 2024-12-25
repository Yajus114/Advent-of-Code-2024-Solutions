with open("input.txt", "r") as file:
    conns = {}
    for x, y in [line.strip().split("-") for line in file]:
        if x not in conns:
            conns[x] = set()
        if y not in conns:
            conns[y] = set()
        conns[x].add(y)
        conns[y].add(x)

total = 0
valids = set()
for x in conns:
    for y in conns[x]:
        for z in conns[y]:
            if x != z and x in conns[z]:
                valids.add(tuple(sorted([x, y, z])))

print(len([s for s in valids if any(c.startswith("t") for c in s)]))
