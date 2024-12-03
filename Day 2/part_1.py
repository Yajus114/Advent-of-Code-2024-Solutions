with open("input.txt", "r") as f:
    print(
        sum(
            all(0 < l[i] - l[i + 1] < 4 for i in range(len(l) - 1))
            + all(-4 < l[i] - l[i + 1] < 0 for i in range(len(l) - 1))
            for l in (
                [int(i) for i in report.split()] for report in f.read().splitlines()
            )
        )
    )
