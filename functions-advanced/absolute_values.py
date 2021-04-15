def conver_to_absoulute(nums):
    converted = list(map(lambda num: abs(num), nums))

    return converted


nums = list(map(lambda num: float(num), input().split()))

print(conver_to_absoulute(nums))