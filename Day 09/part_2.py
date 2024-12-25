# with open("input.txt", "r") as f:
#     inp = [int(x) for x in f.readline().strip()]

# a = []
# answer = 0
# count = 0

# for i, char in enumerate(inp):
#     if i % 2 == 0:
#         a.append([count] * char)
#         count += 1
# print(a)
# count = 0
# for i, char in enumerate(inp):
#     if not a:
#         break
#     if i % 2 == 0:
#         for _ in range(len(a[0])):
#             answer += a[0].pop() * count
#             count += 1
#         a.pop(0)
#         print(a, answer)
#     else:
#         p2 = len(a) - 1
#         while p2 >= 0:
#             if len(a[p2]) <= char:
#                 for _ in range(len(a[p2])):
#                     answer += a[p2].pop() * count
#                     count += 1
#                     char -= 1
#                 a.pop(p2)
#                 print(a, answer)
#                 if char == 0:
#                     break
#             p2 -= 1
#         else:
#             count += 1

# print(answer)
# For some reason, this solution doesn't work. Will have to investigate why later.

fid = 0
files = {}
blanks = []
pos = 0
with open("input.txt", "r") as f:
    for i, char in enumerate(f.readline().strip()):
        x = int(char)
        if i % 2 == 0:
            files[fid] = (pos, x)
            fid += 1
        else:
            if x != 0:
                blanks.append((pos, x))
        pos += x

while fid > 0:
    fid -= 1
    pos, size = files[fid]
    for i, (start, length) in enumerate(blanks):
        if start >= pos:
            blanks = blanks[:i]
            break
        if size <= length:
            files[fid] = (start, size)
            if size == length:
                blanks.pop(i)
            else:
                blanks[i] = (start + size, length - size)
            break
total = 0
for fid, (pos, size) in files.items():
    for x in range(pos, pos + size):
        total += fid * x
print(total)
