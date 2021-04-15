from functools import reduce


def multiply(*args):
    result = reduce(lambda a, b: a * b, args)

    return result
