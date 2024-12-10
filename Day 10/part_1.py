with open("input.txt", "r") as file:
    grid = [[int(x) for x in line] for line in file.read().splitlines()]

R = len(grid)
C = len(grid[0])
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def check(r, c) -> int:
    if (r, c) in seen:
        return 0
    seen.add((r, c))
    cur_val = grid[r][c]
    if cur_val == 9:
        return 1
    answer = 0
    for cur_dir in range(4):
        nr, nc = directions[cur_dir]
        cr, cc = r + nr, c + nc
        if 0 <= cr < R and 0 <= cc < C and grid[cr][cc] == cur_val + 1:
            # print(grid[cr][cc])
            answer += check(cr, cc)
    return answer


# find every 0
result = 0
for i, line in enumerate(grid):
    for ind, item in enumerate(line):
        seen = set()
        if item == 0:
            result += check(i, ind)
print(result)
