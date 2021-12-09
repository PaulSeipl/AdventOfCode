from bingoSequence import *


def isCompletelyMarked(inputRow):
    for i, entry in enumerate(inputRow):
        if type(entry) == int:
            print("input is not marked", inputRow)
            return False
    print("input bingo", inputRow)
    return True


def calculateBoardSum(board):
    boardSum = 0
    for row in board:
        for entry in row:
            if type(entry) == int:
                # print("boardSum: {boardSum} before {entry} is added.".format(boardSum=boardSum, entry=entry))
                boardSum += entry
    return boardSum


def markEntry(board, row, column):
    entry = board[row][column]
    board[row][column] = [entry, "marked"]
    return board


def markBoard(board, draw):
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == draw:
                board = markEntry(board, i, j)
    return board


def checkBingo(board):
    for i, row in enumerate(board):
        if isCompletelyMarked(row):
            return True
    j = 0
    while j < len(board):
        column = []
        for i, row in enumerate(board):
            column.append(board[i][j])
        if isCompletelyMarked(column):
            return True
        j += 1
    return False


def playBingo(boards, drawingSequence):
    winningCombos = []
    for i, draw in enumerate(drawingSequence):
        for j, board in enumerate(boards):
            markBoard(board, draw)
            bingo = checkBingo(board)
            if bingo:
                winningCombos.append([draw, board])
                boards.remove(board)
    return winningCombos


def calculateFinalScore(draw, board):
    return draw * calculateBoardSum(board)


def firstWinningBoard(boards, sequence):
    firstWinningCombo = playBingo(boards, sequence)[0]
    return calculateFinalScore(firstWinningCombo[0], firstWinningCombo[1])


print(firstWinningBoard(bingoBoards, bingoSequence))
