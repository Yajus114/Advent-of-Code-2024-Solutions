from collections import deque
from heapq import heappush, heappop

with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

# Found out the start and end coordinates through observing the input
sr, sc = 139, 1
er, ec = 1, len(grid[0]) - 2
heap = [(0, sr, sc, 0, 1)]
lowest_cost = {(sr, sc, 0, 1): 0}
backtrack = {}
best_cost = float("inf")
end_states = set()

while heap:
    cost, r, c, dr, dc = heappop(heap)
    if cost > lowest_cost.get((r, c, dr, dc), float("inf")):
        continue
    if r == er and c == ec:
        if cost > best_cost:
            break
        best_cost = cost
        end_states.add((r, c, dr, dc))
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
            backtrack[(nr, nc, ndr, ndc)] = set()
            lowest_cost[(nr, nc, ndr, ndc)] = new_cost
        backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
        heappush(heap, (new_cost, nr, nc, ndr, ndc))
states = deque(end_states)
seen = set(end_states)

while states:
    key = states.popleft()
    for last in backtrack.get(key, []):
        if last in seen:
            continue
        seen.add(last)
        states.append(last)

print(len({(r, c) for r, c, _, _ in seen}))
# I have to practice a lot of Djikstra's and Backtracking problems. Today's part 2 was too difficult.
