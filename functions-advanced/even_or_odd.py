def even_odd(*args):
    command = args[-1]
    nums = args[:-1]

    if command == "even":
        return list(filter(lambda x: x % 2 == 0, nums))
    elif command == "odd":
        return list(filter(lambda x: x % 2 == 1, nums))