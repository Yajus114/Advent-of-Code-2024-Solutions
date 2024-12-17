with open("input.txt", "r") as file:
    grid, instr = file.read().split("\n\n")
    grid = grid.strip().splitlines()
    instr = instr.replace("\n", "")

dirs = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}

rows = len(grid) - 1
cols = len(grid[0]) - 1
leave = False
for r in range(1, rows):
    for c in range(1, cols):
        if grid[r][c] == "@":
            leave = True
            break
    if leave:
        break

for i in instr:
    nr, nc = dirs[i]
    if grid[r + nr][c + nc] == "#":
        continue
    elif grid[r + nr][c + nc] == ".":
        grid[r] = grid[r].replace("@", ".")
        r += nr
        c += nc
        grid[r] = grid[r][:c] + "@" + grid[r][c + 1 :]
    else:
        ox, oy = r + nr, c + nc
        do = False
        while True:
            if grid[ox + nr][oy + nc] == "#":
                break
            elif grid[ox + nr][oy + nc] == "O":
                ox += nr
                oy += nc
            else:
                do = True
                ox += nr
                oy += nc
                break
        if do:
            grid[r] = grid[r].replace("@", ".")
            r += nr
            c += nc
            grid[r] = grid[r][:c] + "@" + grid[r][c + 1 :]
            grid[ox] = grid[ox][:oy] + "O" + grid[ox][oy + 1 :]

print(
    sum(
        100 * i + j for j in range(1, cols) for i in range(1, rows) if grid[i][j] == "O"
    )
)
