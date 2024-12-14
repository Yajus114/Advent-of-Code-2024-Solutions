import re

# System of linear equations/intersection of two lines
total = 0
with open("input.txt", "r") as file:
    for block in file.read().split("\n\n"):
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            total += int(ca * 3 + cb)


print(total)
