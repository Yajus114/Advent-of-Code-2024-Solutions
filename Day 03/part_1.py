import re

with open("input.txt", "r") as file:
    print(
        sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", file.read()))
    )
