from .input import fish as rawFish
import numpy as np

fish = np.array(rawFish)


def firstResult():
    population = initial_population(rawFish)
    return sum(grow_population(population, 256))


def secondResult():
    return


def live(fish, days):
    for _ in range(days):
        fish = decrementFish(fish)
        fish = addFish(fish)
    return fish


def decrementFish(fish):
    fish -= 1
    return fish


def addFish(fish):
    eightAnd0 = np.where(fish == -1, 8, False)
    boolArr = eightAnd0 == 8
    fishNew = eightAnd0[boolArr]
    fishOld = np.where(fish == -1, 6, fish)
    return np.concatenate([fishOld, fishNew])


def initial_population(input):
    population = [0] * 9
    for fish_age in input:
        population[fish_age] += 1

    return population


def grow_population(initial, days_to_grow):

    current = list(initial)

    if days_to_grow == 0:
        return current

    for day in range(0, days_to_grow):
        due_index = day % 9
        due_count = current[due_index]

        current[(day + 7) % 9] += due_count
        current[(day + 9) % 9] += due_count
        current[due_index] = max(0, current[due_index] - due_count)

    return current