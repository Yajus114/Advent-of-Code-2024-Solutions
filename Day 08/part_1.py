with open("input.txt", "r") as file:
    grid = file.read().splitlines()


# Analyse the grid to find anything that's not a dot.
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
        for j in range(1 + i, len(elem)):
            r1, c1 = elem[i]
            r2, c2 = elem[j]
            x, y = 2 * r1 - r2, 2 * c1 - c2
            if 0 <= x < R and 0 <= y < C:
                antinodes.add((x, y))
            x, y = 2 * r2 - r1, 2 * c2 - c1
            if 0 <= x < R and 0 <= y < C:
                antinodes.add((x, y))

print(len(antinodes))
