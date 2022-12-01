from .input import rawInput
from helper import convertInputToList

INPUT = convertInputToList(rawInput)


def firstResult():
    return withForLoop(INPUT)


def secondResult():
    return calculateLifeSupportRating(INPUT)


def withForLoop(input):
    gamma = ""
    epsilon = ""
    for index in range(len(input[0])):
        indexList = getListOfIndex(input, index)
        commonBit = getCommonBit(indexList)
        gamma += commonBit
        epsilon += negateBit(commonBit)
    return int(gamma, 2) * int(epsilon, 2)


def calculateLifeSupportRating(input):
    return calculateOxygenRating(input) * calculateCO2Rating(input)


def calculateOxygenRating(input):
    copyInput = input.copy()
    for index in range(len(copyInput[0])):
        commonBit = getCommonBit(getListOfIndex(copyInput, index))
        copyInput = equalIndexBitList(copyInput, index, commonBit)
        if len(copyInput) == 1:
            break

    return int(copyInput[0], 2)


def calculateCO2Rating(input):
    copyInput = input.copy()
    for index in range(len(copyInput[0])):
        commonBit = getUncommonBit(getListOfIndex(copyInput, index))
        copyInput = equalIndexBitList(copyInput, index, commonBit)
        if len(copyInput) == 1:
            break

    return int(copyInput[0], 2)


def equalIndexBitList(input, index, bit):
    return [bits for bits in input if bits[index] == bit]


def getCommonBit(indexList):
    return toIntToString(indexList.count("1") >= indexList.count("0"))


def getUncommonBit(indexList):
    return toIntToString(indexList.count("1") < indexList.count("0"))


def toIntToString(string):
    return str(int(string))


def negateBit(bit):
    return toIntToString(not int(bit))


def getListOfIndex(input, index):
    return list(map(lambda string: string[index], input))
