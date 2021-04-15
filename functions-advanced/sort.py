def sort_numbers(nums):
    sorted_numbers = list(sorted(nums))
    return sorted_numbers


nums = map(lambda x: int(x), input().split())

print(sort_numbers(nums))
