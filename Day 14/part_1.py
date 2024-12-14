import re

rows, cols = 101, 103
q1, q2, q3, q4 = 0, 0, 0, 0
qr, qc = rows // 2, cols // 2

with open("input.txt", "r") as file:
    for line in file.read().splitlines():
        px, py, vx, vy = map(int, re.findall(r"-?\d+", line))

        fx = (px + vx * 100) % rows
        fy = (py + vy * 100) % cols

        if fx == qr or fy == qc:
            continue
        if fx < qr and fy < qc:
            q1 += 1
        elif fx < qr and fy >= qc:
            q2 += 1
        elif fx >= qr and fy < qc:
            q3 += 1
        elif fx >= qr and fy >= qc:
            q4 += 1

print(q1 * q2 * q3 * q4)
