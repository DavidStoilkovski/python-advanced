from functools import reduce


def operate(*args):
    operators = {
        "+": reduce(lambda x, y: x + y, args[1:]),
        "-": reduce(lambda x, y: x - y, args[1:]),
        "*": reduce(lambda x, y: x * y, args[1:]),
        "/": reduce(lambda x, y: x / y, args[1:])
    }

    operator = args[0]
    return operators[operator]