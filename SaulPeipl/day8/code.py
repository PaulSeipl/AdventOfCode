from enum import unique
from .input import input as rawInput
from helper import flatten


def parseInput(rawInput):
    return [strings.split("|") for strings in rawInput.splitlines()]


def firstResult():
    input = parseInput(rawInput)
    fourDigits = getFourDigits(input)
    return len(getAllUniques(fourDigits))


def secondResult():
    input = parseInput(rawInput)
    allDigits = getAllDigits(input)
    print("all digits:\n", allDigits)
    return findPatterns(allDigits[0])


def findPatterns(oneExample):
    uniques = getUniques(oneExample)
    print("uniques:\n", uniques)
    patternsDict = {}
    patternsDict[get1Pattern(uniques)] = 1
    patternsDict[get7Pattern(uniques)] = 7
    print("patternsDict: ", patternsDict)
    return ""


def get1Pattern(uniques):
    return min(uniques, key=len)


def get7Pattern(uniques):
    return [unique for unique in uniques if len(unique) == 3]


def getAllDigits(input):
    return [
        (tenDigits + fourDigits.strip()).split(" ") for tenDigits, fourDigits in input
    ]


def getFourDigits(input):
    return [fourDigitList.strip().split(" ") for _, fourDigitList in input]


def getAllUniques(digits):
    return [digit for digit in flatten(digits) if len(digit) in (2, 3, 4, 7)]


def getUniques(digits):
    return set(
        ["".join(sorted(digit)) for digit in digits if len(digit) in (2, 3, 4, 7)]
    )
