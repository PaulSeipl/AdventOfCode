from .input import crabs


def firstResult():
    counts = getCounts(crabs)
    min = 0
    minPos = 0
    for index, pos in enumerate(crabs):
        if index == 0:
            min = calculateFuel(counts, pos)
        else:
            temp = calculateFuel(counts, pos)
            if temp < min:
                min = temp
                minPos = pos
    return min


def secondResult():
    counts = getCounts(crabs)
    myMin = 0
    minPos = 0
    for index, pos in enumerate(range(max(crabs) + 1)):
        if index == 0:
            myMin = calculateNewFuel(counts, pos)
        else:
            temp = calculateNewFuel(counts, pos)
            if temp < myMin:
                myMin = temp
                minPos = pos
    print(minPos)
    return myMin


def calculateFuel(counts, pos):
    return sum([abs(value - pos) * count for value, count in counts])


def calculateNewFuel(counts, pos):
    return sum([sum(range((abs(value - pos)) + 1)) * count for value, count in counts])


def getAverage(list):
    return round(sum(list) / len(list))


def getCounts(myList):
    return list(set([(value, myList.count(value)) for value in myList]))
