"""
The weirdest puzzle. Nothing is specified, however some things can be deduced.
First, a christmas tree can be assumed to be the case when the density of robots in a quadrant is max. If that's the case, then the safety factor has to be very low. This is because if a + b + c + d = e, then a * b * c * d is max when a = b = c = d (same for just a + b = c). The opposite of that is true if, say, a > (b, c, d). Whenever that is true, the product is smaller, and we can find at what second this occured.
Second, the max number of iterations can only be Height * Width, because after that, all robots will just repeat positions (as per %).

Some information can be deduced from the fact that the quizmaster had made us calculate the product of the quadrants in part 1. I am yet to think the solution for the case if a 'christmas tree' is a traingular structure distributed across the four grids.
"""

import re

min_sf = float("inf")
iteration = None
robots = []
vm = 103 // 2
hm = 101 // 2
with open("input.txt", "r") as file:
    for line in file.read().splitlines():
        robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

for i in range(10_403):
    result = []
    for px, py, vx, vy in robots:
        result.append(((px + vx * i) % 101, (py + vy * i) % 103))
    q1 = q2 = q3 = q4 = 0

    for px, py in result:
        if px == hm or py == vm:
            continue
        elif px < hm:
            if py < vm:
                q1 += 1
            else:
                q3 += 1
        else:
            if py < vm:
                q2 += 1
            else:
                q4 += 1
    sf = q1 * q2 * q3 * q4
    if sf < min_sf:
        min_sf = sf
        iteration = i
print(min_sf, iteration)
