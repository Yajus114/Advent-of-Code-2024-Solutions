from collections import deque

with open("test input.txt", "r") as file:
    grid = file.read().splitlines()

rows = len(grid)
cols = len(grid[0])
regions = []
seen = set()

for r in range(rows):
    for c in range(cols):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        region = {(r, c)}
        q = deque([(r, c)])
        crop = grid[r][c]
        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                if (
                    (nr, nc) in region
                    or nr not in range(rows)
                    or nc not in range(cols)
                    or grid[nr][nc] != crop
                ):
                    continue
                region.add((nr, nc))
                q.append((nr, nc))

        seen |= region
        regions.append(region)


def sides(region):
    cor_cand = set()
    for r, c in region:
        for cr, cc in [
            (r - 0.5, c - 0.5),
            (r + 0.5, c - 0.5),
            (r + 0.5, c + 0.5),
            (r - 0.5, c + 0.5),
        ]:
            cor_cand.add((cr, cc))
    corners = 0
    for cr, cc in cor_cand:
        config = [
            (sr, sc) in region
            for sr, sc in [
                (cr - 0.5, cc - 0.5),
                (cr + 0.5, cc - 0.5),
                (cr + 0.5, cc + 0.5),
                (cr - 0.5, cc + 0.5),
            ]
        ]
        number = sum(config)
        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [
                False,
                True,
                False,
                True,
            ]:
                corners += 2
        elif number == 3:
            corners += 1
    return corners


print(sum(len(region) * sides(region) for region in regions))
