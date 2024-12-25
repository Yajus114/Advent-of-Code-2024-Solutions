def upper(l: list[int]) -> int:
    return all(0 < l[i] - l[i + 1] < 4 for i in range(len(l) - 1))


def lower(l: list[int]) -> int:
    return all(-4 < l[i] - l[i + 1] < 0 for i in range(len(l) - 1))


def find_pattern(l: list[int]) -> int:
    # Try removing each element and check conditions
    return any(
        upper(l[:i] + l[i + 1 :]) or lower(l[:i] + l[i + 1 :]) for i in range(len(l))
    )


with open("input.txt", "r") as f:
    res = sum(
        1
        for report in f.read().splitlines()
        if (l := list(map(int, report.split())))
        and (upper(l) or lower(l) or find_pattern(l))
    )
    print(res)
