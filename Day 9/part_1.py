with open("input.txt", "r") as f:
    inp = f.readline().strip()

a = []
answer = 0
count = 0

for i, char in enumerate(inp):
    intv = int(char)
    if i % 2 == 0:
        a.extend([count] * intv)
        count += 1

count = 0
for i, char in enumerate(inp):
    intv = int(char)
    b = 0 if i % 2 == 0 else -1
    while intv > 0 and a:
        answer += a.pop(b) * count
        intv -= 1
        count += 1

print(answer)
