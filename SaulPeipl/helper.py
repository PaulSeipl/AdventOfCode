def convertInputToIntList(input: str):
    return list(map(int, input.split("\n")))


def convertInputToList(input: str):
    return input.splitlines()


def flatten(t):
    return [item for sublist in t for item in sublist]