from functools import cache
from math import floor, log10

with open("input.txt", "r") as f:
    stones = [int(x) for x in f.readline().split()]


@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)

    half_digits = floor(log10(stone)) + 1
    if half_digits % 2 == 0:
        divisor = 10 ** (half_digits // 2)
        return count(stone // divisor, steps - 1) + count(stone % divisor, steps - 1)

    return count(stone * 2024, steps - 1)


if __name__ == "__main__":
    print(sum(count(stone, 25) for stone in stones))
