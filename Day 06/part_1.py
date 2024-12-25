with open("input.txt", "r") as file:
    inp: list = file.read().splitlines()

directions: list[tuple] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# up, right, down, left - at 90° increments

# Find the coordinates of the starting position
for ind, elem in enumerate(inp):
    if "^" in elem:
        i, j = ind, elem.index("^")
        break

# movement is marking the spot with an 'X' and adding the count if the place hasn't already been marked an 'X'
# start from this position of the grid
# the loop goes on until the guard reaches the end of a row/column
count, current_dir, current_row, current_col = 0, 0, -1, 0
R: int = len(inp)
C: int = len(inp[0])

while True:
    if inp[i][j] != "X":
        count += 1
        inp[i] = inp[i][:j] + "X" + inp[i][j + 1 :]
    if 0 <= i + current_row < R and 0 <= j + current_col < C:
        if inp[i + current_row][j + current_col] == "#":
            current_dir = (current_dir + 1) & 3
            current_row, current_col = directions[current_dir]
        i += current_row
        j += current_col
    else:
        break
print(count)
# I am so proud I was able to solve this
# for powers of two, mod x == & (x - 1) but faster
