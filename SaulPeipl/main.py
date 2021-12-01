from functools import reduce
from day1_input import rawInput


def main():
    # first test
    input = convertInputToList(rawInput)
    res = withReduce(input)
    print(res)
    # second test
    addedList = addTheNextTwo(input)
    print(withReduce(addedList))


def addTheNextTwo(input):
    addedList = []
    for x, y, z in zip(input, input[1:], input[2:]):
        addedList.append(x + y + z)
    return addedList


def withReduce(input):
    result = reduce(
        lambda acc, depth: (acc[0] + 1, depth) if depth > acc[1] else (acc[0], depth),
        input,
        (0, input[0]),
    )
    return result[0]


def withForLoop(input):
    res = 0
    prevDepth = input[0]
    for depth in input:
        if depth > prevDepth:
            res += 1
        prevDepth = depth

    return res


def convertInputToList(input: str):
    return list(map(int, input.split("\n")))


if __name__ == "__main__":
    main()