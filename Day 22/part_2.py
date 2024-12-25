with open("input.txt", "r") as file:
    inp = [int(x) for x in file.read().splitlines()]

seq_to_total = {}

for n in inp:
    prev = n % 10
    seen = set()
    diffs = []
    for _ in range(2000):
        n ^= n * 64
        n %= 16777216
        n ^= n // 32
        n %= 16777216
        n ^= n * 2048
        n %= 16777216
        diffs.append(prev - n % 10)
        prev = n % 10
        if len(diffs) >= 4:
            seq = tuple(diffs)
            diffs.pop(0)
            if seq in seen:
                continue
            seen.add(seq)
            if seq not in seq_to_total:
                seq_to_total[seq] = 0
            seq_to_total[seq] += prev


print(max(seq_to_total.values()))
