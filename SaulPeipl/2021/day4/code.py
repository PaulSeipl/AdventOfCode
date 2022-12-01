from .input import bingoBoardsRaw, drawNumbers
from copy import deepcopy


def firstResult():
    return playBingo(bingoBoardsRaw, drawNumbers)


def secondResult():
    return loseBingo(bingoBoardsRaw, drawNumbers)


def playBingo(bingoBoardsRaw, drawNumbers):
    bingoLists = createBingoLists(bingoBoardsRaw)
    winnerBoard = 0
    lastCalledNumber = 0
    for number in drawNumbers:
        lastCalledNumber = number
        # mark
        bingoLists = markLists(bingoLists, number)
        # check
        checkList = checkBingoLists(bingoLists)
        if any(checkList):
            winnerBoard = checkList.index(True)
            break

    return calculateBoard(bingoLists[winnerBoard], lastCalledNumber)


def loseBingo(bingoBoardsRaw, drawNumbers):
    bingoLists = createBingoLists(bingoBoardsRaw)
    checkListHistory = []
    loserBoard = 0
    lastCalledNumber = 0
    for number in drawNumbers:
        lastCalledNumber = number
        # mark
        bingoLists = markLists(bingoLists, number)
        # check
        checkList = checkBingoLists(bingoLists)
        if all(checkList):
            loserBoard = checkListHistory.pop().index(False)
            break

        checkListHistory.append(checkList)

    return calculateBoard(bingoLists[loserBoard], lastCalledNumber)


def calculateBoard(bingoList, lastCalledNumber):
    return (
        sum([int(number) for number in bingoList if number.isdigit()])
        * lastCalledNumber
    )


def markLists(bingoLists, number):
    return list(map(markList, bingoLists, [number] * len(bingoLists)))


def markList(bingoList, number):
    return [
        "X" if bingoNumber == str(number) else bingoNumber for bingoNumber in bingoList
    ]


def checkBingoLists(bingoLists):
    return list(map(checkBingoList, bingoLists))


def checkBingoList(bingoList):
    return checkColumns(bingoList) or checkRows(bingoList)


def checkRows(bingoList):
    markCount = 0
    for index in range(5):
        markCount = bingoList[index::5].count("X")
        if markCount == 5:
            break
    return markCount == 5


def checkColumns(bingoList):
    markCount = 0
    for index in range(0, 24, 5):
        markCount = bingoList[index : index + 5].count("X")
        if markCount == 5:
            break
    return markCount == 5


def createBingoLists(bingoBoardsRaw):
    bingoBoardsSplit = bingoBoardsRaw.split("\n\n")
    bingoBoards = []
    for bingoBoardSplit in bingoBoardsSplit:
        bingoBoards.append(
            [
                f"{first}{second}".strip()
                for first, second in zip(bingoBoardSplit[::3], bingoBoardSplit[1::3])
            ]
        )
    return bingoBoards