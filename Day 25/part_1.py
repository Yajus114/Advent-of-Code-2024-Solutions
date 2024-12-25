with open("input.txt", "r") as file:
    inp = []
    for line in file.read().split("\n\n"):
        inp.append(line.splitlines())
locks: list = []
keys: list = []
for grid in inp:
    if grid[0] == "#####":
        locks.append(grid)
    else:
        keys.append(grid)


def fits_without_overlap(lock: list, key: list) -> bool:
    for i in range(7):
        for j in range(5):
            if lock[i][j] == "#" and key[i][j] == "#":
                return False
    return True


unique_pairs = 0

for lock in locks:
    for key in keys:
        if fits_without_overlap(lock, key):
            unique_pairs += 1

print(unique_pairs)
