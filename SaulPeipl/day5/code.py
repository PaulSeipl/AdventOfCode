from .input import lines as rawlines
from helper import convertInputToList
from copy import deepcopy
import re

linesListRaw = convertInputToList(rawlines)


def firstResult():
    lines = parseLinesList(linesListRaw)
    coor = createCoor(1000, 1000)
    print(coor)
    return countCoor(insertLines(coor, lines))


def secondResult():
    return


def countCoor(coor):
    return len([x for x in flatten(coor) if x > 1])


def flatten(t):
    return [item for sublist in t for item in sublist]


def insertLines(coor, lines):
    copyCoor = deepcopy(coor)
    for line in lines:
        if not horizontalChecker(line) and not verticalChecker(line):
            print("con")
            continue
        points = getPoints(line)
        print(points)
        for x, y in points:
            copyCoor[y][x] += 1
    print(copyCoor)
    return copyCoor


def getPoints(line):
    point1, point2 = deepcopy(line)
    points = [deepcopy(point1)]
    x1, y1 = point1
    x2, y2 = point2
    if verticalChecker(line):
        while y1 != y2:
            if y1 < y2:
                y1 += 1
            else:
                y1 -= 1
            points.append((x1, y1))

    if horizontalChecker(line):
        while x1 != x2:
            if x1 < x2:
                x1 += 1
            else:
                x1 -= 1
            points.append((x1, y1))

    return points


def verticalChecker(line):
    point1, point2 = line
    return point1[0] == point2[0]


def horizontalChecker(line):
    point1, point2 = line
    return point1[1] == point2[1]


def createCoor(xSize, ySize):
    return [[0 for x in range(xSize)] for y in range(ySize)]


def parseLinesList(linesListRaw):
    return [
        [(int(x1), int(y1)), (int(x2), int(y2))]
        for x1, y1, x2, y2 in [re.split(",| -> ", lineStr) for lineStr in linesListRaw]
    ]
