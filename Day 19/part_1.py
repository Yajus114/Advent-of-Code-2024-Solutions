with open("input.txt", "r") as file:
    towels, recipe = file.read().split("\n\n")
# classic Tower of Hanoi problem, use DP and/or cache
towels = towels.split(", ")
recipe = recipe.split()
cache = set()


def solver(dish):
    if dish == "" or dish in cache:
        return 1
    for elem in towels:
        if dish.startswith(elem):
            if solver(dish[len(elem) :]) == 1:
                cache.add(dish)
                return 1
    return 0


answer = 0
for dish in recipe:
    answer += solver(dish)

print(answer)
