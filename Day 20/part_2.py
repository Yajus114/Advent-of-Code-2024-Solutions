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

# there can now be up to 10 cheats, each cheat being 2 picosecond saving
# if 2 cheats have the same start and finish, then they're the same cheats
# so the check_directions list will have to check in range 2 to 20

count = 0
for r in range(1, rows):
    for c in range(1, cols):
        if grid[r][c] == "#":
            continue
        for x in range(2, 21):
            for dr in range(x + 1):
                dc = x - dr
                # if x is 20, then dr is 0 to 20, and dc is 20 to 0, so it covers all the cases
                for i, j in {
                    (r + dr, c + dc),
                    (r + dr, c - dc),
                    (r - dr, c + dc),
                    (r - dr, c - dc),
                }:
                    if (
                        i not in range(1, rows)
                        or j not in range(1, cols)
                        or grid[i][j] == "#"
                    ):
                        continue
                    if dist[r][c] - dist[i][j] >= 100 + x:
                        count += 1
print(count)
