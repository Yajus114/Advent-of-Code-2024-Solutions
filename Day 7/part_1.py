# Took me so long for such a fairly simple problem lol.


def check(var: int, target: int, elems: list, ind: int, llm: int) -> bool:
    if ind == llm:
        return True if var == target else False

    elem = elems[ind]
    return (
        True
        if check(var + elem, target, elems, ind + 1, llm)
        or check(var * elem, target, elems, ind + 1, llm)
        else False
    )


with open("input.txt", "r") as file:
    inp = file.read().splitlines()

answer: int = 0
for line in inp:
    colon: int = int(line.index(":"))
    target: int = int(line[:colon])
    elems: list[int] = [int(x) for x in line[colon + 1 :].split()]
    if check(0, target, elems, 0, len(elems)):
        answer += target

print(answer)
