"""
I have no idea how to do this one...
Took the hint from this video: https://youtu.be/P1OZJ5ZkLN8?si=wXtziLxHynjKQq_M

For future reference/optimisation, potential things to learn and practice:
1. Numpy (duh)
2. Complex Numbers in Python
3. Rotating of Matrices
"""

with open("input.txt", "r") as file:
    inp = file.read().splitlines()
R: int = len(inp)
C: int = len(inp[0])
ans: int = 0
for r in range(R):
    for c in range(C):
        # Horizontal 'XMAS'
        if (
            c + 3 < C
            and inp[r][c] == "X"
            and inp[r][c + 1] == "M"
            and inp[r][c + 2] == "A"
            and inp[r][c + 3] == "S"
        ):
            ans += 1

        # Horizontal 'SAMX'
        if (
            c + 3 < C
            and inp[r][c] == "S"
            and inp[r][c + 1] == "A"
            and inp[r][c + 2] == "M"
            and inp[r][c + 3] == "X"
        ):
            ans += 1

        # Vertical 'XMAS'
        if (
            r + 3 < R
            and inp[r][c] == "X"
            and inp[r + 1][c] == "M"
            and inp[r + 2][c] == "A"
            and inp[r + 3][c] == "S"
        ):
            ans += 1

        # Vertical 'SAMX'
        if (
            r + 3 < R
            and inp[r][c] == "S"
            and inp[r + 1][c] == "A"
            and inp[r + 2][c] == "M"
            and inp[r + 3][c] == "X"
        ):
            ans += 1

        # Forward diagonal 'XMAS'
        if (
            r + 3 < R
            and c + 3 < C
            and inp[r][c] == "X"
            and inp[r + 1][c + 1] == "M"
            and inp[r + 2][c + 2] == "A"
            and inp[r + 3][c + 3] == "S"
        ):
            ans += 1

        # Forward diagonal 'SAMX'
        if (
            r + 3 < R
            and c + 3 < C
            and inp[r][c] == "S"
            and inp[r + 1][c + 1] == "A"
            and inp[r + 2][c + 2] == "M"
            and inp[r + 3][c + 3] == "X"
        ):
            ans += 1

        # Backward diagonal 'XMAS'
        if (
            r + 3 < R
            and c - 3 >= 0
            and inp[r][c] == "X"
            and inp[r + 1][c - 1] == "M"
            and inp[r + 2][c - 2] == "A"
            and inp[r + 3][c - 3] == "S"
        ):
            ans += 1

        # Backward diagonal 'SAMX'
        if (
            r + 3 < R
            and c - 3 >= 0
            and inp[r][c] == "S"
            and inp[r + 1][c - 1] == "A"
            and inp[r + 2][c - 2] == "M"
            and inp[r + 3][c - 3] == "X"
        ):
            ans += 1
# Used ChatGPT to generate the boilerplate cases after understanding the logic

print(ans)
