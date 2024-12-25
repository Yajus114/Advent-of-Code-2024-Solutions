with open("input.txt", "r") as file:
    a, b = file.read().split("\n\n")

items = {
    coord: int(val) for line in a.splitlines() for coord, val in [line.split(": ")]
}
formulae = {}


def calc(wire):
    if wire in items:
        return items[wire]
    x, y, z = formulae[wire]
    if y == "AND":
        items[wire] = calc(x) & calc(z)
    elif y == "OR":
        items[wire] = calc(x) | calc(z)
    else:
        items[wire] = calc(x) ^ calc(z)
    return items[wire]


for line in b.splitlines():
    left, right = line.split(" -> ")
    formulae[right] = left.split()

for wire in formulae:
    calc(wire)

res = sorted(
    [[x, str(y)] for x, y in items.items() if x.startswith("z")],
    key=lambda x: x[0],
    reverse=True,
)

print(int("".join(y for _, y in res), 2))
