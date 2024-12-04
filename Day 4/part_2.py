with open("input.txt", "r") as file:
    array = file.read().splitlines()

R, C = len(array), len(array[0])
ans = 0

orientations = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

for r in range(1, R - 1):
    for c in range(1, C - 1):
        if array[r][c] == "A":
            ms_count = 0  # Count valid M and S pairs
            for dr, dc in orientations:
                if array[r + dr][c + dc] == "M" and array[r - dr][c - dc] == "S":
                    ms_count += 1
            if ms_count == 2:
                ans += 1

print(ans)
