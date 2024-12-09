# TODO: Fix this function. output > expected
def joining(var: int, target: int, elems: list[int], ind: int, llm: int) -> bool:
    if ind == llm:
        if var == target:
            return True
        else:
            if var not in checked:
                checked.add(var)
            return False
    if var > target:
        return False
    if var in checked:
        return False

    elem = elems[ind]
    ind += 1
    return (
        joining(var + elem, target, elems, ind, llm)
        | joining(var * elem, target, elems, ind, llm)
        | joining(int(str(var) + str(elem)), target, elems, ind, llm)
    )


def possible(elems: list) -> bool:
    if len(elems) == 1:
        return {elems[0]}
    subset = possible(elems[:-1])
    last = elems[-1]
    return (
        {x + last for x in subset}
        | {x * last for x in subset}
        | {int(str(x) + str(last)) for x in subset}
    )


def calculate_answer(file_path: str) -> int:
    with open(file_path, "r") as file:
        inp = file.read().splitlines()

    answer = 0
    for line in inp:
        target, second = line.split(":")
        elems = [int(x) for x in second.split()]
        target = int(target)
        if target in possible(elems):  # joining(0, target, elems, 0, len(elems)):
            answer += target

    return answer


if __name__ == "__main__":
    checked = set()
    print(calculate_answer("input.txt"))
