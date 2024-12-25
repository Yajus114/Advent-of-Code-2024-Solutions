with open("input.txt", "r") as file:
    inp = file.read().splitlines()


def gen_prn(n: int) -> int:
    for _ in range(2000):
        # first multiply by 64 and mix the result into n, then prune
        ## mixing is ^=
        # second we //= 32 and then mix and prune it
        ## pruning is %= 16777216
        # multiply n by 2048, then mix and prune
        n ^= n * 64
        n %= 16777216
        n ^= n // 32
        n %= 16777216
        n ^= n * 2048
        n %= 16777216
    return n


print(sum(gen_prn(int(x)) for x in inp))
