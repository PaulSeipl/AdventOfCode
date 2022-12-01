from .input import rawInput
from helper import convertInputToList

INPUT = convertInputToList(rawInput)


def firstResult():
    return withForLoop(INPUT)


def secondResult():
    return againWithForLoop(INPUT)


def withForLoop(input):
    horizontal = 0
    depth = 0
    for command, unit in splitInput(input):
        if command.startswith("f"):
            horizontal += unit
        if command.startswith("d"):
            depth += unit
        if command.startswith("u"):
            depth -= unit
    return horizontal * depth


def againWithForLoop(input):
    aim = 0
    horizontal = 0
    depth = 0
    for command, unit in splitInput(input):
        if command.startswith("f"):
            horizontal += unit
            depth += aim * unit
        if command.startswith("d"):
            aim += unit
        if command.startswith("u"):
            aim -= unit
    return horizontal * depth


def splitInput(input):
    return list(map(lambda data: (data.split(" ")[0], int(data.split(" ")[1])), input))
