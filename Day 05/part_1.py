# Manually separating the data into two files, namely input.txt and input2.txt
def check_valid(item: str, play_field: list, stuff: dict) -> bool:
    if item not in stuff:
        return True
    for things in stuff[item]:
        if things in play_field:
            return False
    return True


with open("input.txt", "r") as file:
    stuff: dict = {}
    for item in file.read().splitlines():
        a, b = item.split("|")
        if a not in stuff:
            stuff[a] = [b]
        else:
            stuff[a].append(b)


answer: int = 0
with open("input2.txt", "r") as file:
    line: str = file.readline().replace("\n", "")
    while line:
        cont: bool = True
        field: list = line.split(",")
        for i, v in enumerate(field[1:], 1):
            if not check_valid(v, field[:i], stuff):
                cont = False
                break
        if cont:
            answer += int(field[len(field) // 2])
        line = file.readline().replace("\n", "")
print(answer)
