def rounding_numbers(nums):
    rounded = list(map(lambda num: round(num), nums))
    return rounded

nums = list(map(lambda num: float(num), input().split()))
print(rounding_numbers(nums))