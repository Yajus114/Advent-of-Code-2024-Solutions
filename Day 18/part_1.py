from collections import deque


def shortest_path_binary_matrix(grid) -> int:
    grid_len = len(grid)
    if grid[0][0] == "#" or grid[grid_len - 1][grid_len - 1] == "#":
        return -1

    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, length = queue.popleft()
        if r == grid_len - 1 and c == grid_len - 1:
            return length

        for dr, dc in directions:
            if (
                r + dr in range(grid_len)
                and c + dc in range(grid_len)
                and grid[r + dr][c + dc] == "."
                and (r + dr, c + dc) not in visited
            ):
                queue.append((r + dr, c + dc, length + 1))
                visited.add((r + dr, c + dc))

    return -1


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        grid = [["."] * 71 for _ in range(71)]

        for _ in range(1024):
            line = file.readline()
            r, c = map(int, line.split(","))
            grid[c][r] = "#"

    print(shortest_path_binary_matrix(grid))
