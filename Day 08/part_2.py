with open("input.txt", "r") as file:
    grid = file.read().splitlines()


R = len(grid)
C = len(grid[0])
antennas = {}
for i, r in enumerate(grid):
    for j, char in enumerate(r):
        if char != ".":
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((i, j))

antinodes = set()
for elem in antennas.values():
    for i in range(len(elem)):
        for j in range(len(elem)):
            if i == j:
                continue
            r1, c1 = elem[i]
            r2, c2 = elem[j]
            dr = r2 - r1
            dc = c2 - c1
            a, b = r1, c1
            while 0 <= a < R and 0 <= b < C:
                antinodes.add((a, b))
                a += dr
                b += dc
print(len(antinodes))
