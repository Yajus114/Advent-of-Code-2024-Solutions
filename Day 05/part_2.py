from functools import cmp_to_key

# The solution I came up with wasn't able to solve 1 test case, so I referred to the video https://youtu.be/BHFnoc4bw3U?si=Shy2QSn3fxQdlugi
stuff: list = []
answer: int = 0
cache: dict = {}


# Function to find all the inordered updates by verfiying all possible combinations using 2 pointers, i and j
def is_ordered(update: list, l: int):
    for i in range(l):
        for j in range(i + 1, l):
            if cache[(update[i], update[j])] == 1:
                return False
    return True


def cmp(x, y):
    return cache[(x, y)]


with open("input.txt", "r") as file:
    # First we set up our rules
    for line in file:
        if line.isspace():
            break
        stuff.append(list(map(int, line.split("|"))))

    # Next we set up our comparator and conditions
    for x, y in stuff:
        cache[(x, y)] = -1
        cache[(y, x)] = 1

    # Finally we get the second half of the inputs,
    for line in file:
        update = list(map(int, line.split(",")))
        l = len(update)
        if is_ordered(update, l):  # find the unordered updates
            continue
        update.sort(key=cmp_to_key(cmp))  # sort them according to the comparison rules
        # and find the middle value to add it to the answers variable.
        answer += update[l // 2]
print(answer)
