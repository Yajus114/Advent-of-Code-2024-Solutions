import re


with open("input.txt", "r") as file:
    mul_enabled: bool = True
    res: int = 0
    a: str = ""
    for item in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", file.read()):
        if item.startswith("m") and mul_enabled:
            c, d = map(int, item.replace("mul(", "").replace(")", "").split(","))
            res += c * d
        elif item == "don't()":
            mul_enabled = False
        elif item == "do()":
            mul_enabled = True
    print(res)
