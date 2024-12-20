with open("input.txt", "r") as file:
    grid = [[_ for _ in line] for line in file.read().splitlines()]

rows = len(grid) - 1
cols = len(grid[0]) - 1

for r in range(1, rows):
    for c in range(1, cols):
        if grid[r][c] == "S":
            break
    else:
        continue
    break

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
dist = [[-1] * cols for _ in range(rows)]
dist[r][c] = 0
sr, sc = r, c
while grid[r][c] != "E":
    for i, j in directions:
        nr, nc = r + i, c + j
        if (
            nr not in range(1, rows)
            or nc not in range(1, cols)
            or grid[nr][nc] == "#"
            or dist[nr][nc] != -1
        ):
            continue
        dist[nr][nc] = dist[r][c] + 1
        r = nr
        c = nc
count = 0

check_directions = [(0, 2), (2, 0)]
for r in range(1, rows):
    for c in range(1, cols):
        if grid[r][c] == "#":
            continue
        for i, j in check_directions:
            nr, nc = r + i, c + j
            if (
                nr not in range(1, rows)
                or nc not in range(1, cols)
                or grid[nr][nc] == "#"
            ):
                continue
            if abs(dist[nr][nc] - dist[r][c]) >= 102:
                count += 1
print(count)
