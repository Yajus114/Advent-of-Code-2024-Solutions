import re

with open("input.txt", "r") as file:
    a, b, c, *program = map(int, re.findall(r"\d+", file.read()))


def solver(a, b=0, c=0):
    output = []
    pointer = 0

    def combos(operand):
        if operand in range(4):
            return operand
        elif operand == 4:
            return a
        elif operand == 5:
            return b
        elif operand == 6:
            return c

    while pointer < len(program):
        ins = program[pointer]
        operand = program[pointer + 1]
        if ins == 0:
            a >>= combos(operand)
        elif ins == 1:
            b ^= operand
        elif ins == 2:
            b = combos(operand) & 7
        elif ins == 3:
            if a != 0:
                pointer = operand
                continue
        elif ins == 4:
            b ^= c
        elif ins == 5:
            output.append(combos(operand) & 7)
        elif ins == 6:
            b = a >> combos(operand)
        elif ins == 7:
            c = a >> combos(operand)
        pointer += 2
    return output


# print(*solver(a, b, c), sep=",")
candidates = [0]
for i in range(len(program)):
    next_candidate = []
    for val in candidates:
        for j in range(8):
            target = (val << 3) + j
            if solver(target) == program[-i - 1 :]:
                next_candidate.append(target)
    candidates = next_candidate
print(candidates)
