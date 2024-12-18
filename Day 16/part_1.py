from heapq import heappush, heappop

with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

# Found out the start and end coordinates through observing the input
sr, sc = 139, 1
er, ec = 1, len(grid[0]) - 2
heap = [(0, sr, sc, 0, 1)]
lowest_cost = {(sr, sc, 0, 1): 0}

while heap:
    cost, r, c, dr, dc = heappop(heap)
    if cost > lowest_cost.get((r, c, dr, dc), float("inf")):
        continue
    if r == er and c == ec:
        break
    for new_cost, nr, nc, ndr, ndc in [
        (cost + 1, r + dr, c + dc, dr, dc),
        (cost + 1000, r, c, dc, -dr),
        (cost + 1000, r, c, -dc, dr),
    ]:
        if grid[nr][nc] == "#":
            continue
        lowest = lowest_cost.get((nr, nc, ndr, ndc), float("inf"))
        if new_cost > lowest:
            continue
        if new_cost < lowest:
            lowest_cost[(nr, nc, ndr, ndc)] = new_cost
        heappush(heap, (new_cost, nr, nc, ndr, ndc))
print(cost)
