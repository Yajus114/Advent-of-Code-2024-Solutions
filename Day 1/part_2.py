# Day 1, part 2
# I had developed a better solution, but I forgor, so this is the old solution that also works™️
with open("input.txt", "r") as file:
    line = file.read()
    l1, l2 = [], []
    while line:
        temp = line.split()
        l1.append(int(temp[0]))
        l2.append(int(temp[1]))
        line = file.readline()
    print(sum(l2.count(i) * i for i in l1))
