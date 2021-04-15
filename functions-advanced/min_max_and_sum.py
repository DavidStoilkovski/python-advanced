def print_max_min_sum(nums):
    print(f'The minimum number is {min(nums)}')
    print(f'The maximum number is {max(nums)}')
    print(f'The sum number is: {sum(nums)}')


nums = list(map(lambda x: int(x), input().split()))

print_max_min_sum(nums)