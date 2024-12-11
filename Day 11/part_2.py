with open("input.txt", "r") as f:
    inp = [int(x) for x in f.read().split()]


def even_digits(elem: int) -> bool:
    temp = str(elem)
    if len(temp) % 2 == 0:
        return True
    return False


def twice(elem: int) -> list:
    temp = str(elem)
    l_temp = int(len(temp) / 2)
    return [int(temp[:l_temp]), int(temp[l_temp:])]


for _ in range(75):
    l = len(inp)
    i = 0
    while i < l:
        test = inp[i]
        if test == 0:
            inp[i] = 1
        elif even_digits(test):
            inp = inp[:i] + twice(test) + inp[i + 1 :]
            l = len(inp)
            i += 1
        else:
            inp[i] *= 2024
        i += 1
print(len(inp))
