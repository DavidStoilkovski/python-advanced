def positive_vs_negative(nums):
    positive = sum(filter(lambda x: x > 0, nums))
    negative = sum(filter(lambda x: x < 0, nums))
    print(negative)
    print(positive)
    if positive > abs(negative):
        print(f'The positives are stronger than the negatives')
    elif positive < abs(negative):
        print(f'The negatives are stronger than the positives')


nums = list(map(lambda x: int(x), input().split()))
positive_vs_negative(nums)