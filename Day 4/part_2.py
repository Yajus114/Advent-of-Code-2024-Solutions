import numpy as np

with open("input.txt", "r") as file:
    array = np.array(file.read().splitlines())

R, C = len(array), len(array[0])
ans = 0

orientations = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

for r in range(1, R - 1):
    for c in range(1, C - 1):
        if array[r][c] == "A":
            ms_count = 0  # Count valid M and S pairs
            for dr, dc in orientations:
                nr, nc = r + dr, c + dc  # New row, column
                if array[nr][nc] == "M":
                    # Check for corresponding 'S'
                    opposite_r, opposite_c = r - dr, c - dc
                    if array[opposite_r][opposite_c] == "S":
                        ms_count += 1
            # A valid X-MAS has exactly two valid pairs
            if ms_count == 2:
                ans += 1

print(ans)
