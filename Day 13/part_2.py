import re

total = 0
with open("input.txt", "r") as file:
    for block in file.read().split("\n\n"):
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
        px += 1_00_00_00_00_00_000
        py += 1_00_00_00_00_00_000
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            total += int(ca * 3 + cb)


print(total)
