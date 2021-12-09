from lanternFish import *


NEW_FISH = 8
RESET = 6
LOWER_LIMIT = 0
# MAX_DAYS = 256
# MAX_DAYS = 18
MAX_DAYS = 80
# MAX_DAYS = 2


def updateFish(fish):
    if type(fish) == int:
        if fish > 0:
            fish = fish - 1
        else:
            fish = [RESET, NEW_FISH]
        return fish
    else:
        population = fish
        for i, fish in enumerate(population):
            population[i] = updateFish(fish)
        return population


def generatePopulation(population):
    day = 0
    while day < MAX_DAYS:
        for i, fish in enumerate(population):
            population[i] = updateFish(fish)
        day += 1

    return population


def countFish(population):
    numberFish = 0
    for i, fish in enumerate(population):
        if type(fish) == int:
            numberFish += 1
        else:
            numberFish += countFish(fish)
    return numberFish


print("number fish", countFish(generatePopulation(fishPopulation)))
