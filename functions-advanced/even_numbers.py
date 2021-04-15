def even_numbers(numbers):
    filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return filtered_numbers


numbers = map(lambda x: int(x), input().split())

print(even_numbers(numbers))