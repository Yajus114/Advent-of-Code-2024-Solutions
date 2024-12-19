with open("input.txt", "r") as file:
    towels, recipe = file.read().split("\n\n")

towels = towels.split(", ")
recipe = recipe.split()
cache = {}


def solver(dish):
    if dish == "":
        return 1
    if dish in cache:
        return cache[dish]

    count = 0
    for elem in towels:
        if dish.startswith(elem):
            count += solver(dish[len(elem) :])

    cache[dish] = count
    return count


answer = 0
for dish in recipe:
    answer += solver(dish)

print(answer)
