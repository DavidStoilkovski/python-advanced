def concatenate(*args):
    result = list(map(lambda el: el, args))

    return ''.join(result)